# Risk Analysis — Prompts

Copy-paste prompts to drive the `risk-analysis` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in risk analysis. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Risk identification (technical, schedule, resource, market, compliance)
- Qualitative and quantitative scoring (probability × impact)
- Risk response strategies (avoid, mitigate, transfer, accept)
- Risk register ownership and monitoring
- Assumption and dependency risk tracking
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Risk Analysis spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of risk analysis. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Risk Analysis artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- A risk register written once and never revisited
- Risks with no owner and no trigger condition
- Scoring theatre — numbers with no action attached
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Risk Analysis artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
