# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index 861d0d6..a532d09 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -8,7 +8,7 @@ on:
       issue_number:
         description: 'issue number to triage'
         required: true
-        type: 'number'
+        type: number
 
 permissions:
   contents: read
@@ -19,7 +19,7 @@ jobs:
   triage:
     runs-on: ubuntu-latest
     steps:
-      - name: 'Get Issue Info'
+      - name: Get Issue Info
         id: issue
         env:
           INPUT_ISSUE_NUMBER: ${{ github.event.inputs.issue_number }}
@@ -38,12 +38,11 @@ jobs:
             } else {
               issue = context.payload.issue;
             }
-            
             core.setOutput('number', issue.number);
-            core.setOutput('title', issue.title);
+            core.setOutput('title', issue.title || '');
             core.setOutput('body', issue.body || '');
 
-      - name: 'Get Labels'
+      - name: Get Labels
         id: labels
         uses: actions/github-script@v7
         with:
@@ -52,68 +51,87 @@ jobs:
               owner: context.repo.owner,
               repo: context.repo.repo
             });
-            const labelNames = labels.map(l => l.name).join(', ');
-            core.setOutput('available', labelNames);
-            return labelNames;
+            const names = labels.map(l => l.name);
+            core.setOutput('available', names.join(','));
+            return names.join(',');
 
-      - name: 'Analyze with Gemini'
-        uses: google-github-actions/run-gemini-cli@v0
+      - name: Analyze with Gemini
         id: gemini
-        env:
-          ISSUE_TITLE: ${{ steps.issue.outputs.title }}
-          ISSUE_BODY: ${{ steps.issue.outputs.body }}
-          AVAILABLE_LABELS: ${{ steps.labels.outputs.available }}
+        uses: google-github-actions/run-gemini-cli@v0
         with:
           gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
+          # ← ここは ${{ ... }} で式展開するのがポイント
           prompt: |
-            Issue Title: ${ISSUE_TITLE}
-            Issue Body: ${ISSUE_BODY}
-            Available Labels: ${AVAILABLE_LABELS}
-            
-            Select appropriate labels for this GitHub issue. Use this XML format:
+            You are a GitHub issue triage assistant.
+            Issue Title: ${{ steps.issue.outputs.title }}
+            Issue Body:
+            ---
+            ${{ steps.issue.outputs.body }}
+            ---
+            Available Labels (comma-separated): ${{ steps.labels.outputs.available }}
+
+            Task: Choose the MOST relevant labels from the available list only.
+            Return EXACTLY this XML (no prose, no markdown):
             <labels>
-            <label>example</label>
-            <label>kind/task</label>
+            <label>label-1</label>
+            <label>label-2</label>
             </labels>
 
-      - name: 'Apply Labels'
+
+      - name: Apply Labels
+        uses: actions/github-script@v7
         env:
-          GEMINI_OUTPUT: ${{ steps.gemini.outputs.summary }}
+          GEMINI_OUTPUT: ${{ steps.gemini.outputs.text || steps.gemini.outputs.summary }}
           ISSUE_NUMBER: ${{ steps.issue.outputs.number }}
-        uses: actions/github-script@v7
         with:
           script: |
-            const output = process.env.GEMINI_OUTPUT;
+            const raw = process.env.GEMINI_OUTPUT || '';
             const issueNumber = parseInt(process.env.ISSUE_NUMBER);
-            
-            console.log('Gemini output:', output);
-            
+      
+            console.log('Gemini output:', raw);
+      
             let labels = [];
-            
-            // XMLタグから正規表現でラベルを抽出
-            const labelMatches = output.match(/<label>(.*?)<\/label>/g);
-            if (labelMatches) {
-              labels = labelMatches.map(match => 
-                match.replace(/<\/?label>/g, '').trim()
-              ).filter(label => label.length > 0);
+            const matches = raw.match(/<label>(.*?)<\/label>/gis);
+            if (matches) {
+              labels = matches
+                .map(m => m.replace(/<\/?label>/gi, '').trim())
+                .filter(Boolean);
               console.log('Extracted labels from XML:', labels);
             } else {
-              console.log('No XML labels found, using fallback');
+              throw new Error('❌ Gemini output に <label> タグが見つかりませんでした');
             }
-            
-            // フォールバック: needs-triage のみ
-            if (labels.length === 0) {
-              console.log('No labels extracted, applying needs-triage');
-              labels = ['needs-triage'];
-            }
-            
-            // ラベル適用
-            if (labels.length > 0) {
-              await github.rest.issues.addLabels({
-                owner: context.repo.owner,
-                repo: context.repo.repo,
-                issue_number: issueNumber,
-                labels: labels
-              });
-              console.log(`Applied labels: ${labels.join(', ')}`);
+      
+            // ラベルごとに存在チェック → 無ければ作成
+            for (const label of labels) {
+              try {
+                await github.rest.issues.getLabel({
+                  owner: context.repo.owner,
+                  repo: context.repo.repo,
+                  name: label,
+                });
+                console.log(`Label "${label}" already exists`);
+              } catch (err) {
+                if (err.status === 404) {
+                  console.log(`Label "${label}" does not exist. Creating...`);
+                  await github.rest.issues.createLabel({
+                    owner: context.repo.owner,
+                    repo: context.repo.repo,
+                    name: label,
+                    color: 'ededed',   // デフォルト色。必要なら調整
+                    description: `Created automatically by Gemini triage`,
+                  });
+                } else {
+                  throw err;
+                }
+              }
             }
+      
+            // すべて存在するはずなのでまとめて適用
+            await github.rest.issues.addLabels({
+              owner: context.repo.owner,
+              repo: context.repo.repo,
+              issue_number: issueNumber,
+              labels,
+            });
+            console.log(`✅ Applied labels: ${labels.join(', ')}`);
+
```
