# Feature Flag Management — Prompts

Copy-paste prompts to drive the `feature-flag-management` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in feature flag management. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Flag types (release, ops, experiment, permission) and lifecycle
- Targeting, segmentation, and gradual/percentage rollout
- Kill switches, defaults, and fail-safe evaluation
- Experimentation/A-B integration and metrics
- Flag debt: ownership, expiry, and systematic cleanup
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Feature Flag Management spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of feature flag management. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Feature Flag Management artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Flags that never get removed — permanent dead branches
- No default/fail-safe when the flag service is down
- Testing only one side of the flag
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Feature Flag Management artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
