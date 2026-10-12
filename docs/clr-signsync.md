# User Protection & Regulatory Posture (CLR)

**Project:** SignSync
**Date:** 2026-10-12
**Version:** 0.1
**Owner:** Xander
**Status:** Draft
**Last reconciled:** N/A

This is awareness for the build, not legal advice. Effort: UNCALIBRATED.

---

## 0. Target Markets (drives the rest of this document)

| Market | In this slice? | Why |
|--------|----------------|-----|
| Demo judges and the team | Yes | Hackathon demo |
| United States residents | Intended after the hackathon | Named in IDEA.md as later distribution |
| Other countries | [FILL] | Not chosen |
| Children | No | Not a children's product |

No store submission in this cycle.

---

## 1. Data Inventory / Record of Processing

| Activity | Data | Why | Where | Retention | Feature |
|----------|------|-----|-------|-----------|---------|
| Account link | Ring account reference | Send alerts to the right resident | [FILL] | Until unlink. Unlink behavior [FILL]. | PRD-F1 |
| Webhook | Event kind, device id, time | Open the card | [FILL] | Demo window [FILL] | PRD-F1, US-1 |
| Landmarks | Hands and body only | Closed vocabulary | [FILL] | [FILL] | PRD-F3, PRD-F5, US-4 |
| Sentence | Labels and one sentence | The card | [FILL] | Same as the event | PRD-F4, US-2 |
| Face set | Not stored | Dropped before write | Memory only | None | PRD-F5 |
| Visitor audio | [FILL] | Captions only if present | [FILL] | Off unless PRD-F6 is accepted | PRD-F6 |

No payment data (PRD-F7 is Won't-Have). No plate data. No health file. A role label such as "resident" is not a diagnosis.

---

## 2. Multi-Jurisdiction Obligations Matrix (awareness)

| Topic | Demo slice | Later US distribution |
|-------|------------|------------------------|
| Notice | Team and judges know this is a demo | A public notice is [FILL] |
| Deletion | [FILL] | Required before a store launch |
| Biometric paperwork | See §7 | Do not assume the demo choice covers a later launch |

Counsel review: [FILL].

---

## 3. User-Protection Bars (non-negotiable)

| Bar | Design | Evidence the bar is met |
|-----|--------|-------------------------|
| No facial recognition | PRD-F5 and the face-drop RFC | [FILL] until T-4 passes |
| No plate reading | No such feature | No code yet |
| Purpose limit | Landmarks feed the closed list and the card, not an identity graph | [FILL] |
| No silent model action | The resident reads the card. Nothing unlocks or replies by itself | Spec only |
| Children | Out of scope | No age gate designed. [FILL] if the later app needs one |
| Hearing-loss context | Used only to explain the product, not stored as a medical record | Do not add a diagnosis field |

These bars are not deferred. Paperwork around them can be, in §7. A release beyond the demo waits until the evidence column is filled.

---

## 4. Terms of Use / EULA Readiness

Not required for a private demo to judges. Before a public app: [FILL].

| Item | Status |
|------|--------|
| Terms | [FILL] |
| Privacy notice | [FILL] |
| Account deletion | [FILL] |

---

## 5. IP Infringement & Protection Readiness

| Item | Status |
|------|--------|
| Team recordings | Allowed if the people in them agreed. Agreement record: [FILL] |
| Public landmark dataset | Use only if the license allows. Check: [FILL] |
| Ring brand assets | Follow the sponsor rules already copied in HACKATHON.md |
| Repo license | Not added in this cycle |

---

## 6. App Store / Platform Compliance

Not shipping to a store in this cycle.

| Item | Status |
|------|--------|
| Store privacy form | [FILL] |
| Account deletion path | [FILL] |
| Third-party SDK list | Ring and Bedrock at minimum. Full list [FILL] |

---

## 7. Regulatory Posture Register

| ID | Obligation | Applies because | Exposure | Enforcement reality | Posture | Rationale | Revisit when | Kill switch / fallback | Owner | Counsel before |
|----|-----------|-----------------|----------|---------------------|---------|-----------|--------------|------------------------|-------|----------------|
| CLR-P1 | Biometric paperwork, including Illinois BIPA awareness named in IDEA.md | Hand and body landmarks can be treated as biometric identifiers depending on the facts | Civil exposure is the concern named in the research. Amounts are not copied here. | [FILL] | [FILL] | Xander has not chosen COMPLY, ENGAGE, CONTEST, or DEFER | Before any public launch or any stored landmark outside the demo team | Stop ingest. Face path already fails closed. | Xander | [FILL] |
| CLR-P2 | Training-bot and crawler choice on a public repo | S11, repo will be public | Low for a docs repo | [FILL] | DEFER | No public deploy yet | When the repo is flipped public | [FILL] | Xander | No |

§3 bars are not given a CONTEST or DEFER posture. CLR-P1's posture cell is [FILL] on purpose until Xander chooses. CLR-P2 is paperwork about the repo, not a §3 bar.

---

## Self-Check

- [x] Markets for this slice are declared
- [x] Each stored activity has a retention cell, even where it is [FILL]
- [x] §3 bars are unmet in evidence, not waved through
- [x] No price or fine amount is copied into this file
