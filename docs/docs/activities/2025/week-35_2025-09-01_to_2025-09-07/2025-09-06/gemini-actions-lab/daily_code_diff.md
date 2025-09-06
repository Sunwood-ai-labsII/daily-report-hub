# 💻 Daily Code Changes

## Full Diff

```diff
diff --git a/.github/workflows/imagen-generate-and-commit.yml b/.github/workflows/imagen-generate-and-commit.yml
new file mode 100644
index 0000000..a1a254c
--- /dev/null
+++ b/.github/workflows/imagen-generate-and-commit.yml
@@ -0,0 +1,153 @@
+name: "🎨 imagen4-commit-via-gemini-cli"
+
+on:
+  workflow_dispatch:
+    inputs:
+      image_prompt:
+        description: '作りたい画像のプロンプト'
+        required: true
+        default: 'A beautiful Japanese landscape with cherry blossoms and mountains'
+      model:
+        description: '画像生成モデル (imagen-4 / imagen-4-ultra / imagen-3)'
+        required: false
+        default: 'imagen-4'
+      num:
+        description: '生成枚数'
+        required: false
+        default: '2'
+      aspect_ratio:
+        description: 'アスペクト比 (例: 1:1, 16:9, 9:16)'
+        required: false
+        default: '1:1'
+      seed:
+        description: 'シード値 (オプション)'
+        required: false
+        default: ''
+
+jobs:
+  generate_and_commit:
+    runs-on: ubuntu-latest
+    
+    permissions:
+      contents: write
+      
+    steps:
+      - name: Checkout repository
+        uses: actions/checkout@v4
+        with:
+          token: ${{ secrets.GITHUB_TOKEN }}
+
+      - name: Create output directory
+        run: |
+          mkdir -p generated-images
+          echo "Created generated-images directory"
+          ls -la
+
+      - name: Generate images via Gemini CLI (+ Imagen MCP)
+        uses: google-github-actions/run-gemini-cli@v0
+        env:
+          NUM: ${{ github.event.inputs.num }}
+          PROMPT: ${{ github.event.inputs.image_prompt }}
+          AR: ${{ github.event.inputs.aspect_ratio }}
+          SEED: ${{ github.event.inputs.seed }}
+        with:
+          gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
+          gemini_model: gemini-2.5-flash
+          gemini_debug: true
+          settings: |
+            {
+              "mcpServers": {
+                "gemini-imagen": {
+                  "command": "npx",
+                  "args": ["-y", "gemini-imagen-mcp-server",
+                           "--output-dir", "generated-images",
+                           "--model", "${{ github.event.inputs.model }}"],
+                  "env": { "GEMINI_API_KEY": "${{ secrets.GEMINI_API_KEY }}" },
+                  "trust": true,
+                  "includeTools": ["generate_image"]
+                }
+              }
+            }
+          prompt: |
+            Use the @gemini-imagen.generate_image tool to generate ${{ github.event.inputs.num }} image(s)
+            from this prompt: "${{ github.event.inputs.image_prompt }}".
+            Use aspect ratio "${{ github.event.inputs.aspect_ratio }}".
+            ${{ github.event.inputs.seed != '' && format('If a seed is provided, use it: "{0}".', github.event.inputs.seed) || '' }}
+            Save files under ./generated-images and list only the filenames.
+
+      - name: Verify generated files
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
+          echo "✅ Successfully generated $cnt file(s)"
+
+      - name: Add metadata file
+        run: |
+          cat > generated-images/metadata.json << EOF
+          {
+            "generation_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
+            "prompt": "${{ github.event.inputs.image_prompt }}",
+            "model": "${{ github.event.inputs.model }}",
+            "num_images": ${{ github.event.inputs.num }},
+            "aspect_ratio": "${{ github.event.inputs.aspect_ratio }}",
+            "seed": "${{ github.event.inputs.seed }}",
+            "workflow_run": "${{ github.run_number }}",
+            "commit_sha": "${{ github.sha }}"
+          }
+          EOF
+          echo "Created metadata file:"
+          cat generated-images/metadata.json
+
+      - name: Commit and push generated images
+        run: |
+          git config --local user.email "action@github.com"
+          git config --local user.name "GitHub Action"
+          
+          git add generated-images/
+          
+          if git diff --staged --quiet; then
+            echo "No changes to commit"
+          else
+            git commit -m "🎨 Generate images via Gemini Imagen API
+            
+            Prompt: ${{ github.event.inputs.image_prompt }}
+            Model: ${{ github.event.inputs.model }}
+            Images: ${{ github.event.inputs.num }}
+            Aspect ratio: ${{ github.event.inputs.aspect_ratio }}
+            Seed: ${{ github.event.inputs.seed }}
+            Generated at: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
+            
+            git push
+            echo "✅ Successfully committed and pushed generated images"
+          fi
+
+      - name: Upload generated images as artifacts
+        uses: actions/upload-artifact@v4
+        if: always()
+        with:
+          name: generated-images-${{ github.run_number }}
+          path: generated-images/
+          retention-days: 30
+
+      - name: Create workflow summary
+        run: |
+          echo "## 🎨 Image Generation Summary" >> $GITHUB_STEP_SUMMARY
+          echo "" >> $GITHUB_STEP_SUMMARY
+          echo "**Prompt:** ${{ github.event.inputs.image_prompt }}" >> $GITHUB_STEP_SUMMARY
+          echo "**Model:** ${{ github.event.inputs.model }}" >> $GITHUB_STEP_SUMMARY
+          echo "**Number of Images:** ${{ github.event.inputs.num }}" >> $GITHUB_STEP_SUMMARY
+          echo "**Aspect Ratio:** ${{ github.event.inputs.aspect_ratio }}" >> $GITHUB_STEP_SUMMARY
+          echo "**Seed:** ${{ github.event.inputs.seed || 'Random' }}" >> $GITHUB_STEP_SUMMARY
+          echo "" >> $GITHUB_STEP_SUMMARY
+          echo "### Generated Files" >> $GITHUB_STEP_SUMMARY
+          echo "\`\`\`" >> $GITHUB_STEP_SUMMARY
+          ls -la generated-images/ >> $GITHUB_STEP_SUMMARY
+          echo "\`\`\`" >> $GITHUB_STEP_SUMMARY
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
deleted file mode 100644
index 5fe2bca..0000000
--- a/.github/workflows/imagen4.yml
+++ /dev/null
@@ -1,55 +0,0 @@
-name: Imagen4 via Gemini CLI (MCP)
-
-on:
-  workflow_dispatch:
-    inputs:
-      prompt:
-        description: "画像プロンプト"
-        required: true
-      aspect_ratio:
-        description: "1:1 | 3:4 | 4:3 | 9:16 | 16:9"
-        required: false
-        default: "1:1"
-      model:
-        description: "imagen-4.0-(generate|fast-generate|ultra-generate)-preview-06-06"
-        required: false
-        default: "imagen-4.0-fast-generate-preview-06-06"
-
-jobs:
-  generate:
-    runs-on: ubuntu-latest
-    steps:
-      - uses: actions/checkout@v4
-
-      # Gemini CLI をGitHub Actionsから実行
-      - name: Run Gemini CLI with Imagen4 MCP
-        uses: google-github-actions/run-gemini-cli@v0.1.12
-        with:
-          # Gemini CLI が読む settings.json をインラインで書き込み
-          settings: |
-            {
-              "mcpServers": {
-                "gemini-imagen4": {
-                  "command": "npx",
-                  "args": ["gemini-imagen4"],
-                  "env": { "GEMINI_API_KEY": "${{ secrets.GEMINI_API_KEY }}" }
-                }
-              }
-            }
-          # ここが実際の“指示”。MCPツール名はサーバ側ドキュメント準拠
-          prompt: |
-            Use @gemini-imagen4.generate_image_from_text with:
-            prompt="${{ inputs.prompt }}",
-            model="${{ inputs.model }}",
-            aspectRatio="${{ inputs.aspect_ratio }}".
-            Return the saved file paths (./generated-images) and a short summary.
-          gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
-          gemini_cli_version: latest
-          gemini_debug: true
-
-      - name: Upload generated images
-        if: always()
-        uses: actions/upload-artifact@v4
-        with:
-          name: imagen4-output
-          path: generated-images/**
diff --git a/generated-images/imagen-4_2025-09-06T11-49-47-885Z_A_beautiful_Japanese_landscape_with_cherry_blossom_1.png b/generated-images/imagen-4_2025-09-06T11-49-47-885Z_A_beautiful_Japanese_landscape_with_cherry_blossom_1.png
new file mode 100644
index 0000000..9918f0c
Binary files /dev/null and b/generated-images/imagen-4_2025-09-06T11-49-47-885Z_A_beautiful_Japanese_landscape_with_cherry_blossom_1.png differ
diff --git a/generated-images/imagen-4_2025-09-06T11-49-47-892Z_A_beautiful_Japanese_landscape_with_cherry_blossom_2.png b/generated-images/imagen-4_2025-09-06T11-49-47-892Z_A_beautiful_Japanese_landscape_with_cherry_blossom_2.png
new file mode 100644
index 0000000..d3ed6e9
Binary files /dev/null and b/generated-images/imagen-4_2025-09-06T11-49-47-892Z_A_beautiful_Japanese_landscape_with_cherry_blossom_2.png differ
diff --git a/generated-images/metadata.json b/generated-images/metadata.json
new file mode 100644
index 0000000..f54ec06
--- /dev/null
+++ b/generated-images/metadata.json
@@ -0,0 +1,10 @@
+{
+  "generation_date": "2025-09-06T11:49:51Z",
+  "prompt": "A beautiful Japanese landscape with cherry blossoms and mountains",
+  "model": "imagen-4",
+  "num_images": 2,
+  "aspect_ratio": "1:1",
+  "seed": "",
+  "workflow_run": "12",
+  "commit_sha": "b466018b57025ce0bde38ed96e71f39ea8c9b486"
+}
```
