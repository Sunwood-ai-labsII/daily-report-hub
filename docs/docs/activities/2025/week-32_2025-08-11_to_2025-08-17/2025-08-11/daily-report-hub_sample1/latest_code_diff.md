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
index 32fdc85..2b339fe 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -35,7 +35,7 @@ jobs:
 
       - name: Clone report hub and create structure
         env:
-          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
+          GITHUB_TOKEN: ${{ secrets.GH_PAT_YUKIHIKO }}
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
         run: |
           # Git設定
@@ -50,7 +50,7 @@ jobs:
 
       - name: Sync to report hub with PR flow (GitHub CLI)
         env:
-          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
+          GITHUB_TOKEN: ${{ secrets.GH_PAT_YUKIHIKO }}
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
           AUTO_APPROVE: ${{ env.AUTO_APPROVE }}
           AUTO_MERGE: ${{ env.AUTO_MERGE }}
```
