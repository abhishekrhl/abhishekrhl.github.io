---
title: "Pre-push human sign-off card"
date: 2026-10-25T23:42:48+05:30
draft: false
slug: "pre-push-human-sign-off-card"
tags: ["publish", "qa", "disclosure"]
description: "This is article 27 in the local-AI series."
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/).

This is article 27 in the local-AI series.

> **Disclosure:** Links below may earn a commission at no extra cost to you. We only recommend tools we actively use for our workflow.

In automated infrastructure where pipelines run fast, the "human in the loop" often feels like an unnecessary bottleneck. For critical assets bridging local dev environments with global edge networks, however, that pause is a necessity. This document is the **Pre-push Human Sign-off Card**, a single-page gatekeeper required before data leaves your Mac mini for GitHub Pages or similar targets (GitHub Pages — human CF Pages path).

### Why a Dated Signature Is Non-negotiable

The card acts as an operational anchor. Even with automated CI/CD, a dated signature provides proof of intent and accountability at the exact moment of transition. It shifts liability from "the system did it" to "a human verified it." Many jurisdictions require audit trails demonstrating human oversight over sensitive data deployment (local data protection regulations). Without this line, an automated failure or malicious injection becomes indistinguishable from routine operation.

This mechanism also breaks automation loops. Workflows are prone to "set-and-forget" drift; a script might succeed today but fail tomorrow due to subtle environment changes. Forcing a deliberate pause where the human physically reviews and signs prevents the silent propagation of errors.

The card maintains continuity with desk close-out procedures from earlier entries, ensuring no inventory gaps are treated as "soft-note clearance." In high-stakes environments, ambiguity is the enemy; the sign-off demands binary clarity: assets are signed and ready, or they are not.

### What Must Be Attached

**Pack Inventories.** This is the definitive list of assets ready for deployment. It provides hard proof that no files are missing and dependencies are intact. A zero-gap here is mathematical certainty regarding build integrity. Every script, config file, and static asset must be accounted for in this ledger (e.g., `~/AI/inventory.csv`) before the card is valid (pack-inventory-articles.md — expected v2-local drafts; gap 0 != ship).

**Claims Worksheet Initials.** This section requires specific initials from the operator to validate that outstanding doubts are resolved. It confirms any claims in the inventory against reality. If a claim states "All systems nominal," the initial verifies a human checked that statement before data leaves the local environment.

**Smoke Notes (If Applicable).** In operational jargon, "smoke" refers to anomalies or errors detected during inspection. Any observations regarding environmental issues must be logged explicitly. If no notes are written, it implies no issues were detected. This binary approach—write the problem or declare "None"—removes ambiguity (desk practice — dry hugo --minify is not a live Pages push).

### What Strictly Never Belongs

**Invented Smoke Stats.** Fabricating statistics creates false security. The card must reflect reality. If there were ten errors, write ten. If none, write none. Do not invent numbers to test system reactions; the system should react only to real data (desk practice — inventories gap 0 is not soft-note clearance).

**Dry Runs as Proof.** Running `hugo --minify` locally is a valuable test but insufficient proof of readiness. It proves code *can* compile, not that deployment to the edge will succeed or assets are production-ready. A dry run is a rehearsal; the sign-off card is the curtain call.

### Mandatory Order of Ticks

**Step 4: Apply the Dated Human Signature.**
Only after the above three checks are physically complete can the dated signature be applied. This timestamp anchors verification to a specific moment, creating an immutable record of the hand-off (sign-off card practice — dated human signature before Pages dashboard).

### Operational Boundaries

Components such as **Tailscale**, the **Freqtrade dry_run**, and daytime ** They do not trigger on this card; they continue running independently as background monitoring infrastructure. The sign-off does not alter Tailscale connection profiles, pause Freqtrade validation loops, or change 

The distinction is vital: the card governs the *transition* of assets to the edge, not the *management* of local infrastructure. The local environment manages health via active automated loops, while the operator focuses exclusively on deployment package integrity at push time.

### Local Tools in the Workflow

**Ollama (/go/ollama)** serves as the local inference engine. While it might generate documentation or assist with code review locally, its outputs are raw and unverified until they pass through the human sign-off card. Model predictions are suggestions, not facts; the human anchor must validate critical information before it enters the pipeline (Ollama — local inference engine; bot never clicks publish).

**Hugo (/go/hugo)** compiles local content into deployable HTML. It builds the site, but a `hugo --minify` dry run is insufficient proof of readiness. The build must be signed off by a human before files push to the edge (hugo-dry-status.md — dry --minify green still not Pages ready).

**Apple Silicon (/go/apple-silicon)** users have unique advantages with local AI workloads. On a 16 GB Mac mini, unified memory allows rapid processing of models like `qwen3.5:9b` or `4b` at Q4 quantisation within IST windows. However, this speed tempts operators to skip verification. The sign-off card acts as a counterweight, ensuring raw processing power does not bypass human judgment (Apple silicon — efficiency vs verification).

**MLX-Audio** and similar local audio models may be part of the asset inventory. If generated locally, files must be included in Pack Inventories and verified for quality before sign-off. Tool capability does not guarantee a specific file is ready for public consumption; human listening is required (pack-inventory-audio.md — soft-note counts are NOT audio gaps).

**GitHub Pages** is the destination edge platform. The card ensures nothing reaches this global network without explicit human authorisation. Deployment is not a background process; it is a deliberate act of publishing verified data (GitHub Pages — human CF Pages path). Related stack notes: /go/mlx-audio.
