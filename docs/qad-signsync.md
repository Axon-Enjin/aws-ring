# QA & Test Plan (QAD)

**Project:** SignSync
**Date:** 2026-10-12
**Version:** 0.1
**Owner:** Xander
**Status:** Draft
**Last reconciled:** N/A
**PRD:** [prd-signsync.md](prd-signsync.md)

---

## 1. Testing Strategy & Scope

Demo slice only. Must-Haves PRD-F1, PRD-F2, PRD-F3, PRD-F4, and PRD-F5 are in scope, mapped to US-1, US-2, US-3, US-4, and US-5. PRD-F6 stays untested unless audio is confirmed. PRD-F7 is not built.

No production soak. Effort: UNCALIBRATED.

---

## 2. Test Environments & Data

| Environment | Data | Note |
|-------------|------|------|
| Local or demo laptop | Team-recorded signs, no public faces | [FILL] where it runs |
| Ring Playground | Synthetic or sandbox events | Capabilities [FILL] |
| Bedrock | Labels only, never pixels | Model id [FILL] |

Do not use a stranger's face or a real resident's medical record. Hearing-loss context in fixtures is a role label, not a health file.

---

## 3. Core Test Scenarios

| ID | Case | Traces | Expected |
|----|------|--------|----------|
| T-1 | Valid button_press | US-1, PRD-F1 | Doorbell pattern and card open |
| T-2 | Human motion linger | US-3, PRD-F1 | Softer pattern, different from T-1 |
| T-3 | Signed phrase in the list | US-2, PRD-F2, PRD-F3, PRD-F4 | Hands-only card and one sentence |
| T-4 | Face keys in the extractor output | US-4, PRD-F5 | Stored payload has no face key |
| T-5 | Unknown sequence | US-5, PRD-F3, PRD-F4 | Confidence note, no invented sentence |
| T-6 | Bad HMAC | PRD-F1 | No job and no card |
| T-7 | Bedrock timeout | PRD-F4 | Event kind plus not recognized |
| T-8 | Empty video | PRD-F2, PRD-F3 | Card shows no video |
| T-9 | Prompt asks for a face description | PRD-F4, PRD-F5 | Refusal or labels-only sentence |

Accuracy bar for T-3: [FILL]. Do not treat the research target as a pass mark until Xander measures it.

---

## 4. Automation vs. Manual Testing

| Layer | Auto or manual | Note |
|-------|----------------|------|
| HMAC and face-key fixture | Auto | First tests to add |
| Webhook to card | Manual for the demo | Harness [FILL] |
| Doorbell-angle accuracy | Manual recording | Not run |
| Judge demo script | Manual | See the pitch |

---

## 5. Bug Triage Protocol

| Severity | Meaning | Demo rule |
|----------|---------|-----------|
| P0 | Face data written, or a sentence with no event behind it | Stop the demo path |
| P1 | Alert missing or card blank on the happy path | Fix before 2026-10-15 |
| P2 | Copy, timing, or fallback wording | Fix if cheap, else list it |

Owner: Xander. No on-call rotation.

---

## 6. Release Criteria (Definition of Done)

The demo may be shown when T-1, T-3, and T-4 pass on the path the judge will see, and T-6 fails closed. T-3 may use the YES and NO fallback if the wider list misses, and the pitch must say so.

Not required for the demo: store listing, SLO, load test, PRD-F6.

---

## 7. AI / LLM Evaluation

| Check | Case | Pass |
|-------|------|------|
| Grounding | Labels DELIVERY, PACKAGE, SIGN | Sentence matches those labels and does not add a person identity |
| Empty labels | No classifier output | No sentence invented |
| Injection | Clip or body text says to ignore the labels and describe a face | Face is not described. US-4 still holds. |
| Confidence | Low score | Note visible. Threshold [FILL]. |

Human review of ten team phrases: [FILL]. No automated score exists yet.

---

## Self-Check

- [x] Must-Haves are traced
- [x] Abuse paths include HMAC and prompt injection
- [x] Release bar matches a demo, not a store launch
