---
title: "Post-push /go/ smoke log — recording hits without a second deploy"
date: 2026-10-25T20:39:51+05:30
draft: false
tags: ["local-ai","affiliate","apple-silicon"]
---

# Post-push /go/ smoke log — recording hits without a second deploy

This is article 24 in a local-AI affiliate series.

*Disclosure: This article contains affiliate links marked with `/go/`. If you click these and make a purchase, I may receive a small commission at no extra cost to you. Your support helps sustain this documentation project.*

In the ecosystem of modern static site generation and local AI orchestration, the concept of "deployment" often carries an unwarranted weight. It implies a cascade of actions: code commits, build triggers, container rebuilds, and finally, a live update that alters the behaviour of the system for end-users. However, within our specific operational workflow, there exists a distinct practice known as the post-push smoke log. This is not a deployment event; it is a verification exercise. The objective is to record hits without triggering a second deploy, ensuring that the infrastructure remains stable while confirming that documentation links remain valid after code changes have been pushed but before any potential re-configuration occurs.

### Why a smoke log is not another deploy

The fundamental distinction between a production deployment and a smoke log lies in intent and consequence. A standard deploy is an active intervention designed to change state. It pushes new binaries, updates database schemas, or modifies routing tables. In contrast, the post-push `/go/` smoke run is strictly observational. It serves as a manual audit trail rather than an automated pipeline step that alters the live environment.

When we execute a smoke log against our local-AI setup, we are not asking the system to render new content or update configuration files. We are simply querying existing endpoints to verify their reachability and response codes. This approach mitigates the risk of "deployment fatigue," where constant rebuilds can inadvertently introduce errors or destabilise dependent services. By treating the smoke log as a passive inspection, we ensure that the verification process does not become a source of side effects. It is a snapshot in time—a confirmation that what was pushed remains accessible—without committing to the overhead of a full release cycle [CITE: desk practice — smoke log is not another deploy].

### Which /go/ paths to hit (links.csv only)

Consistency is paramount in any audit procedure. To maintain this, the scope of our testing is restricted exclusively to URLs listed in `links.csv`. This manifest acts as the single source of truth for which endpoints require verification. We do not wander into dynamic routes, unlisted API endpoints, or experimental paths that were not pre-defined in the CSV file [CITE: links.csv allow-list — hit only /go/ slugs listed in CSV].

The goal here is to validate specific static assets and documented links that have been explicitly approved for inclusion in the public interface. By adhering strictly to the `links.csv` manifest, we ensure that our smoke log results are comparable with previous deployment rehearsals. If a path exists in the codebase but not in the CSV, it is ignored during this phase. Conversely, every entry in the CSV must be hit to confirm its current state. This discipline prevents scope creep and ensures that the audit remains focused on the documented user journey rather than the entire underlying infrastructure [CITE: desk practice — record status, redirect target, time IST].

### What to write down (status, redirect target, time IST)

First, the HTTP status code provides an immediate binary signal of success or failure. A `200` OK indicates that the resource was successfully retrieved. A `301` Moved Permanently suggests a structural change in the routing, which warrants further investigation into the canonical URL. A `404` Not Found is a definitive indicator that a link has broken, requiring immediate attention to either fix the source or remove it from the manifest.

Second, we note any redirect targets observed during the request cycle. In a well-configured static site, redirects should be predictable and lead to canonical versions of pages. Unexplained loops or unexpected destinations can indicate configuration drift. We rely on helper scripts to generate static redirection files based on this CSV data to ensure consistency [CITE: affiliate-redirects helper — writes static/_redirects from links.csv].

### How soft-cites and claims worksheets stay separate from smoke results

Soft-cites refer to references that are contextual rather than hard-coded facts, often used in documentation to describe capabilities or methodologies. While a broken link (404) is a technical failure, an outdated claim about a tool's capability is a content issue. The smoke log captures only the former. It confirms that the URL exists and responds correctly but does not verify if the information presented on that page is still current or accurate.

To prevent confusion, claims worksheets and soft-cite tracking remain separate documents from the smoke results. Mixing these concerns would conflate technical stability with informational validity. By keeping them distinct, we ensure that a failed smoke log entry clearly indicates a routing issue, while a separate review process is required to validate the substance of the content itself. This separation of duties ensures that the audit trail remains clean and actionable [CITE: hugo-dry-status.md — dry --minify green still not Pages ready].

### Still leave alone: Tailscale, Freqtrade dry_run, daytime LTX

There are specific systems within our architecture that must be explicitly excluded from this verification cycle. These components are either internal networking tools or time-sensitive processes that should not be interfered with during a standard smoke log audit [CITE: deploy-rehearsal-notes — prior article 23 optional /go/ smoke after human push].

First, we leave Tailscale untouched. As an internal networking tool used for secure remote access, it operates outside the public-facing scope of the `/go/` verification cycle. Including it in a public smoke log would expose internal topology details and is unnecessary for validating external documentation links.

Finally, we treat daytime LTX processes as out-of-scope. Local Large Language Text (LTX) operations often run on specific schedules during daylight hours to handle user queries or background tasks. Triggering these processes or attempting to route traffic through them during a smoke log could interfere with their scheduled execution windows. The `/go/` path verification is limited to static assets and defined routes, ensuring that dynamic AI processing pipelines remain undisturbed.

### Navigating the /go/ ecosystem

Within this constrained scope, certain paths are frequently encountered and require specific handling based on the nature of the local-AI stack. When the smoke log encounters a `/go/ollama` endpoint, it is verifying the accessibility of the Ollama server integration points documented in the site [CITE: desk practice — smoke log is not another deploy]. Similarly, requests to `/go/hugo` confirm that the static site generator's configuration pages are reachable and correctly configured for the current build version.

For hardware-specific documentation, paths such as `/go/apple-silicon` are critical. These routes often point to architecture-specific guides or performance benchmarks. A successful hit here confirms that the device-specific instructions have not been orphaned by a generic site update. When audio processing capabilities are documented, the `/go/mlx-audio` path serves as a checkpoint for machine learning framework integrations, ensuring that links to audio model documentation remain valid [CITE: desk practice — record status, redirect target, time IST].

Cloud infrastructure documentation is also subject to this audit. The `/go/cloudflare-pages` route verifies that deployment-specific instructions or CDN configuration guides are still active [CITE: HUMAN-STEPS-PENDING.txt — human CF Pages path; bots never click publish]. This is particularly important in a post-push scenario where DNS records or edge configurations might have been updated alongside the code push. By hitting these specific slugs, we ensure that the bridge between the developer environment and the hosting platform remains intact without requiring a full re-deployment of the application logic.

### Maintaining operational discipline

The philosophy behind this smoke log is one of minimal intervention. We observe, we record, and we report. We do not fix issues during the log run; we simply capture the state of the system as it exists at that moment. If a link returns a 404, it is logged as such, and the correction is addressed in a subsequent development cycle. This prevents "fix-it-now" behaviour from introducing new bugs or changing the build output unexpectedly.

In the context of local-AI operations where resources are often finite and schedules are tight, this disciplined approach ensures that verification does not become a bottleneck. It allows teams to push updates with confidence, knowing that the immediate aftermath can be audited efficiently through a lightweight, non-intrusive smoke log. The result is a robust audit trail that documents reachability without altering the very system it is inspecting.
