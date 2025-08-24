# 🔄 Latest Code Changes

```diff
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
