# Docker Compose Design — Quality Gate Checklist

> Definition of done for the `docker-compose-design` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `docker-compose-design` · **Category:** DevOps & Platform · **Version:** 1.0.0

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

- [ ] Addressed: service composition, dependencies, and healthchecks
- [ ] Addressed: networks, volumes, and data persistence
- [ ] Addressed: environment/config and secret handling
- [ ] Addressed: resource limits and restart policies
- [ ] Addressed: dev/prod parity and override files

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: secrets hardcoded in the compose file
- [ ] Confirmed avoided: no healthchecks — `depends_on` races at startup
- [ ] Confirmed avoided: dev compose drifting far from production reality
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Compose stack with healthchecks and limits
- [ ] Produced: Network/volume/secret layout
- [ ] Produced: Override strategy for environments
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
