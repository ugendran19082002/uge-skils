# Kubernetes Planning — Quality Gate Checklist

> Definition of done for the `kubernetes-planning` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `kubernetes-planning` · **Category:** DevOps & Platform · **Version:** 1.0.0

## Discover

- [ ] Problem statement and success criteria are written down
- [ ] Stakeholders and their concerns are identified
- [ ] Constraints (time, budget, tech, compliance) are explicit
- [ ] Existing artifacts reviewed for reuse

## Specify

- [ ] Intended outcome captured as a reviewable spec
- [ ] Scope and non-goals stated
- [ ] Assumptions and open questions listed

## Design — domain coverage

- [ ] Addressed: workload modeling (Deployments/StatefulSets/Jobs) and resources
- [ ] Addressed: networking, ingress, and service mesh decisions
- [ ] Addressed: autoscaling (HPA/VPA/cluster) and capacity
- [ ] Addressed: security (RBAC, network policies, pod security, secrets)
- [ ] Addressed: gitOps, observability, and upgrade strategy

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: no resource requests/limits — noisy neighbors and OOMs
- [ ] Confirmed avoided: cluster-admin RBAC handed out broadly
- [ ] Confirmed avoided: treating k8s as a goal rather than a fit-for-purpose tool
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Kubernetes platform plan
- [ ] Produced: Resource/scaling and security model
- [ ] Produced: GitOps and operations plan
- [ ] Final artifact stored in the spec registry
- [ ] Owner and review cadence assigned
- [ ] Handoff / communication done

## Sign-off

- [ ] All gates above checked or waived (with reason recorded)
- [ ] Artifact peer-reviewed by at least one other person
- [ ] Decisions/trade-offs captured (ADR or decision log)
- [ ] Owner and review cadence assigned
- [ ] Linked from the project's spec index / `openspec/` registry

| Role | Name | Date |
|------|------|------|
| Author | | |
| Reviewer | | |
| Approver | | |
