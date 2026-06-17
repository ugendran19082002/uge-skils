# State Management — Prompts

Copy-paste prompts to drive the `state-management` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in state management. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- State categorization (server, URL, form, UI, global)
- Server-state caching (query libraries) vs client state
- Store design, selectors, and normalization
- Derived state and avoiding redundant sources of truth
- Performance (re-render control, memoization, splitting)
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable State Management spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of state management. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the State Management artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Putting server data in a global store and hand-syncing it
- One mega-store causing app-wide re-renders
- Duplicating the same truth in multiple places
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the State Management artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
