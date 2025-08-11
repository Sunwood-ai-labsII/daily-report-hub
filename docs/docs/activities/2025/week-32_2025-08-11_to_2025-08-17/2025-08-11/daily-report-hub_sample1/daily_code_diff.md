# 💻 Daily Code Changes

## Full Diff

```diff
diff --git a/.env.example b/.env.example
new file mode 100644
index 0000000..218c470
--- /dev/null
+++ b/.env.example
@@ -0,0 +1,15 @@
+# おみくじアプリ設定例
+# 実際の設定は .env ファイルに記載してください
+
+# アプリケーション設定
+APP_NAME=おみくじアプリ
+APP_VERSION=1.0.0
+
+# 将来的な機能拡張用
+# API_ENDPOINT=https://api.example.com
+# DEBUG_MODE=false
+# ANALYTICS_ID=your-analytics-id
+
+# GitHub Actions関連（必要に応じて）
+# GITHUB_TOKEN=your-github-token
+# REPORT_HUB_REPO=your-username/daily-report-hub
\ No newline at end of file
diff --git a/.github/scripts/README.md b/.github/scripts/README.md
new file mode 100644
index 0000000..4e2fff1
--- /dev/null
+++ b/.github/scripts/README.md
@@ -0,0 +1,100 @@
+# GitHub Actions Scripts
+
+このディレクトリには、Daily Report Hub同期ワークフローで使用されるスクリプトが含まれています。
+
+## スクリプト一覧
+
+### 1. `calculate-week-info.sh`
+週情報を計算し、環境変数を設定します。
+
+**使用方法:**
+```bash
+./calculate-week-info.sh [WEEK_START_DAY]
+```
+
+**パラメータ:**
+- `WEEK_START_DAY`: 週の開始日 (0=日曜日, 1=月曜日, ..., 6=土曜日)
+
+**出力環境変数:**
+- `REPO_NAME`: リポジトリ名
+- `DATE`: 現在の日付 (YYYY-MM-DD)
+- `YEAR`: 現在の年
+- `WEEK_FOLDER`: 週フォルダ名
+- `WEEK_START_DATE`: 週の開始日
+- `WEEK_END_DATE`: 週の終了日
+- `WEEK_NUMBER`: 週番号
+
+### 2. `analyze-git-activity.sh`
+Gitの活動を分析し、生データファイルを生成します。
+
+**生成ファイル:**
+- `daily_commits_raw.txt`: その日のコミット一覧
+- `daily_cumulative_diff_raw.txt`: その日の累積差分
+- `daily_diff_stats_raw.txt`: その日の統計情報
+- `daily_code_diff_raw.txt`: その日のコード差分
+- `latest_diff_raw.txt`: 最新の差分
+- `latest_code_diff_raw.txt`: 最新のコード差分
+
+### 3. `generate-markdown-reports.sh`
+生データからMarkdownレポートを生成します。
+
+**生成ファイル:**
+- `daily_commits.md`: コミット詳細レポート
+- `daily_cumulative_diff.md`: ファイル変更レポート
+- `daily_diff_stats.md`: 統計レポート
+- `daily_code_diff.md`: コード差分レポート
+- `latest_diff.md`: 最新変更レポート
+- `latest_code_diff.md`: 最新コード差分レポート
+- `daily_summary.md`: 日次サマリーレポート
+
+### 4. `create-docusaurus-structure.sh`
+Docusaurusの構造と`_category_.json`ファイルを作成します。
+
+**必要な環境変数:**
+- `REPO_NAME`, `DATE`, `YEAR`, `WEEK_FOLDER`, `WEEK_NUMBER`, `WEEK_START_DATE`, `WEEK_END_DATE`
+
+**出力環境変数:**
+- `TARGET_DIR`: ターゲットディレクトリのパス
+
+### 5. `sync-to-hub.sh`
+レポートハブにファイルを同期します。
+
+**必要な環境変数:**
+- `GITHUB_TOKEN`: GitHubアクセストークン
+- `REPORT_HUB_REPO`: レポートハブのリポジトリ
+- `TARGET_DIR`: ターゲットディレクトリ
+- その他の週情報変数
+
+## 週の開始日設定
+
+ワークフローファイルの`env.WEEK_START_DAY`を変更することで、週の開始日を制御できます：
+
+```yaml
+env:
+  WEEK_START_DAY: 1  # 0=日曜日, 1=月曜日, 2=火曜日, etc.
+```
+
+## フォルダ構造
+
+生成されるフォルダ構造：
+```
+docs/docs/activities/
+├── _category_.json
+└── 2025/
+    ├── _category_.json
+    └── week-06_2025-08-04_to_2025-08-10/
+        ├── _category_.json
+        └── 2025-08-05/
+            ├── _category_.json
+            └── your-repo/
+                ├── _category_.json
+                ├── daily_summary.md
+                ├── daily_commits.md
+                ├── daily_cumulative_diff.md
+                ├── daily_diff_stats.md
+                ├── daily_code_diff.md
+                ├── latest_diff.md
+                ├── latest_code_diff.md
+                ├── README.md
+                └── metadata.json
+```
\ No newline at end of file
diff --git a/.github/scripts/analyze-git-activity.sh b/.github/scripts/analyze-git-activity.sh
new file mode 100644
index 0000000..af185ef
--- /dev/null
+++ b/.github/scripts/analyze-git-activity.sh
@@ -0,0 +1,59 @@
+#!/bin/bash
+
+# Git活動を分析してMarkdownファイルを生成するスクリプト
+
+set -e
+
+DATE=${DATE:-$(date '+%Y-%m-%d')}
+
+echo "🔍 Fetching all commits for $DATE..."
+
+# その日の全コミット履歴を取得（時刻順）
+git log --since="$DATE 00:00:00" --until="$DATE 23:59:59" \
+  --pretty=format:"%h|%s|%an|%ad" --date=format:'%H:%M:%S' \
+  --reverse > daily_commits_raw.txt
+
+# コミット数をカウント
+COMMIT_COUNT=$(wc -l < daily_commits_raw.txt)
+echo "📊 Found $COMMIT_COUNT commits for today"
+
+# その日の全ての差分を統合（安全な方法で）
+if [ $COMMIT_COUNT -gt 0 ]; then
+  FIRST_COMMIT_TODAY=$(git log --since="$DATE 00:00:00" --pretty=format:"%H" --reverse | head -1)
+  LAST_COMMIT_TODAY=$(git log --since="$DATE 00:00:00" --pretty=format:"%H" | head -1)
+  
+  echo "First commit: $FIRST_COMMIT_TODAY"
+  echo "Last commit: $LAST_COMMIT_TODAY"
+  
+  # 親コミットが存在するかチェック
+  if git rev-parse --verify "$FIRST_COMMIT_TODAY^" >/dev/null 2>&1; then
+    # 親コミットが存在する場合
+    PARENT_OF_FIRST=$(git rev-parse $FIRST_COMMIT_TODAY^)
+    git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY --name-status > daily_cumulative_diff_raw.txt 2>/dev/null || echo "No diff available" > daily_cumulative_diff_raw.txt
+    git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY --stat > daily_diff_stats_raw.txt 2>/dev/null || echo "No stats available" > daily_diff_stats_raw.txt
+    # コードの詳細差分を取得
+    git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY > daily_code_diff_raw.txt 2>/dev/null || echo "No code diff available" > daily_code_diff_raw.txt
+  else
+    # 初回コミットの場合（親が存在しない）
+    echo "Initial commit detected - showing all files as new"
+    git diff --name-status 4b825dc642cb6eb9a060e54bf8d69288fbee4904..$LAST_COMMIT_TODAY > daily_cumulative_diff_raw.txt 2>/dev/null || \
+    git ls-tree --name-status $LAST_COMMIT_TODAY > daily_cumulative_diff_raw.txt 2>/dev/null || \
+    echo "A\t(all files added in initial commit)" > daily_cumulative_diff_raw.txt
+    
+    git diff --stat 4b825dc642cb6eb9a060e54bf8d69288fbee4904..$LAST_COMMIT_TODAY > daily_diff_stats_raw.txt 2>/dev/null || \
+    echo "Initial commit - all files added" > daily_diff_stats_raw.txt
+    
+    # 初回コミットのコード内容
+    git show $LAST_COMMIT_TODAY > daily_code_diff_raw.txt 2>/dev/null || echo "No code diff available" > daily_code_diff_raw.txt
+  fi
+else
+  echo "No commits found for today" > daily_cumulative_diff_raw.txt
+  echo "No commits found for today" > daily_diff_stats_raw.txt
+  echo "No commits found for today" > daily_code_diff_raw.txt
+fi
+
+# 最新コミットの個別差分
+git diff HEAD~1 --name-status > latest_diff_raw.txt 2>/dev/null || echo "No recent diff available" > latest_diff_raw.txt
+git diff HEAD~1 > latest_code_diff_raw.txt 2>/dev/null || echo "No recent code diff available" > latest_code_diff_raw.txt
+
+echo "✅ Git activity analysis complete!"
\ No newline at end of file
diff --git a/.github/scripts/calculate-week-info.sh b/.github/scripts/calculate-week-info.sh
new file mode 100644
index 0000000..0d35476
--- /dev/null
+++ b/.github/scripts/calculate-week-info.sh
@@ -0,0 +1,44 @@
+#!/bin/bash
+
+# 週情報を計算するスクリプト
+# 使用方法: ./calculate-week-info.sh [WEEK_START_DAY]
+
+set -e
+
+WEEK_START_DAY=${1:-1}  # デフォルトは月曜日
+
+# リポジトリ名と日付を取得
+REPO_NAME=$(basename $GITHUB_REPOSITORY)
+DATE=$(date '+%Y-%m-%d')
+YEAR=$(date '+%Y')
+
+# 週の計算（週の開始日を考慮）
+CURRENT_DAY_OF_WEEK=$(date '+%w')  # 0=日曜日
+DAYS_SINCE_WEEK_START=$(( (CURRENT_DAY_OF_WEEK - WEEK_START_DAY + 7) % 7 ))
+WEEK_START_DATE=$(date -d "$DATE -$DAYS_SINCE_WEEK_START days" '+%Y-%m-%d')
+WEEK_END_DATE=$(date -d "$WEEK_START_DATE +6 days" '+%Y-%m-%d')
+
+# 週番号を計算（年の最初の週の開始日から数える）
+YEAR_START=$(date -d "$YEAR-01-01" '+%Y-%m-%d')
+YEAR_START_DAY_OF_WEEK=$(date -d "$YEAR_START" '+%w')
+FIRST_WEEK_START_OFFSET=$(( (WEEK_START_DAY - YEAR_START_DAY_OF_WEEK + 7) % 7 ))
+FIRST_WEEK_START=$(date -d "$YEAR_START +$FIRST_WEEK_START_OFFSET days" '+%Y-%m-%d')
+
+# 週番号を計算
+DAYS_DIFF=$(( ($(date -d "$WEEK_START_DATE" '+%s') - $(date -d "$FIRST_WEEK_START" '+%s')) / 86400 ))
+WEEK_NUMBER=$(( DAYS_DIFF / 7 + 1 ))
+
+# 週フォルダ名を作成
+WEEK_FOLDER=$(printf "week-%02d_%s_to_%s" $WEEK_NUMBER $WEEK_START_DATE $WEEK_END_DATE)
+
+# 環境変数に出力
+echo "REPO_NAME=$REPO_NAME" >> $GITHUB_ENV
+echo "DATE=$DATE" >> $GITHUB_ENV
+echo "YEAR=$YEAR" >> $GITHUB_ENV
+echo "WEEK_FOLDER=$WEEK_FOLDER" >> $GITHUB_ENV
+echo "WEEK_START_DATE=$WEEK_START_DATE" >> $GITHUB_ENV
+echo "WEEK_END_DATE=$WEEK_END_DATE" >> $GITHUB_ENV
+echo "WEEK_NUMBER=$WEEK_NUMBER" >> $GITHUB_ENV
+
+echo "📅 Date: $DATE"
+echo "📅 Week: $WEEK_FOLDER"
\ No newline at end of file
diff --git a/.github/scripts/create-docusaurus-structure.sh b/.github/scripts/create-docusaurus-structure.sh
new file mode 100644
index 0000000..5f4d9bf
--- /dev/null
+++ b/.github/scripts/create-docusaurus-structure.sh
@@ -0,0 +1,111 @@
+#!/bin/bash
+
+# Docusaurusの構造と_category_.jsonファイルを作成するスクリプト
+
+set -e
+
+# 必要な環境変数をチェック
+: ${REPO_NAME:?}
+: ${DATE:?}
+: ${YEAR:?}
+: ${WEEK_FOLDER:?}
+: ${WEEK_NUMBER:?}
+: ${WEEK_START_DATE:?}
+: ${WEEK_END_DATE:?}
+
+REPORT_HUB_DIR="daily-report-hub"
+ACTIVITIES_DIR="$REPORT_HUB_DIR/docs/docs/activities"
+YEAR_DIR="$ACTIVITIES_DIR/$YEAR"
+WEEK_DIR="$YEAR_DIR/$WEEK_FOLDER"
+DATE_DIR="$WEEK_DIR/$DATE"
+TARGET_DIR="$DATE_DIR/$REPO_NAME"
+
+# ディレクトリを作成
+mkdir -p "$TARGET_DIR"
+
+# Docusaurus _category_.json ファイルを作成
+
+# 1. activities ディレクトリの _category_.json
+if [ ! -f "$ACTIVITIES_DIR/_category_.json" ]; then
+  cat > "$ACTIVITIES_DIR/_category_.json" << 'EOF'
+{
+  "label": "📊 Activities",
+  "position": 1,
+  "link": {
+    "type": "generated-index",
+    "description": "Daily development activities and reports"
+  }
+}
+EOF
+fi
+
+# 2. 年ディレクトリの _category_.json
+if [ ! -f "$YEAR_DIR/_category_.json" ]; then
+  cat > "$YEAR_DIR/_category_.json" << EOF
+{
+  "label": "$YEAR",
+  "position": 1,
+  "link": {
+    "type": "generated-index",
+    "description": "Activities for year $YEAR"
+  }
+}
+EOF
+fi
+
+# 3. 週ディレクトリの _category_.json
+if [ ! -f "$WEEK_DIR/_category_.json" ]; then
+  WEEK_LABEL="Week $WEEK_NUMBER ($WEEK_START_DATE to $WEEK_END_DATE)"
+  cat > "$WEEK_DIR/_category_.json" << EOF
+{
+  "label": "$WEEK_LABEL",
+  "position": $WEEK_NUMBER,
+  "link": {
+    "type": "generated-index",
+    "description": "Activities for $WEEK_LABEL"
+  }
+}
+EOF
+fi
+
+# 4. 日付ディレクトリの _category_.json
+if [ ! -f "$DATE_DIR/_category_.json" ]; then
+  DATE_LABEL="📅 $DATE"
+  # 日付から位置を計算（月の日にち）
+  DATE_POSITION=$(date -d "$DATE" '+%d' | sed 's/^0*//')
+  cat > "$DATE_DIR/_category_.json" << EOF
+{
+  "label": "$DATE_LABEL",
+  "position": $DATE_POSITION,
+  "link": {
+    "type": "generated-index",
+    "description": "Activities for $DATE"
+  }
+}
+EOF
+fi
+
+# 5. リポジトリディレクトリの _category_.json
+if [ ! -f "$TARGET_DIR/_category_.json" ]; then
+  cat > "$TARGET_DIR/_category_.json" << EOF
+{
+  "label": "🔧 $REPO_NAME",
+  "position": 1,
+  "link": {
+    "type": "generated-index",
+    "description": "Repository: $GITHUB_REPOSITORY"
+  }
+}
+EOF
+fi
+
+echo "📁 Created directory structure:"
+echo "  📂 $YEAR_DIR"
+echo "    📂 $WEEK_FOLDER"
+echo "      📂 $DATE"
+echo "        📂 $REPO_NAME"
+echo ""
+echo "📄 Created _category_.json files for Docusaurus navigation"
+
+# TARGET_DIRを環境変数として出力
+echo "TARGET_DIR=$TARGET_DIR" >> $GITHUB_ENV
\ No newline at end of file
diff --git a/.github/scripts/generate-markdown-reports.sh b/.github/scripts/generate-markdown-reports.sh
new file mode 100644
index 0000000..7d2251f
--- /dev/null
+++ b/.github/scripts/generate-markdown-reports.sh
@@ -0,0 +1,187 @@
+#!/bin/bash
+
+# Markdownレポートを生成するスクリプト
+
+set -e
+
+# 各行に4スペースのインデントを追加する関数
+add_indent() {
+  sed 's/^/    /' "$1"
+}
+
+# ファイル変更のステータスアイコンを取得する関数
+get_status_icon() {
+  case $1 in
+    A) echo "- 🆕 **Added:** \`$2\`" ;;
+    M) echo "- ✏️ **Modified:** \`$2\`" ;;
+    D) echo "- 🗑️ **Deleted:** \`$2\`" ;;
+    R*) echo "- 🔄 **Renamed:** \`$2\`" ;;
+    *) echo "- 📝 **$1:** \`$2\`" ;;
+  esac
+}
+
+# コミット詳細をMarkdown形式で作成（差分付き）
+{
+  echo "# 📝 Daily Commits"
+  echo ""
+  if [ -s daily_commits_raw.txt ]; then
+    while IFS='|' read -r hash subject author time; do
+      echo "## ⏰ $time - \`$hash\`"
+      echo "**$subject**"
+      echo "*by $author*"
+      echo ""
+      
+      # 各コミットの変更ファイル一覧を表示
+      echo "### 📋 Changed Files"
+      echo "\`\`\`"
+      git show --name-status $hash 2>/dev/null | grep -E '^[AMDRC]' || echo "No file changes"
+      echo "\`\`\`"
+      echo ""
+      
+      # 各コミットの統計情報を表示
+      echo "### 📊 Statistics"
+      echo "\`\`\`"
+      git show --stat $hash 2>/dev/null | tail -n +2 || echo "No statistics available"
+      echo "\`\`\`"
+      echo ""
+      
+      # 各コミットのコード差分を表示（最初の100行まで）
+      echo "### 💻 Code Changes"
+      echo "\`\`\`diff"
+      git show $hash --pretty=format:"" 2>/dev/null | head -100 || echo "No code changes available"
+      echo "\`\`\`"
+      echo ""
+      echo "---"
+      echo ""
+    done < daily_commits_raw.txt
+  else
+    echo "*No commits found for today.*"
+  fi
+} > daily_commits.md
+
+# 累積差分をMarkdown形式で作成
+{
+  echo "# 📋 Daily File Changes"
+  echo ""
+  if [ -s daily_cumulative_diff_raw.txt ]; then
+    while read -r line; do
+      if [ ! -z "$line" ]; then
+        status=$(echo "$line" | cut -f1)
+        file=$(echo "$line" | cut -f2)
+        get_status_icon "$status" "$file"
+      fi
+    done < daily_cumulative_diff_raw.txt
+  else
+    echo "*No file changes today.*"
+  fi
+} > daily_cumulative_diff.md
+
+# 統計をMarkdown形式で作成
+{
+  echo "# 📈 Daily Statistics"
+  echo ""
+  add_indent daily_diff_stats_raw.txt
+} > daily_diff_stats.md
+
+# コード差分をMarkdown形式で作成
+{
+  echo "# 💻 Daily Code Changes"
+  echo ""
+  echo "## Full Diff"
+  echo ""
+  echo "\`\`\`diff"
+  cat daily_code_diff_raw.txt
+  echo "\`\`\`"
+} > daily_code_diff.md
+
+# 最新差分をMarkdown形式で作成
+{
+  echo "# 🔄 Latest Changes (File List)"
+  echo ""
+  if [ -s latest_diff_raw.txt ]; then
+    while read -r line; do
+      if [ ! -z "$line" ]; then
+        status=$(echo "$line" | cut -f1)
+        file=$(echo "$line" | cut -f2)
+        get_status_icon "$status" "$file"
+      fi
+    done < latest_diff_raw.txt
+  else
+    echo "*No recent changes.*"
+  fi
+} > latest_diff.md
+
+# 最新コード差分をMarkdown形式で作成
+{
+  echo "# 🔄 Latest Code Changes"
+  echo ""
+  echo "\`\`\`diff"
+  cat latest_code_diff_raw.txt
+  echo "\`\`\`"
+} > latest_code_diff.md
+
+# 詳細なアクティビティサマリーをMarkdown形式で作成
+if [ -s daily_commits_raw.txt ]; then
+  FIRST_COMMIT_TIME=$(head -1 daily_commits_raw.txt | cut -d'|' -f4)
+  LAST_COMMIT_TIME=$(tail -1 daily_commits_raw.txt | cut -d'|' -f4)
+  FILES_CHANGED=$(grep -c '^' daily_cumulative_diff_raw.txt 2>/dev/null || echo "0")
+else
+  FIRST_COMMIT_TIME="N/A"
+  LAST_COMMIT_TIME="N/A" 
+  FILES_CHANGED=0
+fi
+
+# メインサマリーファイルを作成
+{
+  echo "# 📅 Daily Activity Report"
+  echo ""
+  echo "## 📊 Summary"
+  echo "| Item | Value |"
+  echo "|------|-------|"
+  echo "| Repository | \`$GITHUB_REPOSITORY\` |"
+  echo "| Date | $DATE |"
+  echo "| Total Commits | **$(wc -l < daily_commits_raw.txt)** |"
+  echo "| Files Changed | **$FILES_CHANGED** |"
+  echo "| First Activity | $FIRST_COMMIT_TIME |"
+  echo "| Last Activity | $LAST_COMMIT_TIME |"
+  echo "| Sync Time | $(date '+%H:%M:%S') |"
+  echo ""
+  
+  if [ -s daily_commits_raw.txt ]; then
+    echo "## 📝 Commit Details"
+    echo ""
+    while IFS='|' read -r hash subject author time; do
+      echo "### ⏰ $time - \`$hash\`"
+      echo "**$subject**"
+      echo "*by $author*"
+      echo ""
+    done < daily_commits_raw.txt
+    
+    echo "## 📈 File Changes Statistics"
+    echo ""
+    add_indent daily_diff_stats_raw.txt
+    echo ""
+    
+    echo "## 📋 Changed Files List"
+    echo ""
+    while read -r line; do
+      if [ ! -z "$line" ]; then
+        status=$(echo "$line" | cut -f1)
+        file=$(echo "$line" | cut -f2)
+        get_status_icon "$status" "$file"
+      fi
+    done < daily_cumulative_diff_raw.txt
+    echo ""
+    
+  else
+    echo "## 📝 Commit Details"
+    echo ""
+    echo "*No commits found for today.*"
+    echo ""
+  fi
+  
+  echo "---"
+  echo "*Generated by GitHub Actions at $(date '+%Y-%m-%d %H:%M:%S')*"
+} > daily_summary.md
+
+echo "✅ Markdown reports generated successfully!"
\ No newline at end of file
diff --git a/.github/scripts/sync-to-hub.sh b/.github/scripts/sync-to-hub.sh
new file mode 100644
index 0000000..9e96989
--- /dev/null
+++ b/.github/scripts/sync-to-hub.sh
@@ -0,0 +1,70 @@
+#!/bin/bash
+
+# レポートハブに同期するスクリプト
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
+  "files": {
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
+# タイムスタンプ付きでコミット・プッシュ
+cd daily-report-hub
+git add .
+
+if git diff --staged --quiet; then
+  echo "No changes to commit"
+else
+  git commit -m "📊 Weekly sync: $REPO_NAME ($DATE) - Week $WEEK_NUMBER - $COMMIT_COUNT commits"
+  git push
+  echo "✅ Successfully synced to report hub!"
+fi
\ No newline at end of file
diff --git a/.github/workflows/sync-to-report.yml b/.github/workflows/sync-to-report.yml
index 05e88cd..b0a97ba 100644
--- a/.github/workflows/sync-to-report.yml
+++ b/.github/workflows/sync-to-report.yml
@@ -1,9 +1,13 @@
-name: Sync to Daily Report Hub
+name: Sync to Daily Report Hub v1.4
 on:
   push:
     branches: [main, master]
   pull_request:
-    types: [merged]
+    types: [opened, synchronize, closed]
+
+# 週の開始日を制御する設定
+env:
+  WEEK_START_DAY: 1 # 週の開始日 (0=日曜日, 1=月曜日, 2=火曜日, 3=水曜日, 4=木曜日, 5=金曜日, 6=土曜日)
 
 jobs:
   sync-data:
@@ -12,289 +16,37 @@ jobs:
       - name: Checkout current repo
         uses: actions/checkout@v4
         with:
-          fetch-depth: 0  # 全履歴を取得してその日の全コミットを追跡
-      
-      - name: Get repository info and daily activities
-        run: |
-          # リポジトリ名と日付を取得
-          REPO_NAME=$(basename $GITHUB_REPOSITORY)
-          DATE=$(date '+%Y-%m-%d')
-          echo "REPO_NAME=$REPO_NAME" >> $GITHUB_ENV
-          echo "DATE=$DATE" >> $GITHUB_ENV
-          
-          echo "🔍 Fetching all commits for $DATE..."
-          
-          # その日の全コミット履歴を取得（時刻順）
-          git log --since="$DATE 00:00:00" --until="$DATE 23:59:59" \
-            --pretty=format:"%h|%s|%an|%ad" --date=format:'%H:%M:%S' \
-            --reverse > daily_commits_raw.txt
-          
-          # コミット数をカウント
-          COMMIT_COUNT=$(wc -l < daily_commits_raw.txt)
-          echo "📊 Found $COMMIT_COUNT commits for today"
-          
-          # その日の全ての差分を統合（安全な方法で）
-          if [ $COMMIT_COUNT -gt 0 ]; then
-            FIRST_COMMIT_TODAY=$(git log --since="$DATE 00:00:00" --pretty=format:"%H" --reverse | head -1)
-            LAST_COMMIT_TODAY=$(git log --since="$DATE 00:00:00" --pretty=format:"%H" | head -1)
-            
-            echo "First commit: $FIRST_COMMIT_TODAY"
-            echo "Last commit: $LAST_COMMIT_TODAY"
-            
-            # 親コミットが存在するかチェック
-            if git rev-parse --verify "$FIRST_COMMIT_TODAY^" >/dev/null 2>&1; then
-              # 親コミットが存在する場合
-              PARENT_OF_FIRST=$(git rev-parse $FIRST_COMMIT_TODAY^)
-              git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY --name-status > daily_cumulative_diff_raw.txt 2>/dev/null || echo "No diff available" > daily_cumulative_diff_raw.txt
-              git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY --stat > daily_diff_stats_raw.txt 2>/dev/null || echo "No stats available" > daily_diff_stats_raw.txt
-              # コードの詳細差分を取得
-              git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY > daily_code_diff_raw.txt 2>/dev/null || echo "No code diff available" > daily_code_diff_raw.txt
-            else
-              # 初回コミットの場合（親が存在しない）
-              echo "Initial commit detected - showing all files as new"
-              git diff --name-status 4b825dc642cb6eb9a060e54bf8d69288fbee4904..$LAST_COMMIT_TODAY > daily_cumulative_diff_raw.txt 2>/dev/null || \
-              git ls-tree --name-status $LAST_COMMIT_TODAY > daily_cumulative_diff_raw.txt 2>/dev/null || \
-              echo "A\t(all files added in initial commit)" > daily_cumulative_diff_raw.txt
-              
-              git diff --stat 4b825dc642cb6eb9a060e54bf8d69288fbee4904..$LAST_COMMIT_TODAY > daily_diff_stats_raw.txt 2>/dev/null || \
-              echo "Initial commit - all files added" > daily_diff_stats_raw.txt
-              
-              # 初回コミットのコード内容
-              git show $LAST_COMMIT_TODAY > daily_code_diff_raw.txt 2>/dev/null || echo "No code diff available" > daily_code_diff_raw.txt
-            fi
-          else
-            echo "No commits found for today" > daily_cumulative_diff_raw.txt
-            echo "No commits found for today" > daily_diff_stats_raw.txt
-            echo "No commits found for today" > daily_code_diff_raw.txt
-          fi
-          
-          # 最新コミットの個別差分
-          git diff HEAD~1 --name-status > latest_diff_raw.txt 2>/dev/null || echo "No recent diff available" > latest_diff_raw.txt
-          git diff HEAD~1 > latest_code_diff_raw.txt 2>/dev/null || echo "No recent code diff available" > latest_code_diff_raw.txt
-          
-          # Markdownファイルを作成（各行に4スペースのインデントを追加する関数）
-          add_indent() {
-            sed 's/^/    /' "$1"
-          }
-          
-          # コミット詳細をMarkdown形式で作成
-          {
-            echo "# 📝 Daily Commits"
-            echo ""
-            if [ -s daily_commits_raw.txt ]; then
-              while IFS='|' read -r hash subject author time; do
-                echo "## ⏰ $time - \`$hash\`"
-                echo "**$subject**"
-                echo "*by $author*"
-                echo ""
-              done < daily_commits_raw.txt
-            else
-              echo "*No commits found for today.*"
-            fi
-          } > daily_commits.md
-          
-          # 累積差分をMarkdown形式で作成
-          {
-            echo "# 📋 Daily File Changes"
-            echo ""
-            if [ -s daily_cumulative_diff_raw.txt ]; then
-              while read -r line; do
-                if [ ! -z "$line" ]; then
-                  status=$(echo "$line" | cut -f1)
-                  file=$(echo "$line" | cut -f2)
-                  case $status in
-                    A) echo "- 🆕 **Added:** \`$file\`" ;;
-                    M) echo "- ✏️ **Modified:** \`$file\`" ;;
-                    D) echo "- 🗑️ **Deleted:** \`$file\`" ;;
-                    R*) echo "- 🔄 **Renamed:** \`$file\`" ;;
-                    *) echo "- 📝 **$status:** \`$file\`" ;;
-                  esac
-                fi
-              done < daily_cumulative_diff_raw.txt
-            else
-              echo "*No file changes today.*"
-            fi
-          } > daily_cumulative_diff.md
-          
-          # 統計をMarkdown形式で作成
-          {
-            echo "# 📈 Daily Statistics"
-            echo ""
-            add_indent daily_diff_stats_raw.txt
-          } > daily_diff_stats.md
-          
-          # コード差分をMarkdown形式で作成
-          {
-            echo "# 💻 Daily Code Changes"
-            echo ""
-            echo "## Full Diff"
-            echo ""
-            add_indent daily_code_diff_raw.txt
-          } > daily_code_diff.md
-          
-          # 最新差分をMarkdown形式で作成
-          {
-            echo "# 🔄 Latest Changes (File List)"
-            echo ""
-            if [ -s latest_diff_raw.txt ]; then
-              while read -r line; do
-                if [ ! -z "$line" ]; then
-                  status=$(echo "$line" | cut -f1)
-                  file=$(echo "$line" | cut -f2)
-                  case $status in
-                    A) echo "- 🆕 **Added:** \`$file\`" ;;
-                    M) echo "- ✏️ **Modified:** \`$file\`" ;;
-                    D) echo "- 🗑️ **Deleted:** \`$file\`" ;;
-                    R*) echo "- 🔄 **Renamed:** \`$file\`" ;;
-                    *) echo "- 📝 **$status:** \`$file\`" ;;
-                  esac
-                fi
-              done < latest_diff_raw.txt
-            else
-              echo "*No recent changes.*"
-            fi
-          } > latest_diff.md
-          
-          # 最新コード差分をMarkdown形式で作成
-          {
-            echo "# 🔄 Latest Code Changes"
-            echo ""
-            add_indent latest_code_diff_raw.txt
-          } > latest_code_diff.md
-          
-          # 詳細なアクティビティサマリーをMarkdown形式で作成
-          if [ -s daily_commits_raw.txt ]; then
-            FIRST_COMMIT_TIME=$(head -1 daily_commits_raw.txt | cut -d'|' -f4)
-            LAST_COMMIT_TIME=$(tail -1 daily_commits_raw.txt | cut -d'|' -f4)
-            FILES_CHANGED=$(grep -c '^' daily_cumulative_diff_raw.txt 2>/dev/null || echo "0")
-          else
-            FIRST_COMMIT_TIME="N/A"
-            LAST_COMMIT_TIME="N/A" 
-            FILES_CHANGED=0
-          fi
-          
-          # メインサマリーファイルを作成
-          {
-            echo "# 📅 Daily Activity Report"
-            echo ""
-            echo "## 📊 Summary"
-            echo "| Item | Value |"
-            echo "|------|-------|"
-            echo "| Repository | \`$GITHUB_REPOSITORY\` |"
-            echo "| Date | $DATE |"
-            echo "| Total Commits | **$COMMIT_COUNT** |"
-            echo "| Files Changed | **$FILES_CHANGED** |"
-            echo "| First Activity | $FIRST_COMMIT_TIME |"
-            echo "| Last Activity | $LAST_COMMIT_TIME |"
-            echo "| Sync Time | $(date '+%H:%M:%S') |"
-            echo ""
-            
-            if [ -s daily_commits_raw.txt ]; then
-              echo "## 📝 Commit Details"
-              echo ""
-              while IFS='|' read -r hash subject author time; do
-                echo "### ⏰ $time - \`$hash\`"
-                echo "**$subject**"
-                echo "*by $author*"
-                echo ""
-              done < daily_commits_raw.txt
-              
-              echo "## 📈 File Changes Statistics"
-              echo ""
-              add_indent daily_diff_stats_raw.txt
-              echo ""
-              
-              echo "## 📋 Changed Files List"
-              echo ""
-              while read -r line; do
-                if [ ! -z "$line" ]; then
-                  status=$(echo "$line" | cut -f1)
-                  file=$(echo "$line" | cut -f2)
-                  case $status in
-                    A) echo "- 🆕 **Added:** \`$file\`" ;;
-                    M) echo "- ✏️ **Modified:** \`$file\`" ;;
-                    D) echo "- 🗑️ **Deleted:** \`$file\`" ;;
-                    R*) echo "- 🔄 **Renamed:** \`$file\`" ;;
-                    *) echo "- 📝 **$status:** \`$file\`" ;;
-                  esac
-                fi
-              done < daily_cumulative_diff_raw.txt
-              echo ""
-              
-            else
-              echo "## 📝 Commit Details"
-              echo ""
-              echo "*No commits found for today.*"
-              echo ""
-            fi
-            
-            echo "---"
-            echo "*Generated by GitHub Actions at $(date '+%Y-%m-%d %H:%M:%S')*"
-          } > daily_summary.md
-          
-          echo "✅ Daily activity analysis complete!"
-      
-      - name: Clone and update report hub
+          fetch-depth: 0 # 全履歴を取得してその日の全コミットを追跡
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
         env:
-          GITHUB_TOKEN: ${{ secrets.REPORT_TOKEN }}
+          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
+          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
         run: |
           # Git設定
           git config --global user.name "GitHub Actions Bot"
           git config --global user.email "actions@github.com"
           
           # daily-report-hubをクローン
-          git clone https://x-access-token:${GITHUB_TOKEN}@github.com/Sunwood-ai-labs/daily-report-hub.git
-          
-          # 日付ベースのディレクトリ構造を作成
-          TARGET_DIR="daily-report-hub/activities/$DATE/$REPO_NAME"
-          mkdir -p "$TARGET_DIR"
-          
-          # README.mdをコピー
-          cp README.md "$TARGET_DIR/" 2>/dev/null || echo "# $REPO_NAME" > "$TARGET_DIR/README.md"
-          
-          # 当日のアクティビティファイルをコピー（全て.mdファイル）
-          cp daily_commits.md "$TARGET_DIR/"
-          cp daily_cumulative_diff.md "$TARGET_DIR/"
-          cp daily_diff_stats.md "$TARGET_DIR/"
-          cp daily_code_diff.md "$TARGET_DIR/"
-          cp latest_diff.md "$TARGET_DIR/"
-          cp latest_code_diff.md "$TARGET_DIR/"
-          cp daily_summary.md "$TARGET_DIR/"
-          
-          # 詳細メタデータを作成
-          COMMIT_COUNT=$(wc -l < daily_commits_raw.txt)
-          FILES_CHANGED=$(grep -c '^' daily_cumulative_diff_raw.txt 2>/dev/null || echo "0")
-          
-          cat > "$TARGET_DIR/metadata.json" << EOF
-          {
-            "repository": "$GITHUB_REPOSITORY",
-            "date": "$DATE",
-            "branch": "$GITHUB_REF_NAME",
-            "latest_commit_sha": "$GITHUB_SHA",
-            "sync_timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
-            "workflow_run": "$GITHUB_RUN_ID",
-            "daily_commit_count": $COMMIT_COUNT,
-            "daily_files_changed": $FILES_CHANGED,
-            "has_activity": $([ $COMMIT_COUNT -gt 0 ] && echo "true" || echo "false"),
-            "files": {
-              "summary": "daily_summary.md",
-              "commits": "daily_commits.md",
-              "file_changes": "daily_cumulative_diff.md",
-              "stats": "daily_diff_stats.md",
-              "code_diff": "daily_code_diff.md",
-              "latest_diff": "latest_diff.md",
-              "latest_code_diff": "latest_code_diff.md"
-            }
-          }
-          EOF
-          
-          # タイムスタンプ付きでコミット・プッシュ
-          cd daily-report-hub
-          git add .
-          
-          if git diff --staged --quiet; then
-            echo "No changes to commit"
-          else
-            git commit -m "📊 Daily sync: $REPO_NAME ($DATE) - $COMMIT_COUNT commits"
-            git push
-          fi
\ No newline at end of file
+          git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub
+
+      - name: Create Docusaurus structure
+        run: ./.github/scripts/create-docusaurus-structure.sh
+
+      - name: Sync to report hub
+        env:
+          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
+          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
+        run: ./.github/scripts/sync-to-hub.sh
\ No newline at end of file
diff --git a/CHANGELOG.md b/CHANGELOG.md
new file mode 100644
index 0000000..20aeb24
--- /dev/null
+++ b/CHANGELOG.md
@@ -0,0 +1,32 @@
+# 📝 変更履歴
+
+このファイルは、プロジェクトの重要な変更を記録します。
+
+形式は [Keep a Changelog](https://keepachangelog.com/ja/1.0.0/) に基づいており、
+このプロジェクトは [セマンティック バージョニング](https://semver.org/lang/ja/) に準拠しています。
+
+## [Unreleased]
+
+### 追加
+- README.mdの視覚的改善（中央揃え、バッジ、ヘッダー画像）
+- スクリーンショットプレースホルダーの追加
+- JavaScriptファイルへの詳細コメント追加
+- おみくじ結果に応じた色分けスタイリング
+- .env.exampleファイルの追加
+- CONTRIBUTING.mdの追加
+- CHANGELOG.mdの追加（このファイル）
+
+### 変更
+- CSSにアニメーション効果を追加
+- プロジェクト構造の文書化を改善
+
+## [1.0.0] - 2025-01-XX
+
+### 追加
+- 基本的なおみくじ機能
+- シンプルなウェブインターフェース
+- GitHub Actions による日報同期機能
+- レスポンシブデザイン
+
+[Unreleased]: https://github.com/your-username/daily-report-hub_sample1/compare/v1.0.0...HEAD
+[1.0.0]: https://github.com/your-username/daily-report-hub_sample1/releases/tag/v1.0.0
\ No newline at end of file
diff --git a/CONTRIBUTING.md b/CONTRIBUTING.md
new file mode 100644
index 0000000..1962486
--- /dev/null
+++ b/CONTRIBUTING.md
@@ -0,0 +1,51 @@
+# 🤝 コントリビューションガイド
+
+おみくじアプリへの貢献をお考えいただき、ありがとうございます！
+
+## 📋 貢献方法
+
+### 🐛 バグ報告
+
+バグを発見した場合は、以下の情報を含めてIssueを作成してください：
+
+- 使用しているブラウザとバージョン
+- 再現手順
+- 期待される動作
+- 実際の動作
+- スクリーンショット（可能であれば）
+
+### 💡 機能提案
+
+新機能のアイデアがある場合は、以下を含めてIssueを作成してください：
+
+- 機能の詳細説明
+- 使用ケース
+- 実装の提案（任意）
+
+### 🔧 プルリクエスト
+
+1. このリポジトリをフォーク
+2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
+3. 変更をコミット (`git commit -m 'Add some amazing feature'`)
+4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
+5. プルリクエストを作成
+
+## 📝 コーディング規約
+
+- **HTML**: セマンティックなマークアップを心がける
+- **CSS**: BEMまたは類似の命名規則を使用
+- **JavaScript**: ESLintの推奨設定に従う
+- **コメント**: 複雑な処理には適切なコメントを追加
+
+## 🧪 テスト
+
+変更を行う前に、以下のブラウザでテストしてください：
+
+- Chrome (最新版)
+- Firefox (最新版)
+- Safari (最新版)
+- Edge (最新版)
+
+## 📄 ライセンス
+
+このプロジェクトに貢献することで、あなたの貢献が同じライセンスの下で配布されることに同意したものとみなされます。
\ No newline at end of file
diff --git a/README.md b/README.md
index f2432b3..e5baa3d 100644
--- a/README.md
+++ b/README.md
@@ -1,5 +1,17 @@
+<div align="center">
+
+![](https://github.com/user-attachments/assets/f7afed43-1d98-4886-b2e0-57c99dd7874e)
+
 # daily-report-hub_sample1
 
+<p>
+  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
+  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
+  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
+</p>
+
+</div>
+
 > [!IMPORTANT]
 > このリポジトリは、GitHub Actionsを利用してGitのコミット履歴から自動で日報を作成・集約するワークフローのサンプルです。
 >
@@ -9,8 +21,70 @@
 
 シンプルなウェブベースのおみくじアプリケーションです。あなたの今日の運勢を占ってみましょう！🔮
 
-### 遊び方 🎮
+### 📸 スクリーンショット
+
+<div align="center">
+
+![App Screenshot](https://github.com/user-attachments/assets/fc8363f1-3a9f-4684-9b5d-b000a0a9a788)
+
+</div>
+
+### 🎮 遊び方
 
 1️⃣ このリポジトリをクローンまたはダウンロードします。 💻
 2️⃣ `index.html`ファイルをウェブブラウザで開きます。 🌐
-3️⃣ 「おみくじを引く」ボタンをクリックすると、今日の運勢が表示されます。 ✨
\ No newline at end of file
+3️⃣ 「おみくじを引く」ボタンをクリックすると、今日の運勢が表示されます。 ✨
+
+### 🛠️ 技術仕様
+
+- **フロントエンド**: HTML5, CSS3, Vanilla JavaScript
+- **ブラウザ要件**: モダンブラウザ（Chrome, Firefox, Safari, Edge）
+- **依存関係**: なし
+
+### 📁 プロジェクト構造
+
+```
+├── index.html              # メインHTMLファイル
+├── style.css               # スタイルシート
+├── script.js               # JavaScript処理
+├── .github/
+│   └── workflows/
+│       └── sync-to-report.yml  # 日報同期ワークフロー
+└── README.md               # このファイル
+```
+
+### 🚀 クイックスタート
+
+```bash
+# リポジトリをクローン
+git clone https://github.com/your-username/daily-report-hub_sample1.git
+
+# ディレクトリに移動
+cd daily-report-hub_sample1
+
+# ブラウザでindex.htmlを開く
+open index.html  # macOS
+start index.html # Windows
+```
+
+### 📋 機能一覧
+
+- ✨ ランダムなおみくじ結果の表示
+- 🎨 レスポンシブデザイン
+- ⚡ 高速な動作（依存関係なし）
+- 📱 モバイル対応
+
+### 🤝 コントリビューション
+
+プロジェクトへの貢献を歓迎します！詳細は [CONTRIBUTING.md](./CONTRIBUTING.md) をご覧ください。
+
+### 📝 変更履歴
+
+プロジェクトの変更履歴は [CHANGELOG.md](./CHANGELOG.md) で確認できます。
+
+### 🔗 関連リンク
+
+- [日報ハブリポジトリ](https://github.com/Sunwood-ai-labs/daily-report-hub)
+- [GitHub Actions ワークフロー](./.github/workflows/sync-to-report.yml)
+- [コントリビューションガイド](./CONTRIBUTING.md)
+- [変更履歴](./CHANGELOG.md)
\ No newline at end of file
diff --git a/index.html b/index.html
index 5d6aa93..e7b086f 100644
--- a/index.html
+++ b/index.html
@@ -1,17 +1,35 @@
 <!DOCTYPE html>
 <html lang="ja">
 <head>
+    <!-- 基本的なメタ情報 -->
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
-    <title>おみくじアプリ</title>
+    <meta name="description" content="シンプルなウェブベースのおみくじアプリケーション">
+    <meta name="keywords" content="おみくじ, 占い, ウェブアプリ">
+    <meta name="author" content="daily-report-hub_sample1">
+    
+    <title>おみくじアプリ ⛩️</title>
+    
+    <!-- スタイルシート -->
     <link rel="stylesheet" href="style.css">
+    
+    <!-- ファビコン（将来的に追加予定） -->
+    <!-- <link rel="icon" type="image/x-icon" href="/favicon.ico"> -->
 </head>
 <body>
+    <!-- メインコンテナ -->
     <div class="container">
-        <h1>おみくじ</h1>
-        <button id="draw-button">おみくじを引く</button>
-        <p id="result"></p>
+        <!-- アプリタイトル -->
+        <h1>おみくじ ⛩️</h1>
+        
+        <!-- おみくじを引くボタン -->
+        <button id="draw-button" aria-label="おみくじを引く">おみくじを引く</button>
+        
+        <!-- 結果表示エリア -->
+        <p id="result" aria-live="polite" role="status"></p>
     </div>
+    
+    <!-- JavaScript -->
     <script src="script.js"></script>
 </body>
 </html>
diff --git a/script.js b/script.js
index 4259f77..ceaa046 100644
--- a/script.js
+++ b/script.js
@@ -1,9 +1,26 @@
+/**
+ * おみくじアプリのメイン処理
+ * シンプルなランダム選択によるおみくじ機能を提供
+ */
+
+// DOM要素の取得
 const drawButton = document.getElementById('draw-button');
 const result = document.getElementById('result');
 
+// おみくじの結果配列（大吉から大凶まで6段階）
 const fortunes = ['大吉', '中吉', '小吉', '吉', '凶', '大凶'];
 
+/**
+ * おみくじを引く処理
+ * ボタンクリック時にランダムな結果を表示
+ */
 drawButton.addEventListener('click', () => {
+    // 0から配列の長さ-1までのランダムな整数を生成
     const randomIndex = Math.floor(Math.random() * fortunes.length);
+    
+    // 結果を画面に表示
     result.textContent = fortunes[randomIndex];
+    
+    // 結果に応じてスタイルを変更（視覚的フィードバック）
+    result.className = `fortune-${randomIndex}`;
 });
diff --git a/style.css b/style.css
index c90ae90..5023f7d 100644
--- a/style.css
+++ b/style.css
@@ -1,38 +1,66 @@
+/**
+ * おみくじアプリのスタイルシート
+ * シンプルで使いやすいデザインを提供
+ */
+
+/* 基本的なページレイアウト */
 body {
-    font-family: sans-serif;
+    font-family: 'Hiragino Sans', 'Yu Gothic', 'Meiryo', sans-serif;
     display: flex;
     justify-content: center;
     align-items: center;
     height: 100vh;
     margin: 0;
-    background-color: #f0f0f0;
+    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
+    color: #333;
 }
 
+/* メインコンテナ */
 .container {
     text-align: center;
     background-color: white;
     padding: 2rem;
-    border-radius: 10px;
-    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
+    border-radius: 15px;
+    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
+    backdrop-filter: blur(10px);
+    border: 1px solid rgba(255, 255, 255, 0.2);
+    max-width: 400px;
+    width: 90%;
 }
 
+/* タイトルスタイル */
 h1 {
     margin-top: 0;
+    color: #333;
+    font-size: 2.5rem;
+    margin-bottom: 1.5rem;
+    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
 }
 
+/* おみくじボタン */
 button {
-    padding: 10px 20px;
-    font-size: 1rem;
-    background-color: #007bff;
+    padding: 15px 30px;
+    font-size: 1.2rem;
+    background: linear-gradient(45deg, #007bff, #0056b3);
     color: white;
     border: none;
-    border-radius: 5px;
+    border-radius: 25px;
     cursor: pointer;
-    transition: background-color 0.3s;
+    transition: all 0.3s ease;
+    box-shadow: 0 4px 15px rgba(0, 123, 255, 0.3);
+    font-weight: bold;
 }
 
+/* ボタンホバー効果 */
 button:hover {
-    background-color: #0056b3;
+    background: linear-gradient(45deg, #0056b3, #004085);
+    transform: translateY(-2px);
+    box-shadow: 0 6px 20px rgba(0, 123, 255, 0.4);
+}
+
+/* ボタンアクティブ状態 */
+button:active {
+    transform: translateY(0);
 }
 
 #result {
@@ -40,4 +68,39 @@ button:hover {
     font-weight: bold;
     margin-top: 1rem;
     min-height: 3rem;
+    transition: all 0.3s ease;
+    border-radius: 8px;
+    padding: 1rem;
+}
+
+/* おみくじ結果に応じた色分け */
+.fortune-0 { /* 大吉 */
+    background-color: #ffeb3b;
+    color: #d32f2f;
+    box-shadow: 0 0 20px rgba(255, 235, 59, 0.5);
+}
+
+.fortune-1 { /* 中吉 */
+    background-color: #4caf50;
+    color: white;
+}
+
+.fortune-2 { /* 小吉 */
+    background-color: #8bc34a;
+    color: white;
+}
+
+.fortune-3 { /* 吉 */
+    background-color: #03a9f4;
+    color: white;
+}
+
+.fortune-4 { /* 凶 */
+    background-color: #ff9800;
+    color: white;
+}
+
+.fortune-5 { /* 大凶 */
+    background-color: #f44336;
+    color: white;
 }
```
