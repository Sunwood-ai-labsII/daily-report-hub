# 💻 Daily Code Changes

## Full Diff

```diff
commit b256d3793bc2ed6daf2234a74c6849839eff0a5e
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sun Aug 24 12:14:41 2025 +0900

    Update gemini-issue-automated-triage.yml

diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index 12e2f11..14899a7 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -59,7 +59,7 @@ jobs:
           echo "Event name: ${{ github.event_name }}"
           echo "Issue number: ${{ github.event.issue.number }}"
           echo "Issue title: '${{ github.event.issue.title }}'"
-          echo "Issue body length: ${{ github.event.issue.body && length(github.event.issue.body) || 0 }}"
+          echo "Issue body length: ${{ github.event.issue.body && format('{0}', github.event.issue.body) != '' && 'has content' || 'empty' }}"
           echo "Issue body preview: '${{ github.event.issue.body }}'"
 
       - name: 'Get Repository Labels'
@@ -165,7 +165,7 @@ jobs:
                     core.info(`Extracted JSON object: ${jsonString}`);
                   } else {
                     // 4. [ で始まって ] で終わる部分を抽出（配列の場合）
-                    const jsonArrayMatch = jsonString.match /(\[[\s\S]*\])/);
+                    const jsonArrayMatch = jsonString.match(/(\[[\s\S]*\])/);
                     if (jsonArrayMatch) {
                       // 配列が返された場合は、最初の要素を使用（単一issue用）
                       const arrayData = JSON.parse(jsonArrayMatch[1].trim());
@@ -238,5 +238,5 @@ jobs:
               owner: context.repo.owner,
               repo: context.repo.repo,
               issue_number: parseInt(process.env.ISSUE_NUMBER),
-              issue: `There is a problem with the Gemini CLI issue triaging. Please check the [action logs](${process.env.RUN_URL}) for details.`
+              body: `There is a problem with the Gemini CLI issue triaging. Please check the [action logs](${process.env.RUN_URL}) for details.`
             })
```
