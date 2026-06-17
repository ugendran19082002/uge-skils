# Infrastructure Design — Quality Gate Checklist

> Definition of done for the `infra-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `infra-design` · **Category:** DevOps & Platform · **Version:** 1.0.0

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

- [ ] Addressed: environment topology (dev/stage/prod) and isolation
- [ ] Addressed: networking (VPC, subnets, routing, ingress/egress)
- [ ] Addressed: compute/storage selection and right-sizing
- [ ] Addressed: high availability, multi-AZ/region, and DR posture
- [ ] Addressed: cost modeling, tagging, and infrastructure-as-code

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: click-ops infrastructure with no IaC or reproducibility
- [ ] Confirmed avoided: flat network with no segmentation
- [ ] Confirmed avoided: no cost model — surprise cloud bills
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Infrastructure design document and diagram
- [ ] Produced: Environment and network topology
- [ ] Produced: Cost and HA/DR plan
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
