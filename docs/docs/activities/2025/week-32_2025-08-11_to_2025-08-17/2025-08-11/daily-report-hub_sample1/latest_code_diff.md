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
index 79bed22..52888b5
--- a/.github/scripts/sync-to-hub-gh.sh
+++ b/.github/scripts/sync-to-hub-gh.sh
@@ -88,6 +88,10 @@ if [ "$CREATE_PR" = "true" ]; then
   # 新しいブランチを作成してチェックアウト
   git checkout -b "$BRANCH_NAME"
   
+  # コミット作成者を別の人に設定（PATの所有者）
+  git config user.name "Yukihiko Kondo"
+  git config user.email "yukihiko.kondo@example.com"  # 実際のメールアドレスに変更
+  
   # コミットしてプッシュ
   git commit -m "$COMMIT_MESSAGE"
   git push origin "$BRANCH_NAME"
@@ -131,11 +135,15 @@ if [ "$CREATE_PR" = "true" ]; then
   if [ -n "$PR_URL" ]; then
     echo "✅ Pull request created: $PR_URL"
     
-    # 自動承認が有効な場合
+    # 自動承認が有効な場合（自分のPRは承認できないので注意）
     if [ "$AUTO_APPROVE" = "true" ]; then
       echo "👍 Auto-approving pull request..."
-      gh pr review "$PR_URL" --approve --body "✅ Auto-approved by GitHub Actions" --repo "$REPORT_HUB_REPO"
-      echo "✅ Pull request approved"
+      if gh pr review "$PR_URL" --approve --body "✅ Auto-approved by GitHub Actions" --repo "$REPORT_HUB_REPO" 2>/dev/null; then
+        echo "✅ Pull request approved"
+      else
+        echo "⚠️ Cannot approve own pull request. Manual approval required."
+        AUTO_MERGE="false"  # 承認できない場合は自動マージも無効にする
+      fi
     fi
     
     # 自動マージが有効な場合
@@ -166,4 +174,4 @@ else
   git commit -m "$COMMIT_MESSAGE"
   git push
   echo "✅ Successfully synced to report hub!"
-fi
\ No newline at end of file
+fi
diff --git a/.github/scripts/sync-to-hub.sh b/.github/scripts/sync-to-hub.sh
old mode 100644
new mode 100755
```
