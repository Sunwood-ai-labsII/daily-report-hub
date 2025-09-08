# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 16acaf6..f23f691 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -118,6 +118,7 @@ jobs:
         env:
           GITHUB_ACTOR: ${{ github.actor }}
           GITHUB_TOKEN: ${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}
+          GH_TOKEN: ${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}
           ISSUE_NUMBER: ${{ steps.get_context.outputs.issue_number }}
           REPOSITORY: ${{ github.repository }}
         run: |
@@ -130,6 +131,7 @@ jobs:
         id: get_description
         env:
           GITHUB_TOKEN: ${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}
+          GH_TOKEN: ${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}
           IS_PR: ${{ steps.get_context.outputs.is_pr }}
           ISSUE_NUMBER: ${{ steps.get_context.outputs.issue_number }}
         run: |
@@ -149,6 +151,7 @@ jobs:
         id: get_comments
         env:
           GITHUB_TOKEN: ${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}
+          GH_TOKEN: ${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}
           IS_PR: ${{ steps.get_context.outputs.is_pr }}
           ISSUE_NUMBER: ${{ steps.get_context.outputs.issue_number }}
         run: |
@@ -202,6 +205,10 @@ jobs:
         id: run_gemini
         uses: google-github-actions/run-gemini-cli@v0 # ← アクションをピン留め
         # ↑↑ 必要なら v0 固定でもOKだが、マイナーの既知安定版を明示推奨
+        env:
+          # ← ここで “両方” を与えるのがポイント
+          GITHUB_TOKEN: ${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}
+          GH_TOKEN: ${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}
         with:
           # ---- 重要：CLI バージョンを固定して回帰を遮断 ----
           gemini_cli_version: 'latest'                  # ← 直近で動いた版に固定（例）
@@ -218,6 +225,7 @@ jobs:
           gcp_service_account: ${{ vars.SERVICE_ACCOUNT_EMAIL }}
           use_vertex_ai: ${{ vars.GOOGLE_GENAI_USE_VERTEXAI }}
           use_gemini_code_assist: ${{ vars.GOOGLE_GENAI_USE_GCA }}
+          
           settings: |
             {
               "debug": true,
```
