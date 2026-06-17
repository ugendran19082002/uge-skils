# Accessibility Review — Quality Gate Checklist

> Definition of done for the `accessibility-review` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `accessibility-review` · **Category:** Frontend · **Version:** 1.0.0

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

- [ ] Addressed: WCAG 2.2 AA conformance auditing
- [ ] Addressed: keyboard, focus order, and screen-reader testing
- [ ] Addressed: color contrast, target size, and motion preferences
- [ ] Addressed: semantic HTML and ARIA correctness
- [ ] Addressed: automated + manual + assistive-tech testing

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: relying only on automated scanners (catch ~30%)
- [ ] Confirmed avoided: ARIA-over-HTML — reinventing native semantics badly
- [ ] Confirmed avoided: treating a11y as a one-off audit, not a standard
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Accessibility audit report (issues by WCAG criterion)
- [ ] Produced: Prioritized remediation backlog
- [ ] Produced: Conformance statement (VPAT-style)
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
