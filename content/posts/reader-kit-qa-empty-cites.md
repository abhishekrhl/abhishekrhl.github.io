---
title: "Reader Kit QA — empty cites, thin KEEP gates, and local dry builds"
date: 2026-10-25T23:42:48+05:30
draft: false
slug: "reader-kit-qa-empty-cites"
tags: ["qa", "hugo", "local-ai"]
description: "These thresholds filter out brevity that sacrifices clarity. A draft meeting length requirements but lacking nuance still fails. These numeric baselines prov…"
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/).

## The Pre-Publication Audit
Before deploying any content in this local-AI series, a rigorous QA pass is mandatory. This post verifies the writing kit assembled previously. Drafts must be free from structural flaws, empty citations, and insufficient depth before deployment. The rule is strict: nothing deploys to the cloud unless it passes a local dry build on my 16 GB Apple Silicon Mac mini. This eliminates live errors, protects data, and ensures compliance with safety guidelines regarding financial and medical advice.

> **Affiliate Disclosure:** This article contains links to tools that may generate revenue if you use them. We only recommend products tested in our workflow or believed to add genuine value. Your support helps maintain this independent series.

## Auditing Empty Citations
The first step involves a systematic sweep for empty `(...)` placeholders. In an automated workflow, it is easy to leave tags without sources, which undermines credibility. Every draft instance must be checked; if a source cannot be verified against the local reference list, the statement must be rephrased or removed. No void tags remain in the final output.

## Enforcing Thin-KEEP Rejection Thresholds
Depth and substance are non-negotiable. To prevent superficial content, we apply quantitative "Thin-KEEP" gates. For a standard article, word count must exceed 200 words; anything below is rejected outright. For longer chapters or extended sections within a post, the minimum requirement rises to 150 words.

These thresholds filter out brevity that sacrifices clarity. A draft meeting length requirements but lacking nuance still fails. These numeric baselines provide an objective starting point. The system verifies content density justifies the space occupied, ensuring readers receive substantive value rather than filler. This discipline maintains the high standard expected of a technical review series focused on practical application.

## Validating Redirects and Link Integrity
When weaving external references into the text, we utilise specific redirect slugs to ensure consistency across the site architecture. Common destinations include `/go/hugo`, `/go/ollama`, `/go/apple-silicon`, `/go/mlx-audio`, and `/go/github-pages`. These links must be validated against an `allow-list` or a maintained `links.csv` file; we never invent redirects on the fly, as this breaks the deterministic nature of the local build.

Every instance where a redirect is used in the body must correspond exactly to an entry in the source list. If a new tool is introduced, it must first be added to the `allow-list` before appearing in the draft. This prevents "link rot" and ensures that the Hugo site can resolve all paths correctly during the build process without requiring external network access or manual URL correction.

## The Local Dry Build Protocol
Before any content is considered for public deployment, a local dry build is executed using Hugo. This step verifies that the static site generator compiles the HTML successfully without errors. Crucially, this phase occurs entirely offline on the developer's machine. It confirms that all redirects resolve correctly and that no broken links or missing assets prevent the site from rendering.

## What Stays Offline: Secrets and Sensitive Data
Certain categories of information are strictly prohibited from leaving the local development environment. This includes API secrets, trading keys, medical advice, and any live authentication credentials. These elements must never be committed to version control or pushed to a public repository, nor should they appear in a build intended for public consumption.

Even if a dry build succeeds technically, the presence of sensitive data renders the artifact unsafe for publication. The workflow mandates that all such data be scrubbed from the draft before the final check. This ensures that the published series remains safe for readers while protecting the integrity of personal and proprietary information. Only after confirming that no secrets remain does the content proceed to the final approval stage.
