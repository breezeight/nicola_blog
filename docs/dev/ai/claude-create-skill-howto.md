## Prerequisites

- You need to have the skill-creator plugin installed.
- You need to have the clarify command available.

Install the skill-creator plugin
/plugin install skill-creator@anthropic-agent-skills

> [!WARNING]
> As of jan 2026, we didn't manage to install the skill-creator plugin using the /plugin install command. A workaround is to use the following command:
> `npx skills-installer install @anthropics/claude-code/skill-development --local --client claude-code`

## clarify command

```md
---
description: Clarify any text through iterative deep questioning
argument-hint: [text-to-clarify]
allowed-tools: AskUserQuestion
---

# Text Clarification Interview

You are conducting an iterative clarification interview for the text provided below.

## Input Text to Clarify

$ARGUMENTS

If no argument was provided above, look for text to clarify in the recent conversation context. If none found, ask the user to provide text to clarify.

## Core Instruction

Interview me in detail using the AskUserQuestionTool about literally anything: technical implementation, UI and UX, concerns, trade-offs, etc. Make sure the questions are not obvious, be very in-depth, and continue interviewing me continuously until it is complete.

## Process

1. **Analyze** the input text for ambiguities, missing context, unclear requirements, assumed knowledge, and gaps

2. **Interview Loop**:
   - Ask as many deep, non-obvious clarifying questions as needed using `AskUserQuestion`
   - Probe: technical implementation, UI/UX, concerns, trade-offs, edge cases, dependencies, constraints
   - After each round of answers, update your internal thinking scratchpad with the evolving clarification
   - Do NOT show drafts to the user - keep them in your thinking only
   - Continue until the user explicitly indicates they are done (e.g., "done", "that's all", "finished")

3. **Final Output**: When the user says they're done, produce the final clarification in this exact 4-part structure:

1. Problem:
[What problem or need the task addresses - the "why" behind the request]

2. Root Cause:
[The underlying cause or context that created this problem/need]

3. Solution:
[The fully clarified description of what should be built/changed/fixed]

4. Verification:
[How to verify the solution works - concrete steps to test the result/outcome/effects of the completed task]
```

## Question Guidelines

- Questions should be **non-obvious** - don't ask things that are already clear
- Questions should be **in-depth** - probe the "why" and "how", not just the "what"
- Cover multiple dimensions: technical feasibility, user experience, edge cases, constraints, dependencies, trade-offs, success criteria
- Use `AskUserQuestion` with well-structured options when possible, but allow "Other" for open-ended responses
- Ask 3-6 questions per round to maintain momentum without overwhelming

## Important

- Never terminate early - keep interviewing until the user explicitly says done
- Maintain your evolving understanding in internal thinking, not visible output
- The 4-part output format is mandatory for the final response
- Works for any text: technical specs, requirements, bug reports, feature requests, proposals, or general descriptions

Begin by analyzing the input text and asking your first round of clarifying questions.




### PRomt
1. Problem:

  The user needs a Claude Code skill that provides comprehensive Kubernetes cluster management assistance with context-aware intelligence. Currently, there's no structured way to leverage organization-specific K8s configurations, best practices, and runbooks within Claude Code conversations while also adapting to different environments and user expertise levels.

  2. Root Cause:

  Managing Kubernetes effectively requires both general K8s knowledge AND organization-specific context (your manifests, conventions, tooling choices). Generic K8s assistance lacks awareness of your infrastructure patterns, while raw documentation doesn't adapt to task context. The gap is a skill that can intelligently consult relevant reference materials based on what the user is actually trying to accomplish.

  3. Solution:

  Create a Kubernetes management skill with the following characteristics:

  Scope & Capabilities:
  - Covers all K8s domains: troubleshooting/debugging, configuration review/authoring, cluster operations, and security/compliance
  - Beginner-friendly with brief inline explanations of concepts
  - Multi-environment aware (prod/staging/dev) with user verification via AskUserQuestion
  - Flexible tooling detection (kubectl, Helm, GitOps) based on reference file contents

  Reference File System:
  - Files embedded within the skill directory itself
  - Skill analyzes conversation context and user query to determine which files to consult
  - Silent consultation (doesn't explicitly list which files were read)
  - Can suggest edits to reference files with user approval
  - Surfaces conflicts between files for user resolution
  - Falls back to web documentation (WebFetch) for resource types not covered

  Interaction Model:
  - Uses AskUserQuestion tool to clarify tasks and verify environments before acting
  - Conservative triggering: only activates on explicit kubernetes/k8s mentions or skill invocation
  - On-demand cluster state discovery (queries only when needed)
  - Dry-run first for all destructive operations (delete, scale to 0, etc.)

  Output Conventions:
  - Generated manifests follow official Kubernetes style conventions
  - Skill name/trigger to be determined during implementation (options: /k8s, /kubernetes, /kube-ops, /cluster)
  - Quick action modes to be determined during implementation (options: debug mode, review mode, both, or none)

  Implementation Note:
  The skill must first review the provided <files-list> placeholder to understand the existing reference documents before determining how to structure its file selection logic.

  4. Verification:

  1. Trigger test: Invoke the skill explicitly and verify it activates; mention unrelated topics and verify it does NOT activate
  2. Reference consultation: Ask a K8s question that should match a specific reference file; verify the response incorporates that file's content appropriately
  3. Environment verification: Ask about a deployment without specifying environment; verify skill uses AskUserQuestion to confirm target env
  4. Destructive operation safety: Request a delete operation; verify dry-run output is shown before any execution prompt
  5. Beginner explanation: Ask about a complex concept; verify brief inline explanation is provided
  6. Conflict handling: If reference files have conflicting info, verify skill surfaces the conflict for user resolution
  7. Fallback behavior: Ask about an obscure CRD not in reference files; verify skill falls back to web docs
  8. File edit capability: Point out an issue in a reference file; verify skill can propose and make edits with approval


## CREATE THE SKILL

We used the clarify command to create the skill specification below


<FILES-LIST> ==> tutta la documentazione che ho su kubernetes 


____


please read this brief and use the skill-creator skill to create project level skill

FILES TO REVIEW TO INSERT/IMPORT IN THE SKILL AS REFERENCE (DO NOT MOVE THE ORIGINAL FILES:

<FILES-LIST>

BRIEF:
```
  1. Problem

  There is a need for a Claude Code skill that provides intelligent Kubernetes operations assistance—specifically for workload deployment, troubleshooting, and CI/CD pipeline generation—while leveraging project-specific reference files (documentation and manifest examples) to provide contextually relevant guidance rather than generic advice.

  2. Root Cause

  Kubernetes operations require deep contextual knowledge: each project has its own conventions, manifest patterns, tooling (Helm, ArgoCD), and operational procedures. Generic K8s assistance lacks awareness of these project-specific patterns. Additionally, intelligent file selection is needed to avoid context bloat when dealing with 6-15 reference files while ensuring the right documentation is consulted for each task.

  3. Solution

  Create a skill named /k8s with the following specifications:

  Core Capabilities:
  - Workload deployment: Deploy, update, and rollback Deployments, StatefulSets, DaemonSets across any K8s environment (cloud-managed, self-hosted, local dev)
  - Troubleshooting: Context-dependent diagnostic approach—skill asks clarifying questions to determine whether to use pod-first, top-down, or event-driven debugging strategy
  - CI/CD pipeline generation: Help create GitHub Actions, GitLab CI, or other pipeline configs for K8s deployments
  - GitOps awareness: Understand ArgoCD/Flux workflows, check sync status, trigger syncs, view app health; remind users about GitOps implications

  Reference File Integration:
  - Embedded reference files: 6-15 files consisting of markdown documentation + YAML manifests (paths to be provided separately and attached to this spec)
  - Semantic file selection: On invocation, skill reads and understands file contents to determine relevance to the current task/conversation context
  - Manifest generation follows project conventions based on these reference templates

  Tooling Support:
  - kubectl (primary)
  - Helm for chart-based deployments
  - ArgoCD/Flux basic operations
  - kubeconfig is pre-configured; skill uses current context without auth setup

  Execution Model:
  - Confirmation-first execution: All kubectl/helm commands require user approval via AskUserQuestion before execution
  - Read-only commands (get, describe, logs) still require confirmation but are lower-friction
  - Destructive operations: Always require explicit confirmation via AskUserQuestion (delete, scale to 0, force rollbacks)

  Behavioral Patterns:
  - Trigger: Both explicit /k8s command and auto-detection when conversation involves Kubernetes topics
  - Conversation state: Maintains context within the same conversation (e.g., current namespace, last-checked resources) but resets between sessions
  - Ambiguity handling: Uses AskUserQuestion immediately when multiple resources match or intent is unclear
  - Proactive best practices: Always surfaces potential issues (missing resource limits, no liveness probes, security context gaps) even when not explicitly asked
  - Web documentation: Fetches fresh K8s documentation via WebFetch when dealing with unfamiliar resources/APIs or when stuck

  Description for skill metadata:
  Kubernetes operations assistant for workload deployment, troubleshooting, and CI/CD pipeline generation. Supports kubectl, Helm, and ArgoCD/Flux workflows. Uses semantic understanding of embedded reference files to provide project-specific guidance. Requires confirmation before executing commands. Auto-triggers on K8s-related conversations or via /k8s.

  4. Verification

  1. Skill loads correctly: Invoke /k8s and verify it activates with embedded reference files accessible
  2. Semantic file selection: Ask about a deployment issue; skill should read relevant manifest examples and troubleshooting docs (not unrelated files)
  3. Command confirmation: Request a deployment; skill should present the kubectl/helm command and use AskUserQuestion for approval before execution
  4. Destructive operation safety: Ask to delete a resource; skill must require explicit confirmation via AskUserQuestion
  5. Troubleshooting flow: Describe a pod issue; skill should ask clarifying questions about symptoms before prescribing a diagnostic approach
  6. GitOps awareness: Ask about deploying when ArgoCD is mentioned; skill should remind about sync implications
  7. Proactive hints: Deploy a manifest missing resource limits; skill should surface this as a best practice concern
  8. Auto-trigger: Mention Kubernetes in conversation without explicit /k8s; skill should activate based on context
  9. Web fetch: Ask about an obscure K8s resource; skill should use WebFetch to retrieve current documentation
```