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
index df796aa..6562c20 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -8,9 +8,9 @@ on:
 # 週の開始日を制御する設定
 env:
   WEEK_START_DAY: 1 # 週の開始日 (0=日曜日, 1=月曜日, 2=火曜日, 3=水曜日, 4=木曜日, 5=金曜日, 6=土曜日)
-  AUTO_APPROVE: false # プルリクエストの自動承認 (true/false) - 自分のPRは承認不可
-  AUTO_MERGE: false # プルリクエストの自動マージ (true/false) - 承認なしではマージ不可
-  CREATE_PR: false # 完全自動化のため直接プッシュ
+  AUTO_APPROVE: true # プルリクエストの自動承認 (true/false) - 自分のPRは承認不可
+  AUTO_MERGE: true # プルリクエストの自動マージ (true/false) - 承認なしではマージ不可
+  CREATE_PR: true # 完全自動化のため直接プッシュ
 
 jobs:
   sync-data:
```
