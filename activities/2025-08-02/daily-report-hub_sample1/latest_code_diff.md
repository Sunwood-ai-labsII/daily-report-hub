# 🔄 Latest Code Changes

    diff --git a/.github/workflows/sync-to-report.yml b/.github/workflows/sync-to-report.yml
    index 1ff95ea..05e88cd 100644
    --- a/.github/workflows/sync-to-report.yml
    +++ b/.github/workflows/sync-to-report.yml
    @@ -27,10 +27,10 @@ jobs:
               # その日の全コミット履歴を取得（時刻順）
               git log --since="$DATE 00:00:00" --until="$DATE 23:59:59" \
                 --pretty=format:"%h|%s|%an|%ad" --date=format:'%H:%M:%S' \
    -            --reverse > daily_commits.txt
    +            --reverse > daily_commits_raw.txt
               
               # コミット数をカウント
    -          COMMIT_COUNT=$(wc -l < daily_commits.txt)
    +          COMMIT_COUNT=$(wc -l < daily_commits_raw.txt)
               echo "📊 Found $COMMIT_COUNT commits for today"
               
               # その日の全ての差分を統合（安全な方法で）
    @@ -45,45 +45,135 @@ jobs:
                 if git rev-parse --verify "$FIRST_COMMIT_TODAY^" >/dev/null 2>&1; then
                   # 親コミットが存在する場合
                   PARENT_OF_FIRST=$(git rev-parse $FIRST_COMMIT_TODAY^)
    -              git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY --name-status > daily_cumulative_diff.txt 2>/dev/null || echo "No diff available" > daily_cumulative_diff.txt
    -              git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY --stat > daily_diff_stats.txt 2>/dev/null || echo "No stats available" > daily_diff_stats.txt
    +              git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY --name-status > daily_cumulative_diff_raw.txt 2>/dev/null || echo "No diff available" > daily_cumulative_diff_raw.txt
    +              git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY --stat > daily_diff_stats_raw.txt 2>/dev/null || echo "No stats available" > daily_diff_stats_raw.txt
                   # コードの詳細差分を取得
    -              git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY > daily_code_diff.txt 2>/dev/null || echo "No code diff available" > daily_code_diff.txt
    +              git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY > daily_code_diff_raw.txt 2>/dev/null || echo "No code diff available" > daily_code_diff_raw.txt
                 else
                   # 初回コミットの場合（親が存在しない）
                   echo "Initial commit detected - showing all files as new"
    -              git diff --name-status 4b825dc642cb6eb9a060e54bf8d69288fbee4904..$LAST_COMMIT_TODAY > daily_cumulative_diff.txt 2>/dev/null || \
    -              git ls-tree --name-status $LAST_COMMIT_TODAY > daily_cumulative_diff.txt 2>/dev/null || \
    -              echo "A\t(all files added in initial commit)" > daily_cumulative_diff.txt
    +              git diff --name-status 4b825dc642cb6eb9a060e54bf8d69288fbee4904..$LAST_COMMIT_TODAY > daily_cumulative_diff_raw.txt 2>/dev/null || \
    +              git ls-tree --name-status $LAST_COMMIT_TODAY > daily_cumulative_diff_raw.txt 2>/dev/null || \
    +              echo "A\t(all files added in initial commit)" > daily_cumulative_diff_raw.txt
                   
    -              git diff --stat 4b825dc642cb6eb9a060e54bf8d69288fbee4904..$LAST_COMMIT_TODAY > daily_diff_stats.txt 2>/dev/null || \
    -              echo "Initial commit - all files added" > daily_diff_stats.txt
    +              git diff --stat 4b825dc642cb6eb9a060e54bf8d69288fbee4904..$LAST_COMMIT_TODAY > daily_diff_stats_raw.txt 2>/dev/null || \
    +              echo "Initial commit - all files added" > daily_diff_stats_raw.txt
                   
                   # 初回コミットのコード内容
    -              git show $LAST_COMMIT_TODAY > daily_code_diff.txt 2>/dev/null || echo "No code diff available" > daily_code_diff.txt
    +              git show $LAST_COMMIT_TODAY > daily_code_diff_raw.txt 2>/dev/null || echo "No code diff available" > daily_code_diff_raw.txt
                 fi
               else
    -            echo "No commits found for today" > daily_cumulative_diff.txt
    -            echo "No commits found for today" > daily_diff_stats.txt
    -            echo "No commits found for today" > daily_code_diff.txt
    +            echo "No commits found for today" > daily_cumulative_diff_raw.txt
    +            echo "No commits found for today" > daily_diff_stats_raw.txt
    +            echo "No commits found for today" > daily_code_diff_raw.txt
               fi
               
               # 最新コミットの個別差分
    -          git diff HEAD~1 --name-status > latest_diff.txt 2>/dev/null || echo "No recent diff available" > latest_diff.txt
    -          git diff HEAD~1 > latest_code_diff.txt 2>/dev/null || echo "No recent code diff available" > latest_code_diff.txt
    +          git diff HEAD~1 --name-status > latest_diff_raw.txt 2>/dev/null || echo "No recent diff available" > latest_diff_raw.txt
    +          git diff HEAD~1 > latest_code_diff_raw.txt 2>/dev/null || echo "No recent code diff available" > latest_code_diff_raw.txt
    +          
    +          # Markdownファイルを作成（各行に4スペースのインデントを追加する関数）
    +          add_indent() {
    +            sed 's/^/    /' "$1"
    +          }
    +          
    +          # コミット詳細をMarkdown形式で作成
    +          {
    +            echo "# 📝 Daily Commits"
    +            echo ""
    +            if [ -s daily_commits_raw.txt ]; then
    +              while IFS='|' read -r hash subject author time; do
    +                echo "## ⏰ $time - \`$hash\`"
    +                echo "**$subject**"
    +                echo "*by $author*"
    +                echo ""
    +              done < daily_commits_raw.txt
    +            else
    +              echo "*No commits found for today.*"
    +            fi
    +          } > daily_commits.md
    +          
    +          # 累積差分をMarkdown形式で作成
    +          {
    +            echo "# 📋 Daily File Changes"
    +            echo ""
    +            if [ -s daily_cumulative_diff_raw.txt ]; then
    +              while read -r line; do
    +                if [ ! -z "$line" ]; then
    +                  status=$(echo "$line" | cut -f1)
    +                  file=$(echo "$line" | cut -f2)
    +                  case $status in
    +                    A) echo "- 🆕 **Added:** \`$file\`" ;;
    +                    M) echo "- ✏️ **Modified:** \`$file\`" ;;
    +                    D) echo "- 🗑️ **Deleted:** \`$file\`" ;;
    +                    R*) echo "- 🔄 **Renamed:** \`$file\`" ;;
    +                    *) echo "- 📝 **$status:** \`$file\`" ;;
    +                  esac
    +                fi
    +              done < daily_cumulative_diff_raw.txt
    +            else
    +              echo "*No file changes today.*"
    +            fi
    +          } > daily_cumulative_diff.md
    +          
    +          # 統計をMarkdown形式で作成
    +          {
    +            echo "# 📈 Daily Statistics"
    +            echo ""
    +            add_indent daily_diff_stats_raw.txt
    +          } > daily_diff_stats.md
    +          
    +          # コード差分をMarkdown形式で作成
    +          {
    +            echo "# 💻 Daily Code Changes"
    +            echo ""
    +            echo "## Full Diff"
    +            echo ""
    +            add_indent daily_code_diff_raw.txt
    +          } > daily_code_diff.md
    +          
    +          # 最新差分をMarkdown形式で作成
    +          {
    +            echo "# 🔄 Latest Changes (File List)"
    +            echo ""
    +            if [ -s latest_diff_raw.txt ]; then
    +              while read -r line; do
    +                if [ ! -z "$line" ]; then
    +                  status=$(echo "$line" | cut -f1)
    +                  file=$(echo "$line" | cut -f2)
    +                  case $status in
    +                    A) echo "- 🆕 **Added:** \`$file\`" ;;
    +                    M) echo "- ✏️ **Modified:** \`$file\`" ;;
    +                    D) echo "- 🗑️ **Deleted:** \`$file\`" ;;
    +                    R*) echo "- 🔄 **Renamed:** \`$file\`" ;;
    +                    *) echo "- 📝 **$status:** \`$file\`" ;;
    +                  esac
    +                fi
    +              done < latest_diff_raw.txt
    +            else
    +              echo "*No recent changes.*"
    +            fi
    +          } > latest_diff.md
    +          
    +          # 最新コード差分をMarkdown形式で作成
    +          {
    +            echo "# 🔄 Latest Code Changes"
    +            echo ""
    +            add_indent latest_code_diff_raw.txt
    +          } > latest_code_diff.md
               
               # 詳細なアクティビティサマリーをMarkdown形式で作成
    -          if [ -s daily_commits.txt ]; then
    -            FIRST_COMMIT_TIME=$(head -1 daily_commits.txt | cut -d'|' -f4)
    -            LAST_COMMIT_TIME=$(tail -1 daily_commits.txt | cut -d'|' -f4)
    -            FILES_CHANGED=$(grep -c '^' daily_cumulative_diff.txt 2>/dev/null || echo "0")
    +          if [ -s daily_commits_raw.txt ]; then
    +            FIRST_COMMIT_TIME=$(head -1 daily_commits_raw.txt | cut -d'|' -f4)
    +            LAST_COMMIT_TIME=$(tail -1 daily_commits_raw.txt | cut -d'|' -f4)
    +            FILES_CHANGED=$(grep -c '^' daily_cumulative_diff_raw.txt 2>/dev/null || echo "0")
               else
                 FIRST_COMMIT_TIME="N/A"
                 LAST_COMMIT_TIME="N/A" 
                 FILES_CHANGED=0
               fi
               
    -          # Markdownサマリーファイルを作成
    +          # メインサマリーファイルを作成
               {
                 echo "# 📅 Daily Activity Report"
                 echo ""
    @@ -99,7 +189,7 @@ jobs:
                 echo "| Sync Time | $(date '+%H:%M:%S') |"
                 echo ""
                 
    -            if [ -s daily_commits.txt ]; then
    +            if [ -s daily_commits_raw.txt ]; then
                   echo "## 📝 Commit Details"
                   echo ""
                   while IFS='|' read -r hash subject author time; do
    @@ -107,12 +197,11 @@ jobs:
                     echo "**$subject**"
                     echo "*by $author*"
                     echo ""
    -              done < daily_commits.txt
    +              done < daily_commits_raw.txt
                   
                   echo "## 📈 File Changes Statistics"
    -              echo "\`\`\`"
    -              cat daily_diff_stats.txt
    -              echo "\`\`\`"
    +              echo ""
    +              add_indent daily_diff_stats_raw.txt
                   echo ""
                   
                   echo "## 📋 Changed Files List"
    @@ -129,7 +218,7 @@ jobs:
                         *) echo "- 📝 **$status:** \`$file\`" ;;
                       esac
                     fi
    -              done < daily_cumulative_diff.txt
    +              done < daily_cumulative_diff_raw.txt
                   echo ""
                   
                 else
    @@ -163,18 +252,18 @@ jobs:
               # README.mdをコピー
               cp README.md "$TARGET_DIR/" 2>/dev/null || echo "# $REPO_NAME" > "$TARGET_DIR/README.md"
               
    -          # 当日のアクティビティファイルをコピー
    -          cp daily_commits.txt "$TARGET_DIR/"
    -          cp daily_cumulative_diff.txt "$TARGET_DIR/"
    -          cp daily_diff_stats.txt "$TARGET_DIR/"
    -          cp daily_code_diff.txt "$TARGET_DIR/"
    -          cp latest_diff.txt "$TARGET_DIR/"
    -          cp latest_code_diff.txt "$TARGET_DIR/"
    -          cp daily_summary.md "$TARGET_DIR/"  # Markdownサマリー
    +          # 当日のアクティビティファイルをコピー（全て.mdファイル）
    +          cp daily_commits.md "$TARGET_DIR/"
    +          cp daily_cumulative_diff.md "$TARGET_DIR/"
    +          cp daily_diff_stats.md "$TARGET_DIR/"
    +          cp daily_code_diff.md "$TARGET_DIR/"
    +          cp latest_diff.md "$TARGET_DIR/"
    +          cp latest_code_diff.md "$TARGET_DIR/"
    +          cp daily_summary.md "$TARGET_DIR/"
               
               # 詳細メタデータを作成
    -          COMMIT_COUNT=$(wc -l < daily_commits.txt)
    -          FILES_CHANGED=$(grep -c '^' daily_cumulative_diff.txt 2>/dev/null || echo "0")
    +          COMMIT_COUNT=$(wc -l < daily_commits_raw.txt)
    +          FILES_CHANGED=$(grep -c '^' daily_cumulative_diff_raw.txt 2>/dev/null || echo "0")
               
               cat > "$TARGET_DIR/metadata.json" << EOF
               {
    @@ -189,12 +278,12 @@ jobs:
                 "has_activity": $([ $COMMIT_COUNT -gt 0 ] && echo "true" || echo "false"),
                 "files": {
                   "summary": "daily_summary.md",
    -              "commits": "daily_commits.txt",
    -              "file_changes": "daily_cumulative_diff.txt",
    -              "stats": "daily_diff_stats.txt",
    -              "code_diff": "daily_code_diff.txt",
    -              "latest_diff": "latest_diff.txt",
    -              "latest_code_diff": "latest_code_diff.txt"
    +              "commits": "daily_commits.md",
    +              "file_changes": "daily_cumulative_diff.md",
    +              "stats": "daily_diff_stats.md",
    +              "code_diff": "daily_code_diff.md",
    +              "latest_diff": "latest_diff.md",
    +              "latest_code_diff": "latest_code_diff.md"
                 }
               }
               EOF
