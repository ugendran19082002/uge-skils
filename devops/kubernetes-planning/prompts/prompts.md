# Kubernetes Planning — Prompts

Copy-paste prompts to drive the `kubernetes-planning` skill with an AI assistant or to
structure a working session. Replace `<...>` placeholders with your context.

> Tip: feed the matching template from [`templates/`](./templates/) alongside the
> prompt so the output lands in the right structure.

### Discover

```
You are an expert in kubernetes planning. Given this context:
<context>
...
</context>
Identify the goals, constraints, stakeholders, success criteria, and key unknowns. Pay particular attention to these focus areas:
- Workload modeling (Deployments/StatefulSets/Jobs) and resources
- Networking, ingress, and service mesh decisions
- Autoscaling (HPA/VPA/cluster) and capacity
- Security (RBAC, network policies, pod security, secrets)
- GitOps, observability, and upgrade strategy
List what you still need to know before proceeding.
```

### Specify

```
Using the discovered context, draft a reviewable Kubernetes Planning spec following the provided template. Cover every focus area, and state scope, non-goals, assumptions, and objective acceptance criteria.
```

### Design & decide

```
Propose 2-3 viable approaches for <decision> in the context of kubernetes planning. For each give pros, cons, cost, and risk. Recommend one and write it up as an ADR with the rejected options recorded.
```

### Validate (anti-pattern check)

```
Review the Kubernetes Planning artifact against its checklist. For each gate mark pass/fail/waived and justify. Then explicitly confirm none of these anti-patterns are present:
- No resource requests/limits — noisy neighbors and OOMs
- Cluster-admin RBAC handed out broadly
- Treating k8s as a goal rather than a fit-for-purpose tool
List the top risks and a mitigation for each.
```

### Deliver

```
Finalize the Kubernetes Planning artifact: confirm all deliverables exist, assign an owner and review cadence, store it in the spec registry, and draft the handoff/communication note to stakeholders.
```

## Chaining

Run the prompts in lifecycle order — Discover → Specify → Design → Validate →
Deliver — passing each phase's output into the next. Validate every output
against [`checklist.md`](./checklist.md).
