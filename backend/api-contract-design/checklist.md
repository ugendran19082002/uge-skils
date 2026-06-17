# API Contract Design — Quality Gate Checklist

> Definition of done for the `api-contract-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `api-contract-design` · **Category:** Backend · **Version:** 1.0.0

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

- [ ] Addressed: contract-first authoring (OpenAPI / Protobuf / GraphQL SDL)
- [ ] Addressed: schema validation and codegen for clients/servers
- [ ] Addressed: backward/forward compatibility and breaking-change detection
- [ ] Addressed: contract testing (consumer-driven) and mocking
- [ ] Addressed: versioning, deprecation, and changelog discipline

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: code-first with the contract reverse-engineered after
- [ ] Confirmed avoided: merging breaking changes with no automated detection
- [ ] Confirmed avoided: contracts that drift from the running implementation
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Versioned contract artifact in the registry
- [ ] Produced: Compatibility/linting CI checks
- [ ] Produced: Consumer-driven contract tests
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
