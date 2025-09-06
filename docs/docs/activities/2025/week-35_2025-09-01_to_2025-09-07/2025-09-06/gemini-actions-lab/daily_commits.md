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

