# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-issue-scheduled-triage.yml b/.github/workflows/gemini-issue-scheduled-triage.yml
index e22de31..340296b 100644
--- a/.github/workflows/gemini-issue-scheduled-triage.yml
+++ b/.github/workflows/gemini-issue-scheduled-triage.yml
@@ -120,8 +120,8 @@ jobs:
             and pick appropriate labels from the available labels list.
 
             ## Inputs
-            - Available labels: "${AVAILABLE_LABELS}"
-            - Candidate issues (JSON array): "${ISSUES_TO_TRIAGE}"
+            - Available labels: "${{ env.AVAILABLE_LABELS }}"
+            - Candidate issues (JSON array): "${{ env.ISSUES_TO_TRIAGE }}"
 
             ## Critical rules
             - Output MUST be a JSON array.
@@ -131,8 +131,8 @@ jobs:
             - Only choose labels from "${AVAILABLE_LABELS}".
 
             ## Steps
-            1. Read the candidate issues from "${ISSUES_TO_TRIAGE}".
-            2. For each candidate, select one or more labels from "${AVAILABLE_LABELS}".
+            1. Read the candidate issues from "${{ env.ISSUES_TO_TRIAGE }}".
+            2. For each candidate, select one or more labels from "${{ env.AVAILABLE_LABELS }}".
             3. Return a JSON array with objects like:
                \```json
                [
@@ -167,6 +167,7 @@ jobs:
             core.info(`Raw labels JSON: ${rawLabels}`);
 
             let parsedLabels;
+            let parseError = false;
             try {
               let jsonString = rawLabels;
 
@@ -194,8 +195,9 @@ jobs:
               }
               core.info(`Parsed labels JSON entries: ${parsedLabels.length}`);
             } catch (err) {
-              core.setFailed(`Failed to parse labels JSON from Gemini output: ${err.message}\nRaw output: ${rawLabels}`);
-              return;
+              core.warning(`Failed to parse labels JSON from Gemini output: ${err.message}. Will attempt fallback.\nRaw output: ${rawLabels}`);
+              parsedLabels = [];
+              parseError = true;
             }
 
             // Build a set of existing labels, and auto-create missing ones using GH_PAT
@@ -288,7 +290,7 @@ jobs:
             }
 
             // Fallback: if nothing applied to candidates, add a minimal triage label
-            if (appliedCount === 0 && allowed.size > 0) {
+            if ((appliedCount === 0 || parseError) && allowed.size > 0) {
               const fallbackLabel = 'status/needs-triage';
               try {
                 if (!available.has(fallbackLabel)) {
```
