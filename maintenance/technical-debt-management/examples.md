# Technical Debt Management — Worked Examples

Realistic, end-to-end walkthroughs of the `technical-debt-management` skill. Each example
follows the OpenSpec phases (Discover → Specify → Design → Validate → Deliver).

## Example 1: Applying Technical Debt Management on a greenfield feature

**Context.** A team is starting new work and needs technical debt management done properly the first time.

**Applying the skill.**

1. Discover: gather context, constraints, and success criteria from stakeholders.
2. Specify: write the outcome as a reviewable spec using the template.
3. Design: weigh two approaches and record the choice as an ADR.
4. Validate: check against the quality gates and get a peer review.
5. Deliver: store the artifact, assign an owner, and communicate.

**Outcome.** A reviewed, owned artifact that the team builds on with confidence.

---

## Example 2: Applying Technical Debt Management to an existing system

**Context.** An established system needs technical debt management retrofitted to reduce risk.

**Applying the skill.**

1. Discover: inventory the current state and pain points.
2. Specify: capture the target state and the gap.
3. Design: plan an incremental path that avoids a big-bang change.
4. Validate: confirm each step is independently shippable and safe.
5. Deliver: sequence the work and define rollback.

**Outcome.** A low-risk, incremental plan with clear checkpoints.

---

## How to reuse these

1. Pick the example closest to your situation.
2. Copy the matching template from [`templates/`](./templates/).
3. Drive each phase with the prompts in [`prompts/prompts.md`](./prompts/prompts.md).
4. Verify against [`checklist.md`](./checklist.md) before sign-off.
