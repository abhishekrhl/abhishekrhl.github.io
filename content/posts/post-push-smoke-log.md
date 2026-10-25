---
title: "Post-push smoke log — verify /go/ hits without a second deploy"
date: 2026-10-25T23:42:48+05:30
draft: false
slug: "post-push-smoke-log"
tags: ["qa", "github-pages", "affiliate"]
description: "In my workflow on the 16 GB Apple silicon Mac mini, \"deployment\" often carries too much weight. It implies code commits, build triggers, container rebuilds, …"
---

> **Affiliate disclosure:** Some links are affiliate links. As an Amazon Associate I earn from qualifying purchases. See [Disclosure](/disclosure/).

In my workflow on the 16 GB Apple silicon Mac mini, "deployment" often carries too much weight. It implies code commits, build triggers, container rebuilds, and live updates that alter system behaviour for end-users. However, within our specific operational stack, there is a distinct practice known as the post-push smoke log. This is not a deployment event; it is a verification exercise. The objective is to record hits without triggering a second deploy, ensuring infrastructure stability while confirming documentation links remain valid after code changes are pushed but before re-configuration occurs.

The distinction between a production deploy and a smoke log lies in intent. A standard deploy is an active intervention designed to change state: pushing new binaries, updating database schemas, or modifying routing tables. In contrast, the post-push `/go/` smoke run is strictly observational. It serves as a manual audit trail rather than an automated pipeline step that alters the live environment.

When I execute a smoke log against my local-AI setup, I am not asking the system to render new content or update configuration files. I am simply querying existing endpoints to verify reachability and response codes. This approach mitigates "deployment fatigue," where constant rebuilds can inadvertently introduce errors or destabilise dependent services. By treating the smoke log as a passive inspection, I ensure the verification process does not become a source of side effects. It is a snapshot in time—a confirmation that what was pushed remains accessible—without committing to the overhead of a full release cycle.

Consistency is paramount. To maintain this, the scope of testing is restricted exclusively to URLs listed in `links.csv`. This manifest acts as the single source of truth for which endpoints require verification. I do not wander into dynamic routes, unlisted API endpoints, or experimental paths not pre-defined in the CSV file.

The goal is to validate specific static assets and documented links explicitly approved for the public interface. By adhering strictly to the `links.csv` manifest, I ensure smoke log results are comparable with previous deployment rehearsals. If a path exists in the codebase but not in the CSV, it is ignored during this phase. Conversely, every entry in the CSV must be hit to confirm its current state. This discipline prevents scope creep and ensures the audit remains focused on the documented user process rather than the entire underlying infrastructure.

First, the HTTP status code provides an immediate binary signal. A `200` OK indicates successful retrieval. A `301` Moved Permanently suggests a structural routing change, warranting investigation into the canonical URL. A `404` Not Found is a definitive indicator that a link has broken, requiring immediate attention to fix the source or remove it from the manifest.

Second, I note any redirect targets observed during the request cycle. In a well-configured static site, redirects should be predictable and lead to canonical versions of pages. Unexplained loops or unexpected destinations indicate configuration drift. I rely on helper scripts to generate static redirection files based on this CSV data to ensure consistency.

Soft-cites refer to references that are contextual rather than hard-coded facts, often used in documentation to describe capabilities or methodologies. While a broken link (404) is a technical failure, an outdated claim about a tool's capability is a content issue. The smoke log captures only the former. It confirms the URL exists and responds correctly but does not verify if the information presented on that page is still current or accurate.

To prevent confusion, claims worksheets and soft-cite tracking remain separate documents from the smoke results. Mixing these concerns conflates technical stability with informational validity. By keeping them distinct, I ensure a failed smoke log entry clearly indicates a routing issue, while a separate review process validates the substance of the content itself. This separation ensures the audit trail remains clean and actionable.

Specific systems within my architecture must be explicitly excluded from this verification cycle. These components are either internal networking tools or time-sensitive processes that should not be interfered with during a standard smoke log audit.

First, I leave Tailscale untouched. As an internal networking tool for secure remote access, it operates outside the public-facing scope of the `/go/` verification cycle. Including it in a public smoke log would expose internal topology details and is unnecessary for validating external documentation links.

Finally, I treat daytime  Local Large Language Text ( Triggering these processes or routing traffic through them during a smoke log could interfere with their scheduled execution windows. The `/go/` path verification is limited to static assets and defined routes, ensuring dynamic AI processing pipelines remain undisturbed.

Within this constrained scope, certain paths require specific handling based on the local-AI stack. When the smoke log encounters a `/go/ollama` endpoint, it verifies the accessibility of the Ollama server integration points documented in the site. Similarly, requests to `/go/hugo` confirm that the static site generator's configuration pages are reachable and correctly configured for the current build version.

For hardware-specific documentation on my 16 GB Mac mini, paths such as `/go/apple-silicon` are critical. These routes often point to architecture-specific guides or performance benchmarks. A successful hit here confirms device-specific instructions have not been orphaned by a generic site update. When audio processing capabilities are documented, the `/go/mlx-audio` path serves as a checkpoint for machine learning framework integrations, ensuring links to audio model documentation remain valid.

Cloud infrastructure documentation is also subject to this audit. The `/go/github-pages` route verifies that deployment-specific instructions or CDN configuration guides are still active. This is particularly important in a post-push scenario where DNS records or edge configurations might have been updated alongside the code push. By hitting these specific slugs, I ensure the bridge between the developer environment and the hosting platform remains intact without requiring a full re-deployment of application logic.

The philosophy behind this smoke log is minimal intervention. I observe, record, and report. I do not fix issues during the log run; I simply capture the state of the system as it exists at that moment. If a link returns a 404, it is logged as such, and the correction is addressed in a subsequent development cycle. This prevents "fix-it-now" behaviour from introducing new bugs or changing build output unexpectedly.

In the context of local-AI operations where resources are finite and schedules are tight, this disciplined approach ensures verification does not become a bottleneck. It allows me to push updates with confidence, knowing the immediate aftermath can be audited efficiently through a lightweight, non-intrusive smoke log. The result is an audit trail that documents reachability without altering the very system it is inspecting.
