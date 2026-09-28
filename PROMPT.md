# TRACK 4 — Ring · Deep Research Meta Prompt

> **How to use:** Paste everything inside the `PROMPT` block into a deep-research tool (Gemini Deep Research, ChatGPT Deep Research, Perplexity Deep Research, Claude Research). Fill the `{{VARIABLES}}` first, or leave them as-is and the researcher will pick defaults. Run it once for a broad scan, then re-run Part B/C against the pitch you pick.
>
> **Companion files:** [hackathon.md](hackathon.md) (rules), [ORG.md](ORG.md) (sponsor goals).

---

````
PROMPT
======

# ROLE
You are a senior market-research analyst and product strategist specialising in
smart home, computer vision, property technology, and care/accessibility
technology. You combine a strategy consultant's rigor (MBB / Big 4 style) with a
hackathon judge's eye. You report evidence first, then give your judgment, and you
always label which is which.

# MISSION
Find, validate, and size the single best problem to build for in the Ring track of
the "Build, Ship, Shape: Amazon Developer Hackathon". Then generate three genuinely
distinct solution pitches for it, and make the market and business case. The
output must help a builder pick an idea that scores highly on all four equally
weighted judging criteria AND could realistically ship on the Ring Appstore.

# VARIABLES (use the defaults if left blank)
- {{BUILDER_PROFILE}}  = solo or small team, AI-native, agent-assisted development
- {{HOME_MARKET}}      = Philippines-based builder; primary launch market = United States (the Ring Appstore is initially U.S.-only — VERIFY). Flag Philippines/SEA differences where they matter.
- {{FOCUS_AREA}}       = open. If blank, evaluate every priority category below.
- {{DEVICE_ACCESS}}    = assume simulator / Ring Developer Playground only, with no physical device
- {{TIME_LEFT}}        = submission closes Oct 23, 2026, 12:00 PM PDT

# TRACK CONTEXT (treat as given; verify anything marked VERIFY)
- Requirement: a new app or an extension of an existing one using Ring APIs, SDKs,
  simulators, or devices. The demo must show it working through a simulator or a
  real Ring device. The repo must import and actually call Ring tech at runtime.
- Sponsor priority categories: access control, business systems, IoT home
  automation, accessibility, caretaking.
- Judging (equally weighted, scored 1–5 each): Tech Implementation, Design, Potential
  Impact (e.g. could it ship on the Ring Appstore?), Quality of the Idea. Friction
  logs add up to a 10% bonus.
- Judges call these OBVIOUS: a motion-detection alert; a basic doorbell live view.
- Judges call these CREATIVE: non-security use cases (accessibility aid, caretaking
  monitoring, package/delivery management); business system integration (access
  control for commercial spaces); multi-camera pipelines; event-based triggers for
  app functionality.
- Sponsor signals (VERIFY):
  - Jamie Siminoff returned as CEO in April 2025 to refocus on "make neighborhoods
    safer," using AI.
  - The Ring Appstore and third-party APIs launched on 2026-03-31 with about 15
    apps. Siminoff's stated goal is "hundreds of apps in tens of verticals."
  - APIs: live video (WebRTC, RTSP), motion events, doorbell presses, device status,
    event history. REST + OAuth 2.0 account linking + HMAC-signed webhooks.
  - Vision APIs: object detection, anomaly detection, predictive alerting.
  - There is a Ring MCP server for AI-assisted coding.
  - Business model: Ring reportedly takes a 10% commission; subscription, one-time,
    and ad-supported apps are allowed.
  - Publishing path: Draft → Testing → Certification → Beta → Production, with a
    privacy and security questionnaire.
  - Listed categories: business intelligence/operations, elder care, pet wellness,
    home analytics.
- HARD CONSTRAINTS: the Ring Appstore reportedly prohibits facial recognition and
  license-plate reading (VERIFY). There was public backlash in 2026 over the
  "Search Party" Super Bowl ad and the cancelled Flock Safety partnership. Treat
  privacy, consent, and bystander rights as first-order design requirements, not
  footnotes. Avoid anything that resembles neighbourhood surveillance or law-
  enforcement data sharing.

# RESEARCH RULES (non-negotiable)
1. Every factual claim gets: source name, URL, publication date, and a source tier:
   - T1 Primary: government statistics, company filings, official company blogs and
     docs (developer.ring.com, developer.amazon.com/docs/ring), peer-reviewed
     studies
   - T2 Expert: MBB / Big 4 reports, industry analysts (Parks Associates, IDC,
     Omdia, Gartner, Forrester, Strategy Analytics, Berg Insight), academic preprints
   - T3 Journalistic: Reuters, Bloomberg, FT, WSJ, The Verge, TechCrunch, CNET,
     Ars Technica
   - T4 Web: blogs, forums, Reddit, app reviews, vendor marketing
2. Label every statement [FACT] (sourced) or [INFERENCE] (your reasoning).
3. Never invent a number. If a figure can't be found, write `DATA GAP — <what is
   missing> — <how to get it>` and keep going. A visible gap beats a plausible guess.
4. When sources conflict, show both and mark the conflict `RESOLVED (<why>)` or
   `UNRESOLVED`.
5. Prefer data from 2024–2026. Flag anything older than 2023 as `STALE`.
6. Paywalled reports: use the publisher's free executive summary, press release, or
   a reputable citing article, and say which one you used.
7. Do not estimate build effort in hours, sprints, or headcount. Describe scope as a
   list of components only.

# SOURCE MAP (search these deliberately)
- Big 3 (MBB):
  - McKinsey: the connected home / IoT value at stake, aging and the longevity
    economy, the future of caregiving, the future of retail last-mile delivery
  - BCG: smart home, the silver economy
  - Bain: technology report (edge AI and computer vision), healthcare at home
- Big 4:
  - Deloitte: Connected Consumer survey, TMT Predictions (smart home, edge AI),
    Future of Health / aging-in-place
  - PwC: the smart-home consumer, Health Research Institute (home care)
  - EY: the connected home / Future Home, real estate/proptech
  - KPMG: consumer trust and privacy, real estate innovation
- Industry data:
  - Smart home and security: Parks Associates (smart-home and security adoption,
    video doorbell penetration), Strategy Analytics / Omdia, SDM Magazine, SIA
    (Security Industry Association)
  - Package theft and last mile: SafeWise and C+R Research surveys (T4 — label
    them), Capital One Shopping research (T4), USPS/UPS/FedEx data, Pitney Bowes
    Parcel Shipping Index
  - Aging and caregiving: AARP + National Alliance for Caregiving "Caregiving in the
    U.S." (T1/T2), U.S. Census (65+ population), CDC falls data, Administration for
    Community Living, WHO healthy aging
  - Accessibility: CDC disability statistics, WHO/World Bank disability reports,
    National Federation of the Blind, the National Association of the Deaf
  - SMB and access control: U.S. SBA small-business counts, access-control market
    reports (Omdia, IHS), Kisi/Verkada/Brivo public data (T4 unless audited)
  - Pets: APPA (American Pet Products Association) National Pet Owners Survey
  - Property management: NMHC (multifamily), NAR, Buildium/AppFolio industry reports
- Primary / regulatory: Amazon 10-K and Ring press releases, the Ring Appstore
  listings, the Ring Developer portal and UX design guide, the FTC 2023 Ring
  settlement (privacy lessons), state biometric laws (Illinois BIPA, Texas, Washington),
  GDPR (for global flags), the Philippines Data Privacy Act of 2012 (RA 10173) and
  NPC CCTV guidelines
- Competitive and deal data: Crunchbase, PitchBook, CB Insights; competing
  platforms' app ecosystems (Google Nest, SimpliSafe, ADT, Arlo, Wyze, Eufy,
  Verkada, SmartThings, Home Assistant)
- Voice of customer: r/Ring, r/homesecurity, r/smarthome, r/homeassistant,
  r/AgingParents, r/CaregiverSupport, r/propertymanagement, r/smallbusiness,
  r/Blind, 1–3 star reviews of Ring and competitor apps

---

# PART A — PROBLEM (the 5 tests)

Step A0 — Build a candidate list of 8–12 problems, at least one per priority
category (access control, business systems, IoT home automation, accessibility,
caretaking), and at least half non-security. Each must use what only a Ring camera
or doorbell sees or triggers. Write each problem as:
"<Specific person> struggles to <job> because <root cause>, which costs them <pain>."

Seed candidates to test (add your own):
- Adult children can't tell whether an aging parent living alone is okay today
  (routine anomalies, missed deliveries, unusual inactivity), without invasive
  monitoring
- Package theft and missed deliveries for households and small businesses
- Small businesses and short-term rentals need simple visitor and contractor access
  logs without enterprise access-control systems
- Deaf or hard-of-hearing residents miss doorbell events and visitor context
- Blind or low-vision residents can't tell who or what is at the door
- Property managers can't verify vendor visits, move-ins, or common-area issues
- Pet owners worry about pets left home alone (escapes, distress, dog walkers)
- Home automation that reacts to real-world events (arrivals, deliveries, weather)
  instead of fixed schedules

Step A1 — Score each candidate on the 5 tests. For every test, answer the questions,
cite evidence, and give a score from 1 to 5 with a one-line justification.

1. IS IT REAL? Does the problem exist in behaviour, not just in opinion?
   - Evidence of the behaviour: incident data, surveys with n and method stated,
     caregiving time-use data
   - Voice of customer: at least 5 verbatim complaints (quote under 25 words each,
     with a link)
   - Existing workarounds (check-in calls, neighbours, paid caregivers, lockboxes,
     spreadsheets, manual clip review)
   - Pass bar: at least one T1/T2 source AND observable workaround behaviour

2. IS IT LARGE? How many people or businesses have it, and how often?
   - Number of affected U.S. households or businesses, and frequency
   - Ring-reachable share: Ring installed base / active users (VERIFY what Amazon
     discloses; otherwise mark DATA GAP and use a labelled proxy such as video-
     doorbell household penetration × Ring share) × incidence. Show the formula.
   - Pass bar: millions affected, or a smaller segment (e.g. SMBs, property managers)
     with high willingness to pay

3. IS IT SIGNIFICANT? How much does it hurt?
   - Cost in money (losses, caregiver hours, staff time), safety, independence,
     stress. Quantify.
   - What people already pay (professional monitoring, caregiver apps, access-control
     SaaS, pet cameras)
   - Pain intensity: "hair on fire" or "nice to have"?
   - Pass bar: a measurable cost, or evidence that people already pay to solve it

4. IS IT RELEVANT? Does it fit this sponsor, this platform, and this builder?
   - Maps to a named Ring priority category, and ideally a non-security use case?
   - Aligns with Ring's stated strategy (long-tail verticals on the Appstore, AI,
     the "neighbourhoods safer" mission) WITHOUT crossing its privacy lines? Cite
     sources.
   - Uses Ring-specific capability (doorbell events, Vision APIs, multi-camera,
     webhooks) that a generic camera app can't replicate as easily?
   - Can it be built and demoed via the simulator / Developer Playground within
     {{TIME_LEFT}}?
   - OBVIOUS or CREATIVE per the track rubric?
   - Privacy test: can it pass Ring's certification privacy questionnaire and stay
     clear of facial recognition / plate reading?

5. IS IT URGENT? Why now?
   - Catalysts: Ring Appstore and open APIs (Mar 2026), Vision APIs, AI agents,
     demographics (the aging population), e-commerce delivery volume
   - Competitive timing: are Google Nest, SimpliSafe, ADT, Arlo, or Verkada
     shipping the same thing?
   - Pass bar: a dated catalyst within the last 18 months

Step A2 — Output a PROBLEM SCORECARD table:
| # | Problem statement | Real | Large | Significant | Relevant | Urgent | Privacy risk (L/M/H) | Total /25 | Key evidence | Biggest doubt |
Rank the candidates. Pick the top problem (and one runner-up). Explain the pick in
3 sentences, name the strongest counterargument, and say what evidence would change
the pick.

---

# PART B — SOLUTION (Pixar "Three Pitches" rule)

Do not settle for the first idea. For the chosen problem, develop THREE pitches that
are meaningfully different from each other. Each pitch must differ from the others
on at least TWO of these axes:
- Who: primary user (homeowner vs. remote family caregiver vs. SMB owner /
  property manager vs. a person with a disability)
- How: core mechanism (Vision-API event understanding vs. multi-camera pipeline vs.
  an event-driven agent that takes actions vs. an accessible alert/interaction
  layer)
- Where: device scope (Ring only vs. Ring + Alexa+/Echo vs. Ring + Fire TV screen vs.
  Ring + third-party systems such as smart locks, POS, property-management software,
  or calendars)
- Model: business model (consumer subscription on the Ring Appstore vs. per-site B2B
  SaaS vs. B2B2C through senior-care or insurance partners vs. usage-based)

Pitch archetypes to force spread:
- Pitch 1 — "The Safe Bet": a focused, Appstore-ready app for one clear non-obvious
  job
- Pitch 2 — "The Platform Play": the one most aligned with Ring/Amazon strategy
  (a long-tail vertical, Vision APIs + webhooks + an agent that acts, cross-device
  with Alexa+ or Fire TV)
- Pitch 3 — "The Wild Card": a surprising reframe (a new vertical, a new user
  group, or the camera used for something that isn't watching people)

For EACH pitch provide:
- Name + one-line pitch ("For <ICP> who <problem>, <name> is a <category> that
  <key benefit>. Unlike <alternative>, it <differentiator>.")
- The hero moment: the first 30 seconds of the demo video, shot by shot (simulator
  event → the app's intelligent response)
- Event pipeline: trigger (motion, doorbell press, vision detection, webhook) →
  processing → decision → action → notification, with the Ring API or endpoint used
  at each step
- Privacy-by-design: data minimisation, retention, on-device vs. cloud processing,
  consent for bystanders and household members, what the app deliberately does NOT
  do
- Tech stack: optional AWS services (Bedrock, AgentCore, Strands, Rekognition —
  check whether it conflicts with Ring's rules, Kiro/Kiro Crew) for the AWS Builder
  mini challenge; which component can be released open source (e.g. a webhook
  toolkit or simulator harness) for the Open Source mini challenge
- Scope as components (no time estimates): must-have for the demo vs. cut list
- OBVIOUS vs CREATIVE self-check against the judges' examples
- Top 3 risks, including false positives/negatives, privacy backlash, and any case
  where AI is less reliable than a simple rule
- Evidence it would work: analogous products, adoption data, studies

Then output a PITCH COMPARISON MATRIX (score 1–5):
| Pitch | Tech Implementation | Design | Potential Impact | Quality of Idea | Buildability | Strategic fit with Ring | Privacy safety | Friction-log potential | Total |
Recommend one pitch. State why in one sentence, defend it, name the strongest
counterargument, and say what would flip the recommendation.

---

# PART C — VALUE (market value + business value)

Complete this for the recommended pitch. Add short notes on the other two.

C1. IDEAL CUSTOMER PROFILE (ICP)
- Consumer ICP: household type, age band, Ring devices and subscription (Ring Home
  plans), other smart-home gear, tech comfort, income band
- Caregiver ICP (if relevant): relationship, distance, caregiving hours, emotional
  load
- Business ICP (if relevant): business type and size, number of sites, current
  access/security tools, budget owner, buying process, compliance needs
- Psychographics and jobs-to-be-done (functional, emotional, social)
- Trigger events (a fall, a theft, a new rental property, a new hire, a move)
- Where they hang out; willingness to pay (with sources)
- Secondary ICP and anti-ICP

C2. COMPETITIVE MARKET ANALYSIS
- On-platform: existing Ring Appstore apps in the category (list them all)
- Competing ecosystems: Google Nest (with Gemini), Arlo, SimpliSafe, ADT, Wyze, Eufy,
  Apple Home, SmartThings, Home Assistant (open source)
- Vertical specialists:
  - aging-in-place: Lively, Aloe Care, Cherish, CarePredict, Amazon Alexa Together
    (discontinued — why?)
  - SMB access control: Verkada, Kisi, Brivo, Openpath
  - package management: Amazon Key, lockers
  - pets: Furbo, Petcube
- Status quo: phone calls, neighbours, manual review, paid monitoring
- Competitor table:
  | Competitor | Platform | Offer | Price | Traction (sourced) | Strengths | Weaknesses | Recent moves |
- Platform-owner risk: could Ring build this natively (e.g. in Ring Home plans)? How
  does the pitch survive that (vertical depth, integrations, a trust brand), or
  become an Appstore showcase?
- A 2×2 positioning map (choose axes that reveal white space) and the chosen white space
- Moat candidates: vertical workflow integrations, trust/privacy reputation,
  caregiver network effects, data

C3. MARKET SIZING — TAM / SAM / SOM
Do BOTH approaches, then reconcile them:
- Top-down: the relevant market (aging-in-place tech, SMB access control, package
  security, pet tech, smart-home services), narrowed to camera/doorbell households
  or sites, then to Ring's base. Cite each layer.
- Bottom-up: Ring-reachable users or sites × incidence × adoption × ARPU, minus
  Ring's commission (VERIFY the 10%). State every assumption.
- TAM / SAM / SOM table with formulas. Mark every unsourced layer as DATA GAP.
- Philippines/SEA flag: Ring availability, CCTV norms, the NPC CCTV guidelines,
  and whether the vertical (e.g. OFW families remotely checking on elderly parents)
  is a stronger local niche. Cite PSA/POEA/DMW data if used.

C4. BUSINESS VALUE
- For the end user: the measurable outcome (hours of caregiving saved, losses
  avoided, faster response, independence maintained)
- For Ring/Amazon: which stated goals it advances (Appstore breadth — "hundreds of
  apps in tens of verticals," AI features, subscription attach, repairing trust
  after the 2026 backlash). Cite sources.
- For businesses (if B2B): cost avoided vs. enterprise systems, time saved,
  compliance
- For AWS (if used): the showcase value of the architecture
- Revenue model options: Appstore subscription or one-time purchase (net of Ring's
  commission), B2B per-site SaaS, partner channels (insurers, senior living, property
  managers)
- Unit economics sketch: ARPU, Ring commission, inference/vision compute per event,
  video egress costs, CAC, churn benchmarks for smart-home subscriptions. Show the
  inputs; mark any gaps.
- Go-to-market: Ring Appstore discovery, Ring community, caregiver communities,
  property-management associations, SMB channels. What is the first 100 paying
  users plan?
- Risks and mitigations: privacy/regulatory (BIPA, FTC, state laws, Philippines
  DPA), certification rejection, false alarms, liability for missed events,
  platform dependency
- Kill criteria: what signal in the first 90 days would show this is not worth
  continuing?

C5. VALIDATION PLAN
- 3 riskiest assumptions, ranked (always include: "the target user accepts the
  privacy trade-off")
- For each: a test (caregiver interviews, a concierge MVP using simulator events, a
  landing page, property-manager outreach), a success threshold, and a source of
  participants
- 5 customer interview questions (non-leading, focused on past behaviour)

---

# PART D — HACKATHON FIT CHECK
- Mapping to each judging criterion: what in the build or demo earns a 5/5?
- Proof of Ring tech: exactly what the video must show (simulator/device event →
  app behaviour) and what the repo must contain (runtime Ring API calls, webhook
  handlers, OAuth)
- Mini challenge double-dips: AWS Builder (Bedrock/AgentCore/Strands doing real
  work on events) and Open Source (a reusable Ring webhook/agent toolkit)
- Friction-log opportunities: Developer Playground/simulator gaps, OAuth account
  linking, webhook testing, Vision API accuracy, certification process, the Ring
  MCP server
- Submission red flags to avoid: an obvious security-only alert, any facial
  recognition or plate reading, recognisable bystanders in the demo without
  consent, a video over 3 minutes

# OUTPUT FORMAT
Return a single Markdown report with exactly these sections:
0. Executive summary (≤ 12 bullets: chosen problem, recommended pitch, ICP,
   TAM/SAM/SOM headline, top risk, confidence level)
1. Problem candidates and scorecard
2. Deep dive: the chosen problem (the 5 tests with evidence)
3. Three pitches + comparison matrix + recommendation
4. ICP
5. Competitive analysis (table + positioning map description)
6. TAM / SAM / SOM (table with formulas)
7. Business value, revenue model, unit economics, GTM
8. Risks (including privacy/legal), kill criteria, validation plan
9. Hackathon fit check
10. DATA GAPS and UNRESOLVED conflicts (consolidated list)
11. Sources (numbered, with tier, date, URL)

Style: tables over prose, specific over vague, and no filler. Keep evidence and
judgment clearly separated. When confidence is low, say so. For any legal point,
add: "Regulatory awareness only — not legal advice. Consult a licensed attorney
in the relevant jurisdiction (Philippines and U.S.)."
````
