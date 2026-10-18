# Pitch & Demo

**Project:** SignSync
**Date:** 2026-10-12
**Version:** 0.1
**Owner:** Xander
**Status:** Draft
**Last reconciled:** N/A
**IDEA:** [idea-signsync.md](idea-signsync.md)

---

## 1. Narrative Spine

**Audience:** Hackathon judges on the Ring track.

**Promise:** The door tells a Deaf or hard-of-hearing resident who is there and what they want, in a form the resident can perceive.

**Proof:** A bell alert they can feel or see, then a high-contrast card. A teammate signs a short doorstep phrase. The card shows a hands-only sketch and one sentence. Faces are not analyzed.

**Limit we will say out loud:** This is a closed list, not full sign-language translation. If the wider list misses, we show yes and no and say so.

**Ask:** Score the Ring integration, the accessibility use, and the single cloud sentence. Not a store launch.

---

## 2. Slide / Scene Outline

| # | Scene | What the judge hears | What is on screen |
|---|-------|----------------------|-------------------|
| 1 | The gap | A strobe says someone is here. It does not say who or why. | One line of text |
| 2 | The product | Alert, then a card from hand and body landmarks. | Card empty state |
| 3 | The demo | Bell, then the signed phrase. | Live card |
| 4 | The limit | Closed list. Faces never stored. | Hands-only sketch |
| 5 | The ask | Ring at runtime, plus one cloud sentence. | The sentence |

No slide file exists yet. Path: [FILL].

---

## 3. Live Demo Script

Time budget: [FILL]. Owner: Xander. Backup if the playground has no video: play the team clip through the same ingest path and say, on the recording, that the clip is labeled.

| Step | Action | Visible result | If it fails |
|------|--------|----------------|-------------|
| 1 | Fire a bell event | Doorbell pattern, card opens | Show the event from a saved payload and say it is saved |
| 2 | Sign "delivery, package, signature" at the camera | Hands-only sketch and one sentence | Fall back to yes and no, and say the list missed |
| 3 | Linger as a person, not a bell | Softer pattern | Skip with one sentence of explanation |

Do not show a face. Do not claim a measured accuracy number. The number is [FILL].

---

## 4. Judging Criteria Map

| Criterion | Where the demo shows it |
|-----------|-------------------------|
| Ring at runtime | Webhook and video, or a labeled clip on the same path |
| Accessibility and caretaking | Alert plus a card that states the visit |
| Not a generic camera popup | The card is the product, not a live face view |
| Cloud sentence | One sentence from the recognized signs and the event |
| Open source | Webhook and landmark harness noted in the submission. Repo link: [FILL] |

---

## 5. Production Readiness Gate (pre-demo)

This is a hackathon demo, not a production release. Rollback, uptime, a public privacy notice, and a store form are [FILL]. Do not describe the demo as production-ready.

| Check | Ready for the demo? |
|-------|---------------------|
| Happy path rehearsed | [FILL] |
| Face not stored | Designed. Test not run. |
| Backup clip labeled honestly | Scripted above |
| Secrets out of the repo | [FILL] |

---

## 6. Anticipated Q&A

| Question | Answer |
|----------|--------|
| Is this full sign language? | No. A short doorstep list plus yes and no. |
| Do you recognize faces? | No. Face landmarks are dropped before storage. |
| What if the visitor does not sign? | The alert and the card still say that someone is there. The sentence stays empty or says not recognized. |
| Can the doorbell talk back? | No. That path is not in the partner surface we are using. |
| What is the accuracy? | Not measured yet. |
| Is this a medical device? | No. It is a doorstep card. |

---

## Self-Check

- [x] The script matches the idea's three beats
- [x] Limits are spoken, not hidden
- [x] No production claim
