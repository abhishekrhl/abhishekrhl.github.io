---
title: "Avoiding Swap Thrash: Batch Drafting AI Content on a 16 GB Mac mini Without Compromising Freqtrade"
date: 2026-10-26T14:34:08+05:30
draft: false
slug: "batch-drafting-without-swap-thrash"
tags: ["local-ai", "apple-silicon", "ollama"]
description: "Local AI desk note — quality-gated draft."
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/). AI-assisted drafting runs on a local Ollama desk; a human still gates claims before public ship.

Your 16 GB Mac mini will enter swap thrash if you stack large `askai` contexts alongside an open browser and IDE while Freqtrade runs in the background. This post delivers a concrete workflow to generate multiple drafts without halting your trading bot or crashing the system. See also [local-llm-memory-optimization](~/AI/notes/local-llm-memory-optimization.md).

***

This post discusses the use of local AI tools on specific hardware configurations. Any references to third-party software or services are for informational purposes only. I may receive commissions on affiliate links, but this does not influence my technical recommendations. Always verify compatibility with your specific hardware and software versions.

# Avoiding Swap Thrash: Batch Drafting AI Content on a 16 GB Mac mini Without Compromising Freqtrade

## The 16 GB Reality Check

You cannot treat 16 GB of unified memory as an infinite pool when running macOS, a local LLM, a web browser, and a trading bot simultaneously. Apple Silicon allocates this memory dynamically, but the system reserves a portion for the kernel, background services, and the "free MB floor" required to prevent thrashing. When you attempt to load a 128k context window into `askai` while Chrome holds onto gigabytes of tab data and your IDE indexes codebases, the available free memory collapses rapidly. Once this floor drops below a critical threshold—often around 2 GB on a stressed 16 GB machine—the OS begins swapping aggressively to the SSD. This process introduces latency spikes that can stall Freqtrade's heartbeats or cause it to miss critical market signals, effectively halting your strategy execution until memory is reclaimed.

## The Anti-Pattern

The most common failure mode involves the "stacking drafts" approach: keeping a persistent `askai` session open with a massive conversation history while simultaneously researching in the browser and coding in an IDE. Users often believe that because the model is already loaded, adding new prompts incurs zero marginal cost. In reality, every new draft request expands the context window, pushing memory usage higher. When you combine this with a browser full of research tabs and an IDE actively editing files, the system quickly exhausts its usable RAM. The result is not just slow generation; it is complete swap thrash. Your fan speeds will max out, disk activity will spike to 100%, and your Freqtrade bot may pause or fail to process new candles due to CPU starvation caused by the OS prioritising memory paging over application logic. This anti-pattern renders the local setup unstable for any workflow requiring sustained multi-tool usage.

## The `ai-window` Strategy

To maintain stability, you must utilise the `ai-window` feature to isolate generation tasks rather than relying on a single, bloated context history. Instead of appending every research note and previous draft to one long conversation, create distinct, lightweight windows for each drafting session. This technique caps the maximum memory footprint of any individual LLM instance, ensuring that even if you generate five drafts in succession, the total allocated RAM remains predictable and bounded. By keeping the active context window small and focused on the immediate task, you preserve a larger "free MB floor" for the browser, IDE, and Freqtrade. This isolation prevents one heavy generation burst from cascading into a system-wide memory crisis, allowing you to work continuously without triggering swap thrash.

## Protecting Freqtrade

Your trading bot must never be allowed to compete with local AI inference for CPU cycles or memory bandwidth during intensive drafting sessions. The protocol is simple but strict: pause or isolate the Freqtrade instance before initiating a batch of AI generations. You can do this by stopping the bot via the command line, disabling specific strategies in the configuration, or simply closing the terminal window if it is not actively monitoring the market. While the model is generating content, the system should dedicate its resources entirely to inference and I/O operations. Once the drafting session concludes and you have saved your drafts, resume Freqtrade immediately. This ensures that your trading logic runs on a stable thermal headroom and without the risk of being starved by background swapping or high-priority AI processes.

## One-at-a-Time Workflow

The most reliable method for maintaining stability on constrained hardware is an iterative, single-draft approach. Do not attempt to generate a full article in one go; instead, produce one paragraph or section at a time within a fresh `ai-window`. This minimises the context overhead for each request and keeps the overall memory consumption low. After generating a segment, save it to your local file system, close the AI window, and then open a new one for the next section. This workflow guarantees that you never exceed the safe memory threshold, keeping swap thrash at bay while allowing you to produce substantial content over time. It is a slower process than bulk generation on 64 GB machines, but it is the only way to guarantee consistent performance on a 16 GB Mac mini without compromising your trading bot's integrity.

## Summary of Actions

1.  **Define your budget**: Assume 8–10 GB is available for applications; do not exceed this.
2.  **Isolate contexts**: Use `ai-window` to keep individual sessions under 4 GB.
3.  **Pause trading**: Stop Freqtrade before starting heavy AI workloads.
4.  **Iterate**: Generate one section at a time, save, and reset the context.

By adhering to this workflow, you transform your Mac mini from a fragile experiment into a reliable local production environment. You gain the benefits of privacy and zero-latency inference without sacrificing the stability required for live trading strategies.

## Further Reading

*   [Quiet Desk Setup Guide](~/AI/notes/qiet-desk-setup-guide.md)
*   [Local LLM Configuration](~/AI/notes/local-llm-configuration.md)
*   [Freqtrade Deployment Checklist](~/AI/notes/freqtrade-deployment-checklist.md)
*   [Memory Management Best Practices](~/AI/notes/memory-management-best-practices.md)
