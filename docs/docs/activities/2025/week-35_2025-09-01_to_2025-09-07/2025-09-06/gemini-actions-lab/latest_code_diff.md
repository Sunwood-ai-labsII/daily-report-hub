# 🔄 Latest Code Changes

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
+
+          # 保存先（ランID＋日付でユニーク化）
+          DATE_UTC=$(date -u +%Y%m%d)
+          DEST="assets/imagen4/${DATE_UTC}-${{ github.run_id }}"
+          mkdir -p "$DEST"
+
+          # 画像コピー
+          cp -v generated-images/* "$DEST"/
+
+          # メタデータ（後から追跡しやすく）
+          cat > "$DEST/index.json" <<EOF
+          {
+            "repo": "${{ github.repository }}",
+            "run_id": "${{ github.run_id }}",
+            "run_url": "https://github.com/${{ github.repository }}/actions/runs/${{ github.run_id }}",
+            "workflow": "${{ github.workflow }}",
+            "prompt": "${{ github.event.inputs.image_prompt || '' }}",
+            "model": "${{ github.event.inputs.model || '' }}",
+            "aspect_ratio": "${{ github.event.inputs.aspect_ratio || '' }}",
+            "num": "${{ github.event.inputs.num || '' }}",
+            "seed": "${{ github.event.inputs.seed || '' }}",
+            "timestamp_utc": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
+          }
+          EOF
+
+          git config user.name  "$GH_USER_NAME"
+          git config user.email "$GH_USER_EMAIL"
+          git add "$DEST"
+
+          # 変更がなければスキップ
+          if git diff --cached --quiet; then
+            echo "No changes to commit."
+            exit 0
+          fi
+
+          git commit -m "chore(images): add Imagen outputs for run ${{ github.run_id }}"
+          # 手動実行ブランチへそのままpush（通常は default branch）
+          git push origin HEAD:${{ github.ref_name }}
+
+      # （任意）最終的に保存先をログ出力
+      - name: Show saved path
+        run: echo "Saved to: assets/imagen4/${{ steps.date_tag.outputs.tag || '' }} (run ${{ github.run_id }})" || true
```
