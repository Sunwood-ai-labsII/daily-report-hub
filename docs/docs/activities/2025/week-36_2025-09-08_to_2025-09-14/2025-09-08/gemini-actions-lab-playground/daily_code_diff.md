# 💻 Daily Code Changes

## Full Diff

```diff
commit 518aa5a0630de0764202852cd871b79348bb3fff
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 22:59:50 2025 +0900

    Update gemini-issue-automated-triage.yml

diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index a532d09..cb45ff5 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -42,25 +42,24 @@ jobs:
             core.setOutput('title', issue.title || '');
             core.setOutput('body', issue.body || '');
 
-      - name: Get Labels
+      - name: Get Labels (existing in repo)
         id: labels
         uses: actions/github-script@v7
         with:
           script: |
             const labels = await github.paginate(github.rest.issues.listLabelsForRepo, {
               owner: context.repo.owner,
-              repo: context.repo.repo
+              repo: context.repo.repo,
+              per_page: 100
             });
             const names = labels.map(l => l.name);
             core.setOutput('available', names.join(','));
-            return names.join(',');
 
       - name: Analyze with Gemini
         id: gemini
         uses: google-github-actions/run-gemini-cli@v0
         with:
           gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
-          # ← ここは ${{ ... }} で式展開するのがポイント
           prompt: |
             You are a GitHub issue triage assistant.
             Issue Title: ${{ steps.issue.outputs.title }}
@@ -68,65 +67,92 @@ jobs:
             ---
             ${{ steps.issue.outputs.body }}
             ---
-            Available Labels (comma-separated): ${{ steps.labels.outputs.available }}
+            Existing Labels: ${{ steps.labels.outputs.available }}
+
+            Task:
+            - Suggest 1–3 labels that best categorize this issue.
+            - Prefer existing labels when a good match exists.
+            - If no existing label is a good match, you MAY propose new ones.
+            - New labels must be short, kebab-case (lowercase, hyphen-separated), no spaces or emojis.
+            - Output EXACTLY this XML (no extra text):
 
-            Task: Choose the MOST relevant labels from the available list only.
-            Return EXACTLY this XML (no prose, no markdown):
             <labels>
-            <label>label-1</label>
-            <label>label-2</label>
+              <label>first-label</label>
+              <label>second-label</label>
             </labels>
 
-
-      - name: Apply Labels
+      - name: Apply (create if missing) and Add Labels
         uses: actions/github-script@v7
         env:
           GEMINI_OUTPUT: ${{ steps.gemini.outputs.text || steps.gemini.outputs.summary }}
           ISSUE_NUMBER: ${{ steps.issue.outputs.number }}
+          EXISTING: ${{ steps.labels.outputs.available }}
         with:
           script: |
             const raw = process.env.GEMINI_OUTPUT || '';
-            const issueNumber = parseInt(process.env.ISSUE_NUMBER);
-      
+            const issueNumber = parseInt(process.env.ISSUE_NUMBER || '0', 10);
+            const existing = (process.env.EXISTING || '').split(',').map(s => s.trim()).filter(Boolean);
+
             console.log('Gemini output:', raw);
-      
-            let labels = [];
+
+            // 1) XMLから<label>…</label>を抽出
             const matches = raw.match(/<label>(.*?)<\/label>/gis);
-            if (matches) {
-              labels = matches
-                .map(m => m.replace(/<\/?label>/gi, '').trim())
-                .filter(Boolean);
-              console.log('Extracted labels from XML:', labels);
-            } else {
+            if (!matches) {
               throw new Error('❌ Gemini output に <label> タグが見つかりませんでした');
             }
-      
-            // ラベルごとに存在チェック → 無ければ作成
+
+            // 2) ラベル名の正規化（kebab-case & 不要文字除去）
+            const toKebab = (s) => {
+              return s
+                .toLowerCase()
+                .replace(/[_\s]+/g, '-')      // 空白/アンダーをハイフンへ
+                .replace(/[^a-z0-9-]/g, '')   // 英数とハイフン以外除去
+                .replace(/-+/g, '-')          // 連続ハイフンを1つに
+                .replace(/^-|-$/g, '');       // 先頭/末尾のハイフン除去
+            };
+
+            let labels = matches
+              .map(m => m.replace(/<\/?label>/gi, '').trim())
+              .map(toKebab)
+              .filter(Boolean);
+
+            // 3) 重複排除 & 上限（保守的に3件まで）
+            labels = [...new Set(labels)].slice(0, 3);
+
+            if (labels.length === 0) {
+              // フォールバック（最低限 triage を付与）
+              labels = ['triage'];
+            }
+
+            console.log('Normalized labels:', labels);
+
+            // 4) ラベルの存在確認 → 無ければ作成（色・説明はお好みで）
+            const existingSet = new Set(existing.map(toKebab));
             for (const label of labels) {
+              if (existingSet.has(label)) {
+                console.log(`Label "${label}" already exists`);
+                continue;
+              }
               try {
-                await github.rest.issues.getLabel({
+                console.log(`Creating missing label: ${label}`);
+                await github.rest.issues.createLabel({
                   owner: context.repo.owner,
                   repo: context.repo.repo,
                   name: label,
+                  color: 'ededed',
+                  description: 'Created automatically by Gemini triage',
                 });
-                console.log(`Label "${label}" already exists`);
               } catch (err) {
-                if (err.status === 404) {
-                  console.log(`Label "${label}" does not exist. Creating...`);
-                  await github.rest.issues.createLabel({
-                    owner: context.repo.owner,
-                    repo: context.repo.repo,
-                    name: label,
-                    color: 'ededed',   // デフォルト色。必要なら調整
-                    description: `Created automatically by Gemini triage`,
-                  });
+                // 既に誰かが並行で作ったなど race 条件にも寛容に
+                if (err.status === 422) {
+                  console.log(`Label "${label}" creation returned 422 (likely already exists). Continuing.`);
                 } else {
                   throw err;
                 }
               }
             }
-      
-            // すべて存在するはずなのでまとめて適用
+
+            // 5) まとめて適用
             await github.rest.issues.addLabels({
               owner: context.repo.owner,
               repo: context.repo.repo,
@@ -134,4 +160,3 @@ jobs:
               labels,
             });
             console.log(`✅ Applied labels: ${labels.join(', ')}`);
-
```
