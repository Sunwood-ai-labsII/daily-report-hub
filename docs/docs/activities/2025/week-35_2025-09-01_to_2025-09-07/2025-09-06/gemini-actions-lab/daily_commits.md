# 📝 Daily Commits

## ⏰ 20:20:25 - `a8d4954`
**Update imagen4.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:20:25 2025 +0900
M	.github/workflows/imagen4.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:20:25 2025 +0900

    Update imagen4.yml

 .github/workflows/imagen4.yml | 60 +++++++++++++++++++++++--------------------
 1 file changed, 32 insertions(+), 28 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
index 5fe2bca..62a1fe4 100644
--- a/.github/workflows/imagen4.yml
+++ b/.github/workflows/imagen4.yml
@@ -1,19 +1,22 @@
-name: Imagen4 via Gemini CLI (MCP)
-
+name: imagen4-via-gemini-cli
 on:
   workflow_dispatch:
     inputs:
-      prompt:
-        description: "画像プロンプト"
+      image_prompt:
+        description: '作りたい画像のプロンプト'
         required: true
-      aspect_ratio:
-        description: "1:1 | 3:4 | 4:3 | 9:16 | 16:9"
-        required: false
-        default: "1:1"
       model:
-        description: "imagen-4.0-(generate|fast-generate|ultra-generate)-preview-06-06"
+        description: '画像生成モデル (imagen-4 / imagen-4-ultra / imagen-3)'
+        required: false
+        default: 'imagen-4'
+      num:
+        description: '生成枚数'
+        required: false
+        default: '2'
+      aspect_ratio:
+        description: 'アスペクト比 (例: 1:1, 16:9, 9:16)'
         required: false
-        default: "imagen-4.0-fast-generate-preview-06-06"
+        default: '1:1'
 
 jobs:
   generate:
@@ -21,35 +24,36 @@ jobs:
     steps:
       - uses: actions/checkout@v4
 
-      # Gemini CLI をGitHub Actionsから実行
-      - name: Run Gemini CLI with Imagen4 MCP
-        uses: google-github-actions/run-gemini-cli@v0.1.12
+      - name: Generate images via Gemini CLI (+ Imagen MCP)
+        uses: google-github-actions/run-gemini-cli@v0
         with:
-          # Gemini CLI が読む settings.json をインラインで書き込み
+          gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
+          gemini_model: gemini-2.5-flash        # 本体はテキスト思考用。画像生成はMCP側が担当
+          gemini_debug: true
+          # Gemini CLI のプロジェクト設定をその場で注入
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
+          # モデルに対する指示（MCPツールを明示的に使わせる）
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
+            from this prompt: "${{ github.event.inputs.image_prompt }}"
+            Use aspect ratio "${{ github.event.inputs.aspect_ratio }}".
+            Confirm files are saved under ./generated-images and list the filenames only.
 
       - name: Upload generated images
-        if: always()
         uses: actions/upload-artifact@v4
         with:
-          name: imagen4-output
+          name: generated-images
           path: generated-images/**
```

---

## ⏰ 20:31:37 - `9194f6b`
**Update imagen4.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:31:37 2025 +0900
M	.github/workflows/imagen4.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:31:37 2025 +0900

    Update imagen4.yml

 .github/workflows/imagen4.yml | 107 +++++++++++++++++++++++++++++++++---------
 1 file changed, 85 insertions(+), 22 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
index 62a1fe4..569e8bf 100644
--- a/.github/workflows/imagen4.yml
+++ b/.github/workflows/imagen4.yml
@@ -1,36 +1,44 @@
-name: imagen4-via-gemini-cli
+name: 🖼 imagen4-commit-via-gemini-cli
+
 on:
   workflow_dispatch:
     inputs:
       image_prompt:
-        description: '作りたい画像のプロンプト'
+        description: "作りたい画像のプロンプト"
         required: true
       model:
-        description: '画像生成モデル (imagen-4 / imagen-4-ultra / imagen-3)'
-        required: false
-        default: 'imagen-4'
+        description: "画像生成モデル (imagen-4 / imagen-4-ultra / imagen-3)"
+        default: "imagen-4"
       num:
-        description: '生成枚数'
-        required: false
-        default: '2'
+        description: "生成枚数 (1-4)"
+        default: "1"
       aspect_ratio:
-        description: 'アスペクト比 (例: 1:1, 16:9, 9:16)'
+        description: "アスペクト比 (例: 1:1, 16:9, 9:16, 3:4, 4:3)"
+        default: "1:1"
+      seed:
+        description: "固定シード（任意）"
         required: false
-        default: '1:1'
+
+permissions:
+  contents: write   # ← 直接コミットに必要
 
 jobs:
-  generate:
+  generate_and_commit:
     runs-on: ubuntu-latest
     steps:
-      - uses: actions/checkout@v4
+      - name: Checkout
+        uses: actions/checkout@v4
+        with:
+          persist-credentials: true  # GITHUB_TOKEN で push する
 
+      # 画像生成：Gemini CLI + Imagen MCP（GEMINI_API_KEYだけで動作）
       - name: Generate images via Gemini CLI (+ Imagen MCP)
         uses: google-github-actions/run-gemini-cli@v0
         with:
           gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
-          gemini_model: gemini-2.5-flash        # 本体はテキスト思考用。画像生成はMCP側が担当
+          gemini_model: gemini-2.5-flash
+          gemini_cli_version: latest
           gemini_debug: true
-          # Gemini CLI のプロジェクト設定をその場で注入
           settings: |
             {
               "mcpServers": {
@@ -45,15 +53,70 @@ jobs:
                 }
               }
             }
-          # モデルに対する指示（MCPツールを明示的に使わせる）
           prompt: |
             Use the @gemini-imagen.generate_image tool to generate ${{ github.event.inputs.num }} image(s)
-            from this prompt: "${{ github.event.inputs.image_prompt }}"
+            from this prompt: "${{ github.event.inputs.image_prompt }}".
             Use aspect ratio "${{ github.event.inputs.aspect_ratio }}".
-            Confirm files are saved under ./generated-images and list the filenames only.
+            If "seed" is provided, use it: "${{ github.event.inputs.seed || '' }}".
+            Save files under ./generated-images and list only the filenames.
 
-      - name: Upload generated images
-        uses: actions/upload-artifact@v4
-        with:
-          name: generated-images
-          path: generated-images/**
+      - name: Verify outputs
+        run: |
+          set -euo pipefail
+          test -d generated-images || { echo "generated-images not found"; exit 1; }
+          echo "== Generated files =="
+          ls -lh generated-images
+          # 一応1枚以上あるか確認
+          cnt=$(ls -1 generated-images | wc -l)
+          if [ "$cnt" -lt 1 ]; then
+            echo "No images were generated"; exit 1
+          fi
+
+      - name: Commit directly to branch
+        env:
+          GH_USER_NAME: github-actions[bot]
+          GH_USER_EMAIL: 41898282+github-actions[bot]@users.noreply.github.com
+        run: |
+          set -euo pipefail
```

---

## ⏰ 20:32:08 - `0a334bf`
**Update imagen4.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:32:08 2025 +0900
M	.github/workflows/imagen4.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:32:08 2025 +0900

    Update imagen4.yml

 .github/workflows/imagen4.yml | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
index 569e8bf..87bc12b 100644
--- a/.github/workflows/imagen4.yml
+++ b/.github/workflows/imagen4.yml
@@ -1,4 +1,4 @@
-name: 🖼 imagen4-commit-via-gemini-cli
+name: imagen4-commit-via-gemini-cli
 
 on:
   workflow_dispatch:
```

---

## ⏰ 20:33:56 - `e77eaea`
**Update imagen4.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:33:56 2025 +0900
M	.github/workflows/imagen4.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:33:56 2025 +0900

    Update imagen4.yml

 .github/workflows/imagen4.yml | 19 +++++++------------
 1 file changed, 7 insertions(+), 12 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
index 87bc12b..f1da8e9 100644
--- a/.github/workflows/imagen4.yml
+++ b/.github/workflows/imagen4.yml
@@ -20,7 +20,7 @@ on:
         required: false
 
 permissions:
-  contents: write   # ← 直接コミットに必要
+  contents: write
 
 jobs:
   generate_and_commit:
@@ -29,9 +29,8 @@ jobs:
       - name: Checkout
         uses: actions/checkout@v4
         with:
-          persist-credentials: true  # GITHUB_TOKEN で push する
+          persist-credentials: true
 
-      # 画像生成：Gemini CLI + Imagen MCP（GEMINI_API_KEYだけで動作）
       - name: Generate images via Gemini CLI (+ Imagen MCP)
         uses: google-github-actions/run-gemini-cli@v0
         with:
@@ -61,34 +60,32 @@ jobs:
             Save files under ./generated-images and list only the filenames.
 
       - name: Verify outputs
+        shell: bash
         run: |
           set -euo pipefail
           test -d generated-images || { echo "generated-images not found"; exit 1; }
           echo "== Generated files =="
           ls -lh generated-images
-          # 一応1枚以上あるか確認
           cnt=$(ls -1 generated-images | wc -l)
           if [ "$cnt" -lt 1 ]; then
             echo "No images were generated"; exit 1
           fi
 
       - name: Commit directly to branch
+        shell: bash
         env:
           GH_USER_NAME: github-actions[bot]
           GH_USER_EMAIL: 41898282+github-actions[bot]@users.noreply.github.com
         run: |
           set -euo pipefail
 
-          # 保存先（ランID＋日付でユニーク化）
           DATE_UTC=$(date -u +%Y%m%d)
           DEST="assets/imagen4/${DATE_UTC}-${{ github.run_id }}"
           mkdir -p "$DEST"
 
-          # 画像コピー
           cp -v generated-images/* "$DEST"/
 
-          # メタデータ（後から追跡しやすく）
-          cat > "$DEST/index.json" <<EOF
+          cat > "$DEST/index.json" <<'EOF'
           {
             "repo": "${{ github.repository }}",
             "run_id": "${{ github.run_id }}",
@@ -107,16 +104,14 @@ jobs:
           git config user.email "$GH_USER_EMAIL"
           git add "$DEST"
 
-          # 変更がなければスキップ
           if git diff --cached --quiet; then
             echo "No changes to commit."
             exit 0
           fi
 
           git commit -m "chore(images): add Imagen outputs for run ${{ github.run_id }}"
-          # 手動実行ブランチへそのままpush（通常は default branch）
           git push origin HEAD:${{ github.ref_name }}
 
-      # （任意）最終的に保存先をログ出力
       - name: Show saved path
-        run: echo "Saved to: assets/imagen4/${{ steps.date_tag.outputs.tag || '' }} (run ${{ github.run_id }})" || true
+        shell: bash
+        run: echo "Saved to: assets/imagen4/${{ github.run_id }}"
```

---

## ⏰ 20:35:29 - `05d6607`
**Refactor Imagen workflow for improved clarity**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:35:29 2025 +0900
M	.github/workflows/imagen4.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:35:29 2025 +0900

    Refactor Imagen workflow for improved clarity

 .github/workflows/imagen4.yml | 43 +++++++++++++++++++++++--------------------
 1 file changed, 23 insertions(+), 20 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
index f1da8e9..fd62fa1 100644
--- a/.github/workflows/imagen4.yml
+++ b/.github/workflows/imagen4.yml
@@ -25,6 +25,7 @@ permissions:
 jobs:
   generate_and_commit:
     runs-on: ubuntu-latest
+
     steps:
       - name: Checkout
         uses: actions/checkout@v4
@@ -56,14 +57,16 @@ jobs:
             Use the @gemini-imagen.generate_image tool to generate ${{ github.event.inputs.num }} image(s)
             from this prompt: "${{ github.event.inputs.image_prompt }}".
             Use aspect ratio "${{ github.event.inputs.aspect_ratio }}".
-            If "seed" is provided, use it: "${{ github.event.inputs.seed || '' }}".
+            If a seed is provided, use it: "${{ github.event.inputs.seed }}".
             Save files under ./generated-images and list only the filenames.
 
       - name: Verify outputs
         shell: bash
         run: |
           set -euo pipefail
-          test -d generated-images || { echo "generated-images not found"; exit 1; }
+          if [ ! -d generated-images ]; then
+            echo "generated-images not found"; exit 1
+          fi
           echo "== Generated files =="
           ls -lh generated-images
           cnt=$(ls -1 generated-images | wc -l)
@@ -80,25 +83,25 @@ jobs:
           set -euo pipefail
 
           DATE_UTC=$(date -u +%Y%m%d)
-          DEST="assets/imagen4/${DATE_UTC}-${{ github.run_id }}"
+          TS_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)
+          DEST="assets/imagen4/${DATE_UTC}-${GITHUB_RUN_ID}"
           mkdir -p "$DEST"
 
           cp -v generated-images/* "$DEST"/
 
-          cat > "$DEST/index.json" <<'EOF'
-          {
-            "repo": "${{ github.repository }}",
-            "run_id": "${{ github.run_id }}",
-            "run_url": "https://github.com/${{ github.repository }}/actions/runs/${{ github.run_id }}",
-            "workflow": "${{ github.workflow }}",
-            "prompt": "${{ github.event.inputs.image_prompt || '' }}",
-            "model": "${{ github.event.inputs.model || '' }}",
-            "aspect_ratio": "${{ github.event.inputs.aspect_ratio || '' }}",
-            "num": "${{ github.event.inputs.num || '' }}",
-            "seed": "${{ github.event.inputs.seed || '' }}",
-            "timestamp_utc": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
-          }
-          EOF
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
 
           git config user.name  "$GH_USER_NAME"
           git config user.email "$GH_USER_EMAIL"
@@ -109,9 +112,9 @@ jobs:
             exit 0
           fi
 
-          git commit -m "chore(images): add Imagen outputs for run ${{ github.run_id }}"
-          git push origin HEAD:${{ github.ref_name }}
+          git commit -m "chore(images): add Imagen outputs for run ${GITHUB_RUN_ID}"
+          git push origin "HEAD:${GITHUB_REF_NAME}"
 
       - name: Show saved path
         shell: bash
-        run: echo "Saved to: assets/imagen4/${{ github.run_id }}"
+        run: echo "Saved to: assets/imagen4/$(date -u +%Y%m%d)-${GITHUB_RUN_ID}"
```

---

## ⏰ 20:36:13 - `72a6e20`
**Update imagen4.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:36:13 2025 +0900
M	.github/workflows/imagen4.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:36:13 2025 +0900

    Update imagen4.yml

 .github/workflows/imagen4.yml | 49 +++++++++++++++++++++++++++----------------
 1 file changed, 31 insertions(+), 18 deletions(-)
```

### 💻 Code Changes
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

---

## ⏰ 20:37:26 - `55be039`
**Update imagen4.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:37:26 2025 +0900
M	.github/workflows/imagen4.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:37:26 2025 +0900

    Update imagen4.yml

 .github/workflows/imagen4.yml | 6 ------
 1 file changed, 6 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
index f5a1c9f..2bbb708 100644
--- a/.github/workflows/imagen4.yml
+++ b/.github/workflows/imagen4.yml
@@ -93,14 +93,11 @@ jobs:
           SEED: ${{ inputs.seed }}
         run: |
           set -euo pipefail
-
           DATE_UTC=$(date -u +%Y%m%d)
           TS_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)
           DEST="assets/imagen4/${DATE_UTC}-${GITHUB_RUN_ID}"
           mkdir -p "$DEST"
-
           cp -v generated-images/* "$DEST"/
-
           # jq で JSON を安全に生成（Ubuntu イメージに jq は標準で入っています）
           jq -n \
             --arg repo "$GITHUB_REPOSITORY" \
@@ -115,16 +112,13 @@ jobs:
             --arg ts "$TS_UTC" \
             '{repo:$repo, run_id:$run_id, run_url:$run_url, workflow:$workflow, prompt:$prompt, model:$model, aspect_ratio:$aspect_ratio, num:$num, seed:$seed, timestamp_utc:$ts}' \
             > "$DEST/index.json"
-
           git config user.name  "$GH_USER_NAME"
           git config user.email "$GH_USER_EMAIL"
           git add "$DEST"
-
           if git diff --cached --quiet; then
             echo "No changes to commit."
             exit 0
           fi
-
           git commit -m "chore(images): add Imagen outputs for run ${GITHUB_RUN_ID}"
           git push origin "HEAD:${GITHUB_REF_NAME}"
 
```

---

## ⏰ 20:39:58 - `035164e`
**Update imagen4.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:39:58 2025 +0900
M	.github/workflows/imagen4.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:39:58 2025 +0900

    Update imagen4.yml

 .github/workflows/imagen4.yml | 4 +++-
 1 file changed, 3 insertions(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
index 2bbb708..a5b3b05 100644
--- a/.github/workflows/imagen4.yml
+++ b/.github/workflows/imagen4.yml
@@ -124,4 +124,6 @@ jobs:
 
       - name: Show saved path
         shell: bash
-        run: echo "Saved to: assets/imagen4/$(date -u +%Y%m%d)-${GITHUB_RUN_ID}"
+        env:
+          DATE_FORMAT: "%Y%m%d"
+        run: echo "Saved to: assets/imagen4/$(date -u +"$DATE_FORMAT")-$GITHUB_RUN_ID"
```

---

## ⏰ 20:41:47 - `34e41d1`
**Update imagen4.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:41:47 2025 +0900
M	.github/workflows/imagen4.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sat Sep 6 20:41:47 2025 +0900

    Update imagen4.yml

 .github/workflows/imagen4.yml | 22 +++++++++-------------
 1 file changed, 9 insertions(+), 13 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
index a5b3b05..e1fcb26 100644
--- a/.github/workflows/imagen4.yml
+++ b/.github/workflows/imagen4.yml
@@ -39,7 +39,6 @@ jobs:
           gemini_model: gemini-2.5-flash
           gemini_cli_version: latest
           gemini_debug: true
-          # ここでは model だけを埋め込み、それ以外は prompt 内で渡す
           settings: |
             {
               "mcpServers": {
@@ -54,7 +53,6 @@ jobs:
                 }
               }
             }
-          # ユーザー入力は env で受け渡し、プロンプトに素直に埋め込む
           env: |
             PROMPT=${{ inputs.image_prompt }}
             NUM=${{ inputs.num }}
@@ -91,14 +89,15 @@ jobs:
           AR: ${{ inputs.aspect_ratio }}
           NUM: ${{ inputs.num }}
           SEED: ${{ inputs.seed }}
+          DATE_FORMAT: "%Y%m%d"
+          TIMESTAMP_FORMAT: "%Y-%m-%dT%H:%M:%SZ"
         run: |
           set -euo pipefail
-          DATE_UTC=$(date -u +%Y%m%d)
-          TS_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)
-          DEST="assets/imagen4/${DATE_UTC}-${GITHUB_RUN_ID}"
+          DATE_UTC=$(date -u +"$DATE_FORMAT")
+          TS_UTC=$(date -u +"$TIMESTAMP_FORMAT")
+          DEST="assets/imagen4/$DATE_UTC-$GITHUB_RUN_ID"
           mkdir -p "$DEST"
           cp -v generated-images/* "$DEST"/
-          # jq で JSON を安全に生成（Ubuntu イメージに jq は標準で入っています）
           jq -n \
             --arg repo "$GITHUB_REPOSITORY" \
             --arg run_id "$GITHUB_RUN_ID" \
@@ -112,18 +111,15 @@ jobs:
             --arg ts "$TS_UTC" \
             '{repo:$repo, run_id:$run_id, run_url:$run_url, workflow:$workflow, prompt:$prompt, model:$model, aspect_ratio:$aspect_ratio, num:$num, seed:$seed, timestamp_utc:$ts}' \
             > "$DEST/index.json"
-          git config user.name  "$GH_USER_NAME"
+          git config user.name "$GH_USER_NAME"
           git config user.email "$GH_USER_EMAIL"
           git add "$DEST"
           if git diff --cached --quiet; then
             echo "No changes to commit."
             exit 0
           fi
-          git commit -m "chore(images): add Imagen outputs for run ${GITHUB_RUN_ID}"
-          git push origin "HEAD:${GITHUB_REF_NAME}"
+          git commit -m "chore(images): add Imagen outputs for run $GITHUB_RUN_ID"
+          git push origin "HEAD:$GITHUB_REF_NAME"
 
       - name: Show saved path
-        shell: bash
-        env:
-          DATE_FORMAT: "%Y%m%d"
-        run: echo "Saved to: assets/imagen4/$(date -u +"$DATE_FORMAT")-$GITHUB_RUN_ID"
+        run: echo "Saved to assets/imagen4/$(date -u +%Y%m%d)-$GITHUB_RUN_ID"
```

---

