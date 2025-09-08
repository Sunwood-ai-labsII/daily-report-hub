# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index 32a71f6..2ded6df 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -70,10 +70,15 @@ jobs:
             </labels>
 
       - name: 'Apply Labels'
+        env:
+          GEMINI_OUTPUT: ${{ steps.gemini.outputs.summary }}
+          ISSUE_NUMBER: ${{ steps.issue.outputs.number }}
         uses: actions/github-script@v7
         with:
           script: |
-            const output = `${{ steps.gemini.outputs.summary }}`;
+            const output = process.env.GEMINI_OUTPUT;
+            const issueNumber = parseInt(process.env.ISSUE_NUMBER);
+            
             console.log('Gemini output:', output);
             
             let labels = [];
@@ -100,7 +105,7 @@ jobs:
               await github.rest.issues.addLabels({
                 owner: context.repo.owner,
                 repo: context.repo.repo,
-                issue_number: ${{ steps.issue.outputs.number }},
+                issue_number: issueNumber,
                 labels: labels
               });
               console.log(`Applied labels: ${labels.join(', ')}`);
```
