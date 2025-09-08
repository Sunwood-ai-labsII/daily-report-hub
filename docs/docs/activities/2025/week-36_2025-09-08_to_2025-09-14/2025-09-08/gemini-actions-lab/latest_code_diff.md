# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index 2ded6df..861d0d6 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -21,15 +21,18 @@ jobs:
     steps:
       - name: 'Get Issue Info'
         id: issue
+        env:
+          INPUT_ISSUE_NUMBER: ${{ github.event.inputs.issue_number }}
         uses: actions/github-script@v7
         with:
           script: |
             let issue;
             if (context.eventName === 'workflow_dispatch') {
+              const issueNumber = parseInt(process.env.INPUT_ISSUE_NUMBER);
               const { data } = await github.rest.issues.get({
                 owner: context.repo.owner,
                 repo: context.repo.repo,
-                issue_number: ${{ github.event.inputs.issue_number }}
+                issue_number: issueNumber
               });
               issue = data;
             } else {
@@ -56,12 +59,16 @@ jobs:
       - name: 'Analyze with Gemini'
         uses: google-github-actions/run-gemini-cli@v0
         id: gemini
+        env:
+          ISSUE_TITLE: ${{ steps.issue.outputs.title }}
+          ISSUE_BODY: ${{ steps.issue.outputs.body }}
+          AVAILABLE_LABELS: ${{ steps.labels.outputs.available }}
         with:
           gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
           prompt: |
-            Issue Title: ${{ steps.issue.outputs.title }}
-            Issue Body: ${{ steps.issue.outputs.body }}
-            Available Labels: ${{ steps.labels.outputs.available }}
+            Issue Title: ${ISSUE_TITLE}
+            Issue Body: ${ISSUE_BODY}
+            Available Labels: ${AVAILABLE_LABELS}
             
             Select appropriate labels for this GitHub issue. Use this XML format:
             <labels>
```
