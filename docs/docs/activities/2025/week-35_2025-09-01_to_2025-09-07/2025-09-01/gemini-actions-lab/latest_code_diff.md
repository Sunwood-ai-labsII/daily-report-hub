# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index 4c85ade..bc76c52 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -129,9 +129,7 @@ jobs:
             {
               "debug": true,
               "maxSessionTurns": 25,
-              "coreTools": [
-                "run_shell_command(echo)"
-              ],
+              "coreTools": [],
               "telemetry": {
                 "enabled": false,
                 "target": "gcp"
@@ -150,6 +148,10 @@ jobs:
             
             Important: Respond with ONLY the JSON object, no additional text or explanations before or after.
 
+            Constraints:
+            - Do NOT run any shell or external commands; use only the provided environment variables
+            - Do NOT attempt to execute `gh label list` or call the GitHub API to fetch labels. The available labels are already provided in "${AVAILABLE_LABELS}".
+
             Output format (JSON only):
             {"labels_to_set": ["label1", "label2"], "explanation": "reasoning for these labels"}
 
diff --git a/.github/workflows/gemini-issue-scheduled-triage.yml b/.github/workflows/gemini-issue-scheduled-triage.yml
index 878dc72..aacbbe4 100644
--- a/.github/workflows/gemini-issue-scheduled-triage.yml
+++ b/.github/workflows/gemini-issue-scheduled-triage.yml
@@ -100,9 +100,7 @@ jobs:
             {
               "debug": ${{ fromJSON(env.DEBUG || env.ACTIONS_STEP_DEBUG || false) }},
               "maxSessionTurns": 25,
-              "coreTools": [
-                "run_shell_command(echo)"
-              ],
+              "coreTools": [],
               "telemetry": {
                 "enabled": false,
                 "target": "gcp"
@@ -142,6 +140,9 @@ jobs:
             - Only use labels that already exist in the repository
             - Assign all applicable labels based on the issue content
             - Reference all shell variables as "${VAR}" (with quotes and braces)
+            - Do NOT run any shell or external commands; use only the provided environment variables
+            - Do NOT attempt to execute `gh label list` or call the GitHub API to fetch labels. The full list of labels is provided in "${AVAILABLE_LABELS}".
+            - Do NOT attempt to list or fetch issues yourself. The issues to triage are provided in "${ISSUES_TO_TRIAGE}".
             - Output only valid JSON format
             - Do not include any explanation or additional text, just the JSON
 
@@ -156,14 +157,37 @@ jobs:
         with:
           github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           script: |-
-            // Strip code block markers if present
-            const rawLabels = process.env.LABELS_OUTPUT;
+            // Hardened JSON extraction to tolerate extra text
+            const rawLabels = process.env.LABELS_OUTPUT || '';
             core.info(`Raw labels JSON: ${rawLabels}`);
+
             let parsedLabels;
             try {
-              const trimmedLabels = rawLabels.replace(/^\```(?:json)?\s*/, '').replace(/\s*\```$/, '').trim();
-              parsedLabels = JSON.parse(trimmedLabels);
-              core.info(`Parsed labels JSON: ${JSON.stringify(parsedLabels)}`);
+              let jsonString = rawLabels;
+
+              // 1) Extract from \```json ... \```
+              const jsonBlock = jsonString.match(/\```json\s*([\s\S]*?)\s*\```/);
+              if (jsonBlock) {
+                jsonString = jsonBlock[1].trim();
+              } else {
+                // 2) Extract from \``` ... \```
+                const codeBlock = jsonString.match(/\```\s*([\s\S]*?)\s*\```/);
+                if (codeBlock) {
+                  jsonString = codeBlock[1].trim();
+                } else {
+                  // 3) Extract array substring [ ... ]
+                  const arrayMatch = jsonString.match(/(\[[\s\S]*\])/);
+                  if (arrayMatch) {
+                    jsonString = arrayMatch[1].trim();
+                  }
+                }
+              }
+
+              parsedLabels = JSON.parse(jsonString);
+              if (!Array.isArray(parsedLabels)) {
+                throw new Error('Expected a JSON array for multiple issues');
+              }
+              core.info(`Parsed labels JSON entries: ${parsedLabels.length}`);
             } catch (err) {
               core.setFailed(`Failed to parse labels JSON from Gemini output: ${err.message}\nRaw output: ${rawLabels}`);
               return;
```
