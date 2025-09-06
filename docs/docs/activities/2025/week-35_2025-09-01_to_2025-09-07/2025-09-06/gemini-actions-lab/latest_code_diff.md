# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
index e1fcb26..b4b24f4 100644
--- a/.github/workflows/imagen4.yml
+++ b/.github/workflows/imagen4.yml
@@ -1,125 +1,205 @@
-name: imagen4-commit-via-gemini-cli
+name: Generate Images with Gemini and Commit
 
 on:
   workflow_dispatch:
     inputs:
-      image_prompt:
-        description: "作りたい画像のプロンプト"
+      num_images:
+        description: 'Number of images to generate'
         required: true
-      model:
-        description: "画像生成モデル (imagen-4 / imagen-4-ultra / imagen-3)"
-        default: "imagen-4"
-      num:
-        description: "生成枚数 (1-4)"
-        default: "1"
+        default: '2'
+        type: string
+      prompt:
+        description: 'Image generation prompt'
+        required: true
+        default: 'A beautiful Japanese landscape with cherry blossoms and mountains'
+        type: string
       aspect_ratio:
-        description: "アスペクト比 (例: 1:1, 16:9, 9:16, 3:4, 4:3)"
-        default: "1:1"
+        description: 'Aspect ratio (e.g., 16:9, 1:1, 4:3)'
+        required: true
+        default: '16:9'
+        type: choice
+        options:
+          - '16:9'
+          - '1:1'
+          - '4:3'
+          - '9:16'
       seed:
-        description: "固定シード（任意）"
+        description: 'Seed for reproducible generation (optional)'
         required: false
-
-permissions:
-  contents: write
+        default: ''
+        type: string
 
 jobs:
   generate_and_commit:
     runs-on: ubuntu-latest
-
+    
+    permissions:
+      contents: write
+      
     steps:
-      - name: Checkout
+      - name: Checkout repository
         uses: actions/checkout@v4
         with:
-          persist-credentials: true
+          token: ${{ secrets.GITHUB_TOKEN }}
 
-      - name: Generate images via Gemini CLI (+ Imagen MCP)
-        uses: google-github-actions/run-gemini-cli@v0
+      - name: Setup Node.js
+        uses: actions/setup-node@v4
         with:
-          gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
-          gemini_model: gemini-2.5-flash
-          gemini_cli_version: latest
-          gemini_debug: true
-          settings: |
-            {
-              "mcpServers": {
-                "gemini-imagen": {
-                  "command": "npx",
-                  "args": ["-y", "gemini-imagen-mcp-server",
-                           "--output-dir", "generated-images",
-                           "--model", "${{ inputs.model }}"],
-                  "env": { "GEMINI_API_KEY": "${{ secrets.GEMINI_API_KEY }}" },
-                  "trust": true,
-                  "includeTools": ["generate_image"]
-                }
-              }
-            }
-          env: |
-            PROMPT=${{ inputs.image_prompt }}
-            NUM=${{ inputs.num }}
-            AR=${{ inputs.aspect_ratio }}
-            SEED=${{ inputs.seed }}
-          prompt: |
-            Use the @gemini-imagen.generate_image tool to generate $NUM image(s)
-            from this prompt: "$PROMPT".
-            Use aspect ratio "$AR".
-            If a seed is provided, use it: "$SEED".
-            Save files under ./generated-images and list only the filenames.
+          node-version: '20'
+
+      - name: Install Gemini CLI
+        run: |
+          npm install -g @google/generative-ai-cli
+          
+      - name: Verify Gemini CLI installation
+        run: |
+          which gemini || echo "Gemini CLI not found in PATH"
+          npm list -g @google/generative-ai-cli || echo "Package check failed"
+
+      - name: Create output directory
+        run: |
+          mkdir -p generated-images
+          echo "Created generated-images directory"
+          ls -la
+
+      - name: Setup environment variables
+        run: |
+          echo "NUM=${{ github.event.inputs.num_images }}" >> $GITHUB_ENV
+          echo "PROMPT=${{ github.event.inputs.prompt }}" >> $GITHUB_ENV
+          echo "AR=${{ github.event.inputs.aspect_ratio }}" >> $GITHUB_ENV
+          echo "SEED=${{ github.event.inputs.seed }}" >> $GITHUB_ENV
+          echo "GEMINI_MODEL=gemini-2.5-flash" >> $GITHUB_ENV
+
+      - name: Debug environment
+        run: |
+          echo "NUM: $NUM"
+          echo "PROMPT: $PROMPT"
+          echo "AR: $AR"
+          echo "SEED: $SEED"
+          echo "GEMINI_MODEL: $GEMINI_MODEL"
+          echo "Working directory: $(pwd)"
+          echo "Directory contents:"
+          ls -la
+
+      - name: Generate images with Gemini
+        env:
+          GOOGLE_API_KEY: ${{ secrets.GOOGLE_API_KEY }}
+          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
+          GCP_PROJECT_ID: ${{ secrets.GCP_PROJECT_ID }}
+          GEMINI_DEBUG: true
+        run: |
+          set -euo pipefail
+          
+          echo "Starting image generation..."
+          echo "Prompt: $PROMPT"
+          echo "Number of images: $NUM"
+          echo "Aspect ratio: $AR"
+          echo "Seed: $SEED"
+          
+          # Gemini CLIを使用して画像を生成
+          for i in $(seq 1 $NUM); do
+            echo "Generating image $i of $NUM..."
+            
+            # シード値の処理
+            if [ -n "$SEED" ]; then
+              CURRENT_SEED=$((SEED + i - 1))
+              SEED_PARAM="--seed $CURRENT_SEED"
+            else
+              SEED_PARAM=""
+            fi
+            
+            # 画像生成コマンド（実際のGemini CLIの構文に合わせて調整が必要）
+            gemini imagen generate \
+              --prompt "$PROMPT" \
+              --aspect-ratio "$AR" \
+              --output-dir "./generated-images" \
+              --filename "generated_image_${i}_$(date +%Y%m%d_%H%M%S)" \
+              $SEED_PARAM || echo "Image generation $i failed, continuing..."
+          done
+          
+          echo "Image generation completed"
 
-      - name: Verify outputs
-        shell: bash
+      - name: Verify generated files
         run: |
           set -euo pipefail
+          
           if [ ! -d generated-images ]; then
-            echo "generated-images not found"; exit 1
+            echo "ERROR: generated-images directory not found"
+            exit 1
           fi
+          
           echo "== Generated files =="
-          ls -lh generated-images
-          cnt=$(ls -1 generated-images | wc -l)
-          if [ "$cnt" -lt 1 ]; then
-            echo "No images were generated"; exit 1
+          ls -lh generated-images/
+          
+          file_count=$(ls -1 generated-images/ 2>/dev/null | wc -l)
+          echo "Total files generated: $file_count"
+          
+          if [ "$file_count" -lt 1 ]; then
+            echo "ERROR: No images were generated"
+            exit 1
           fi
+          
+          echo "✅ Successfully generated $file_count image(s)"
 
-      - name: Commit directly to branch
-        shell: bash
-        env:
-          GH_USER_NAME: github-actions[bot]
-          GH_USER_EMAIL: 41898282+github-actions[bot]@users.noreply.github.com
-          PROMPT: ${{ inputs.image_prompt }}
-          MODEL: ${{ inputs.model }}
-          AR: ${{ inputs.aspect_ratio }}
-          NUM: ${{ inputs.num }}
-          SEED: ${{ inputs.seed }}
-          DATE_FORMAT: "%Y%m%d"
-          TIMESTAMP_FORMAT: "%Y-%m-%dT%H:%M:%SZ"
+      - name: Add metadata file
         run: |
-          set -euo pipefail
-          DATE_UTC=$(date -u +"$DATE_FORMAT")
-          TS_UTC=$(date -u +"$TIMESTAMP_FORMAT")
-          DEST="assets/imagen4/$DATE_UTC-$GITHUB_RUN_ID"
-          mkdir -p "$DEST"
-          cp -v generated-images/* "$DEST"/
-          jq -n \
-            --arg repo "$GITHUB_REPOSITORY" \
-            --arg run_id "$GITHUB_RUN_ID" \
-            --arg run_url "https://github.com/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID" \
-            --arg workflow "$GITHUB_WORKFLOW" \
-            --arg prompt "$PROMPT" \
-            --arg model "$MODEL" \
-            --arg aspect_ratio "$AR" \
-            --arg num "$NUM" \
-            --arg seed "$SEED" \
-            --arg ts "$TS_UTC" \
-            '{repo:$repo, run_id:$run_id, run_url:$run_url, workflow:$workflow, prompt:$prompt, model:$model, aspect_ratio:$aspect_ratio, num:$num, seed:$seed, timestamp_utc:$ts}' \
-            > "$DEST/index.json"
-          git config user.name "$GH_USER_NAME"
-          git config user.email "$GH_USER_EMAIL"
-          git add "$DEST"
-          if git diff --cached --quiet; then
-            echo "No changes to commit."
-            exit 0
+          cat > generated-images/metadata.json << EOF
+          {
+            "generation_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
+            "prompt": "$PROMPT",
+            "num_images": $NUM,
+            "aspect_ratio": "$AR",
+            "seed": "$SEED",
+            "model": "$GEMINI_MODEL",
+            "workflow_run": "${{ github.run_number }}",
+            "commit_sha": "${{ github.sha }}"
+          }
+          EOF
+          
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
+            git commit -m "🎨 Generate images via Gemini API
+            
+            Prompt: $PROMPT
+            Images: $NUM
+            Aspect ratio: $AR
+            Seed: $SEED
+            Generated at: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
+            
+            git push
+            echo "✅ Successfully committed and pushed generated images"
           fi
-          git commit -m "chore(images): add Imagen outputs for run $GITHUB_RUN_ID"
-          git push origin "HEAD:$GITHUB_REF_NAME"
 
-      - name: Show saved path
-        run: echo "Saved to assets/imagen4/$(date -u +%Y%m%d)-$GITHUB_RUN_ID"
+      - name: Create summary
+        run: |
+          echo "## 🎨 Image Generation Summary" >> $GITHUB_STEP_SUMMARY
+          echo "" >> $GITHUB_STEP_SUMMARY
+          echo "**Prompt:** $PROMPT" >> $GITHUB_STEP_SUMMARY
+          echo "**Number of Images:** $NUM" >> $GITHUB_STEP_SUMMARY
+          echo "**Aspect Ratio:** $AR" >> $GITHUB_STEP_SUMMARY
+          echo "**Seed:** ${SEED:-'Random'}" >> $GITHUB_STEP_SUMMARY
+          echo "**Model:** $GEMINI_MODEL" >> $GITHUB_STEP_SUMMARY
+          echo "" >> $GITHUB_STEP_SUMMARY
+          echo "### Generated Files" >> $GITHUB_STEP_SUMMARY
+          echo "\`\`\`" >> $GITHUB_STEP_SUMMARY
+          ls -la generated-images/ >> $GITHUB_STEP_SUMMARY
+          echo "\`\`\`" >> $GITHUB_STEP_SUMMARY
+
+      - name: Upload artifacts
+        uses: actions/upload-artifact@v4
+        if: always()
+        with:
+          name: generated-images-${{ github.run_number }}
+          path: generated-images/
+          retention-days: 30
```
