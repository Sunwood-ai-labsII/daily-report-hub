# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index 12875fe..bf0bf84 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -137,26 +137,44 @@ jobs:
               }
             }
           prompt: |-
-            You are an issue triage assistant. Analyze the GitHub issue and suggest appropriate labels.
+            You are an expert GitHub issue triage assistant. Your task is to analyze the provided issue and suggest appropriate labels.
 
+            **ISSUE DETAILS:**
             Repository: ${REPOSITORY}
             Issue Number: ${ISSUE_NUMBER}
-            Issue Title: "${ISSUE_TITLE}"
-            Issue Body: "${ISSUE_BODY}"
-            Available Labels: ${AVAILABLE_LABELS}
+            Title: "${ISSUE_TITLE}"
+            Body: "${ISSUE_BODY}"
 
-            Please analyze this issue carefully and suggest appropriate labels from the available labels list.
+            **AVAILABLE LABELS:**
+            ${AVAILABLE_LABELS}
+
+            **INSTRUCTIONS:**
+            1. Carefully analyze the issue title and body content
+            2. Select appropriate labels from the available labels list
+            3. If no existing labels are suitable, suggest new labels that would be helpful
+            4. Provide a brief explanation for your label choices
+
+            **CRITICAL: You must respond with ONLY a valid JSON object in this exact format:**
             
-            Important: Respond with ONLY the JSON object, no additional text or explanations before or after.
+            {
+              "labels_to_set": ["label1", "label2"],
+              "explanation": "Brief explanation of why these labels were chosen"
+            }
 
-            Constraints:
-            - Do NOT run any shell or external commands; use only the provided environment variables
-            - Do NOT attempt to execute `gh label list` or call the GitHub API to fetch labels. The available labels are already provided in "${AVAILABLE_LABELS}".
+            **RULES:**
+            - Response must be valid JSON only
+            - No additional text before or after the JSON
+            - No markdown code blocks
+            - No explanatory text outside the JSON
+            - If unsure, choose the most general applicable labels
+            - If no labels apply, use empty array: []
 
-            Output format (JSON only):
-            {"labels_to_set": ["label1", "label2"], "explanation": "reasoning for these labels"}
+            **EXAMPLES:**
+            Bug report: {"labels_to_set": ["bug"], "explanation": "Issue reports unexpected behavior"}
+            Feature request: {"labels_to_set": ["enhancement"], "explanation": "User requesting new functionality"}
+            Documentation: {"labels_to_set": ["documentation"], "explanation": "Related to documentation updates"}
 
-            If the issue content appears to be empty or placeholder text, still try to categorize it based on any available information.
+            Analyze the issue now and respond with the JSON:
 
       - name: 'Apply Labels to Issue'
         if: |-
@@ -175,67 +193,93 @@ jobs:
             
             let parsedLabels;
             try {
-              // 改良されたJSON抽出ロジック
-              let jsonString = rawLabels;
+              // 改良されたJSON抽出および検証ロジック
+              let jsonString = rawLabels.trim();
               
-              // 1. \```json \``` ブロックを抽出
-              const jsonBlockMatch = jsonString.match(/\```json\s*([\s\S]*?)\s*\```/);
-              if (jsonBlockMatch) {
-                jsonString = jsonBlockMatch[1].trim();
-                core.info(`Extracted JSON from json code block: ${jsonString}`);
+              // まず、生の出力がJSONかどうかをチェック
+              if (!jsonString.startsWith('{') && !jsonString.startsWith('[')) {
+                // JSONではない場合、フォールバック処理
+                core.warning(`Output is not JSON format: ${jsonString}`);
+                
+                // 基本的なフォールバック: 空のラベル配列を返す
+                parsedLabels = {
+                  labels_to_set: [],
+                  explanation: `Failed to parse Gemini output: ${jsonString.substring(0, 100)}...`
+                };
               } else {
-                // 2. \``` \``` ブロックを抽出（json指定なし）
-                const codeBlockMatch = jsonString.match(/\```\s*([\s\S]*?)\s*\```/);
-                if (codeBlockMatch) {
-                  jsonString = codeBlockMatch[1].trim();
-                  core.info(`Extracted JSON from code block: ${jsonString}`);
+                // 1. \```json \``` ブロックを抽出
+                const jsonBlockMatch = jsonString.match(/\```json\s*([\s\S]*?)\s*\```/);
+                if (jsonBlockMatch) {
+                  jsonString = jsonBlockMatch[1].trim();
+                  core.info(`Extracted JSON from json code block: ${jsonString}`);
                 } else {
-                  // 3. { で始まって } で終わる部分を抽出
-                  const jsonObjectMatch = jsonString.match(/(\{[\s\S]*\})/);
-                  if (jsonObjectMatch) {
-                    jsonString = jsonObjectMatch[1].trim();
-                    core.info(`Extracted JSON object: ${jsonString}`);
+                  // 2. \``` \``` ブロックを抽出（json指定なし）
+                  const codeBlockMatch = jsonString.match(/\```\s*([\s\S]*?)\s*\```/);
+                  if (codeBlockMatch) {
+                    jsonString = codeBlockMatch[1].trim();
+                    core.info(`Extracted JSON from code block: ${jsonString}`);
                   } else {
-                    // 4. [ で始まって ] で終わる部分を抽出（配列の場合）
-                    const jsonArrayMatch = jsonString.match(/(\[[\s\S]*\])/);
-                    if (jsonArrayMatch) {
-                      // 配列が返された場合は、最初の要素を使用（単一issue用）
-                      const arrayData = JSON.parse(jsonArrayMatch[1].trim());
-                      if (Array.isArray(arrayData) && arrayData.length > 0) {
-                        // 現在のissue番号に一致するものを探す
-                        const currentIssueNumber = parseInt(process.env.ISSUE_NUMBER);
-                        const matchingIssue = arrayData.find(item => item.issue_number === currentIssueNumber);
-                        if (matchingIssue) {
-                          parsedLabels = {
-                            labels_to_set: matchingIssue.labels_to_set,
-                            explanation: matchingIssue.explanation
-                          };
-                        } else {
-                          // 一致するissue番号がない場合は最初の要素を使用
-                          const firstItem = arrayData[0];
-                          parsedLabels = {
-                            labels_to_set: firstItem.labels_to_set,
-                            explanation: firstItem.explanation
-                          };
+                    // 3. { で始まって } で終わる部分を抽出
+                    const jsonObjectMatch = jsonString.match(/(\{[\s\S]*\})/);
+                    if (jsonObjectMatch) {
+                      jsonString = jsonObjectMatch[1].trim();
+                      core.info(`Extracted JSON object: ${jsonString}`);
+                    } else {
+                      // 4. [ で始まって ] で終わる部分を抽出（配列の場合）
+                      const jsonArrayMatch = jsonString.match(/(\[[\s\S]*\])/);
+                      if (jsonArrayMatch) {
+                        // 配列が返された場合は、最初の要素を使用（単一issue用）
+                        const arrayData = JSON.parse(jsonArrayMatch[1].trim());
+                        if (Array.isArray(arrayData) && arrayData.length > 0) {
+                          // 現在のissue番号に一致するものを探す
+                          const currentIssueNumber = parseInt(process.env.ISSUE_NUMBER);
+                          const matchingIssue = arrayData.find(item => item.issue_number === currentIssueNumber);
+                          if (matchingIssue) {
+                            parsedLabels = {
+                              labels_to_set: matchingIssue.labels_to_set,
+                              explanation: matchingIssue.explanation
+                            };
+                          } else {
+                            // 一致するissue番号がない場合は最初の要素を使用
+                            const firstItem = arrayData[0];
+                            parsedLabels = {
+                              labels_to_set: firstItem.labels_to_set,
+                              explanation: firstItem.explanation
+                            };
+                          }
+                          core.info(`Successfully parsed from array: ${JSON.stringify(parsedLabels)}`);
                         }
-                        core.info(`Successfully parsed from array: ${JSON.stringify(parsedLabels)}`);
                       }
-                    } else {
-                      // 5. フォールバック: そのままパース
-                      core.info(`Using fallback - trying to parse as-is`);
                     }
                   }
                 }
-              }
-              
-              // まだparsedLabelsが設定されていない場合、通常のJSONパースを試行
-              if (!parsedLabels) {
-                parsedLabels = JSON.parse(jsonString);
-                core.info(`Successfully parsed labels JSON: ${JSON.stringify(parsedLabels)}`);
+                
+                // まだparsedLabelsが設定されていない場合、通常のJSONパースを試行
+                if (!parsedLabels) {
+                  parsedLabels = JSON.parse(jsonString);
+                  core.info(`Successfully parsed labels JSON: ${JSON.stringify(parsedLabels)}`);
+                }
+                
+                // 結果の検証
+                if (!parsedLabels.labels_to_set) {
+                  parsedLabels.labels_to_set = [];
+                }
+                if (!Array.isArray(parsedLabels.labels_to_set)) {
+                  parsedLabels.labels_to_set = [];
+                }
+                if (!parsedLabels.explanation) {
+                  parsedLabels.explanation = "No explanation provided";
+                }
               }
             } catch (err) {
-              core.setFailed(`Failed to parse labels JSON from Gemini output: ${err.message}\nRaw output: ${rawLabels}`);
-              return;
+              core.warning(`Failed to parse labels JSON from Gemini output: ${err.message}`);
+              core.info(`Raw output: ${rawLabels}`);
+              
+              // フォールバック: 空のラベル配列を使用
+              parsedLabels = {
+                labels_to_set: [],
+                explanation: `Parsing failed: ${err.message}`
+              };
             }
 
             const issueNumber = parseInt(process.env.ISSUE_NUMBER);
```
