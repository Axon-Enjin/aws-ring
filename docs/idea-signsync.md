# Idea Brief (IDEA)

**Project:** SignSync
**Date:** 2026-10-12
**Version:** 0.1
**Owner:** Xander
**Status:** Draft
**Last reconciled:** N/A
**Event / context:** Amazon Developer Hackathon, Ring track. Demo target 2026-10-15. Submission closes 2026-10-24, 3:00 AM PHT.

---

## 1. The Spark

**One-line pitch:** SignSync makes the front door work for Deaf and hard-of-hearing residents: a perceivable alert, then a high-contrast card that turns doorstep hand and body landmarks into text. Faces are dropped.

**Problem:** Doorbells assume hearing. A strobe says someone is here, not who is there or what they want.

**Insight (why us, why now):** The landmark pitch is the new one, and it uses Ring video, which this track guarantees. Alerts and a visitor card cover visitors who do not sign. Spoken replies through the doorbell are out because the Partner API has no two-way talk.

**Riskiest assumption:** Landmarks from a doorbell angle, including low light, can be classified into a closed doorstep vocabulary well enough to demo. The research pack names a target; this build has not measured it. The number is [FILL].

---

## 2. Who It's For

**Primary user (named, specific):** A Deaf or hard-of-hearing resident at a Ring doorbell. No individual tester is named yet: [FILL]. Xander is the track builder, not the user.

**Their moment of pain:** The bell rings or a person approaches, and the resident cannot perceive it or tell who is there and why.

**Success in their words:** "I knew it was a delivery that needs a signature, without someone hearing the bell for me."

---

## 3. Scope & Cut Line

| # | Capability | Core to the one thing? |
|---|------------|------------------------|
| 1 | Perceivable alert on button_press and human motion | yes |
| 2 | High-contrast visitor card | yes |
| 3 | Closed doorstep vocabulary from hand and body landmarks | yes |
| 4 | One clear sentence plus a confidence note | yes |
| 5 | Face landmarks dropped before storage | yes |
| 6 | Speech captions if visitor audio exists | no |

**Explicitly out of scope (v0):** Spoken doorbell replies, open-ended sign translation, Filipino Sign Language, weekly caregiver reports, store billing, facial recognition, and license-plate reading.

**If we only ship one thing:** Closed doorstep vocabulary from hand and body landmarks, on the visitor card, demoed by 2026-10-15.

---

## 4. Success & Judging Criteria

**How we know it worked:** A judge sees a button_press alert the resident can perceive, then a hands-only card whose text matches a short signed phrase, with faces never analyzed.

| Criterion | How we hit it |
|-----------|---------------|
| Ring API at runtime | OAuth linking, HMAC webhook, and video or a plainly labeled clip through the same ingest path |
| Accessibility and caretaking | Alert plus visitor card, not a generic motion popup |
| AWS builder | One Bedrock sentence from the recognized signs and the event |
| Open source | Webhook plus landmark-extraction harness released with the submission |
| No face or plate analysis | Face landmarks dropped before storage; no plate path exists |

---

## 5. Concept Visuals

No frames exist. This table does not describe images that were not made.

| Screen / section | Asset path | Decision |
|------------------|------------|----------|
| Visitor card | [FILL] | Do not invent a picture. High contrast, hands-only skeleton, short text. |

---

## 6. Open Questions

| Question | Owner | Resolve by |
|----------|-------|------------|
| Playground: events only, or clips and streams too? | Xander | Before the demo |
| Does the stream or clip include visitor audio? | Xander | [FILL] |
| Measured accuracy bar, and is fingerspelled YES and NO the fallback? | Xander | 2026-10-15 |

**Spike plan (optional):** Not built. This cycle adds no application code. The cheapest test is a doorbell-angle recording scored against the closed vocabulary. Result: [FILL].

---

## Self-Check

- [x] Lock bar fields are real, specific, and not placeholders
- [x] Riskiest assumption named; a spike is planned only as a later test because code is out of this cycle
- [x] Cut line explicit; "If we only ship one thing" named
