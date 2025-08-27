# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-jp-cli.yml b/.github/workflows/gemini-jp-cli.yml
index 858f00e..12fe964 100644
--- a/.github/workflows/gemini-jp-cli.yml
+++ b/.github/workflows/gemini-jp-cli.yml
@@ -112,8 +112,11 @@ jobs:
           # ユーザーリクエストをクリーンアップ
           USER_REQUEST=$(echo "${USER_REQUEST}" | sed 's/.*@gemini-jp-cli//' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
 
+          # GITHUB_OUTPUTへの書き込みをheredoc形式に変更して、特殊文字によるエラーを回避
           {
-            echo "user_request=${USER_REQUEST}"
+            echo 'user_request<<EOF'
+            echo "${USER_REQUEST}"
+            echo 'EOF'
             echo "issue_number=${ISSUE_NUMBER}"
             echo "is_pr=${IS_PR}"
           } >> "${GITHUB_OUTPUT}"
@@ -148,7 +151,6 @@ jobs:
           GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           ISSUE_NUMBER: '${{ steps.get_context.outputs.issue_number }}'
           REPOSITORY: '${{ github.repository }}'
-          REQUEST_TYPE: '${{ steps.get_context.outputs.request_type }}'
         run: |-
           set -euo pipefail
           MESSAGE="@${GITHUB_ACTOR} リクエストを受け取りました。今から作業を開始します！ 🤖"
```
