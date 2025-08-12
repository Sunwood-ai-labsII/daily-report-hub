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
index b5818cd..76a5f41
--- a/.github/scripts/generate-markdown-reports.sh
+++ b/.github/scripts/generate-markdown-reports.sh
@@ -23,7 +23,7 @@ get_status_icon() {
 # コードブロック内容をサニタイズする関数
 sanitize_code_block() {
   # バッククォート3つをエスケープ
-  sed 's/\```/`\`\`/g' "$1"
+  sed 's/\```/\\\```/g' "$1"
 }
 
 # コミット詳細をMarkdown形式で作成（差分付き）
@@ -54,7 +54,7 @@ sanitize_code_block() {
       # 各コミットのコード差分を表示（最初の100行まで、サニタイズ済み）
       echo "### 💻 Code Changes"
       echo "\`\`\`diff"
-      git show $hash --pretty=format:"" 2>/dev/null | head -100 | sed 's/\```/`\`\`/g' || echo "No code changes available"
+      git show $hash --pretty=format:"" 2>/dev/null | head -100 | sed 's/\```/\\\```/g' || echo "No code changes available"
       echo "\`\`\`"
       echo ""
       echo "---"
@@ -88,7 +88,7 @@ sanitize_code_block() {
   echo ""
   echo "\`\`\`diff"
   # バッククォートをエスケープして出力
-  cat daily_diff_stats_raw.txt | sed 's/\```/`\`\`/g'
+  cat daily_diff_stats_raw.txt | sed 's/\```/\\\```/g'
   echo "\`\`\`"
 } > daily_diff_stats.md
 
@@ -100,7 +100,7 @@ sanitize_code_block() {
   echo ""
   echo "\`\`\`diff"
   # バッククォートをエスケープして出力
-  cat daily_code_diff_raw.txt | sed 's/\```/`\`\`/g'
+  cat daily_code_diff_raw.txt | sed 's/\```/\\\```/g'
   echo "\`\`\`"
 } > daily_code_diff.md
 
@@ -127,7 +127,7 @@ sanitize_code_block() {
   echo ""
   echo "\`\`\`diff"
   # バッククォートをエスケープして出力
-  cat latest_code_diff_raw.txt | sed 's/\```/`\`\`/g'
+  cat latest_code_diff_raw.txt | sed 's/\```/\\\```/g'
   echo "\`\`\`"
 } > latest_code_diff.md
 
@@ -172,7 +172,7 @@ fi
     echo ""
     echo "\`\`\`diff"
     # バッククォートをエスケープして出力
-    cat daily_diff_stats_raw.txt | sed 's/\```/`\`\`/g'
+    cat daily_diff_stats_raw.txt | sed 's/\```/\\\```/g'
     echo "\`\`\`"
     echo ""
     
diff --git a/.github/scripts/sync-to-hub-gh.sh b/.github/scripts/sync-to-hub-gh.sh
old mode 100644
new mode 100755
diff --git a/.github/scripts/sync-to-hub.sh b/.github/scripts/sync-to-hub.sh
old mode 100644
new mode 100755
```
