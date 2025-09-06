# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
index fd62fa1..f5a1c9f 100644
--- a/.github/workflows/imagen4.yml
+++ b/.github/workflows/imagen4.yml
@@ -39,6 +39,7 @@ jobs:
           gemini_model: gemini-2.5-flash
           gemini_cli_version: latest
           gemini_debug: true
+          # ここでは model だけを埋め込み、それ以外は prompt 内で渡す
           settings: |
             {
               "mcpServers": {
@@ -46,18 +47,24 @@ jobs:
                   "command": "npx",
                   "args": ["-y", "gemini-imagen-mcp-server",
                            "--output-dir", "generated-images",
-                           "--model", "${{ github.event.inputs.model }}"],
+                           "--model", "${{ inputs.model }}"],
                   "env": { "GEMINI_API_KEY": "${{ secrets.GEMINI_API_KEY }}" },
                   "trust": true,
                   "includeTools": ["generate_image"]
                 }
               }
             }
+          # ユーザー入力は env で受け渡し、プロンプトに素直に埋め込む
+          env: |
+            PROMPT=${{ inputs.image_prompt }}
+            NUM=${{ inputs.num }}
+            AR=${{ inputs.aspect_ratio }}
+            SEED=${{ inputs.seed }}
           prompt: |
-            Use the @gemini-imagen.generate_image tool to generate ${{ github.event.inputs.num }} image(s)
-            from this prompt: "${{ github.event.inputs.image_prompt }}".
-            Use aspect ratio "${{ github.event.inputs.aspect_ratio }}".
-            If a seed is provided, use it: "${{ github.event.inputs.seed }}".
+            Use the @gemini-imagen.generate_image tool to generate $NUM image(s)
+            from this prompt: "$PROMPT".
+            Use aspect ratio "$AR".
+            If a seed is provided, use it: "$SEED".
             Save files under ./generated-images and list only the filenames.
 
       - name: Verify outputs
@@ -79,6 +86,11 @@ jobs:
         env:
           GH_USER_NAME: github-actions[bot]
           GH_USER_EMAIL: 41898282+github-actions[bot]@users.noreply.github.com
+          PROMPT: ${{ inputs.image_prompt }}
+          MODEL: ${{ inputs.model }}
+          AR: ${{ inputs.aspect_ratio }}
+          NUM: ${{ inputs.num }}
+          SEED: ${{ inputs.seed }}
         run: |
           set -euo pipefail
 
@@ -89,19 +101,20 @@ jobs:
 
           cp -v generated-images/* "$DEST"/
 
-          # index.json を安全に生成（式展開はbash側で完結させる）
-          printf '%s\n' "{
-            \"repo\": \"${GITHUB_REPOSITORY}\",
-            \"run_id\": \"${GITHUB_RUN_ID}\",
-            \"run_url\": \"https://github.com/${GITHUB_REPOSITORY}/actions/runs/${GITHUB_RUN_ID}\",
-            \"workflow\": \"${GITHUB_WORKFLOW}\",
-            \"prompt\": \"${{ github.event.inputs.image_prompt }}\",
-            \"model\": \"${{ github.event.inputs.model }}\",
-            \"aspect_ratio\": \"${{ github.event.inputs.aspect_ratio }}\",
-            \"num\": \"${{ github.event.inputs.num }}\",
-            \"seed\": \"${{ github.event.inputs.seed }}\",
-            \"timestamp_utc\": \"${TS_UTC}\"
-          }" > "$DEST/index.json"
+          # jq で JSON を安全に生成（Ubuntu イメージに jq は標準で入っています）
+          jq -n \
+            --arg repo "$GITHUB_REPOSITORY" \
+            --arg run_id "$GITHUB_RUN_ID" \
+            --arg run_url "https://github.com/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID" \
+            --arg workflow "$GITHUB_WORKFLOW" \
+            --arg prompt "$PROMPT" \
+            --arg model "$MODEL" \
+            --arg aspect_ratio "$AR" \
+            --arg num "$NUM" \
+            --arg seed "$SEED" \
+            --arg ts "$TS_UTC" \
+            '{repo:$repo, run_id:$run_id, run_url:$run_url, workflow:$workflow, prompt:$prompt, model:$model, aspect_ratio:$aspect_ratio, num:$num, seed:$seed, timestamp_utc:$ts}' \
+            > "$DEST/index.json"
 
           git config user.name  "$GH_USER_NAME"
           git config user.email "$GH_USER_EMAIL"
```
