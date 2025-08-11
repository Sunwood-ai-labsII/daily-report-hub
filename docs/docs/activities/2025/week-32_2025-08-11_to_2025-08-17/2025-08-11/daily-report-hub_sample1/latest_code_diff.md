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
index 5e6aaac..3688357 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -47,7 +47,7 @@ jobs:
       - name: 🚀 YUKIHIKO権限でPR作成＆自動承認
         env:
           GITHUB_TOKEN_ORIGINAL: ${{ secrets.GH_PAT }}      # 承認用
-          YUKIHIKO_TOKEN: ${{ secrets.YUKIHIKO_TOKEN }}     # PR作成用
+          YUKIHIKO_TOKEN: ${{ secrets.GH_PAT_YUKIHIKO }}     # PR作成用
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}              # デフォルト
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
         run: ./.github/scripts/sync-to-hub-gh.sh
```
