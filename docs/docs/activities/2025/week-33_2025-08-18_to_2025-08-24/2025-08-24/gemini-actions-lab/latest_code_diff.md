# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-jp-cli.yml b/.github/workflows/gemini-jp-cli.yml
index 5188cfe..fc52afb 100644
--- a/.github/workflows/gemini-jp-cli.yml
+++ b/.github/workflows/gemini-jp-cli.yml
@@ -83,17 +83,17 @@ jobs:
           echo "=== Issue情報 ==="
           echo "Issue Number: ${{ github.event.issue.number || 'N/A' }}"
           echo "Issue Title: ${{ github.event.issue.title || 'N/A' }}"
-          echo "Issue Body Length: ${{ length(github.event.issue.body || '') }}"
+          echo "Issue Body Length: $(echo '${{ github.event.issue.body || '' }}' | wc -c)"
           echo "Issue Author: ${{ github.event.issue.user.login || 'N/A' }}"
           echo "Issue Association: ${{ github.event.issue.author_association || 'N/A' }}"
           echo ""
           echo "=== Comment情報 ==="
-          echo "Comment Body Length: ${{ length(github.event.comment.body || '') }}"
+          echo "Comment Body Length: $(echo '${{ github.event.comment.body || '' }}' | wc -c)"
           echo "Comment Author: ${{ github.event.comment.user.login || 'N/A' }}"
           echo "Comment Association: ${{ github.event.comment.author_association || 'N/A' }}"
           echo ""
           echo "=== PR Review情報 ==="
-          echo "Review Body Length: ${{ length(github.event.review.body || '') }}"
+          echo "Review Body Length: $(echo '${{ github.event.review.body || '' }}' | wc -c)"
           echo "PR Number: ${{ github.event.pull_request.number || 'N/A' }}"
           echo ""
           echo "=== 完全なイベントペイロード ==="
@@ -390,8 +390,8 @@ jobs:
           echo "User Request: '${{ steps.get_context.outputs.user_request }}'"
           echo "Issue Number: '${{ steps.get_context.outputs.issue_number }}'"
           echo "Issue Title: '${{ steps.get_context.outputs.issue_title }}'"
-          echo "Description Length: ${{ length(steps.get_description.outputs.description) }}"
-          echo "Comments Length: ${{ length(steps.get_comments.outputs.comments) }}"
+          echo "Description Length: $(echo '${{ steps.get_description.outputs.description }}' | wc -c)"
+          echo "Comments Length: $(echo '${{ steps.get_comments.outputs.comments }}' | wc -c)"
           echo "Is PR: '${{ steps.get_context.outputs.is_pr }}'"
 
       - name: 'Geminiを実行'
@@ -425,8 +425,8 @@ jobs:
             
             - **生のBody**: `${{ steps.get_context.outputs.raw_body }}`
             - **処理されたユーザーリクエスト**: `${{ steps.get_context.outputs.user_request }}`
-            - **Issue Body長さ**: ${{ length(steps.get_description.outputs.description) }}文字
-            - **コメント長さ**: ${{ length(steps.get_comments.outputs.comments) }}文字
+            - **Issue Body文字数**: 詳細はログを確認してください
+            - **コメント文字数**: 詳細はログを確認してください
 
             ## 役割
 
```
