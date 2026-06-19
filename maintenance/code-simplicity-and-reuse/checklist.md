# Code Simplicity & Reuse — Quality Gate Checklist

> Definition of done for the `code-simplicity-and-reuse` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `code-simplicity-and-reuse` · **Category:** Maintenance & Operations · **Version:** 1.0.0

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

- [ ] Addressed: reuse-first: search the codebase, standard library, and existing modules before writing new code (DRY)
- [ ] Addressed: YAGNI: build only what a current, real requirement needs — defer the speculative
- [ ] Addressed: KISS: choose the simplest design that meets the requirement; treat any added complexity as something to justify
- [ ] Addressed: right abstraction timing: tolerate duplication until the shared concept is proven (rule of three) — a wrong abstraction costs more than repetition
- [ ] Addressed: subtract: remove dead code, redundant layers, needless configuration, and unused flags
- [ ] Addressed: readability over cleverness: optimize for the next reader, not for fewer lines or a trick

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: copy-pasting logic into a third place instead of extracting it
- [ ] Confirmed avoided: adding abstraction or configuration for an imagined future requirement
- [ ] Confirmed avoided: choosing a clever solution over a clear one
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Simplicity & reuse review notes (what was reused, simplified, or deleted, with rationale)
- [ ] Produced: A short project simplicity guideline (the codebase's DRY/KISS/YAGNI rules)
- [ ] Produced: A reuse index of shared utilities and where to find them
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
