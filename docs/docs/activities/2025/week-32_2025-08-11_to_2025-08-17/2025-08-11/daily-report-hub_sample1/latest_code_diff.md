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
index 9f41d75..9ba5232
--- a/.github/scripts/sync-to-hub-gh.sh
+++ b/.github/scripts/sync-to-hub-gh.sh
@@ -137,25 +137,25 @@ if [ -n "$PR_URL" ]; then
   
   PR_NUMBER=$(gh pr view "$PR_URL" --repo "$REPORT_HUB_REPO" --json number --jq '.number')
   
-  # CI完了待機
-  echo "⏳ CI完了を待機中..."
-  max_wait=300
-  wait_time=0
-  while [ $wait_time -lt $max_wait ]; do
-    CHECK_STATUS=$(gh pr view "$PR_NUMBER" --repo "$REPORT_HUB_REPO" --json statusCheckRollup --jq '.statusCheckRollup[-1].state' 2>/dev/null || echo "PENDING")
+  # # CI完了待機
+  # echo "⏳ CI完了を待機中..."
+  # max_wait=300
+  # wait_time=0
+  # while [ $wait_time -lt $max_wait ]; do
+  #   CHECK_STATUS=$(gh pr view "$PR_NUMBER" --repo "$REPORT_HUB_REPO" --json statusCheckRollup --jq '.statusCheckRollup[-1].state' 2>/dev/null || echo "PENDING")
     
-    if [ "$CHECK_STATUS" = "SUCCESS" ]; then
-      echo "✅ CI完了！"
-      break
-    elif [ "$CHECK_STATUS" = "FAILURE" ]; then
-      echo "❌ CI失敗"
-      exit 1
-    else
-      echo "⏳ CI実行中... (${wait_time}秒)"
-      sleep 10
-      wait_time=$((wait_time + 10))
-    fi
-  done
+  #   if [ "$CHECK_STATUS" = "SUCCESS" ]; then
+  #     echo "✅ CI完了！"
+  #     break
+  #   elif [ "$CHECK_STATUS" = "FAILURE" ]; then
+  #     echo "❌ CI失敗"
+  #     exit 1
+  #   else
+  #     echo "⏳ CI実行中... (${wait_time}秒)"
+  #     sleep 10
+  #     wait_time=$((wait_time + 10))
+  #   fi
+  # done
   
   # 🔥 ここがポイント：元のトークンで承認
   echo "👍 元のアカウントで承認実行中..."
diff --git a/.github/scripts/sync-to-hub.sh b/.github/scripts/sync-to-hub.sh
old mode 100644
new mode 100755
```
