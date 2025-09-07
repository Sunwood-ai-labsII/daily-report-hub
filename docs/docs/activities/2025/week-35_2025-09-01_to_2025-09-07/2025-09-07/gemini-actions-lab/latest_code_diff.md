# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 1539ea8..1049c1b 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -76,17 +76,16 @@ jobs:
       github.event_name == 'issues' && github.event.action == 'opened' &&
       contains(github.event.issue.body, '@gemini-cli')
 
-    timeout-minutes: 10
+          timeout-minutes: 10
     runs-on: 'ubuntu-latest'
     steps:
       - name: 'Debug Event Information'
         run: |-
           echo "Event Name: ${{ github.event_name }}"
-          echo "Event Action: ${{ github.event.action }}"  
-          echo "Repository Private: ${{ github.event.repository.private }}"
+          echo "Event Action: ${{ github.event.action }}"
+          echo "Issue Author: ${{ github.event.issue.user.login }}"
           echo "Author Association: ${{ github.event.issue.author_association }}"
-          echo "Issue Body Contains @gemini-cli: ${{ contains(github.event.issue.body, '@gemini-cli') }}"
-          
+
       - name: 'Generate GitHub App Token'
         id: 'generate_token'
         if: |-
@@ -128,13 +127,18 @@ jobs:
           fi
 
           # Clean up user request
-          USER_REQUEST=$(echo "${USER_REQUEST}" | sed 's/.*@gemini-cli//' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
-
+          CLEANED_USER_REQUEST=$(echo "${USER_REQUEST}" | sed 's/.*@gemini-cli//' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
+          
+          # ⬇⬇⬇ ここからが修正箇所 ⬇⬇⬇
+          # GITHUB_OUTPUTへの書き込みをヒアドキュメント形式に変更して、特殊文字によるエラーを回避
           {
-            echo "user_request=${USER_REQUEST}"
+            echo 'user_request<<EOF'
+            echo "${CLEANED_USER_REQUEST}"
+            echo 'EOF'
             echo "issue_number=${ISSUE_NUMBER}"
             echo "is_pr=${IS_PR}"
           } >> "${GITHUB_OUTPUT}"
+          # ⬆⬆⬆ ここまでが修正箇所 ⬆⬆⬆
 
       - name: 'Set up git user for commits'
         run: |-
```
