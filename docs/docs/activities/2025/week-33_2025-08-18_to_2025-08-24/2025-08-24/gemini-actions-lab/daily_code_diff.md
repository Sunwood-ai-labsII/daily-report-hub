# 💻 Daily Code Changes

## Full Diff

```diff
commit 97af745b98f140a8756650f1f2287c4089875325
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sun Aug 24 12:01:07 2025 +0900

    Update gemini-issue-automated-triage.yml

diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index 375bc0e..49d20e3 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -101,35 +101,21 @@ jobs:
               }
             }
           prompt: |-
-            ## Role
-
-            You are an issue triage assistant. Analyze the current GitHub issue
-            and identify the most appropriate existing labels. Use the available
-            tools to gather information; do not ask for information to be
-            provided.
-
-            ## Steps
-
-            1. Review the available labels in the environment variable: "${AVAILABLE_LABELS}".
-            2. Review the issue title and body provided in the environment
-               variables: "${ISSUE_TITLE}" and "${ISSUE_BODY}".
-            3. Classify the issue by the appropriate labels from the available labels.
-            4. Output the appropriate labels for this issue in JSON format with explanation, for example:
-               \```
-               {"labels_to_set": ["kind/bug", "priority/p0"], "explanation": "This is a critical bug report affecting main functionality"}
-               \```
-            5. If the issue cannot be classified using the available labels, output:
-               \```
-               {"labels_to_set": [], "explanation": "Unable to classify this issue with available labels"}
-               \```
-
-            ## Guidelines
-
-            - Only use labels that already exist in the repository
-            - Assign all applicable labels based on the issue content
-            - Reference all shell variables as "${VAR}" (with quotes and braces)
-            - Output only valid JSON format
-            - Do not include any explanation or additional text, just the JSON
+            You are an issue triage assistant. Analyze the GitHub issue and output ONLY valid JSON.
+
+            Available labels: ${AVAILABLE_LABELS}
+            Issue title: ${ISSUE_TITLE}
+            Issue body: ${ISSUE_BODY}
+
+            IMPORTANT: Output ONLY the JSON response, no explanations or additional text.
+
+            Required JSON format:
+            {"labels_to_set": ["label1", "label2"], "explanation": "brief explanation"}
+
+            If no appropriate labels exist, output:
+            {"labels_to_set": [], "explanation": "No suitable labels found"}
+
+            JSON response:
 
       - name: 'Apply Labels to Issue'
         if: |-
@@ -142,14 +128,36 @@ jobs:
         with:
           github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           script: |-
-            // Strip code block markers if present
+            // Strip code block markers if present and extract JSON
             const rawLabels = process.env.LABELS_OUTPUT;
-            core.info(`Raw labels JSON: ${rawLabels}`);
+            core.info(`Raw labels output: ${rawLabels}`);
+            
             let parsedLabels;
             try {
-              const trimmedLabels = rawLabels.replace(/^\```(?:json)?\s*/, '').replace(/\s*\```$/, '').trim();
-              parsedLabels = JSON.parse(trimmedLabels);
-              core.info(`Parsed labels JSON: ${JSON.stringify(parsedLabels)}`);
+              // JSONブロックを抽出するための正規表現
+              const jsonMatch = rawLabels.match(/\```json\s*([\s\S]*?)\s*\```/);
+              
+              let jsonString;
+              if (jsonMatch) {
+                // \```json \``` ブロックが見つかった場合
+                jsonString = jsonMatch[1].trim();
+                core.info(`Extracted JSON from code block: ${jsonString}`);
+              } else {
+                // JSONブロックがない場合、{ で始まる最初の行を探す
+                const lines = rawLabels.split('\n');
+                const jsonLine = lines.find(line => line.trim().startsWith('{'));
+                if (jsonLine) {
+                  jsonString = jsonLine.trim();
+                  core.info(`Extracted JSON from line: ${jsonString}`);
+                } else {
+                  // フォールバック: 元の方法
+                  jsonString = rawLabels.replace(/^\```(?:json)?\s*/, '').replace(/\s*\```$/, '').trim();
+                  core.info(`Using fallback extraction: ${jsonString}`);
+                }
+              }
+              
+              parsedLabels = JSON.parse(jsonString);
+              core.info(`Successfully parsed labels JSON: ${JSON.stringify(parsedLabels)}`);
             } catch (err) {
               core.setFailed(`Failed to parse labels JSON from Gemini output: ${err.message}\nRaw output: ${rawLabels}`);
               return;
@@ -187,5 +195,5 @@ jobs:
               owner: context.repo.owner,
               repo: context.repo.repo,
               issue_number: parseInt(process.env.ISSUE_NUMBER),
-              body: 'There is a problem with the Gemini CLI issue triaging. Please check the [action logs](${process.env.RUN_URL}) for details.'
+              body: `There is a problem with the Gemini CLI issue triaging. Please check the [action logs](${process.env.RUN_URL}) for details.`
             })
```
