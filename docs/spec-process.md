# Requirements Spec Process — Multi-Agent Review

The website requirements document (`website-requirements.md`) is refined through a multi-agent
review loop. This file defines the agents and the loop so the work can continue (e.g. on the cloud).

## Agents

1. **Junior Product Manager** — drafts and refines `website-requirements.md` from the brief
   (`brief.md`) and incorporates all reviewer feedback.
2. **Senior Product Manager** — reviews the draft and rates it **out of 10**, with specific
   strengths, weaknesses, and required changes.
3. **Startup persona** — an end customer (startup founder). Rates **out of 10** based on how
   appealing the content is and whether they'd want to talk to iKITES and buy its services.
4. **Enterprise persona** — an end customer (enterprise decision-maker). Same rating basis.

## Loop

### Phase 1 — Drafting & internal review
1. Junior PM writes/updates the requirements.
2. Senior PM rates out of 10.
3. Junior PM keeps refining **until the senior rating is > 8**.

### Phase 2 — Customer persona review
Once the senior PM gives the go-ahead:
1. Startup persona and enterprise persona each review and rate out of 10.
2. The persona rating reflects **appeal** and **intent to engage iKITES**.
3. If either rating is ≤ 8, the Junior PM refines (Senior PM re-checks), then personas re-rate.
4. Continue **until both persona ratings are > 8**.

Each round should be logged (round number + ratings) so progress is traceable. Cap at ~5 rounds
per phase to avoid runaway loops; escalate if the bar isn't met.

## Definition of done
- Senior PM rating > 8, **and**
- Startup persona rating > 8, **and**
- Enterprise persona rating > 8.
