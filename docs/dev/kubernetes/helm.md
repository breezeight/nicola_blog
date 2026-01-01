## What is a Helm chart? Minimal mental model

A Helm chart is a parameterized Kubernetes manifest generator with lifecycle management.

A **Helm chart** is a **packaged, parameterized set of Kubernetes manifests**.

Conceptually: `Helm Chart = Kubernetes YAML + values + templating + release management`


### Typical Helm chart directory structure

```bash
my-chart/
├── Chart.yaml
├── values.yaml
├── values-prod.yaml        # optional
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── secret.yaml
│   ├── configmap.yaml
│   ├── job.yaml
│   └── _helpers.tpl
├── charts/                 # optional (dependencies)
└── README.md               # optional
```

#### `Chart.yaml`

is Mandatory, it defines chart metadata:

```yaml
apiVersion: v2
name: my-chart
description: My application Helm chart
type: application
version: 0.1.0
appVersion: "1.0.0"
```


| Field        | Meaning                       |
| ------------ | ----------------------------- |
| `name`       | Chart name                    |
| `version`    | Chart version (Helm-specific) |
| `appVersion` | Application version           |
| `type`       | `application` or `library`    |


#### `values.yaml` 
is Mandatory, it defines default configuration values used by templates:

```yaml
replicaCount: 2

image:
  repository: myorg/app
  tag: latest

service:
  port: 80
```

Values are accessed in templates via:

```yaml
{{ .Values.replicaCount }}
{{ .Values.image.repository }}
{{ .Values.image.tag }}
{{ .Values.service.port }}
```


#### `values-*.yaml`

(optional), contains Environment-specific overrides.

To use them: `helm install myapp . -f values-prod.yaml`

Common patterns: `values-dev.yaml`, `values-staging.yaml`, `values-prod.yaml`

#### `templates/` directory

In a Helm chart, the `templates/` directory is where you put Kubernetes manifest templates that Helm will render into valid YAML before applying them to the cluster.

Helm renders templates into plain Kubernetes YAML and applies them to the cluster.


If you understand:
- Kubernetes YAML
- Variables
- Templating

Then you understand Helm charts.





#### ´_helpers.tpl´

https://helm.sh/docs/chart_template_guide/named_templates/



Is `_helpers.tpl` commonly used? Yes — effectively standard.

Used by:
- Helm default chart (`helm create`)
- Official charts (Bitnami, Prometheus, Grafana)
- Internal enterprise charts

You are expected to use it if:
- Chart has more than 1–2 templates
- You want consistent naming/labels
- You care about maintainability

Not using it in non-trivial charts is considered a code smell.




### Helm templates syntax

This section explains **Helm template syntax** by focusing on how templates are written, how expressions are evaluated, and how input values are transformed into output Kubernetes manifests. The goal is to build a correct mental model of *what the syntax means* and *what it produces*, not how to scaffold or operate Helm.


#### 1. Template delimiters

Helm templates are written using **Go template delimiters**.

```yaml
{{ ... }}
```

Anything inside `{{ }}` is **evaluated**, anything outside is **literal YAML**.

Example:

**Template (input):**

```yaml
replicas: {{ .Values.replicaCount }}
```

**Values (input):**

```yaml
replicaCount: 3
```

**Rendered output:**

```yaml
replicas: 3
```

---

#### 2. The dot (`.`) context

The dot (`.`) represents the **current context object**. At the top level, it is the root context passed by Helm.

Common root fields:

* `.Values` – merged user values
* `.Release` – release metadata
* `.Chart` – chart metadata

Example:

**Template:**

```yaml
name: {{ .Release.Name }}
```

**Rendered output:**

```yaml
name: my-release
```

If the dot changes (e.g. inside a `range`), `.Values` is no longer directly accessible unless you capture the root context.

#### 3. Pipelines (`|`)

Pipelines pass the output of one expression as the input of the next function, left to right.

```yaml
{{ VALUE | function1 | function2 }}
```

Example:

**Template:**

```yaml
env:
  - name: DEBUG
    value: {{ .Values.debug | quote }}
```

**Values:**

```yaml
debug: true
```

**Rendered output:**

```yaml
env:
  - name: DEBUG
    value: "true"
```

Without `quote`, the value could be rendered as a boolean instead of a string.

#### 4. Functions

Helm exposes functions from:

* Go templates
* the Sprig library
* Helm-specific helpers

Common functions with input/output:

`default` function:

```yaml
{{ .Values.image.tag | default "latest" }}
```

* If `.Values.image.tag` is unset → `latest`
* If set → its actual value

`toYaml` function:

`toYaml` converts a map/list value (a structured object in .Values) into a YAML-formatted string. This is mainly used when you want to inject whole YAML subtrees (resources, affinity, tolerations, nodeSelector, extra labels, etc.) without manually writing every key.

**Template (input):**

```yaml
resources:
{{ .Values.resources | toYaml | nindent 2 }}
```

`toYaml` turns the object into YAML text.

`nindent 2` adds a leading newline and indents every line by 2 spaces, so the injected YAML becomes valid under `resources:`.

**Values (input):**

```yaml
resources:
  limits:
    cpu: "500m"
```

**Rendered output:**

```yaml
resources:
  limits:
    cpu: "500m"
```

**Counterexample (what goes wrong without toYaml):**

**Template:**

```yaml
resources: {{ .Values.resources }}
```

**Rendered output (invalid YAML for K8S schema):**

```yaml
resources: map[limits:map[cpu:500m]]
```

That output is just the Go string representation of a map, not YAML.

**Counterexample (what goes wrong without correct indentation):**

**Template:**

```yaml
resources:
{{ .Values.resources | toYaml }}
```

**Rendered output (often invalid YAML due to indentation):**

```yaml
resources:
limits:
  cpu: "500m"
```

Here `limits` is no longer nested under `resources` because it isn't indented.

---

#### 5. Whitespace control (`{{-` and `-}}`)

By default, Go templates preserve surrounding whitespace. Helm allows trimming it.

```yaml
{{- ... -}}
```

Example:

**Template:**

```yaml
{{- if .Values.enabled }}
enabled: true
{{- end }}
```

**When `enabled: false`**, the entire block is removed *without leaving empty lines*.

This is critical for producing clean YAML.

---

#### 6. Conditionals (`if`, `else`)

Conditionals control whether sections are rendered.

Example:

**Template:**

```yaml
{{- if .Values.ingress.enabled }}
kind: Ingress
{{- end }}
```

**Values:**

```yaml
ingress:
  enabled: false
```

**Rendered output:**

```yaml
# (nothing rendered)
```

Helm does not validate YAML semantics at this stage; it only renders text.

---

##### 6.1. Advanced Conditionals with Logical Operators and Validation

Helm templates support logical operators (`and`, `or`, `not`) to create complex conditional expressions. Combined with the `fail` function, you can implement validation logic that prevents invalid chart configurations.

**Logical Operators:**

- `and` - Returns true if all arguments are truthy
- `or` - Returns true if any argument is truthy  
- `not` - Negates a boolean value

**The `fail` Function:**

The `fail` function stops template rendering immediately and returns an error message. This is useful for validating that required values are set correctly or that certain value combinations are valid.

**Example: Validating Configuration Dependencies**

```yaml
{{- if and .Values.backend.eamEnabled (not .Values.backend.featureModernEamBackend) }}
{{- fail "Error: 'backend.featureModernEamBackend' must be true for 'backend.eamEnabled' to be set to true too" }}
{{- end }}
```

**What this does:**

1. **Condition Check**: `{{- if and .Values.backend.eamEnabled (not .Values.backend.featureModernEamBackend) }}`
   - Checks if `backend.eamEnabled` is `true` AND `backend.featureModernEamBackend` is `false`
   - The `-` trims whitespace before the template tag

2. **Validation Failure**: `{{- fail "Error: ..." }}`
   - If the condition is true (invalid configuration), the template rendering stops
   - Returns the error message to the user
   - Prevents deploying a chart with incompatible settings

3. **Block Closure**: `{{- end }}`
   - Closes the `if` block

**Valid Configuration Scenarios:**

```yaml
# ✅ Valid: eamEnabled=false, featureModernEamBackend=false
backend:
  eamEnabled: false
  featureModernEamBackend: false

# ✅ Valid: eamEnabled=true, featureModernEamBackend=true
backend:
  eamEnabled: true
  featureModernEamBackend: true

# ❌ Invalid: eamEnabled=true, featureModernEamBackend=false
# This will fail with the error message
backend:
  eamEnabled: true
  featureModernEamBackend: false
```

**Common Use Cases:**

- Enforcing feature flags: "Feature X requires Feature Y to be enabled"
- Validating dependencies: "Service A cannot be enabled without Service B"
- Checking required combinations: "Production mode requires monitoring to be enabled"
- Preventing invalid states: "Cannot disable authentication when admin access is enabled"

**Syntax Notes:**

- `{{-` trims whitespace before the template (removes preceding newline/space)
- `-}}` trims whitespace after the template (removes following newline/space)
- Without the `-`, template tags would leave empty lines in the rendered YAML

---

#### 7. Loops (`range`)

`range` iterates over lists or maps and **changes the dot context**.

Example:

**Template:**

```yaml
env:
{{- range .Values.env }}
  - name: {{ .name }}
    value: {{ .value | quote }}
{{- end }}
```

**Values:**

```yaml
env:
  - name: MODE
    value: prod
  - name: LOG_LEVEL
    value: info
  - name: DATABASE_URL
    value: postgres://localhost:5432/mydb
```

**Rendered output:**

```yaml
env:
  - name: MODE
    value: "prod"
  - name: LOG_LEVEL
    value: "info"
  - name: DATABASE_URL
    value: "postgres://localhost:5432/mydb"
```

Inside `range`, `.` refers to the current item. To access the root context (e.g., `.Release.Name` or `.Values`) from within a `range`, use `$`:

**Template:**

```yaml
env:
{{- range .Values.env }}
  - name: {{ .name }}
    value: {{ .value | quote }}
    release: {{ $.Release.Name }}
{{- end }}
```

**Rendered output:**

```yaml
env:
  - name: MODE
    value: "prod"
    release: my-release
  - name: LOG_LEVEL
    value: "info"
    release: my-release
```

---

#### 8. Named templates and `include`

Named templates are reusable fragments, usually defined in `_helpers.tpl`.

**Definition (input):**

```yaml
{{- define "myapp.fullname" -}}
{{ .Release.Name }}-{{ .Chart.Name }}
{{- end }}
```

**Usage (input):**

```yaml
metadata:
  name: {{ include "myapp.fullname" . }}
```

**Rendered output:**

```yaml
metadata:
  name: my-release-myapp
```

`include` always returns a string; formatting must be applied explicitly.

---

#### 9. `with` blocks (context narrowing)

`with` is used to conditionally enter a block and temporarily change the dot (`.`) context. The block is rendered only if the value is non-empty (not `nil`, not empty list/map, not `false`).

The most common use is to:

* avoid repeating long paths like `.Values.volumeMounts`
* render optional nested YAML blocks cleanly

**Given template:**

```yaml
{{- with .Values.volumeMounts }}
volumeMounts:
  {{- toYaml . | nindent 12 }}
{{- end }}
```

This combines three concepts:

* `with` → conditional + context switch
* `.` inside the block → now equals `.Values.volumeMounts`
* `toYaml | nindent` → inject structured YAML correctly

**Step-by-step semantics:**

1. **Condition check**

   `with .Values.volumeMounts`

   * If `.Values.volumeMounts` is undefined, empty, or `null` → the entire block is skipped
   * If it exists and is non-empty → the block is rendered

   This avoids rendering empty `volumeMounts:` sections.

2. **Context switch**

   Inside the `with` block:

   * `.` now refers to: `.Values.volumeMounts`

   So this line:

   ```yaml
   {{- toYaml . | nindent 12 }}
   ```

   means: Convert `.Values.volumeMounts` to YAML and indent it

**Example (working case):**

**Values (input):**

```yaml
volumeMounts:
  - name: data
    mountPath: /data
```

**Rendered output:**

```yaml
volumeMounts:
            - name: data
              mountPath: /data
```

(The large indentation comes from `nindent 12`, matching the surrounding manifest structure.)

**Counterexample 1: without `with`**

**Template:**

```yaml
volumeMounts:
  {{- toYaml .Values.volumeMounts | nindent 12 }}
```

**When `volumeMounts` is undefined, the rendered output is:**

```yaml
volumeMounts:
            null
```

This produces invalid Kubernetes manifests.

**Counterexample 2: forgetting that `with` changes `.`**

**Template:**

```yaml
{{- with .Values.volumeMounts }}
# trying to access other values
image: {{ .Values.image.repository }}
{{- end }}
```

**Rendered result:**

```
Error: can't evaluate field Values in type []interface {}
```

Because inside `with`, `.` is no longer the root context.

**Correct version:**

```yaml
{{- $root := . }}
{{- with .Values.volumeMounts }}
image: {{ $root.Values.image.repository }}
{{- end }}
```

**Mental rule for `with`:**

* `with X` == `if X` plus `.` becomes `X`
* Use it for optional nested structures
* Capture the root context if you need to access it inside the block

---

####  Mental model summary

Helm templating is:

* **Pure text rendering** (not YAML-aware)
* **Context-driven** (dot matters)
* **Function-based** (via pipelines)
* **Order-sensitive** (render first, validate later)

Understanding the syntax means understanding *how text transforms from input to output*, not how Helm deploys resources.
