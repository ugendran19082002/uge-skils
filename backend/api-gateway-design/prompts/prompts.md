# API Gateway Design — Prompts

Copy-paste prompts to drive the `api-gateway-design` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in api gateway design. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Routing, aggregation, and protocol translation (REST/gRPC/GraphQL)
- Edge authn/authz, key management, and token validation
- Rate limiting, quotas, throttling, and circuit breaking
- Versioning, canary routing, and request/response transformation
- Edge observability, tracing propagation, and WAF integration
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable API Gateway Design spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of api gateway design. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the API Gateway Design artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Putting business logic in the gateway — a new monolith
- No rate limiting — one client can starve the rest
- Breaking clients with unversioned routing changes
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the API Gateway Design artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
