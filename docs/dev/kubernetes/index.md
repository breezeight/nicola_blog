## HOWTOS


### Kubernetes Context Management

- [manage different kubernetes credentials and kubeconfig files](manage-different-kubernetes-credentials-and-kubeconfig-files.md)

## What is Kubernetes?

Think of **orchestration** like a conductor leading an orchestra: each musician (a container) can play alone, but the conductor coordinates who plays, when, and how loud, so the whole thing works together. Kubernetes is that conductor for containers that run on your servers.

A **container** packages an app with everything it needs to run. When you have many containers across many servers, managing them by hand is painful. Kubernetes automates that coordination.

Main characteristics:

- **Automatic scheduling** — decides which server (node) runs each container based on available resources.
- **Self-healing** — if a container crashes, it restarts or replaces it automatically.
- **Scaling** — adds or removes container copies based on demand (e.g. more traffic → more copies).
- **Load balancing** — spreads incoming traffic across containers so none gets overwhelmed.
- **Rolling updates & rollbacks** — updates your app gradually with no downtime, and reverts if something breaks.
- **Declarative config** — you describe the desired state ("I want 5 copies running"), and Kubernetes works to maintain it.

The mental model: you tell Kubernetes *what* you want, and it continuously works to keep reality matching that, without you babysitting individual containers.

Sources:
- [Kubernetes official overview](https://kubernetes.io/docs/concepts/overview/)
- [What is Kubernetes? (Google Cloud)](https://cloud.google.com/learn/what-is-kubernetes)

Here's an expanded version that stays digestible — I added a sentence of context per part and the key components, without dumping every detail:


Here it is without the table — the node-vs-node distinction is carried by the two opening bullets, and the component sections stay honestly labeled so they're never confused with the nodes themselves:

## Kubernetes Architecture

At a very high level, Kubernetes is a cluster of machines (called **nodes**) that come in two roles:

- **Control plane node** — the "brain." Its job is to decide *what* should happen: scheduling containers, detecting failures, and keeping the cluster in its desired state. A cluster has one or more.
- **Worker node** — the "muscle." Its job is to *do* the work: running your actual application containers. A cluster has one or more (optional, but recommended).

The difference is purely about **what job each node does**. Every node — regardless of role — runs the same base agents (kubelet, container runtime, kube-proxy) that make it a node. A control plane node is simply a node that *additionally* runs the control plane components on top.

See the diagram below for a visual representation of the Kubernetes architecture: [Kubernetes Architecture](https://kubernetes.io/docs/concepts/architecture/)

### What runs on a control plane node

The components that make the global decisions:

- **API server** — the front door to the cluster; everything communicates through it.
- **Scheduler** — decides which worker node a new container should run on.
- **Controller manager** — watches the cluster and fixes any drift from the desired state (e.g. restarting a crashed container).
- **etcd** — the cluster's database, storing all configuration and state.
- etc...

### What runs on every node

The base agents present on both control plane and worker nodes:

- **kubelet** — ensures the containers it's told to run are healthy.
- **Container runtime** — the software that actually runs containers (e.g. containerd).
- **kube-proxy** — handles networking, routing traffic to the right containers.

The single takeaway: **the control plane decides what should happen, the worker nodes make it happen — and a control plane node is just a node with extra responsibilities.**

Sources:
- [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)
- [Cluster Architecture](https://kubernetes.io/docs/concepts/architecture/)


### Control Plane Node Components: The API Server

The **API server** (`kube-apiserver`) is the central hub of the control plane — every interaction goes through it.

What it does:

- **Single entry point** — `kubectl`, the other control plane components, and the kubelets on every node all talk to the cluster *only* through the API server. Nothing talks to etcd directly.
- **Validates & processes requests** — when you submit a change (e.g. "run 5 copies of this app"), it authenticates you, checks permissions (authz), validates the request, then persists the new desired state to etcd.
- **The only component that reads/writes etcd** — it's the gatekeeper to the cluster's database, which keeps state access consistent and secure.
- **Exposes the REST API** — everything in Kubernetes is an object (pods, services, deployments) accessed via a RESTful HTTP API that the API server serves.

The mental model: it's the **front door and switchboard** — all roads in and out of the cluster pass through it, which is why it's the one component nothing else can bypass.

Sources:
- [kube-apiserver](https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver)
- [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)

### Control Plane Node Components: Scheduler

The **scheduler** (`kube-scheduler`) decides *which node* each new container (pod) should run on. It only places pods — it doesn't run them; the kubelet on the chosen node does that.

It picks a node in two phases:

- **Filtering** — drops nodes that *can't* run the pod (not enough resources, or constraints like affinity/taints not met).
- **Scoring** — ranks the remaining nodes to find the *best* fit; the highest score wins.

It then records the decision through the API server, and the kubelet on the chosen node actually starts the pod.

The mental model: the scheduler is the **seating host at a restaurant** — it finds free, suitable tables (filtering), picks the best one (scoring), and seats you — but it doesn't cook or serve the food.

Sources:
- [kube-scheduler](https://kubernetes.io/docs/concepts/overview/components/#kube-scheduler)
- [Kubernetes Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)


### Control Plane Node Components: Controller managers

A **controller** is a watch-loop process: it continuously compares the cluster's **desired state** (from objects' configuration) against its **current state** (read from etcd via the API server), and takes corrective action whenever the two don't match — until reality matches intent.

There are **few controller managers but many controllers**: each manager is a single binary that bundles and runs a whole collection of individual controllers.

- **kube-controller-manager** — runs the built-in controllers that regulate the cluster's *own* state: acting when nodes become unavailable, ensuring pod counts are as expected, and creating endpoints, service accounts, and API access tokens.
- **cloud-controller-manager** — runs the controllers that interact with the underlying **cloud provider**: handling nodes that become unavailable at the infrastructure level, managing storage volumes, and configuring load balancing and routing. It only exists when running on a cloud provider.

The split keeps cloud-specific logic isolated, so the core Kubernetes controllers stay provider-agnostic and the cluster runs identically across clouds or bare metal.

The mental model: a controller is a **thermostat** — you set the target, and it keeps nudging reality back toward it whenever it drifts.

Sources:
- [kube-controller-manager](https://kubernetes.io/docs/concepts/overview/components/#kube-controller-manager)
- [cloud-controller-manager](https://kubernetes.io/docs/concepts/architecture/cloud-controller/)
- [Controllers](https://kubernetes.io/docs/concepts/architecture/controller/)


### Control Plane Node Components: etcd - Key-Value Data Store

**etcd** is the cluster's internal key-value store — it holds the entire cluster state and is the **source of truth**. Only the API server talks to it.

The mental model: etcd is the cluster's **memory** — lose it, and the cluster forgets everything.

### Worker Node Overview

A **worker node** is where your client applications actually run. These apps are typically microservices packaged as **containers**, which Kubernetes wraps in **Pods**.

A **Pod** is Kubernetes' smallest scheduling unit: a logical group of one or more containers that are scheduled, started, stopped, and moved together as a single unit. The control plane decides *where* Pods go; the worker node provides the compute, memory, storage, and networking they need to run.

User traffic to your applications flows **directly to the worker nodes** — it does not pass through the control plane.

The mental model: worker nodes are the **shop floor** — the control plane plans the work, but the actual product gets made here.

A worker node has the following components:

- Container Runtime (containerd, CRI-O, etc.)
- Node Agent - kubelet
- Proxy - kube-proxy
- Add-ons for DNS, observability components such as dashboards, cluster-level monitoring and logging, and device plugins.

### Worker Node Components: Node Agent - kubelet

The **kubelet** is an agent running on **every** node (control plane and workers) that communicates with the control plane. It receives Pod definitions — primarily from the API server — and tells the **container runtime** on its node to run the containers, talking to it through a standard interface (the **CRI**). The runtime first **pulls** the required **container images** (read-only app snapshots) from a registry, then starts the containers. The kubelet continuously **reports node and Pod status back** to the API server, and manages only the containers Kubernetes created — not any others on the node.

The mental model: the kubelet is the **on-site foreman** — it takes orders from the control plane, makes sure the containers on its node get built and stay healthy, and reports back on how things are going.

### Worker Node Components: Proxy - kube-proxy

The kube-proxy is the network agent which runs on each node, control plane and workers, responsible for dynamic updates and maintenance of all networking rules on the node. It abstracts the details of Pods networking and forwards connection requests to the containers in the Pods. 

The kube-proxy is responsible for TCP, UDP, and SCTP stream forwarding or random forwarding across a set of Pod backends of an application, and it implements forwarding rules defined by users through Service API objects.

The kube-proxy node agent operates in conjunction with the iptables of the node. Iptables is a firewall utility created for the Linux OS that can be managed by users through a CLI utility of the same name. The iptables utility is available for and pre-installed on many Linux distributions.

### Worker Node Components: Add-ons

Add-ons are cluster features and functionality not yet available in Kubernetes, therefore implemented through 3rd-party pods and services.

- DNS: Cluster DNS is a DNS server required to assign DNS records to Kubernetes objects and resources.
- Dashboard: A general purpose web-based user interface for cluster management.
- Monitoring: Collects cluster-level container metrics and saves them to a central data store.
- Logging: Collects cluster-level container logs and saves them to a central log store for analysis.
- Device plugins: For system hardware resources, such as GPU, FPGA, high-performance NIC, to be advertised by the node to application pods.

### Networking

Networking, in general, is not the easiest to understand and implement. Kubernetes is no exception - as a containerized microservices orchestrator it needs to address a few distinct networking challenges:

- Container-to-Container communication inside Pods
- Pod-to-Pod communication on the same node and across cluster nodes
- Service-to-Pod communication within the same namespace and across cluster namespaces
- External-to-Service communication for clients to access applications in a cluster

All these networking challenges must be addressed by a Kubernetes cluster and its plugins.

#### Container-to-Container communication inside Pods

Containers in a Pod need to talk to each other directly, as if on the same machine. Kubernetes makes this possible by having all containers in a Pod **share a single network namespace** (a Linux kernel feature that isolates networking).

Because they share that namespace, the containers can communicate over **localhost**, while the outside world is walled off.

#### Pod-to-Pod communication on the same node and across cluster nodes

In a Kubernetes cluster Pods, groups of containers, are scheduled on nodes in a nearly unpredictable fashion. Regardless of their host node, Pods are expected to be able to communicate with all other Pods in the cluster, all this without the implementation of Network Address Translation (NAT). This is a fundamental requirement of any networking implementation in Kubernetes.

The Kubernetes network model aims to reduce complexity, and it treats Pods as VMs on a network, where each VM is equipped with a network interface - thus each Pod receiving a unique IP address. This model is called **IP-per-Pod** and ensures Pod-to-Pod communication, just as VMs are able to communicate with each other on the same network.

There's exactly one pod IP, and every container in the pod shares it. It belongs to the shared network namespace, not to any individual container.

Practical consequences:
- From **outside** the pod, all containers are reachable at that single pod IP — distinguished only by port (e.g. `10.0.0.1:8080` → container A, `10.0.0.1:9090` → container B).
- This is why port coordination matters: two containers can't both expose `:8080` on the shared IP.
- From **inside** the pod, they reach each other over `localhost`; from outside, peers reach them via `podIP:port`.

So a container has two ways to be addressed — `localhost:port` for its pod-mates, `podIP:port` for everyone else — but it's the same single network identity underneath.

Source: [Kubernetes – Pods networking](https://kubernetes.io/docs/concepts/workloads/pods/#pod-networking)

#### External-to-Pod Communication

### External-to-Pod communication & Services

Pods are unreliable targets: they're created, destroyed, and rescheduled constantly, getting a new IP each time. So you can't expose a Pod's IP directly — you need a **stable** address.

A **Service** solves this: it's a stable front-end for a group of Pods, giving you one **fixed virtual IP + port** that automatically routes traffic to whichever healthy Pods are currently behind it. Pods can churn underneath; the Service stays put.

Under the hood, a Service is a set of routing rules ("traffic for this virtual IP → these Pods") stored as **iptables** entries on each node. The **kube-proxy** agent writes and continuously updates those rules as Pods come and go.

The mental model: a Service is the **front desk with a permanent phone number** — you always call the same number, and it routes you to whoever's currently on shift.

## Installing Kubernetes

There are a variety of installation tools allowing us to deploy single- or multi-node Kubernetes clusters on our workstations, for learning and development purposes. While not an exhaustive list, below we enumerate a few popular ones:

* [Minikube](https://minikube.sigs.k8s.io/docs/)  
  Single- and multi-node local Kubernetes cluster, recommended for a learning environment deployed on a single host.  
  * [Kind](https://kind.sigs.k8s.io/)  
    Multi-node Kubernetes cluster deployed in Docker containers acting as Kubernetes nodes, recommended for a learning environment.  
    * [Docker Desktop](https://www.docker.com/products/docker-desktop)   
      Including a local Kubernetes cluster for Docker users.   
    * [Podman Desktop](https://podman-desktop.io/)  
      Including Kubernetes integration for Podman users.  
    * [MicroK8s](https://microk8s.io/)   
      Local and cloud Kubernetes cluster for developers and production, from Canonical.  
    * [K3S](https://k3s.io/)   
      Lightweight Kubernetes cluster for local, cloud, edge, IoT deployments, originally from Rancher, currently a CNCF project.

Minikube is an easy and flexible method to create a local Kubernetes setup. We will be using it extensively in this course to manage certain aspects of a Kubernetes cluster, while taking advantage of several automated features designed to simplify the user interaction with the Kubernetes environment and the containerized applications deployed to the cluster.



## Concepts

### Objects in Kubernetes

A Kubernetes object is a "record of intent"--once you create the object, the Kubernetes system will constantly work to ensure that the object exists. By creating an object, you're effectively telling the Kubernetes system what you want your cluster's workload to look like; this is **your cluster's desired state**.

- Objects are **persistent entities** representing the **desired state** of the cluster.
- They define what should run, how it should run, and with which resources.
- Kubernetes continuously reconciles **actual state** to **desired state**.


- Every object is defined by:
  - `apiVersion`
  - `kind`
  - `metadata.name`

- Names are unique within a namespace.
- Each object has a globally unique **UID**.

##### Working with objects

###### API-driven model
- All objects are created, read, updated, and deleted via the **Kubernetes API**.
- Tools like `kubectl`, Helm, and GitOps systems interact with this API.

###### Declarative vs. imperative management
- **Imperative**: you issue specific commands that tell Kubernetes *how* to make changes (e.g., `kubectl create`, `kubectl edit`). These commands act immediately against the live cluster and perform the action you request.
- **Declarative**: you define the *desired end state* of objects in manifests and then apply them (e.g., `kubectl apply -f`). Kubernetes figures out what changes are needed to match that desired state and reconciles the actual state accordingly.
- Declarative management supports idempotency (applying the same manifest repeatedly won’t cause unintended changes) and fits well with version control and automation workflows. See the official Kubernetes docs on object management: https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/

###### Desired vs. actual state (manifests and live objects)

In a Kubernetes cluster managed declaratively, you usually start by writing a **manifest**.  
A manifest is a YAML (or JSON) file that describes *what you want* Kubernetes to run. It is the primary input to the system and is applied using tools such as `kubectl apply`, Helm, or GitOps controllers.

The manifest focuses on **intent**, not outcomes:
- `metadata` identifies the object (name, namespace, labels).
- `spec` defines the **desired state** (for example, how many replicas to run, which container image to use, which ports to expose).

Once the manifest is submitted, Kubernetes stores the object internally and begins acting on it. Controllers continuously work to make the real cluster state match what you declared in the `spec`.

As the cluster operates, Kubernetes records **what is actually happening** in a separate field called `status`. 

The `status` is:
- Computed and updated by Kubernetes components
- A reflection of current reality (running, failed, available replicas, conditions, errors)
- Not something users define in manifests

This separation enables Kubernetes’ reconciliation model: you declare intent in `spec`, and Kubernetes reports results in `status`.

- **Manifest** (what you apply):
  - Contains `metadata` and `spec`
  - Does **not** contain `status`
- **Live object in Kubernetes** (stored in the API server / etcd):
  - Contains `metadata`, `spec`, and `status`
  - `status` is system-managed and read-only for users

###### Identity and selection

Official documentation: [Names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/)

Required manifest fields to uniquely identify an object:
When defining an object in a manifest, the following fields establish its type and human-facing identity:

- `apiVersion`: Specifies the API group and version (for example, apps/v1).
- `kind`: Defines the resource type (for example, Pod, Deployment, Service).
- `metadata.name`: A human-readable identifier that must be unique per resource type within a namespace.
- `metadata.namespace` (optional): Defines the logical scope for namespaced resources (if not provided use the default or current namespace). 

> [!NOTE]
>   It is strongly recommended to use **DNS-style names** (lowercase alphanumeric characters, `-`, and `.`) to ensure compatibility and consistency across Kubernetes components.

Together, these form the typical identifier: `(apiVersion, kind, namespace, name)`

After creation, Kubernetes assigns additional identity `metadata.uid`, a cluster-generated UUID:
- Globally unique for the lifetime of the cluster.
- Never reused, even if an object with the same name and namespace is deleted and recreated.
- This is the true unique identifier used internally by the Kubernetes API.


**Metadata used for grouping and tooling**: Beyond identity, objects include metadata that supports selection and automation:

- `labels` (metadata.labels):
  - Key/value pairs used to group and select objects.
  - Not required to be unique.
  - Commonly used by Services, Deployments, and controllers.

- `annotations` (metadata.annotations):
  - Key/value metadata intended for tools and controllers.
  - Not used for selection.
  - Typically store auxiliary or tool-specific information.

###### Minimal example: manifest and observing status changes

**Example manifest (Pod):**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: demo-pod
spec:
  containers:
    - name: app
      image: nginx:1.25
```

This manifest declares only the **desired state** (`spec`). There is no `status`.

Apply the manifest:

```bash
kubectl apply -f pod.yaml
```

At this point, Kubernetes creates the object and begins working to satisfy the spec.

**Check high-level status:**

```bash
kubectl get pod demo-pod
```

Example output over time:

* `Pending` → the Pod is being scheduled
* `Running` → the container is running

This phase comes from `status.phase`.

**Inspect full spec and status:**

```bash
kubectl get pod demo-pod -o yaml
```
output:

###### Example output: `kubectl get pod demo-pod -o yaml`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: demo-pod
  namespace: default
  uid: 8b3f7d9c-1c2a-4a9e-9d7e-abc123456789
  creationTimestamp: "2026-01-04T10:15:30Z"

spec:
  containers:
    - name: app
      image: nginx:1.25
      imagePullPolicy: IfNotPresent
  restartPolicy: Always

status:
  phase: Running
  podIP: 10.244.1.15
  hostIP: 192.168.1.20
  startTime: "2026-01-04T10:15:42Z"
  conditions:
    - type: Initialized
      status: "True"
    - type: Ready
      status: "True"
    - type: ContainersReady
      status: "True"
    - type: PodScheduled
      status: "True"
  containerStatuses:
    - name: app
      ready: true
      restartCount: 0
      state:
        running:
          startedAt: "2026-01-04T10:15:45Z"
```

You will now see:
  - `spec`: exactly what you applied (desired state)
  - `status`: Kubernetes-reported state, including:
    - `phase`: high-level Pod lifecycle state (e.g. Pending, Running)
    - `podIP`: IP address assigned to the Pod
    - `hostIP`: IP address of the node running the Pod
    - `conditions`: fine-grained Pod state indicators:
      - `PodScheduled`: Pod has been assigned to a node
      - `Initialized`: init containers (if any) have completed
      - `ContainersReady`: all containers are running and ready
      - `Ready`: Pod is ready to receive traffic
    - `containerStatuses`: per-container runtime details:
      - `state`: current container state (`waiting`, `running`, `terminated`)
      - `ready`: whether the container passed its readiness probe
      - `restartCount`: number of container restarts
      - timestamps and reasons for starts, waits, or terminations


> [!NOTE]
> A **Pod can contain more than one container**.
>
> All containers in a Pod:
> - Share the same network namespace (one IP, `localhost` communication)
> - Can share storage via volumes
> - Are scheduled and managed together as a single unit
>
> **Common multi-container use cases:**
> - **Sidecar**: adds supporting functionality (logging, metrics, service mesh proxy)
> - **Adapter**: transforms or normalizes data produced by the main container
> - **Ambassador**: handles networking or proxying on behalf of the main container
>
> Use multiple containers only when they must be tightly coupled; otherwise, prefer one container per Pod.


Human-readable status and events:

```bash
kubectl describe pod demo-pod
```

This view emphasizes:
- Current conditions
- Recent events (image pull, container start, failures)

###### Key metadata

**Labels**:
- Key–value pairs for **identification and selection**.
- Used by Services, Deployments, ReplicaSets, NetworkPolicies, etc.
- Indexed and queryable.

**Annotations**:
- Key–value pairs for **non-identifying metadata**.
- Not indexed and not selectable.
- Used for tooling, configuration hints, and bookkeeping.

**Namespaces**:
- Provide **logical isolation** inside a cluster.
- Scope object names and access control.
- Commonly used for environments, teams, or applications.

###### Why objects matter
- Objects are the **foundation of Kubernetes**.
- They enable declarative infrastructure, automated reconciliation, and scalable operations.

#### Labels and Selectors

[Official documentation: Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)

`metadata.labels` are **key–value metadata** attached to Kubernetes resources.  
They are used by the Kubernetes control plane and tools to **identify, group, and select** objects.

##### What labels are used for
- **Selection** (Services → Pods, Deployments → Pods)
- **Organization & filtering** (`kubectl get … -l key=value`)
- **Driving behavior** (NetworkPolicies, RBAC, autoscaling)
- **Observability & GitOps** (Prometheus, Argo CD, cost allocation)

Labels are:
- Small, simple strings
- Non-unique
- Mutable
- Indexed by Kubernetes

##### Relation to Docker labels
- **Conceptually similar**: both are metadata
- **Technically independent**:  
  - Docker labels live on images/containers  
  - Kubernetes labels live on Kubernetes resources
- Labels do **not propagate automatically** from Docker to Kubernetes

---

##### Recommended Kubernetes label convention
Use standard labels under `app.kubernetes.io/*`:

- `app.kubernetes.io/name`
- `app.kubernetes.io/instance`
- `app.kubernetes.io/version`
- `app.kubernetes.io/component`
- `app.kubernetes.io/part-of`
- `app.kubernetes.io/managed-by`

These align well with Helm, GitOps, and observability tooling.

---

##### Labels vs Annotations
| Labels | Annotations |
|------|-------------|
| Selectable | Not selectable |
| Small, indexed | Large, free-form |
| Affect behavior | Informational only |

Rule of thumb:
- **Labels = identity & grouping**
- **Annotations = extra metadata**

---

##### Best practice
- Always label workloads consistently
- Keep labels stable and meaningful
- Use annotations for anything that is not used for selection
- Prefer standard `app.kubernetes.io/*` keys

Official documentation: [Common Labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/), sugget to apply these labels consistently to all resource objects:

| Key                          | Purpose              | Example      |
|------------------------------|----------------------|--------------|
| app.kubernetes.io/name       | App name             | mysql        |
| app.kubernetes.io/instance   | App instance ID      | mysql-abcxyz |
| app.kubernetes.io/version    | App version          | 5.7.21       |
| app.kubernetes.io/component  | Architectural role   | database     |
| app.kubernetes.io/part-of    | Parent application   | wordpress    |
| app.kubernetes.io/managed-by | Managing tool        | Helm         |



#### Namespaces

Official documentation: [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)

- Namespaces provide a **mechanism to group and isolate resources** within a single Kubernetes cluster.
- They are intended for **multiple users, teams, or projects**, not for strong security isolation.
- **Resource names are scoped to a namespace**; the same name can exist in different namespaces.
- Some resources are **namespaced** (Pods, Services, Deployments), others are **cluster-scoped** (Nodes, PersistentVolumes, Namespaces itself).
- Namespaces enable **resource quotas**, **limits**, and **RBAC access control** per namespace.
- Namespace context can be set per request or via client configuration (e.g., `kubectl`).


Kubernetes creates initial namespaces:
  - `default` – used when no namespace is specified
  - `kube-system` – system components
  - `kube-public` – publicly readable
  - `kube-node-lease` – node heartbeat leases

Namespaces are not recommended for **small clusters or single-user setups**.

#### Annotations

**TL;DR** : Annotations attach **informational, non-behavioral metadata** to Kubernetes objects.

**Purpose**
- Store metadata that must not affect selection or controller behavior
- Support tooling, automation, and human context

**Characteristics**
- Key–value pairs in object metadata
- Not indexed and not selectable
- Can contain large or structured values

**Typical uses**
- Tool and operator-specific data
- Git SHAs, timestamps, checksums
- Generated configuration or links

**Rule**
If changing the value should be safe and have no behavioral impact, use an annotation.

> [!NOTE]
> **Why not only labels?**  
> Labels are indexed and drive selection and controller behavior. Using them for verbose or tool-specific data risks performance issues and accidental behavior changes. Annotations exist to safely store metadata that must not influence Kubernetes logic.

#### Field Selectors

Field selectors let you select Kubernetes objects based on the value of one or more resource fields.

**Examples**

```bash
# 1. List running Pods
kubectl get pods \
  --field-selector=status.phase=Running

# 2. Select a Pod by exact name
kubectl get pods \
  --field-selector=metadata.name=my-pod

# 3. Chained field selectors (logical AND)
#    Pods that are Running AND scheduled on a specific node
kubectl get pods \
  --field-selector=status.phase=Running,spec.nodeName=worker-node-1

```

Official documentation: [Field Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/):
- list of supported fields
- supported operators
- supported value types
- supported logical operators
- supported chaining
- supported precedence
- supported grouping
- supported precedence

###### Use Labels and Field Selectors Together

You can apply **label selectors** and **field selectors** in the same query.  
Both filters are evaluated server-side and combined with **logical AND**.

**Example**
```bash
# Running Pods with label app=web
kubectl get pods \
  -l app=web \
  --field-selector=status.phase=Running
```

**Why combine them**

* Labels express **intent** (what the object represents)
* Field selectors express **state or placement** (how/where it runs)
* Together they enable precise, safe filtering

**Common use cases**

* Debug a specific app only when Pods are running
* Target workloads on a specific node
* Automate cleanup of labeled resources in a given state

**Guideline** :Use labels for ownership and grouping; add field selectors to narrow by runtime state.

#### Finalizers

Finalizers are a mechanism in Kubernetes that allows you to perform custom actions when an object is deleted.

When you create a resource using a manifest file, you can specify finalizers in the `metadata.finalizers` field. Finalizers are a list of strings.

For example, Kubernetes uses finalizers to prevent deleting a `PersistentVolumeClaim (PVC)` that is still in use.

While the PVS is in use kubernetes will keep the finalizer in place to prevent the deletion of the PVC.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data-pvc
  finalizers:
    - kubernetes.io/pvc-protection
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

**What happens**

1. You delete the PVC.
2. Kubernetes sets `deletionTimestamp`; PVC enters `Terminating`.
3. As long as a Pod is using the volume, the finalizer remains.
4. Once the volume is no longer in use, the finalizer is removed.
5. The PVC is actually deleted.

**Key point**: Finalizers block deletion until required cleanup (or safety checks) are complete.

Learn more in the Official documentation:
 - [Finalizers](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/)
 - [Using Finalizers to Control Deletion](https://kubernetes.io/blog/2021/05/14/using-finalizers-to-control-deletion/)


#### Owners and Dependents

TL:DR: Owners and dependents are a mechanism in Kubernetes that allows you to control the lifecycle of objects.

* **Concept:** Some Kubernetes objects *own* others. The owning object is the **owner**; the associated objects are its **dependents**. For example, a ReplicaSet owns its Pods. This relationship helps manage lifecycles and avoid interfering with resources not under a controller’s control.

* **Owner references:** Dependents have a `metadata.ownerReferences` field pointing to their owner (name, UID, kind, apiVersion). Kubernetes automatically sets this for many controller-created objects (ReplicaSets, Deployments, Jobs, etc.), but it can also be set manually.

* **Difference from labels/selectors:** Labels and selectors match or group resources; owner references express a structural, lifecycle relationship used by the control plane.

* **Garbage collection:** The garbage collector uses owner references to determine when a dependent should be automatically deleted if its owner is removed (cascade). Cross-namespace owner references are disallowed; a namespaced owner must be in the same namespace.

* **Use cases:**
  • Enable cascading deletion of dependents when an owner is deleted
  • Let controllers track and manage the objects they create
  • Prevent accidental interference by other controllers or users

Learn more in the Official documentation:
 - [Owners and Dependents](https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/)
 - [Garbage Collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/)

#### Storage Version
TODO: https://kubernetes.io/docs/concepts/overview/working-with-objects/storage-version/

#### Kubernetes API
TODO: https://kubernetes.io/docs/concepts/overview/kubernetes-api/

### Containers
Official documentation: [Containers](https://kubernetes.io/docs/concepts/containers/)

A container is a lightweight and portable executable image that contains software and all of its dependencies.

Pods:
- Kubernetes runs containers inside Pods. 
- A Pod can contain one or more containers that share resources such as networking and storage.

**Container images** are typically pulled from a container registry and referenced in the Pod specification.
Image pulling behavior is controlled by the `imagePullPolicy` field.

**Container Runtime Interface (CRI)**:  Kubernetes supports multiple container runtimes through the **Container Runtime Interface (CRI)**. The CRI defines the API boundary between Kubernetes components and the container runtime.

#### Container lifecycle

Each container in a Pod has a lifecycle. Kubernetes tracks container states and reports them through the Pod status.

A container can be in one of the following states:
- Waiting
- Running
- Terminated

Container restarts are handled according to the Pod’s `restartPolicy` and the controller managing the Pod.

#### Container probes

Kubernetes can periodically check container health using probes:
- Liveness probes
- Readiness probes
- Startup probes

Probe results influence container restarts and Service endpoint inclusion.


#### Resource management for containers

Containers specify compute resource requirements:
- Requests
- Limits

The scheduler uses requests to place Pods on nodes. Limits are enforced at runtime.

#### Container environment variables

Environment variables can be set for containers in the Pod specification. Values can be defined directly or sourced from ConfigMaps and Secrets.

Environment variables are set when the container starts.

#### Container commands and arguments

The `command` and `args` fields allow overriding the container image defaults.

Kubernetes passes these values directly to the container process.

#### Init containers

Init containers run before application containers start. Each init container must complete successfully before the next one begins.

They share the Pod’s resources but run sequentially.

#### Ephemeral containers

Ephemeral containers can be added to a running Pod for debugging purposes.

They are not restarted and are not part of the Pod’s normal lifecycle.


#### Images — Docker Similarities and Kubernetes-Specific Differences

Official documentation: [Images](https://kubernetes.io/docs/concepts/containers/images/)

This section is intentionally very close to Docker concepts. The key value is understanding **where Kubernetes behavior diverges or adds constraints**.

##### Image names

**Same as Docker**
- Registry / repository / tag / digest syntax
- Default registry and default `latest` tag behavior

**Kubernetes differences**
- Image name resolution happens on the **node**, not centrally
- No global image configuration; behavior depends on node runtime + kubelet

##### Image pull policy

**Same as Docker**
- Pull vs reuse cached images
- Tag mutability implications

**Kubernetes differences**
- Pull behavior is **explicitly modeled** via `imagePullPolicy`:  `Always` (pull on every container start), `IfNotPresent` (pull only if missing on node), `Never` (require image to already exist locally)
- Default policy is derived from tag (`latest` → `Always`)
- Policy is evaluated by **kubelet**, not the runtime CLI

##### ImagePullBackOff

`ImagePullBackOff`: container state indicating repeated image pull failures, with retries governed by kubelet-controlled exponential backoff

**Same as Docker**
- Pull failures due to auth, network, or missing images

**Kubernetes differences**
- Failure is surfaced as a **container state**, not a command error
- Retries use kubelet-controlled exponential backoff
- Backoff state affects Pod scheduling and readiness semantics

##### Image pull secrets

**Same as Docker**
- Registry credentials
- Auth material not embedded in images

**Kubernetes differences**
- Credentials are **declarative objects** (Secrets)
- Can be injected implicitly via ServiceAccounts
- Scoped to namespaces and Pods, not users or hosts

For practical examples: [k8s-registry-auth-howto.md](k8s-registry-auth-howto.md)

##### Using a private registry

**Same as Docker**
- Requires network access and valid credentials

**Kubernetes differences**
- Registry access is evaluated per-node
- Failures are opaque unless node-level logging is inspected
- No interactive auth flows; everything must be preconfigured

---

##### Multi-architecture images

**Same as Docker**
- Manifest lists and platform-specific image selection

**Kubernetes differences**
- Platform selection is driven by **node architecture**
- Pod spec remains architecture-agnostic
- Scheduling + runtime jointly determine the final image variant

---

##### Image updating

**Same as Docker**
- Running containers are not mutated in place

**Kubernetes differences**
- Image updates are triggered by **Pod recreation**, not image change alone
- Controllers, not images, define rollout behavior
- `imagePullPolicy` only affects *when* images are fetched, not *what* restarts

---

##### Mental shortcut

> If Docker answers *“how does this image run?”*  
> Kubernetes answers *“when, where, and under what guarantees does this image run?”*
