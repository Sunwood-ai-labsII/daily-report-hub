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
index 693725b..7d2251f
--- a/.github/scripts/generate-markdown-reports.sh
+++ b/.github/scripts/generate-markdown-reports.sh
@@ -89,7 +89,9 @@ get_status_icon() {
   echo ""
   echo "## Full Diff"
   echo ""
-  add_indent daily_code_diff_raw.txt
+  echo "\`\`\`diff"
+  cat daily_code_diff_raw.txt
+  echo "\`\`\`"
 } > daily_code_diff.md
 
 # 最新差分をMarkdown形式で作成
@@ -113,7 +115,9 @@ get_status_icon() {
 {
   echo "# 🔄 Latest Code Changes"
   echo ""
-  add_indent latest_code_diff_raw.txt
+  echo "\`\`\`diff"
+  cat latest_code_diff_raw.txt
+  echo "\`\`\`"
 } > latest_code_diff.md
 
 # 詳細なアクティビティサマリーをMarkdown形式で作成
diff --git a/.github/scripts/sync-to-hub.sh b/.github/scripts/sync-to-hub.sh
old mode 100644
new mode 100755
diff --git a/README.md b/README.md
index 28c2ccc..e5baa3d 100644
--- a/README.md
+++ b/README.md
@@ -5,9 +5,9 @@
 # daily-report-hub_sample1
 
 <p>
-  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
-  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
-  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
+  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
+  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
+  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
 </p>
 
 </div>
```
