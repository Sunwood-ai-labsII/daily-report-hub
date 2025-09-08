# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index bf0bf84..8dda875 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -178,89 +178,86 @@ jobs:
 
       - name: 'Apply Labels to Issue'
         if: |-
-          ${{ steps.gemini_issue_analysis.outputs.summary != '' }}
+          ${{ always() && steps.gemini_issue_analysis.outputs.summary != '' }}
         env:
           REPOSITORY: '${{ github.repository }}'
           ISSUE_NUMBER: '${{ steps.get_issue.outputs.issue_number }}'
           LABELS_OUTPUT: '${{ steps.gemini_issue_analysis.outputs.summary }}'
+          GEMINI_RESPONSE: '${{ steps.gemini_issue_analysis.outputs.gemini_response }}'
         uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
         with:
           github-token: '${{ secrets.GH_PAT || steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           script: |-
-            // Strip code block markers if present and extract JSON
-            const rawLabels = process.env.LABELS_OUTPUT;
-            core.info(`Raw labels output: ${rawLabels}`);
+            // Get output from multiple sources
+            const summaryOutput = process.env.LABELS_OUTPUT || '';
+            const geminiResponse = process.env.GEMINI_RESPONSE || '';
+            
+            console.log(`Summary output: "${summaryOutput}"`);
+            console.log(`Gemini response: "${geminiResponse}"`);
+            
+            // Try to use the best available output
+            const rawLabels = summaryOutput || geminiResponse;
+            
+            if (!rawLabels || rawLabels.trim() === '') {
+              core.warning('No output received from Gemini CLI');
+              return;
+            }
+            
+            core.info(`Processing output: ${rawLabels}`);
             
             let parsedLabels;
             try {
               // 改良されたJSON抽出および検証ロジック
               let jsonString = rawLabels.trim();
               
-              // まず、生の出力がJSONかどうかをチェック
-              if (!jsonString.startsWith('{') && !jsonString.startsWith('[')) {
-                // JSONではない場合、フォールバック処理
-                core.warning(`Output is not JSON format: ${jsonString}`);
+              // Check if output looks like JSON
+              if (!jsonString.includes('{') && !jsonString.includes('[')) {
+                core.warning(`Output does not appear to be JSON: ${jsonString}`);
+                
+                // Try to extract meaningful labels from the text content
+                const titleAndBody = `${process.env.ISSUE_TITLE || ''} ${process.env.ISSUE_BODY || ''}`.toLowerCase();
+                const suggestedLabels = [];
+                
+                if (titleAndBody.includes('bug') || titleAndBody.includes('error') || titleAndBody.includes('問題')) {
+                  suggestedLabels.push('bug');
+                }
+                if (titleAndBody.includes('feature') || titleAndBody.includes('enhancement') || titleAndBody.includes('機能')) {
+                  suggestedLabels.push('enhancement');
+                }
+                if (titleAndBody.includes('doc') || titleAndBody.includes('documentation') || titleAndBody.includes('ドキュメント')) {
+                  suggestedLabels.push('documentation');
+                }
+                if (titleAndBody.includes('example') || titleAndBody.includes('demo') || titleAndBody.includes('sample') || titleAndBody.includes('サンプル')) {
+                  suggestedLabels.push('example', 'demo');
+                }
+                if (titleAndBody.includes('todo') || titleAndBody.includes('task') || titleAndBody.includes('作成')) {
+                  suggestedLabels.push('kind/task');
+                }
+                if (titleAndBody.includes('app') || titleAndBody.includes('アプリ')) {
+                  suggestedLabels.push('example');
+                }
                 
-                // 基本的なフォールバック: 空のラベル配列を返す
                 parsedLabels = {
-                  labels_to_set: [],
-                  explanation: `Failed to parse Gemini output: ${jsonString.substring(0, 100)}...`
+                  labels_to_set: [...new Set(suggestedLabels)],
+                  explanation: `Auto-detected from content analysis (Gemini output was not JSON): ${jsonString.substring(0, 100)}`
                 };
+                
+                core.info(`Fallback labels selected: ${JSON.stringify(parsedLabels)}`);
               } else {
-                // 1. \```json \``` ブロックを抽出
-                const jsonBlockMatch = jsonString.match(/\```json\s*([\s\S]*?)\s*\```/);
+                // Extract JSON from various formats
+                const jsonBlockMatch = jsonString.match(/\```json\s*([\s\S]*?)\s*\```/) ||
+                                    jsonString.match(/\```\s*([\s\S]*?)\s*\```/) ||
+                                    jsonString.match(/(\{[\s\S]*\})/) ||
+                                    jsonString.match(/(\[[\s\S]*\])/);
+                
                 if (jsonBlockMatch) {
                   jsonString = jsonBlockMatch[1].trim();
-                  core.info(`Extracted JSON from json code block: ${jsonString}`);
-                } else {
-                  // 2. \``` \``` ブロックを抽出（json指定なし）
-                  const codeBlockMatch = jsonString.match(/\```\s*([\s\S]*?)\s*\```/);
-                  if (codeBlockMatch) {
-                    jsonString = codeBlockMatch[1].trim();
-                    core.info(`Extracted JSON from code block: ${jsonString}`);
-                  } else {
-                    // 3. { で始まって } で終わる部分を抽出
-                    const jsonObjectMatch = jsonString.match(/(\{[\s\S]*\})/);
-                    if (jsonObjectMatch) {
-                      jsonString = jsonObjectMatch[1].trim();
-                      core.info(`Extracted JSON object: ${jsonString}`);
-                    } else {
-                      // 4. [ で始まって ] で終わる部分を抽出（配列の場合）
-                      const jsonArrayMatch = jsonString.match(/(\[[\s\S]*\])/);
-                      if (jsonArrayMatch) {
-                        // 配列が返された場合は、最初の要素を使用（単一issue用）
-                        const arrayData = JSON.parse(jsonArrayMatch[1].trim());
-                        if (Array.isArray(arrayData) && arrayData.length > 0) {
-                          // 現在のissue番号に一致するものを探す
-                          const currentIssueNumber = parseInt(process.env.ISSUE_NUMBER);
-                          const matchingIssue = arrayData.find(item => item.issue_number === currentIssueNumber);
-                          if (matchingIssue) {
-                            parsedLabels = {
-                              labels_to_set: matchingIssue.labels_to_set,
-                              explanation: matchingIssue.explanation
-                            };
-                          } else {
-                            // 一致するissue番号がない場合は最初の要素を使用
-                            const firstItem = arrayData[0];
-                            parsedLabels = {
-                              labels_to_set: firstItem.labels_to_set,
-                              explanation: firstItem.explanation
-                            };
-                          }
-                          core.info(`Successfully parsed from array: ${JSON.stringify(parsedLabels)}`);
-                        }
-                      }
-                    }
-                  }
+                  core.info(`Extracted JSON: ${jsonString}`);
                 }
                 
-                // まだparsedLabelsが設定されていない場合、通常のJSONパースを試行
-                if (!parsedLabels) {
-                  parsedLabels = JSON.parse(jsonString);
-                  core.info(`Successfully parsed labels JSON: ${JSON.stringify(parsedLabels)}`);
-                }
+                parsedLabels = JSON.parse(jsonString);
                 
-                // 結果の検証
+                // Validate structure
                 if (!parsedLabels.labels_to_set) {
                   parsedLabels.labels_to_set = [];
                 }
@@ -270,21 +267,32 @@ jobs:
                 if (!parsedLabels.explanation) {
                   parsedLabels.explanation = "No explanation provided";
                 }
+                
+                core.info(`Successfully parsed JSON: ${JSON.stringify(parsedLabels)}`);
               }
             } catch (err) {
-              core.warning(`Failed to parse labels JSON from Gemini output: ${err.message}`);
-              core.info(`Raw output: ${rawLabels}`);
+              core.warning(`JSON parsing failed: ${err.message}`);
+              
+              // Final fallback based on issue content
+              const titleAndBody = `${process.env.ISSUE_TITLE || ''} ${process.env.ISSUE_BODY || ''}`.toLowerCase();
+              const fallbackLabels = [];
+              
+              if (titleAndBody.includes('example') || titleAndBody.includes('demo') || titleAndBody.includes('sample') || titleAndBody.includes('サンプル')) {
+                fallbackLabels.push('example', 'demo');
+              }
+              if (titleAndBody.includes('todo') || titleAndBody.includes('task') || titleAndBody.includes('作成')) {
+                fallbackLabels.push('kind/task');
+              }
               
-              // フォールバック: 空のラベル配列を使用
               parsedLabels = {
-                labels_to_set: [],
-                explanation: `Parsing failed: ${err.message}`
+                labels_to_set: [...new Set(fallbackLabels)],
+                explanation: `Content-based fallback labeling due to parsing error: ${err.message}`
               };
             }
 
             const issueNumber = parseInt(process.env.ISSUE_NUMBER);
-
-            // Track available labels and allow auto-create of missing labels using GH_PAT
+            
+            // Get available labels
             const available = new Set(
               (process.env.AVAILABLE_LABELS || '')
                 .split(',')
@@ -292,11 +300,11 @@ jobs:
                 .filter(Boolean)
             );
 
-            // Set labels based on triage result
+            // Process labels
             if (parsedLabels.labels_to_set && parsedLabels.labels_to_set.length > 0) {
               const proposed = [...new Set(parsedLabels.labels_to_set.map(s => String(s).trim()).filter(Boolean))];
 
-              // Attempt to create any missing labels using the provided token
+              // Create missing labels if needed
               for (const label of proposed) {
                 if (available.has(label)) continue;
                 try {
@@ -310,10 +318,9 @@ jobs:
                   core.info(`Created missing label: ${label}`);
                   available.add(label);
                 } catch (err) {
-                  // Ignore if already exists (422), otherwise log error and continue
                   const status = err?.status || err?.response?.status;
                   if (status === 422) {
-                    core.info(`Label already exists (race): ${label}`);
+                    core.info(`Label already exists: ${label}`);
                     available.add(label);
                   } else {
                     core.error(`Failed to create label '${label}': ${err}`);
@@ -321,10 +328,10 @@ jobs:
                 }
               }
 
+              // Apply labels
               const finalLabels = proposed.filter(l => available.has(l));
               if (finalLabels.length === 0) {
-                const explanation = parsedLabels.explanation ? ` - ${parsedLabels.explanation}` : '';
-                core.info(`No applicable labels for #${issueNumber} after creation attempts. Skipping.${explanation}`);
+                core.info(`No applicable labels for #${issueNumber}. ${parsedLabels.explanation}`);
               } else {
                 await github.rest.issues.addLabels({
                   owner: context.repo.owner,
@@ -332,13 +339,10 @@ jobs:
                   issue_number: issueNumber,
                   labels: finalLabels
                 });
-                const explanation = parsedLabels.explanation ? ` - ${parsedLabels.explanation}` : '';
-                core.info(`Applied labels for #${issueNumber}: ${finalLabels.join(', ')}${explanation}`);
+                core.info(`Applied labels for #${issueNumber}: ${finalLabels.join(', ')} - ${parsedLabels.explanation}`);
               }
             } else {
-              // If no labels to set, leave the issue as is
-              const explanation = parsedLabels.explanation ? ` - ${parsedLabels.explanation}` : '';
-              core.info(`No labels to set for #${issueNumber}, leaving as is${explanation}`);
+              core.info(`No labels to set for #${issueNumber}. ${parsedLabels.explanation}`);
             }
 
       - name: 'Post Issue Analysis Failure Comment'
```
