# 💻 Daily Code Changes

## Full Diff

```diff
commit a859e11d68408b15cbbd6cbc187f92098f02972d
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Tue Sep 9 00:05:59 2025 +0900

    Update gemini-cli.yml

diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index af6a92f..b58b174 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -200,7 +200,7 @@ jobs:
 
       - name: Run Gemini (pinned + explicit model)
         id: run_gemini
-        uses: google-github-actions/run-gemini-cli@v0.1.10 # ← アクションをピン留め
+        uses: google-github-actions/run-gemini-cli@v0 # ← アクションをピン留め
         # ↑↑ 必要なら v0 固定でもOKだが、マイナーの既知安定版を明示推奨
         with:
           # ---- 重要：CLI バージョンを固定して回帰を遮断 ----
```
