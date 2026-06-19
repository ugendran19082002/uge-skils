# Realtime Architecture — Quality Gate Checklist

> Definition of done for the `realtime-architecture` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `realtime-architecture` · **Category:** Architecture · **Version:** 1.0.0

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

- [ ] Addressed: transport choice: WebSocket vs SSE vs long-poll vs WebTransport
- [ ] Addressed: fan-out and pub/sub topology, presence, and connection state
- [ ] Addressed: ordering, delivery guarantees, backpressure, and reconnection
- [ ] Addressed: horizontal scaling of stateful connections and sticky routing
- [ ] Addressed: authn/authz on persistent connections and message authorization

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: assuming sockets scale like stateless HTTP
- [ ] Confirmed avoided: no reconnection/replay strategy — clients silently drift
- [ ] Confirmed avoided: broadcasting to everyone instead of scoped channels
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Realtime transport and topology decision (ADR)
- [ ] Produced: Delivery-guarantee and reconnection/backpressure plan
- [ ] Produced: Scaling and connection-state design
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
