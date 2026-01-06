# How to manage different kubernetes credentials and kubeconfig files

## Why choose **kubie** for Kubernetes context management

You have a single machine with multiple kubernetes clusters and you need to manage the credentials for each cluster.

### Problem
Managing multiple Kubernetes clusters across customers and environments introduces recurring issues:

- Risk of operating on the wrong cluster
- Global `KUBECONFIG` pollution across shells
- Manual exports and shell scripts
- Accidental context/namespace leakage between terminals
- Need to keep kubeconfigs **separated**, not merged

### Solution: kubie
**kubie** is designed to solve these problems explicitly.

It is an alternative to:
- `kubectx`
- `kubens`
- shell prompt modification scripts

while covering **more ground** in a safer way.

**Key advantages:**

#### 1. Shell isolation (core feature)
- Each shell has its own active kubeconfig, context, and namespace
- Switching in one terminal does **not** affect others
- Eliminates cross-customer and cross-environment mistakes

#### 2. Native support for multiple kubeconfig files
- One kubeconfig per customer (or per environment)
- No need to merge configs
- Central configuration (`~/.kubie.yaml`) defines where kubeconfigs live

Example:
```yaml
configs:
  acme: ~/.kube/configs/acme.yaml
  beta: ~/.kube/configs/beta.yaml
```


#### 3. Unified context + namespace switching

- `kubie ctx` → switch context
- `kubie ns` → switch namespace
- Prompt is updated automatically
- No additional tools required

#### 4. Zero environment variable management

- No export KUBECONFIG=...
- No aliases or shell glue
- `kubie` manages lifecycle transparently

#### 5. Safe one-off command execution

Run commands in a specific context/namespace without spawning a shell:

```bash
kubie exec acme-prod -- kubectl get pods
```

Useful for scripts, CI checks, or quick inspections.

#### 6. Configuration linting
Detect issues early:

```bash
kubie lint
```

Finds:
- Duplicate context names
- Broken references
- Misconfigured users/clusters

#### Comparison with common tools

| Tool            | Multi kubeconfig | Shell isolation | Context | Namespace | Prompt |
|-----------------|:----------------:|:---------------:|:-------:|:---------:|:------:|
| kubectx         | ❌               | ❌              | ✅      | ❌        | ❌     |
| kubens          | ❌               | ❌              | ❌      | ✅        | ❌     |
| prompt scripts  | ❌               | ❌              | ❌      | ❌        | ✅     |
| kubie           | ✅               | ✅              | ✅      | ✅        | ✅     |

Recommended usage pattern
- Boundary = kubeconfig (customer / account / organization)
- Inside boundary: contexts and namespaces
- One shell = one cluster
- No shared global state

Conclusion

If your goals are:
	•	strict separation between customers
	•	zero-risk context switching
	•	no kubeconfig merging
	•	no environment-variable juggling

kubie is the correct tool.

It provides a clean, explicit, and safe mental model for working with Kubernetes at scale.













## How to use kubie

See [kubie usage](https://github.com/sbstp/kubie?tab=readme-ov-file#usage) for complete documentation.

Most common commands:

```bash
# Choose a context
kubie ctx

# Choose a namespace
kubie ns
```