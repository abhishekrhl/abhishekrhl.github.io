---
title: "Soft-cite discipline — filling empty [CITE:] without inventing sources"
date: 2026-10-25T18:22:25+05:30
draft: false
tags: ["local-ai","affiliate","apple-silicon"]
---

# Soft-cite discipline — filling empty [CITE:] without inventing sources

**Series:** local-AI affiliate desk series (article 16)

This is article 16 in our local-AI affiliate series.

> **Disclosure:** This article contains affiliate links to tools I use or recommend. Purchases through them may earn a commission at no extra cost to you.

In the rush to accelerate content generation with local-AI workflows, a subtle but dangerous habit can creep in: leaving citation placeholders empty or filling them with fabricated details. In technical writing and journalism, an honest placeholder is a visible flag for human review; a filled-but-wrong source is a silent error that silently damages credibility. We must distinguish between an AI's probabilistic suggestion and a factual guarantee. When an AI model generates text, it predicts the next token based on patterns in its training data, not by accessing a verified database of current facts. Therefore, every assertion made by the model requires a human gatekeeper to confirm its origin and accuracy before publication.

## The danger of silent invention

The primary risk in automated drafting is the temptation to treat an empty `[CITE:]` tag as acceptable or to fill it with a plausible-sounding but non-existent URL. An empty bracket is a deliberate signal: "I have made a claim, but I do not yet know the source; please verify this." It invites scrutiny. Conversely, filling that bracket with a hallucinated title or a fake DOI creates a false sense of authority. Readers trust a citation; if they click a link expecting a primary source and find a dead end or an irrelevant paper, their trust in the entire article evaporates.

This distinction is critical when using local models running on hardware like Apple silicon (/go/apple-silicon) via frameworks such as mlx-audio (/go/mlx-audio) or general inference engines. The model does not "know" facts; it guesses context. If the prompt asks for a statistic regarding energy efficiency, the model might confidently output a number and attach an empty `[CITE:]`. If the workflow then auto-fills that slot with a random URL from the training set, the article becomes technically impressive but factually hollow. The discipline required is to treat every empty `[CITE:]` as a mandatory checkpoint, not an optional footnote.

## Extract-claims worksheets: Lists are not proof

An extract-claims sheet is essentially a scratchpad for hypotheses. It records *what* was said, but not *where* it came from or *if* it is true. Relying on such a list as proof of research is akin to keeping a shopping list and claiming the groceries have been delivered; the list exists, but the delivery (the evidence) has not yet occurred. In rigorous scientific publishing, the standard for evidence is exceptionally high. For instance, consider the stringent peer-review processes required for careful technical publishing, where every claim should be backed by a checkable primary source **[CITE: extract-claims.sh header reminder — worksheets list claims, do not verify]**.

In a local-AI workflow, the extract-claims sheet should function as a to-do list for verification, not a certificate of truth. The human author must take each item on that list, locate the primary source in a database or repository, and confirm that the text actually supports the specific claim being made. Only then can the soft-cite marker be resolved with confidence. Until that manual step is completed, the claim remains unverified, regardless of how many times it appears in a spreadsheet.

## The division of labour: Bots fill hints, humans verify facts

The most effective workflow for maintaining integrity is a clear division of labour between the bot and the human. The AI's role should be strictly limited to generating "soft-cite" hints. This means the model identifies where a claim likely needs support and suggests a lookup string or a partial URL based on its training data, leaving the final resolution open. It might suggest: `[CITE: replace off-topic model hint with topic-relevant lookup]`.

## Technical enforcement via /go/ allow-list

To prevent the accidental invention of URLs, we can implement a structural guardrail using an allow-list mechanism for internal links. In our publishing stack, we restrict direct linking to only those slugs defined in our `links.csv` file. [CITE: /go/ slugs must match links.csv allow-list] We achieve this by enforcing a `/go/` prefix on all hyperlinks within the content.

This constraint ensures that citations must resolve only to pre-approved paths. If an AI model attempts to invent a URL for a source that does not exist in our system, it cannot generate a valid `/go/` link because the slug is not present in the allowed list. This forces the model to either leave the citation empty (triggering a human review) or use a known, verified internal path.

For example, if we are discussing local deployment options, we can safely link to our documentation using Ollama (/go/ollama). Similarly, if we discuss our static site generator configuration, we reference Hugo (/go/hugo). This approach prevents the AI from hallucinating arbitrary URLs like `https://example.com/fake-paper` or creating non-existent internal pages. It acts as a hard boundary: if the link is not in the list, it cannot be rendered.

This mechanism is particularly useful when integrating with deployment platforms like Cloudflare Pages (/go/cloudflare-pages). By ensuring that all outgoing links are pre-validated slugs, we reduce the risk of broken links or malicious redirects in the final build. It shifts the burden of URL validity from the probabilistic model to a deterministic configuration file. However, one must remember that this list is merely an allow-list; it does not inherently validate external facts, only internal navigation paths **[CITE: links.csv allow-list vs body /go/ audit]**.

## Dry Hugo and the human gate

Therefore, no article should reach the staging environment without manual verification of all `[CITE: claims-qa checklist 2026-10-25 — publish gate = canonical finals]` entries. The "human gate" must occur before the build is pushed. We must ensure that every placeholder has been either resolved with a verified source or removed entirely. Relying on the build process alone to catch factual errors is a critical failure mode. Automation speeds up the compilation, but it cannot replace the cognitive verification required to own the truth **[CITE: desk practice — dry hugo --minify before human Pages push]**.

## Conclusion: Discipline over automation

The path to reliable output in an automated world requires discipline over pure automation. We must accept that local-AI models are powerful drafters but unreliable fact-checkers. By adopting a soft-cite discipline where empty `[CITE:]` tags are treated as mandatory flags for human review, we maintain integrity without sacrificing speed.

We utilise extract-claims worksheets not as proof, but as roadmaps for verification. We leverage technical constraints like the `/go/` allow-list to prevent invented URLs, ensuring that every link points to a known entity in our `links.csv`. Whether we are discussing the nuances of running models on Apple silicon, configuring **Hugo** locally, or deploying via **Cloudflare Pages**, the underlying principle remains the same: the machine suggests, but the human decides.

In this ecosystem, bots fill hints and humans verify facts. Automation is a tool for amplifying our reach and efficiency, not a replacement for our responsibility. The final reminder stands firm: while automation speeds up drafting, humans must own the truth. Only through rigorous, manual verification of every citation hint can we ensure that our content remains credible, accurate, and trustworthy in an increasingly automated landscape.

