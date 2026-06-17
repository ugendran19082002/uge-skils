# Architecture Review — Quality Gate Checklist

> Definition of done for the `architecture-review` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `architecture-review` · **Category:** Architecture · **Version:** 1.0.0

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

- [ ] Addressed: quality-attribute scenario evaluation (ATAM-style)
- [ ] Addressed: risk, sensitivity, and trade-off point identification
- [ ] Addressed: fitness-function and constraint checking
- [ ] Addressed: tech-debt and coupling assessment
- [ ] Addressed: compliance with reference architecture and standards

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: opinion-based review with no quality-attribute scenarios
- [ ] Confirmed avoided: reviewing the diagram, not the running system's reality
- [ ] Confirmed avoided: findings with no severity, owner, or remediation
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Architecture review report with findings and severity
- [ ] Produced: Risk and trade-off log
- [ ] Produced: Prioritized remediation recommendations
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
