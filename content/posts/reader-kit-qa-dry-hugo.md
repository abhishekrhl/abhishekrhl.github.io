---
title: "Reader Kit QA — Empty Cites, Thin KEEP Gates, and Local Dry Builds"
date: 2026-10-25
draft: false
---

## The Necessity of a Pre-Publication Audit
Before any content reaches the public eye in this local-AI affiliate series, a rigorous Quality Assurance (QA) pass is mandatory. This eleventh post serves not as new commentary, but as a verification of the writing kit assembled previously. We must ensure that drafts are free from structural flaws, empty citations, and insufficient depth before considering any form of deployment. The philosophy here is strict: nothing deploys to the cloud unless it passes a local dry build. This approach eliminates the risk of live errors, protects sensitive data, and ensures compliance with safety guidelines regarding financial and medical advice.

> **Affiliate Disclosure:** This article contains links to tools and services that may generate revenue for us if you use them. We only recommend products we have tested or believe add genuine value to your workflow. Your support helps maintain this independent series.

## Auditing Empty Citations and Off-topic Content
The first line of defence in our QA process involves a systematic sweep for empty `[CITE: empty-cite marker audit across ebook and blog drafts]` placeholders. In an automated or semi-automated workflow, it is easy to leave citation tags without corresponding sources, which undermines credibility. The audit requires checking every draft instance to ensure that no tag remains void; if a source cannot be verified, the statement must be rephrased or removed rather than leaving a broken reference.

## Enforcing Thin-KEEP Rejection Thresholds
Depth and substance are non-negotiable in this series. To prevent the publication of superficial or skeletal content, we apply quantitative "Thin-KEEP" gates. For a standard article, the word count must exceed 200 words; anything below this threshold is rejected outright as insufficiently developed. Similarly, for longer chapters or extended sections within a post, the minimum requirement rises to 150 words.

These thresholds act as a filter against brevity that sacrifices clarity. A draft that meets the length requirement but lacks nuance still fails, yet these numeric baselines provide an objective starting point. The system must verify that the content density justifies the space occupied, ensuring that readers receive substantive value rather than filler. This discipline maintains the high standard expected of a technical review series focused on practical application.

## Validating Redirects and Link Integrity
When weaving external references into the text, we utilise specific redirect slugs to ensure consistency across the site architecture. Common destinations include `/go/hugo`, `/go/ollama`, `/go/apple-silicon`, `/go/mlx-audio`, and `/go/cloudflare-pages`. These links must be validated against an `allow-list` or a maintained `links.csv` file; we never invent redirects on the fly, as this breaks the deterministic nature of the local build.

Every instance where a redirect is used in the body must correspond exactly to an entry in the source list. If a new tool is introduced, it must first be added to the `allow-list` before appearing in the draft. This prevents "link rot" and ensures that the Hugo site can resolve all paths correctly during the build process without requiring external network access or manual URL correction.

## The Local Dry Build Protocol
Before any content is considered for public deployment, a local dry build is executed using Hugo. This step verifies that the static site generator compiles the HTML successfully without errors. Crucially, this phase occurs entirely offline on the developer's machine. It confirms that all redirects resolve correctly and that no broken links or missing assets prevent the site from rendering.

## What Stays Offline: Secrets and Sensitive Data
Certain categories of information are strictly prohibited from leaving the local development environment. This includes API secrets, trading keys, medical advice, and any live authentication credentials. These elements must never be committed to version control or pushed to a public repository, nor should they appear in a build intended for public consumption.

Even if a dry build succeeds technically, the presence of sensitive data renders the artifact unsafe for publication. The workflow mandates that all such data be scrubbed from the draft before the final check. This ensures that the published series remains safe for readers while protecting the integrity of personal and proprietary information. Only after confirming that no secrets remain does the content proceed to the final approval stage.
