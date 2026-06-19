# Market Research — Prompts

Copy-paste prompts to drive the `market-research` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in market research. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- TAM / SAM / SOM market sizing (top-down and bottom-up)
- Competitive landscape and feature/positioning matrices
- Customer segmentation, jobs-to-be-done, and demand signals
- Pricing and willingness-to-pay analysis
- Trend, regulatory, and PESTEL scanning
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Market Research spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of market research. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Market Research artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Cherry-picking data that confirms the desired conclusion
- Citing TAM without a credible bottom-up cross-check
- Treating a few customer interviews as statistically representative
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Market Research artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
