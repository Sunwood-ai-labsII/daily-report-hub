# 💻 Daily Code Changes

## Full Diff

```diff
commit eef87b912266c1d6d8a151f160a025bb3a2309be
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sun Aug 24 15:18:40 2025 +0900

    Update and rename gemini-cli-jp.yml to gemini-jp-cli.yml

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
