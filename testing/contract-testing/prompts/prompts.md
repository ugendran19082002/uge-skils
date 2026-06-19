# Contract Testing — Prompts

Copy-paste prompts to drive the `contract-testing` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in contract testing. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Consumer-driven contract definition (what each consumer actually uses)
- Provider verification against all consumer contracts in CI
- Contract broker/registry for sharing and versioning contracts
- API and message/event contract coverage (sync and async)
- Backward/forward compatibility and can-i-deploy gating
- Contract evolution, versioning, and deprecation workflow
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Contract Testing spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of contract testing. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Contract Testing artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Relying on slow, flaky end-to-end tests instead of contracts
- Provider-defined contracts that ignore what consumers truly use
- Contracts not verified in CI, so they drift from reality
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Contract Testing artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
