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
index 2b339fe..df796aa 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -8,9 +8,9 @@ on:
 # 週の開始日を制御する設定
 env:
   WEEK_START_DAY: 1 # 週の開始日 (0=日曜日, 1=月曜日, 2=火曜日, 3=水曜日, 4=木曜日, 5=金曜日, 6=土曜日)
-  AUTO_APPROVE: true # プルリクエストの自動承認 (true/false)
-  AUTO_MERGE: true # プルリクエストの自動マージ (true/false)
-  CREATE_PR: true # プルリクエストを作成するか直接プッシュするか (true/false)
+  AUTO_APPROVE: false # プルリクエストの自動承認 (true/false) - 自分のPRは承認不可
+  AUTO_MERGE: false # プルリクエストの自動マージ (true/false) - 承認なしではマージ不可
+  CREATE_PR: false # 完全自動化のため直接プッシュ
 
 jobs:
   sync-data:
@@ -35,7 +35,7 @@ jobs:
 
       - name: Clone report hub and create structure
         env:
-          GITHUB_TOKEN: ${{ secrets.GH_PAT_YUKIHIKO }}
+          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
         run: |
           # Git設定
@@ -50,7 +50,7 @@ jobs:
 
       - name: Sync to report hub with PR flow (GitHub CLI)
         env:
-          GITHUB_TOKEN: ${{ secrets.GH_PAT_YUKIHIKO }}
+          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
           AUTO_APPROVE: ${{ env.AUTO_APPROVE }}
           AUTO_MERGE: ${{ env.AUTO_MERGE }}
```
