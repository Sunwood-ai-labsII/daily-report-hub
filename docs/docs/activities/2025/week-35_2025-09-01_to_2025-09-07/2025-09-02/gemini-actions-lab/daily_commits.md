# 📝 Daily Commits

## ⏰ 14:12:03 - `fe23559`
**add**
*by maki*

### 📋 Changed Files
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Tue Sep 2 14:12:03 2025 +0000
M	.github/workflows/gemini-issue-automated-triage.yml
M	.github/workflows/gemini-issue-scheduled-triage.yml
```

### 📊 Statistics
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Tue Sep 2 14:12:03 2025 +0000

    add

 .../workflows/gemini-issue-automated-triage.yml    | 64 ++++++++++++++++----
 .../workflows/gemini-issue-scheduled-triage.yml    | 69 ++++++++++++++++++----
 2 files changed, 111 insertions(+), 22 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index bc76c52..12875fe 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -97,11 +97,12 @@ jobs:
         with:
           github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           script: |-
-            const { data: labels } = await github.rest.issues.listLabelsForRepo({
+            const labels = await github.paginate(github.rest.issues.listLabelsForRepo, {
               owner: context.repo.owner,
               repo: context.repo.repo,
+              per_page: 100,
             });
-            const labelNames = labels.map(label => label.name);
+            const labelNames = labels.map(label => label.name).filter(Boolean);
             core.setOutput('available_labels', labelNames.join(','));
             core.info(`Found ${labelNames.length} labels: ${labelNames.join(', ')}`);
             return labelNames;
@@ -166,7 +167,7 @@ jobs:
           LABELS_OUTPUT: '${{ steps.gemini_issue_analysis.outputs.summary }}'
         uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
         with:
-          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          github-token: '${{ secrets.GH_PAT || steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           script: |-
             // Strip code block markers if present and extract JSON
             const rawLabels = process.env.LABELS_OUTPUT;
@@ -239,16 +240,57 @@ jobs:
 
             const issueNumber = parseInt(process.env.ISSUE_NUMBER);
 
+            // Track available labels and allow auto-create of missing labels using GH_PAT
+            const available = new Set(
+              (process.env.AVAILABLE_LABELS || '')
+                .split(',')
+                .map(s => s.trim())
+                .filter(Boolean)
+            );
+
             // Set labels based on triage result
             if (parsedLabels.labels_to_set && parsedLabels.labels_to_set.length > 0) {
-              await github.rest.issues.setLabels({
-                owner: context.repo.owner,
-                repo: context.repo.repo,
-                issue_number: issueNumber,
-                labels: parsedLabels.labels_to_set
-              });
-              const explanation = parsedLabels.explanation ? ` - ${parsedLabels.explanation}` : '';
-              core.info(`Successfully set labels for #${issueNumber}: ${parsedLabels.labels_to_set.join(', ')}${explanation}`);
+              const proposed = [...new Set(parsedLabels.labels_to_set.map(s => String(s).trim()).filter(Boolean))];
+
+              // Attempt to create any missing labels using the provided token
+              for (const label of proposed) {
+                if (available.has(label)) continue;
+                try {
+                  await github.rest.issues.createLabel({
+                    owner: context.repo.owner,
+                    repo: context.repo.repo,
+                    name: label,
+                    color: 'ededed',
+                    description: 'Auto-created by Gemini triage'
+                  });
+                  core.info(`Created missing label: ${label}`);
+                  available.add(label);
+                } catch (err) {
+                  // Ignore if already exists (422), otherwise log error and continue
+                  const status = err?.status || err?.response?.status;
+                  if (status === 422) {
+                    core.info(`Label already exists (race): ${label}`);
+                    available.add(label);
+                  } else {
+                    core.error(`Failed to create label '${label}': ${err}`);
+                  }
+                }
+              }
+
+              const finalLabels = proposed.filter(l => available.has(l));
+              if (finalLabels.length === 0) {
+                const explanation = parsedLabels.explanation ? ` - ${parsedLabels.explanation}` : '';
+                core.info(`No applicable labels for #${issueNumber} after creation attempts. Skipping.${explanation}`);
+              } else {
+                await github.rest.issues.addLabels({
+                  owner: context.repo.owner,
+                  repo: context.repo.repo,
+                  issue_number: issueNumber,
+                  labels: finalLabels
+                });
+                const explanation = parsedLabels.explanation ? ` - ${parsedLabels.explanation}` : '';
+                core.info(`Applied labels for #${issueNumber}: ${finalLabels.join(', ')}${explanation}`);
+              }
             } else {
               // If no labels to set, leave the issue as is
               const explanation = parsedLabels.explanation ? ` - ${parsedLabels.explanation}` : '';
diff --git a/.github/workflows/gemini-issue-scheduled-triage.yml b/.github/workflows/gemini-issue-scheduled-triage.yml
index aacbbe4..3b18806 100644
--- a/.github/workflows/gemini-issue-scheduled-triage.yml
+++ b/.github/workflows/gemini-issue-scheduled-triage.yml
@@ -68,11 +68,12 @@ jobs:
         with:
```

---

## ⏰ 14:41:14 - `d1f492c`
**add**
*by maki*

### 📋 Changed Files
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Tue Sep 2 14:41:14 2025 +0000
M	.github/workflows/gemini-issue-scheduled-triage.yml
```

### 📊 Statistics
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Tue Sep 2 14:41:14 2025 +0000

    add

 .../workflows/gemini-issue-scheduled-triage.yml    | 46 ++++++++++++----------
 1 file changed, 26 insertions(+), 20 deletions(-)
```

### 💻 Code Changes
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

---

