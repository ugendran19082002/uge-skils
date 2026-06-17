# Enterprise OpenSpec Skill Catalog

**78 production-ready, spec-driven skills** spanning the full software delivery lifecycle — from idea to maintenance. Each skill is an OpenSpec artifact: a reviewable, versioned, gated way of doing one thing well.

## What is an OpenSpec skill?

Each skill follows the same spec-driven lifecycle so they compose into one method:

| Phase | Intent |
|-------|--------|
| **Discover** | Establish context, constraints, and success criteria before proposing anything. |
| **Specify** | Capture the intended outcome as a reviewable spec / proposal — the source of truth. |
| **Design** | Decide the approach, record trade-offs, and document decisions (ADRs). |
| **Validate** | Prove the spec is correct, complete, and testable against the quality gates. |
| **Deliver** | Produce the final artifact, hand it off, and define how it will be maintained. |

Every skill folder contains:

```
<category>/<skill>/
  SKILL.md            # frontmatter + purpose, workflow, deliverables, anti-patterns
  checklist.md        # quality gates = definition of done
  examples.md         # worked, end-to-end examples
  templates/          # ready-to-fill domain artifacts
  prompts/prompts.md  # copy-paste prompts to drive each phase
```

## How to use a skill

1. Open the skill's `SKILL.md` and read **Purpose** and **When to Use**.
2. Work the five phases in order; do not skip one (record *why* if it has no work).
3. Copy the relevant file from `templates/` and fill it in.
4. Drive each phase with `prompts/prompts.md`.
5. Verify against `checklist.md` before sign-off — it is the definition of done.

## Catalog

### Product (9)

| Skill | What it does |
|-------|--------------|
| [`business-analysis`](product/business-analysis/SKILL.md) | Translate business problems into clear, evidence-based opportunities and requirements. |
| [`market-research`](product/market-research/SKILL.md) | Size the market, map competitors, and validate demand before committing to build. |
| [`prd-generation`](product/prd-generation/SKILL.md) | Produce a crisp Product Requirements Document that aligns teams on what and why. |
| [`requirements-analysis`](product/requirements-analysis/SKILL.md) | Elicit, analyze, specify, and validate requirements that are complete and testable. |
| [`proposal-creation`](product/proposal-creation/SKILL.md) | Craft persuasive, accurate proposals that win approval and set correct expectations. |
| [`user-story-generation`](product/user-story-generation/SKILL.md) | Write small, valuable, testable user stories with clear acceptance criteria. |
| [`risk-analysis`](product/risk-analysis/SKILL.md) | Identify, assess, and plan responses to risks before they become incidents. |
| [`cost-estimation`](product/cost-estimation/SKILL.md) | Produce defensible effort and cost estimates with explicit ranges and assumptions. |
| [`roadmap-planning`](product/roadmap-planning/SKILL.md) | Sequence outcomes over time, balancing value, dependencies, and capacity. |

### Architecture (12)

| Skill | What it does |
|-------|--------------|
| [`design-document`](architecture/design-document/SKILL.md) | Author a technical design doc that explains the what, why, and trade-offs of a solution. |
| [`architecture-review`](architecture/architecture-review/SKILL.md) | Systematically evaluate an architecture against quality attributes and risks. |
| [`frontend-architecture`](architecture/frontend-architecture/SKILL.md) | Define the structure, boundaries, and standards for a maintainable frontend. |
| [`backend-architecture`](architecture/backend-architecture/SKILL.md) | Define service boundaries, data ownership, and communication for the backend. |
| [`api-design`](architecture/api-design/SKILL.md) | Design clear, consistent, evolvable APIs that are a pleasure to consume. |
| [`database-design`](architecture/database-design/SKILL.md) | Model data for correctness, performance, and evolution. |
| [`security-architecture`](architecture/security-architecture/SKILL.md) | Design defense-in-depth security into the system from the start. |
| [`scalability-planning`](architecture/scalability-planning/SKILL.md) | Plan how the system grows with load without surprise cost or failure. |
| [`event-driven-architecture`](architecture/event-driven-architecture/SKILL.md) | Design loosely-coupled systems around events, with reliable delivery semantics. |
| [`multi-tenant-architecture`](architecture/multi-tenant-architecture/SKILL.md) | Isolate, scale, and operate many tenants safely on shared infrastructure. |
| [`domain-driven-design`](architecture/domain-driven-design/SKILL.md) | Model complex domains with bounded contexts and a shared ubiquitous language. |
| [`microservices-governance`](architecture/microservices-governance/SKILL.md) | Set the standards that keep many services consistent, observable, and safe. |

### Frontend (7)

| Skill | What it does |
|-------|--------------|
| [`ui-ux-design`](frontend/ui-ux-design/SKILL.md) | Design usable, accessible, consistent interfaces grounded in user needs. |
| [`component-design`](frontend/component-design/SKILL.md) | Design reusable, composable, well-documented UI components. |
| [`state-management`](frontend/state-management/SKILL.md) | Choose and structure client state for predictability and performance. |
| [`frontend-testing`](frontend/frontend-testing/SKILL.md) | Build a layered frontend test strategy that catches regressions cheaply. |
| [`frontend-optimization`](frontend/frontend-optimization/SKILL.md) | Improve load and runtime performance against measured budgets. |
| [`accessibility-review`](frontend/accessibility-review/SKILL.md) | Audit and remediate against WCAG so the product works for everyone. |
| [`design-system`](frontend/design-system/SKILL.md) | Build a shared system of tokens, components, and guidelines for consistency at scale. |

### Backend (8)

| Skill | What it does |
|-------|--------------|
| [`service-design`](backend/service-design/SKILL.md) | Design a single backend service with clear contracts, boundaries, and operations. |
| [`authentication-design`](backend/authentication-design/SKILL.md) | Design secure authentication and session/token handling. |
| [`database-optimization`](backend/database-optimization/SKILL.md) | Diagnose and fix database performance against real workloads. |
| [`caching-strategy`](backend/caching-strategy/SKILL.md) | Add caching that speeds things up without serving wrong data. |
| [`background-jobs`](backend/background-jobs/SKILL.md) | Design reliable async job processing with retries, idempotency, and visibility. |
| [`api-contract-design`](backend/api-contract-design/SKILL.md) | Define and govern machine-readable contracts as the source of truth. |
| [`file-storage-design`](backend/file-storage-design/SKILL.md) | Design secure, scalable storage for files and media. |
| [`search-architecture`](backend/search-architecture/SKILL.md) | Design relevant, fast, scalable search over your data. |

### AI & Data (10)

| Skill | What it does |
|-------|--------------|
| [`ai-agent-design`](ai/ai-agent-design/SKILL.md) | Design reliable LLM agents with clear tools, control flow, and guardrails. |
| [`rag-architecture`](ai/rag-architecture/SKILL.md) | Design retrieval-augmented generation that is accurate and grounded. |
| [`prompt-engineering`](ai/prompt-engineering/SKILL.md) | Design, version, and test prompts that are reliable and maintainable. |
| [`model-selection`](ai/model-selection/SKILL.md) | Choose the right model for the task on quality, cost, latency, and risk. |
| [`ai-evaluation`](ai/ai-evaluation/SKILL.md) | Build evaluation harnesses that measure AI quality objectively and repeatably. |
| [`llmops`](ai/llmops/SKILL.md) | Operate LLM applications in production with versioning, monitoring, and cost control. |
| [`vector-database-design`](ai/vector-database-design/SKILL.md) | Design vector storage and indexing for fast, accurate similarity search. |
| [`ai-monitoring`](ai/ai-monitoring/SKILL.md) | Monitor AI systems for quality, drift, safety, and cost in production. |
| [`model-finetuning`](ai/model-finetuning/SKILL.md) | Decide when and how to fine-tune, with data, method, and evaluation discipline. |
| [`guardrails-design`](ai/guardrails-design/SKILL.md) | Design input/output safety controls for AI systems. |

### Testing & Quality (6)

| Skill | What it does |
|-------|--------------|
| [`testing-strategy`](testing/testing-strategy/SKILL.md) | Define the overall test approach: levels, coverage, environments, and ownership. |
| [`unit-testing`](testing/unit-testing/SKILL.md) | Write fast, focused, maintainable unit tests with good design. |
| [`integration-testing`](testing/integration-testing/SKILL.md) | Verify components work together across real boundaries. |
| [`performance-testing`](testing/performance-testing/SKILL.md) | Validate the system meets performance and scalability targets under load. |
| [`e2e-testing`](testing/e2e-testing/SKILL.md) | Validate complete user journeys through the real system. |
| [`security-testing`](testing/security-testing/SKILL.md) | Find vulnerabilities through systematic, layered security testing. |

### DevOps & Platform (13)

| Skill | What it does |
|-------|--------------|
| [`infra-design`](devops/infra-design/SKILL.md) | Design cloud/on-prem infrastructure for reliability, security, and cost. |
| [`docker-architecture`](devops/docker-architecture/SKILL.md) | Build secure, small, reproducible container images. |
| [`docker-compose-design`](devops/docker-compose-design/SKILL.md) | Design multi-container local/edge stacks with Compose, done right. |
| [`kubernetes-planning`](devops/kubernetes-planning/SKILL.md) | Plan a Kubernetes platform: workloads, scaling, security, and operations. |
| [`nginx-reverse-proxy`](devops/nginx-reverse-proxy/SKILL.md) | Configure a robust reverse proxy: routing, TLS, caching, and limits. |
| [`ssl-management`](devops/ssl-management/SKILL.md) | Manage certificates and TLS configuration securely and automatically. |
| [`ci-cd-pipeline`](devops/ci-cd-pipeline/SKILL.md) | Design automated build-test-deploy pipelines that are fast and safe. |
| [`observability-design`](devops/observability-design/SKILL.md) | Design logs, metrics, and traces that make the system debuggable. |
| [`backup-recovery`](devops/backup-recovery/SKILL.md) | Design backups that are complete, tested, and actually restorable. |
| [`server-hardening`](devops/server-hardening/SKILL.md) | Reduce attack surface on hosts via baseline secure configuration. |
| [`secrets-management`](devops/secrets-management/SKILL.md) | Store, rotate, and access secrets securely across the lifecycle. |
| [`disaster-recovery`](devops/disaster-recovery/SKILL.md) | Plan for surviving major failures with tested recovery procedures. |
| [`infrastructure-as-code`](devops/infrastructure-as-code/SKILL.md) | Manage infrastructure declaratively, reviewed and versioned like software. |

### Security & Compliance (4)

| Skill | What it does |
|-------|--------------|
| [`threat-modeling`](security/threat-modeling/SKILL.md) | Systematically identify threats and design controls before building. |
| [`compliance-audit`](security/compliance-audit/SKILL.md) | Assess and evidence compliance against a framework (SOC2, ISO, GDPR, HIPAA). |
| [`vulnerability-management`](security/vulnerability-management/SKILL.md) | Continuously find, prioritize, and remediate vulnerabilities. |
| [`access-control-design`](security/access-control-design/SKILL.md) | Design authorization models that enforce least privilege. |

### Maintenance & Operations (9)

| Skill | What it does |
|-------|--------------|
| [`troubleshooting`](maintenance/troubleshooting/SKILL.md) | Diagnose problems methodically from symptom to root cause. |
| [`bug-investigation`](maintenance/bug-investigation/SKILL.md) | Investigate bugs to a confirmed root cause with a regression test. |
| [`refactoring-planning`](maintenance/refactoring-planning/SKILL.md) | Plan safe, incremental refactors that improve code without changing behavior. |
| [`migration-planning`](maintenance/migration-planning/SKILL.md) | Plan low-risk migrations (data, platform, version) with rollback. |
| [`release-planning`](maintenance/release-planning/SKILL.md) | Coordinate releases so changes ship predictably and safely. |
| [`documentation-generator`](maintenance/documentation-generator/SKILL.md) | Produce and maintain documentation that stays useful and current. |
| [`incident-response`](maintenance/incident-response/SKILL.md) | Respond to production incidents with structure, then learn from them. |
| [`monitoring-alerting`](maintenance/monitoring-alerting/SKILL.md) | Design alerts that fire on real, actionable problems — and nothing else. |
| [`technical-debt-management`](maintenance/technical-debt-management/SKILL.md) | Make technical debt visible, prioritized, and paid down deliberately. |

## Lifecycle map

These skills are designed to be run in sequence across a project's life:

```
Idea → market-research → business-analysis → prd-generation →
requirements-analysis → proposal-creation → user-story-generation →
design-document → frontend/backend-architecture → api-design →
database-design → security-architecture → testing-strategy →
docker-architecture → ci-cd-pipeline → observability-design →
incident-response → bug-investigation → refactoring-planning →
scalability-planning → technical-debt-management
```

## Regenerating

This catalog is generated. To change a skill, edit its definition in
`_generator/skills_data.py` and run:

```bash
python3 _generator/generate.py
```

---
*78 skills · OpenSpec spec v1.0 · Apache-2.0*
