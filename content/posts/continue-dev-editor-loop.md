---
title: "Running local AI on 16 GB Apple silicon: avoiding the second model fight"
date: 2026-10-25T23:15:20+05:30
draft: false
slug: "continue-dev-editor-loop"
tags: ["local-ai", "continue-dev", "ollama"]
description: "Practical local-AI notes for a 16 GB Apple silicon Mac mini — affiliate links disclosed."
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/).

This is article 05 of a local-AI series. Some links may generate revenue at no extra cost; we recommend only what we use or trust.

The core challenge on a 16 GB Mac mini is avoiding a "second heavy model fight." While Ollama (`/go/ollama/`) works in the terminal, it creates friction regarding context management and RAM allocation compared to dedicated editor extensions. Running models directly in the CLI demands manual prompt injection—system instructions, history, and file contents—which causes mental fatigue. If context drifts during long-form drafting, output degrades frequently, losing the thread of argument or code logic.

A dedicated extension like Continue.dev acts as a lightweight bridge between your local inference engine and the editor environment. It does not replace the heavy model but manages its interaction with the workspace. The primary advantage is context retention: the extension maintains session history within the IDE, knowing which files are open and what the immediate task is. This delivers rich, structured prompts without manual copy-pasting.

Resource allocation is critical here. Even on Apple Silicon (`/go/apple-silicon/`) using Ollama, loading multiple instances or managing separate processes can strain RAM. Continue handles orchestration, fetching only necessary code snippets and conversation turns for the prompt sent to the running model. This reduces overhead; you do not need a second instance of the model just for a conversational UI.

Continue.dev solves this bottleneck by offloading completion logic to an extension that talks to a single running model. The extension handles the UI side—pop-up suggestions and command palette integration—while the local server handles inference. This ensures only one inference engine is active per task, resulting in smoother performance and reduced RAM overhead. You avoid scenarios where two heavy models fight for dominance over your hardware.

This setup is particularly relevant for writers with an established local stack. If you use Open WebUI (`/go/open-webui/`) for general chat or Llama.cpp (`/go/llama-cpp/`) for specific inference tasks, adding a raw CLI workflow can feel disjointed. Continue integrates into the editor loop, understanding file structure and current code lines. When requesting completions, it provides suggestions contextually aware of immediate surroundings, reducing cognitive load in long documents.

The extension manages the context window intelligently better than raw CLI sessions. In a terminal, pasting an entire document often exceeds token limits or causes the model to lose focus on the specific line being edited. Continue allows selecting text ranges or referencing specific files, constructing prompts that include only necessary details. This precision keeps the model focused and prevents hallucinations based on irrelevant background information.

For Apple Silicon users, memory management is critical. While unified memory supports larger context windows than many consumer PCs, inefficient usage can still lead to swapping or slowdowns. Using an extension that optimises prompt construction ensures the model receives dense, high-value information rather than padded text. This efficiency maximises local hardware utility without constant re-prompting or manual context injection.

Ultimately, the decision rests on workflow integration versus raw flexibility. If your goal is rapid code or document writing without interruption, the extension offers a superior path. It removes manual prompt management friction, keeping the model's attention on immediate tasks. This approach avoids latency spikes from running multiple heavy models simultaneously, delivering local completions that feel native to your editor rather than like an external tool fighting for resources.

When a Hugo (`/go/hugo/`) build or overnight video window is active, keep the editor model quiet so compile and render jobs stay light.

## Pointing the editor at a local Ollama endpoint

Configure the editor to talk only to a local Ollama (`/go/ollama/`) endpoint on localhost. Prefer binding to `127.0.0.1` so prompts never leave the machine. Confirm the port is free before starting a second runner. (source: local bind 127.0.0.1 privacy practice)

## One-model rule while drafting

While drafting in the editor, keep a single model loaded. Use Open WebUI (`/go/open-webui/`) for exploratory chat in a separate session, not as a second heavy load beside Continue.

## Disclosure and human rewrite
