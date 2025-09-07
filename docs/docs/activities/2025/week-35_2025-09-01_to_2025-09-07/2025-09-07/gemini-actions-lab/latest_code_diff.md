# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 979f1f2..1539ea8 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -30,48 +30,63 @@ permissions:
   issues: 'write'
 
 jobs:
+  # gemini-cli:
+  #   # This condition seeks to ensure the action is only run when it is triggered by a trusted user.
+  #   # For private repos, users who have access to the repo are considered trusted.
+  #   # For public repos, users who members, owners, or collaborators are considered trusted.
+  #   if: |-
+  #     github.event_name == 'workflow_dispatch' ||
+  #     (
+  #       github.event_name == 'issues' && github.event.action == 'opened' &&
+  #       contains(github.event.issue.body, '@gemini-cli') &&
+  #       !contains(github.event.issue.body, '@gemini-cli /review') &&
+  #       !contains(github.event.issue.body, '@gemini-cli /triage') &&
+  #       (
+  #         github.event.repository.private == true ||
+  #         contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.issue.author_association)
+  #       )
+  #     ) ||
+  #     (
+  #       (
+  #         github.event_name == 'issue_comment' ||
+  #         github.event_name == 'pull_request_review_comment'
+  #       ) &&
+  #       contains(github.event.comment.body, '@gemini-cli') &&
+  #       !contains(github.event.comment.body, '@gemini-cli /review') &&
+  #       !contains(github.event.comment.body, '@gemini-cli /triage') &&
+  #       (
+  #         github.event.repository.private == true ||
+  #         contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association)
+  #       )
+  #     ) ||
+  #     (
+  #       github.event_name == 'pull_request_review' &&
+  #       contains(github.event.review.body, '@gemini-cli') &&
+  #       !contains(github.event.review.body, '@gemini-cli /review') &&
+  #       !contains(github.event.review.body, '@gemini-cli /triage') &&
+  #       (
+  #         github.event.repository.private == true ||
+  #         contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.review.author_association)
+  #       )
+  #     )
+
   gemini-cli:
-    # This condition seeks to ensure the action is only run when it is triggered by a trusted user.
-    # For private repos, users who have access to the repo are considered trusted.
-    # For public repos, users who members, owners, or collaborators are considered trusted.
+    # 一時的にシンプルな条件に変更してテスト
     if: |-
-      github.event_name == 'workflow_dispatch' ||
-      (
-        github.event_name == 'issues' && github.event.action == 'opened' &&
-        contains(github.event.issue.body, '@gemini-cli') &&
-        !contains(github.event.issue.body, '@gemini-cli /review') &&
-        !contains(github.event.issue.body, '@gemini-cli /triage') &&
-        (
-          github.event.repository.private == true ||
-          contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.issue.author_association)
-        )
-      ) ||
-      (
-        (
-          github.event_name == 'issue_comment' ||
-          github.event_name == 'pull_request_review_comment'
-        ) &&
-        contains(github.event.comment.body, '@gemini-cli') &&
-        !contains(github.event.comment.body, '@gemini-cli /review') &&
-        !contains(github.event.comment.body, '@gemini-cli /triage') &&
-        (
-          github.event.repository.private == true ||
-          contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association)
-        )
-      ) ||
-      (
-        github.event_name == 'pull_request_review' &&
-        contains(github.event.review.body, '@gemini-cli') &&
-        !contains(github.event.review.body, '@gemini-cli /review') &&
-        !contains(github.event.review.body, '@gemini-cli /triage') &&
-        (
-          github.event.repository.private == true ||
-          contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.review.author_association)
-        )
-      )
+      github.event_name == 'issues' && github.event.action == 'opened' &&
+      contains(github.event.issue.body, '@gemini-cli')
+
     timeout-minutes: 10
     runs-on: 'ubuntu-latest'
     steps:
+      - name: 'Debug Event Information'
+        run: |-
+          echo "Event Name: ${{ github.event_name }}"
+          echo "Event Action: ${{ github.event.action }}"  
+          echo "Repository Private: ${{ github.event.repository.private }}"
+          echo "Author Association: ${{ github.event.issue.author_association }}"
+          echo "Issue Body Contains @gemini-cli: ${{ contains(github.event.issue.body, '@gemini-cli') }}"
+          
       - name: 'Generate GitHub App Token'
         id: 'generate_token'
         if: |-
@@ -115,11 +130,8 @@ jobs:
           # Clean up user request
           USER_REQUEST=$(echo "${USER_REQUEST}" | sed 's/.*@gemini-cli//' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
 
-          # Write outputs safely (supporting newlines/special chars)
           {
-            echo 'user_request<<EOF'
-            echo "${USER_REQUEST}"
-            echo 'EOF'
+            echo "user_request=${USER_REQUEST}"
             echo "issue_number=${ISSUE_NUMBER}"
             echo "is_pr=${IS_PR}"
           } >> "${GITHUB_OUTPUT}"
@@ -212,7 +224,6 @@ jobs:
           DESCRIPTION: '${{ steps.get_description.outputs.description }}'
           COMMENTS: '${{ steps.get_comments.outputs.comments }}'
           USER_REQUEST: '${{ steps.get_context.outputs.user_request }}'
-          GITHUB_WORKSPACE: '${{ github.workspace }}'
         run: |-
           set -euo pipefail
           TEMPLATE_PATH=".github/prompts/gemini-cli_prompt.ja.md"
@@ -220,9 +231,16 @@ jobs:
             echo "Prompt template not found: ${TEMPLATE_PATH}" >&2
             exit 1
           fi
-          # Robust variable substitution using envsubst (handles braces/newlines safely)
-          # Limit substitution to specific variables to avoid accidental replacements
-          EXPANDED=$(envsubst '${REPOSITORY} ${EVENT_NAME} ${ISSUE_NUMBER} ${IS_PR} ${DESCRIPTION} ${COMMENTS} ${USER_REQUEST} ${GITHUB_WORKSPACE}' < "${TEMPLATE_PATH}")
+          # Safe variable substitution without executing content
+          EXPANDED=$(sed \
+            -e "s|\\$\\{REPOSITORY\\}|${REPOSITORY}|g" \
+            -e "s|\\$\\{EVENT_NAME\\}|${EVENT_NAME}|g" \
+            -e "s|\\$\\{ISSUE_NUMBER\\}|${ISSUE_NUMBER}|g" \
+            -e "s|\\$\\{IS_PR\\}|${IS_PR}|g" \
+            -e "s|\\$\\{DESCRIPTION\\}|${DESCRIPTION}|g" \
+            -e "s|\\$\\{COMMENTS\\}|${COMMENTS}|g" \
+            -e "s|\\$\\{USER_REQUEST\\}|${USER_REQUEST}|g" \
+            "${TEMPLATE_PATH}")
           {
             echo "prompt<<EOF"
             echo "${EXPANDED}"
```
