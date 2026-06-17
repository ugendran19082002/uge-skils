# AI Agent Design — Prompts

Copy-paste prompts to drive the `ai-agent-design` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in ai agent design. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Task scoping, success criteria, and stop conditions
- Tool/function definitions and permissioning
- Control flow (single-shot, ReAct, planner-executor, multi-agent)
- Memory, context management, and state
- Guardrails, human-in-the-loop, and failure handling
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable AI Agent Design spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of ai agent design. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the AI Agent Design artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Giving an agent powerful tools with no permission scoping
- No stop conditions — runaway loops and cost
- Demo-driven design with no eval of real task success
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the AI Agent Design artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
