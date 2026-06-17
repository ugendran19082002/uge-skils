# Service Design — Prompts

Copy-paste prompts to drive the `service-design` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in service design. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Single-responsibility boundary and public contract
- Data ownership and persistence choice
- Dependency, timeout, retry, and circuit-breaker policy
- Idempotency, concurrency, and consistency handling
- Observability, health checks, and SLOs
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Service Design spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of service design. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Service Design artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- A service that owns no data and just forwards calls
- No timeouts/retries — one slow dependency cascades
- No health checks or SLOs to operate against
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Service Design artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
