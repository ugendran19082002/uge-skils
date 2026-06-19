# CI/CD Pipeline — Prompts

Copy-paste prompts to drive the `ci-cd-pipeline` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in ci/cd pipeline. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Pipeline stages (build, test, scan, package, deploy)
- Quality and security gates (lint, tests, SAST, SCA)
- Artifact management and environment promotion
- Deployment strategies (blue-green, canary, rollback)
- Pipeline speed, caching, and observability
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable CI/CD Pipeline spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of ci/cd pipeline. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the CI/CD Pipeline artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Deploying without automated rollback
- Gates so slow developers bypass them
- Secrets exposed in pipeline logs/config
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the CI/CD Pipeline artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
