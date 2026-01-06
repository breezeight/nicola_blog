

## Claude Agents SDK

[claude_agents_sdk](claude_agents_sdk.md)

## Claude Code

### Slash commands
https://code.claude.com/docs/en/slash-commands

[Official documentation](https://code.claude.com/docs/en/common-workflows#create-custom-slash-commands)

Problem that they solve: you have a bunch of prompts that you constantly use using copy/paste but you want to be able to use them with a single command. So you can use them with a single command.


### Agents Skills

Some concepts are explained in the [Agent Skills](#agent-skills) section because agents skills are a concept that is related not only to cloud code. In this section, we will focus on the concepts that are specific to Claude Code.






## Agent Skills

[Official documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)


#### Agent Skill State of the art and positioning dec-2025

Key points of the Anthropic Agent Skills video ("Don't Build Agents, Build Skills Instead – Barry Zhang & Mahesh Murag, Anthropic"):

1. **Framing the problem**
   Agents are now widely used, but they still fall short for real work because they lack consistent domain expertise. The talk introduces a shift from building agents to building skills.
   [https://www.youtube.com/watch?v=CEvIs9y1uog&t=16](https://www.youtube.com/watch?v=CEvIs9y1uog&t=16)

2. **Agents vs domain expertise**
   Today’s agents are very intelligent but resemble a “300-IQ generalist”: brilliant, yet unreliable for tasks that require established professional practice (e.g. tax law).
   [https://www.youtube.com/watch?v=CEvIs9y1uog&t=20](https://www.youtube.com/watch?v=CEvIs9y1uog&t=20)

3. **Code as the universal interface**
   Code is not just a use case; it is the universal interface to the digital world. A single general-purpose agent can operate across domains through code execution.
   [https://www.youtube.com/watch?v=CEvIs9y1uog&t=70](https://www.youtube.com/watch?v=CEvIs9y1uog&t=70)

4. **From specialized agents to general agents**
   What looked like many domain-specific agents turns out to be one largely universal agent paired with a runtime environment (filesystem, shell, code execution).
   [https://www.youtube.com/watch?v=CEvIs9y1uog&t=90](https://www.youtube.com/watch?v=CEvIs9y1uog&t=90)

5. **Definition of skills**
   Skills are organized collections of files—essentially folders—that package composable procedural knowledge for agents.
   [https://www.youtube.com/watch?v=CEvIs9y1uog&t=120](https://www.youtube.com/watch?v=CEvIs9y1uog&t=120)

6. **Why skills are file-based**
   Files are human- and agent-friendly, versionable, shareable, and already embedded in existing workflows (Git, Drive, ZIP).
   [https://www.youtube.com/watch?v=CEvIs9y1uog&t=160](https://www.youtube.com/watch?v=CEvIs9y1uog&t=160)

7. **Scripts as tools inside skills**
   Skills can include scripts that act as reusable tools, improving consistency and avoiding repeated regeneration of the same logic.
   [https://www.youtube.com/watch?v=CEvIs9y1uog&t=240](https://www.youtube.com/watch?v=CEvIs9y1uog&t=240)

8. **Progressive disclosure and context efficiency**
   Only lightweight metadata is shown initially; full contents are loaded on demand, protecting the context window.
   [https://www.youtube.com/watch?v=CEvIs9y1uog&t=270](https://www.youtube.com/watch?v=CEvIs9y1uog&t=270)

9. **Rapid ecosystem growth**
   Thousands of skills emerged within weeks, spanning foundational, partner, and enterprise skills.
   [https://www.youtube.com/watch?v=CEvIs9y1uog&t=300](https://www.youtube.com/watch?v=CEvIs9y1uog&t=300)

10. **Foundational and partner skills**
    Examples include document editing, scientific research, browser automation, and workspace-specific integrations.
    [https://www.youtube.com/watch?v=CEvIs9y1uog&t=330](https://www.youtube.com/watch?v=CEvIs9y1uog&t=330)

11. **Enterprise adoption**
    Large organizations use skills to encode internal best practices, bespoke tooling, and developer workflows.
    [https://www.youtube.com/watch?v=CEvIs9y1uog&t=390](https://www.youtube.com/watch?v=CEvIs9y1uog&t=390)

12. **Skills becoming more complex**
    Skills are evolving into maintained software artifacts containing binaries, assets, and workflows.
    [https://www.youtube.com/watch?v=CEvIs9y1uog&t=420](https://www.youtube.com/watch?v=CEvIs9y1uog&t=420)

13. **Skills and MCP complement each other**
    MCP servers provide connectivity; skills provide expertise. Together they enable complex workflows.
    [https://www.youtube.com/watch?v=CEvIs9y1uog&t=510](https://www.youtube.com/watch?v=CEvIs9y1uog&t=510)

14. **Emerging agent architecture**
    A general agent consists of a runtime, MCP connections, and a large on-demand library of skills.
    [https://www.youtube.com/watch?v=CEvIs9y1uog&t=560](https://www.youtube.com/watch?v=CEvIs9y1uog&t=560)

15. **Treating skills like software**
    Future focus includes testing, evaluation, versioning, dependency management, and quality measurement.
    [https://www.youtube.com/watch?v=CEvIs9y1uog&t=630](https://www.youtube.com/watch?v=CEvIs9y1uog&t=630)

16. **Skills as transferable memory**
    Skills act as persistent procedural memory that improves agent performance over time.
    [https://www.youtube.com/watch?v=CEvIs9y1uog&t=800](https://www.youtube.com/watch?v=CEvIs9y1uog&t=800)

17. **Continuous learning and evolution**
    Agents can acquire, evolve, and discard skills, making later performance meaningfully better than day one.
    [https://www.youtube.com/watch?v=CEvIs9y1uog&t=820](https://www.youtube.com/watch?v=CEvIs9y1uog&t=820)

18. **Computing analogy**
    Models are processors, agent runtimes are operating systems, and skills are applications encoding expertise.
    [https://www.youtube.com/watch?v=CEvIs9y1uog&t=860](https://www.youtube.com/watch?v=CEvIs9y1uog&t=860)

    **Moving up the stack:**

```mermaid
flowchart TD
    Skills["<b>Applications</b><br/><small>becomes ==> Skills, Commands & Hooks</small><br/><br/><small>Reusable capabilities encoding expertise<br/>Custom shortcuts and workflow triggers</small>"]
    Agents["<b>Operating Systems</b><br/><small>becomes ==> Agents</small><br/><br/><small>Agent runtimes that<br/>orchestrate workflows</small>"]
    Models["<b>Processors</b><br/><small>becomes ==> Models</small><br/><br/><small>LLMs that process<br/>and generate content</small>"]
    
    Skills -->|built on| Agents
    Agents -->|built on| Models
    
    style Skills fill:#E8D5B7,stroke:#C4A574,stroke-width:3px,color:#000000
    style Agents fill:#D3D3D3,stroke:#A0A0A0,stroke-width:3px,color:#000000
    style Models fill:#FFB380,stroke:#FF8C42,stroke-width:3px,color:#000000
```

    

19. **Final conclusion**
    The future is general agents + MCP servers + skills. Stop rebuilding agents; start building skills.
    [https://www.youtube.com/watch?v=CEvIs9y1uog&t=960](https://www.youtube.com/watch?v=CEvIs9y1uog&t=960)

If you want, I can compress this into a **single-screen summary**, or map it directly to **MCP + skills design notes** for your own stack.





### Howto create a skill 

SEE [Claude - create a skill - howto](claude-create-skill-howto.md)

