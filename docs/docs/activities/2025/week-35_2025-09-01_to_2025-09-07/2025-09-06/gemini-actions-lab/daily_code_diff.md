# 💻 Daily Code Changes

## Full Diff

```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
index 5fe2bca..fd62fa1 100644
--- a/.github/workflows/imagen4.yml
+++ b/.github/workflows/imagen4.yml
@@ -1,55 +1,120 @@
-name: Imagen4 via Gemini CLI (MCP)
+name: imagen4-commit-via-gemini-cli
 
 on:
   workflow_dispatch:
     inputs:
-      prompt:
-        description: "画像プロンプト"
+      image_prompt:
+        description: "作りたい画像のプロンプト"
         required: true
+      model:
+        description: "画像生成モデル (imagen-4 / imagen-4-ultra / imagen-3)"
+        default: "imagen-4"
+      num:
+        description: "生成枚数 (1-4)"
+        default: "1"
       aspect_ratio:
-        description: "1:1 | 3:4 | 4:3 | 9:16 | 16:9"
-        required: false
+        description: "アスペクト比 (例: 1:1, 16:9, 9:16, 3:4, 4:3)"
         default: "1:1"
-      model:
-        description: "imagen-4.0-(generate|fast-generate|ultra-generate)-preview-06-06"
+      seed:
+        description: "固定シード（任意）"
         required: false
-        default: "imagen-4.0-fast-generate-preview-06-06"
+
+permissions:
+  contents: write
 
 jobs:
-  generate:
+  generate_and_commit:
     runs-on: ubuntu-latest
+
     steps:
-      - uses: actions/checkout@v4
+      - name: Checkout
+        uses: actions/checkout@v4
+        with:
+          persist-credentials: true
 
-      # Gemini CLI をGitHub Actionsから実行
-      - name: Run Gemini CLI with Imagen4 MCP
-        uses: google-github-actions/run-gemini-cli@v0.1.12
+      - name: Generate images via Gemini CLI (+ Imagen MCP)
+        uses: google-github-actions/run-gemini-cli@v0
         with:
-          # Gemini CLI が読む settings.json をインラインで書き込み
+          gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
+          gemini_model: gemini-2.5-flash
+          gemini_cli_version: latest
+          gemini_debug: true
           settings: |
             {
               "mcpServers": {
-                "gemini-imagen4": {
+                "gemini-imagen": {
                   "command": "npx",
-                  "args": ["gemini-imagen4"],
-                  "env": { "GEMINI_API_KEY": "${{ secrets.GEMINI_API_KEY }}" }
+                  "args": ["-y", "gemini-imagen-mcp-server",
+                           "--output-dir", "generated-images",
+                           "--model", "${{ github.event.inputs.model }}"],
+                  "env": { "GEMINI_API_KEY": "${{ secrets.GEMINI_API_KEY }}" },
+                  "trust": true,
+                  "includeTools": ["generate_image"]
                 }
               }
             }
-          # ここが実際の“指示”。MCPツール名はサーバ側ドキュメント準拠
           prompt: |
-            Use @gemini-imagen4.generate_image_from_text with:
-            prompt="${{ inputs.prompt }}",
-            model="${{ inputs.model }}",
-            aspectRatio="${{ inputs.aspect_ratio }}".
-            Return the saved file paths (./generated-images) and a short summary.
-          gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
-          gemini_cli_version: latest
-          gemini_debug: true
+            Use the @gemini-imagen.generate_image tool to generate ${{ github.event.inputs.num }} image(s)
+            from this prompt: "${{ github.event.inputs.image_prompt }}".
+            Use aspect ratio "${{ github.event.inputs.aspect_ratio }}".
+            If a seed is provided, use it: "${{ github.event.inputs.seed }}".
+            Save files under ./generated-images and list only the filenames.
 
-      - name: Upload generated images
-        if: always()
-        uses: actions/upload-artifact@v4
-        with:
-          name: imagen4-output
-          path: generated-images/**
+      - name: Verify outputs
+        shell: bash
+        run: |
+          set -euo pipefail
+          if [ ! -d generated-images ]; then
+            echo "generated-images not found"; exit 1
+          fi
+          echo "== Generated files =="
+          ls -lh generated-images
+          cnt=$(ls -1 generated-images | wc -l)
+          if [ "$cnt" -lt 1 ]; then
+            echo "No images were generated"; exit 1
+          fi
+
+      - name: Commit directly to branch
+        shell: bash
+        env:
+          GH_USER_NAME: github-actions[bot]
+          GH_USER_EMAIL: 41898282+github-actions[bot]@users.noreply.github.com
+        run: |
+          set -euo pipefail
+
+          DATE_UTC=$(date -u +%Y%m%d)
+          TS_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)
+          DEST="assets/imagen4/${DATE_UTC}-${GITHUB_RUN_ID}"
+          mkdir -p "$DEST"
+
+          cp -v generated-images/* "$DEST"/
+
+          # index.json を安全に生成（式展開はbash側で完結させる）
+          printf '%s\n' "{
+            \"repo\": \"${GITHUB_REPOSITORY}\",
+            \"run_id\": \"${GITHUB_RUN_ID}\",
+            \"run_url\": \"https://github.com/${GITHUB_REPOSITORY}/actions/runs/${GITHUB_RUN_ID}\",
+            \"workflow\": \"${GITHUB_WORKFLOW}\",
+            \"prompt\": \"${{ github.event.inputs.image_prompt }}\",
+            \"model\": \"${{ github.event.inputs.model }}\",
+            \"aspect_ratio\": \"${{ github.event.inputs.aspect_ratio }}\",
+            \"num\": \"${{ github.event.inputs.num }}\",
+            \"seed\": \"${{ github.event.inputs.seed }}\",
+            \"timestamp_utc\": \"${TS_UTC}\"
+          }" > "$DEST/index.json"
+
+          git config user.name  "$GH_USER_NAME"
+          git config user.email "$GH_USER_EMAIL"
+          git add "$DEST"
+
+          if git diff --cached --quiet; then
+            echo "No changes to commit."
+            exit 0
+          fi
+
+          git commit -m "chore(images): add Imagen outputs for run ${GITHUB_RUN_ID}"
+          git push origin "HEAD:${GITHUB_REF_NAME}"
+
+      - name: Show saved path
+        shell: bash
+        run: echo "Saved to: assets/imagen4/$(date -u +%Y%m%d)-${GITHUB_RUN_ID}"
```
