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
diff --git a/.github/scripts/sync-to-hub.sh b/.github/scripts/sync-to-hub.sh
old mode 100644
new mode 100755
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index 1589d29..16e1235 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -1,4 +1,4 @@
-name: Sync to Daily Report Hub v2.0 (GitHub CLI)
+name: Sync to Daily Report Hub v2.0
 on:
   push:
     branches: [main, master]
@@ -21,11 +21,6 @@ jobs:
         with:
           fetch-depth: 0 # 全履歴を取得してその日の全コミットを追跡
 
-      - name: Setup GitHub CLI
-        run: |
-          # GitHub CLIは既にubuntu-latestにインストール済み
-          gh --version
-
       - name: Make scripts executable
         run: chmod +x .github/scripts/*.sh
 
@@ -47,20 +42,17 @@ jobs:
           git config --global user.name "GitHub Actions Bot"
           git config --global user.email "actions@github.com"
 
-          # GitHub CLI認証
-          echo "$GITHUB_TOKEN" | gh auth login --with-token
-
           # daily-report-hubをクローン
           git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub
 
       - name: Create Docusaurus structure
         run: ./.github/scripts/create-docusaurus-structure.sh
 
-      - name: Sync to report hub with PR flow (GitHub CLI)
+      - name: Sync to report hub with PR flow
         env:
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
           AUTO_APPROVE: ${{ env.AUTO_APPROVE }}
           AUTO_MERGE: ${{ env.AUTO_MERGE }}
           CREATE_PR: ${{ env.CREATE_PR }}
-        run: ./.github/scripts/sync-to-hub-gh.sh
+        run: ./.github/scripts/sync-to-hub.sh
```
