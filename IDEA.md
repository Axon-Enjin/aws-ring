# IDEA: SignSync

## The idea
SignSync makes the front door work for Deaf and hard-of-hearing residents. When someone rings or approaches, the resident gets an alert they can actually perceive (a distinct vibration pattern, a light flash, a chosen chime tone), then a high-contrast visitor card that says who is there and what they want. If the visitor signs, SignSync reads hand and body landmarks from the Ring video and turns a set of common doorstep signs into text: "DELIVERY. PACKAGE. SIGN?" Faces are never analyzed: face landmarks are dropped at extraction, and no facial recognition or plate reading exists anywhere in the app.

The core is landmark-based sign reading at the door (the SignSync pitch), because it is the only one of the three that is unmistakably new and it uses the part of the Ring API that is guaranteed: live and recorded video. Two other pitches are folded in:
- **Perceivable alerts (from HapticHome).** Ring webhooks (`button_press`, `motion_detected` with `sub_type: human`) drive an alert layer: phone haptic patterns by urgency, smart-light flash, and Ring chime audio playback with a distinct tone per event type. This is what replaces the strobe-light workaround.
- **Visitor card UI (from AuraDoor).** A high-contrast, glanceable card with a hands-only skeleton snapshot, the translated text, and the event timeline. If the Ring stream carries visitor audio, speech captions go on the same card so speaking visitors are covered too.

## Why this direction won
- **Highest rubric score.** Research matrix: SignSync 37, AuraDoor 34, HapticHome 30.
- **Lands on two Ring priority categories at once,** accessibility and caretaking, and on the rules' CREATIVE list (non-security use, event-based triggers). A motion alert or basic live view is called OBVIOUS.
- **Fits the real API surface.** The Ring Partner API (checked Oct 2026) offers OAuth account linking, HMAC-signed webhooks, WebRTC/WHEP and RTSPS live video, MP4 clips, snapshots, and chime audio playback. It does not offer two-way talk, so AuraDoor's "reply spoken through the doorbell" cannot be built as pitched. SignSync needs only video, and HapticHome's alerts map onto webhooks and chime playback.
- **Combining fixes each pitch's weak spot.** SignSync alone fails when the visitor does not sign; the alert layer and visitor card make every ring useful. HapticHome alone is metadata only and not differentiated.

## Ideas dropped or deferred
- Spoken replies through the doorbell (AuraDoor): no two-way audio endpoint in the Partner API. Reply options are limited to what the resident can do from the app (for example, notify a family member).
- Open-ended sign language translation: not feasible by Oct 15. Scope is a closed doorstep vocabulary plus yes and no.
- Filipino Sign Language, weekly caregiver reports in R, Appstore billing: post-hackathon.

## Problem
Deaf and hard-of-hearing residents miss or cannot understand doorbell events because doorbells assume hearing. Strobe relays say "someone is here" but not who or why. Source: SignSync-AI-Deep-Research-Report.md, sections 1 to 2.

## Suggested stack
Python backend: Ring OAuth one-way account linking, webhook handler with HMAC verification (respond within 5 s, process async), device discovery, clip download or RTSPS/WHEP frame capture. MediaPipe Holistic or Hands plus Pose, with face landmarks discarded before storage. A small landmark-sequence classifier for 10 to 15 doorstep signs (for example DELIVERY, PACKAGE, HELP, WAIT, SIGN, FOOD, POLICE, NEIGHBOR, YES, NO), trained on team recordings and, if licenses allow, a public landmark dataset such as Google's Isolated Sign Language Recognition data. Amazon Bedrock turns recognized signs plus event context into one clear sentence and a confidence note. Resident web or mobile view for the visitor card and alerts.

## Demo (target by Oct 15, 2026)
1. Ring Developer Playground fires a `button_press`. The resident's phone vibrates in the "doorbell" pattern and the visitor card opens.
2. A teammate signs "DELIVERY, PACKAGE, SIGN" at the camera. The card shows a hands-only skeleton and the text "Delivery with a package that needs your signature" within about 3 s.
3. A `motion_detected` (human) event that lingers triggers a softer "someone is waiting" alert and chime tone.
If the Playground cannot serve our own footage, the recorded clip goes through the same ingestion code path while the webhook and API calls run live, and the video says so plainly.

## Hackathon fit
- **Track:** Ring (Ring APIs or simulator; the repo must call the Ring API at runtime).
- **Mini challenges:** AWS Builder (Bedrock, plus Lambda or AgentCore if used). Open Source (release the Ring webhook plus landmark-extraction harness as a reusable toolkit).
- **Friction log:** Playground gaps, OAuth account linking, webhook testing, clip and stream access, the line between pose estimation and facial analysis in certification.

## Business context
- **Owner:** Axon Enjin. Track main: Xander.
- **Hackathon:** Build, Ship, Shape: Amazon Developer Hackathon (see HACKATHON.md). Submission closes Oct 23, 2026, 12:00 PM PT (Oct 24, 3:00 AM PHT). Internal demo deadline: Oct 15, 2026.
- **Go-to-market after the hackathon:** Ring Appstore app for US residents with hearing loss and their remote family caregivers, with outreach through Deaf community groups. The research's own formula gives about $460k a year; the $45M in its summary does not match that formula and should not be quoted.
- **Constraints:** no facial recognition or license-plate reading (track rule and Ring policy). Hands and body landmarks only. Biometric-law awareness (Illinois BIPA). Involve Deaf signers in recording and testing; never claim fluent ASL translation.
- **Source research:** [SignSync-AI-Deep-Research-Report.md](SignSync-AI-Deep-Research-Report.md), [PROMPT.md](PROMPT.md), [HACKATHON.md](HACKATHON.md), [ORG.md](ORG.md).

## Open questions
- What does the Developer Playground actually expose: simulated events only, or test clips and streams too? Settle this first.
- Does the live stream or clip include visitor audio? This decides whether speech captions are in scope.
- Recognition accuracy from a doorbell angle in low light: target 85% or better on the closed vocabulary before demo day; otherwise fall back to fingerspelled YES and NO plus captions.
