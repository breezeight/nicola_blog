Key points about Argo CD from the meeting:

- **How it works**
  - Uses `helm template` (not `helm install`) to render manifests.
  - Compares rendered manifests with what’s actually in the cluster.
  - Marks apps as *synced* / *out of sync* and shows a diff between Git and cluster.

- **Applications vs ApplicationSets**
  - **Application**: describes a single deployment (one app).
  - **ApplicationSet**: generates multiple similar Applications (e.g., one per namespace/campaign) from a template.
  - In your setup there is an “app-of-apps” pattern: one Application that points Argo CD at a repo/directory, and Argo auto‑creates/updates the individual Applications from there.

- **Image updater integration**
  - A separate **Argo CD Image Updater** component:
    - Polls ECR for the latest images ~every 3 minutes.
    - Writes new tags into the Helm values files in Git (creating commits).
    - Argo CD then sees the Git change, re‑renders the chart, and syncs.
  - Needs ECR credentials; token expiry can cause updater to stall until fixed.

- **Why it only uses `template`**
  - Argo wants full control: it renders manifests with Helm and then applies them itself.
  - So Helm releases are not visible via `helm list` (Argo is just using the templating, not Helm’s release DB).

- **CI/CD implications**
  - Current flow: code → CI builds & pushes image → Argo Image Updater commits new tag → Argo CD syncs.
  - This adds a small delay and some complexity.
  - You discussed possibly simplifying by letting CI write the image tag directly into the Helm values repo, instead of using Image Updater.


  -   **Argo CD as a controller**
    
    -   Argo CD is installed in the cluster (in its own namespace) and acts as a Kubernetes controller.
    -   It continuously reconciles desired state (Git) vs actual state (cluster) for:
        -   `Application` and `ApplicationSet` CRDs
        -   All the Kubernetes resources those generate (Deployments, Pods, etc.).
-   **App-of-apps / Application controller**
    
    -   There is an “app-of-apps” setup:
        -   One top‑level `Application` points to a Git repo + directory that contains other `Application` manifests.
        -   When you add/edit an app file in that directory and commit, Argo CD’s controller detects it and creates/updates the corresponding Application automatically.
-   **Custom Resources in the ecosystem**
    
    -   Argo components (CD, Workflows, etc.) are all based on **CRDs + controllers**:
        -   You define custom resources like `Application`, `ApplicationSet`, `Workflow`, etc.
        -   Their respective controllers (Argo CD, Argo Workflows) watch those CRDs and then create/update “normal” Kubernetes resources (Deployments, Jobs, Pods, etc.).

If you want, I can pull out the minimal YAML skeleton for an `Application` you’d define for PDB (prod/staging).