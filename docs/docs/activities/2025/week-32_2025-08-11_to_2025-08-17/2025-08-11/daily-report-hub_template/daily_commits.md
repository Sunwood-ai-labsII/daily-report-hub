# 📝 Daily Commits

## ⏰ 01:32:33 - `60869c6`
**Initial commit**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Tue Aug 12 01:32:33 2025 +0900
A	.SourceSageignore
A	.github/scripts/README.md
A	.github/scripts/analyze-git-activity.sh
A	.github/scripts/calculate-week-info.sh
A	.github/scripts/create-docusaurus-structure.sh
A	.github/scripts/generate-markdown-reports.sh
A	.github/scripts/sync-to-hub-gh.sh
A	.github/scripts/sync-to-hub.sh
A	.github/workflows/sync-to-report-gh.yml
A	.gitignore
A	LICENSE
A	README.md
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Tue Aug 12 01:32:33 2025 +0900

    Initial commit

 .SourceSageignore                              |  54 ++++++
 .github/scripts/README.md                      | 141 +++++++++++++++
 .github/scripts/analyze-git-activity.sh        |  59 ++++++
 .github/scripts/calculate-week-info.sh         |  44 +++++
 .github/scripts/create-docusaurus-structure.sh | 111 ++++++++++++
 .github/scripts/generate-markdown-reports.sh   | 201 +++++++++++++++++++++
 .github/scripts/sync-to-hub-gh.sh              | 182 +++++++++++++++++++
 .github/scripts/sync-to-hub.sh                 | 184 +++++++++++++++++++
 .github/workflows/sync-to-report-gh.yml        |  53 ++++++
 .gitignore                                     | 208 +++++++++++++++++++++
 LICENSE                                        |  21 +++
 README.md                                      | 240 +++++++++++++++++++++++++
 12 files changed, 1498 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/.SourceSageignore b/.SourceSageignore
new file mode 100644
index 0000000..a029c83
--- /dev/null
+++ b/.SourceSageignore
@@ -0,0 +1,54 @@
+# バージョン管理システム関連
+.git/
+.gitignore
+
+# キャッシュファイル
+__pycache__/
+.pytest_cache/
+**/__pycache__/**
+*.pyc
+
+# ビルド・配布関連
+build/
+dist/
+*.egg-info/
+
+# 一時ファイル・出力
+output/
+output.md
+test_output/
+.SourceSageAssets/
+.SourceSageAssetsDemo/
+
+# アセット
+*.png
+*.svg
+*.jpg
+*.jepg
+assets/
+
+# その他
+LICENSE
+example/
+package-lock.json
+.DS_Store
+
+# 特定のディレクトリを除外
+tests/temp/
+docs/drafts/
+
+# パターンの例外（除外対象から除外）
+!docs/important.md
+!.github/workflows/
+repository_summary.md
+
+# Terraform関連
+.terraform
+*.terraform.lock.hcl
+*.backup
+*.tfstate
+
+# Python仮想環境
+venv
+.venv
+
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
```

---

## ⏰ 01:40:34 - `df5c440`
**🗑️ 不要なスクリプトファイルを削除**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 01:40:34 2025 +0900
D	.github/scripts/README.md
D	.github/scripts/analyze-git-activity.sh
D	.github/scripts/calculate-week-info.sh
D	.github/scripts/create-docusaurus-structure.sh
D	.github/scripts/generate-markdown-reports.sh
D	.github/scripts/sync-to-hub-gh.sh
D	.github/scripts/sync-to-hub.sh
M	.github/workflows/sync-to-report-gh.yml
M	README.md
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 01:40:34 2025 +0900

    🗑️ 不要なスクリプトファイルを削除
    
    - .github/scripts/ ディレクトリ内のスクリプトを全て削除
    - GitHub Actionsワークフローがリモートスクリプトを使用するように変更済み
    - ローカルスクリプトは不要となったため削除

 .github/scripts/README.md                      | 141 -----------------
 .github/scripts/analyze-git-activity.sh        |  59 --------
 .github/scripts/calculate-week-info.sh         |  44 ------
 .github/scripts/create-docusaurus-structure.sh | 111 --------------
 .github/scripts/generate-markdown-reports.sh   | 201 -------------------------
 .github/scripts/sync-to-hub-gh.sh              | 182 ----------------------
 .github/scripts/sync-to-hub.sh                 | 184 ----------------------
 .github/workflows/sync-to-report-gh.yml        |  17 +--
 README.md                                      |   4 +
 9 files changed, 12 insertions(+), 931 deletions(-)
```

### 💻 Code Changes
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
```

---

## ⏰ 01:41:17 - `f8d6c78`
**🔀 Merge: 不要なスクリプトファイルの削除とワークフローの更新**
*by Maki*

### 📋 Changed Files
```bash
Merge: 60869c6 df5c440
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 01:41:17 2025 +0900
```

### 📊 Statistics
```bash
Merge: 60869c6 df5c440
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 01:41:17 2025 +0900

    🔀 Merge: 不要なスクリプトファイルの削除とワークフローの更新

 .github/scripts/README.md                      | 141 -----------------
 .github/scripts/analyze-git-activity.sh        |  59 --------
 .github/scripts/calculate-week-info.sh         |  44 ------
 .github/scripts/create-docusaurus-structure.sh | 111 --------------
 .github/scripts/generate-markdown-reports.sh   | 201 -------------------------
 .github/scripts/sync-to-hub-gh.sh              | 182 ----------------------
 .github/scripts/sync-to-hub.sh                 | 184 ----------------------
 .github/workflows/sync-to-report-gh.yml        |  17 +--
 README.md                                      |   4 +
 9 files changed, 12 insertions(+), 931 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 01:43:19 - `aea5093`
**📝 README.mdをテンプレートリポジトリ向けに更新**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 01:43:19 2025 +0900
M	README.md
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 01:43:19 2025 +0900

    📝 README.mdをテンプレートリポジトリ向けに更新
    
    - 開発リポジトリからテンプレートリポジトリへの変更
    - テンプレートの使い方と設定方法を明確化
    - GitHubのMarkdown注意書き形式を導入
    - 参考リンクとディレクトリ構成を更新

 README.md | 111 +++++++++++++++++++++++++++++++++++++-------------------------
 1 file changed, 67 insertions(+), 44 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/README.md b/README.md
index 6710e24..2b43334 100644
--- a/README.md
+++ b/README.md
@@ -3,7 +3,7 @@
 
 <div align="center">
 
-# daily-report-hub dev
+# Daily Report Hub Template
 
 <img src="https://img.shields.io/badge/GitHub%20Actions-CICD-blue?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
 <img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Bash" />
@@ -18,31 +18,27 @@
 
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
@@ -67,7 +63,7 @@ graph TB
 ### 📋 処理ステップ
 
 1. **トリガー**: **GitHub Actions**がmainブランチへのpushやPRをトリガー
-2. **データ収集**: `.github/scripts/`配下のシェルスクリプトで
+2. **データ収集**: リモートスクリプトで
    - 週情報の計算
    - Git活動の分析
    - Markdownレポートの生成
@@ -86,37 +82,52 @@ graph TB
 
 ---
 
-## 📝 主なスクリプト
+## 📝 主な機能
+
+> [!NOTE]
+> このテンプレートから作成されたリポジトリでは、以下の機能が自動で有効になります。
+
+### 🔄 自動実行されるスクリプト（リモート）
 
-- `.github/scripts/calculate-week-info.sh`  
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
```

---

