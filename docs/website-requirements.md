# iKITES Website — Requirements Document

**Status:** Draft v0.1 (basic requirements — to be refined via the review process in `spec-process.md`)
**Owner:** Product
**Last updated:** 2026-06-19

---

## 1. Purpose & goals

Build the iKITES services website: a credible, measured shop window for an AI-first software
engineering company that earns a conversation with the right customers.

**Primary goal:** Get qualified startups and enterprises to reach out (book a call / send an enquiry).

**Secondary goals:**
- Communicate clearly *what we do* and *who it is for* within seconds.
- Make the "AI-first" claim believable through evidence, not adjectives.
- Establish a confident-but-grounded tone that the rest of the brand inherits.

### Success metrics (initial)
- Qualified enquiries per month (primary conversion).
- Visit → enquiry conversion rate.
- % of visitors who can correctly identify "what iKITES does" (qualitative / interviews).
- Bounce rate on the homepage and vertical pages.

---

## 2. Audience & messaging

Two segments, each addressed on its own terms. Speed is the common thread; the *kind* of speed differs.

| Segment | Core promise | Sub-segments | What they need to hear |
|---------|--------------|--------------|------------------------|
| **Startups** | Rapid product development — ideas to working product, fast | Early-stage; Established | "Small-ticket, fast moves that accelerate go-to-market. You bring the idea; we build it quickly." |
| **Enterprises** | Speed applied to re-engineering and managing complexity | — | "We move fast even where systems are large and tangled — modernizing and de-risking complexity." |

### Positioning statement (working)
> iKITES is an AI-first software engineering company. We run swarms of agents and continuously
> experiment with AI so that startups ship faster and enterprises tame complexity — measured by
> what we deliver, not what we promise.

### Messaging guardrails (tone)
- **Confident, not brazen.** No superlatives we can't back up ("world-leading", "revolutionary").
- **Grounded.** Prefer concrete capability statements over aspiration.
- **Balanced.** Neither over- nor under-claiming. Every sentence earns its place.
- Lead with the customer's outcome (speed, shipped product, reduced complexity), not our tooling.
- "AI-first" must always be paired with *how* (agent swarms, continuous experimentation, cost-efficiency).

---

## 3. Technology verticals

Each vertical gets a dedicated section/page with the same structure: what it is, who it's for,
how we apply it, and an illustrative outcome.

1. **Agentic AI** — designing and shipping systems of cooperating agents.
2. **Computer Vision** — perception systems for real-world inputs.
3. **Embedded Systems** — software close to the hardware.

---

## 4. Site structure (information architecture)

```
/                     Home
/startups             For Startups (speed, rapid product dev, early vs established)
/enterprises          For Enterprises (re-engineering, managing complexity)
/verticals/agentic-ai
/verticals/computer-vision
/verticals/embedded-systems
/how-we-work          AI-first delivery: agent swarms, experimentation, cost-efficiency
/about                Who we are / team / values
/contact              Enquiry form + booking
```

Global nav: Startups · Enterprises · Verticals (dropdown) · How we work · About · Contact (CTA).

---

## 5. Page requirements

### 5.1 Home
- **Hero:** one-line value proposition + primary CTA ("Talk to us" / "Book a call"). Measured tone.
- **Two audience entry points:** "For Startups" and "For Enterprises" cards routing to segment pages.
- **Verticals strip:** Agentic AI, Computer Vision, Embedded Systems with one-line descriptions.
- **AI-first proof block:** short, concrete explanation of agent swarms + continuous experimentation
  + cost-efficiency. Evidence over adjectives.
- **Trust signals:** (placeholder) logos / outcomes / short proof points where available.
- **Closing CTA.**

### 5.2 For Startups
- Speak to *speed* and *rapid product development*.
- Differentiate **early-stage** (small-ticket, go-to-market acceleration, idea → product) vs
  **established** (scaling delivery).
- Concrete "how it works" (idea in → product out, fast).
- CTA tuned to startups.

### 5.3 For Enterprises
- Speak to *speed applied to re-engineering and managing complexity*.
- Address modernization, de-risking, and working within existing/large systems.
- CTA tuned to enterprise procurement (e.g. "Discuss your system").

### 5.4 Vertical pages (×3)
Shared template: What it is · Who it's for · How iKITES applies it (AI-first) · Illustrative outcome · CTA.

### 5.5 How we work (AI-first)
- Make "AI-first" concrete: software processes aligned with AI; **swarms of agents** for speed and
  productivity; **continuous experimentation** for cost-efficiency.
- Frame as customer benefit (faster, cheaper, reliable), not internal tooling pride.

### 5.6 About
- Who we are, what we believe, the people. Grounded, human, no flaunting.

### 5.7 Contact
- Enquiry form (name, work email, company, segment [startup/enterprise], vertical of interest,
  message) + optional call booking.
- Clear, low-friction. Confirmation state.

---

## 6. Functional requirements
- Responsive across mobile, tablet, desktop.
- Working navigation incl. verticals dropdown.
- Contact/enquiry form with validation, spam protection, and delivery to a monitored inbox/CRM.
- Optional meeting booking integration.
- Basic analytics (page views, conversions, source).
- SEO essentials: per-page titles/meta, semantic headings, sitemap, OpenGraph/social cards.

## 7. Non-functional requirements
- **Performance:** fast first load (target Lighthouse performance ≥ 90; LCP < 2.5s on 4G).
- **Accessibility:** WCAG 2.1 AA.
- **Security/privacy:** HTTPS, form data handled per privacy policy, no unnecessary trackers.
- **Maintainability:** content easy to update (CMS or structured content), component-based UI.
- **Browser support:** current evergreen browsers.

## 8. Content requirements
- Final copy for every page in the agreed tone (see §2 guardrails).
- Real proof points / outcomes to substitute the trust-signal placeholders.
- Visual direction consistent with "confident but not brazen."

## 9. Open questions
- Do we have named case studies / logos we can show now, or do we launch with capability statements only?
- Primary conversion: call booking, form, or both?
- Is there an existing brand/visual identity to inherit, or is this greenfield?
- Geographic / language scope (single locale vs multi)?
- CMS preference and hosting constraints?

## 10. Out of scope (for v1)
- Blog / content marketing engine (can follow in a later phase).
- Customer portal / authenticated areas.
- Multi-language localization (unless answered otherwise in §9).

---

*This is a basic, reviewable baseline. It is intended to be iterated through the multi-agent
review loop described in `spec-process.md` until it clears the senior-PM and customer-persona
quality bars.*
