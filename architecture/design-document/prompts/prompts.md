# Design Document — Prompts

Copy-paste prompts to drive the `design-document` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in design document. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Context, problem statement, and goals/non-goals
- Proposed design with diagrams (C4, sequence, data flow)
- Alternatives considered and why rejected
- Cross-cutting concerns (security, scaling, observability, cost)
- Rollout, migration, and testing strategy
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Design Document spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of design document. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Design Document artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Describing the solution without the alternatives or trade-offs
- Diagrams that don't match the prose
- No non-goals, so review scope creeps endlessly
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Design Document artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
