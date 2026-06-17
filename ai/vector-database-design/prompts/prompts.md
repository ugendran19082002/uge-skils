# Vector Database Design — Prompts

Copy-paste prompts to drive the `vector-database-design` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in vector database design. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Vector store selection and deployment model
- Index type (HNSW, IVF, etc.) and parameter tuning
- Distance metric and embedding dimensionality
- Metadata filtering and hybrid search
- Recall/latency trade-offs, sharding, and scaling
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Vector Database Design spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of vector database design. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Vector Database Design artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Default index params without recall/latency testing
- Mismatched distance metric vs embedding model
- Ignoring metadata filtering and re-indexing cost
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Vector Database Design artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
