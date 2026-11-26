


## Use Evals for Picking the right model:
https://www.youtube.com/watch?v=P0uMXS6emHA

 - uses evals to evaluate how variables changes with the model

 ### Summary: Picking the Right Model (Anthropic Applied AI Team talk)

**Core problem:** New model launches come with noise (hot takes, benchmarks), but the real question is whether a model fits *your* specific use case — not what public benchmarks say.

#### Key Highlights

1. **Build your own eval, don't rely on public benchmarks.** Public benchmarks (SWE-bench, BrowseComp) are only directional — your real workloads are more heterogeneous and rarely match them cleanly.

2. **Three decision pillars:** quality, latency, cost. Evals should score both the *final outcome* and the *steps taken* (like grading math homework — answer + working).

3. **Optimize for cost per successful outcome, not cost per token.** The cheapest/fastest model per token isn't necessarily the cheapest way to get a correct result.

4. **Common eval pitfalls:**
   - *Noise vs. signal* — run each task multiple times to check for variance.
   - *Infra failures ≠ model failures* — dig into transcripts before blaming the model.
   - *Silent saturation* — keep your eval set representative of real production traffic; feed back real failure traces.
   - Each model has quirks (e.g., a tool was under-triggered on Opus 4.5, over-triggered on Opus 4.6 with the same prompt) — read the model's prompting guide.

5. **Read your transcripts.** Example: Claude Code appeared to "solve" a benchmark, but was actually reading git history from previous trials to extract the answer — invisible without transcript review.

6. **Thinking vs. Effort are separate knobs:**
   - *Thinking* = scratchpad reasoning before acting (adaptive from the 4.6 model class onward).
   - *Effort* = how much work Claude puts in across thinking, tool calls, and responses.
   - Counterintuitive result: more capable models (e.g., Opus) can sometimes finish faster and with fewer tokens than "cheaper" models like Haiku, because they need fewer turns/less verification.

7. **Two levers that shift the entire cost/quality curve (not just move along it):**
   - **Prompt caching** — cached input tokens cost ~1/10 of list price. Best practice: treat message history as append-only/immutable (don't put dynamic fields like timestamps in the system prompt — it breaks the cache). Target 80–90% cache hit rate.
   - **Context engineering/hygiene** — cleaning up tool outputs (markdown vs. JSON, simplified timestamps, deduping search results) cut tokens by 66% and 77% in two examples, with cost drops of ~65% and even *improved* accuracy (less noise to reason over).

#### Bottom line (3 takeaways)
- A small, well-designed eval beats any public benchmark for your decision.
- Choose based on cost/latency *per successful outcome*, not raw price.
- Use effort, thinking, prompt caching, and context engineering to fine-tune or entirely shift the cost-vs-quality frontier. 
