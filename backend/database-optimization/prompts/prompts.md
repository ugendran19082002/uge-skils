# Database Optimization — Prompts

Copy-paste prompts to drive the `database-optimization` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in database optimization. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Slow-query identification and EXPLAIN plan analysis
- Index design, covering indexes, and index hygiene
- Query rewriting and N+1 elimination
- Connection pooling, caching, and read replicas
- Partitioning, vacuum/stats, and configuration tuning
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Database Optimization spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of database optimization. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Database Optimization artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Adding indexes blindly without checking plans
- Optimizing queries that aren't the bottleneck
- Fixing symptoms in app code instead of the query/schema
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Database Optimization artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
