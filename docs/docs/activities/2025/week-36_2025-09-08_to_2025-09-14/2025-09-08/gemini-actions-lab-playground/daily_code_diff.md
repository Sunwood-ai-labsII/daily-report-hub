# 💻 Daily Code Changes

## Full Diff

```diff
commit cb40e3cf318eb4c06c77b450cf3ecc5eaf9b06a0
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 23:44:43 2025 +0900

    Update gemini-cli.yml

diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index c0c051d..7c78682 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -200,7 +200,7 @@ jobs:
 
       - name: Run Gemini (pinned + explicit model)
         id: run_gemini
-        uses: google-github-actions/run-gemini-cli@latest # ← アクションをピン留め
+        uses: google-github-actions/run-gemini-cli@v0.1.12 # ← アクションをピン留め
         # ↑↑ 必要なら v0 固定でもOKだが、マイナーの既知安定版を明示推奨
         with:
           # ---- 重要：CLI バージョンを固定して回帰を遮断 ----
```
