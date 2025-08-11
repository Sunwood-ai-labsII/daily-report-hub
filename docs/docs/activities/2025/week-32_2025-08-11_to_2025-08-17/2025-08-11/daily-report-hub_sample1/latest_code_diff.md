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
index b32fc9a..142df6d
--- a/.github/scripts/sync-to-hub-gh.sh
+++ b/.github/scripts/sync-to-hub-gh.sh
@@ -74,11 +74,12 @@ cd daily-report-hub
 # 最新のmainブランチを取得
 git fetch origin main
 git checkout main
-git reset --hard origin/main
+git pull origin main
 
 # 変更をステージング
 git add .
 
+# ステージされた変更をチェック（リセット前に）
 if git diff --staged --quiet; then
   echo "No changes to commit"
   exit 0
@@ -87,31 +88,39 @@ fi
 COMMIT_MESSAGE="📊 Weekly sync: $REPO_NAME ($DATE) - Week $WEEK_NUMBER - $COMMIT_COUNT commits"
 
 if [ "$CREATE_PR" = "true" ]; then
-  # 既存のPRブランチがあれば削除
+  # 既存の同名PRブランチを削除（安全に）
   BRANCH_NAME="sync/$REPO_NAME-$DATE"
-  git push origin --delete "$BRANCH_NAME" 2>/dev/null || true
+  
+  # ローカルブランチがあれば削除
   git branch -D "$BRANCH_NAME" 2>/dev/null || true
   
+  # リモートブランチがあれば削除
+  git push origin --delete "$BRANCH_NAME" 2>/dev/null || true
+  
   echo "🔀 Creating pull request flow with branch: $BRANCH_NAME"
   
   # 新しいブランチを作成してチェックアウト
   git checkout -b "$BRANCH_NAME"
   
-  # コミット作成者を別の人に設定（PATの所有者）
+  # コミット作成者を設定
   git config user.name "Yukihiko Kondo"
   git config user.email "yukihiko.fuyuki@example.com"
   
   # コミットして強制プッシュ
   git commit -m "$COMMIT_MESSAGE"
-  git push -f origin "$BRANCH_NAME"
+  git push origin "$BRANCH_NAME"
   
-  # 既存のPRがあれば閉じる
+  # 既存のPRをチェックして閉じる
   echo "🔍 Checking for existing pull requests..."
-  EXISTING_PR=$(gh pr list --repo "$REPORT_HUB_REPO" --head "$BRANCH_NAME" --json number --jq '.[0].number' 2>/dev/null || echo "")
+  EXISTING_PRS=$(gh pr list --repo "$REPORT_HUB_REPO" --author "@me" --state open --json number,headRefName --jq '.[] | select(.headRefName | startswith("sync/'$REPO_NAME'")) | .number' 2>/dev/null || echo "")
   
-  if [ -n "$EXISTING_PR" ] && [ "$EXISTING_PR" != "null" ]; then
-    echo "🗑️ Closing existing PR #$EXISTING_PR"
-    gh pr close "$EXISTING_PR" --repo "$REPORT_HUB_REPO" --comment "Superseded by new sync" 2>/dev/null || true
+  if [ -n "$EXISTING_PRS" ]; then
+    echo "🗑️ Closing existing PRs for this repo..."
+    echo "$EXISTING_PRS" | while read pr_number; do
+      if [ -n "$pr_number" ]; then
+        gh pr close "$pr_number" --repo "$REPORT_HUB_REPO" --comment "Superseded by new daily sync" 2>/dev/null || true
+      fi
+    done
   fi
   
   # GitHub CLIでプルリクエストを作成
@@ -187,9 +196,9 @@ if [ "$CREATE_PR" = "true" ]; then
     git push origin --delete "$BRANCH_NAME" 2>/dev/null || true
   fi
 else
-  # 直接プッシュフロー（強制上書き）
-  echo "⚡ Direct push mode (force overwrite)"
+  # 直接プッシュフロー
+  echo "⚡ Direct push mode"
   git commit -m "$COMMIT_MESSAGE"
   git push origin main
-  echo "✅ Successfully synced to report hub with force overwrite!"
+  echo "✅ Successfully synced to report hub via direct push!"
 fi
diff --git a/.github/scripts/sync-to-hub.sh b/.github/scripts/sync-to-hub.sh
old mode 100644
new mode 100755
```
