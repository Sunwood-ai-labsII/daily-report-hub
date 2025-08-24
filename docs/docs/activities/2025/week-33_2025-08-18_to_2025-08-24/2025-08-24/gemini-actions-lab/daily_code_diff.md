# 💻 Daily Code Changes

## Full Diff

```diff
commit 1987f769980bd01ed56686d9ea2a65ca5c8c355d
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sun Aug 24 12:19:14 2025 +0900

    Update gemini-issue-automated-triage.yml

diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index 14899a7..6914b92 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -16,7 +16,7 @@ on:
         type: 'number'
 
 concurrency:
-  group: '${{ github.workflow }}-${{ github.event.issue.number }}'
+  group: '${{ github.workflow }}-${{ github.event.issue.number || github.event.inputs.issue_number }}'
   cancel-in-progress: true
 
 defaults:
@@ -54,13 +54,45 @@ jobs:
           app-id: '${{ vars.APP_ID }}'
           private-key: '${{ secrets.APP_PRIVATE_KEY }}'
 
-      - name: 'Debug Issue Information'
-        run: |
-          echo "Event name: ${{ github.event_name }}"
-          echo "Issue number: ${{ github.event.issue.number }}"
-          echo "Issue title: '${{ github.event.issue.title }}'"
-          echo "Issue body length: ${{ github.event.issue.body && format('{0}', github.event.issue.body) != '' && 'has content' || 'empty' }}"
-          echo "Issue body preview: '${{ github.event.issue.body }}'"
+      - name: 'Get Issue Information'
+        id: 'get_issue'
+        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+        with:
+          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          script: |
+            let issueNumber, issueTitle, issueBody;
+            
+            if (context.eventName === 'workflow_dispatch') {
+              // 手動実行の場合はinputから取得
+              issueNumber = parseInt('${{ github.event.inputs.issue_number }}');
+              console.log(`Manual dispatch for issue #${issueNumber}`);
+              
+              // APIでissue情報を取得
+              const { data: issue } = await github.rest.issues.get({
+                owner: context.repo.owner,
+                repo: context.repo.repo,
+                issue_number: issueNumber
+              });
+              
+              issueTitle = issue.title;
+              issueBody = issue.body || '';
+            } else {
+              // 通常のイベントの場合
+              issueNumber = context.payload.issue.number;
+              issueTitle = context.payload.issue.title;
+              issueBody = context.payload.issue.body || '';
+            }
+            
+            console.log(`Event name: ${context.eventName}`);
+            console.log(`Issue number: ${issueNumber}`);
+            console.log(`Issue title: '${issueTitle}'`);
+            console.log(`Issue body length: ${issueBody.length}`);
+            console.log(`Issue body preview: '${issueBody.substring(0, 200)}${issueBody.length > 200 ? '...' : ''}'`);
+            
+            // 後続のステップで使用するために出力
+            core.setOutput('issue_number', issueNumber);
+            core.setOutput('issue_title', issueTitle);
+            core.setOutput('issue_body', issueBody);
 
       - name: 'Get Repository Labels'
         id: 'get_labels'
@@ -82,9 +114,9 @@ jobs:
         id: 'gemini_issue_analysis'
         env:
           GITHUB_TOKEN: '' # Do not pass any auth token here since this runs on untrusted inputs
-          ISSUE_TITLE: '${{ github.event.issue.title }}'
-          ISSUE_BODY: '${{ github.event.issue.body }}'
-          ISSUE_NUMBER: '${{ github.event.issue.number }}'
+          ISSUE_TITLE: '${{ steps.get_issue.outputs.issue_title }}'
+          ISSUE_BODY: '${{ steps.get_issue.outputs.issue_body }}'
+          ISSUE_NUMBER: '${{ steps.get_issue.outputs.issue_number }}'
           REPOSITORY: '${{ github.repository }}'
           AVAILABLE_LABELS: '${{ steps.get_labels.outputs.available_labels }}'
         with:
@@ -131,7 +163,7 @@ jobs:
           ${{ steps.gemini_issue_analysis.outputs.summary != '' }}
         env:
           REPOSITORY: '${{ github.repository }}'
-          ISSUE_NUMBER: '${{ github.event.issue.number }}'
+          ISSUE_NUMBER: '${{ steps.get_issue.outputs.issue_number }}'
           LABELS_OUTPUT: '${{ steps.gemini_issue_analysis.outputs.summary }}'
         uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
         with:
@@ -228,7 +260,7 @@ jobs:
         if: |-
           ${{ failure() && steps.gemini_issue_analysis.outcome == 'failure' }}
         env:
-          ISSUE_NUMBER: '${{ github.event.issue.number }}'
+          ISSUE_NUMBER: '${{ steps.get_issue.outputs.issue_number }}'
           RUN_URL: '${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}'
         uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
         with:
```
