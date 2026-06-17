# File Storage Design — Prompts

Copy-paste prompts to drive the `file-storage-design` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in file storage design. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Storage backend selection (object store, CDN, tiers)
- Upload/download flow with pre-signed URLs
- Access control, encryption, and virus scanning
- Media processing (resize/transcode) pipeline
- Lifecycle, retention, versioning, and cost tiering
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable File Storage Design spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of file storage design. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the File Storage Design artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Storing large blobs in the relational database
- Public buckets / unsigned access to private files
- No retention policy — storage and cost grow forever
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the File Storage Design artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
