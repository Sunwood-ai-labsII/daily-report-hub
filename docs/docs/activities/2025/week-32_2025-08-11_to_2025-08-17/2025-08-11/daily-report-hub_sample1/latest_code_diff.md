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
index 7d2251f..b5738eb
--- a/.github/scripts/generate-markdown-reports.sh
+++ b/.github/scripts/generate-markdown-reports.sh
@@ -33,14 +33,14 @@ get_status_icon() {
       
       # 各コミットの変更ファイル一覧を表示
       echo "### 📋 Changed Files"
-      echo "\`\`\`"
+      echo "\`\`\`bash"
       git show --name-status $hash 2>/dev/null | grep -E '^[AMDRC]' || echo "No file changes"
       echo "\`\`\`"
       echo ""
       
       # 各コミットの統計情報を表示
       echo "### 📊 Statistics"
-      echo "\`\`\`"
+      echo "\`\`\`bash"
       git show --stat $hash 2>/dev/null | tail -n +2 || echo "No statistics available"
       echo "\`\`\`"
       echo ""
@@ -80,7 +80,9 @@ get_status_icon() {
 {
   echo "# 📈 Daily Statistics"
   echo ""
-  add_indent daily_diff_stats_raw.txt
+  echo "\`\`\`diff"
+  cat daily_diff_stats_raw.txt
+  echo "\`\`\`"
 } > daily_diff_stats.md
 
 # コード差分をMarkdown形式で作成
@@ -159,7 +161,9 @@ fi
     
     echo "## 📈 File Changes Statistics"
     echo ""
-    add_indent daily_diff_stats_raw.txt
+    echo "\`\`\`diff"
+    cat daily_diff_stats_raw.txt
+    echo "\`\`\`"
     echo ""
     
     echo "## 📋 Changed Files List"
diff --git a/.github/scripts/sync-to-hub.sh b/.github/scripts/sync-to-hub.sh
old mode 100644
new mode 100755
index 9e96989..fc870c6
--- a/.github/scripts/sync-to-hub.sh
+++ b/.github/scripts/sync-to-hub.sh
@@ -46,6 +46,7 @@ cat > "$TARGET_DIR/metadata.json" << EOF
   "daily_files_changed": $FILES_CHANGED,
   "has_activity": $([ $COMMIT_COUNT -gt 0 ] && echo "true" || echo "false"),
   "files": {
+    "readme": "README.md",
     "summary": "daily_summary.md",
     "commits": "daily_commits.md",
     "file_changes": "daily_cumulative_diff.md",
```
