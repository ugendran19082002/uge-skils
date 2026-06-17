# Microservices Governance — Quality Gate Checklist

> Definition of done for the `microservices-governance` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `microservices-governance` · **Category:** Architecture · **Version:** 1.0.0

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

- [ ] Addressed: service ownership, catalog, and a paved-road platform
- [ ] Addressed: API/contract versioning and compatibility policy
- [ ] Addressed: cross-cutting standards (logging, tracing, health, security)
- [ ] Addressed: service maturity/readiness checklists
- [ ] Addressed: decentralized data and inter-service dependency rules

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: governance as a gatekeeping committee that slows everyone
- [ ] Confirmed avoided: no standards — every service reinvents logging/auth
- [ ] Confirmed avoided: a service catalog nobody keeps up to date
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Service standards and golden-path templates
- [ ] Produced: Service catalog with ownership
- [ ] Produced: Versioning and readiness policy
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
