# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-release-notes.yml b/.github/workflows/gemini-release-notes.yml
index d922bfa..9d95cd6 100644
--- a/.github/workflows/gemini-release-notes.yml
+++ b/.github/workflows/gemini-release-notes.yml
@@ -118,7 +118,7 @@ jobs:
             - 出力はMarkdownのみ（余計な前置きや後書き、コードフェンスは不要）。
 
             # 期待するMarkdownの構成例
-            # ${{ steps.ctx.outputs.tag }}
+            # ${{ steps.ctx.outputs.tag }} ～このリリースノートの内容が分かるようなタイトル～
             ## ✨ Highlights
             - 主要な変更点の要約…
 
```
