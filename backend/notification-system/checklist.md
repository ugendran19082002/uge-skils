# Notification System — Quality Gate Checklist

> Definition of done for the `notification-system` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `notification-system` · **Category:** Backend · **Version:** 1.0.0

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

- [ ] Addressed: channel strategy (email, push, SMS, in-app) and provider selection
- [ ] Addressed: template/content management, localization, and personalization
- [ ] Addressed: user preferences, consent, quiet hours, and unsubscribe
- [ ] Addressed: delivery reliability: queues, retries, idempotency, dedup
- [ ] Addressed: deliverability, rate limiting, batching, and digesting

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: sending duplicate or storm notifications on retries
- [ ] Confirmed avoided: ignoring user preferences, consent, and quiet hours
- [ ] Confirmed avoided: no deliverability handling — landing in spam
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Notification architecture and channel routing design
- [ ] Produced: Preference/consent model and template system
- [ ] Produced: Delivery reliability and rate-limit plan
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
