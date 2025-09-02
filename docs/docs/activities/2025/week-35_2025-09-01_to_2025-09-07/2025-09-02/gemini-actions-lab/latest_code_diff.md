# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-issue-scheduled-triage.yml b/.github/workflows/gemini-issue-scheduled-triage.yml
index 914a5ac..47060bf 100644
--- a/.github/workflows/gemini-issue-scheduled-triage.yml
+++ b/.github/workflows/gemini-issue-scheduled-triage.yml
@@ -161,6 +161,7 @@ jobs:
           REPOSITORY: '${{ github.repository }}'
           LABELS_OUTPUT: '${{ steps.gemini_issue_analysis.outputs.summary }}'
           AVAILABLE_LABELS: '${{ steps.get_labels.outputs.available_labels }}'
+          ISSUES_TO_TRIAGE: '${{ steps.find_issues.outputs.issues_to_triage }}'
         uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
         with:
           github-token: '${{ secrets.GH_PAT || steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
@@ -210,6 +211,14 @@ jobs:
             );
             core.info(`Available labels (enforced): ${[...available].join(', ')}`);
 
+            // Build a set of candidate issue numbers to enforce scope
+            let candidates = [];
+            try {
+              candidates = JSON.parse(process.env.ISSUES_TO_TRIAGE || '[]');
+            } catch {}
+            const allowed = new Set(candidates.map(c => Number(c.number)).filter(n => Number.isInteger(n)));
+            core.info(`Will only apply to candidate issues: ${[...allowed].map(n => '#' + n).join(', ')}`);
+
             for (const entry of parsedLabels) {
               const issueNumber = entry.issue_number;
               if (!issueNumber) {
@@ -217,6 +226,11 @@ jobs:
                 continue;
               }
 
+              if (!allowed.has(Number(issueNumber))) {
+                core.info(`Ignoring non-candidate issue #${issueNumber}`);
+                continue;
+              }
+
               // Set labels based on triage result
               if (entry.labels_to_set && entry.labels_to_set.length > 0) {
                 const proposed = [...new Set(entry.labels_to_set.map(s => String(s).trim()).filter(Boolean))];
```
