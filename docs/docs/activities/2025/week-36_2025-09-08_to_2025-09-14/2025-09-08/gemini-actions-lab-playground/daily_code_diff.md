# 💻 Daily Code Changes

## Full Diff

```diff
commit 37dcb8464c142b6ad70ea54ad6d9b5b44eea428a
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 23:32:21 2025 +0900

    Update gemini-cli.yml

diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 3d6fc1f..b25cac0 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -225,6 +225,13 @@ jobs:
           prompt: ${{ steps.read_prompt.outputs.prompt }}
 
       - name: Fail clearly when secrets are missing
-        if: ${{ failure() && (secrets.GEMINI_API_KEY == '' && (vars.GOOGLE_GENAI_USE_VERTEXAI != 'true')) }}
+        if: ${{ failure() }}
+        env:
+          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
+          USE_VERTEX_AI: ${{ vars.GOOGLE_GENAI_USE_VERTEXAI }}
         run: |
-          echo "::error:: GEMINI_API_KEY が未設定です（Vertex AI を使わない構成の場合は必須）。" && exit 1
+          set -euo pipefail
+          if [[ "${USE_VERTEX_AI}" != "true" && -z "${GEMINI_API_KEY}" ]]; then
+            echo "::error:: GEMINI_API_KEY が未設定です（Vertex AI を使わない構成では必須）。"
+            exit 1
+          fi
```
