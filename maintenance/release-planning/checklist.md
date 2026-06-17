# Release Planning — Quality Gate Checklist

> Definition of done for the `release-planning` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `release-planning` · **Category:** Maintenance & Operations · **Version:** 1.0.0

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

- [ ] Addressed: release scope, versioning (semver), and changelog
- [ ] Addressed: release process and approval gates
- [ ] Addressed: deployment strategy and feature flagging
- [ ] Addressed: communication, release notes, and stakeholder sign-off
- [ ] Addressed: rollback criteria and post-release verification

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: big, infrequent releases that bundle high risk
- [ ] Confirmed avoided: no clear rollback criteria or owner
- [ ] Confirmed avoided: surprising users/stakeholders with unannounced changes
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Release plan and checklist
- [ ] Produced: Versioning and changelog
- [ ] Produced: Rollback and comms plan
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
