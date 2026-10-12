# Validation Brief (VALIDATION)

**Project:** SignSync
**Date:** 2026-10-12
**Version:** 0.1
**Owner:** Xander
**Status:** Draft
**Last reconciled:** N/A
**IDEA:** [idea-signsync.md](idea-signsync.md)

---

## 1. Problem Evidence

External residents exist: Deaf and hard-of-hearing people who live with a video doorbell. This file does not add interviews. It records the evidence already in the repo and the gaps.

| # | Evidence | Source | What it supports | Gap |
|---|----------|--------|------------------|-----|
| V-1 | Doorbells assume hearing; a strobe does not say who or why | SignSync-AI-Deep-Research-Report.md, 2026, local | The pain in IDEA §1 | Not re-checked against a primary study. [FILL] |
| V-2 | Three pitches were scored in that same pack; landmarks ranked first | Same local report, 2026 | Why this direction was chosen | Internal score only |
| V-3 | Hackathon rules ban facial recognition and plate reading | HACKATHON.md, copied public rules | The face-drop constraint | Rules text, not a user test |

No new outreach was run. Effort: UNCALIBRATED.

---

## 2. Competitor / Substitute Scan

| Substitute | What the resident does today | What this demo changes |
|------------|------------------------------|------------------------|
| Strobe or lamp relay | Shows that someone is here | Adds who and why, if the signs are in the closed list |
| A hearing person at home | Interprets the visit | Not replaced. The card is for when that person is absent. |
| Generic live view | Requires watching a camera | Pushes a short card instead of a feed the resident may not perceive |

Named products beyond the three pitches in the research pack: [FILL].

---

## 3. Feasibility in Timebox

| Piece | In the demo window? | Note |
|-------|---------------------|------|
| Webhook alert | Yes, if Playground events fire | Else [FILL] |
| Clip or frames through one ingest path | Yes, as a labeled fallback | Playground video is [FILL] |
| Closed vocabulary | Yes, if the list stays small | Accuracy [FILL] |
| One sentence from the recognized signs | Yes | Model id [FILL] |
| Open-ended translation | No | Cut |

---

## 4. Kill Criteria

| # | Stop or cut if | Owner |
|---|----------------|-------|
| K-1 | Ring video cannot be shown at runtime, even as a labeled clip through the same ingest path | Xander |
| K-2 | Face landmarks cannot be dropped before storage | Xander |
| K-3 | The closed list cannot be demonstrated at all, including the YES and NO fallback | Xander |
| K-4 | A tester says the card is not perceivable | [FILL] |

A miss on accuracy alone narrows the vocabulary. It does not by itself kill the alert and card.

---

## 5. Concept Visual Reactions

No concept frames exist, so there are no reactions. Do not treat a missing picture as approval.

| Screen | Reaction | Source |
|--------|----------|--------|
| Visitor card | [FILL] | No asset |

---

## Self-Check

- [x] Evidence is cited as local input, not as a new study
- [x] Kill criteria name an owner or [FILL]
- [x] Feasibility matches the cut line in the IDEA
