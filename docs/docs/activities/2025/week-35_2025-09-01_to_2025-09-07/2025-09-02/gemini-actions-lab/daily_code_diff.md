# 💻 Daily Code Changes

## Full Diff

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
index aacbbe4..e22de31 100644
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
@@ -68,11 +74,12 @@ jobs:
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
@@ -109,42 +116,38 @@ jobs:
           prompt: |-
             ## Role
 
-            You are an issue triage assistant. Analyze the GitHub issues and
-            identify the most appropriate existing labels to apply.
+            You are an issue triage assistant. Analyze ONLY the provided GitHub issues
+            and pick appropriate labels from the available labels list.
 
-            ## Steps
+            ## Inputs
+            - Available labels: "${AVAILABLE_LABELS}"
+            - Candidate issues (JSON array): "${ISSUES_TO_TRIAGE}"
 
-            1. Review the available labels in the environment variable: "${AVAILABLE_LABELS}".
-            2. Review the issues in the environment variable: "${ISSUES_TO_TRIAGE}".
-            3. For each issue, classify it by the appropriate labels from the available labels.
-            4. Output a JSON array of objects, each containing the issue number,
-               the labels to set, and a brief explanation. For example:
-               \```
+            ## Critical rules
+            - Output MUST be a JSON array.
+            - Every object MUST have an `issue_number` that appears in "${ISSUES_TO_TRIAGE}".
+            - Never include any issue numbers that are not in "${ISSUES_TO_TRIAGE}".
+            - If there is exactly one candidate, output exactly one object for that issue.
+            - Only choose labels from "${AVAILABLE_LABELS}".
+
+            ## Steps
+            1. Read the candidate issues from "${ISSUES_TO_TRIAGE}".
+            2. For each candidate, select one or more labels from "${AVAILABLE_LABELS}".
+            3. Return a JSON array with objects like:
+               \```json
                [
                  {
                    "issue_number": 123,
                    "labels_to_set": ["kind/bug", "priority/p2"],
-                   "explanation": "This is a bug report with high priority based on the error description"
-                 },
-                 {
-                   "issue_number": 456,
-                   "labels_to_set": ["kind/enhancement"],
-                   "explanation": "This is a feature request for improving the UI"
+                   "explanation": "Brief reason"
                  }
                ]
                \```
-            5. If an issue cannot be classified, do not include it in the output array.
 
-            ## Guidelines
-
-            - Only use labels that already exist in the repository
-            - Assign all applicable labels based on the issue content
-            - Reference all shell variables as "${VAR}" (with quotes and braces)
-            - Do NOT run any shell or external commands; use only the provided environment variables
-            - Do NOT attempt to execute `gh label list` or call the GitHub API to fetch labels. The full list of labels is provided in "${AVAILABLE_LABELS}".
-            - Do NOT attempt to list or fetch issues yourself. The issues to triage are provided in "${ISSUES_TO_TRIAGE}".
-            - Output only valid JSON format
-            - Do not include any explanation or additional text, just the JSON
+            ## Constraints
+            - Reference variables exactly as shown; do NOT execute any shell commands.
+            - Do NOT fetch labels or issues yourself; use the inputs above.
+            - Output only valid JSON. Do not write any additional text.
 
       - name: 'Apply Labels to Issues'
         if: |-
@@ -153,9 +156,11 @@ jobs:
         env:
           REPOSITORY: '${{ github.repository }}'
           LABELS_OUTPUT: '${{ steps.gemini_issue_analysis.outputs.summary }}'
+          AVAILABLE_LABELS: '${{ steps.get_labels.outputs.available_labels }}'
+          ISSUES_TO_TRIAGE: '${{ steps.find_issues.outputs.issues_to_triage }}'
         uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
         with:
-          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          github-token: '${{ secrets.GH_PAT || steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           script: |-
             // Hardened JSON extraction to tolerate extra text
             const rawLabels = process.env.LABELS_OUTPUT || '';
@@ -193,6 +198,26 @@ jobs:
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
+            // Build a set of candidate issue numbers to enforce scope
+            let candidates = [];
+            try {
+              candidates = JSON.parse(process.env.ISSUES_TO_TRIAGE || '[]');
+            } catch {}
+            const allowed = new Set(candidates.map(c => Number(c.number)).filter(n => Number.isInteger(n)));
+            core.info(`Will only apply to candidate issues: ${[...allowed].map(n => '#' + n).join(', ')}`);
+
+            let appliedCount = 0;
+            const ignoredNonCandidates = [];
+
             for (const entry of parsedLabels) {
               const issueNumber = entry.issue_number;
               if (!issueNumber) {
@@ -200,18 +225,98 @@ jobs:
                 continue;
               }
 
+              if (!allowed.has(Number(issueNumber))) {
+                ignoredNonCandidates.push(Number(issueNumber));
+                continue;
+              }
+
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
+                  appliedCount++;
+                } catch (err) {
+                  core.error(`Failed applying labels to #${issueNumber}: ${err}`);
+                }
               } else {
                 // If no labels to set, leave the issue as is
                 core.info(`No labels to set for #${issueNumber}, leaving as is`);
               }
             }
+
+            if (ignoredNonCandidates.length > 0) {
+              core.info(`Ignored non-candidate issues from model output: ${ignoredNonCandidates.map(n => '#' + n).join(', ')}`);
+            }
+
+            // Fallback: if nothing applied to candidates, add a minimal triage label
+            if (appliedCount === 0 && allowed.size > 0) {
+              const fallbackLabel = 'status/needs-triage';
+              try {
+                if (!available.has(fallbackLabel)) {
+                  await github.rest.issues.createLabel({
+                    owner: context.repo.owner,
+                    repo: context.repo.repo,
+                    name: fallbackLabel,
+                    color: 'ededed',
+                    description: 'Auto-created fallback triage label'
+                  });
+                  available.add(fallbackLabel);
+                  core.info(`Created fallback label: ${fallbackLabel}`);
+                }
+
+                for (const num of allowed) {
+                  try {
+                    await github.rest.issues.addLabels({
+                      owner: context.repo.owner,
+                      repo: context.repo.repo,
+                      issue_number: num,
+                      labels: [fallbackLabel]
+                    });
+                    core.info(`Applied fallback label to #${num}: ${fallbackLabel}`);
+                  } catch (err) {
+                    core.error(`Failed applying fallback label to #${num}: ${err}`);
+                  }
+                }
+              } catch (err) {
+                core.error(`Fallback labeling failed: ${err}`);
+              }
+            }
```
