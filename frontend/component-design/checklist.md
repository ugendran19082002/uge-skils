# Component Design — Quality Gate Checklist

> Definition of done for the `component-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `component-design` · **Category:** Frontend · **Version:** 1.0.0

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

- [ ] Addressed: component API (props/events/slots) and composition model
- [ ] Addressed: state, variant, and interaction matrix
- [ ] Addressed: accessibility (roles, keyboard, focus, ARIA)
- [ ] Addressed: theming, tokens, and style encapsulation
- [ ] Addressed: stories, docs, and visual-regression coverage

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: over-configurable components with 30 boolean props
- [ ] Confirmed avoided: components that hard-code spacing/colors instead of tokens
- [ ] Confirmed avoided: skipping keyboard/focus handling
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Component spec with API and states
- [ ] Produced: Accessibility and interaction checklist
- [ ] Produced: Stories/docs and tests
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
