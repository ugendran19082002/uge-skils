# Contract Testing — Quality Gate Checklist

> Definition of done for the `contract-testing` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `contract-testing` · **Category:** Testing & Quality · **Version:** 1.0.0

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

- [ ] Addressed: consumer-driven contract definition (what each consumer actually uses)
- [ ] Addressed: provider verification against all consumer contracts in CI
- [ ] Addressed: contract broker/registry for sharing and versioning contracts
- [ ] Addressed: API and message/event contract coverage (sync and async)
- [ ] Addressed: backward/forward compatibility and can-i-deploy gating
- [ ] Addressed: contract evolution, versioning, and deprecation workflow

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: relying on slow, flaky end-to-end tests instead of contracts
- [ ] Confirmed avoided: provider-defined contracts that ignore what consumers truly use
- [ ] Confirmed avoided: contracts not verified in CI, so they drift from reality
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Consumer-driven contracts per consumer/provider pair
- [ ] Produced: Provider verification in CI with a can-i-deploy gate
- [ ] Produced: Contract broker/registry setup and versioning policy
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
