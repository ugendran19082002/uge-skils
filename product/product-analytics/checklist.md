# Product Analytics — Quality Gate Checklist

> Definition of done for the `product-analytics` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `product-analytics` · **Category:** Product · **Version:** 1.0.0

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

- [ ] Addressed: tracking plan: events, properties, naming conventions, and ownership
- [ ] Addressed: north-star and funnel/retention/cohort metric design
- [ ] Addressed: client vs server-side instrumentation and identity resolution
- [ ] Addressed: privacy, consent, and PII minimization in analytics
- [ ] Addressed: data quality, validation, and governance of the event stream

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: tracking everything 'just in case' — unusable, costly noise
- [ ] Confirmed avoided: inconsistent event names that break analysis
- [ ] Confirmed avoided: capturing PII without consent or minimization
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Versioned tracking plan with event schema
- [ ] Produced: Funnel, retention, and activation metric definitions
- [ ] Produced: Instrumentation + QA checklist for events
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
