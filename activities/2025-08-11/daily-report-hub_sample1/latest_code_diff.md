# 🔄 Latest Code Changes

    diff --git a/.github/workflows/sync-to-report.yml b/.github/workflows/sync-to-report.yml
    index 20876db..a830de9 100644
    --- a/.github/workflows/sync-to-report.yml
    +++ b/.github/workflows/sync-to-report.yml
    @@ -12,8 +12,8 @@ jobs:
           - name: Checkout current repo
             uses: actions/checkout@v4
             with:
    -          fetch-depth: 0  # 全履歴を取得してその日の全コミットを追跡
    -      
    +          fetch-depth: 0 # 全履歴を取得してその日の全コミットを追跡
    +
           - name: Get repository info and daily activities
             run: |
               # リポジトリ名と日付を取得
    @@ -21,18 +21,18 @@ jobs:
               DATE=$(date '+%Y-%m-%d')
               echo "REPO_NAME=$REPO_NAME" >> $GITHUB_ENV
               echo "DATE=$DATE" >> $GITHUB_ENV
    -          
    +
               echo "🔍 Fetching all commits for $DATE..."
    -          
    +
               # その日の全コミット履歴を取得（時刻順）
               git log --since="$DATE 00:00:00" --until="$DATE 23:59:59" \
                 --pretty=format:"%h|%s|%an|%ad" --date=format:'%H:%M:%S' \
                 --reverse > daily_commits_raw.txt
    -          
    +
               # コミット数をカウント
               COMMIT_COUNT=$(wc -l < daily_commits_raw.txt)
               echo "📊 Found $COMMIT_COUNT commits for today"
    -          
    +
               # その日の全ての差分を統合（安全な方法で）
               if [ $COMMIT_COUNT -gt 0 ]; then
                 FIRST_COMMIT_TODAY=$(git log --since="$DATE 00:00:00" --pretty=format:"%H" --reverse | head -1)
    @@ -67,17 +67,17 @@ jobs:
                 echo "No commits found for today" > daily_diff_stats_raw.txt
                 echo "No commits found for today" > daily_code_diff_raw.txt
               fi
    -          
    +
               # 最新コミットの個別差分
               git diff HEAD~1 --name-status > latest_diff_raw.txt 2>/dev/null || echo "No recent diff available" > latest_diff_raw.txt
               git diff HEAD~1 > latest_code_diff_raw.txt 2>/dev/null || echo "No recent code diff available" > latest_code_diff_raw.txt
    -          
    +
               # Markdownファイルを作成（各行に4スペースのインデントを追加する関数）
               add_indent() {
                 sed 's/^/    /' "$1"
               }
    -          
    -          # コミット詳細をMarkdown形式で作成
    +
    +          # コミット詳細をMarkdown形式で作成（差分付き）
               {
                 echo "# 📝 Daily Commits"
                 echo ""
    @@ -87,12 +87,35 @@ jobs:
                     echo "**$subject**"
                     echo "*by $author*"
                     echo ""
    +                
    +                # 各コミットの変更ファイル一覧を表示
    +                echo "### 📋 Changed Files"
    +                echo "\`\`\`"
    +                git show --name-status $hash 2>/dev/null | grep -E '^[AMDRC]' || echo "No file changes"
    +                echo "\`\`\`"
    +                echo ""
    +                
    +                # 各コミットの統計情報を表示
    +                echo "### 📊 Statistics"
    +                echo "\`\`\`"
    +                git show --stat $hash 2>/dev/null | tail -n +2 || echo "No statistics available"
    +                echo "\`\`\`"
    +                echo ""
    +                
    +                # 各コミットのコード差分を表示（最初の100行まで）
    +                echo "### 💻 Code Changes"
    +                echo "\`\`\`diff"
    +                git show $hash --pretty=format:"" 2>/dev/null | head -100 || echo "No code changes available"
    +                echo "\`\`\`"
    +                echo ""
    +                echo "---"
    +                echo ""
                   done < daily_commits_raw.txt
                 else
                   echo "*No commits found for today.*"
                 fi
               } > daily_commits.md
    -          
    +
               # 累積差分をMarkdown形式で作成
               {
                 echo "# 📋 Daily File Changes"
    @@ -115,14 +138,14 @@ jobs:
                   echo "*No file changes today.*"
                 fi
               } > daily_cumulative_diff.md
    -          
    +
               # 統計をMarkdown形式で作成
               {
                 echo "# 📈 Daily Statistics"
                 echo ""
                 add_indent daily_diff_stats_raw.txt
               } > daily_diff_stats.md
    -          
    +
               # コード差分をMarkdown形式で作成
               {
                 echo "# 💻 Daily Code Changes"
    @@ -131,7 +154,7 @@ jobs:
                 echo ""
                 add_indent daily_code_diff_raw.txt
               } > daily_code_diff.md
    -          
    +
               # 最新差分をMarkdown形式で作成
               {
                 echo "# 🔄 Latest Changes (File List)"
    @@ -154,14 +177,14 @@ jobs:
                   echo "*No recent changes.*"
                 fi
               } > latest_diff.md
    -          
    +
               # 最新コード差分をMarkdown形式で作成
               {
                 echo "# 🔄 Latest Code Changes"
                 echo ""
                 add_indent latest_code_diff_raw.txt
               } > latest_code_diff.md
    -          
    +
               # 詳細なアクティビティサマリーをMarkdown形式で作成
               if [ -s daily_commits_raw.txt ]; then
                 FIRST_COMMIT_TIME=$(head -1 daily_commits_raw.txt | cut -d'|' -f4)
    @@ -172,7 +195,7 @@ jobs:
                 LAST_COMMIT_TIME="N/A" 
                 FILES_CHANGED=0
               fi
    -          
    +
               # メインサマリーファイルを作成
               {
                 echo "# 📅 Daily Activity Report"
    @@ -231,9 +254,9 @@ jobs:
                 echo "---"
                 echo "*Generated by GitHub Actions at $(date '+%Y-%m-%d %H:%M:%S')*"
               } > daily_summary.md
    -          
    +
               echo "✅ Daily activity analysis complete!"
    -      
    +
           - name: Clone and update report hub
             env:
               GITHUB_TOKEN: ${{ secrets.GH_PAT }}
    @@ -242,17 +265,17 @@ jobs:
               # Git設定
               git config --global user.name "GitHub Actions Bot"
               git config --global user.email "actions@github.com"
    -          
    +
               # daily-report-hubをクローン
               git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub
    -          
    +
               # 日付ベースのディレクトリ構造を作成
               TARGET_DIR="daily-report-hub/activities/$DATE/$REPO_NAME"
               mkdir -p "$TARGET_DIR"
    -          
    +
               # README.mdをコピー
               cp README.md "$TARGET_DIR/" 2>/dev/null || echo "# $REPO_NAME" > "$TARGET_DIR/README.md"
    -          
    +
               # 当日のアクティビティファイルをコピー（全て.mdファイル）
               cp daily_commits.md "$TARGET_DIR/"
               cp daily_cumulative_diff.md "$TARGET_DIR/"
    @@ -261,11 +284,11 @@ jobs:
               cp latest_diff.md "$TARGET_DIR/"
               cp latest_code_diff.md "$TARGET_DIR/"
               cp daily_summary.md "$TARGET_DIR/"
    -          
    +
               # 詳細メタデータを作成
               COMMIT_COUNT=$(wc -l < daily_commits_raw.txt)
               FILES_CHANGED=$(grep -c '^' daily_cumulative_diff_raw.txt 2>/dev/null || echo "0")
    -          
    +
               cat > "$TARGET_DIR/metadata.json" << EOF
               {
                 "repository": "$GITHUB_REPOSITORY",
    @@ -288,11 +311,11 @@ jobs:
                 }
               }
               EOF
    -          
    +
               # タイムスタンプ付きでコミット・プッシュ
               cd daily-report-hub
               git add .
    -          
    +
               if git diff --staged --quiet; then
                 echo "No changes to commit"
               else
    diff --git a/README.md b/README.md
    index e26ebfc..28c2ccc 100644
    --- a/README.md
    +++ b/README.md
    @@ -4,8 +4,6 @@
     
     # daily-report-hub_sample1
     
    -![Omikuji App](https://via.placeholder.com/800x200/FF6B6B/FFFFFF?text=🎋+Omikuji+App+⛩️)
    -
     <p>
       <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
       <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
    @@ -27,7 +25,7 @@
     
     <div align="center">
     
    -![App Screenshot](https://via.placeholder.com/600x400/F0F0F0/333333?text=🎋+おみくじアプリ+⛩️)
    +![App Screenshot](https://github.com/user-attachments/assets/fc8363f1-3a9f-4684-9b5d-b000a0a9a788)
     
     </div>
     
