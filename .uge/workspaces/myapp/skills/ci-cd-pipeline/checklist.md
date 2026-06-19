# CI/CD Pipeline — Quality Gate Checklist

> Definition of done for the `ci-cd-pipeline` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `ci-cd-pipeline` · **Category:** DevOps & Platform · **Version:** 1.0.0

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

- [ ] Addressed: pipeline stages (build, test, scan, package, deploy)
- [ ] Addressed: quality and security gates (lint, tests, SAST, SCA)
- [ ] Addressed: artifact management and environment promotion
- [ ] Addressed: deployment strategies (blue-green, canary, rollback)
- [ ] Addressed: pipeline speed, caching, and observability

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: deploying without automated rollback
- [ ] Confirmed avoided: gates so slow developers bypass them
- [ ] Confirmed avoided: secrets exposed in pipeline logs/config
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: CI/CD pipeline design and config
- [ ] Produced: Quality/security gate definitions
- [ ] Produced: Deployment and rollback strategy
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
