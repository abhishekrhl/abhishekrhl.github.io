---
title: "Deploy rehearsal notes — what a human does in Cloudflare Pages (/go/cloudflare-pages) after sign-off (still no bot click)"
date: 2026-10-25T20:23:22+05:30
draft: false
tags: ["local-ai","affiliate","apple-silicon"]
---

# Deploy rehearsal notes — what a human does in Cloudflare Pages (/go/cloudflare-pages) after sign-off (still no bot click)

This is article 23 in a local-AI affiliate series.

*Disclosure: This article contains an affiliate disclosure for Cloudflare Pages at the end. As an affiliate, I may earn a commission if you purchase through my links, at no extra cost to you.*

In the rhythm of modern infrastructure development, there exists a critical boundary between preparation and execution. It is the moment where local validation transforms into a potential global state change. This article explores that precise juncture: the human intervention required after sign-off in Cloudflare Pages. Specifically, it distinguishes why rehearsal notes are never a deploy, how redirects are strictly controlled by source data, and why certain critical systems remain immune to automated traffic patterns [CITE: claims-worksheet-sign-off — prior article 22 human gate before rehearsal].

## Why Rehearsal Notes Are Not a Deploy

A signed worksheet confirms that the logic holds up under local scrutiny, but it does not possess the agency to alter live production databases or trigger edge functions across a distributed network. It is crucial to understand that running `hugo --minify (/go/hugo)` serves only as a build artifact for review; it is a static compilation step designed to verify syntax and asset integrity, not a production push mechanism [CITE: hugo-dry-status.md — dry --minify green still not Pages ready]. The distinction lies in the "dry" boundary. Local execution prevents accidental data mutation or external API calls during testing phases. This isolation ensures that any errors found are contained within the developer's machine, preventing cascading failures that could affect end-users [CITE: HUMAN-STEPS-PENDING.txt — human CF Pages path; bots never click publish].

## Dashboard Path a Human Walks After Sign-off

The first step involves inspecting the build logs directly in the dashboard. While local builds provide immediate feedback, the Cloudflare Pages environment introduces variables that a local machine cannot simulate, such as edge function latency, specific runtime constraints, or network topology differences between the developer's node and the global edge network. A human must confirm that these logs show no runtime errors before proceeding. It is not enough for the build to succeed locally; it must succeed in the target environment [CITE: desk practice — optional /go/ smoke after a human push only].

Following the log inspection, the operator must confirm that the "Production" branch is clean. This involves checking the commit history and ensuring no unintended changes have been merged or pushed during the rehearsal phase. Only after this manual verification does the human initiate the deployment action. This step is non-negotiable; it ensures that the state of the production environment is explicitly approved by a person who understands the context of the changes. The dashboard path is not merely a UI traversal; it is a security checkpoint where automation stops and human judgment resumes [CITE: HUMAN-STEPS-PENDING.txt — human CF Pages path; bots never click publish].

## _redirects Regenerated from links.csv Only

The regeneration process is deterministic, meaning that given the same input data, the output will always be identical. This reliance on `links.csv` as the single source of truth prevents drift between the intended routing structure and the actual configuration. During the rehearsal phase, the system reads this CSV, processes the entries, and generates a temporary `_redirects` file for local testing. If the CSV contains invalid paths or conflicting rules, the local build will fail or highlight the discrepancy, but no changes are persisted to the live environment [CITE: affiliate-redirects helper — writes static/_redirects from links.csv].

This approach highlights that the regeneration is dependent entirely on validated input sources. By tying the routing configuration directly to a data file that undergoes its own review process, we create a chain of custody for every redirect rule. There are no "magic" paths hidden in the code; every jump in the URL structure is traceable back to a specific entry in `links.csv`. This reduces the attack surface for misconfiguration and ensures that the live environment reflects exactly what was validated during the rehearsal phase [CITE: links.csv allow-list — regenerate _redirects from CSV rows only].

## Optional /go/ Smoke Checklist After a Human Push
Short voice abstracts are rendered later with mlx-audio (/go/mlx-audio); they summarise the rehearsal, they do not publish it.


Following the human-initiated push to the production branch, an optional smoke test is conducted to verify core service availability. This check typically targets a lightweight endpoint, such as `/go/`, which serves as a minimal health indicator for the system [CITE: desk practice — optional /go/ smoke after a human push only]. The purpose of this step is to confirm that the application has loaded successfully and is responding to requests without triggering complex operational logic or sensitive data processing.

The role of this `/go/` endpoint is strictly observational. It returns a simple status signal indicating that the server is up and running, allowing operators to proceed with confidence. However, it is vital to note that automated bots must never trigger this checklist independently. The smoke test requires explicit human confirmation to proceed; it is part of the final release gate, not an autonomous background task [CITE: HUMAN-STEPS-PENDING.txt — human CF Pages path; bots never click publish].

By requiring a human push before the smoke test runs, we ensure that the decision to expose the system to public traffic is deliberate. This prevents scenarios where a bot might misinterpret a local success as a global readiness signal and initiate checks that could destabilise the environment if something subtle has gone wrong. The steps for verification are straightforward: access the endpoint, observe the response time and status code, and confirm that no errors appear in the logs. This lightweight check provides assurance without risking sensitive operational logic or consuming significant computational resources [CITE: desk practice — optional /go/ smoke after a human push only].

## What Bots Must Never Click (And Why Tailscale/Freqtrade Stay Untouched)
Prose for this series is drafted through the local Ollama (/go/ollama) stack on Apple silicon (/go/apple-silicon); that does not grant bots a Pages click.


`Tailscale` is often used to create secure mesh networks for internal services, while `freqtrade` manages algorithmic trading strategies or similar high-stakes operations [CITE: desk practice — KEEP Tailscale; leave Freqtrade dry_run; LTX inspect-only daytime]. Exposing these systems to automated traffic, even for "inspection," introduces unnecessary risk. A bot might inadvertently trigger a rate limit, misinterpret a status code, or execute a command that was intended only for manual review. The security rationale is clear: bots document the rehearsal, but humans retain exclusive control over live production assets [CITE: desk practice — KEEP Tailscale; leave Freqtrade dry_run; LTX inspect-only daytime].

The daytime inspection of these systems is strictly limited to human operators who can interpret the context of the data and understand the potential impact of their actions. Automated scripts are kept away from these domains to prevent unintended service disruption. Even if a bot detects an anomaly in the logs, it does not have the authority to interact with `tailscaled` or `freqtrade`. This separation ensures that the most sensitive parts of the infrastructure remain protected behind a wall of human decision-making [CITE: desk practice — KEEP Tailscale; leave Freqtrade dry_run; LTX inspect-only daytime].

In summary, the deployment process described here prioritises safety through human intervention at every critical juncture. From the distinction between rehearsal and deploy, to the manual verification of dashboard logs, the deterministic generation of redirects from `links.csv`, the optional smoke check after a human push, and the strict isolation of sensitive services, each step reinforces the principle that automation serves the human operator, not the other way around [CITE: desk practice — KEEP Tailscale; leave Freqtrade dry_run; LTX inspect-only daytime]. This approach ensures that the transition from local validation to live publication is deliberate, secure, and free from the risks associated with unmonitored bot activity.

*(Affiliate disclosure: This article contains an affiliate disclosure for Cloudflare Pages at the beginning. As an affiliate, I may earn a commission if you purchase through my links, at no extra cost to you.)*
