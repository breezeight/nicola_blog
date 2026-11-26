# How-to: Pull images in K8S clusters from Amazon ECR

This howto covers some common scenarios for pulling images from docker registries in K8S clusters.  
Choose the section that matches where your Kubernetes cluster runs.

At the moment of writing, this document is valid for K8S clusters that:

* Scenario 1: running on AWS EKS that connect to ECR
* Scenario 2: running outside AWS that connect to ECR

This howto can be extended to other cloud providers and registries.

## Scenario 1 — Pulling from ECR **inside an EKS cluster**

TL;DR: EKS nodes are already integrated with AWS IAM. Prefer IAM-based access over Secrets.


### Option 1A: Use node IAM role (no `imagePullSecrets`) — recommended

EKS worker nodes (or Fargate execution roles) authenticate to ECR using their IAM role.

#### Step 1: Grant ECR pull permissions to the node role

Minimum required permissions:
- `ecr:GetAuthorizationToken`
- `ecr:BatchCheckLayerAvailability`
- `ecr:GetDownloadUrlForLayer`
- `ecr:BatchGetImage`

> [!NOTE]
> Image pulls are performed by the **node**, not the Pod.
> IRSA (IAM Roles for Service Accounts) is not required just to pull images.
> IRSA allows Pods to assume IAM roles for AWS API access (e.g., S3, DynamoDB), but for ECR image pulls, the node's IAM role is sufficient.

---

#### Step 2: Reference the image normally

```yaml
spec:
  containers:
    - name: app
      image: <account>.dkr.ecr.<region>.amazonaws.com/app@sha256:...
```

> [!NOTE]
> No `imagePullSecrets` are needed. Authentication is implicit via the node role.

## Scenario 2 — Pulling from ECR from a Kubernetes cluster **outside AWS**

### HOWTO: choose an approach
ECR authentication must be handled explicitly.

Before picking an option, decide where AWS credentials should live and how much operational and security risk you can accept.

**Key considerations**
- **Can you change node / kubelet configuration?**
  - Yes → Option C is usually the cleanest.
  - No → Option B is usually the safest.
- **Can you avoid long-lived credentials in the cluster?**
  - Yes → Option B or C.
  - No → Option A or Option D (temporary only).
- **Is this production?**
  - Yes → Avoid Option D entirely.
  - No / short-lived → Option D may be acceptable.

**Summary:**

| Option | Credentials        | Automation | Production |
| ------ | ------------------ | ---------- | ---------- |
| A      | IAM keys in Secret | Required   | ⚠️         |
| B      | OIDC / STS         | Yes        | ✅          |
| C      | Node-level         | Yes        | ✅          |
| D      | ECR token only     | No         | ❌          |

> [!NOTE]
> **Rule of thumb**
> If Option D looks attractive in production, stop and implement Option B or C instead.

### Option A: Static IAM keys in a Kubernetes Secret + refresh `imagePullSecret` (fallback)

This option stores long-lived AWS credentials in Kubernetes and uses them to mint ECR registry credentials.

#### Step 1: Create an IAM principal with least privilege
Grant only ECR pull permissions:
- `ecr:GetAuthorizationToken`
- `ecr:BatchCheckLayerAvailability`
- `ecr:GetDownloadUrlForLayer`
- `ecr:BatchGetImage`

> [!NOTE]
> Use a dedicated IAM principal for image pulling only.

---

#### Step 2: Store IAM keys as a Kubernetes Secret
```bash
kubectl -n <ns> create secret generic aws-iam-ecr \
  --from-literal=AWS_ACCESS_KEY_ID='<access_key_id>' \
  --from-literal=AWS_SECRET_ACCESS_KEY='<secret_access_key>'
```

> [!NOTE]
> Protect this Secret carefully using RBAC and etcd encryption.

---

#### Step 3: Create or update the `docker-registry` Secret

```bash
export AWS_ACCESS_KEY_ID='<access_key_id>'
export AWS_SECRET_ACCESS_KEY='<secret_access_key>'

kubectl -n <ns> create secret docker-registry ecr-pull \
  --docker-server=<account>.dkr.ecr.eu-west-1.amazonaws.com \
  --docker-username=AWS \
  --docker-password="$(aws ecr get-login-password --region eu-west-1)" \
  --dry-run=client -o yaml | kubectl apply -f -
```

---

#### Step 4: Reference the Secret from workloads

```yaml
spec:
  imagePullSecrets:
    - name: ecr-pull
```

---

#### Step 5: Handle token expiry

Automate Step 3 using a CronJob or pipeline.

> [!NOTE]
> Without automation, new Pods will eventually fail with `ImagePullBackOff`.

---

### Option B: OIDC federation (cluster → AWS role) + refresh `imagePullSecret` (recommended)

This option uses short-lived STS credentials obtained via Kubernetes-issued OIDC tokens.

#### Step 1: Ensure the cluster exposes an OIDC issuer

Your Kubernetes API server must publish OIDC discovery metadata.

---

#### Step 2: Register the OIDC provider in AWS IAM

Create an IAM OIDC identity provider pointing to the cluster issuer.

---

#### Step 3: Create an IAM role with a ServiceAccount-bound trust policy

Restrict the trust policy to:

* one namespace
* one ServiceAccount

Attach minimal ECR pull permissions.

> [!NOTE]
> The trust policy is the primary security boundary.

---

#### Step 4: Create a ServiceAccount for credential refresh

Bind the ServiceAccount to the IAM role using your platform’s OIDC wiring.

---

#### Step 5: Refresh the image pull Secret on a schedule

```bash
kubectl -n <ns> create secret docker-registry ecr-pull \
  --docker-server=<account>.dkr.ecr.eu-west-1.amazonaws.com \
  --docker-username=AWS \
  --docker-password="$(aws ecr get-login-password --region eu-west-1)" \
  --dry-run=client -o yaml | kubectl apply -f -
```

> [!NOTE]
> Updating the Secret does not restart running Pods.

---

#### Step 6: Reference the Secret from workloads

```yaml
spec:
  imagePullSecrets:
    - name: ecr-pull
```

---

### Option C: Kubelet ECR credential provider (node-level, no Secrets)

This option moves ECR authentication entirely to kubelet.

#### Step 1: Confirm node and kubelet access

You must be able to install binaries and restart kubelet safely.

---

#### Step 2: Install the ECR credential provider plugin

Install the plugin binary on every node in a known directory.

---

#### Step 3: Create the kubelet credential provider config

Configure registry matching rules for:

* `*.dkr.ecr.<region>.amazonaws.com`

---

#### Step 4: Configure kubelet to use the provider

Set kubelet flags or config:

* `--image-credential-provider-bin-dir`
* `--image-credential-provider-config`

Restart kubelet.

---

#### Step 5: Provide AWS auth to the node

Choose one:

* node-level IAM (if on AWS)
* node-level OIDC
* node-level IAM keys (last resort)

---

#### Step 6: Deploy workloads without `imagePullSecrets`

```yaml
spec:
  containers:
    - name: app
      image: <account>.dkr.ecr.<region>.amazonaws.com/app@sha256:...
```

---

### ⚠️ Option D: Static `docker-registry` Secret (simple, fragile, temporary only)

This option relies on a single ECR auth token with no refresh mechanism.

> [!WARNING]
> This approach is **not production-ready**.
> Use only for testing, demos, or very short-lived environments.

---

#### Step 1: Create the image pull Secret

Using IAM access keys to authenticate:

```bash
export AWS_ACCESS_KEY_ID='<access_key_id>'
export AWS_SECRET_ACCESS_KEY='<secret_access_key>'

kubectl create secret docker-registry ecr-pull \
  --docker-server=<account>.dkr.ecr.eu-west-1.amazonaws.com \
  --docker-username=AWS \
  --docker-password="$(aws ecr get-login-password --region eu-west-1)" \
  --namespace <ns>
```

> [!NOTE]
> `kubectl create secret docker-registry` has no stdin option, so the password is passed with `--docker-password`. The value comes from `aws ecr get-login-password` (a short-lived ECR authentication token) via command substitution `$(...)`, so you never type or store the password yourself.

> [!WARNING]
> The Secret object persists, but the ECR token expires.
> When it expires, new Pods will fail with `ImagePullBackOff`.
> 
> **Security:** Never commit IAM keys to version control. Use environment variables or a secrets manager.

---

#### Step 2: Reference the Secret

```yaml
spec:
  imagePullSecrets:
    - name: ecr-pull
```

---
