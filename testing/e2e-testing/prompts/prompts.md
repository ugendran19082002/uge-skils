# End-to-End Testing — Prompts

Copy-paste prompts to drive the `e2e-testing` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in end-to-end testing. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Critical user-journey selection
- Stable selectors and resilient locators
- Test data, environment, and state management
- Flake reduction (waits, retries, isolation)
- Cross-browser/device and CI/parallelization
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable End-to-End Testing spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of end-to-end testing. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the End-to-End Testing artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- E2E-testing everything instead of critical paths
- Brittle selectors (CSS/text) that break on UI tweaks
- Tolerating flaky e2e that erode trust in the suite
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the End-to-End Testing artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
