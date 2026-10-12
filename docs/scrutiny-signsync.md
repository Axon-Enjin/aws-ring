# IDEA Scrutiny Gate (SCRUTINY)

**Project:** SignSync
**Date:** 2026-10-12
**Version:** 0.1
**Owner:** Xander
**Status:** Draft
**Last reconciled:** N/A
**IDEA:** [idea-signsync.md](idea-signsync.md)

---

## 1. Verdict

**Decision:** PROCEED WITH FIXES

**One-line rationale:** The lock bar is specific, the cut line matches the Ring track, and the open items are carry-forward gaps rather than a contradicted assumption.

**If PROCEED WITH FIXES, items carried into the build:**

- PRD: Playground versus clip fallback, visitor audio, and the accuracy fallback stay [FILL].
- QAD: the accuracy bar stays [FILL] until a recording is measured.
- CLR: biometric paperwork posture stays [FILL] until Xander records COMPLY, ENGAGE, CONTEST, or DEFER. The user-protection bar (no face landmarks stored) is designed and not yet evidenced in code.
- AIA: model id and cost stay [FILL].
- No spike in this cycle. The doorbell-angle test result is [FILL].

---

## 2. Claim & Reference Audit

**Coverage:** Claims extracted: 6; load-bearing: 6; verified: 0; unverified: 6; contradicted: 0.

| # | Category | Claim (from IDEA) | Finding | Source (required if Verified) | Severity if wrong |
|---|----------|-------------------|---------|-------------------------------|-------------------|
| FC-1 | Problem | Doorbells assume hearing, so residents miss who and why | Unverified; needs check | Local research pack, 2026, sections 1 to 2. Not re-checked against a primary study this session. | Significant |
| FC-2 | Solution | Ring video is available for landmarks, and two-way talk is not | Unverified; needs check | IDEA.md, checked against the research pack in 2026. Partner API page not re-fetched this session. | Fatal if video is missing |
| FC-3 | Insight | Alerts plus a card cover visitors who do not sign | Unverified; needs check | IDEA.md scope note, 2026. No user test yet. | Significant |
| FC-4 | Technical | A closed vocabulary of doorstep signs is demoable by 2026-10-15 | Unverified; needs check | IDEA.md demo script, 2026. No measured accuracy. | Significant |
| FC-5 | Technical | Face landmarks can be dropped before storage | Unverified; needs check | IDEA.md constraint, 2026. No implementation evidence. | Fatal if the drop cannot be done |
| FC-6 | Market | Landmark pitch scored highest of the three ideas in the research matrix | Unverified; needs check | SignSync-AI-Deep-Research-Report.md, 2026. Internal score, not an external citation. | Minor |

### 2.1 References Integrity

| # | Reference | Backs claim | Resolves? | Supports it? | Finding |
|---|-----------|-------------|-----------|--------------|---------|
| R-1 | IDEA.md in this repo | FC-2, FC-3, FC-4, FC-5 | Yes, local file | Partly: it states the product, it is not independent evidence | Unverified |
| R-2 | SignSync-AI-Deep-Research-Report.md | FC-1, FC-6 | Yes, local file | Partly: research input, not re-audited | Unverified |
| R-3 | HACKATHON.md | Track rules and dates | Yes, local file | Yes for dates and the face and plate ban, as copied rules | Unverified |
| R-4 | ORG.md, PROMPT.md | Sponsor context | Yes, local files | Background only | Unverified |

No external URL was fetched this session. Nothing cited is marked Verified.

---

## 3. Gap Analysis

| # | Missing input | Needed by (doc) | Blocker or TBD |
|---|---------------|-----------------|----------------|
| G-1 | Playground capabilities | PRD, SDD | TBD |
| G-2 | Visitor audio present or absent | PRD | TBD |
| G-3 | Measured accuracy and fallback | QAD, AIA | TBD |
| G-4 | Model id and spend ceiling | AIA | TBD |
| G-5 | Named tester | IDEA §2 | TBD |
| G-6 | Regulatory posture choice | CLR §7 | TBD |

None of these is a fatal flaw. The lock bar names a user, a pain moment, a pitch, and one thing to ship.

---

## 4. Assumption Stress-Test

**Load-bearing assumption:** Doorbell-angle hand and body landmarks are classifiable into the closed vocabulary well enough for the demo.

**Strongest argument against it:** A low camera, backlight, and short signs can collapse the sequence into noise, so the card would be wrong often enough to fail the demo.

**Does it hold?** Holds with caveat. The idea does not require open-ended translation, and IDEA.md already names a narrower fallback. No measurement exists.

**Cheapest test:** Score a doorbell-angle recording against the closed list. Not run. Result: [FILL]. Effort: UNCALIBRATED.

### 4.1 Audience / 10-second stress

| Check | Finding |
|-------|---------|
| Stranger hook: who hurts and why, in 10 seconds, without slides | Pass. A resident cannot tell who is at the door. |
| Named user and pain present in IDEA §2 | Pass, as a role. An individual name is [FILL]. |
| One-liner repeatable (not generic SaaS) | Pass. Landmarks to text, faces dropped. |
| Why not keep coping with the status quo? | Pass. A strobe does not say who or why. |

**Audience verdict:** Holds. The hook is specific to the doorstep.

---

## 5. Feasibility & Scope

| Check | Finding |
|-------|---------|
| "If we ship only one thing" is shippable in the window | Holds with caveat. The demo date is close and accuracy is unmeasured. |
| Production-grade reachable (security, data, rollback) | Not this cycle. Demo only. Production runbook is absent on purpose. |
| Cut line honest, not hiding work | Holds. Spoken replies, open vocabulary, and billing are named as out. |

---

## 6. Risk & Regulatory Pre-flight

| Flag | Present? | Pulls in |
|------|----------|----------|
| Collects user data / PII | Yes | CLR §1, §3 |
| Children, health, payment, biometric, or precise-location data | Yes | CLR §3 user-protection bars |
| Regulated activity (license, franchise, permit, sector rule) | Yes | CLR §7 posture row |
| AI component with untrusted input or tools | Yes | SDD §8.1, QAD abuse cases, AIA |
| Security-critical paths (auth, money, deletes) | Yes | SDD §5, QAD abuse paths. No money path. |
| Public deploy | No | Repo will be public. No production uptime. |

Regulation does not stop this gate.

---

## 7. Blocking Questions

None. Verdict is not DO NOT BUILD YET.

---

## Self-Check

- [x] Verdict matches the findings
- [x] Coverage line filled; every load-bearing claim has a row
- [x] No Verified row without a source
- [x] §2.1 audits every reference cited in the IDEA
- [x] §4.1 filled
- [x] §6 flags name the docs they pull in
