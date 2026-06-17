# Prompt Engineering — Prompts

Copy-paste prompts to drive the `prompt-engineering` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in prompt engineering. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Prompt structure (role, instructions, context, examples, format)
- Few-shot, chain-of-thought, and decomposition techniques
- Output formatting (JSON/schema) and parsing robustness
- Prompt versioning, testing, and regression evals
- Injection resistance and failure handling
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Prompt Engineering spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of prompt engineering. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Prompt Engineering artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Untracked prompt strings edited live in production
- No eval set — 'it looked better' tuning
- Trusting model output format without validation
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Prompt Engineering artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
