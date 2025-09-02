# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-issue-scheduled-triage.yml b/.github/workflows/gemini-issue-scheduled-triage.yml
index 3b18806..914a5ac 100644
--- a/.github/workflows/gemini-issue-scheduled-triage.yml
+++ b/.github/workflows/gemini-issue-scheduled-triage.yml
@@ -38,29 +38,35 @@ jobs:
 
       - name: 'Find untriaged issues'
         id: 'find_issues'
-        env:
-          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          GITHUB_REPOSITORY: '${{ github.repository }}'
-          GITHUB_OUTPUT: '${{ github.output }}'
-        run: |-
-          set -euo pipefail
-
-          echo '🔍 Finding issues without labels...'
-          NO_LABEL_ISSUES="$(gh issue list --repo "${GITHUB_REPOSITORY}" \
-            --search 'is:open is:issue no:label' --json number,title,body)"
-
-          echo '🏷️ Finding issues that need triage...'
-          NEED_TRIAGE_ISSUES="$(gh issue list --repo "${GITHUB_REPOSITORY}" \
-            --search 'is:open is:issue label:"status/needs-triage"' --json number,title,body)"
+        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+        with:
+          github-token: '${{ secrets.GH_PAT || steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          script: |-
+            const owner = context.repo.owner;
+            const repo = context.repo.repo;
 
-          echo '🔄 Merging and deduplicating issues...'
-          ISSUES="$(echo "${NO_LABEL_ISSUES}" "${NEED_TRIAGE_ISSUES}" | jq -c -s 'add | unique_by(.number)')"
+            // Fetch all open issues with pagination
+            const allOpen = await github.paginate(github.rest.issues.listForRepo, {
+              owner,
+              repo,
+              state: 'open',
+              per_page: 100,
+            });
 
-          echo '📝 Setting output for GitHub Actions...'
-          echo "issues_to_triage=${ISSUES}" >> "${GITHUB_OUTPUT}"
+            const candidates = [];
+            for (const it of allOpen) {
+              // Skip pull requests
+              if (it.pull_request) continue;
+              const labels = (it.labels || []).map(l => typeof l === 'string' ? l : l.name).filter(Boolean);
+              const hasNeedsTriage = labels.includes('status/needs-triage');
+              const hasNoLabels = labels.length === 0;
+              if (hasNoLabels || hasNeedsTriage) {
+                candidates.push({ number: it.number, title: it.title || '', body: it.body || '' });
+              }
+            }
 
-          ISSUE_COUNT="$(echo "${ISSUES}" | jq 'length')"
-          echo "✅ Found ${ISSUE_COUNT} issues to triage! 🎯"
+            core.info(`✅ Found ${candidates.length} issues to triage: ${candidates.map(i => '#' + i.number).join(', ')}`);
+            core.setOutput('issues_to_triage', JSON.stringify(candidates));
 
       - name: 'Get Repository Labels'
         id: 'get_labels'
```
