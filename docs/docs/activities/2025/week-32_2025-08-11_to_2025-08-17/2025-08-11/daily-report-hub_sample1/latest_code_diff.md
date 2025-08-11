# 🔄 Latest Code Changes

```diff
diff --git a/.github/scripts/README.md b/.github/scripts/README.md
index 4e2fff1..c7e07f4 100644
--- a/.github/scripts/README.md
+++ b/.github/scripts/README.md
@@ -74,6 +74,47 @@ env:
   WEEK_START_DAY: 1  # 0=日曜日, 1=月曜日, 2=火曜日, etc.
 ```
 
+## プルリクエストフロー設定
+
+v2.0では、プルリクエストベースのフローと自動承認機能が追加されました：
+
+```yaml
+env:
+  WEEK_START_DAY: 1     # 週の開始日
+  AUTO_APPROVE: true    # プルリクエストの自動承認
+  AUTO_MERGE: true      # プルリクエストの自動マージ
+  CREATE_PR: true       # プルリクエストを作成するか直接プッシュするか
+```
+
+### 設定オプション
+
+| 設定 | 説明 | デフォルト |
+|------|------|------------|
+| `CREATE_PR` | `true`: プルリクエストを作成<br>`false`: 直接プッシュ | `true` |
+| `AUTO_APPROVE` | `true`: プルリクエストを自動承認<br>`false`: 手動承認が必要 | `false` |
+| `AUTO_MERGE` | `true`: 承認後に自動マージ<br>`false`: 手動マージが必要 | `false` |
+
+### フロー例
+
+1. **完全自動化**: `CREATE_PR=true`, `AUTO_APPROVE=true`, `AUTO_MERGE=true`
+   - プルリクエスト作成 → 自動承認 → 自動マージ
+
+2. **承認のみ手動**: `CREATE_PR=true`, `AUTO_APPROVE=false`, `AUTO_MERGE=true`
+   - プルリクエスト作成 → 手動承認 → 自動マージ
+
+3. **完全手動**: `CREATE_PR=true`, `AUTO_APPROVE=false`, `AUTO_MERGE=false`
+   - プルリクエスト作成 → 手動承認 → 手動マージ
+
+4. **直接プッシュ**: `CREATE_PR=false`
+   - 従来通りの直接プッシュ（v1.4と同じ動作）
+
+## ワークフローファイル
+
+2つのバージョンが利用可能です：
+
+- `sync-to-report.yml`: cURLベースの実装
+- `sync-to-report-gh.yml`: GitHub CLI使用版（推奨）
+
 ## フォルダ構造
 
 生成されるフォルダ構造：
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
new file mode 100755
index 0000000..79bed22
--- /dev/null
+++ b/.github/scripts/sync-to-hub-gh.sh
@@ -0,0 +1,169 @@
+#!/bin/bash
+
+# レポートハブに同期するスクリプト（GitHub CLI使用版）
+
+set -e
+
+# 必要な環境変数をチェック
+: ${GITHUB_TOKEN:?}
+: ${REPORT_HUB_REPO:?}
+: ${TARGET_DIR:?}
+: ${REPO_NAME:?}
+: ${DATE:?}
+: ${WEEK_NUMBER:?}
+
+# プルリクエストフロー設定（デフォルト値）
+CREATE_PR=${CREATE_PR:-true}
+AUTO_APPROVE=${AUTO_APPROVE:-false}
+AUTO_MERGE=${AUTO_MERGE:-false}
+
+# daily-report-hubは既にクローン済み
+
+# README.mdをコピー
+cp README.md "$TARGET_DIR/" 2>/dev/null || echo "# $REPO_NAME" > "$TARGET_DIR/README.md"
+
+# 当日のアクティビティファイルをコピー（全て.mdファイル）
+cp daily_commits.md "$TARGET_DIR/"
+cp daily_cumulative_diff.md "$TARGET_DIR/"
+cp daily_diff_stats.md "$TARGET_DIR/"
+cp daily_code_diff.md "$TARGET_DIR/"
+cp latest_diff.md "$TARGET_DIR/"
+cp latest_code_diff.md "$TARGET_DIR/"
+cp daily_summary.md "$TARGET_DIR/"
+
+# 詳細メタデータを作成
+COMMIT_COUNT=$(wc -l < daily_commits_raw.txt)
+FILES_CHANGED=$(grep -c '^' daily_cumulative_diff_raw.txt 2>/dev/null || echo "0")
+
+cat > "$TARGET_DIR/metadata.json" << EOF
+{
+  "repository": "$GITHUB_REPOSITORY",
+  "date": "$DATE",
+  "week_folder": "$WEEK_FOLDER",
+  "week_number": $WEEK_NUMBER,
+  "week_start_date": "$WEEK_START_DATE",
+  "week_end_date": "$WEEK_END_DATE",
+  "branch": "$GITHUB_REF_NAME",
+  "latest_commit_sha": "$GITHUB_SHA",
+  "sync_timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
+  "workflow_run": "$GITHUB_RUN_ID",
+  "daily_commit_count": $COMMIT_COUNT,
+  "daily_files_changed": $FILES_CHANGED,
+  "has_activity": $([ $COMMIT_COUNT -gt 0 ] && echo "true" || echo "false"),
+  "pr_flow": {
+    "create_pr": $CREATE_PR,
+    "auto_approve": $AUTO_APPROVE,
+    "auto_merge": $AUTO_MERGE
+  },
+  "files": {
+    "readme": "README.md",
+    "summary": "daily_summary.md",
+    "commits": "daily_commits.md",
+    "file_changes": "daily_cumulative_diff.md",
+    "stats": "daily_diff_stats.md",
+    "code_diff": "daily_code_diff.md",
+    "latest_diff": "latest_diff.md",
+    "latest_code_diff": "latest_code_diff.md"
+  }
+}
+EOF
+
+# プルリクエストフローまたは直接プッシュ
+cd daily-report-hub
+git add .
+
+if git diff --staged --quiet; then
+  echo "No changes to commit"
+  exit 0
+fi
+
+COMMIT_MESSAGE="📊 Weekly sync: $REPO_NAME ($DATE) - Week $WEEK_NUMBER - $COMMIT_COUNT commits"
+
+if [ "$CREATE_PR" = "true" ]; then
+  # プルリクエストフロー（GitHub CLI使用）
+  BRANCH_NAME="sync/$REPO_NAME-$DATE-$(date +%s)"
+  
+  echo "🔀 Creating pull request flow with branch: $BRANCH_NAME"
+  
+  # 新しいブランチを作成してチェックアウト
+  git checkout -b "$BRANCH_NAME"
+  
+  # コミットしてプッシュ
+  git commit -m "$COMMIT_MESSAGE"
+  git push origin "$BRANCH_NAME"
+  
+  # GitHub CLIでプルリクエストを作成
+  PR_BODY="## 📊 Daily Report Sync
+
+**Repository:** \`$GITHUB_REPOSITORY\`
+**Date:** $DATE
+**Week:** $WEEK_NUMBER ($WEEK_START_DATE to $WEEK_END_DATE)
+
+### 📈 Activity Summary
+- **Commits:** $COMMIT_COUNT
+- **Files Changed:** $FILES_CHANGED
+- **Sync Time:** $(date '+%Y-%m-%d %H:%M:%S')
+
+### 📋 Generated Files
+- Daily summary report
+- Commit details
+- File changes
+- Code differences
+- Statistics
+
+### ⚙️ Automation Settings
+- **Auto Approve:** $AUTO_APPROVE
+- **Auto Merge:** $AUTO_MERGE
+
+---
+*Auto-generated by GitHub Actions*"
+
+  echo "📝 Creating pull request with GitHub CLI..."
+  
+  # GitHub CLIでプルリクエストを作成
+  PR_URL=$(gh pr create \
+    --title "$COMMIT_MESSAGE" \
+    --body "$PR_BODY" \
+    --base main \
+    --head "$BRANCH_NAME" \
+    --repo "$REPORT_HUB_REPO" 2>/dev/null || echo "")
+  
+  if [ -n "$PR_URL" ]; then
+    echo "✅ Pull request created: $PR_URL"
+    
+    # 自動承認が有効な場合
+    if [ "$AUTO_APPROVE" = "true" ]; then
+      echo "👍 Auto-approving pull request..."
+      gh pr review "$PR_URL" --approve --body "✅ Auto-approved by GitHub Actions" --repo "$REPORT_HUB_REPO"
+      echo "✅ Pull request approved"
+    fi
+    
+    # 自動マージが有効な場合
+    if [ "$AUTO_MERGE" = "true" ]; then
+      echo "🔀 Auto-merging pull request..."
+      sleep 2  # APIの反映を待つ
+      
+      if gh pr merge "$PR_URL" --squash --delete-branch --repo "$REPORT_HUB_REPO" 2>/dev/null; then
+        echo "✅ Pull request merged and branch deleted successfully"
+      else
+        echo "⚠️ Failed to auto-merge. Manual merge required."
+        echo "PR URL: $PR_URL"
+      fi
+    else
+      echo "📋 Pull request created and ready for manual review: $PR_URL"
+    fi
+  else
+    echo "❌ Failed to create pull request with GitHub CLI. Falling back to direct push."
+    git checkout main
+    git merge "$BRANCH_NAME"
+    git push origin main
+    git branch -d "$BRANCH_NAME"
+    git push origin --delete "$BRANCH_NAME" 2>/dev/null || true
+  fi
+else
+  # 直接プッシュフロー
+  echo "⚡ Direct push mode"
+  git commit -m "$COMMIT_MESSAGE"
+  git push
+  echo "✅ Successfully synced to report hub!"
+fi
\ No newline at end of file
diff --git a/.github/scripts/sync-to-hub.sh b/.github/scripts/sync-to-hub.sh
old mode 100644
new mode 100755
index fc870c6..0a7d604
--- a/.github/scripts/sync-to-hub.sh
+++ b/.github/scripts/sync-to-hub.sh
@@ -1,6 +1,6 @@
 #!/bin/bash
 
-# レポートハブに同期するスクリプト
+# レポートハブに同期するスクリプト（プルリクエストフロー対応）
 
 set -e
 
@@ -12,6 +12,11 @@ set -e
 : ${DATE:?}
 : ${WEEK_NUMBER:?}
 
+# プルリクエストフロー設定（デフォルト値）
+CREATE_PR=${CREATE_PR:-true}
+AUTO_APPROVE=${AUTO_APPROVE:-false}
+AUTO_MERGE=${AUTO_MERGE:-false}
+
 # daily-report-hubは既にクローン済み
 
 # README.mdをコピー
@@ -58,14 +63,122 @@ cat > "$TARGET_DIR/metadata.json" << EOF
 }
 EOF
 
-# タイムスタンプ付きでコミット・プッシュ
+# プルリクエストフローまたは直接プッシュ
 cd daily-report-hub
 git add .
 
 if git diff --staged --quiet; then
   echo "No changes to commit"
+  exit 0
+fi
+
+COMMIT_MESSAGE="📊 Weekly sync: $REPO_NAME ($DATE) - Week $WEEK_NUMBER - $COMMIT_COUNT commits"
+
+if [ "$CREATE_PR" = "true" ]; then
+  # プルリクエストフロー
+  BRANCH_NAME="sync/$REPO_NAME-$DATE-$(date +%s)"
+  
+  echo "🔀 Creating pull request flow with branch: $BRANCH_NAME"
+  
+  # 新しいブランチを作成してチェックアウト
+  git checkout -b "$BRANCH_NAME"
+  
+  # コミットしてプッシュ
+  git commit -m "$COMMIT_MESSAGE"
+  git push origin "$BRANCH_NAME"
+  
+  # プルリクエストを作成
+  PR_BODY="## 📊 Daily Report Sync
+
+**Repository:** \`$GITHUB_REPOSITORY\`
+**Date:** $DATE
+**Week:** $WEEK_NUMBER ($WEEK_START_DATE to $WEEK_END_DATE)
+
+### 📈 Activity Summary
+- **Commits:** $COMMIT_COUNT
+- **Files Changed:** $FILES_CHANGED
+- **Sync Time:** $(date '+%Y-%m-%d %H:%M:%S')
+
+### 📋 Generated Files
+- Daily summary report
+- Commit details
+- File changes
+- Code differences
+- Statistics
+
+---
+*Auto-generated by GitHub Actions*"
+
+  echo "📝 Creating pull request..."
+  PR_URL=$(curl -s -X POST \
+    -H "Authorization: token $GITHUB_TOKEN" \
+    -H "Accept: application/vnd.github.v3+json" \
+    "https://api.github.com/repos/$REPORT_HUB_REPO/pulls" \
+    -d "{
+      \"title\": \"$COMMIT_MESSAGE\",
+      \"body\": \"$PR_BODY\",
+      \"head\": \"$BRANCH_NAME\",
+      \"base\": \"main\"
+    }" | jq -r '.html_url // empty')
+  
+  if [ -n "$PR_URL" ]; then
+    echo "✅ Pull request created: $PR_URL"
+    
+    # プルリクエスト番号を取得
+    PR_NUMBER=$(echo "$PR_URL" | grep -o '[0-9]*$')
+    
+    # 自動承認が有効な場合
+    if [ "$AUTO_APPROVE" = "true" ]; then
+      echo "👍 Auto-approving pull request..."
+      curl -s -X POST \
+        -H "Authorization: token $GITHUB_TOKEN" \
+        -H "Accept: application/vnd.github.v3+json" \
+        "https://api.github.com/repos/$REPORT_HUB_REPO/pulls/$PR_NUMBER/reviews" \
+        -d '{"event": "APPROVE", "body": "✅ Auto-approved by GitHub Actions"}' > /dev/null
+      echo "✅ Pull request approved"
+    fi
+    
+    # 自動マージが有効な場合
+    if [ "$AUTO_MERGE" = "true" ]; then
+      echo "🔀 Auto-merging pull request..."
+      sleep 2  # APIの反映を待つ
+      MERGE_RESULT=$(curl -s -X PUT \
+        -H "Authorization: token $GITHUB_TOKEN" \
+        -H "Accept: application/vnd.github.v3+json" \
+        "https://api.github.com/repos/$REPORT_HUB_REPO/pulls/$PR_NUMBER/merge" \
+        -d "{
+          \"commit_title\": \"$COMMIT_MESSAGE\",
+          \"merge_method\": \"squash\"
+        }")
+      
+      if echo "$MERGE_RESULT" | jq -e '.merged' > /dev/null 2>&1; then
+        echo "✅ Pull request merged successfully"
+        
+        # マージ後にブランチを削除
+        curl -s -X DELETE \
+          -H "Authorization: token $GITHUB_TOKEN" \
+          -H "Accept: application/vnd.github.v3+json" \
+          "https://api.github.com/repos/$REPORT_HUB_REPO/git/refs/heads/$BRANCH_NAME" > /dev/null
+        echo "🗑️ Branch $BRANCH_NAME deleted"
+      else
+        echo "⚠️ Failed to auto-merge. Manual merge required."
+        echo "PR URL: $PR_URL"
+      fi
+    else
+      echo "📋 Pull request created and ready for manual review: $PR_URL"
+    fi
+  else
+    echo "❌ Failed to create pull request. Falling back to direct push."
+    git checkout main
+    git merge "$BRANCH_NAME"
+    git push origin main
+    git branch -d "$BRANCH_NAME"
+    git push origin --delete "$BRANCH_NAME" 2>/dev/null || true
+  fi
 else
-  git commit -m "📊 Weekly sync: $REPO_NAME ($DATE) - Week $WEEK_NUMBER - $COMMIT_COUNT commits"
+  # 直接プッシュフロー
+  echo "⚡ Direct push mode"
+  git commit -m "$COMMIT_MESSAGE"
   git push
   echo "✅ Successfully synced to report hub!"
 fi
\ No newline at end of file
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
new file mode 100644
index 0000000..89b88fd
--- /dev/null
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -0,0 +1,66 @@
+name: Sync to Daily Report Hub v2.0 (GitHub CLI)
+on:
+  push:
+    branches: [main, master]
+  pull_request:
+    types: [opened, synchronize, closed]
+
+# 週の開始日を制御する設定
+env:
+  WEEK_START_DAY: 1 # 週の開始日 (0=日曜日, 1=月曜日, 2=火曜日, 3=水曜日, 4=木曜日, 5=金曜日, 6=土曜日)
+  AUTO_APPROVE: true # プルリクエストの自動承認 (true/false)
+  AUTO_MERGE: true # プルリクエストの自動マージ (true/false)
+  CREATE_PR: true # プルリクエストを作成するか直接プッシュするか (true/false)
+
+jobs:
+  sync-data:
+    runs-on: ubuntu-latest
+    steps:
+      - name: Checkout current repo
+        uses: actions/checkout@v4
+        with:
+          fetch-depth: 0 # 全履歴を取得してその日の全コミットを追跡
+
+      - name: Setup GitHub CLI
+        run: |
+          # GitHub CLIは既にubuntu-latestにインストール済み
+          gh --version
+
+      - name: Make scripts executable
+        run: chmod +x .github/scripts/*.sh
+
+      - name: Calculate week information
+        run: ./.github/scripts/calculate-week-info.sh ${{ env.WEEK_START_DAY }}
+
+      - name: Analyze Git activity
+        run: ./.github/scripts/analyze-git-activity.sh
+
+      - name: Generate Markdown reports
+        run: ./.github/scripts/generate-markdown-reports.sh
+
+      - name: Clone report hub and create structure
+        env:
+          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
+          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
+        run: |
+          # Git設定
+          git config --global user.name "GitHub Actions Bot"
+          git config --global user.email "actions@github.com"
+
+          # GitHub CLI認証
+          echo "$GITHUB_TOKEN" | gh auth login --with-token
+
+          # daily-report-hubをクローン
+          git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub
+
+      - name: Create Docusaurus structure
+        run: ./.github/scripts/create-docusaurus-structure.sh
+
+      - name: Sync to report hub with PR flow (GitHub CLI)
+        env:
+          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
+          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
+          AUTO_APPROVE: ${{ env.AUTO_APPROVE }}
+          AUTO_MERGE: ${{ env.AUTO_MERGE }}
+          CREATE_PR: ${{ env.CREATE_PR }}
+        run: ./.github/scripts/sync-to-hub-gh.sh
\ No newline at end of file
diff --git a/.github/workflows/sync-to-report.yml b/.github/workflows/sync-to-report.yml
index b0a97ba..16e1235 100644
--- a/.github/workflows/sync-to-report.yml
+++ b/.github/workflows/sync-to-report.yml
@@ -1,4 +1,4 @@
-name: Sync to Daily Report Hub v1.4
+name: Sync to Daily Report Hub v2.0
 on:
   push:
     branches: [main, master]
@@ -8,6 +8,9 @@ on:
 # 週の開始日を制御する設定
 env:
   WEEK_START_DAY: 1 # 週の開始日 (0=日曜日, 1=月曜日, 2=火曜日, 3=水曜日, 4=木曜日, 5=金曜日, 6=土曜日)
+  AUTO_APPROVE: true # プルリクエストの自動承認 (true/false)
+  AUTO_MERGE: true # プルリクエストの自動マージ (true/false)
+  CREATE_PR: true # プルリクエストを作成するか直接プッシュするか (true/false)
 
 jobs:
   sync-data:
@@ -38,15 +41,18 @@ jobs:
           # Git設定
           git config --global user.name "GitHub Actions Bot"
           git config --global user.email "actions@github.com"
-          
+
           # daily-report-hubをクローン
           git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub
 
       - name: Create Docusaurus structure
         run: ./.github/scripts/create-docusaurus-structure.sh
 
-      - name: Sync to report hub
+      - name: Sync to report hub with PR flow
         env:
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
-        run: ./.github/scripts/sync-to-hub.sh
\ No newline at end of file
+          AUTO_APPROVE: ${{ env.AUTO_APPROVE }}
+          AUTO_MERGE: ${{ env.AUTO_MERGE }}
+          CREATE_PR: ${{ env.CREATE_PR }}
+        run: ./.github/scripts/sync-to-hub.sh
```
