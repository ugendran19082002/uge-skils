# Business Analysis — Prompts

Copy-paste prompts to drive the `business-analysis` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in business analysis. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Stakeholder identification and elicitation (interviews, workshops, observation)
- Current-state (as-is) vs target-state (to-be) process modeling
- Problem framing, root-cause analysis, and value quantification
- Business capability and gap analysis
- Success metrics and KPI definition tied to business outcomes
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Business Analysis spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of business analysis. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Business Analysis artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Jumping to solutions before the problem is understood
- Confusing outputs (features shipped) with outcomes (value delivered)
- Eliciting from one loud stakeholder and missing the silent majority
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Business Analysis artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
