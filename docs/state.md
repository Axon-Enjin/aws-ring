# Project State: SignSync

**Project slug:** `signsync`
**Owner:** Xander
**Last updated:** 2026-10-12

---

## 1. Position

| Field | Value |
|-------|-------|
| **Current milestone** | Decide, moving to Specify |
| **Entered on** | 2026-10-12 |
| **Exit condition** | Scrutiny is PROCEED WITH FIXES and the triggered Draft docs exist |
| **Next milestone** | Specify |
| **Current blocker** | None for docs. No application code in this cycle. |
| **Owner of the next step** | Xander |

**What we are building, in one line:** A Ring doorstep reader that alerts a Deaf or hard-of-hearing resident in a way they can perceive, then shows a high-contrast card with text from hand and body landmarks. Faces are dropped.

**Engagement type:** product-led hackathon entry

**Vault status:** none

**Effort:** UNCALIBRATED

---

## 2. Active signals

| Signal | True? | Evidence | Requires |
|--------|-------|----------|----------|
| S1 Frontend | yes | Visitor card in IDEA.md | DSD |
| S2 Backend, data, integration, auth | yes | Ring OAuth, HMAC webhooks, video ingest | SDD |
| S3 Irreversible data choice | yes | Face landmarks dropped before storage | RFC |
| S4 Non-trivial behavior | yes | Alerts, card, closed vocabulary, sentence | PRD |
| S5 Implementation by an agent or team | yes | Track main Xander; docs will guide the build | BUILD |
| S7 Release to users intended | yes | Demo target 2026-10-15; submission 2026-10-24 | QAD |
| S9 User data | yes | Account link and video-derived landmarks | CLR |
| S10 Sensitive class | yes | Hand and body landmarks; hearing-loss context | CLR |
| S11 Public surface | yes | Repo will be public and judged | Existing human README |
| S12 AI component ships | yes | Landmark classifier and a Bedrock sentence | AIA |
| S20 External integrations | yes | Ring and Bedrock | Failure modes in SDD |
| S22 Audience presentation | yes | Judges and the demo | PITCH |
| S27 Time box | yes | Hackathon demo and submission dates | Shorter docs, no extra artifact |
| S29 Regulated activity | yes | Biometric-law awareness named in IDEA.md | CLR posture row |
| S30 Riskiest assumption is testable in code | yes | Doorbell-angle accuracy | Spike not built: no application code this cycle |

**Deliberate absences:**

- S6: no repeated specialist spawn, so no SAD.
- S8: no production deploy and no users depending on uptime, so no OPS.
- S13: post-hackathon billing is named in IDEA.md and is not a pricing decision in these public docs, so no UES. No amounts are copied here.
- S14: no named buyer, so no OPP or PROP.
- S15: the demo slice is inside a week, so no BRD.
- S16: a second committer is not established. Roles beyond track main are [FILL].
- S17: no repeated regression class yet.
- S18: not shipping more than weekly.
- S19: no financial transactions in this slice.
- S21: user acquisition is post-hackathon, so no GTM.
- S23: no product code and no prior PRD, so no CHANGE loop.
- S24, S25, S26: no locked contradiction, no incident, no invalidated direction.
- S28: this is the owner's repo, so external mode is off.
- WRAP: the event has not ended.

---

## 3. Operating frameworks

| Dimension | Choice | Why |
|-----------|--------|-----|
| **Project management** | milestones | One demo date and one submission date |
| **Engineering maturity** | L0 | No CI, preview, or deploy exists yet |
| **Subagents** | none | Fewer than three real spawns |

---

## 4. Open assumptions

| ID | Assumption | Risk if wrong | Reversible? | Owner | Resolve by |
|----|-----------|---------------|-------------|-------|------------|
| A1 | Doorbell-angle landmarks can be classified into a closed doorstep vocabulary well enough to demo | The demo falls back to fingerspelled YES and NO, or the landmark pitch is cut | yes | Xander | 2026-10-15 |
| A2 | The Developer Playground can fire button_press, or a recorded clip can use the same ingest path | Demo step 1 cannot be shown live | yes | Xander | Before demo |
| A3 | Face landmarks can be discarded before any storage or model call | The irreversible choice fails and that path must not ship | no | Xander | Before any stored frame |
| A4 | Visitor audio may be absent | Speech captions stay out of the demo | yes | Xander | [FILL] |

**Open questions for the user:**

1. What does the Developer Playground expose: events only, or clips and streams too?
2. Does the live stream or clip include visitor audio?
3. What measured accuracy is required before the demo, and is fingerspelled YES and NO the fallback?
4. Which regulatory posture (COMPLY, ENGAGE, CONTEST, or DEFER) does Xander record for biometric paperwork?

---

## 5. Decisions

| ID | Question | Decision | Evidence class | Review when |
|----|----------|----------|----------------|-------------|
| D1 | Which pitch is the product? | SignSync landmarks, plus perceivable alerts and a visitor card. Spoken doorbell replies are dropped. | Project Canonical | If the Ring video path cannot be shown |
| D2 | How wide is recognition? | Closed doorstep vocabulary plus yes and no. Open-ended translation is out. | Project Canonical | After the first measured set |
| D3 | Build a spike now? | No. This cycle is docs only. The accuracy test is [FILL]. | Human Decision | When application code is allowed |

---

## 6. Context exclusions

| Excluded | Reason | Where it lives now |
|----------|--------|--------------------|
| Engine tree | Must not be committed | Outside this repo |
| Post-hackathon prices and revenue formulas | Not a public decision this cycle | IDEA.md and the research report only |
| Council or maintainer identities | Not part of this product | Not copied |

---

## 7. Next actions

1. Xander settles Playground scope, audio, and the accuracy bar.
2. Implementing agent builds only from the Draft specs, still without storing face landmarks.
3. Re-run the doc check after the first code slice changes a spec.

**Artifact plan for this slice:**

| Artifact | Why it is justified now | Status |
|----------|-------------------------|--------|
| state.md | Operating position | done |
| idea-signsync.md | Frame artifact | done |
| scrutiny-signsync.md | Gate before the suite | done |
| val-signsync.md | External residents exist; research pack is already in the repo | done |
| prd-signsync.md | S4 | done |
| dsd-signsync.md | S1 | done |
| sdd-signsync.md | S2 and S20 | done |
| rfc-signsync-face-drop.md | S3 | done |
| qad-signsync.md | S7 | done |
| build-signsync.md | S5 | done |
| clr-signsync.md | S9, S10, S29 | done |
| aia-signsync.md | S12 | done |
| pitch-signsync.md | S22 | done |

---

## 8. Self-Check

| Check | Done |
|-------|------|
| Milestone and exit condition are current | yes |
| Every listed signal has real evidence | yes |
| Every assumption made this session is in §4 | yes |
| Artifact plan contains no untriggered artifact | yes |
| Context exclusions updated after any pivot | yes |
