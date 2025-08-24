# 💻 Daily Code Changes

## Full Diff

```diff
commit 065c3e3581046d8511efbec76e5e4c29aab7031b
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sun Aug 24 12:06:04 2025 +0900

    Update gemini-issue-automated-triage.yml

diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index 49d20e3..baae78b 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -54,6 +54,14 @@ jobs:
           app-id: '${{ vars.APP_ID }}'
           private-key: '${{ secrets.APP_PRIVATE_KEY }}'
 
+      - name: 'Debug Issue Information'
+        run: |
+          echo "Event name: ${{ github.event_name }}"
+          echo "Issue number: ${{ github.event.issue.number }}"
+          echo "Issue title: '${{ github.event.issue.title }}'"
+          echo "Issue body length: ${{ github.event.issue.body && length(github.event.issue.body) || 0 }}"
+          echo "Issue body preview: '${{ github.event.issue.body }}'"
+
       - name: 'Get Repository Labels'
         id: 'get_labels'
         uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
@@ -90,7 +98,7 @@ jobs:
           use_gemini_code_assist: '${{ vars.GOOGLE_GENAI_USE_GCA }}'
           settings: |-
             {
-              "debug": ${{ fromJSON(env.DEBUG || env.ACTIONS_STEP_DEBUG || false) }},
+              "debug": true,
               "maxSessionTurns": 25,
               "coreTools": [
                 "run_shell_command(echo)"
@@ -101,21 +109,20 @@ jobs:
               }
             }
           prompt: |-
-            You are an issue triage assistant. Analyze the GitHub issue and output ONLY valid JSON.
-
-            Available labels: ${AVAILABLE_LABELS}
-            Issue title: ${ISSUE_TITLE}
-            Issue body: ${ISSUE_BODY}
+            You are an issue triage assistant. Analyze the GitHub issue and suggest appropriate labels.
 
-            IMPORTANT: Output ONLY the JSON response, no explanations or additional text.
+            Repository: ${REPOSITORY}
+            Issue Number: ${ISSUE_NUMBER}
+            Issue Title: "${ISSUE_TITLE}"
+            Issue Body: "${ISSUE_BODY}"
+            Available Labels: ${AVAILABLE_LABELS}
 
-            Required JSON format:
-            {"labels_to_set": ["label1", "label2"], "explanation": "brief explanation"}
+            Please analyze this issue carefully and suggest appropriate labels from the available labels list.
 
-            If no appropriate labels exist, output:
-            {"labels_to_set": [], "explanation": "No suitable labels found"}
+            Output format (JSON only):
+            {"labels_to_set": ["label1", "label2"], "explanation": "reasoning for these labels"}
 
-            JSON response:
+            If the issue content appears to be empty or placeholder text, still try to categorize it based on any available information.
 
       - name: 'Apply Labels to Issue'
         if: |-
```
