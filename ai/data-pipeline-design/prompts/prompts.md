# Data Pipeline Design — Prompts

Copy-paste prompts to drive the `data-pipeline-design` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in data pipeline design. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Source/sink inventory and the batch vs streaming decision
- Pipeline stages: ingest/extract, validate, transform, load (ETL/ELT)
- Schema management, source contracts, and schema-drift handling
- Data-quality checks, deduplication, and idempotent/exactly-once processing
- Orchestration, scheduling, dependencies, and backfills
- Lineage, freshness SLAs, observability, and failure recovery/replay
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Data Pipeline Design spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of data pipeline design. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Data Pipeline Design artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Pipelines with no data-quality checks that propagate corruption downstream
- Non-idempotent loads that double-count on retry or backfill
- No schema-drift handling, so an upstream change breaks the pipeline silently
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Data Pipeline Design artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
