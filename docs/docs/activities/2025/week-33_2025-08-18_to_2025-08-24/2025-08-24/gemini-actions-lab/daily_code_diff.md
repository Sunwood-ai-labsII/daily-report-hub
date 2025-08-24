# 💻 Daily Code Changes

## Full Diff

```diff
commit 1209c071e647f9e14f5cf638003a9fbff868012f
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sun Aug 24 13:54:03 2025 +0900

    Update gemini-issue-automated-triage.yml

diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index 6914b92..4c85ade 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -5,9 +5,6 @@ on:
     types:
       - 'opened'
       - 'reopened'
-  issue_comment:
-    types:
-      - 'created'
   workflow_dispatch:
     inputs:
       issue_number:
```
