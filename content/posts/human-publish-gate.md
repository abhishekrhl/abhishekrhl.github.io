---
title: "Human publish gate — pack map before any public push"
date: 2026-10-25T23:42:48+05:30
draft: false
slug: "human-publish-gate"
tags: ["publish", "qa", "github-pages"]
description: "This is article 21 in a local-AI affiliate series."
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/).

This is article 21 in a local-AI affiliate series.

**Affiliate Disclosure:** This article contains affiliate links to tools and services I use and recommend. If you click through and make a purchase, I may receive a small commission at no extra cost to you. These funds support the continued development of this project.

In an era defined by rapid automation, where local-AI models generate coherent content in seconds, the final step before making something public often feels like a mere formality. However, when deploying via GitHub Pages, that final step must remain firmly in human hands. We are not merely pushing code; we are publishing ideas, and the integrity of those ideas depends on biological judgment rather than syntactic correctness.

This article details the "human publish gate," a critical checkpoint designed to ensure no automated process deploys content without explicit confirmation. It covers reading the pack map, managing inventories, and distinguishing between technical success and editorial readiness before touching the deployment button. The goal is maintaining a rigorous boundary where technology accelerates creation but never replaces the responsibility of publication.

## Why a human still owns the Pages button

While CI/CD pipelines excel at handling syntax errors, linting issues, and asset linking, they are blind to semantic validity and strategic alignment. A model might generate perfectly formatted Markdown that argues a logically flawed point or hallucinates a non-existent study. The CI pipeline builds this content because the code is valid; it cannot judge whether the argument holds water.

Clarifying roles is essential: GitHub Pages is merely the delivery mechanism, the high-performance edge network responsible for serving static files to users. It has no agency regarding *what* is published or *when*. The human remains the sole author of the publish decision. As noted in the project's internal documentation (HUMAN-STEPS-PENDING.txt — shell listing of v2-local drafts), removing this file signals readiness, but its presence enforces a pause requiring conscious intervention. This ensures the "publish" action is an intentional act of curation, not a passive result of a completed build cycle.

## Desk order: articles inventory then audio inventory then soft notes

First, verify the **articles inventory**. Confirm all markdown files exist within the local directory structure and link correctly within the Hugo (/go/hugo) structure. Using `hugo` to generate the site preview allows you to navigate proposed links before they go live. If a reference points to a non-existent file or broken image path, the build fails or produces a 404 error. This step ensures structural integrity but does not guarantee content quality (hugo documentation — standard static generation guidelines).

Second, audit the **audio inventory**. In a multimedia workflow, transcriptions must match timestamps precisely. Ensure audio assets are hosted reliably and corresponding text files align with the spoken word. A mismatch creates a disjointed user experience where the reader cannot verify what was said or the listener cannot find the relevant section. Reliable hosting is crucial; using tools like mlx-audio (/go/mlx-audio) (mlx-audio — local inference library for audio models) can significantly speed up local processing of these large audio files, ensuring generation and embedding do not introduce latency or corruption into the final package.

Finally, process **soft notes**. These are ephemeral thoughts, rough drafts, and incomplete ideas that may never reach publication but must be accounted for in the local workspace. They serve as a raw data dump of intellectual exploration. By segregating them from the final article inventory, you maintain a clean distinction between "ready for public consumption" and "working notes." This separation prevents soft noise from cluttering the signal intended for the audience.

## Reading gap count vs soft notes without conflating them

Conversely, a **soft note** is an incomplete thought or speculative idea that does not block publication but indicates areas for future refinement. For example, a soft note might say "I need to verify the source of this statistic later" without actually providing the statistic yet. While important for future accuracy, it does not necessarily warrant a deploy freeze if the current context remains coherent and the lack of data is clearly flagged as speculative.

Avoid conflating the two: do not treat an unresolved soft note as a critical error warranting a deployment halt, nor should you ignore a reading gap in the pursuit of speed. The distinction lies in the impact on the user's ability to understand and trust the content. As outlined in the claims quality assurance checklist (claims-qa-checklist — worksheets list claims but are not proof), only gaps preventing logical continuity or factual verification should trigger a "do not publish" status. Soft notes remain part of the iterative improvement cycle, separate from the gatekeeping function.

## Dry Hugo success as necessary-not-sufficient

The static site generator operates on a syntactic level. It checks if tags are closed, if frontmatter is formatted correctly, and if assets are found. It does not read for truth. Therefore, a successful build tells you only that the *container* is sound, not that the *content* inside is valid. Technical stability does not equate to editorial readiness.

Consider a scenario where an AI generates a comprehensive article on a technical topic but cites a study that does not exist. The Hugo build passes because the citation link might resolve to a generic placeholder or the error might be masked in the preview. However, upon publication, this constitutes misinformation. The pack map must be intellectually sound, not just syntactically valid. Relying solely on the build output as a proxy for quality is a dangerous assumption that bypasses the very human judgment we are trying to protect.

## Explicit do-not-publish-yet checklist (CF + claims QA)

**GitHub Pages Check:** Verify DNS propagation and ensure no staging conflicts exist. It is easy to accidentally push changes to a production environment intended for testing, or vice versa. Confirm domain resolution is correct and the specific branch you are deploying from matches the expected state. Ensure no other team members or automated scripts are pushing conflicting updates simultaneously.

**Claims QA:** Cross-reference every factual assertion against primary sources. This is the most critical step. Every statistic, name, date, and technical claim must be verified. Mark any unverified statement clearly within the text before deployment. If a claim cannot be substantiated with a reliable source, remove it or flag as speculative until evidence is found. Do not let the allure of a completed build pressure you into publishing uncertain information.

The workflow looks like this:
1. Check `HUMAN-STEPS-PENDING.txt`. If it exists, stop and review.
2. Run `hugo` to ensure the site builds without syntax errors.
3. Audit the articles inventory for broken links and logical flow.
4. Audit the audio inventory for timestamp alignment and asset reliability.
5. Scan for reading gaps that halt understanding.
6. Verify all claims against primary sources (primary-source-verification — human CF + claims QA publish checklist).

By maintaining this rigorous gate, we protect our audience from hallucinations and errors, ensuring content served via GitHub Pages is not just technically functional, but intellectually honest. The button to publish remains in your hand, waiting for your confirmation that the pack map is complete and claims are sound. Related stack notes: /go/ollama, /go/apple-silicon.
