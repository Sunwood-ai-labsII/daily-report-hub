# 💻 Daily Code Changes

## Full Diff

```diff
commit b4216a37be9bea46abc6b808c628951d3379719d
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 23:41:39 2025 +0900

    Update gemini-cli.yml

diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 613b206..c0c051d 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -200,7 +200,7 @@ jobs:
 
       - name: Run Gemini (pinned + explicit model)
         id: run_gemini
-        uses: google-github-actions/run-gemini-cli@v0.1.12  # ← アクションをピン留め
+        uses: google-github-actions/run-gemini-cli@latest # ← アクションをピン留め
         # ↑↑ 必要なら v0 固定でもOKだが、マイナーの既知安定版を明示推奨
         with:
           # ---- 重要：CLI バージョンを固定して回帰を遮断 ----
```
