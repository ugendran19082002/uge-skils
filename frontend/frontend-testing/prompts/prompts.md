# Frontend Testing — Prompts

Copy-paste prompts to drive the `frontend-testing` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in frontend testing. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Test pyramid for the frontend and what each layer owns
- Component testing with user-centric queries
- Mocking the network at the boundary and test-data strategy
- Visual-regression and accessibility testing
- Flake control, determinism, and CI integration
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Frontend Testing spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of frontend testing. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Frontend Testing artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Testing implementation details that break on refactor
- An inverted pyramid — slow e2e for everything
- Tolerating flaky tests instead of fixing them
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Frontend Testing artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
