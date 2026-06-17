# Infrastructure as Code — Prompts

Copy-paste prompts to drive the `infrastructure-as-code` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in infrastructure as code. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Tool/approach (Terraform, Pulumi, CloudFormation) and structure
- Module design, reuse, and DRY composition
- State management, locking, and drift detection
- Environment separation and promotion
- Policy-as-code, plan review, and CI/CD integration
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Infrastructure as Code spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of infrastructure as code. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Infrastructure as Code artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- Manual changes that cause state drift
- Copy-paste per environment instead of modules
- Applying without reviewing the plan
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Infrastructure as Code artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
