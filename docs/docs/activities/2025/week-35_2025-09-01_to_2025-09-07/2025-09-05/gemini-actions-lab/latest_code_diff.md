# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-release-notes.yml b/.github/workflows/gemini-release-notes.yml
index 36d68bb..d922bfa 100644
--- a/.github/workflows/gemini-release-notes.yml
+++ b/.github/workflows/gemini-release-notes.yml
@@ -95,19 +95,19 @@ jobs:
             あなたはリリースノート作成のエキスパートです。以下の情報から、日本語で読みやすいMarkdownのリリースノートを作成してください。
 
             # コンテキスト
-            - リポジトリ: ${REPOSITORY}
-            - リリースタグ: ${TAG_NAME}
-            - 前リリースタグ: ${PREV_TAG}
-            - 比較URL: ${COMPARE_URL}
+            - リポジトリ: ${{ github.repository }}
+            - リリースタグ: ${{ steps.ctx.outputs.tag }}
+            - 前リリースタグ: ${{ steps.ctx.outputs.prev_tag }}
+            - 比較URL: ${{ steps.ctx.outputs.compare_url }}
 
             # 変更コミット（抜粋）
-            ${COMMITS}
+            ${{ steps.ctx.outputs.commits }}
 
             # 変更ファイル（抜粋）
-            ${CHANGED_FILES}
+            ${{ steps.ctx.outputs.files }}
 
             # コントリビューター（抜粋）
-            ${CONTRIBUTORS}
+            ${{ steps.ctx.outputs.contributors }}
 
             # 執筆方針
             - 見出しと箇条書きを用いて簡潔に。
@@ -118,7 +118,7 @@ jobs:
             - 出力はMarkdownのみ（余計な前置きや後書き、コードフェンスは不要）。
 
             # 期待するMarkdownの構成例
-            # ${TAG_NAME}
+            # ${{ steps.ctx.outputs.tag }}
             ## ✨ Highlights
             - 主要な変更点の要約…
 
@@ -136,13 +136,15 @@ jobs:
             - ユーザー名一覧（抜粋）
 
             ---
-            比較: ${COMPARE_URL}
+            比較: ${{ steps.ctx.outputs.compare_url }}
 
       - name: Write notes to file
         run: |
           set -euo pipefail
-          NOTES_OUT="${{ steps.gemini.outputs.summary }}"
-          printf "%s\n" "${NOTES_OUT}" > release_notes.md
+          # Write without shell interpolation to avoid ${...} expansion issues
+          cat > release_notes.md << 'EOF'
+          ${{ steps.gemini.outputs.summary }}
+          EOF
           echo "Wrote release_notes.md (size: $(wc -c < release_notes.md) bytes)"
 
       - name: Create or update GitHub Release
```
