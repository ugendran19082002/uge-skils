# API Design — Quality Gate Checklist

> Definition of done for the `api-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `api-design` · **Category:** Architecture · **Version:** 1.0.0

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

- [ ] Addressed: resource modeling and REST/GraphQL/gRPC style selection
- [ ] Addressed: naming, pagination, filtering, and consistency conventions
- [ ] Addressed: error model, status codes, and idempotency
- [ ] Addressed: versioning and backward-compatibility strategy
- [ ] Addressed: authN/Z, rate limiting, and contract documentation (OpenAPI)

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: leaking internal data models straight to the wire
- [ ] Confirmed avoided: breaking changes without versioning or deprecation policy
- [ ] Confirmed avoided: inconsistent naming/errors across endpoints
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: API design spec / OpenAPI definition
- [ ] Produced: Error and versioning conventions
- [ ] Produced: Consumer-facing API documentation
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
