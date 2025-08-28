# 🔄 Latest Code Changes

```diff
diff --git a/README.ja.md b/README.ja.md
index 087a0b0..e0b1057 100644
--- a/README.ja.md
+++ b/README.ja.md
@@ -1,169 +1,27 @@
-<div align="center">
+# Prompt Books
 
-# Gemini Actions Lab
+Prompt Booksは、プロンプトを閲覧・検索できるウェブアプリケーションです。
 
-<a href="./README.md"><img src="https://img.shields.io/badge/English-Readme-blue?style=for-the-badge&logo=github&logoColor=white" alt="English" /></a>
-<a href="./README.ja.md"><img src="https://img.shields.io/badge/日本語-Readme-red?style=for-the-badge&logo=github&logoColor=white" alt="日本語" /></a>
+## 機能
 
-![Image](https://github.com/user-attachments/assets/1e294058-a1e6-4b44-979d-f4c8f09cb8ae)
+-   プロンプトの一覧表示
+-   タイトルや説明文でのプロンプト検索
 
-<img src="https://img.shields.io/badge/GitHub%20Actions-AI-blue?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
-<img src="https://img.shields.io/badge/Gemini-AI-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Gemini" />
-</div>
+## 使い方
 
----
+1.  `index.html`をウェブブラウザで開きます。
+2.  プロンプトの一覧が表示されます。
+3.  検索ボックスを使ってプロンプトを絞り込めます。
 
-## 📖 概要
-
-このリポジトリは、GoogleのGemini AIをGitHub Actionsと統合するための実験室およびショーケースとして機能します。生成AIの力を利用して、さまざまなリポジトリ管理タスクを自動化する方法を示します。
-
-### 🎯 主な機能
-- **AIによる自動化**: Geminiを活用して、Issueのトリアージ、プルリクエストのレビューなどのタスクを処理します。
-- **CLIライクな対話**: Issueのコメントから直接AIアシスタントと対話します。
-- **拡張可能なワークフロー**: 独自のプロジェクトに合わせてワークフローを簡単に適応およびカスタマイズできます。
-
----
-
-## 🤖 ワークフロー
-
-このリポジトリには、以下のGitHub Actionsワークフローが含まれています：
-
-### 📄 `gemini-cli-jp.yml`
-- **トリガー**: Issueのコメント
-- **機能**: ユーザーがIssueにコメント（例：`@gemini-cli-jp /do-something`）を作成することで、Gemini搭載のCLIアシスタントと対話できるようにします。アシスタントは、ユーザーのリクエストに基づいてリポジトリでアクションを実行できます。
-
-###  triage `gemini-issue-automated-triage.yml`
-- **トリガー**: Issueの作成または編集
-- **機能**: 新規または更新されたIssueを自動的にトリアージします。Geminiによって決定されたIssueの内容に基づいて、ラベルの追加、担当者の割り当て、またはコメントの投稿ができます。
-
-### 🕒 `gemini-issue-scheduled-triage.yml`
-- **トリガー**: スケジュールされたcronジョブ
-- **機能**: 定期的にオープンなIssueをスキャンし、古いIssueの特定や優先順位の提案などのトリアージタスクを実行します。
-
-### 🔍 `gemini-pr-review.yml`
-- **トリガー**: プルリクエストの作成または更新
-- **機能**: プルリクエストを自動的にレビューします。Geminiは、コードの品質に関するフィードバックの提供、改善の提案、または潜在的な問題の特定ができます。
-
-### 🔄 `sync-to-report-gh.yml`
-- **トリガー**: mainブランチへのプッシュ
-- **機能**: これは以前のテンプレートからのレガシーワークフローであり、このラボでは積極的に使用されていません。日次レポートを中央リポジトリに同期するように設計されていました。
-
----
-
-## 📸 スクリーンショットと例
-
-### 🤖 CLIの対話例
-Issueを作成し、`@gemini-cli-jp /help`とコメントして、利用可能なコマンドを確認します:
-
-\```
-@gemini-cli-jp /help
-\```
-
-AIアシスタントが利用可能なコマンドと使用例を返信します。
-
-### 🏗️ ワークフローのアーキテクチャ
-\```mermaid
-graph TD
-    A[GitHub Issue/PR] --> B[GitHub Actions トリガー]
-    B --> C[Gemini CLI ワークフロー]
-    C --> D[Gemini AI 処理]
-    D --> E[リポジトリ操作]
-    E --> F[自動応答]
-
-    G[スケジュール/Cron] --> H[自動トリアージ]
-    H --> I[Issue管理]
-
-    J[PR作成] --> K[PRレビューワークフロー]
-    K --> L[コード解析]
-    L --> M[フィードバックと提案]
-\```
-
-### 💬 対話の例
-
-**コードレビューのリクエスト:**
-\```
-@gemini-cli-jp /review-pr
-このプルリクエストをレビューし、改善点を提案してください
-\```
-
-**Issueのトリアージ:**
-\```
-@gemini-cli-jp /triage
-このIssueを分析し、適切なラベルと担当者を提案してください
-\```
-
----
-
-## 🛠️ トラブルシューティング
-
-### 一般的な問題
-
-**❌ ワークフローがトリガーされない:**
-- リポジトリの設定でGitHub Actionsが有効になっているか確認してください
-- リポジトリの設定でWebhookの配信を確認してください
-- トリガー条件（例：コメントに`@gemini-cli-jp`が含まれているか）が満たされているか確認してください
-
-**❌ Gemini APIのエラー:**
-- `GEMINI_API_KEY`シークレットが設定されているか確認してください
-- APIキーの権限とクォータを確認してください
-- APIキーが有効で期限切れでないことを確認してください
-
-**❌ 権限エラー:**
-- ユーザーに書き込み権限があることを確認してください
-- リポジトリがプライベートでないか確認してください（信頼されたユーザーの検出に影響します）
-
-### ヘルプの入手方法
-1. [GitHub Issues](https://github.com/your-repo/issues)で同様の問題がないか確認してください
-2. 詳細なエラーログを記載した新しいIssueを作成してください
-3. Issueを報告する際には、ワークフローの実行ログを含めてください
-
----
-
-## 🚀 インストールとセットアップ
-
-### 前提条件
-- リポジトリ作成権限のあるGitHubアカウント
-- Google AI StudioのGemini APIキー
-- GitHub Actionsの基本的な理解
-
-### クイックスタート
-1. **このリポジトリをフォーク**して、自分のGitHubアカウントにコピーします
-2. リポジトリの設定で**GitHubシークレットを設定**します:
-   - `GEMINI_API_KEY`: あなたのGemini APIキー
-   - `GITHUB_TOKEN`: (自動的に提供されます)
-3. `.github/workflows/`からあなたのリポジトリに**ワークフローファイルをコピー**します
-4. あなたのニーズに合わせて**ワークフローをカスタマイズ**します
-5. Issueを作成し、`@gemini-cli-jp /help`とコメントして**セットアップをテスト**します
-
-### 高度な設定
-追加機能を利用するには、これらのオプションのシークレットを設定します:
-- `APP_ID`と`APP_PRIVATE_KEY`: GitHub App連携用
-- `GCP_WIF_PROVIDER`と関連するGCP変数: Vertex AI利用のため
-
----
-
-## 📁 ディレクトリ構造
+## ディレクトリ構造
 
 \```
 .
-├── .github/
-│   └── workflows/
-│       ├── gemini-cli-jp.yml
-│       ├── gemini-issue-automated-triage.yml
-│       ├── gemini-issue-scheduled-triage.yml
-│       ├── gemini-pr-review.yml
-│       └── sync-to-report-gh.yml
-├── .gitignore
-├── LICENSE
-└── README.md
+├── index.html
+├── style.css
+└── script.js
 \```
 
----
-
-## 📝 ライセンス
+## ライセンス
 
 このプロジェクトは、[LICENSE](LICENSE)ファイルの条件に基づいてライセンスされています。
-
----
-
-© 2025 Sunwood-ai-labsII
\ No newline at end of file
diff --git a/README.md b/README.md
index ca6ca29..1ea32ab 100644
--- a/README.md
+++ b/README.md
@@ -1,169 +1,27 @@
-<div align="center">
+# Prompt Books
 
-# Gemini Actions Lab
+Prompt Books is a web application that allows you to browse and search for prompts.
 
-<a href="./README.md"><img src="https://img.shields.io/badge/English-Readme-blue?style=for-the-badge&logo=github&logoColor=white" alt="English" /></a>
-<a href="./README.ja.md"><img src="https://img.shields.io/badge/日本語-Readme-red?style=for-the-badge&logo=github&logoColor=white" alt="日本語" /></a>
+## Features
 
-![Image](https://github.com/user-attachments/assets/1e294058-a1e6-4b44-979d-f4c8f09cb8ae)
+-   Browse a list of prompts
+-   Search for prompts by title or description
 
-<img src="https://img.shields.io/badge/GitHub%20Actions-AI-blue?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
-<img src="https://img.shields.io/badge/Gemini-AI-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Gemini" />
-</div>
+## Usage
 
----
+1.  Open `index.html` in your web browser.
+2.  The list of prompts will be displayed.
+3.  Use the search box to filter the prompts.
 
-## 📖 Overview
-
-This repository serves as a laboratory and showcase for integrating Google's Gemini AI with GitHub Actions. It demonstrates how to automate various repository management tasks using the power of generative AI.
-
-### 🎯 Key Features
-- **AI-Powered Automation**: Leverage Gemini to handle tasks like issue triage, pull request reviews, and more.
-- **CLI-like Interaction**: Interact with the AI assistant directly from issue comments.
-- **Extensible Workflows**: Easily adapt and customize the workflows for your own projects.
-
----
-
-## 🤖 Workflows
-
-This repository includes the following GitHub Actions workflows:
-
-### 📄 `gemini-cli-jp.yml`
-- **Trigger**: Issue comments
-- **Function**: Allows users to interact with a Gemini-powered CLI assistant by creating comments on issues (e.g., `@gemini-cli-jp /do-something`). The assistant can then perform actions on the repository based on the user's request.
-
-###  triage `gemini-issue-automated-triage.yml`
-- **Trigger**: Issue creation or edits
-- **Function**: Automatically triages new or updated issues. It can add labels, assignees, or post comments based on the issue's content as determined by Gemini.
-
-### 🕒 `gemini-issue-scheduled-triage.yml`
-- **Trigger**: Scheduled cron job
-- **Function**: Periodically scans open issues and performs triage tasks, such as identifying stale issues or suggesting priorities.
-
-### 🔍 `gemini-pr-review.yml`
-- **Trigger**: Pull request creation or updates
-- **Function**: Automatically reviews pull requests. Gemini can provide feedback on code quality, suggest improvements, or identify potential issues.
-
-### 🔄 `sync-to-report-gh.yml`
-- **Trigger**: Push to the main branch
-- **Function**: This is a legacy workflow from a previous template and is not actively used in this lab. It was designed to sync daily reports to a central repository.
-
----
-
-## 📸 Screenshots & Examples
-
-### 🤖 CLI Interaction Example
-Create an issue and comment with `@gemini-cli /help` to see available commands:
-
-\```
-@gemini-cli /help
-\```
-
-The AI assistant will respond with available commands and usage examples.
-
-### 🏗️ Workflow Architecture
-\```mermaid
-graph TD
-    A[GitHub Issue/PR] --> B[GitHub Actions Trigger]
-    B --> C[Gemini CLI Workflow]
-    C --> D[Gemini AI Processing]
-    D --> E[Repository Actions]
-    E --> F[Automated Response]
-
-    G[Schedule/Cron] --> H[Automated Triage]
-    H --> I[Issue Management]
-
-    J[PR Created] --> K[PR Review Workflow]
-    K --> L[Code Analysis]
-    L --> M[Feedback & Suggestions]
-\```
-
-### 💬 Example Interactions
-
-**Code Review Request:**
-\```
-@gemini-cli /review-pr
-Please review this pull request and suggest improvements
-\```
-
-**Issue Triage:**
-\```
-@gemini-cli /triage
-Analyze this issue and suggest appropriate labels and assignees
-\```
-
----
-
-## 🛠️ Troubleshooting
-
-### Common Issues
-
-**❌ Workflow not triggering:**
-- Check if GitHub Actions are enabled in repository settings
-- Verify webhook delivery in repository settings
-- Ensure the trigger conditions are met (e.g., `@gemini-cli` in comment)
-
-**❌ Gemini API errors:**
-- Verify `GEMINI_API_KEY` secret is configured
-- Check API key permissions and quota
-- Ensure the API key is valid and not expired
-
-**❌ Permission errors:**
-- Confirm the user has write permissions
-- Check if the repository is private (affects trusted user detection)
-
-### Getting Help
-1. Check the [GitHub Issues](https://github.com/your-repo/issues) for similar problems
-2. Create a new issue with detailed error logs
-3. Include workflow run logs when reporting issues
-
----
-
-## 🚀 Installation & Setup
-
-### Prerequisites
-- GitHub account with repository creation permissions
-- Gemini API key from Google AI Studio
-- Basic understanding of GitHub Actions
-
-### Quick Start
-1. **Fork this repository** to your GitHub account
-2. **Configure GitHub Secrets** in your repository settings:
-   - `GEMINI_API_KEY`: Your Gemini API key
-   - `GITHUB_TOKEN`: (automatically provided)
-3. **Copy workflow files** from `.github/workflows/` to your repository
-4. **Customize workflows** according to your needs
-5. **Test the setup** by creating an issue and commenting `@gemini-cli /help`
-
-### Advanced Configuration
-For additional features, configure these optional secrets:
-- `APP_ID` and `APP_PRIVATE_KEY`: For GitHub App integration
-- `GCP_WIF_PROVIDER` and related GCP variables: For Vertex AI usage
-
----
-
-## 📁 Directory Structure
+## Directory Structure
 
 \```
 .
-├── .github/
-│   └── workflows/
-│       ├── gemini-cli-jp.yml
-│       ├── gemini-issue-automated-triage.yml
-│       ├── gemini-issue-scheduled-triage.yml
-│       ├── gemini-pr-review.yml
-│       └── sync-to-report-gh.yml
-├── .gitignore
-├── LICENSE
-└── README.md
+├── index.html
+├── style.css
+└── script.js
 \```
 
----
-
-## 📝 License
+## License
 
 This project is licensed under the terms of the [LICENSE](LICENSE) file.
-
----
-
-© 2025 Sunwood-ai-labsII
\ No newline at end of file
diff --git a/index.html b/index.html
index 55cb102..95813bf 100644
--- a/index.html
+++ b/index.html
@@ -7,10 +7,13 @@
     <link rel="stylesheet" href="style.css">
 </head>
 <body>
-    <h1>Prompt Books</h1>
-
-    <div id="app"></div>
-
+    <header>
+        <h1>Prompt Books</h1>
+        <input type="search" id="search-box" placeholder="Search prompts...">
+    </header>
+    <main>
+        <div id="prompt-list"></div>
+    </main>
     <script src="script.js"></script>
 </body>
 </html>
\ No newline at end of file
diff --git a/plan.md b/plan.md
new file mode 100644
index 0000000..ab0faf8
--- /dev/null
+++ b/plan.md
@@ -0,0 +1,6 @@
+### 計画
+- [ ] `index.html` に、プロンプトを表示するためのUI（リストや検索バーなど）を実装する。
+- [ ] `script.js` に、プロンプトデータを取得し、表示するロジックを実装する。
+- [ ] `style.css` に、基本的なスタイリングを追加する。
+- [ ] `README.md` と `README.ja.md` を、作成するアプリケーション「Prompt Books」の説明に書き換える。
+- [ ] 変更内容を新しいブランチにコミットし、プルリクエストを作成する。
\ No newline at end of file
diff --git a/script.js b/script.js
index 8938b43..f886206 100644
--- a/script.js
+++ b/script.js
@@ -1 +1,49 @@
-console.log("Hello from script.js!");
\ No newline at end of file
+const prompts = [
+    {
+        title: "ブログ記事のアイデア出し",
+        description: "新しいブログ記事のアイデアを10個生成します。",
+        prompt: "新しいブログ記事のアイデアを10個考えてください。"
+    },
+    {
+        title: "メールの件名作成",
+        description: "マーケティングメールの件名を5個提案します。",
+        prompt: "製品Xの発売に関するマーケティングメールの件名を5個提案してください。"
+    },
+    {
+        title: "コードのリファクタリング",
+        description: "指定されたコードをより効率的にリファクタリングします。",
+        prompt: "以下のPythonコードをリファクタリングしてください：\n\n[コード]"
+    },
+    {
+        title: "SNS投稿文の作成",
+        description: "新機能に関するSNS投稿文を作成します。",
+        prompt: "新機能Yについての魅力的なInstagram投稿文を作成してください。"
+    }
+];
+
+const promptList = document.getElementById('prompt-list');
+const searchBox = document.getElementById('search-box');
+
+function displayPrompts(filteredPrompts) {
+    promptList.innerHTML = '';
+    filteredPrompts.forEach(prompt => {
+        const card = document.createElement('div');
+        card.className = 'prompt-card';
+        card.innerHTML = `
+            <h2>${prompt.title}</h2>
+            <p>${prompt.description}</p>
+        `;
+        promptList.appendChild(card);
+    });
+}
+
+searchBox.addEventListener('input', (e) => {
+    const searchTerm = e.target.value.toLowerCase();
+    const filteredPrompts = prompts.filter(prompt => 
+        prompt.title.toLowerCase().includes(searchTerm) || 
+        prompt.description.toLowerCase().includes(searchTerm)
+    );
+    displayPrompts(filteredPrompts);
+});
+
+displayPrompts(prompts);
diff --git a/style.css b/style.css
index f302add..21d652a 100644
--- a/style.css
+++ b/style.css
@@ -1,8 +1,40 @@
 body {
     font-family: sans-serif;
+    margin: 0;
+    background-color: #f0f0f0;
 }
 
-#app {
+header {
+    background-color: #333;
+    color: white;
+    padding: 1rem;
+    text-align: center;
+}
+
+#search-box {
     width: 80%;
-    margin: 0 auto;
-}
\ No newline at end of file
+    padding: 0.5rem;
+    border-radius: 5px;
+    border: 1px solid #ccc;
+}
+
+main {
+    padding: 1rem;
+}
+
+#prompt-list {
+    display: grid;
+    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
+    gap: 1rem;
+}
+
+.prompt-card {
+    background-color: white;
+    border-radius: 5px;
+    padding: 1rem;
+    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
+}
+
+.prompt-card h2 {
+    margin-top: 0;
+}
```
