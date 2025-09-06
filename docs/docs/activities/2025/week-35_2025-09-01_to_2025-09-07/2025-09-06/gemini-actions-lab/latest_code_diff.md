# 🔄 Latest Code Changes

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
