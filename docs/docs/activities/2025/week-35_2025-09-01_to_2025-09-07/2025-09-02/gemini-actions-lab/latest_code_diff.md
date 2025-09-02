# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-issue-scheduled-triage.yml b/.github/workflows/gemini-issue-scheduled-triage.yml
index 47060bf..e22de31 100644
--- a/.github/workflows/gemini-issue-scheduled-triage.yml
+++ b/.github/workflows/gemini-issue-scheduled-triage.yml
@@ -116,42 +116,38 @@ jobs:
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
-
-            ## Guidelines
 
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
@@ -219,6 +215,9 @@ jobs:
             const allowed = new Set(candidates.map(c => Number(c.number)).filter(n => Number.isInteger(n)));
             core.info(`Will only apply to candidate issues: ${[...allowed].map(n => '#' + n).join(', ')}`);
 
+            let appliedCount = 0;
+            const ignoredNonCandidates = [];
+
             for (const entry of parsedLabels) {
               const issueNumber = entry.issue_number;
               if (!issueNumber) {
@@ -227,7 +226,7 @@ jobs:
               }
 
               if (!allowed.has(Number(issueNumber))) {
-                core.info(`Ignoring non-candidate issue #${issueNumber}`);
+                ignoredNonCandidates.push(Number(issueNumber));
                 continue;
               }
 
@@ -274,6 +273,7 @@ jobs:
                   });
                   const explanation = entry.explanation ? ` - ${entry.explanation}` : '';
                   core.info(`Applied labels to #${issueNumber}: ${finalLabels.join(', ')}${explanation}`);
+                  appliedCount++;
                 } catch (err) {
                   core.error(`Failed applying labels to #${issueNumber}: ${err}`);
                 }
@@ -282,3 +282,41 @@ jobs:
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
