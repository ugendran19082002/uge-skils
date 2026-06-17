# Frontend Architecture — Quality Gate Checklist

> Definition of done for the `frontend-architecture` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `frontend-architecture` · **Category:** Architecture · **Version:** 1.0.0

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

- [ ] Addressed: rendering strategy (SPA, SSR, SSG, ISR, islands) selection
- [ ] Addressed: module/feature boundaries and folder architecture
- [ ] Addressed: state and data-fetching architecture
- [ ] Addressed: design-system and component-library integration
- [ ] Addressed: build, bundling, code-splitting, and performance budgets

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: choosing SSR/SPA by trend rather than requirements
- [ ] Confirmed avoided: global mutable state as the default for everything
- [ ] Confirmed avoided: no performance budget — bundle size grows unchecked
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Frontend architecture document
- [ ] Produced: Module boundary and dependency rules
- [ ] Produced: Rendering and data-fetching decision record
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
