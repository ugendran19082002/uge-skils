# Architecture Review — Prompts

Copy-paste prompts to drive the `architecture-review` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in architecture review. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Quality-attribute scenario evaluation (ATAM-style)
- Risk, sensitivity, and trade-off point identification
- Fitness-function and constraint checking
- Tech-debt and coupling assessment
- Compliance with reference architecture and standards
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Architecture Review spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of architecture review. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Architecture Review artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Opinion-based review with no quality-attribute scenarios
- Reviewing the diagram, not the running system's reality
- Findings with no severity, owner, or remediation
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Architecture Review artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
