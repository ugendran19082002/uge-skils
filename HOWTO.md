# How to Use ugendran — Start to End

A simple, plain-English guide. `ugendran` turns one sentence about what you want
into real, spec-driven project artifacts — and can implement and verify them as code.

---

## 1. What this tool does (in one minute)

You describe what you want ("add Google login", "build a SaaS"). The tool:

1. **Picks the right skill** from 89 expert playbooks (api-design, rag-architecture, auth, etc.).
2. **Writes a real spec** for your project (not a blank template — filled-in content).
3. **Checks the spec** against a quality checklist (and, in OpenSpec mode, the real
   `openspec validate --strict`).
4. **Implements it as code** and **runs the build/tests** to prove it works.
5. **Archives it into living specs** so your spec set is always current.

Think of it as: **idea → spec → code → verified → recorded.**

---

## 2. Before you start (setup)

**You need:** Python 3.10+. Optional but recommended: an LLM CLI (`claude` or `gemini`)
so it can write real content. Without one, it still works in a simpler "keyword" mode.

**Check what's detected:**
```bash
python3 ugendran.py llm
```
- 🟣 Claude or 🔵 Gemini = full AI mode.
- 🟡 Keyword-Fallback = works offline, simpler output.

**Install the global command** (so you can type `ugendran` anywhere):
```bash
python3 ugendran.py install
```
After this you can use `ugendran ...` instead of `python3 ugendran.py ...`.

**For the strongest, validated mode**, also install the real OpenSpec CLI:
```bash
npm install -g @fission-ai/openspec
```

---

## 3. The everyday workflow (start to end)

### Step 1 — Create a project
```bash
ugendran new myapp "a web app where users search and save articles"
```
This creates a project called `myapp` and remembers your idea.

### Step 2 — Do one thing at a time (single skill)
```bash
ugendran do myapp "add Google login with MFA"
```
The AI picks the best skill (here: authentication-design), writes a real spec for it,
checks it against the quality checklist, and records it.

More examples:
```bash
ugendran do myapp "I need Redis caching for the API"
ugendran do myapp "design the search architecture"
ugendran do myapp "set up production CI/CD on GitHub Actions"
```

### Step 3 — Or build the whole thing at once (autonomous)
```bash
ugendran build myapp "multi-tenant SaaS with billing, auth, and search"
```
The AI plans ALL the skills your project needs, runs them in parallel waves,
self-checks each one, and archives as it goes. You get a full set of specs from one command.

**Want objective, validated specs?** Add `--openspec`:
```bash
ugendran build myapp "multi-tenant SaaS with billing and auth" --openspec
```
This emits **real OpenSpec changes** and proves each one with `openspec validate --strict`
(objective pass/fail, not self-graded). Use this when accuracy matters.

### Step 4 — Turn a validated change into real code
```bash
ugendran apply myapp
```
This implements one validated change as actual files, then runs its build/tests to
**verify** it works. If green, it **archives the change into your living specs** automatically.

Useful options:
```bash
ugendran apply myapp my-change-name --path ./my-real-repo   # write into a specific repo
ugendran apply myapp --no-verify                            # skip running tests
ugendran apply myapp --no-archive                           # don't fold into specs yet
```

### Step 5 — Check your specs stay consistent (drift detector)
```bash
ugendran verify-specs myapp
```
Runs the real `openspec validate --specs --strict` over your living specs and tells you
if anything has drifted. Great to run in CI.

---

## 4. Keeping track of progress

```bash
ugendran status myapp      # dashboard: which skills are done / pending
ugendran history myapp     # full timeline of everything that happened
ugendran suggest myapp     # AI suggests the best next skill to do
```

---

## 5. Other handy commands

```bash
ugendran skills                 # list all 89 skills
ugendran skills architecture    # list skills in one category
ugendran audit ./old-project myapp   # AI reviews an existing codebase → continue/finetune/kill
ugendran kill myapp             # archive a finished project
```

---

## 6. The lifecycle in one picture

```
  new        →  do / build         →  apply            →  archive          →  verify-specs
  ───────       ─────────────────     ──────────────      ───────────────     ───────────────
  create a      AI writes & checks    implement as        fold into living    prove specs are
  project       real specs            code + run tests     specs/             still consistent
                (--openspec = the     (auto-archives
                 validated mode)       when tests pass)
```

This is the OpenSpec idea (**propose → apply → archive**) wrapped around your 89 domain
playbooks — so you get both expert methodology *and* an always-current source of truth.

---

## 7. Two modes — which to use?

| You want… | Command | Notes |
|---|---|---|
| The fastest draft | `ugendran do` / `build` | Self-checked, very fast |
| The most accurate, audit-safe result | add `--openspec`, then `apply` | Proven by real `openspec validate`; archives into living specs |

**Rule of thumb:** explore fast with the default mode; ship important work with `--openspec` + `apply`.

---

## 8. Quick troubleshooting

- **"apply needs an LLM CLI"** → install `claude` or `gemini`, then re-run.
- **"No OpenSpec changes for ..."** → run `ugendran build <name> "..." --openspec` first.
- **"openspec CLI not installed"** → `npm install -g @fission-ai/openspec`.
- **Output looks generic** → you're in 🟡 keyword mode; install an LLM CLI for real content.

---

## 9. A full example, start to finish

```bash
# 1. set up
python3 ugendran.py install
ugendran llm                              # confirm an LLM is detected

# 2. create and spec a project (validated mode)
ugendran new shop "online store with product search and checkout"
ugendran build shop "product catalog, search, cart, and Stripe checkout" --openspec

# 3. turn it into verified code, folded into living specs
ugendran apply shop --path ./shop-repo

# 4. confirm nothing drifted
ugendran verify-specs shop

# 5. see where you are
ugendran status shop
```

That's the whole loop: **idea → validated specs → verified code → living source of truth.**
