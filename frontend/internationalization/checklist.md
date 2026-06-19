# Internationalization & Localization — Quality Gate Checklist

> Definition of done for the `internationalization` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `internationalization` · **Category:** Frontend · **Version:** 1.0.0

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

- [ ] Addressed: locale strategy, fallback chains, and language negotiation
- [ ] Addressed: externalized strings, ICU message format, and pluralization
- [ ] Addressed: date/number/currency formatting and time zones
- [ ] Addressed: right-to-left layout, bidi text, and locale-aware UI
- [ ] Addressed: translation workflow, TMS integration, and pseudo-localization

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: concatenating translated strings — grammatically broken
- [ ] Confirmed avoided: hardcoding date/number/currency formats
- [ ] Confirmed avoided: ignoring RTL and text-expansion until launch
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: i18n architecture and locale strategy
- [ ] Produced: Translation/extraction workflow and catalog format
- [ ] Produced: RTL and formatting test checklist
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
