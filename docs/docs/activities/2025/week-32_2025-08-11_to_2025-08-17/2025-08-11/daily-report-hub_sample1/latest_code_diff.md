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
index 142df6d..e3a82a1
--- a/.github/scripts/sync-to-hub-gh.sh
+++ b/.github/scripts/sync-to-hub-gh.sh
@@ -17,6 +17,12 @@ CREATE_PR=${CREATE_PR:-true}
 AUTO_APPROVE=${AUTO_APPROVE:-false}
 AUTO_MERGE=${AUTO_MERGE:-false}
 
+# デバッグ用：環境変数を表示
+echo "🔍 Environment Variables:"
+echo "  CREATE_PR: $CREATE_PR"
+echo "  AUTO_APPROVE: $AUTO_APPROVE"
+echo "  AUTO_MERGE: $AUTO_MERGE"
+
 # daily-report-hubは既にクローン済み
 
 # README.mdをコピー
diff --git a/.github/scripts/sync-to-hub.sh b/.github/scripts/sync-to-hub.sh
old mode 100644
new mode 100755
```
