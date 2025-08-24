# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-cli-jp.yml b/.github/workflows/gemini-cli-jp.yml
index dee8545..858f00e 100644
--- a/.github/workflows/gemini-cli-jp.yml
+++ b/.github/workflows/gemini-cli-jp.yml
@@ -35,9 +35,9 @@ jobs:
       github.event_name == 'workflow_dispatch' ||
       (
         github.event_name == 'issues' && github.event.action == 'opened' &&
-        contains(github.event.issue.body, '@gemini-cli-jp') &&
-        !contains(github.event.issue.body, '@gemini-cli-jp /review') &&
-        !contains(github.event.issue.body, '@gemini-cli-jp /triage') &&
+        contains(github.event.issue.body, '@gemini-jp-cli') &&
+        !contains(github.event.issue.body, '@gemini-jp-cli /review') &&
+        !contains(github.event.issue.body, '@gemini-jp-cli /triage') &&
         (
           github.event.repository.private == true ||
           contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.issue.author_association)
@@ -48,9 +48,9 @@ jobs:
           github.event_name == 'issue_comment' ||
           github.event_name == 'pull_request_review_comment'
         ) &&
-        contains(github.event.comment.body, '@gemini-cli-jp') &&
-        !contains(github.event.comment.body, '@gemini-cli-jp /review') &&
-        !contains(github.event.comment.body, '@gemini-cli-jp /triage') &&
+        contains(github.event.comment.body, '@gemini-jp-cli') &&
+        !contains(github.event.comment.body, '@gemini-jp-cli /review') &&
+        !contains(github.event.comment.body, '@gemini-jp-cli /triage') &&
         (
           github.event.repository.private == true ||
           contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association)
@@ -58,9 +58,9 @@ jobs:
       ) ||
       (
         github.event_name == 'pull_request_review' &&
-        contains(github.event.review.body, '@gemini-cli-jp') &&
-        !contains(github.event.review.body, '@gemini-cli-jp /review') &&
-        !contains(github.event.review.body, '@gemini-cli-jp /triage') &&
+        contains(github.event.review.body, '@gemini-jp-cli') &&
+        !contains(github.event.review.body, '@gemini-jp-cli /review') &&
+        !contains(github.event.review.body, '@gemini-jp-cli /triage') &&
         (
           github.event.repository.private == true ||
           contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.review.author_association)
@@ -110,7 +110,7 @@ jobs:
           fi
 
           # ユーザーリクエストをクリーンアップ
-          USER_REQUEST=$(echo "${USER_REQUEST}" | sed 's/.*@gemini-cli-jp//' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
+          USER_REQUEST=$(echo "${USER_REQUEST}" | sed 's/.*@gemini-jp-cli//' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
 
           {
             echo "user_request=${USER_REQUEST}"
```
