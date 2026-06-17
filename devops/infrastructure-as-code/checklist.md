# Infrastructure as Code — Quality Gate Checklist

> Definition of done for the `infrastructure-as-code` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `infrastructure-as-code` · **Category:** DevOps & Platform · **Version:** 1.0.0

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

- [ ] Addressed: tool/approach (Terraform, Pulumi, CloudFormation) and structure
- [ ] Addressed: module design, reuse, and DRY composition
- [ ] Addressed: state management, locking, and drift detection
- [ ] Addressed: environment separation and promotion
- [ ] Addressed: policy-as-code, plan review, and CI/CD integration

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: manual changes that cause state drift
- [ ] Confirmed avoided: copy-paste per environment instead of modules
- [ ] Confirmed avoided: applying without reviewing the plan
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: IaC structure and module standards
- [ ] Produced: State and environment strategy
- [ ] Produced: Plan-review and policy-as-code gates
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
