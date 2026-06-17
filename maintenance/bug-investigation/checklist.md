# Bug Investigation — Quality Gate Checklist

> Definition of done for the `bug-investigation` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `bug-investigation` · **Category:** Maintenance & Operations · **Version:** 1.0.0

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

- [ ] Addressed: reliable reproduction and minimal test case
- [ ] Addressed: root-cause analysis (5 whys, bisection, debugging)
- [ ] Addressed: impact/blast-radius and severity assessment
- [ ] Addressed: fix design with regression test
- [ ] Addressed: related-defect search and prevention

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: patching the stack trace location, not the cause
- [ ] Confirmed avoided: no regression test — the bug silently returns
- [ ] Confirmed avoided: not checking whether the same bug exists elsewhere
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Bug report with confirmed root cause
- [ ] Produced: Fix plus regression test
- [ ] Produced: Prevention/related-issue notes
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
