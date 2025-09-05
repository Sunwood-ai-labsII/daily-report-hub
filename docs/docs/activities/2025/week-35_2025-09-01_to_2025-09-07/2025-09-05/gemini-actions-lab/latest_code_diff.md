# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
new file mode 100644
index 0000000..5fe2bca
--- /dev/null
+++ b/.github/workflows/imagen4.yml
@@ -0,0 +1,55 @@
+name: Imagen4 via Gemini CLI (MCP)
+
+on:
+  workflow_dispatch:
+    inputs:
+      prompt:
+        description: "画像プロンプト"
+        required: true
+      aspect_ratio:
+        description: "1:1 | 3:4 | 4:3 | 9:16 | 16:9"
+        required: false
+        default: "1:1"
+      model:
+        description: "imagen-4.0-(generate|fast-generate|ultra-generate)-preview-06-06"
+        required: false
+        default: "imagen-4.0-fast-generate-preview-06-06"
+
+jobs:
+  generate:
+    runs-on: ubuntu-latest
+    steps:
+      - uses: actions/checkout@v4
+
+      # Gemini CLI をGitHub Actionsから実行
+      - name: Run Gemini CLI with Imagen4 MCP
+        uses: google-github-actions/run-gemini-cli@v0.1.12
+        with:
+          # Gemini CLI が読む settings.json をインラインで書き込み
+          settings: |
+            {
+              "mcpServers": {
+                "gemini-imagen4": {
+                  "command": "npx",
+                  "args": ["gemini-imagen4"],
+                  "env": { "GEMINI_API_KEY": "${{ secrets.GEMINI_API_KEY }}" }
+                }
+              }
+            }
+          # ここが実際の“指示”。MCPツール名はサーバ側ドキュメント準拠
+          prompt: |
+            Use @gemini-imagen4.generate_image_from_text with:
+            prompt="${{ inputs.prompt }}",
+            model="${{ inputs.model }}",
+            aspectRatio="${{ inputs.aspect_ratio }}".
+            Return the saved file paths (./generated-images) and a short summary.
+          gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
+          gemini_cli_version: latest
+          gemini_debug: true
+
+      - name: Upload generated images
+        if: always()
+        uses: actions/upload-artifact@v4
+        with:
+          name: imagen4-output
+          path: generated-images/**
```
