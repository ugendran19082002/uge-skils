# Migration Planning — Quality Gate Checklist

> Definition of done for the `migration-planning` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `migration-planning` · **Category:** Maintenance & Operations · **Version:** 1.0.0

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

- [ ] Addressed: scope, dependency, and compatibility assessment
- [ ] Addressed: strategy selection (big-bang, phased, parallel-run, strangler)
- [ ] Addressed: data migration, validation, and reconciliation
- [ ] Addressed: cutover plan, rollback, and contingency
- [ ] Addressed: coexistence period and decommissioning

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: big-bang cutover with no rollback path
- [ ] Confirmed avoided: no data validation/reconciliation after migration
- [ ] Confirmed avoided: decommissioning the old system before the new one is proven
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Migration plan with phases and rollback
- [ ] Produced: Data migration and validation approach
- [ ] Produced: Cutover runbook
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
