# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index fb89603..af6a92f 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -200,7 +200,7 @@ jobs:
 
       - name: Run Gemini (pinned + explicit model)
         id: run_gemini
-        uses: google-github-actions/run-gemini-cli@v0.1.12 # ← アクションをピン留め
+        uses: google-github-actions/run-gemini-cli@v0.1.10 # ← アクションをピン留め
         # ↑↑ 必要なら v0 固定でもOKだが、マイナーの既知安定版を明示推奨
         with:
           # ---- 重要：CLI バージョンを固定して回帰を遮断 ----
```
