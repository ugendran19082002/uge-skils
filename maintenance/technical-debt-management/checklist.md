# Technical Debt Management — Quality Gate Checklist

> Definition of done for the `technical-debt-management` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `technical-debt-management` · **Category:** Maintenance & Operations · **Version:** 1.0.0

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

- [ ] Addressed: debt inventory, classification, and tagging
- [ ] Addressed: cost/risk/interest quantification
- [ ] Addressed: prioritization (impact vs effort, hotspots)
- [ ] Addressed: paydown budgeting and the boy-scout rule
- [ ] Addressed: prevention, standards, and tracking

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: debt that's invisible because it's never written down
- [ ] Confirmed avoided: either ignoring debt or stop-the-world rewrites
- [ ] Confirmed avoided: no paydown budget — debt only ever grows
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Technical debt register with impact/effort
- [ ] Produced: Prioritized paydown plan and budget
- [ ] Produced: Prevention guidelines
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
