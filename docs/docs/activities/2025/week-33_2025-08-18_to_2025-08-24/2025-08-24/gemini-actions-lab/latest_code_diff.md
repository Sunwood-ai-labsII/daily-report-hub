# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index baae78b..12e2f11 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -118,6 +118,8 @@ jobs:
             Available Labels: ${AVAILABLE_LABELS}
 
             Please analyze this issue carefully and suggest appropriate labels from the available labels list.
+            
+            Important: Respond with ONLY the JSON object, no additional text or explanations before or after.
 
             Output format (JSON only):
             {"labels_to_set": ["label1", "label2"], "explanation": "reasoning for these labels"}
@@ -141,30 +143,64 @@ jobs:
             
             let parsedLabels;
             try {
-              // JSONブロックを抽出するための正規表現
-              const jsonMatch = rawLabels.match(/\```json\s*([\s\S]*?)\s*\```/);
+              // 改良されたJSON抽出ロジック
+              let jsonString = rawLabels;
               
-              let jsonString;
-              if (jsonMatch) {
-                // \```json \``` ブロックが見つかった場合
-                jsonString = jsonMatch[1].trim();
-                core.info(`Extracted JSON from code block: ${jsonString}`);
+              // 1. \```json \``` ブロックを抽出
+              const jsonBlockMatch = jsonString.match(/\```json\s*([\s\S]*?)\s*\```/);
+              if (jsonBlockMatch) {
+                jsonString = jsonBlockMatch[1].trim();
+                core.info(`Extracted JSON from json code block: ${jsonString}`);
               } else {
-                // JSONブロックがない場合、{ で始まる最初の行を探す
-                const lines = rawLabels.split('\n');
-                const jsonLine = lines.find(line => line.trim().startsWith('{'));
-                if (jsonLine) {
-                  jsonString = jsonLine.trim();
-                  core.info(`Extracted JSON from line: ${jsonString}`);
+                // 2. \``` \``` ブロックを抽出（json指定なし）
+                const codeBlockMatch = jsonString.match(/\```\s*([\s\S]*?)\s*\```/);
+                if (codeBlockMatch) {
+                  jsonString = codeBlockMatch[1].trim();
+                  core.info(`Extracted JSON from code block: ${jsonString}`);
                 } else {
-                  // フォールバック: 元の方法
-                  jsonString = rawLabels.replace(/^\```(?:json)?\s*/, '').replace(/\s*\```$/, '').trim();
-                  core.info(`Using fallback extraction: ${jsonString}`);
+                  // 3. { で始まって } で終わる部分を抽出
+                  const jsonObjectMatch = jsonString.match(/(\{[\s\S]*\})/);
+                  if (jsonObjectMatch) {
+                    jsonString = jsonObjectMatch[1].trim();
+                    core.info(`Extracted JSON object: ${jsonString}`);
+                  } else {
+                    // 4. [ で始まって ] で終わる部分を抽出（配列の場合）
+                    const jsonArrayMatch = jsonString.match /(\[[\s\S]*\])/);
+                    if (jsonArrayMatch) {
+                      // 配列が返された場合は、最初の要素を使用（単一issue用）
+                      const arrayData = JSON.parse(jsonArrayMatch[1].trim());
+                      if (Array.isArray(arrayData) && arrayData.length > 0) {
+                        // 現在のissue番号に一致するものを探す
+                        const currentIssueNumber = parseInt(process.env.ISSUE_NUMBER);
+                        const matchingIssue = arrayData.find(item => item.issue_number === currentIssueNumber);
+                        if (matchingIssue) {
+                          parsedLabels = {
+                            labels_to_set: matchingIssue.labels_to_set,
+                            explanation: matchingIssue.explanation
+                          };
+                        } else {
+                          // 一致するissue番号がない場合は最初の要素を使用
+                          const firstItem = arrayData[0];
+                          parsedLabels = {
+                            labels_to_set: firstItem.labels_to_set,
+                            explanation: firstItem.explanation
+                          };
+                        }
+                        core.info(`Successfully parsed from array: ${JSON.stringify(parsedLabels)}`);
+                      }
+                    } else {
+                      // 5. フォールバック: そのままパース
+                      core.info(`Using fallback - trying to parse as-is`);
+                    }
+                  }
                 }
               }
               
-              parsedLabels = JSON.parse(jsonString);
-              core.info(`Successfully parsed labels JSON: ${JSON.stringify(parsedLabels)}`);
+              // まだparsedLabelsが設定されていない場合、通常のJSONパースを試行
+              if (!parsedLabels) {
+                parsedLabels = JSON.parse(jsonString);
+                core.info(`Successfully parsed labels JSON: ${JSON.stringify(parsedLabels)}`);
+              }
             } catch (err) {
               core.setFailed(`Failed to parse labels JSON from Gemini output: ${err.message}\nRaw output: ${rawLabels}`);
               return;
@@ -202,5 +238,5 @@ jobs:
               owner: context.repo.owner,
               repo: context.repo.repo,
               issue_number: parseInt(process.env.ISSUE_NUMBER),
-              body: `There is a problem with the Gemini CLI issue triaging. Please check the [action logs](${process.env.RUN_URL}) for details.`
+              issue: `There is a problem with the Gemini CLI issue triaging. Please check the [action logs](${process.env.RUN_URL}) for details.`
             })
```
