---
title: "Deploy rehearsal notes — what a human does on GitHub Pages after sign-off"
date: 2026-10-25T23:42:48+05:30
draft: false
slug: "deploy-rehearsal-github-pages"
tags: ["github-pages", "publish", "hugo"]
description: "This is article 23 in a local-AI affiliate series."
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/).

This is article 23 in a local-AI affiliate series.

*Disclosure: This article contains an affiliate disclosure for GitHub Pages at the end. As an affiliate, I may earn a commission if you purchase through my links, at no extra cost to you.*

In my workflow on the Mac mini (16 GB unified memory), the boundary between preparation and execution is strict. Local validation does not equal global state change. This note covers the human intervention required after sign-off in GitHub Pages. Specifically, why rehearsal notes are never a deploy, how redirects rely strictly on `links.csv`, and why critical systems like Tailscale remain immune to automated traffic patterns (claims-worksheet-sign-off — prior article 22 human gate before rehearsal).

## Why Rehearsal Notes Are Not a Deploy

A signed worksheet confirms logic holds under local scrutiny, but it lacks the agency to alter live production databases or trigger edge functions across the distributed network. Running `hugo --minify` (located at `/go/hugo`) serves only as a build artifact for review; it is a static compilation step designed to verify syntax and asset integrity, not a production push mechanism (hugo-dry-status.md — dry --minify green still not Pages ready). The distinction lies in the "dry" boundary. Local execution prevents accidental data mutation or external API calls during testing phases. This isolation ensures errors are contained within the developer's machine, preventing cascading failures that could affect end-users (HUMAN-STEPS-PENDING.txt — human CF Pages path; bots never click publish).

## Dashboard Path a Human Walks After Sign-off

The first step involves inspecting build logs directly in the GitHub Pages dashboard. While local builds provide immediate feedback, the GitHub Pages environment introduces variables a local machine cannot simulate, such as edge function latency, specific runtime constraints, or network topology differences between my node and the global edge. I must confirm these logs show no runtime errors before proceeding. It is not enough for the build to succeed locally; it must succeed in the target environment (desk practice — optional /go/ smoke after a human push only).

Following log inspection, I verify the "Production" branch is clean. This involves checking commit history to ensure no unintended changes were merged or pushed during the rehearsal phase. Only after this manual verification do I initiate the deployment action. This step is non-negotiable; it ensures the state of the production environment is explicitly approved by a person who understands the context of the changes. The dashboard path is not merely UI traversal; it is a security checkpoint where automation stops and human judgment resumes (HUMAN-STEPS-PENDING.txt — human CF Pages path; bots never click publish).

## _redirects Regenerated from links.csv Only

The regeneration process is deterministic. Given the same input data, the output is always identical. This reliance on `links.csv` as the single source of truth prevents drift between the intended routing structure and actual configuration. During rehearsal, the system reads this CSV, processes entries, and generates a temporary `_redirects` file for local testing. If the CSV contains invalid paths or conflicting rules, the local build fails or highlights the discrepancy, but no changes persist to the live environment (affiliate-redirects helper — writes static/_redirects from links.csv).

This approach ties routing configuration directly to a data file that undergoes its own review process. By doing so, we create a chain of custody for every redirect rule. There are no "magic" paths hidden in the code; every URL jump is traceable back to a specific entry in `links.csv`. This reduces the attack surface for misconfiguration and ensures the live environment reflects exactly what was validated during rehearsal (links.csv allow-list — regenerate _redirects from CSV rows only).

## Optional /go/ Smoke Checklist After a Human Push

Short voice abstracts are rendered later with mlx-audio (`/go/mlx-audio`); they summarise the rehearsal, they do not publish it.

Following the human-initiated push to the production branch, I conduct an optional smoke test to verify core service availability. This check targets a lightweight endpoint, such as `/go/`, which serves as a minimal health indicator (desk practice — optional /go/ smoke after a human push only). The purpose is to confirm the application loaded successfully and responds without triggering complex operational logic or sensitive data processing.

The role of this `/go/` endpoint is strictly observational. It returns a simple status signal indicating the server is up, allowing me to proceed with confidence. However, automated bots must never trigger this checklist independently. The smoke test requires explicit human confirmation; it is part of the final release gate, not an autonomous background task (HUMAN-STEPS-PENDING.txt — human CF Pages path; bots never click publish).

By requiring a human push before the smoke test runs, I ensure the decision to expose the system to public traffic is deliberate. This prevents scenarios where a bot might misinterpret local success as global readiness and initiate checks that could destabilise the environment if something subtle has gone wrong. The steps are straightforward: access the endpoint, observe response time and status code, and confirm no errors appear in the logs. This lightweight check provides assurance without risking sensitive operational logic or consuming significant computational resources (desk practice — optional /go/ smoke after a human push only).

## What Bots Must Never Click (And Why Tailscale/Freqtrade Stay Untouched)

Prose for this series is drafted through the local Ollama stack on Apple silicon (`/go/ollama`); that does not grant bots a Pages click.

`Tailscale` creates secure mesh networks for internal services, while `freqtrade` manages algorithmic trading strategies or similar high-stakes operations [CITE: desk practice — KEEP Tailscale; leave Freqtrade dry_run;  Exposing these systems to automated traffic, even for "inspection," introduces unnecessary risk. A bot might inadvertently trigger a rate limit, misinterpret a status code, or execute a command intended only for manual review. The security rationale is clear: bots document the rehearsal, but humans retain exclusive control over live production assets [CITE: desk practice — KEEP Tailscale; leave Freqtrade dry_run; 

Daytime inspection of these systems is strictly limited to human operators who can interpret data context and understand potential impact. Automated scripts are kept away from these domains to prevent unintended service disruption. Even if a bot detects an anomaly in the logs, it lacks authority to interact with `tailscaled` or `freqtrade`. This separation ensures sensitive infrastructure remains protected behind human decision-making [CITE: desk practice — KEEP Tailscale; leave Freqtrade dry_run; 

In summary, the deployment process prioritises safety through human intervention at every critical juncture. From distinguishing rehearsal from deploy, to manual verification of dashboard logs, deterministic generation of redirects from `links.csv`, optional smoke checks after a human push, and strict isolation of sensitive services, each step reinforces that automation serves the operator, not the other way around [CITE: desk practice — KEEP Tailscale; leave Freqtrade dry_run;  This ensures the transition from local validation to live publication is deliberate, secure, and free from unmonitored bot activity.

*(Affiliate disclosure: This article contains an affiliate disclosure for GitHub Pages at the beginning. As an affiliate, I may earn a commission if you purchase through my links, at no extra cost to you.)*
