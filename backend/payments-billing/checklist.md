# Payments & Billing — Quality Gate Checklist

> Definition of done for the `payments-billing` skill. Every applicable item must be
> checked, or waived with a one-line recorded reason. Unchecked, unwaived items
> block delivery.

**Skill:** `payments-billing` · **Category:** Backend · **Version:** 1.0.0

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

- [ ] Addressed: provider integration (Stripe/Adyen/etc.) and PCI scope minimization
- [ ] Addressed: subscription, metering, proration, tax, and invoicing models
- [ ] Addressed: idempotency, webhooks, retries, and reconciliation
- [ ] Addressed: dunning, refunds, chargebacks, and revenue recognition
- [ ] Addressed: ledger design, auditability, and money/currency precision

## Validate — anti-patterns avoided

- [ ] Confirmed avoided: storing card data and expanding PCI scope needlessly
- [ ] Confirmed avoided: floating-point money or missing currency precision
- [ ] Confirmed avoided: non-idempotent payment handlers — double charges
- [ ] Spec is testable — acceptance criteria are objective
- [ ] Reviewed by domain expert(s)
- [ ] Risks identified with mitigations

## Deliver — artifacts

- [ ] Produced: Billing/subscription data model and ledger design
- [ ] Produced: Provider integration + webhook/idempotency plan
- [ ] Produced: Reconciliation, refund, and dunning runbook
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
