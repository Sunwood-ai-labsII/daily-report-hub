# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
index b4b24f4..9e3f640 100644
--- a/.github/workflows/imagen4.yml
+++ b/.github/workflows/imagen4.yml
@@ -1,33 +1,28 @@
-name: Generate Images with Gemini and Commit
+name: imagen4-commit-via-gemini-cli
 
 on:
   workflow_dispatch:
     inputs:
-      num_images:
-        description: 'Number of images to generate'
-        required: true
-        default: '2'
-        type: string
-      prompt:
-        description: 'Image generation prompt'
+      image_prompt:
+        description: '作りたい画像のプロンプト'
         required: true
         default: 'A beautiful Japanese landscape with cherry blossoms and mountains'
-        type: string
+      model:
+        description: '画像生成モデル (imagen-4 / imagen-4-ultra / imagen-3)'
+        required: false
+        default: 'imagen-4'
+      num:
+        description: '生成枚数'
+        required: false
+        default: '2'
       aspect_ratio:
-        description: 'Aspect ratio (e.g., 16:9, 1:1, 4:3)'
-        required: true
-        default: '16:9'
-        type: choice
-        options:
-          - '16:9'
-          - '1:1'
-          - '4:3'
-          - '9:16'
+        description: 'アスペクト比 (例: 1:1, 16:9, 9:16)'
+        required: false
+        default: '1:1'
       seed:
-        description: 'Seed for reproducible generation (optional)'
+        description: 'シード値 (オプション)'
         required: false
         default: ''
-        type: string
 
 jobs:
   generate_and_commit:
@@ -42,120 +37,72 @@ jobs:
         with:
           token: ${{ secrets.GITHUB_TOKEN }}
 
-      - name: Setup Node.js
-        uses: actions/setup-node@v4
-        with:
-          node-version: '20'
-
-      - name: Install Gemini CLI
-        run: |
-          npm install -g @google/generative-ai-cli
-          
-      - name: Verify Gemini CLI installation
-        run: |
-          which gemini || echo "Gemini CLI not found in PATH"
-          npm list -g @google/generative-ai-cli || echo "Package check failed"
-
       - name: Create output directory
         run: |
           mkdir -p generated-images
           echo "Created generated-images directory"
           ls -la
 
-      - name: Setup environment variables
-        run: |
-          echo "NUM=${{ github.event.inputs.num_images }}" >> $GITHUB_ENV
-          echo "PROMPT=${{ github.event.inputs.prompt }}" >> $GITHUB_ENV
-          echo "AR=${{ github.event.inputs.aspect_ratio }}" >> $GITHUB_ENV
-          echo "SEED=${{ github.event.inputs.seed }}" >> $GITHUB_ENV
-          echo "GEMINI_MODEL=gemini-2.5-flash" >> $GITHUB_ENV
-
-      - name: Debug environment
-        run: |
-          echo "NUM: $NUM"
-          echo "PROMPT: $PROMPT"
-          echo "AR: $AR"
-          echo "SEED: $SEED"
-          echo "GEMINI_MODEL: $GEMINI_MODEL"
-          echo "Working directory: $(pwd)"
-          echo "Directory contents:"
-          ls -la
-
-      - name: Generate images with Gemini
+      - name: Generate images via Gemini CLI (+ Imagen MCP)
+        uses: google-github-actions/run-gemini-cli@v0
         env:
-          GOOGLE_API_KEY: ${{ secrets.GOOGLE_API_KEY }}
-          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
-          GCP_PROJECT_ID: ${{ secrets.GCP_PROJECT_ID }}
-          GEMINI_DEBUG: true
-        run: |
-          set -euo pipefail
-          
-          echo "Starting image generation..."
-          echo "Prompt: $PROMPT"
-          echo "Number of images: $NUM"
-          echo "Aspect ratio: $AR"
-          echo "Seed: $SEED"
-          
-          # Gemini CLIを使用して画像を生成
-          for i in $(seq 1 $NUM); do
-            echo "Generating image $i of $NUM..."
-            
-            # シード値の処理
-            if [ -n "$SEED" ]; then
-              CURRENT_SEED=$((SEED + i - 1))
-              SEED_PARAM="--seed $CURRENT_SEED"
-            else
-              SEED_PARAM=""
-            fi
-            
-            # 画像生成コマンド（実際のGemini CLIの構文に合わせて調整が必要）
-            gemini imagen generate \
-              --prompt "$PROMPT" \
-              --aspect-ratio "$AR" \
-              --output-dir "./generated-images" \
-              --filename "generated_image_${i}_$(date +%Y%m%d_%H%M%S)" \
-              $SEED_PARAM || echo "Image generation $i failed, continuing..."
-          done
-          
-          echo "Image generation completed"
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
 
       - name: Verify generated files
         run: |
           set -euo pipefail
-          
           if [ ! -d generated-images ]; then
-            echo "ERROR: generated-images directory not found"
-            exit 1
+            echo "generated-images not found"; exit 1
           fi
-          
           echo "== Generated files =="
-          ls -lh generated-images/
-          
-          file_count=$(ls -1 generated-images/ 2>/dev/null | wc -l)
-          echo "Total files generated: $file_count"
-          
-          if [ "$file_count" -lt 1 ]; then
-            echo "ERROR: No images were generated"
-            exit 1
+          ls -lh generated-images
+          cnt=$(ls -1 generated-images | wc -l)
+          if [ "$cnt" -lt 1 ]; then
+            echo "No images were generated"; exit 1
           fi
-          
-          echo "✅ Successfully generated $file_count image(s)"
+          echo "✅ Successfully generated $cnt file(s)"
 
       - name: Add metadata file
         run: |
           cat > generated-images/metadata.json << EOF
           {
             "generation_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
-            "prompt": "$PROMPT",
-            "num_images": $NUM,
-            "aspect_ratio": "$AR",
-            "seed": "$SEED",
-            "model": "$GEMINI_MODEL",
+            "prompt": "${{ github.event.inputs.image_prompt }}",
+            "model": "${{ github.event.inputs.model }}",
+            "num_images": ${{ github.event.inputs.num }},
+            "aspect_ratio": "${{ github.event.inputs.aspect_ratio }}",
+            "seed": "${{ github.event.inputs.seed }}",
             "workflow_run": "${{ github.run_number }}",
             "commit_sha": "${{ github.sha }}"
           }
           EOF
-          
           echo "Created metadata file:"
           cat generated-images/metadata.json
 
@@ -169,37 +116,38 @@ jobs:
           if git diff --staged --quiet; then
             echo "No changes to commit"
           else
-            git commit -m "🎨 Generate images via Gemini API
+            git commit -m "🎨 Generate images via Gemini Imagen API
             
-            Prompt: $PROMPT
-            Images: $NUM
-            Aspect ratio: $AR
-            Seed: $SEED
+            Prompt: ${{ github.event.inputs.image_prompt }}
+            Model: ${{ github.event.inputs.model }}
+            Images: ${{ github.event.inputs.num }}
+            Aspect ratio: ${{ github.event.inputs.aspect_ratio }}
+            Seed: ${{ github.event.inputs.seed }}
             Generated at: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
             
             git push
             echo "✅ Successfully committed and pushed generated images"
           fi
 
-      - name: Create summary
+      - name: Upload generated images as artifacts
+        uses: actions/upload-artifact@v4
+        if: always()
+        with:
+          name: generated-images-${{ github.run_number }}
+          path: generated-images/
+          retention-days: 30
+
+      - name: Create workflow summary
         run: |
           echo "## 🎨 Image Generation Summary" >> $GITHUB_STEP_SUMMARY
           echo "" >> $GITHUB_STEP_SUMMARY
-          echo "**Prompt:** $PROMPT" >> $GITHUB_STEP_SUMMARY
-          echo "**Number of Images:** $NUM" >> $GITHUB_STEP_SUMMARY
-          echo "**Aspect Ratio:** $AR" >> $GITHUB_STEP_SUMMARY
-          echo "**Seed:** ${SEED:-'Random'}" >> $GITHUB_STEP_SUMMARY
-          echo "**Model:** $GEMINI_MODEL" >> $GITHUB_STEP_SUMMARY
+          echo "**Prompt:** ${{ github.event.inputs.image_prompt }}" >> $GITHUB_STEP_SUMMARY
+          echo "**Model:** ${{ github.event.inputs.model }}" >> $GITHUB_STEP_SUMMARY
+          echo "**Number of Images:** ${{ github.event.inputs.num }}" >> $GITHUB_STEP_SUMMARY
+          echo "**Aspect Ratio:** ${{ github.event.inputs.aspect_ratio }}" >> $GITHUB_STEP_SUMMARY
+          echo "**Seed:** ${{ github.event.inputs.seed || 'Random' }}" >> $GITHUB_STEP_SUMMARY
           echo "" >> $GITHUB_STEP_SUMMARY
           echo "### Generated Files" >> $GITHUB_STEP_SUMMARY
           echo "\`\`\`" >> $GITHUB_STEP_SUMMARY
           ls -la generated-images/ >> $GITHUB_STEP_SUMMARY
           echo "\`\`\`" >> $GITHUB_STEP_SUMMARY
-
-      - name: Upload artifacts
-        uses: actions/upload-artifact@v4
-        if: always()
-        with:
-          name: generated-images-${{ github.run_number }}
-          path: generated-images/
-          retention-days: 30
```
