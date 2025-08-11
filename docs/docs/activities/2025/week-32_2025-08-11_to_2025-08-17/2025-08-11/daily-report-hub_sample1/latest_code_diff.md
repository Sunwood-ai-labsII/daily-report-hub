# 🔄 Latest Code Changes

```diff
diff --git a/.github/scripts/analyze-git-activity.sh b/.github/scripts/analyze-git-activity.sh
old mode 100644
new mode 100755
diff --git a/.github/scripts/calculate-week-info.sh b/.github/scripts/calculate-week-info.sh
old mode 100644
new mode 100755
diff --git a/.github/scripts/create-docusaurus-structure.sh b/.github/scripts/create-docusaurus-structure.sh
old mode 100644
new mode 100755
diff --git a/.github/scripts/generate-markdown-reports.sh b/.github/scripts/generate-markdown-reports.sh
old mode 100644
new mode 100755
diff --git a/.github/scripts/sync-to-hub-gh.sh b/.github/scripts/sync-to-hub-gh.sh
old mode 100644
new mode 100755
diff --git a/.github/scripts/sync-to-hub.sh b/.github/scripts/sync-to-hub.sh
old mode 100644
new mode 100755
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index 16e1235..32fdc85 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -36,7 +36,7 @@ jobs:
       - name: Clone report hub and create structure
         env:
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}
-          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
+          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
         run: |
           # Git設定
           git config --global user.name "GitHub Actions Bot"
@@ -48,11 +48,11 @@ jobs:
       - name: Create Docusaurus structure
         run: ./.github/scripts/create-docusaurus-structure.sh
 
-      - name: Sync to report hub with PR flow
+      - name: Sync to report hub with PR flow (GitHub CLI)
         env:
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}
-          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
+          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
           AUTO_APPROVE: ${{ env.AUTO_APPROVE }}
           AUTO_MERGE: ${{ env.AUTO_MERGE }}
           CREATE_PR: ${{ env.CREATE_PR }}
-        run: ./.github/scripts/sync-to-hub.sh
+        run: ./.github/scripts/sync-to-hub-gh.sh
```
