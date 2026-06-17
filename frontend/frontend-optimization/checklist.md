# Frontend Optimization — Quality Gate Checklist

> Definition of done for the `frontend-optimization` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `frontend-optimization` · **Category:** Frontend · **Version:** 1.0.0

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

- [ ] Addressed: core Web Vitals (LCP, INP, CLS) measurement and budgets
- [ ] Addressed: bundle analysis, code-splitting, and tree-shaking
- [ ] Addressed: image/font optimization and resource hints
- [ ] Addressed: rendering/runtime perf (virtualization, memoization)
- [ ] Addressed: caching, CDN, and network optimization

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: optimizing without measuring first
- [ ] Confirmed avoided: micro-optimizing JS while shipping a 4 MB hero image
- [ ] Confirmed avoided: no budget — gains regress silently next release
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Performance budget and baseline
- [ ] Produced: Optimization backlog ranked by impact
- [ ] Produced: Before/after measurements
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
