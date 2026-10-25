---
title: "Affiliate allow-list hygiene — links.csv, /go/ redirects, and rejecting invented slugs"
date: 2026-10-25T23:15:20+05:30
draft: false
slug: "affiliate-allow-list-hygiene"
tags: ["affiliate", "hugo", "go-redirects"]
description: "Practical local-AI notes for a 16 GB Apple silicon Mac mini — affiliate links disclosed."
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/).

**Series:** local-AI affiliate desk series (article 15)

> **Disclosure:** This article contains affiliate links to tools I use or recommend. Purchases through them may earn a commission at no extra cost to you.

## Why invented /go/ slugs fail QA

Affiliate redirects are a closed set. If a draft invents a `/go/` path that is not a row in `links.csv`, the click has nowhere honest to land. Locally you may not notice; on Pages the missing rule becomes a 404 or an unintended fallback. Either way the reader loses trust and the disclosure promise is empty for that click.

QA therefore treats orphan slugs as a hard fail, not a polish item. The check is mechanical: collect every `/go/<slug>` from v2-local drafts and from `site/content/posts`, then require each slug to appear in `links.csv`. Anything else is blocked from the dry public tree until it is either removed or added deliberately to the CSV.

Prompt text that says "style: Tool (go-slug)" is instructional, not an affiliate target. Do not add a `slug` row to `links.csv` for that placeholder, and do not leave a real invented product path in body copy "as an example."

## links.csv as the single source of truth

`links.csv` is the allow-list. Columns are `slug,url,note`. The generator accepts lowercase `a-z0-9-` slugs and `https://` destinations only; other rows are skipped.

On this desk the live allow-list is small on purpose: `apple-silicon`, `ollama`, `mlx-audio`, `cloudflare-pages`, `hugo`, `open-webui`, `llama-cpp`. Article bodies may use only the subset named in the brief. New tools wait for a CSV row before they earn a `/go/` weave.

Humans own CSV edits. Bots may regenerate redirects from the file; they do not invent destinations mid-draft.

## affiliate-redirects → static/_redirects (dry)

Never hand-edit `_redirects`. Run:

```bash
affiliate-redirects links.csv site/static/_redirects
```

The script writes a dated header and one `302` line per allow-listed slug. Mirror the same file to the site root copy if your kit keeps both. Confirm the count matches the CSV (seven redirects on the 2026-10-25 desk audit; zero skipped).

This path is dry: it updates local static files only. It is not a Cloudflare publish.

## Hugo local public vs Pages deploy (human gate)

`hugo --minify` may refresh `site/public` for local inspection. That tree is a rehearsal, not a ship. GitHub Pages stays a human gate: review `_redirects`, re-run the allow-list audit, clear claims worksheets, then deploy with a human-owned tool. Daytime agents do not run Pages publish.

Hugo wiring still matters. Every new post should carry only allow-listed `/go/` weaves, keep the disclosure block above the first tool link in the body, and rebuild dry so `public/` matches content.

## Disclosure before the first affiliate click

Place a short disclosure immediately under the title (and series line), before any in-body `/go/` tool link. Titles may mention the `/go/` pattern as a topic; the clickable weaves belong after the disclosure.

Weave tools in-body where they earn context — Ollama for local drafting, Hugo for the static kit, Apple silicon for the quiet desk, mlx-audio for short voice, GitHub Pages for the eventual host — rather than dumping a "Related stack" footer. Prefer the live CSV over memory when a brief names the allow-list.

## Desk checklist before any human ship

1. Audit v2-local drafts and Hugo posts for `/go/` vs `links.csv`.
2. Regenerate `_redirects` with `affiliate-redirects`; do not hand-edit.
3. Dry `hugo --minify`; inspect `public/` locally.
4. Confirm disclosure sits before the first in-body affiliate weave.
5. Leave Cloudflare publish, payments, Tailscale, and Freqtrade alone unless the wake brief says otherwise.

That is allow-list hygiene for this series: CSV owns truth, redirects are generated, Hugo stays dry until a human clears the first public Pages push.
