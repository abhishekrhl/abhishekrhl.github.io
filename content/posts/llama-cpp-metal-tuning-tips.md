---
title: "Squeezing Performance: A Practical Guide to `llama.cpp` Metal Tuning on Apple Silicon"
date: 2026-10-28T14:34:54+05:30
draft: false
slug: "llama-cpp-metal-tuning-tips"
tags: ["local-ai", "apple-silicon", "ollama"]
description: "Local AI desk note — quality-gated draft."
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/). AI-assisted drafting runs on a local Ollama desk; a human still gates claims before public ship.

A 16 GB Mac mini stalls when the model weights and context window collectively exceed available unified memory, forcing the system to swap data to disk. This post delivers a concrete checklist for balancing GPU offloading (`-ngl`), context size, and batch parameters to maintain stable tokens-per-second without triggering crashes.

---

This post contains affiliate links to hardware and software tools. As a participant in relevant affiliate programmes, I may earn a commission from qualifying purchases at no extra cost to you. This does not influence my recommendations; all advice is based on local testing on Apple Silicon.

# Squeezing Performance: A Practical Guide to `llama.cpp` Metal Tuning on Apple Silicon

## The 16 GB Memory Budget: Why Unified Memory Matters

Your M1, M2, or M3 Mac mini presents a specific constraint: unified memory. Unlike systems with discrete GPUs and separate RAM pools, Apple Silicon shares the same address space for both CPU and GPU. When you run `llama.cpp`, the model weights occupy a fixed portion of this pool, while the context window (the history of tokens) consumes the remainder. If the sum of these allocations plus the batch processing buffer exceeds 16 GB, the operating system intervenes by swapping data to the SSD. This process introduces latency that effectively kills performance, turning what should be rapid inference into a sluggish crawl.

Consequently, you must treat your 16 GB budget as a hard ceiling. A common failure mode involves loading a large model with an excessively long context, leaving insufficient space for the batch size. The result is frequent stalling or complete application termination. To avoid this, you must calculate the maximum viable configuration before launching the model. You are not merely guessing; you are allocating finite resources against competing demands.

For further details on selecting models that fit within these constraints, see [content-pillars-models-2026-10-25.md](~/AI/notes/content-pillars-models-2026-10-25.md).

## Calculating Your `-ngl` Limit

The most critical parameter for performance on Apple Silicon is the number of layers offloaded to the GPU, specified via the `-ngl` flag. While it might seem beneficial to offload every layer possible, doing so risks exceeding the available memory if your context window is large. The standard rule of thumb for 16 GB systems is to reserve approximately 4–5 GB for the model weights and an additional 2–3 GB for the context and batch buffer.

For a 7B parameter model (roughly 5 GB in quantised form), you can typically offload all layers safely, as the remaining memory accommodates a reasonable context. However, with a 13B or larger model, you must be more conservative. If your chosen model requires 6 GB of RAM for weights, you have only 8–9 GB left for everything else. In this scenario, pushing `-ngl` to the maximum (e.g., `--n-gpu-layers 52`) might still cause swapping if the context is large.

A practical approach is to set `-ngl` to match the total layer count of the model unless you are running a very long context. If you intend to maintain a context window of 4096 tokens or more, consider reducing `-ngl` by a few layers (e.g., setting it to `--n-gpu-layers 38` for a 52-layer model) to ensure the CPU handles the overflow without triggering memory pressure. This slight reduction in GPU parallelism often yields higher overall throughput because it prevents the system from swapping.

## Context Window vs. Batch Size: The Speed Trade-off

Distinguishing between `--ctx-size` and `--batch-size` is essential for optimising speed on limited hardware. The context window (`--ctx-size`) defines how many tokens the model remembers; this is a static memory allocation that remains in use throughout the session. A larger context allows for better long-form reasoning but consumes valuable RAM that could otherwise be used for processing new tokens.

Conversely, the batch size (`--batch-size`) dictates how many tokens are processed simultaneously during inference. On a 16 GB system, increasing this value improves tokens-per-second (t/s) up to a point, after which memory fragmentation or swapping occurs. The optimal starting point for a 16 GB Mac mini is usually between 512 and 1024, depending on your context size. If you set `--ctx-size` to 8192, you should likely cap `--batch-size` at 512 or lower to leave room for the model weights and intermediate calculations.

Attempting to maximise both simultaneously often leads to instability. Prioritise a context size that meets your specific writing needs first; only then adjust the batch size to extract maximum speed from the remaining headroom. For example, if you require 4096 tokens for summarising documents, set `--ctx-size 4096` and test `--batch-size 512`. If performance is sluggish, increase the batch size incrementally until you observe a drop in t/s or system instability.

## Flash Attention and the Metal Backend

The `--flash-attn` flag offers significant speed improvements on NVIDIA GPUs using CUDA, but its utility on Apple Silicon's Metal backend is nuanced. While recent versions of `llama.cpp` include experimental Metal implementations for flash attention, these are not yet as mature or universally stable as their CUDA counterparts. On a 16 GB system, enabling this flag without verifying version compatibility can introduce subtle bugs or unexpected memory spikes that lead to crashes.

The safest initial configuration is to run inference without `--flash-attn`. This ensures baseline stability across different model versions and quantisations. Only after confirming that the core parameters (`-ngl`, `--ctx-size`, `--batch-size`) are optimised should you consider enabling flash attention. If you do test it, monitor memory usage closely; any increase in peak RAM consumption suggests the implementation is less efficient than standard attention on your specific hardware configuration.

For a deeper dive into model selection strategies, refer to [content-pillars-models-2026-10-25.md](~/AI/notes/content-pillars-models-2026-10-25.md).

## The `mlock` Safety Net

The `mlock` flag instructs the operating system to lock model weights into physical RAM, preventing them from being swapped to disk. This is vital for maintaining consistent performance, as swapping introduces massive latency spikes. However, on a 16 GB Mac mini, enabling `mlock` without precise memory budgeting can cause immediate application crashes if the total required memory exceeds the physical limit.

Use `mlock` only after you have calculated your exact memory footprint using tools like `ps` or Activity Monitor. The command typically looks like this:

```bash
./main -m model.gguf --n-gpu-layers 38 --ctx-size 4096 --batch-size 512 --mlock
```

If the sum of model weights, context window, and batch buffer exceeds 16 GB, enabling `mlock` will result in an "Out of memory" error or a forced kill from the system. In such cases, you must reduce either the context size or the number of offloaded layers before re-enabling `mlock`. Treat this flag as a final safety measure rather than a default setting for constrained hardware.

For more details on privacy-focused setups, see [content-pillars-privacy-2026-10-25.md](~/AI/notes/content-pillars-privacy-2026-10-25.md).

---

### Summary Checklist

*   **Memory Budget:** Ensure `Model Weights` + `Context Window` + `Batch Buffer` < 16 GB.
*   **GPU Offloading:** Set `-ngl` to total layers unless context size is large; reduce slightly if swapping occurs.
*   **Batch Size:** Start at 512 for long contexts; increase only if memory allows.
*   **Flash Attention:** Disable initially; enable only after confirming stability on your specific `llama.cpp` version.
*   **mlock:** Enable only after verifying total RAM usage stays within physical limits.

### Further Reading

*   [content-pillars-hardware-2026-10-25.md](~/AI/notes/content-pillars-hardware-2026-10-25.md)
*   [content-pillars-setup-2026-10-25.md](~/AI/notes/content-pillars-seo-2026-10-25.md)

### Next Steps

If you found these tuning parameters useful, consider joining the local askai community to share your own benchmarks and configurations. You can also download the full local inference checklist for a comprehensive reference guide. For regular updates on hardware optimisation and model releases, subscribe to the monthly newsletter.
