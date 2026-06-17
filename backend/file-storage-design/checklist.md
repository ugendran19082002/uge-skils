# File Storage Design — Quality Gate Checklist

> Definition of done for the `file-storage-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `file-storage-design` · **Category:** Backend · **Version:** 1.0.0

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

- [ ] Addressed: storage backend selection (object store, CDN, tiers)
- [ ] Addressed: upload/download flow with pre-signed URLs
- [ ] Addressed: access control, encryption, and virus scanning
- [ ] Addressed: media processing (resize/transcode) pipeline
- [ ] Addressed: lifecycle, retention, versioning, and cost tiering

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: storing large blobs in the relational database
- [ ] Confirmed avoided: public buckets / unsigned access to private files
- [ ] Confirmed avoided: no retention policy — storage and cost grow forever
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: File storage design
- [ ] Produced: Access-control and signed-URL flow
- [ ] Produced: Lifecycle/retention policy
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
