# 💻 Daily Code Changes

## Full Diff

    diff --git a/.github/workflows/sync-to-report.yml b/.github/workflows/sync-to-report.yml
    index 05e88cd..20876db 100644
    --- a/.github/workflows/sync-to-report.yml
    +++ b/.github/workflows/sync-to-report.yml
    @@ -1,4 +1,4 @@
    -name: Sync to Daily Report Hub
    +name: Sync to Daily Report Hub v1.3
     on:
       push:
         branches: [main, master]
    @@ -236,14 +236,15 @@ jobs:
           
           - name: Clone and update report hub
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
    +          git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub
               
               # 日付ベースのディレクトリ構造を作成
               TARGET_DIR="daily-report-hub/activities/$DATE/$REPO_NAME"
    @@ -297,4 +298,4 @@ jobs:
               else
                 git commit -m "📊 Daily sync: $REPO_NAME ($DATE) - $COMMIT_COUNT commits"
                 git push
    -          fi
    \ No newline at end of file
    +          fi
