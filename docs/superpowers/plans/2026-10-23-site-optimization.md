# Website optimization implementation plan

Goal: apply the concrete issues from the website audit while retaining the current Jekyll theme and local Docker preview.

Scope: correct routes and old enrollment navigation; responsive header; a complete application entry point using existing contact details; Chinese interface text and semantic headings; page-specific metadata; latest news on the home page; a smaller member portrait; build-time regression checks.

Constraints: preserve existing posts and research data; do not invent admissions deadlines or commitments; keep the current checkout because it contains the new article and is mounted by the user's running preview; no publishing or commits requested. Keep the original portrait. External font hosting and a new publication taxonomy are separate follow-up work.

1. Add generated-HTML checks for local links/fragments, duplicate navigation, language/headings, page sharing metadata and homepage news. Run against the existing build to reproduce audit findings.
2. Repair links and duplicate navigation; redirect the old enrollment URL; add the application section; localize dates/search/navigation; repair headings and accessible names.
3. Fix the header at tablet widths; compact the news intro on mobile; add latest news and a research entry point on the homepage. Generate an optimized portrait without removing its original.
4. Generate canonical URLs, page-specific descriptions/social images and article metadata with JSON escaping; check baseurl handling. Add checks to deployment workflows.
5. Build in Docker, run the full generated-site checks including a subpath build, inspect mobile/tablet/desktop and search/dark mode, request independent review, and address material findings.

Verification: six generated-site checks pass on the local build and a production-mode /preview build. Browser checks at 320px, 820px and 1280px show no horizontal overflow; seven unique nav destinations. Search, dark mode and the application section verified. Independent review identified a missing preview origin, now fixed; delta review found no material issues. The original portrait and detailed center profile remain available. Changes are local and uncommitted.
