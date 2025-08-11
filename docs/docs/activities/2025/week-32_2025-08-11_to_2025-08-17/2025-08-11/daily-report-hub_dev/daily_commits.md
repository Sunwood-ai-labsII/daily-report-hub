# 📝 Daily Commits

## ⏰ 23:26:04 - `0a48d12`
**Initial commit**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 23:26:04 2025 +0900
A	.env.example
A	.github/scripts/README.md
A	.github/scripts/analyze-git-activity.sh
A	.github/scripts/calculate-week-info.sh
A	.github/scripts/create-docusaurus-structure.sh
A	.github/scripts/generate-markdown-reports.sh
A	.github/scripts/sync-to-hub-gh.sh
A	.github/scripts/sync-to-hub.sh
A	.github/workflows/sync-to-report-gh.yml
A	.gitignore
A	CHANGELOG.md
A	CONTRIBUTING.md
A	LICENSE
A	README.md
A	index.html
A	memo.md
A	script.js
A	style.css
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 23:26:04 2025 +0900

    Initial commit

 .env.example                                   |  15 ++
 .github/scripts/README.md                      | 141 +++++++++++++++++
 .github/scripts/analyze-git-activity.sh        |  59 +++++++
 .github/scripts/calculate-week-info.sh         |  44 ++++++
 .github/scripts/create-docusaurus-structure.sh | 111 +++++++++++++
 .github/scripts/generate-markdown-reports.sh   | 191 +++++++++++++++++++++++
 .github/scripts/sync-to-hub-gh.sh              | 182 ++++++++++++++++++++++
 .github/scripts/sync-to-hub.sh                 | 184 ++++++++++++++++++++++
 .github/workflows/sync-to-report-gh.yml        |  53 +++++++
 .gitignore                                     | 207 +++++++++++++++++++++++++
 CHANGELOG.md                                   |  32 ++++
 CONTRIBUTING.md                                |  51 ++++++
 LICENSE                                        |  21 +++
 README.md                                      |  90 +++++++++++
 index.html                                     |  35 +++++
 memo.md                                        |  47 ++++++
 script.js                                      |  26 ++++
 style.css                                      | 106 +++++++++++++
 18 files changed, 1595 insertions(+)
```

### 💻 Code Changes
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
index 0000000..c7e07f4
--- /dev/null
+++ b/.github/scripts/README.md
@@ -0,0 +1,141 @@
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
```

---

