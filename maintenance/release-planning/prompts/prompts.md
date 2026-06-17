# Release Planning — Prompts

Copy-paste prompts to drive the `release-planning` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in release planning. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Release scope, versioning (semver), and changelog
- Release process and approval gates
- Deployment strategy and feature flagging
- Communication, release notes, and stakeholder sign-off
- Rollback criteria and post-release verification
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Release Planning spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of release planning. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Release Planning artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Big, infrequent releases that bundle high risk
- No clear rollback criteria or owner
- Surprising users/stakeholders with unannounced changes
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Release Planning artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
