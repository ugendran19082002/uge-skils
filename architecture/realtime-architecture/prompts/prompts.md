# Realtime Architecture — Prompts

Copy-paste prompts to drive the `realtime-architecture` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in realtime architecture. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Transport choice: WebSocket vs SSE vs long-poll vs WebTransport
- Fan-out and pub/sub topology, presence, and connection state
- Ordering, delivery guarantees, backpressure, and reconnection
- Horizontal scaling of stateful connections and sticky routing
- Authn/authz on persistent connections and message authorization
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Realtime Architecture spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of realtime architecture. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Realtime Architecture artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Assuming sockets scale like stateless HTTP
- No reconnection/replay strategy — clients silently drift
- Broadcasting to everyone instead of scoped channels
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Realtime Architecture artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
