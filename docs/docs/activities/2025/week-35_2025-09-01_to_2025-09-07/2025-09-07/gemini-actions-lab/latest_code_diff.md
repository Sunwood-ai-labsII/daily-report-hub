# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 56e56dd..9b2d7fa 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -76,7 +76,7 @@ jobs:
       github.event_name == 'issues' && github.event.action == 'opened' &&
       contains(github.event.issue.body, '@gemini-cli')
 
-          timeout-minutes: 10
+    timeout-minutes: 10
     runs-on: 'ubuntu-latest'
     steps:
       - name: 'Debug Event Information'
```
