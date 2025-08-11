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

## ⏰ 23:28:30 - `2c8f5a1`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 23:28:30 2025 +0900
M	.github/workflows/sync-to-report-gh.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 23:28:30 2025 +0900

    Update sync-to-report-gh.yml

 .github/workflows/sync-to-report-gh.yml | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index 3688357..f2cefaf 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -1,4 +1,4 @@
-name: 📊 デイリーレポートハブ同期 v2.3 (YUKIHIKO PR版)
+name: 📊 デイリーレポートハブ同期 v2.4 (YUKIHIKO PR版)
 on:
   push:
     branches: [main, master]
```

---

## ⏰ 23:49:12 - `dd72c7f`
**🔥 おみくじアプリ関連ファイルを削除**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:49:12 2025 +0900
D	.env.example
D	index.html
D	memo.md
D	script.js
D	style.css
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:49:12 2025 +0900

    🔥 おみくじアプリ関連ファイルを削除

 .env.example |  15 ---------
 index.html   |  35 --------------------
 memo.md      |  47 --------------------------
 script.js    |  26 ---------------
 style.css    | 106 -----------------------------------------------------------
 5 files changed, 229 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.env.example b/.env.example
deleted file mode 100644
index 218c470..0000000
--- a/.env.example
+++ /dev/null
@@ -1,15 +0,0 @@
-# おみくじアプリ設定例
-# 実際の設定は .env ファイルに記載してください
-
-# アプリケーション設定
-APP_NAME=おみくじアプリ
-APP_VERSION=1.0.0
-
-# 将来的な機能拡張用
-# API_ENDPOINT=https://api.example.com
-# DEBUG_MODE=false
-# ANALYTICS_ID=your-analytics-id
-
-# GitHub Actions関連（必要に応じて）
-# GITHUB_TOKEN=your-github-token
-# REPORT_HUB_REPO=your-username/daily-report-hub
\ No newline at end of file
diff --git a/index.html b/index.html
deleted file mode 100644
index e7b086f..0000000
--- a/index.html
+++ /dev/null
@@ -1,35 +0,0 @@
-<!DOCTYPE html>
-<html lang="ja">
-<head>
-    <!-- 基本的なメタ情報 -->
-    <meta charset="UTF-8">
-    <meta name="viewport" content="width=device-width, initial-scale=1.0">
-    <meta name="description" content="シンプルなウェブベースのおみくじアプリケーション">
-    <meta name="keywords" content="おみくじ, 占い, ウェブアプリ">
-    <meta name="author" content="daily-report-hub_sample1">
-    
-    <title>おみくじアプリ ⛩️</title>
-    
-    <!-- スタイルシート -->
-    <link rel="stylesheet" href="style.css">
-    
-    <!-- ファビコン（将来的に追加予定） -->
-    <!-- <link rel="icon" type="image/x-icon" href="/favicon.ico"> -->
-</head>
-<body>
-    <!-- メインコンテナ -->
-    <div class="container">
-        <!-- アプリタイトル -->
-        <h1>おみくじ ⛩️</h1>
-        
-        <!-- おみくじを引くボタン -->
-        <button id="draw-button" aria-label="おみくじを引く">おみくじを引く</button>
-        
-        <!-- 結果表示エリア -->
-        <p id="result" aria-live="polite" role="status"></p>
-    </div>
-    
-    <!-- JavaScript -->
-    <script src="script.js"></script>
-</body>
-</html>
diff --git a/memo.md b/memo.md
deleted file mode 100644
index 5c9eae4..0000000
--- a/memo.md
+++ /dev/null
@@ -1,47 +0,0 @@
-既存の開発リポジトリのサンプル名を提案しますね！
-
-## フロントエンド系
-
-- `user-dashboard-app`
-- `e-commerce-frontend`
-- `react-admin-panel`
-- `mobile-app-ui`
-
-## バックエンド系
-
-- `api-gateway-service`
-- `user-management-api`
-- `payment-processing-service`
-- `notification-microservice`
-
-## フルスタック系
-
-- `task-management-system`
-- `inventory-tracker`
-- `blog-platform`
-- `chat-application`
-
-## ライブラリ・ツール系
-
-- `ui-component-library`
-- `data-validation-utils`
-- `logging-framework`
-- `config-management-tool`
-
-## インフラ・DevOps系
```

---

## ⏰ 23:49:23 - `5b0d58c`
**🗑️ ドキュメントファイルを削除**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:49:23 2025 +0900
D	CHANGELOG.md
D	CONTRIBUTING.md
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:49:23 2025 +0900

    🗑️ ドキュメントファイルを削除

 CHANGELOG.md    | 32 --------------------------------
 CONTRIBUTING.md | 51 ---------------------------------------------------
 2 files changed, 83 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/CHANGELOG.md b/CHANGELOG.md
deleted file mode 100644
index 20aeb24..0000000
--- a/CHANGELOG.md
+++ /dev/null
@@ -1,32 +0,0 @@
-# 📝 変更履歴
-
-このファイルは、プロジェクトの重要な変更を記録します。
-
-形式は [Keep a Changelog](https://keepachangelog.com/ja/1.0.0/) に基づいており、
-このプロジェクトは [セマンティック バージョニング](https://semver.org/lang/ja/) に準拠しています。
-
-## [Unreleased]
-
-### 追加
-- README.mdの視覚的改善（中央揃え、バッジ、ヘッダー画像）
-- スクリーンショットプレースホルダーの追加
-- JavaScriptファイルへの詳細コメント追加
-- おみくじ結果に応じた色分けスタイリング
-- .env.exampleファイルの追加
-- CONTRIBUTING.mdの追加
-- CHANGELOG.mdの追加（このファイル）
-
-### 変更
-- CSSにアニメーション効果を追加
-- プロジェクト構造の文書化を改善
-
-## [1.0.0] - 2025-01-XX
-
-### 追加
-- 基本的なおみくじ機能
-- シンプルなウェブインターフェース
-- GitHub Actions による日報同期機能
-- レスポンシブデザイン
-
-[Unreleased]: https://github.com/your-username/daily-report-hub_sample1/compare/v1.0.0...HEAD
-[1.0.0]: https://github.com/your-username/daily-report-hub_sample1/releases/tag/v1.0.0
\ No newline at end of file
diff --git a/CONTRIBUTING.md b/CONTRIBUTING.md
deleted file mode 100644
index 1962486..0000000
--- a/CONTRIBUTING.md
+++ /dev/null
@@ -1,51 +0,0 @@
-# 🤝 コントリビューションガイド
-
-おみくじアプリへの貢献をお考えいただき、ありがとうございます！
-
-## 📋 貢献方法
-
-### 🐛 バグ報告
-
-バグを発見した場合は、以下の情報を含めてIssueを作成してください：
-
-- 使用しているブラウザとバージョン
-- 再現手順
-- 期待される動作
-- 実際の動作
-- スクリーンショット（可能であれば）
-
-### 💡 機能提案
-
-新機能のアイデアがある場合は、以下を含めてIssueを作成してください：
-
-- 機能の詳細説明
-- 使用ケース
-- 実装の提案（任意）
-
-### 🔧 プルリクエスト
-
-1. このリポジトリをフォーク
-2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
-3. 変更をコミット (`git commit -m 'Add some amazing feature'`)
-4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
-5. プルリクエストを作成
-
-## 📝 コーディング規約
-
-- **HTML**: セマンティックなマークアップを心がける
-- **CSS**: BEMまたは類似の命名規則を使用
-- **JavaScript**: ESLintの推奨設定に従う
-- **コメント**: 複雑な処理には適切なコメントを追加
-
-## 🧪 テスト
-
-変更を行う前に、以下のブラウザでテストしてください：
-
-- Chrome (最新版)
-- Firefox (最新版)
-- Safari (最新版)
-- Edge (最新版)
-
-## 📄 ライセンス
-
-このプロジェクトに貢献することで、あなたの貢献が同じライセンスの下で配布されることに同意したものとみなされます。
\ No newline at end of file
```

---

## ⏰ 23:49:31 - `8199048`
**📝 .gitignoreを更新**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:49:31 2025 +0900
M	.gitignore
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:49:31 2025 +0900

    📝 .gitignoreを更新

 .gitignore | 1 +
 1 file changed, 1 insertion(+)
```

### 💻 Code Changes
```diff
diff --git a/.gitignore b/.gitignore
index b7faf40..16c3c78 100644
--- a/.gitignore
+++ b/.gitignore
@@ -205,3 +205,4 @@ cython_debug/
 marimo/_static/
 marimo/_lsp/
 __marimo__/
+.SourceSageAssets/
```

---

## ⏰ 23:49:35 - `67f5ffe`
**📝 README.mdを大幅リニューアル**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:49:35 2025 +0900
M	README.md
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:49:35 2025 +0900

    📝 README.mdを大幅リニューアル

 README.md | 141 ++++++++++++++++++++++++++++++++++++--------------------------
 1 file changed, 82 insertions(+), 59 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/README.md b/README.md
index e5baa3d..d0ce306 100644
--- a/README.md
+++ b/README.md
@@ -1,90 +1,113 @@
+# daily-report-hub_dev
+
 <div align="center">
 
-![](https://github.com/user-attachments/assets/f7afed43-1d98-4886-b2e0-57c99dd7874e)
+<img src="https://img.shields.io/badge/GitHub%20Actions-CICD-blue?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
+<img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Bash" />
 
-# daily-report-hub_sample1
+</div>
 
-<p>
-  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
-  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
-  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
-</p>
+---
 
-</div>
+## 📖 概要
 
-> [!IMPORTANT]
-> このリポジトリは、GitHub Actionsを利用してGitのコミット履歴から自動で日報を作成・集約するワークフローのサンプルです。
->
-> ここでの開発アクティビティ（コミットや差分）は、[`sync-to-report.yml`](./.github/workflows/sync-to-report.yml) ワークフローによって自動的に[`daily-report-hub`](https://github.com/Sunwood-ai-labs/daily-report-hub)リポジトリへレポートとして送信されます。
+このリポジトリは、**GitHub Actionsを活用してGitのコミット履歴から日報を自動生成し、集約用リポジトリ（[daily-report-hub](https://github.com/Sunwood-ai-labs/daily-report-hub)）へ同期するCICDワークフローのサンプル・テンプレートです。
 
-## おみくじアプリ ⛩️
+- **開発アクティビティの可視化・自動集約**
+- **週次・日次レポートの自動生成**
+- **PRベースの自動同期・自動承認・自動マージ対応**
 
-シンプルなウェブベースのおみくじアプリケーションです。あなたの今日の運勢を占ってみましょう！🔮
+---
 
-### 📸 スクリーンショット
+## 🚩 このリポジトリでできること
 
-<div align="center">
+- Gitのコミット履歴・差分から日報（Markdown形式）を自動生成
+- 週単位・日単位でレポートを整理
+- 別リポジトリ（daily-report-hub）へPRベースで自動同期
+- プルリクエストの自動承認・自動マージ（設定可）
+- Docusaurus用のディレクトリ・ナビゲーション構造も自動生成
 
-![App Screenshot](https://github.com/user-attachments/assets/fc8363f1-3a9f-4684-9b5d-b000a0a9a788)
+---
 
-</div>
+## ⚙️ ワークフロー概要
 
-### 🎮 遊び方
+1. **GitHub Actions**がmainブランチへのpushやPRをトリガー
+2. `.github/scripts/`配下のシェルスクリプトで
+    - 週情報の計算
+    - Git活動の分析
+    - Markdownレポートの生成
+    - Docusaurus用ディレクトリ構造の作成
+3. 集約用リポジトリ（daily-report-hub）をクローンし、レポートをコピー
+4. PR作成・自動承認・自動マージ（設定に応じて自動化）
 
-1️⃣ このリポジトリをクローンまたはダウンロードします。 💻
-2️⃣ `index.html`ファイルをウェブブラウザで開きます。 🌐
-3️⃣ 「おみくじを引く」ボタンをクリックすると、今日の運勢が表示されます。 ✨
+---
 
-### 🛠️ 技術仕様
+## 📝 主なスクリプト
 
-- **フロントエンド**: HTML5, CSS3, Vanilla JavaScript
-- **ブラウザ要件**: モダンブラウザ（Chrome, Firefox, Safari, Edge）
-- **依存関係**: なし
+- `.github/scripts/calculate-week-info.sh`  
+  週情報（週番号・開始日・終了日など）を計算し環境変数に出力
 
-### 📁 プロジェクト構造
+- `.github/scripts/analyze-git-activity.sh`  
+  Gitのコミット履歴・差分を分析し、生データファイルを生成
 
-```
-├── index.html              # メインHTMLファイル
-├── style.css               # スタイルシート
-├── script.js               # JavaScript処理
-├── .github/
-│   └── workflows/
-│       └── sync-to-report.yml  # 日報同期ワークフロー
-└── README.md               # このファイル
-```
+- `.github/scripts/generate-markdown-reports.sh`  
+  生データから日報・統計・差分などのMarkdownレポートを自動生成
 
-### 🚀 クイックスタート
+- `.github/scripts/create-docusaurus-structure.sh`  
+  Docusaurus用のディレクトリ・_category_.jsonを自動生成
 
```

---

## ⏰ 23:49:43 - `7f57ea4`
**🔀 Merge: Remove omikuji app and docs cleanup**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Merge: 2c8f5a1 67f5ffe
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:49:43 2025 +0900
```

### 📊 Statistics
```bash
Merge: 2c8f5a1 67f5ffe
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:49:43 2025 +0900

    🔀 Merge: Remove omikuji app and docs cleanup

 .env.example    |  15 ------
 .gitignore      |   1 +
 CHANGELOG.md    |  32 -------------
 CONTRIBUTING.md |  51 --------------------
 README.md       | 141 ++++++++++++++++++++++++++++++++------------------------
 index.html      |  35 --------------
 memo.md         |  47 -------------------
 script.js       |  26 -----------
 style.css       | 106 ------------------------------------------
 9 files changed, 83 insertions(+), 371 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 23:50:19 - `8a09816`
**✨ .SourceSageignoreファイルを新規追加**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:50:19 2025 +0900
A	.SourceSageignore
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:50:19 2025 +0900

    ✨ .SourceSageignoreファイルを新規追加

 .SourceSageignore | 54 ++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 54 insertions(+)
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
```

---

## ⏰ 23:50:26 - `8a3dda7`
**🔀 Merge: .SourceSageignoreファイル追加**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Merge: 7f57ea4 8a09816
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:50:26 2025 +0900
```

### 📊 Statistics
```bash
Merge: 7f57ea4 8a09816
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:50:26 2025 +0900

    🔀 Merge: .SourceSageignoreファイル追加

 .SourceSageignore | 54 ++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 54 insertions(+)
```

### 💻 Code Changes
```diff
```

---

