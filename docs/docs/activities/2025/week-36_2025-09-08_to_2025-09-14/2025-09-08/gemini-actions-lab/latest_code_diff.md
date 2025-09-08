# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index 8dda875..32a71f6 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -2,9 +2,7 @@ name: '🏷️ Gemini Automated Issue Triage'
 
 on:
   issues:
-    types:
-      - 'opened'
-      - 'reopened'
+    types: [opened, reopened]
   workflow_dispatch:
     inputs:
       issue_number:
@@ -12,352 +10,98 @@ on:
         required: true
         type: 'number'
 
-concurrency:
-  group: '${{ github.workflow }}-${{ github.event.issue.number || github.event.inputs.issue_number }}'
-  cancel-in-progress: true
-
-defaults:
-  run:
-    shell: 'bash'
-
 permissions:
-  contents: 'read'
-  id-token: 'write'
-  issues: 'write'
-  statuses: 'write'
+  contents: read
+  issues: write
+  id-token: write
 
 jobs:
-  triage-issue:
-    if: |-
-      github.event_name == 'issues' ||
-      github.event_name == 'workflow_dispatch' ||
-      (
-        github.event_name == 'issue_comment' &&
-        contains(github.event.comment.body, '@gemini-cli /triage') &&
-        contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association)
-      )
-    timeout-minutes: 5
-    runs-on: 'ubuntu-latest'
+  triage:
+    runs-on: ubuntu-latest
     steps:
-      - name: 'Checkout repository'
-        uses: 'actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683' # ratchet:actions/checkout@v4
-
-      - name: 'Generate GitHub App Token'
-        id: 'generate_token'
-        if: |-
-          ${{ vars.APP_ID }}
-        uses: 'actions/create-github-app-token@df432ceedc7162793a195dd1713ff69aefc7379e' # ratchet:actions/create-github-app-token@v2
-        with:
-          app-id: '${{ vars.APP_ID }}'
-          private-key: '${{ secrets.APP_PRIVATE_KEY }}'
-
-      - name: 'Get Issue Information'
-        id: 'get_issue'
-        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+      - name: 'Get Issue Info'
+        id: issue
+        uses: actions/github-script@v7
         with:
-          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           script: |
-            let issueNumber, issueTitle, issueBody;
-            
+            let issue;
             if (context.eventName === 'workflow_dispatch') {
-              // 手動実行の場合はinputから取得
-              issueNumber = parseInt('${{ github.event.inputs.issue_number }}');
-              console.log(`Manual dispatch for issue #${issueNumber}`);
-              
-              // APIでissue情報を取得
-              const { data: issue } = await github.rest.issues.get({
+              const { data } = await github.rest.issues.get({
                 owner: context.repo.owner,
                 repo: context.repo.repo,
-                issue_number: issueNumber
+                issue_number: ${{ github.event.inputs.issue_number }}
               });
-              
-              issueTitle = issue.title;
-              issueBody = issue.body || '';
+              issue = data;
             } else {
-              // 通常のイベントの場合
-              issueNumber = context.payload.issue.number;
-              issueTitle = context.payload.issue.title;
-              issueBody = context.payload.issue.body || '';
+              issue = context.payload.issue;
             }
             
-            console.log(`Event name: ${context.eventName}`);
-            console.log(`Issue number: ${issueNumber}`);
-            console.log(`Issue title: '${issueTitle}'`);
-            console.log(`Issue body length: ${issueBody.length}`);
-            console.log(`Issue body preview: '${issueBody.substring(0, 200)}${issueBody.length > 200 ? '...' : ''}'`);
-            
-            // 後続のステップで使用するために出力
-            core.setOutput('issue_number', issueNumber);
-            core.setOutput('issue_title', issueTitle);
-            core.setOutput('issue_body', issueBody);
+            core.setOutput('number', issue.number);
+            core.setOutput('title', issue.title);
+            core.setOutput('body', issue.body || '');
 
-      - name: 'Get Repository Labels'
-        id: 'get_labels'
-        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+      - name: 'Get Labels'
+        id: labels
+        uses: actions/github-script@v7
         with:
-          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          script: |-
+          script: |
             const labels = await github.paginate(github.rest.issues.listLabelsForRepo, {
               owner: context.repo.owner,
-              repo: context.repo.repo,
-              per_page: 100,
+              repo: context.repo.repo
             });
-            const labelNames = labels.map(label => label.name).filter(Boolean);
-            core.setOutput('available_labels', labelNames.join(','));
-            core.info(`Found ${labelNames.length} labels: ${labelNames.join(', ')}`);
+            const labelNames = labels.map(l => l.name).join(', ');
+            core.setOutput('available', labelNames);
             return labelNames;
 
-      - name: 'Run Gemini Issue Analysis'
-        uses: 'google-github-actions/run-gemini-cli@v0'
-        id: 'gemini_issue_analysis'
-        env:
-          GITHUB_TOKEN: '' # Do not pass any auth token here since this runs on untrusted inputs
-          ISSUE_TITLE: '${{ steps.get_issue.outputs.issue_title }}'
-          ISSUE_BODY: '${{ steps.get_issue.outputs.issue_body }}'
-          ISSUE_NUMBER: '${{ steps.get_issue.outputs.issue_number }}'
-          REPOSITORY: '${{ github.repository }}'
-          AVAILABLE_LABELS: '${{ steps.get_labels.outputs.available_labels }}'
+      - name: 'Analyze with Gemini'
+        uses: google-github-actions/run-gemini-cli@v0
+        id: gemini
         with:
-          gemini_cli_version: '${{ vars.GEMINI_CLI_VERSION }}'
-          gcp_workload_identity_provider: '${{ vars.GCP_WIF_PROVIDER }}'
-          gcp_project_id: '${{ vars.GOOGLE_CLOUD_PROJECT }}'
-          gcp_location: '${{ vars.GOOGLE_CLOUD_LOCATION }}'
-          gcp_service_account: '${{ vars.SERVICE_ACCOUNT_EMAIL }}'
-          gemini_api_key: '${{ secrets.GEMINI_API_KEY }}'
-          use_vertex_ai: '${{ vars.GOOGLE_GENAI_USE_VERTEXAI }}'
-          use_gemini_code_assist: '${{ vars.GOOGLE_GENAI_USE_GCA }}'
-          settings: |-
-            {
-              "debug": true,
-              "maxSessionTurns": 25,
-              "coreTools": [],
-              "telemetry": {
-                "enabled": false,
-                "target": "gcp"
-              }
-            }
-          prompt: |-
-            You are an expert GitHub issue triage assistant. Your task is to analyze the provided issue and suggest appropriate labels.
-
-            **ISSUE DETAILS:**
-            Repository: ${REPOSITORY}
-            Issue Number: ${ISSUE_NUMBER}
-            Title: "${ISSUE_TITLE}"
-            Body: "${ISSUE_BODY}"
-
-            **AVAILABLE LABELS:**
-            ${AVAILABLE_LABELS}
-
-            **INSTRUCTIONS:**
-            1. Carefully analyze the issue title and body content
-            2. Select appropriate labels from the available labels list
-            3. If no existing labels are suitable, suggest new labels that would be helpful
-            4. Provide a brief explanation for your label choices
-
-            **CRITICAL: You must respond with ONLY a valid JSON object in this exact format:**
+          gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
+          prompt: |
+            Issue Title: ${{ steps.issue.outputs.title }}
+            Issue Body: ${{ steps.issue.outputs.body }}
+            Available Labels: ${{ steps.labels.outputs.available }}
             
-            {
-              "labels_to_set": ["label1", "label2"],
-              "explanation": "Brief explanation of why these labels were chosen"
-            }
-
-            **RULES:**
-            - Response must be valid JSON only
-            - No additional text before or after the JSON
-            - No markdown code blocks
-            - No explanatory text outside the JSON
-            - If unsure, choose the most general applicable labels
-            - If no labels apply, use empty array: []
-
-            **EXAMPLES:**
-            Bug report: {"labels_to_set": ["bug"], "explanation": "Issue reports unexpected behavior"}
-            Feature request: {"labels_to_set": ["enhancement"], "explanation": "User requesting new functionality"}
-            Documentation: {"labels_to_set": ["documentation"], "explanation": "Related to documentation updates"}
-
-            Analyze the issue now and respond with the JSON:
-
-      - name: 'Apply Labels to Issue'
-        if: |-
-          ${{ always() && steps.gemini_issue_analysis.outputs.summary != '' }}
-        env:
-          REPOSITORY: '${{ github.repository }}'
-          ISSUE_NUMBER: '${{ steps.get_issue.outputs.issue_number }}'
-          LABELS_OUTPUT: '${{ steps.gemini_issue_analysis.outputs.summary }}'
-          GEMINI_RESPONSE: '${{ steps.gemini_issue_analysis.outputs.gemini_response }}'
-        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+            Select appropriate labels for this GitHub issue. Use this XML format:
+            <labels>
+            <label>example</label>
+            <label>kind/task</label>
+            </labels>
+
+      - name: 'Apply Labels'
+        uses: actions/github-script@v7
         with:
-          github-token: '${{ secrets.GH_PAT || steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          script: |-
-            // Get output from multiple sources
-            const summaryOutput = process.env.LABELS_OUTPUT || '';
-            const geminiResponse = process.env.GEMINI_RESPONSE || '';
-            
-            console.log(`Summary output: "${summaryOutput}"`);
-            console.log(`Gemini response: "${geminiResponse}"`);
+          script: |
+            const output = `${{ steps.gemini.outputs.summary }}`;
+            console.log('Gemini output:', output);
             
-            // Try to use the best available output
-            const rawLabels = summaryOutput || geminiResponse;
+            let labels = [];
             
-            if (!rawLabels || rawLabels.trim() === '') {
-              core.warning('No output received from Gemini CLI');
-              return;
+            // XMLタグから正規表現でラベルを抽出
+            const labelMatches = output.match(/<label>(.*?)<\/label>/g);
+            if (labelMatches) {
+              labels = labelMatches.map(match => 
+                match.replace(/<\/?label>/g, '').trim()
+              ).filter(label => label.length > 0);
+              console.log('Extracted labels from XML:', labels);
+            } else {
+              console.log('No XML labels found, using fallback');
             }
             
-            core.info(`Processing output: ${rawLabels}`);
-            
-            let parsedLabels;
-            try {
-              // 改良されたJSON抽出および検証ロジック
-              let jsonString = rawLabels.trim();
-              
-              // Check if output looks like JSON
-              if (!jsonString.includes('{') && !jsonString.includes('[')) {
-                core.warning(`Output does not appear to be JSON: ${jsonString}`);
-                
-                // Try to extract meaningful labels from the text content
-                const titleAndBody = `${process.env.ISSUE_TITLE || ''} ${process.env.ISSUE_BODY || ''}`.toLowerCase();
-                const suggestedLabels = [];
-                
-                if (titleAndBody.includes('bug') || titleAndBody.includes('error') || titleAndBody.includes('問題')) {
-                  suggestedLabels.push('bug');
-                }
-                if (titleAndBody.includes('feature') || titleAndBody.includes('enhancement') || titleAndBody.includes('機能')) {
-                  suggestedLabels.push('enhancement');
-                }
-                if (titleAndBody.includes('doc') || titleAndBody.includes('documentation') || titleAndBody.includes('ドキュメント')) {
-                  suggestedLabels.push('documentation');
-                }
-                if (titleAndBody.includes('example') || titleAndBody.includes('demo') || titleAndBody.includes('sample') || titleAndBody.includes('サンプル')) {
-                  suggestedLabels.push('example', 'demo');
-                }
-                if (titleAndBody.includes('todo') || titleAndBody.includes('task') || titleAndBody.includes('作成')) {
-                  suggestedLabels.push('kind/task');
-                }
-                if (titleAndBody.includes('app') || titleAndBody.includes('アプリ')) {
-                  suggestedLabels.push('example');
-                }
-                
-                parsedLabels = {
-                  labels_to_set: [...new Set(suggestedLabels)],
-                  explanation: `Auto-detected from content analysis (Gemini output was not JSON): ${jsonString.substring(0, 100)}`
-                };
-                
-                core.info(`Fallback labels selected: ${JSON.stringify(parsedLabels)}`);
-              } else {
-                // Extract JSON from various formats
-                const jsonBlockMatch = jsonString.match(/\```json\s*([\s\S]*?)\s*\```/) ||
-                                    jsonString.match(/\```\s*([\s\S]*?)\s*\```/) ||
-                                    jsonString.match(/(\{[\s\S]*\})/) ||
-                                    jsonString.match(/(\[[\s\S]*\])/);
-                
-                if (jsonBlockMatch) {
-                  jsonString = jsonBlockMatch[1].trim();
-                  core.info(`Extracted JSON: ${jsonString}`);
-                }
-                
-                parsedLabels = JSON.parse(jsonString);
-                
-                // Validate structure
-                if (!parsedLabels.labels_to_set) {
-                  parsedLabels.labels_to_set = [];
-                }
-                if (!Array.isArray(parsedLabels.labels_to_set)) {
-                  parsedLabels.labels_to_set = [];
-                }
-                if (!parsedLabels.explanation) {
-                  parsedLabels.explanation = "No explanation provided";
-                }
-                
-                core.info(`Successfully parsed JSON: ${JSON.stringify(parsedLabels)}`);
-              }
-            } catch (err) {
-              core.warning(`JSON parsing failed: ${err.message}`);
-              
-              // Final fallback based on issue content
-              const titleAndBody = `${process.env.ISSUE_TITLE || ''} ${process.env.ISSUE_BODY || ''}`.toLowerCase();
-              const fallbackLabels = [];
-              
-              if (titleAndBody.includes('example') || titleAndBody.includes('demo') || titleAndBody.includes('sample') || titleAndBody.includes('サンプル')) {
-                fallbackLabels.push('example', 'demo');
-              }
-              if (titleAndBody.includes('todo') || titleAndBody.includes('task') || titleAndBody.includes('作成')) {
-                fallbackLabels.push('kind/task');
-              }
-              
-              parsedLabels = {
-                labels_to_set: [...new Set(fallbackLabels)],
-                explanation: `Content-based fallback labeling due to parsing error: ${err.message}`
-              };
+            // フォールバック: needs-triage のみ
+            if (labels.length === 0) {
+              console.log('No labels extracted, applying needs-triage');
+              labels = ['needs-triage'];
             }
-
-            const issueNumber = parseInt(process.env.ISSUE_NUMBER);
             
-            // Get available labels
-            const available = new Set(
-              (process.env.AVAILABLE_LABELS || '')
-                .split(',')
-                .map(s => s.trim())
-                .filter(Boolean)
-            );
-
-            // Process labels
-            if (parsedLabels.labels_to_set && parsedLabels.labels_to_set.length > 0) {
-              const proposed = [...new Set(parsedLabels.labels_to_set.map(s => String(s).trim()).filter(Boolean))];
-
-              // Create missing labels if needed
-              for (const label of proposed) {
-                if (available.has(label)) continue;
-                try {
-                  await github.rest.issues.createLabel({
-                    owner: context.repo.owner,
-                    repo: context.repo.repo,
-                    name: label,
-                    color: 'ededed',
-                    description: 'Auto-created by Gemini triage'
-                  });
-                  core.info(`Created missing label: ${label}`);
-                  available.add(label);
-                } catch (err) {
-                  const status = err?.status || err?.response?.status;
-                  if (status === 422) {
-                    core.info(`Label already exists: ${label}`);
-                    available.add(label);
-                  } else {
-                    core.error(`Failed to create label '${label}': ${err}`);
-                  }
-                }
-              }
-
-              // Apply labels
-              const finalLabels = proposed.filter(l => available.has(l));
-              if (finalLabels.length === 0) {
-                core.info(`No applicable labels for #${issueNumber}. ${parsedLabels.explanation}`);
-              } else {
-                await github.rest.issues.addLabels({
-                  owner: context.repo.owner,
-                  repo: context.repo.repo,
-                  issue_number: issueNumber,
-                  labels: finalLabels
-                });
-                core.info(`Applied labels for #${issueNumber}: ${finalLabels.join(', ')} - ${parsedLabels.explanation}`);
-              }
-            } else {
-              core.info(`No labels to set for #${issueNumber}. ${parsedLabels.explanation}`);
+            // ラベル適用
+            if (labels.length > 0) {
+              await github.rest.issues.addLabels({
+                owner: context.repo.owner,
+                repo: context.repo.repo,
+                issue_number: ${{ steps.issue.outputs.number }},
+                labels: labels
+              });
+              console.log(`Applied labels: ${labels.join(', ')}`);
             }
-
-      - name: 'Post Issue Analysis Failure Comment'
-        if: |-
-          ${{ failure() && steps.gemini_issue_analysis.outcome == 'failure' }}
-        env:
-          ISSUE_NUMBER: '${{ steps.get_issue.outputs.issue_number }}'
-          RUN_URL: '${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}'
-        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
-        with:
-          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          script: |-
-            github.rest.issues.createComment({
-              owner: context.repo.owner,
-              repo: context.repo.repo,
-              issue_number: parseInt(process.env.ISSUE_NUMBER),
-              body: `There is a problem with the Gemini CLI issue triaging. Please check the [action logs](${process.env.RUN_URL}) for details.`
-            })
```
