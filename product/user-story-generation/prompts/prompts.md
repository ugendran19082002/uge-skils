# User Story Generation — Prompts

Copy-paste prompts to drive the `user-story-generation` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in user story generation. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- INVEST-compliant story slicing
- Role-goal-benefit framing ('As a... I want... so that...')
- Acceptance criteria in Given/When/Then
- Vertical slicing and story splitting patterns
- Definition of Ready and Definition of Done
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable User Story Generation spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of user story generation. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the User Story Generation artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Horizontal slices (DB story, API story) with no user value
- Acceptance criteria that restate the title
- Epics masquerading as stories — too big to finish in a sprint
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the User Story Generation artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
