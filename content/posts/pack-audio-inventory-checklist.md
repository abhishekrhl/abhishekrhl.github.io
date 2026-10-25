---
title: "Pack audio inventory checklist — wav ↔ soft-cite alignment before dry Hugo"
date: 2026-10-25T23:42:48+05:30
draft: false
slug: "pack-audio-inventory-checklist"
tags: ["audio", "qa", "hugo"]
description: "This is article 19 in a local-AI workflow series on a 16 GB Apple silicon Mac mini."
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/).

This is article 19 in a local-AI workflow series on a 16 GB Apple silicon Mac mini.

**Affiliate Disclosure:** This article references tools we use or recommend. Clicking `/go/` links may result in a commission at no extra cost to you. We only endorse tools evaluated for practical utility in our own stack.

### Why wav ↔ soft-cite alignment matters before dry Hugo

Ensuring every generated audio snippet maps strictly to its source text prevents hallucinated claims in the final build. The issue arises when a local inference engine, such as one running via `/go/ollama`, generates speech from a prompt lacking sufficient grounding. If the model is not constrained by a strict mapping between the audio waveform and the specific paragraph it represents, it may introduce information absent from the source document. This is dangerous in technical contexts where accuracy is paramount. Misaligned waveforms risk propagating unverified statements when rendered via `/go/ollama` or similar local engines, effectively turning a reliable static site into a vehicle for misleading audio content. The audio becomes a black box that speaks without reference, breaking the chain of trust established by the written text.

Alignment acts as a safety valve, ensuring spoken output remains faithful to the documented script before deployment. We treat the soft-cite not merely as a hyperlink but as a binding contract between the audio asset and its textual origin (desk practice — spoken claims inherit body soft-cites only). If a claim in the script lacks a corresponding source reference marked by a filled soft-cite with a lookup hint, that segment must be treated as suspect. By enforcing this alignment prior to the build process, we create a filter stopping unverified content from entering the pipeline. This is far more effective than auditing the final site for inconsistencies after the fact, especially when dealing with dynamic or generated assets.

### Checklist rows: script words, Kokoro disclose footer, /go/ allow-list, empty CITE scan

The checklist rows required to maintain this integrity focus on four key areas: script words, Kokoro disclosure footers, the `/go/` allow-list, and empty soft-cite marker scans.

First, verify that every word in the script corresponds to an existing entry in the source document for traceability. This ensures the audio is a direct representation of documented facts rather than a drift-prone summary or paraphrase. Second, confirm the presence of the mandatory Kokoro disclosure footer pattern from `voiceover.sh` on posts shipping synthetic clips (voiceover.sh footer — Kokoro Apache-2.0 disclose synthetic voice). Regulatory standards increasingly demand clear labeling when AI generates human-like speech; omitting this can lead to compliance issues and erode user trust. Third, cross-reference generated assets against the `/go/` allow-list (e.g., `/go/hugo`, `/go/apple-silicon`) to ensure only approved paths are processed (links.csv allow-list — /go/ slugs only from CSV rows). This prevents accidental execution of unvetted tools introducing security risks into the build environment. Finally, scan for empty soft-cite markers within the script. An empty citation is a red flag suggesting the model generated content without a clear anchor; such segments must be flagged for immediate review or deletion.

### Inventory file layout beside pack-inventory-articles.md

The inventory file layout beside `pack-inventory-articles.md` follows a structured approach to manage these assets efficiently. Structure `pack-inventory-audio.md` to mirror the row-based format of `pack-inventory-articles.md` for consistent parsing (pack-inventory-audio.md beside pack-inventory-articles.md). This parallel structure allows automated scripts or human auditors to switch between text and audio inventories without confusion. Include columns mapping stem, script word count, wav presence, soft-cite count, and status so a desk scan can spot gaps without inventing pass ratios. Maintain this inventory locally on the Mac mini to facilitate quick audits without rebuilding the entire site structure. By keeping this metadata separate, we decouple validation logic from content generation logic, allowing granular control over the deployment pipeline.

### Fail closed: missing soft-cite → omit spoken claim

Fail closed: missing soft-cite → omit spoken claim (no invention) is the governing principle for our audio processing strategy. Implement a strict rule where any spoken claim lacking a valid body soft-cite is omitted from the abstract — no invention (fail-closed — missing soft-cite omit spoken claim). This approach prioritises safety and accuracy over completeness; it is better to have a site with slightly less audio coverage than one containing unverified claims. Treat missing citations as a failure condition rather than a warning, ensuring no unverified claims reach production. In software engineering terms, this is a "fail-closed" system, where the default state in the face of uncertainty is to deny access or execution. This guarantees that the final site contains only content backed by explicit source references. If a model generates a sentence about a specific statistic without a corresponding citation in the source text, that audio clip must be discarded. We do not attempt to guess the source or patch the citation later; the absence of evidence is treated as evidence of absence regarding the validity of the claim.

### Dry Hugo still ≠ Pages publish

Running `hugo --minify` locally via `/go/hugo` is merely a validation gate and does not constitute a live deployment to `/go/github-pages` (desk practice — dry hugo --minify before human Pages push). Many developers assume that if a local build completes without errors, the site is ready for public consumption. However, a successful dry run confirms structural integrity but leaves the actual hosting environment untouched until an explicit deploy command is issued. The local build validates that inventory files are correct and soft-cite alignment checks have passed, but it does not push content to the edge network or configure necessary caching strategies. Do not assume local build success implies readiness for public consumption or edge caching. There is a distinct phase between generating static files locally on the Mac mini and publishing them to a distributed edge network served globally. Each phase requires its own set of checks.

Local inference on `/go/apple-silicon` with `/go/ollama` and speech via `/go/mlx-audio` still inherits the same allow-list and inventory gates; dry Hugo success never replaces the human GitHub Pages decision.
