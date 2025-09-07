# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 1049c1b..56e56dd 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -129,8 +129,8 @@ jobs:
           # Clean up user request
           CLEANED_USER_REQUEST=$(echo "${USER_REQUEST}" | sed 's/.*@gemini-cli//' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
           
-          # ⬇⬇⬇ ここからが修正箇所 ⬇⬇⬇
-          # GITHUB_OUTPUTへの書き込みをヒアドキュメント形式に変更して、特殊文字によるエラーを回避
+          # ⬇⬇⬇ ここを修正 ⬇⬇⬇
+          # GITHUB_OUTPUTへの書き込みをヒアドキュメント形式に変更
           {
             echo 'user_request<<EOF'
             echo "${CLEANED_USER_REQUEST}"
@@ -138,7 +138,6 @@ jobs:
             echo "issue_number=${ISSUE_NUMBER}"
             echo "is_pr=${IS_PR}"
           } >> "${GITHUB_OUTPUT}"
-          # ⬆⬆⬆ ここまでが修正箇所 ⬆⬆⬆
 
       - name: 'Set up git user for commits'
         run: |-
```
