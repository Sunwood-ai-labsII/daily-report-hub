# 🔄 Latest Code Changes

```diff
diff --git a/.github/scripts/README.md b/.github/scripts/README.md
deleted file mode 100644
index c7e07f4..0000000
--- a/.github/scripts/README.md
+++ /dev/null
@@ -1,141 +0,0 @@
-# GitHub Actions Scripts
-
-このディレクトリには、Daily Report Hub同期ワークフローで使用されるスクリプトが含まれています。
-
-## スクリプト一覧
-
-### 1. `calculate-week-info.sh`
-週情報を計算し、環境変数を設定します。
-
-**使用方法:**
-```bash
-./calculate-week-info.sh [WEEK_START_DAY]
-```
-
-**パラメータ:**
-- `WEEK_START_DAY`: 週の開始日 (0=日曜日, 1=月曜日, ..., 6=土曜日)
-
-**出力環境変数:**
-- `REPO_NAME`: リポジトリ名
-- `DATE`: 現在の日付 (YYYY-MM-DD)
-- `YEAR`: 現在の年
-- `WEEK_FOLDER`: 週フォルダ名
-- `WEEK_START_DATE`: 週の開始日
-- `WEEK_END_DATE`: 週の終了日
-- `WEEK_NUMBER`: 週番号
-
-### 2. `analyze-git-activity.sh`
-Gitの活動を分析し、生データファイルを生成します。
-
-**生成ファイル:**
-- `daily_commits_raw.txt`: その日のコミット一覧
-- `daily_cumulative_diff_raw.txt`: その日の累積差分
-- `daily_diff_stats_raw.txt`: その日の統計情報
-- `daily_code_diff_raw.txt`: その日のコード差分
-- `latest_diff_raw.txt`: 最新の差分
-- `latest_code_diff_raw.txt`: 最新のコード差分
-
-### 3. `generate-markdown-reports.sh`
-生データからMarkdownレポートを生成します。
-
-**生成ファイル:**
-- `daily_commits.md`: コミット詳細レポート
-- `daily_cumulative_diff.md`: ファイル変更レポート
-- `daily_diff_stats.md`: 統計レポート
-- `daily_code_diff.md`: コード差分レポート
-- `latest_diff.md`: 最新変更レポート
-- `latest_code_diff.md`: 最新コード差分レポート
-- `daily_summary.md`: 日次サマリーレポート
-
-### 4. `create-docusaurus-structure.sh`
-Docusaurusの構造と`_category_.json`ファイルを作成します。
-
-**必要な環境変数:**
-- `REPO_NAME`, `DATE`, `YEAR`, `WEEK_FOLDER`, `WEEK_NUMBER`, `WEEK_START_DATE`, `WEEK_END_DATE`
-
-**出力環境変数:**
-- `TARGET_DIR`: ターゲットディレクトリのパス
-
-### 5. `sync-to-hub.sh`
-レポートハブにファイルを同期します。
-
-**必要な環境変数:**
-- `GITHUB_TOKEN`: GitHubアクセストークン
-- `REPORT_HUB_REPO`: レポートハブのリポジトリ
-- `TARGET_DIR`: ターゲットディレクトリ
-- その他の週情報変数
-
-## 週の開始日設定
-
-ワークフローファイルの`env.WEEK_START_DAY`を変更することで、週の開始日を制御できます：
-
-```yaml
-env:
-  WEEK_START_DAY: 1  # 0=日曜日, 1=月曜日, 2=火曜日, etc.
-```
-
-## プルリクエストフロー設定
-
-v2.0では、プルリクエストベースのフローと自動承認機能が追加されました：
-
-```yaml
-env:
-  WEEK_START_DAY: 1     # 週の開始日
-  AUTO_APPROVE: true    # プルリクエストの自動承認
-  AUTO_MERGE: true      # プルリクエストの自動マージ
-  CREATE_PR: true       # プルリクエストを作成するか直接プッシュするか
-```
-
-### 設定オプション
-
-| 設定 | 説明 | デフォルト |
-|------|------|------------|
-| `CREATE_PR` | `true`: プルリクエストを作成<br>`false`: 直接プッシュ | `true` |
-| `AUTO_APPROVE` | `true`: プルリクエストを自動承認<br>`false`: 手動承認が必要 | `false` |
-| `AUTO_MERGE` | `true`: 承認後に自動マージ<br>`false`: 手動マージが必要 | `false` |
-
-### フロー例
-
-1. **完全自動化**: `CREATE_PR=true`, `AUTO_APPROVE=true`, `AUTO_MERGE=true`
-   - プルリクエスト作成 → 自動承認 → 自動マージ
-
-2. **承認のみ手動**: `CREATE_PR=true`, `AUTO_APPROVE=false`, `AUTO_MERGE=true`
-   - プルリクエスト作成 → 手動承認 → 自動マージ
-
-3. **完全手動**: `CREATE_PR=true`, `AUTO_APPROVE=false`, `AUTO_MERGE=false`
-   - プルリクエスト作成 → 手動承認 → 手動マージ
-
-4. **直接プッシュ**: `CREATE_PR=false`
-   - 従来通りの直接プッシュ（v1.4と同じ動作）
-
-## ワークフローファイル
-
-2つのバージョンが利用可能です：
-
-- `sync-to-report.yml`: cURLベースの実装
-- `sync-to-report-gh.yml`: GitHub CLI使用版（推奨）
-
-## フォルダ構造
-
-生成されるフォルダ構造：
-```
-docs/docs/activities/
-├── _category_.json
-└── 2025/
-    ├── _category_.json
-    └── week-06_2025-08-04_to_2025-08-10/
-        ├── _category_.json
-        └── 2025-08-05/
-            ├── _category_.json
-            └── your-repo/
-                ├── _category_.json
-                ├── daily_summary.md
-                ├── daily_commits.md
-                ├── daily_cumulative_diff.md
-                ├── daily_diff_stats.md
-                ├── daily_code_diff.md
-                ├── latest_diff.md
-                ├── latest_code_diff.md
-                ├── README.md
-                └── metadata.json
-```
\ No newline at end of file
diff --git a/.github/scripts/analyze-git-activity.sh b/.github/scripts/analyze-git-activity.sh
deleted file mode 100644
index af185ef..0000000
--- a/.github/scripts/analyze-git-activity.sh
+++ /dev/null
@@ -1,59 +0,0 @@
-#!/bin/bash
-
-# Git活動を分析してMarkdownファイルを生成するスクリプト
-
-set -e
-
-DATE=${DATE:-$(date '+%Y-%m-%d')}
-
-echo "🔍 Fetching all commits for $DATE..."
-
-# その日の全コミット履歴を取得（時刻順）
-git log --since="$DATE 00:00:00" --until="$DATE 23:59:59" \
-  --pretty=format:"%h|%s|%an|%ad" --date=format:'%H:%M:%S' \
-  --reverse > daily_commits_raw.txt
-
-# コミット数をカウント
-COMMIT_COUNT=$(wc -l < daily_commits_raw.txt)
-echo "📊 Found $COMMIT_COUNT commits for today"
-
-# その日の全ての差分を統合（安全な方法で）
-if [ $COMMIT_COUNT -gt 0 ]; then
-  FIRST_COMMIT_TODAY=$(git log --since="$DATE 00:00:00" --pretty=format:"%H" --reverse | head -1)
-  LAST_COMMIT_TODAY=$(git log --since="$DATE 00:00:00" --pretty=format:"%H" | head -1)
-  
-  echo "First commit: $FIRST_COMMIT_TODAY"
-  echo "Last commit: $LAST_COMMIT_TODAY"
-  
-  # 親コミットが存在するかチェック
-  if git rev-parse --verify "$FIRST_COMMIT_TODAY^" >/dev/null 2>&1; then
-    # 親コミットが存在する場合
-    PARENT_OF_FIRST=$(git rev-parse $FIRST_COMMIT_TODAY^)
-    git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY --name-status > daily_cumulative_diff_raw.txt 2>/dev/null || echo "No diff available" > daily_cumulative_diff_raw.txt
-    git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY --stat > daily_diff_stats_raw.txt 2>/dev/null || echo "No stats available" > daily_diff_stats_raw.txt
-    # コードの詳細差分を取得
-    git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY > daily_code_diff_raw.txt 2>/dev/null || echo "No code diff available" > daily_code_diff_raw.txt
-  else
-    # 初回コミットの場合（親が存在しない）
-    echo "Initial commit detected - showing all files as new"
-    git diff --name-status 4b825dc642cb6eb9a060e54bf8d69288fbee4904..$LAST_COMMIT_TODAY > daily_cumulative_diff_raw.txt 2>/dev/null || \
-    git ls-tree --name-status $LAST_COMMIT_TODAY > daily_cumulative_diff_raw.txt 2>/dev/null || \
-    echo "A\t(all files added in initial commit)" > daily_cumulative_diff_raw.txt
-    
-    git diff --stat 4b825dc642cb6eb9a060e54bf8d69288fbee4904..$LAST_COMMIT_TODAY > daily_diff_stats_raw.txt 2>/dev/null || \
-    echo "Initial commit - all files added" > daily_diff_stats_raw.txt
-    
-    # 初回コミットのコード内容
-    git show $LAST_COMMIT_TODAY > daily_code_diff_raw.txt 2>/dev/null || echo "No code diff available" > daily_code_diff_raw.txt
-  fi
-else
-  echo "No commits found for today" > daily_cumulative_diff_raw.txt
-  echo "No commits found for today" > daily_diff_stats_raw.txt
-  echo "No commits found for today" > daily_code_diff_raw.txt
-fi
-
-# 最新コミットの個別差分
-git diff HEAD~1 --name-status > latest_diff_raw.txt 2>/dev/null || echo "No recent diff available" > latest_diff_raw.txt
-git diff HEAD~1 > latest_code_diff_raw.txt 2>/dev/null || echo "No recent code diff available" > latest_code_diff_raw.txt
-
-echo "✅ Git activity analysis complete!"
\ No newline at end of file
diff --git a/.github/scripts/calculate-week-info.sh b/.github/scripts/calculate-week-info.sh
deleted file mode 100644
index 0d35476..0000000
--- a/.github/scripts/calculate-week-info.sh
+++ /dev/null
@@ -1,44 +0,0 @@
-#!/bin/bash
-
-# 週情報を計算するスクリプト
-# 使用方法: ./calculate-week-info.sh [WEEK_START_DAY]
-
-set -e
-
-WEEK_START_DAY=${1:-1}  # デフォルトは月曜日
-
-# リポジトリ名と日付を取得
-REPO_NAME=$(basename $GITHUB_REPOSITORY)
-DATE=$(date '+%Y-%m-%d')
-YEAR=$(date '+%Y')
-
-# 週の計算（週の開始日を考慮）
-CURRENT_DAY_OF_WEEK=$(date '+%w')  # 0=日曜日
-DAYS_SINCE_WEEK_START=$(( (CURRENT_DAY_OF_WEEK - WEEK_START_DAY + 7) % 7 ))
-WEEK_START_DATE=$(date -d "$DATE -$DAYS_SINCE_WEEK_START days" '+%Y-%m-%d')
-WEEK_END_DATE=$(date -d "$WEEK_START_DATE +6 days" '+%Y-%m-%d')
-
-# 週番号を計算（年の最初の週の開始日から数える）
-YEAR_START=$(date -d "$YEAR-01-01" '+%Y-%m-%d')
-YEAR_START_DAY_OF_WEEK=$(date -d "$YEAR_START" '+%w')
-FIRST_WEEK_START_OFFSET=$(( (WEEK_START_DAY - YEAR_START_DAY_OF_WEEK + 7) % 7 ))
-FIRST_WEEK_START=$(date -d "$YEAR_START +$FIRST_WEEK_START_OFFSET days" '+%Y-%m-%d')
-
-# 週番号を計算
-DAYS_DIFF=$(( ($(date -d "$WEEK_START_DATE" '+%s') - $(date -d "$FIRST_WEEK_START" '+%s')) / 86400 ))
-WEEK_NUMBER=$(( DAYS_DIFF / 7 + 1 ))
-
-# 週フォルダ名を作成
-WEEK_FOLDER=$(printf "week-%02d_%s_to_%s" $WEEK_NUMBER $WEEK_START_DATE $WEEK_END_DATE)
-
-# 環境変数に出力
-echo "REPO_NAME=$REPO_NAME" >> $GITHUB_ENV
-echo "DATE=$DATE" >> $GITHUB_ENV
-echo "YEAR=$YEAR" >> $GITHUB_ENV
-echo "WEEK_FOLDER=$WEEK_FOLDER" >> $GITHUB_ENV
-echo "WEEK_START_DATE=$WEEK_START_DATE" >> $GITHUB_ENV
-echo "WEEK_END_DATE=$WEEK_END_DATE" >> $GITHUB_ENV
-echo "WEEK_NUMBER=$WEEK_NUMBER" >> $GITHUB_ENV
-
-echo "📅 Date: $DATE"
-echo "📅 Week: $WEEK_FOLDER"
\ No newline at end of file
diff --git a/.github/scripts/create-docusaurus-structure.sh b/.github/scripts/create-docusaurus-structure.sh
deleted file mode 100644
index 5f4d9bf..0000000
--- a/.github/scripts/create-docusaurus-structure.sh
+++ /dev/null
@@ -1,111 +0,0 @@
-#!/bin/bash
-
-# Docusaurusの構造と_category_.jsonファイルを作成するスクリプト
-
-set -e
-
-# 必要な環境変数をチェック
-: ${REPO_NAME:?}
-: ${DATE:?}
-: ${YEAR:?}
-: ${WEEK_FOLDER:?}
-: ${WEEK_NUMBER:?}
-: ${WEEK_START_DATE:?}
-: ${WEEK_END_DATE:?}
-
-REPORT_HUB_DIR="daily-report-hub"
-ACTIVITIES_DIR="$REPORT_HUB_DIR/docs/docs/activities"
-YEAR_DIR="$ACTIVITIES_DIR/$YEAR"
-WEEK_DIR="$YEAR_DIR/$WEEK_FOLDER"
-DATE_DIR="$WEEK_DIR/$DATE"
-TARGET_DIR="$DATE_DIR/$REPO_NAME"
-
-# ディレクトリを作成
-mkdir -p "$TARGET_DIR"
-
-# Docusaurus _category_.json ファイルを作成
-
-# 1. activities ディレクトリの _category_.json
-if [ ! -f "$ACTIVITIES_DIR/_category_.json" ]; then
-  cat > "$ACTIVITIES_DIR/_category_.json" << 'EOF'
-{
-  "label": "📊 Activities",
-  "position": 1,
-  "link": {
-    "type": "generated-index",
-    "description": "Daily development activities and reports"
-  }
-}
-EOF
-fi
-
-# 2. 年ディレクトリの _category_.json
-if [ ! -f "$YEAR_DIR/_category_.json" ]; then
-  cat > "$YEAR_DIR/_category_.json" << EOF
-{
-  "label": "$YEAR",
-  "position": 1,
-  "link": {
-    "type": "generated-index",
-    "description": "Activities for year $YEAR"
-  }
-}
-EOF
-fi
-
-# 3. 週ディレクトリの _category_.json
-if [ ! -f "$WEEK_DIR/_category_.json" ]; then
-  WEEK_LABEL="Week $WEEK_NUMBER ($WEEK_START_DATE to $WEEK_END_DATE)"
-  cat > "$WEEK_DIR/_category_.json" << EOF
-{
-  "label": "$WEEK_LABEL",
-  "position": $WEEK_NUMBER,
-  "link": {
-    "type": "generated-index",
-    "description": "Activities for $WEEK_LABEL"
-  }
-}
-EOF
-fi
-
-# 4. 日付ディレクトリの _category_.json
-if [ ! -f "$DATE_DIR/_category_.json" ]; then
-  DATE_LABEL="📅 $DATE"
-  # 日付から位置を計算（月の日にち）
-  DATE_POSITION=$(date -d "$DATE" '+%d' | sed 's/^0*//')
-  cat > "$DATE_DIR/_category_.json" << EOF
-{
-  "label": "$DATE_LABEL",
-  "position": $DATE_POSITION,
-  "link": {
-    "type": "generated-index",
-    "description": "Activities for $DATE"
-  }
-}
-EOF
-fi
-
-# 5. リポジトリディレクトリの _category_.json
-if [ ! -f "$TARGET_DIR/_category_.json" ]; then
-  cat > "$TARGET_DIR/_category_.json" << EOF
-{
-  "label": "🔧 $REPO_NAME",
-  "position": 1,
-  "link": {
-    "type": "generated-index",
-    "description": "Repository: $GITHUB_REPOSITORY"
-  }
-}
-EOF
-fi
-
-echo "📁 Created directory structure:"
-echo "  📂 $YEAR_DIR"
-echo "    📂 $WEEK_FOLDER"
-echo "      📂 $DATE"
-echo "        📂 $REPO_NAME"
-echo ""
-echo "📄 Created _category_.json files for Docusaurus navigation"
-
-# TARGET_DIRを環境変数として出力
-echo "TARGET_DIR=$TARGET_DIR" >> $GITHUB_ENV
\ No newline at end of file
diff --git a/.github/scripts/generate-markdown-reports.sh b/.github/scripts/generate-markdown-reports.sh
deleted file mode 100644
index b5818cd..0000000
--- a/.github/scripts/generate-markdown-reports.sh
+++ /dev/null
@@ -1,201 +0,0 @@
-#!/bin/bash
-
-# Markdownレポートを生成するスクリプト（修正版）
-
-set -e
-
-# 各行に4スペースのインデントを追加する関数
-add_indent() {
-  sed 's/^/    /' "$1"
-}
-
-# ファイル変更のステータスアイコンを取得する関数
-get_status_icon() {
-  case $1 in
-    A) echo "- 🆕 **Added:** \`$2\`" ;;
-    M) echo "- ✏️ **Modified:** \`$2\`" ;;
-    D) echo "- 🗑️ **Deleted:** \`$2\`" ;;
-    R*) echo "- 🔄 **Renamed:** \`$2\`" ;;
-    *) echo "- 📝 **$1:** \`$2\`" ;;
-  esac
-}
-
-# コードブロック内容をサニタイズする関数
-sanitize_code_block() {
-  # バッククォート3つをエスケープ
-  sed 's/```/`\`\`/g' "$1"
-}
-
-# コミット詳細をMarkdown形式で作成（差分付き）
-{
-  echo "# 📝 Daily Commits"
-  echo ""
-  if [ -s daily_commits_raw.txt ]; then
-    while IFS='|' read -r hash subject author time; do
-      echo "## ⏰ $time - \`$hash\`"
-      echo "**$subject**"
-      echo "*by $author*"
-      echo ""
-      
-      # 各コミットの変更ファイル一覧を表示
-      echo "### 📋 Changed Files"
-      echo "\`\`\`bash"
-      git show --name-status $hash 2>/dev/null | grep -E '^[AMDRC]' || echo "No file changes"
-      echo "\`\`\`"
-      echo ""
-      
-      # 各コミットの統計情報を表示
-      echo "### 📊 Statistics"
-      echo "\`\`\`bash"
-      git show --stat $hash 2>/dev/null | tail -n +2 || echo "No statistics available"
-      echo "\`\`\`"
-      echo ""
-      
-      # 各コミットのコード差分を表示（最初の100行まで、サニタイズ済み）
-      echo "### 💻 Code Changes"
-      echo "\`\`\`diff"
-      git show $hash --pretty=format:"" 2>/dev/null | head -100 | sed 's/```/`\`\`/g' || echo "No code changes available"
-      echo "\`\`\`"
-      echo ""
-      echo "---"
-      echo ""
-    done < daily_commits_raw.txt
-  else
-    echo "*No commits found for today.*"
-  fi
-} > daily_commits.md
-
-# 累積差分をMarkdown形式で作成
-{
-  echo "# 📋 Daily File Changes"
-  echo ""
-  if [ -s daily_cumulative_diff_raw.txt ]; then
-    while read -r line; do
-      if [ ! -z "$line" ]; then
-        status=$(echo "$line" | cut -f1)
-        file=$(echo "$line" | cut -f2)
-        get_status_icon "$status" "$file"
-      fi
-    done < daily_cumulative_diff_raw.txt
-  else
-    echo "*No file changes today.*"
-  fi
-} > daily_cumulative_diff.md
-
-# 統計をMarkdown形式で作成
-{
-  echo "# 📈 Daily Statistics"
-  echo ""
-  echo "\`\`\`diff"
-  # バッククォートをエスケープして出力
-  cat daily_diff_stats_raw.txt | sed 's/```/`\`\`/g'
-  echo "\`\`\`"
-} > daily_diff_stats.md
-
-# コード差分をMarkdown形式で作成（サニタイズ済み）
-{
-  echo "# 💻 Daily Code Changes"
-  echo ""
-  echo "## Full Diff"
-  echo ""
-  echo "\`\`\`diff"
-  # バッククォートをエスケープして出力
-  cat daily_code_diff_raw.txt | sed 's/```/`\`\`/g'
-  echo "\`\`\`"
-} > daily_code_diff.md
-
-# 最新差分をMarkdown形式で作成
-{
-  echo "# 🔄 Latest Changes (File List)"
-  echo ""
-  if [ -s latest_diff_raw.txt ]; then
-    while read -r line; do
-      if [ ! -z "$line" ]; then
-        status=$(echo "$line" | cut -f1)
-        file=$(echo "$line" | cut -f2)
-        get_status_icon "$status" "$file"
-      fi
-    done < latest_diff_raw.txt
-  else
-    echo "*No recent changes.*"
-  fi
-} > latest_diff.md
-
-# 最新コード差分をMarkdown形式で作成（修正版）
-{
-  echo "# 🔄 Latest Code Changes"
-  echo ""
-  echo "\`\`\`diff"
-  # バッククォートをエスケープして出力
-  cat latest_code_diff_raw.txt | sed 's/```/`\`\`/g'
-  echo "\`\`\`"
-} > latest_code_diff.md
-
-# 詳細なアクティビティサマリーをMarkdown形式で作成
-if [ -s daily_commits_raw.txt ]; then
-  FIRST_COMMIT_TIME=$(head -1 daily_commits_raw.txt | cut -d'|' -f4)
-  LAST_COMMIT_TIME=$(tail -1 daily_commits_raw.txt | cut -d'|' -f4)
-  FILES_CHANGED=$(grep -c '^' daily_cumulative_diff_raw.txt 2>/dev/null || echo "0")
-else
-  FIRST_COMMIT_TIME="N/A"
-  LAST_COMMIT_TIME="N/A" 
-  FILES_CHANGED=0
-fi
-
-# メインサマリーファイルを作成
-{
-  echo "# 📅 Daily Activity Report"
-  echo ""
-  echo "## 📊 Summary"
-  echo "| Item | Value |"
-  echo "|------|-------|"
-  echo "| Repository | \`$GITHUB_REPOSITORY\` |"
-  echo "| Date | $DATE |"
-  echo "| Total Commits | **$(wc -l < daily_commits_raw.txt)** |"
-  echo "| Files Changed | **$FILES_CHANGED** |"
-  echo "| First Activity | $FIRST_COMMIT_TIME |"
-  echo "| Last Activity | $LAST_COMMIT_TIME |"
-  echo "| Sync Time | $(date '+%H:%M:%S') |"
-  echo ""
-  
-  if [ -s daily_commits_raw.txt ]; then
-    echo "## 📝 Commit Details"
-    echo ""
-    while IFS='|' read -r hash subject author time; do
-      echo "### ⏰ $time - \`$hash\`"
-      echo "**$subject**"
-      echo "*by $author*"
-      echo ""
-    done < daily_commits_raw.txt
-    
-    echo "## 📈 File Changes Statistics"
-    echo ""
-    echo "\`\`\`diff"
-    # バッククォートをエスケープして出力
-    cat daily_diff_stats_raw.txt | sed 's/```/`\`\`/g'
-    echo "\`\`\`"
-    echo ""
-    
-    echo "## 📋 Changed Files List"
-    echo ""
-    while read -r line; do
-      if [ ! -z "$line" ]; then
-        status=$(echo "$line" | cut -f1)
-        file=$(echo "$line" | cut -f2)
-        get_status_icon "$status" "$file"
-      fi
-    done < daily_cumulative_diff_raw.txt
-    echo ""
-    
-  else
-    echo "## 📝 Commit Details"
-    echo ""
-    echo "*No commits found for today.*"
-    echo ""
-  fi
-  
-  echo "---"
-  echo "*Generated by GitHub Actions at $(date '+%Y-%m-%d %H:%M:%S')*"
-} > daily_summary.md
-
-echo "✅ Markdown reports generated successfully!"
diff --git a/.github/scripts/sync-to-hub-gh.sh b/.github/scripts/sync-to-hub-gh.sh
deleted file mode 100644
index 9ba5232..0000000
--- a/.github/scripts/sync-to-hub-gh.sh
+++ /dev/null
@@ -1,182 +0,0 @@
-#!/bin/bash
-
-# YUKIHIKOアカウントでPR作成＆自動承認するスクリプト
-
-set -e
-
-# 必要な環境変数をチェック
-: ${GITHUB_TOKEN:?}
-: ${YUKIHIKO_TOKEN:?}  # YUKIHIKOのトークン
-: ${REPORT_HUB_REPO:?}
-: ${TARGET_DIR:?}
-: ${REPO_NAME:?}
-: ${DATE:?}
-: ${WEEK_NUMBER:?}
-
-echo "🔥 YUKIHIKOアカウントでPR作成モード開始！"
-
-# ファイルコピー処理
-cp README.md "$TARGET_DIR/" 2>/dev/null || echo "# $REPO_NAME" > "$TARGET_DIR/README.md"
-cp daily_commits.md "$TARGET_DIR/"
-cp daily_cumulative_diff.md "$TARGET_DIR/"
-cp daily_diff_stats.md "$TARGET_DIR/"
-cp daily_code_diff.md "$TARGET_DIR/"
-cp latest_diff.md "$TARGET_DIR/"
-cp latest_code_diff.md "$TARGET_DIR/"
-cp daily_summary.md "$TARGET_DIR/"
-
-# メタデータ作成
-COMMIT_COUNT=$(wc -l < daily_commits_raw.txt)
-FILES_CHANGED=$(grep -c '^' daily_cumulative_diff_raw.txt 2>/dev/null || echo "0")
-
-cat > "$TARGET_DIR/metadata.json" << EOF
-{
-  "repository": "$GITHUB_REPOSITORY",
-  "date": "$DATE",
-  "week_folder": "$WEEK_FOLDER",
-  "week_number": $WEEK_NUMBER,
-  "week_start_date": "$WEEK_START_DATE",
-  "week_end_date": "$WEEK_END_DATE",
-  "branch": "$GITHUB_REF_NAME",
-  "latest_commit_sha": "$GITHUB_SHA",
-  "sync_timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
-  "workflow_run": "$GITHUB_RUN_ID",
-  "daily_commit_count": $COMMIT_COUNT,
-  "daily_files_changed": $FILES_CHANGED,
-  "has_activity": $([ $COMMIT_COUNT -gt 0 ] && echo "true" || echo "false"),
-  "pr_creator": "yukihiko",
-  "auto_approved": true,
-  "files": {
-    "readme": "README.md",
-    "summary": "daily_summary.md",
-    "commits": "daily_commits.md",
-    "file_changes": "daily_cumulative_diff.md",
-    "stats": "daily_diff_stats.md",
-    "code_diff": "daily_code_diff.md",
-    "latest_diff": "latest_diff.md",
-    "latest_code_diff": "latest_code_diff.md"
-  }
-}
-EOF
-
-cd daily-report-hub
-
-# 最新のmainブランチを取得
-git fetch origin main
-git checkout main
-git pull origin main
-
-# 変更をステージング
-git add .
-
-if git diff --staged --quiet; then
-  echo "📝 変更がありません"
-  exit 0
-fi
-
-COMMIT_MESSAGE="📊 週次同期: $REPO_NAME ($DATE) - 第${WEEK_NUMBER}週 - ${COMMIT_COUNT}件のコミット"
-BRANCH_NAME="sync/$REPO_NAME-$DATE"
-
-# 既存ブランチとPRをクリーンアップ
-git branch -D "$BRANCH_NAME" 2>/dev/null || true
-git push origin --delete "$BRANCH_NAME" 2>/dev/null || true
-
-# 🔥 重要：YUKIHIKOアカウントでコミット作成
-echo "👤 YUKIHIKOアカウントでコミット作成中..."
-git config user.name "Yukihiko Kondo"
-git config user.email "yukihiko.fuyuki@example.com"
-
-# ブランチ作成・コミット・プッシュ（YUKIHIKOトークンで）
-git checkout -b "$BRANCH_NAME"
-git commit -m "$COMMIT_MESSAGE"
-
-# YUKIHIKOのトークンでプッシュ
-git remote set-url origin https://x-access-token:${YUKIHIKO_TOKEN}@github.com/${REPORT_HUB_REPO}.git
-git push origin "$BRANCH_NAME"
-
-# 日本語PR作成（YUKIHIKOトークンで）
-PR_BODY="## 📊 デイリーレポート同期
-
-**リポジトリ:** \`$GITHUB_REPOSITORY\`  
-**日付:** $DATE  
-**週:** 第${WEEK_NUMBER}週 ($WEEK_START_DATE ～ $WEEK_END_DATE)
-
-### 📈 アクティビティサマリー
-- **コミット数:** ${COMMIT_COUNT}件
-- **変更ファイル数:** ${FILES_CHANGED}件  
-- **同期時刻:** $(date '+%Y年%m月%d日 %H:%M:%S')
-
-### 📋 生成されたファイル
-- 📄 日次サマリーレポート
-- 📝 コミット詳細  
-- 📁 ファイル変更一覧
-- 💻 コード差分
-- 📊 統計情報
-
-### 🤖 自動化情報
-- **PR作成者:** YUKIHIKO (自動承認可能)
-- **データ作成者:** GitHub Actions
-- **承認者:** 手動 or 自動
-
----
-*GitHub Actions により自動生成（YUKIHIKO権限）*"
-
-echo "📝 YUKIHIKOアカウントでPR作成中..."
-
-# YUKIHIKOトークンでPR作成
-export GITHUB_TOKEN="$YUKIHIKO_TOKEN"
-PR_URL=$(gh pr create \
-  --title "$COMMIT_MESSAGE" \
-  --body "$PR_BODY" \
-  --base main \
-  --head "$BRANCH_NAME" \
-  --repo "$REPORT_HUB_REPO" 2>/dev/null || echo "")
-
-if [ -n "$PR_URL" ]; then
-  echo "✅ YUKIHIKOアカウントでPR作成完了: $PR_URL"
-  
-  PR_NUMBER=$(gh pr view "$PR_URL" --repo "$REPORT_HUB_REPO" --json number --jq '.number')
-  
-  # # CI完了待機
-  # echo "⏳ CI完了を待機中..."
-  # max_wait=300
-  # wait_time=0
-  # while [ $wait_time -lt $max_wait ]; do
-  #   CHECK_STATUS=$(gh pr view "$PR_NUMBER" --repo "$REPORT_HUB_REPO" --json statusCheckRollup --jq '.statusCheckRollup[-1].state' 2>/dev/null || echo "PENDING")
-    
-  #   if [ "$CHECK_STATUS" = "SUCCESS" ]; then
-  #     echo "✅ CI完了！"
-  #     break
-  #   elif [ "$CHECK_STATUS" = "FAILURE" ]; then
-  #     echo "❌ CI失敗"
-  #     exit 1
-  #   else
-  #     echo "⏳ CI実行中... (${wait_time}秒)"
-  #     sleep 10
-  #     wait_time=$((wait_time + 10))
-  #   fi
-  # done
-  
-  # 🔥 ここがポイント：元のトークンで承認
-  echo "👍 元のアカウントで承認実行中..."
-  export GITHUB_TOKEN="$GITHUB_TOKEN_ORIGINAL"  # 元のトークンに戻す
-  
-  if gh pr review "$PR_NUMBER" --approve --body "✅ 自動承認：データ同期完了" --repo "$REPORT_HUB_REPO" 2>/dev/null; then
-    echo "✅ 承認完了！"
-    
-    # 自動マージ実行
-    echo "🔀 自動マージ実行中..."
-    sleep 3
-    
-    if gh pr merge "$PR_NUMBER" --squash --delete-branch --repo "$REPORT_HUB_REPO" 2>/dev/null; then
-      echo "🎉 完全自動化成功！PRがマージされました！"
-    else
-      echo "⚠️ マージ失敗。手動マージが必要: $PR_URL"
-    fi
-  else
-    echo "⚠️ 承認失敗。手動承認が必要: $PR_URL"
-  fi
-else
-  echo "❌ PR作成失敗"
-  exit 1
-fi
diff --git a/.github/scripts/sync-to-hub.sh b/.github/scripts/sync-to-hub.sh
deleted file mode 100644
index 0a7d604..0000000
--- a/.github/scripts/sync-to-hub.sh
+++ /dev/null
@@ -1,184 +0,0 @@
-#!/bin/bash
-
-# レポートハブに同期するスクリプト（プルリクエストフロー対応）
-
-set -e
-
-# 必要な環境変数をチェック
-: ${GITHUB_TOKEN:?}
-: ${REPORT_HUB_REPO:?}
-: ${TARGET_DIR:?}
-: ${REPO_NAME:?}
-: ${DATE:?}
-: ${WEEK_NUMBER:?}
-
-# プルリクエストフロー設定（デフォルト値）
-CREATE_PR=${CREATE_PR:-true}
-AUTO_APPROVE=${AUTO_APPROVE:-false}
-AUTO_MERGE=${AUTO_MERGE:-false}
-
-# daily-report-hubは既にクローン済み
-
-# README.mdをコピー
-cp README.md "$TARGET_DIR/" 2>/dev/null || echo "# $REPO_NAME" > "$TARGET_DIR/README.md"
-
-# 当日のアクティビティファイルをコピー（全て.mdファイル）
-cp daily_commits.md "$TARGET_DIR/"
-cp daily_cumulative_diff.md "$TARGET_DIR/"
-cp daily_diff_stats.md "$TARGET_DIR/"
-cp daily_code_diff.md "$TARGET_DIR/"
-cp latest_diff.md "$TARGET_DIR/"
-cp latest_code_diff.md "$TARGET_DIR/"
-cp daily_summary.md "$TARGET_DIR/"
-
-# 詳細メタデータを作成
-COMMIT_COUNT=$(wc -l < daily_commits_raw.txt)
-FILES_CHANGED=$(grep -c '^' daily_cumulative_diff_raw.txt 2>/dev/null || echo "0")
-
-cat > "$TARGET_DIR/metadata.json" << EOF
-{
-  "repository": "$GITHUB_REPOSITORY",
-  "date": "$DATE",
-  "week_folder": "$WEEK_FOLDER",
-  "week_number": $WEEK_NUMBER,
-  "week_start_date": "$WEEK_START_DATE",
-  "week_end_date": "$WEEK_END_DATE",
-  "branch": "$GITHUB_REF_NAME",
-  "latest_commit_sha": "$GITHUB_SHA",
-  "sync_timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
-  "workflow_run": "$GITHUB_RUN_ID",
-  "daily_commit_count": $COMMIT_COUNT,
-  "daily_files_changed": $FILES_CHANGED,
-  "has_activity": $([ $COMMIT_COUNT -gt 0 ] && echo "true" || echo "false"),
-  "files": {
-    "readme": "README.md",
-    "summary": "daily_summary.md",
-    "commits": "daily_commits.md",
-    "file_changes": "daily_cumulative_diff.md",
-    "stats": "daily_diff_stats.md",
-    "code_diff": "daily_code_diff.md",
-    "latest_diff": "latest_diff.md",
-    "latest_code_diff": "latest_code_diff.md"
-  }
-}
-EOF
-
-# プルリクエストフローまたは直接プッシュ
-cd daily-report-hub
-git add .
-
-if git diff --staged --quiet; then
-  echo "No changes to commit"
-  exit 0
-fi
-
-COMMIT_MESSAGE="📊 Weekly sync: $REPO_NAME ($DATE) - Week $WEEK_NUMBER - $COMMIT_COUNT commits"
-
-if [ "$CREATE_PR" = "true" ]; then
-  # プルリクエストフロー
-  BRANCH_NAME="sync/$REPO_NAME-$DATE-$(date +%s)"
-  
-  echo "🔀 Creating pull request flow with branch: $BRANCH_NAME"
-  
-  # 新しいブランチを作成してチェックアウト
-  git checkout -b "$BRANCH_NAME"
-  
-  # コミットしてプッシュ
-  git commit -m "$COMMIT_MESSAGE"
-  git push origin "$BRANCH_NAME"
-  
-  # プルリクエストを作成
-  PR_BODY="## 📊 Daily Report Sync
-
-**Repository:** \`$GITHUB_REPOSITORY\`
-**Date:** $DATE
-**Week:** $WEEK_NUMBER ($WEEK_START_DATE to $WEEK_END_DATE)
-
-### 📈 Activity Summary
-- **Commits:** $COMMIT_COUNT
-- **Files Changed:** $FILES_CHANGED
-- **Sync Time:** $(date '+%Y-%m-%d %H:%M:%S')
-
-### 📋 Generated Files
-- Daily summary report
-- Commit details
-- File changes
-- Code differences
-- Statistics
-
----
-*Auto-generated by GitHub Actions*"
-
-  echo "📝 Creating pull request..."
-  PR_URL=$(curl -s -X POST \
-    -H "Authorization: token $GITHUB_TOKEN" \
-    -H "Accept: application/vnd.github.v3+json" \
-    "https://api.github.com/repos/$REPORT_HUB_REPO/pulls" \
-    -d "{
-      \"title\": \"$COMMIT_MESSAGE\",
-      \"body\": \"$PR_BODY\",
-      \"head\": \"$BRANCH_NAME\",
-      \"base\": \"main\"
-    }" | jq -r '.html_url // empty')
-  
-  if [ -n "$PR_URL" ]; then
-    echo "✅ Pull request created: $PR_URL"
-    
-    # プルリクエスト番号を取得
-    PR_NUMBER=$(echo "$PR_URL" | grep -o '[0-9]*$')
-    
-    # 自動承認が有効な場合
-    if [ "$AUTO_APPROVE" = "true" ]; then
-      echo "👍 Auto-approving pull request..."
-      curl -s -X POST \
-        -H "Authorization: token $GITHUB_TOKEN" \
-        -H "Accept: application/vnd.github.v3+json" \
-        "https://api.github.com/repos/$REPORT_HUB_REPO/pulls/$PR_NUMBER/reviews" \
-        -d '{"event": "APPROVE", "body": "✅ Auto-approved by GitHub Actions"}' > /dev/null
-      echo "✅ Pull request approved"
-    fi
-    
-    # 自動マージが有効な場合
-    if [ "$AUTO_MERGE" = "true" ]; then
-      echo "🔀 Auto-merging pull request..."
-      sleep 2  # APIの反映を待つ
-      MERGE_RESULT=$(curl -s -X PUT \
-        -H "Authorization: token $GITHUB_TOKEN" \
-        -H "Accept: application/vnd.github.v3+json" \
-        "https://api.github.com/repos/$REPORT_HUB_REPO/pulls/$PR_NUMBER/merge" \
-        -d "{
-          \"commit_title\": \"$COMMIT_MESSAGE\",
-          \"merge_method\": \"squash\"
-        }")
-      
-      if echo "$MERGE_RESULT" | jq -e '.merged' > /dev/null 2>&1; then
-        echo "✅ Pull request merged successfully"
-        
-        # マージ後にブランチを削除
-        curl -s -X DELETE \
-          -H "Authorization: token $GITHUB_TOKEN" \
-          -H "Accept: application/vnd.github.v3+json" \
-          "https://api.github.com/repos/$REPORT_HUB_REPO/git/refs/heads/$BRANCH_NAME" > /dev/null
-        echo "🗑️ Branch $BRANCH_NAME deleted"
-      else
-        echo "⚠️ Failed to auto-merge. Manual merge required."
-        echo "PR URL: $PR_URL"
-      fi
-    else
-      echo "📋 Pull request created and ready for manual review: $PR_URL"
-    fi
-  else
-    echo "❌ Failed to create pull request. Falling back to direct push."
-    git checkout main
-    git merge "$BRANCH_NAME"
-    git push origin main
-    git branch -d "$BRANCH_NAME"
-    git push origin --delete "$BRANCH_NAME" 2>/dev/null || true
-  fi
-else
-  # 直接プッシュフロー
-  echo "⚡ Direct push mode"
-  git commit -m "$COMMIT_MESSAGE"
-  git push
-  echo "✅ Successfully synced to report hub!"
-fi
\ No newline at end of file
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index f2cefaf..6dc1edd 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -1,4 +1,4 @@
-name: 📊 デイリーレポートハブ同期 v2.4 (YUKIHIKO PR版)
+name: 📊 デイリーレポートハブ同期 v2.3 (YUKIHIKO PR版 - 完全リモート実行)
 on:
   push:
     branches: [main, master]
@@ -10,6 +10,8 @@ env:
   AUTO_APPROVE: true
   AUTO_MERGE: true  
   CREATE_PR: true
+  # リモートスクリプトの設定
+  SCRIPTS_BASE_URL: https://raw.githubusercontent.com/Sunwood-ai-labsII/daily-report-hub_dev/main/.github/scripts
 
 jobs:
   sync-data:
@@ -20,17 +22,14 @@ jobs:
         with:
           fetch-depth: 0
 
-      - name: 🔧 スクリプトを実行可能にする
-        run: chmod +x .github/scripts/*.sh
-
       - name: 📅 週情報を計算
-        run: ./.github/scripts/calculate-week-info.sh ${{ env.WEEK_START_DAY }}
+        run: curl -LsSf ${SCRIPTS_BASE_URL}/calculate-week-info.sh | sh -s -- ${{ env.WEEK_START_DAY }}
 
       - name: 🔍 Git活動を分析
-        run: ./.github/scripts/analyze-git-activity.sh
+        run: curl -LsSf ${SCRIPTS_BASE_URL}/analyze-git-activity.sh | sh
 
       - name: 📝 Markdownレポートを生成
-        run: ./.github/scripts/generate-markdown-reports.sh
+        run: curl -LsSf ${SCRIPTS_BASE_URL}/generate-markdown-reports.sh | sh
 
       - name: 📂 レポートハブをクローン
         env:
@@ -42,7 +41,7 @@ jobs:
           git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub
 
       - name: 🏗️ Docusaurus構造を作成
-        run: ./.github/scripts/create-docusaurus-structure.sh
+        run: curl -LsSf ${SCRIPTS_BASE_URL}/create-docusaurus-structure.sh | sh
 
       - name: 🚀 YUKIHIKO権限でPR作成＆自動承認
         env:
@@ -50,4 +49,4 @@ jobs:
           YUKIHIKO_TOKEN: ${{ secrets.GH_PAT_YUKIHIKO }}     # PR作成用
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}              # デフォルト
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
-        run: ./.github/scripts/sync-to-hub-gh.sh
+        run: curl -LsSf ${SCRIPTS_BASE_URL}/sync-to-hub-gh.sh | sh
diff --git a/README.md b/README.md
index 3f9d0dc..2b43334 100644
--- a/README.md
+++ b/README.md
@@ -3,42 +3,42 @@
 
 <div align="center">
 
-# daily-report-hub dev
+# Daily Report Hub Template
 
 <img src="https://img.shields.io/badge/GitHub%20Actions-CICD-blue?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
 <img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Bash" />
+<a href="https://github.com/Sunwood-ai-labsII/daily-report-hub">
+  <img src="https://img.shields.io/badge/daily--report--hub-PANDA-00D4AA?style=for-the-badge&logo=github&logoColor=white" alt="daily-report-hub PANDA" />
+</a>
 
 </div>
 
+
 ---
 
 ## 📖 概要
 
-このリポジトリは、**daily-report-hubの開発リポジトリ**です。ここで開発・保守されたスクリプトは、リモート実行される形でdaily-report-hub本体のワークフローで利用されます。
+このリポジトリは、**Daily Report Hubのテンプレートリポジトリ**です。このテンプレートからリポジトリを作成すると、自動で日報生成・同期機能が有効になります。
 
 ### 🎯 主な用途
-- GitHub Actionsスクリプトの開発・テスト・保守
-- 日報自動生成機能の実装と改善
-- 集約用リポジトリとの同期機能の提供
+- 日報自動生成機能を必要とするプロジェクトのテンプレート
+- 集約用リポジトリ（daily-report-hub）への自動同期
+- GitHub Actionsによる完全自動化されたレポート生成
 
 ### 🔄 運用方式
-このリポジトリで開発されたスクリプトは、daily-report-hub本体のワークフローから**リモート実行**されます。以下のようなcurlコマンドでスクリプトを取得・実行します：
-
-```bash
-curl -LsSf https://raw.githubusercontent.com/Sunwood-ai-labsII/daily-report-hub_dev/main/.github/scripts/スクリプト名.sh | sh
-```
+このテンプレートから作成されたリポジトリは、daily-report-hub本体のワークフローから**リモート実行**されるスクリプトを使用して日報を生成・同期します。
 
 ---
 
-## 🚩 このリポジトリの役割
+## 🚩 このテンプレートの役割
 
-### 🛠️ 開発・保守リポジトリとしての機能
-- **スクリプト開発**: GitHub Actions用スクリプトの開発とテスト
-- **機能改善**: 日報生成機能の継続的な改善とバグ修正
-- **ドキュメント**: スクリプトの使い方と設定方法のドキュメント管理
-- **バージョン管理**: スクリプトのバージョン管理と変更履歴の追跡
+### 🛠️ テンプレートとしての機能
+- **自動セットアップ**: 日報生成機能の自動有効化
+- **ワークフロー提供**: GitHub Actionsワークフローの自動適用
+- **同期機能**: 集約用リポジトリへの自動同期機能
+- **カスタマイズ**: 必要に応じた設定変更の容易性
 
-### 📦 提供されるスクリプト
+### 📦 提供される機能
 - Gitのコミット履歴・差分から日報（Markdown形式）を自動生成
 - 週単位・日単位でレポートを整理
 - 別リポジトリ（daily-report-hub）へPRベースで自動同期
@@ -63,7 +63,7 @@ graph TB
 ### 📋 処理ステップ
 
 1. **トリガー**: **GitHub Actions**がmainブランチへのpushやPRをトリガー
-2. **データ収集**: `.github/scripts/`配下のシェルスクリプトで
+2. **データ収集**: リモートスクリプトで
    - 週情報の計算
    - Git活動の分析
    - Markdownレポートの生成
@@ -82,37 +82,52 @@ graph TB
 
 ---
 
-## 📝 主なスクリプト
+## 📝 主な機能
+
+> [!NOTE]
+> このテンプレートから作成されたリポジトリでは、以下の機能が自動で有効になります。
 
-- `.github/scripts/calculate-week-info.sh`  
+### 🔄 自動実行されるスクリプト（リモート）
+
+- **週情報計算**
   週情報（週番号・開始日・終了日など）を計算し環境変数に出力
 
-- `.github/scripts/analyze-git-activity.sh`  
+- **Git活動分析**
   Gitのコミット履歴・差分を分析し、生データファイルを生成
 
-- `.github/scripts/generate-markdown-reports.sh`  
+- **Markdownレポート生成**
   生データから日報・統計・差分などのMarkdownレポートを自動生成
 
-- `.github/scripts/create-docusaurus-structure.sh`  
+- **Docusaurus構造作成**
   Docusaurus用のディレクトリ・_category_.jsonを自動生成
 
-- `.github/scripts/sync-to-hub-gh.sh`  
-  集約リポジトリへPR作成・自動承認・自動マージ（YUKIHIKO権限）
+- **同期処理**
+  集約リポジトリへPR作成・自動承認・自動マージ
 
 ---
 
 ## 🚀 使い方（クイックスタート）
 
-### 📝 開発者向けの使い方
+### 📝 テンプレートからリポジトリを作成する方法
+
+> [!TIP]
+> このテンプレートから新しいリポジトリを作成すると、日報生成機能が自動で有効になります。
+
+1. **このリポジトリをテンプレートとして使用**
+   - リポジトリトップページの「Use this template」ボタンをクリック
+   - リポジトリ名を入力して「Create repository from template」をクリック
+
+2. **必要なシークレットを設定**
+   - 作成したリポジトリの「Settings」→「Secrets and variables」→「Actions」に移動
+   - 必要なシークレットを設定（下記参照）
 
-1. このリポジトリをforkまたはclone
-2. `.github/workflows/sync-to-report-gh.yml`の設定を必要に応じて編集
-3. 必要なシークレットを設定（下記参照）
-4. mainブランチにpushすると自動で日報生成＆集約リポジトリへ同期
+3. **自動で日報生成が開始**
+   - mainブランチにpushすると自動で日報生成＆集約リポジトリへ同期
 
-### 🌐 daily-report-hubでの実際の運用例
+### 🌐 ワークフローの実際の動作
 
-このリポジトリで開発されたスクリプトは、daily-report-hub本体で以下のようにリモート実行されます：
+> [!IMPORTANT]
+> 作成されたリポジトリでは、以下のワークフローが自動で実行されます：
 
 ```yaml
 name: 📊 デイリーレポートハブ同期 v2.3 (YUKIHIKO PR版 - 完全リモート実行)
@@ -171,7 +186,8 @@ jobs:
 
 ### 🔑 環境変数・シークレット設定
 
-以下の環境変数を設定する必要があります：
+> [!WARNING]
+> 以下のシークレットを設定しないと、日報同期機能が正常に動作しません。
 
 #### 必須シークレット
 - `GH_PAT`: GitHub Personal Access Token（リポジトリアクセス用）
@@ -189,6 +205,9 @@ jobs:
 
 ### 📋 シークレット設定手順
 
+> [!CAUTION]
+> シークレットの漏洩には注意してください。GitHubリポジトリ内に直接記述しないでください。
+
 1. リポジトリの「Settings」→「Secrets and variables」→「Actions」に移動
 2. 「New repository secret」をクリックして各シークレットを追加
 3. 以下のシークレットを設定：
@@ -199,42 +218,50 @@ jobs:
 
 ## 📁 ディレクトリ構成例
 
+> [!NOTE]
+> このテンプレートから作成されたリポジトリの基本的な構成です。
+
 ```
 .
 ├── .github/
-│   ├── scripts/
-│   │   ├── calculate-week-info.sh
-│   │   ├── analyze-git-activity.sh
-│   │   ├── generate-markdown-reports.sh
-│   │   ├── create-docusaurus-structure.sh
-│   │   ├── sync-to-hub-gh.sh
-│   │   └── sync-to-hub.sh
 │   └── workflows/
 │       └── sync-to-report-gh.yml
-├── .SourceSageignore
+├── .gitignore
+├── LICENSE
 ├── README.md
+└── [プロジェクト固有のファイル]
 ```
 
 ---
 
 ## 🛠️ 設定・カスタマイズ
 
-- `.github/workflows/sync-to-report-gh.yml`  
+> [!TIP]
+> 必要に応じてワークフローファイルをカスタマイズできます。
+
+- `.github/workflows/sync-to-report-gh.yml`
   - `WEEK_START_DAY`：週の開始曜日（0=日, 1=月, ...）
   - `AUTO_APPROVE`：PR自動承認
   - `AUTO_MERGE`：PR自動マージ
   - `CREATE_PR`：PR作成/直接push切替
 
-- スクリプトの詳細は[.github/scripts/README.md](.github/scripts/README.md)参照
+- リモートスクリプトの詳細は開発リポジトリを参照
 
 ---
 
 ## 🔗 参考リンク
 
-- [集約用日報ハブリポジトリ](https://github.com/Sunwood-ai-labs/daily-report-hub)
+- [集約用日報ハブリポジトリ](https://github.com/Sunwood-ai-labsII/daily-report-hub)
+- [開発リポジトリ（スクリプトソース）](https://github.com/Sunwood-ai-labsII/daily-report-hub_dev)
 - [GitHub Actions公式ドキュメント](https://docs.github.com/ja/actions)
 - [Docusaurus公式サイト](https://docusaurus.io/ja/)
 
 ---
 
+## 📝 ライセンス
+
+このテンプレートは [LICENSE](LICENSE) に基づいて提供されています。
+
+---
+
 © 2025 Sunwood-ai-labsII
```
