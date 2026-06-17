# Docker Architecture — Quality Gate Checklist

> Definition of done for the `docker-architecture` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `docker-architecture` · **Category:** DevOps & Platform · **Version:** 1.0.0

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

- [ ] Addressed: base-image selection (distroless/slim) and pinning
- [ ] Addressed: multi-stage builds and layer/cache optimization
- [ ] Addressed: non-root, least-privilege, and image hardening
- [ ] Addressed: image scanning, SBOM, and signing
- [ ] Addressed: tagging, registry, and reproducibility

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: running as root in the container
- [ ] Confirmed avoided: huge images from single-stage builds and dev deps
- [ ] Confirmed avoided: mutable `latest` tags with no provenance
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Dockerfile standards and base-image policy
- [ ] Produced: Image build/scan/sign pipeline
- [ ] Produced: Tagging and registry conventions
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
