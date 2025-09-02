# 🔄 Latest Code Changes

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
@@ -153,9 +154,10 @@ jobs:
         env:
           REPOSITORY: '${{ github.repository }}'
           LABELS_OUTPUT: '${{ steps.gemini_issue_analysis.outputs.summary }}'
+          AVAILABLE_LABELS: '${{ steps.get_labels.outputs.available_labels }}'
         uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
         with:
-          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          github-token: '${{ secrets.GH_PAT || steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           script: |-
             // Hardened JSON extraction to tolerate extra text
             const rawLabels = process.env.LABELS_OUTPUT || '';
@@ -193,6 +195,15 @@ jobs:
               return;
             }
 
+            // Build a set of existing labels, and auto-create missing ones using GH_PAT
+            const available = new Set(
+              (process.env.AVAILABLE_LABELS || '')
+                .split(',')
+                .map(s => s.trim())
+                .filter(Boolean)
+            );
+            core.info(`Available labels (enforced): ${[...available].join(', ')}`);
+
             for (const entry of parsedLabels) {
               const issueNumber = entry.issue_number;
               if (!issueNumber) {
@@ -202,14 +213,50 @@ jobs:
 
               // Set labels based on triage result
               if (entry.labels_to_set && entry.labels_to_set.length > 0) {
-                await github.rest.issues.setLabels({
-                  owner: context.repo.owner,
-                  repo: context.repo.repo,
-                  issue_number: issueNumber,
-                  labels: entry.labels_to_set
-                });
-                const explanation = entry.explanation ? ` - ${entry.explanation}` : '';
-                core.info(`Successfully set labels for #${issueNumber}: ${entry.labels_to_set.join(', ')}${explanation}`);
+                const proposed = [...new Set(entry.labels_to_set.map(s => String(s).trim()).filter(Boolean))];
+
+                // Create any missing labels first
+                for (const label of proposed) {
+                  if (available.has(label)) continue;
+                  try {
+                    await github.rest.issues.createLabel({
+                      owner: context.repo.owner,
+                      repo: context.repo.repo,
+                      name: label,
+                      color: 'ededed',
+                      description: 'Auto-created by Gemini triage'
+                    });
+                    core.info(`Created missing label: ${label}`);
+                    available.add(label);
+                  } catch (err) {
+                    const status = err?.status || err?.response?.status;
+                    if (status === 422) {
+                      core.info(`Label already exists (race): ${label}`);
+                      available.add(label);
+                    } else {
+                      core.error(`Failed to create label '${label}': ${err}`);
+                    }
+                  }
+                }
+
+                const finalLabels = proposed.filter(l => available.has(l));
+                if (finalLabels.length === 0) {
+                  core.info(`Skipping #${issueNumber}: no applicable labels after creation attempts [${proposed.join(', ')}]`);
+                  continue;
+                }
+
+                try {
+                  await github.rest.issues.addLabels({
+                    owner: context.repo.owner,
+                    repo: context.repo.repo,
+                    issue_number: issueNumber,
+                    labels: finalLabels
+                  });
+                  const explanation = entry.explanation ? ` - ${entry.explanation}` : '';
+                  core.info(`Applied labels to #${issueNumber}: ${finalLabels.join(', ')}${explanation}`);
+                } catch (err) {
+                  core.error(`Failed applying labels to #${issueNumber}: ${err}`);
+                }
               } else {
                 // If no labels to set, leave the issue as is
                 core.info(`No labels to set for #${issueNumber}, leaving as is`);
```
