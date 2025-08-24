# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-cli-jp.yml b/.github/workflows/gemini-jp-cli.yml
similarity index 99%
rename from .github/workflows/gemini-cli-jp.yml
rename to .github/workflows/gemini-jp-cli.yml
index 858f00e..f9a7772 100644
--- a/.github/workflows/gemini-cli-jp.yml
+++ b/.github/workflows/gemini-jp-cli.yml
@@ -1,6 +1,9 @@
 name: '💬 Gemini CLI (日本語版)'
 
 on:
+  issues:
+    types:
+      - 'opened'
   pull_request_review_comment:
     types:
       - 'created'
```
