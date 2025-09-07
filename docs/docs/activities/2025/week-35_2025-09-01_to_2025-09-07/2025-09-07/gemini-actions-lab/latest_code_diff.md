# 🔄 Latest Code Changes

```diff
diff --git a/README.ja.md b/README.ja.md
deleted file mode 100644
index 56a17a7..0000000
--- a/README.ja.md
+++ /dev/null
@@ -1,171 +0,0 @@
-<div align="center">
-
-# Gemini Actions Lab
-
-<a href="./README.md"><img src="https://img.shields.io/badge/English-Readme-blue?style=for-the-badge&logo=github&logoColor=white" alt="English" /></a>
-<a href="./README.ja.md"><img src="https://img.shields.io/badge/日本語-Readme-red?style=for-the-badge&logo=github&logoColor=white" alt="日本語" /></a>
-
-[![💬 Gemini CLI](https://github.com/Sunwood-ai-labsII/gemini-actions-lab/actions/workflows/gemini-cli.yml/badge.svg)](https://github.com/Sunwood-ai-labsII/gemini-actions-lab/actions/workflows/gemini-cli.yml)
-
-![Image](https://github.com/user-attachments/assets/1e294058-a1e6-4b44-979d-f4c8f09cb8ae)
-
-<img src="https://img.shields.io/badge/GitHub%20Actions-AI-blue?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
-<img src="https://img.shields.io/badge/Gemini-AI-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Gemini" />
-</div>
-
----
-
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
-
-\```
-.
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
-\```
-
----
-
-## 📝 ライセンス
-
-このプロジェクトは、[LICENSE](LICENSE)ファイルの条件に基づいてライセンスされています。
-
----
-
-© 2025 Sunwood-ai-labsII
\ No newline at end of file
diff --git a/README.md b/README.md
index 6ce4bca..a4c7124 100644
--- a/README.md
+++ b/README.md
@@ -15,136 +15,136 @@
 
 ---
 
-## 📖 Overview
+## 📖 概要
 
-This repository serves as a laboratory and showcase for integrating Google's Gemini AI with GitHub Actions. It demonstrates how to automate various repository management tasks using the power of generative AI.
+このリポジトリは、GoogleのGemini AIをGitHub Actionsと統合するための実験室およびショーケースとして機能します。生成AIの力を利用して、さまざまなリポジトリ管理タスクを自動化する方法を示します。
 
-### 🎯 Key Features
-- **AI-Powered Automation**: Leverage Gemini to handle tasks like issue triage, pull request reviews, and more.
-- **CLI-like Interaction**: Interact with the AI assistant directly from issue comments.
-- **Extensible Workflows**: Easily adapt and customize the workflows for your own projects.
+### 🎯 主な機能
+- **AIによる自動化**: Geminiを活用して、Issueのトリアージ、プルリクエストのレビューなどのタスクを処理します。
+- **CLIライクな対話**: Issueのコメントから直接AIアシスタントと対話します。
+- **拡張可能なワークフロー**: 独自のプロジェクトに合わせてワークフローを簡単に適応およびカスタマイズできます。
 
 ---
 
-## 🤖 Workflows
+## 🤖 ワークフロー
 
-This repository includes the following GitHub Actions workflows:
+このリポジトリには、以下のGitHub Actionsワークフローが含まれています：
 
 ### 📄 `gemini-cli-jp.yml`
-- **Trigger**: Issue comments
-- **Function**: Allows users to interact with a Gemini-powered CLI assistant by creating comments on issues (e.g., `@gemini-cli-jp /do-something`). The assistant can then perform actions on the repository based on the user's request.
+- **トリガー**: Issueのコメント
+- **機能**: ユーザーがIssueにコメント（例：`@gemini-cli-jp /do-something`）を作成することで、Gemini搭載のCLIアシスタントと対話できるようにします。アシスタントは、ユーザーのリクエストに基づいてリポジトリでアクションを実行できます。
 
 ###  triage `gemini-issue-automated-triage.yml`
-- **Trigger**: Issue creation or edits
-- **Function**: Automatically triages new or updated issues. It can add labels, assignees, or post comments based on the issue's content as determined by Gemini.
+- **トリガー**: Issueの作成または編集
+- **機能**: 新規または更新されたIssueを自動的にトリアージします。Geminiによって決定されたIssueの内容に基づいて、ラベルの追加、担当者の割り当て、またはコメントの投稿ができます。
 
 ### 🕒 `gemini-issue-scheduled-triage.yml`
-- **Trigger**: Scheduled cron job
-- **Function**: Periodically scans open issues and performs triage tasks, such as identifying stale issues or suggesting priorities.
+- **トリガー**: スケジュールされたcronジョブ
+- **機能**: 定期的にオープンなIssueをスキャンし、古いIssueの特定や優先順位の提案などのトリアージタスクを実行します。
 
 ### 🔍 `gemini-pr-review.yml`
-- **Trigger**: Pull request creation or updates
-- **Function**: Automatically reviews pull requests. Gemini can provide feedback on code quality, suggest improvements, or identify potential issues.
+- **トリガー**: プルリクエストの作成または更新
+- **機能**: プルリクエストを自動的にレビューします。Geminiは、コードの品質に関するフィードバックの提供、改善の提案、または潜在的な問題の特定ができます。
 
 ### 🔄 `sync-to-report-gh.yml`
-- **Trigger**: Push to the main branch
-- **Function**: This is a legacy workflow from a previous template and is not actively used in this lab. It was designed to sync daily reports to a central repository.
+- **トリガー**: mainブランチへのプッシュ
+- **機能**: これは以前のテンプレートからのレガシーワークフローであり、このラボでは積極的に使用されていません。日次レポートを中央リポジトリに同期するように設計されていました。
 
 ---
 
-## 📸 Screenshots & Examples
+## 📸 スクリーンショットと例
 
-### 🤖 CLI Interaction Example
-Create an issue and comment with `@gemini-cli /help` to see available commands:
+### 🤖 CLIの対話例
+Issueを作成し、`@gemini-cli-jp /help`とコメントして、利用可能なコマンドを確認します:
 
 \```
-@gemini-cli /help
+@gemini-cli-jp /help
 \```
 
-The AI assistant will respond with available commands and usage examples.
+AIアシスタントが利用可能なコマンドと使用例を返信します。
 
-### 🏗️ Workflow Architecture
+### 🏗️ ワークフローのアーキテクチャ
 \```mermaid
 graph TD
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
+    A[GitHub Issue/PR] --> B[GitHub Actions トリガー]
+    B --> C[Gemini CLI ワークフロー]
+    C --> D[Gemini AI 処理]
+    D --> E[リポジトリ操作]
+    E --> F[自動応答]
+
+    G[スケジュール/Cron] --> H[自動トリアージ]
+    H --> I[Issue管理]
+
+    J[PR作成] --> K[PRレビューワークフロー]
+    K --> L[コード解析]
+    L --> M[フィードバックと提案]
 \```
 
-### 💬 Example Interactions
+### 💬 対話の例
 
-**Code Review Request:**
+**コードレビューのリクエスト:**
 \```
-@gemini-cli /review-pr
-Please review this pull request and suggest improvements
+@gemini-cli-jp /review-pr
+このプルリクエストをレビューし、改善点を提案してください
 \```
 
-**Issue Triage:**
+**Issueのトリアージ:**
 \```
-@gemini-cli /triage
-Analyze this issue and suggest appropriate labels and assignees
+@gemini-cli-jp /triage
+このIssueを分析し、適切なラベルと担当者を提案してください
 \```
 
 ---
 
-## 🛠️ Troubleshooting
+## 🛠️ トラブルシューティング
 
-### Common Issues
+### 一般的な問題
 
-**❌ Workflow not triggering:**
-- Check if GitHub Actions are enabled in repository settings
-- Verify webhook delivery in repository settings
-- Ensure the trigger conditions are met (e.g., `@gemini-cli` in comment)
+**❌ ワークフローがトリガーされない:**
+- リポジトリの設定でGitHub Actionsが有効になっているか確認してください
+- リポジトリの設定でWebhookの配信を確認してください
+- トリガー条件（例：コメントに`@gemini-cli-jp`が含まれているか）が満たされているか確認してください
 
-**❌ Gemini API errors:**
-- Verify `GEMINI_API_KEY` secret is configured
-- Check API key permissions and quota
-- Ensure the API key is valid and not expired
+**❌ Gemini APIのエラー:**
+- `GEMINI_API_KEY`シークレットが設定されているか確認してください
+- APIキーの権限とクォータを確認してください
+- APIキーが有効で期限切れでないことを確認してください
 
-**❌ Permission errors:**
-- Confirm the user has write permissions
-- Check if the repository is private (affects trusted user detection)
+**❌ 権限エラー:**
+- ユーザーに書き込み権限があることを確認してください
+- リポジトリがプライベートでないか確認してください（信頼されたユーザーの検出に影響します）
 
-### Getting Help
-1. Check the [GitHub Issues](https://github.com/your-repo/issues) for similar problems
-2. Create a new issue with detailed error logs
-3. Include workflow run logs when reporting issues
+### ヘルプの入手方法
+1. [GitHub Issues](https://github.com/your-repo/issues)で同様の問題がないか確認してください
+2. 詳細なエラーログを記載した新しいIssueを作成してください
+3. Issueを報告する際には、ワークフローの実行ログを含めてください
 
 ---
 
-## 🚀 Installation & Setup
+## 🚀 インストールとセットアップ
 
-### Prerequisites
-- GitHub account with repository creation permissions
-- Gemini API key from Google AI Studio
-- Basic understanding of GitHub Actions
+### 前提条件
+- リポジトリ作成権限のあるGitHubアカウント
+- Google AI StudioのGemini APIキー
+- GitHub Actionsの基本的な理解
 
-### Quick Start
-1. **Fork this repository** to your GitHub account
-2. **Configure GitHub Secrets** in your repository settings:
-   - `GEMINI_API_KEY`: Your Gemini API key
-   - `GITHUB_TOKEN`: (automatically provided)
-3. **Copy workflow files** from `.github/workflows/` to your repository
-4. **Customize workflows** according to your needs
-5. **Test the setup** by creating an issue and commenting `@gemini-cli /help`
+### クイックスタート
+1. **このリポジトリをフォーク**して、自分のGitHubアカウントにコピーします
+2. リポジトリの設定で**GitHubシークレットを設定**します:
+   - `GEMINI_API_KEY`: あなたのGemini APIキー
+   - `GITHUB_TOKEN`: (自動的に提供されます)
+3. `.github/workflows/`からあなたのリポジトリに**ワークフローファイルをコピー**します
+4. あなたのニーズに合わせて**ワークフローをカスタマイズ**します
+5. Issueを作成し、`@gemini-cli-jp /help`とコメントして**セットアップをテスト**します
 
-### Advanced Configuration
-For additional features, configure these optional secrets:
-- `APP_ID` and `APP_PRIVATE_KEY`: For GitHub App integration
-- `GCP_WIF_PROVIDER` and related GCP variables: For Vertex AI usage
+### 高度な設定
+追加機能を利用するには、これらのオプションのシークレットを設定します:
+- `APP_ID`と`APP_PRIVATE_KEY`: GitHub App連携用
+- `GCP_WIF_PROVIDER`と関連するGCP変数: Vertex AI利用のため
 
 ---
 
-## 📁 Directory Structure
+## 📁 ディレクトリ構造
 
 \```
 .
@@ -155,6 +155,11 @@ For additional features, configure these optional secrets:
 │       ├── gemini-issue-scheduled-triage.yml
 │       ├── gemini-pr-review.yml
 │       └── sync-to-report-gh.yml
+├── discord-issue-bot/
+│   ├── Dockerfile
+│   ├── pyproject.toml
+│   ├── compose.yaml
+│   └── bot.py
 ├── .gitignore
 ├── LICENSE
 └── README.md
@@ -162,10 +167,35 @@ For additional features, configure these optional secrets:
 
 ---
 
-## 📝 License
+## 📝 ライセンス
 
-This project is licensed under the terms of the [LICENSE](LICENSE) file.
+このプロジェクトは、[LICENSE](LICENSE)ファイルの条件に基づいてライセンスされています。
 
 ---
 
-© 2025 Sunwood-ai-labsII
\ No newline at end of file
+© 2025 Sunwood-ai-labsII
+
+
+---
+
+## 🤖 Discord Issue Bot（ワークフロー不要・最小構成）
+
+- 直に GitHub REST API で Issue を作成する最小ボットです。
+- 必要な環境変数は 2 つのみ: `DISCORD_BOT_TOKEN`, `GITHUB_TOKEN`。
+
+使い方:
+\```
+export DISCORD_BOT_TOKEN=xxxx
+export GITHUB_TOKEN=ghp_xxx
+cd discord-issue-bot
+docker compose -f compose.yaml up -d --build
+\```
+
+Discord で投稿（例）:
+\```
+!issue owner/repo "バグ: 保存できない" 再現手順… #kind/bug +maki
+\```
+ルール:
+- 先頭 `!issue`、直後に `owner/repo` を含める
+- タイトルは "ダブルクオート" で囲む（未指定時は1行目をタイトル）
+- `#label` がラベル、`+user` がアサイン
diff --git a/discord-issue-bot/.env.example b/discord-issue-bot/.env.example
new file mode 100644
index 0000000..c4bf152
--- /dev/null
+++ b/discord-issue-bot/.env.example
@@ -0,0 +1,7 @@
+# Required
+DISCORD_BOT_TOKEN=your_discord_bot_token_here
+GITHUB_TOKEN=ghp_your_github_token_here
+
+# Optional
+# GITHUB_API=https://api.github.com
+# DISCORD_MESSAGE_PREFIX=!issue
diff --git a/discord-issue-bot/Dockerfile b/discord-issue-bot/Dockerfile
new file mode 100644
index 0000000..52331ab
--- /dev/null
+++ b/discord-issue-bot/Dockerfile
@@ -0,0 +1,10 @@
+FROM ghcr.io/astral-sh/uv:python3.13-bookworm
+
+ENV PYTHONDONTWRITEBYTECODE=1 \
+    PYTHONUNBUFFERED=1
+
+WORKDIR /app
+COPY pyproject.toml ./
+RUN uv sync
+COPY . .
+CMD ["uv", "run", "bot.py"]
diff --git a/discord-issue-bot/README.md b/discord-issue-bot/README.md
new file mode 100644
index 0000000..e6c2d1f
--- /dev/null
+++ b/discord-issue-bot/README.md
@@ -0,0 +1,92 @@
+# Discord Issue Bot (Simple)
+
+シンプルな Discord ボットです。Discord のチャットから直接 GitHub Issue を作成します（ワークフロー不要）。
+
+必要な環境変数は 2 つだけ:
+- `DISCORD_BOT_TOKEN`
+- `GITHUB_TOKEN`（プライベートリポの場合は `repo` 権限推奨）
+
+## 使い方
+
+1) 環境変数を設定
+
+\```bash
+export DISCORD_BOT_TOKEN=xxxx
+export GITHUB_TOKEN=ghp_xxx
+\```
+
+2) Docker で起動（uv sync により依存を自動セットアップ）
+
+\```bash
+cd discord-issue-bot
+docker compose -f compose.yaml up -d --build
+docker compose -f compose.yaml logs -f
+\```
+
+3) Discord で投稿（例）
+
+\```
+!issue owner/repo "バグ: 保存できない" 再現手順… #kind/bug #priority/p2 +maki
+\```
+
+書式:
+- プレフィックス: `!issue`
+- 最初に `owner/repo` を必ず含める
+- タイトルは `"ダブルクオート"` で囲むと1行で指定可能（未指定なら1行目がタイトル、2行目以降が本文）
+- `#label` でラベル、`+user` でアサイン
+
+### Discord でのチャット例
+
+以下は、実際に Discord 上でボットに話しかけて Issue を作成する際の例です。
+
+- 1行で完結（タイトルをダブルクオートで囲む）
+
+\```
+!issue Sunwood-ai-labsII/gemini-actions-lab "バグ: セーブできない" 再現手順を書きます。 #bug #p2 +your-github-username
+\```
+
+- 複数行で本文をしっかり書く（1行目がタイトル、2行目以降が本文）
+
+\```
+!issue Sunwood-ai-labsII/gemini-actions-lab
+エディタがクラッシュする
+特定のファイルを開いた直後にクラッシュします。
+再現手順:
+1. プロジェクトを開く
+2. settings.json を開く
+3. 5秒後にクラッシュ
+#bug #crash +your-github-username
+\```
+
+- ラベルやアサインを省略してシンプルに
+
+\```
+!issue Sunwood-ai-labsII/gemini-actions-lab "ドキュメントを更新" README の手順が古いので更新してください。
+\```
+
+ヒント:
+- 既定のプレフィックスは `!issue` です。変更したい場合は環境変数 `DISCORD_MESSAGE_PREFIX` を設定してください。
+- ボットは作成に成功すると Issue の URL を返信します。メッセージへのリンク（jump URL）は本文末尾に自動で記録されます。
+- ギルド（サーバー）内でボットがメッセージ本文を読むには、Developer Portal で「Message Content Intent」を ON にしてください（下記「Discord 設定（特権インテント）」参照）。
+
+## 実装
+- `bot.py`: Discord メッセージをパースし、GitHub API (`POST /repos/{owner}/{repo}/issues`) に直接作成
+- 依存: `discord.py`
+- ビルド: `Dockerfile`（uv インストール → `uv sync` → `uv run bot.py`）
+
+## Discord 設定（特権インテント）
+- 本ボットはメッセージ本文を読むため、Discord の「Message Content Intent（特権インテント）」が必要です。
+- 設定手順:
+  - https://discord.com/developers/applications で対象アプリを開く
+  - 左メニュー「Bot」→ Privileged Gateway Intents → 「MESSAGE CONTENT INTENT」を ON
+  - 「Save Changes」で保存
+- 反映後、コンテナを再起動してください（例: `docker compose up -d --build` または `docker-compose up --build`）。
+
+## トラブルシューティング
+- 起動時に以下のエラーが出る場合:
+  - `discord.errors.PrivilegedIntentsRequired: ... requesting privileged intents ... enable the privileged intents ...`
+  - 上記「Discord 設定（特権インテント）」の手順で「Message Content Intent」を有効化してください。
+- 応急処置（動作制限あり）:
+  - `bot.py` の `intents.message_content = True` を外す/`False` にすると接続自体は通りますが、ギルド内のメッセージ本文を読めず、本ボットのコマンドは動作しません。
+- 代替案:
+  - スラッシュコマンドに移行すると、Message Content Intent なしでも運用できます（実装変更が必要）。
diff --git a/discord-issue-bot/bot.py b/discord-issue-bot/bot.py
new file mode 100644
index 0000000..b41e924
--- /dev/null
+++ b/discord-issue-bot/bot.py
@@ -0,0 +1,141 @@
+#!/usr/bin/env python3
+import os
+import re
+import json
+from urllib import request, error
+
+import discord
+
+DISCORD_TOKEN = os.environ.get("DISCORD_BOT_TOKEN", "")
+GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_PAT")
+GITHUB_API = os.environ.get("GITHUB_API", "https://api.github.com")
+
+PREFIX = os.environ.get("DISCORD_MESSAGE_PREFIX", "!issue").strip()
+
+
+def http_post(url: str, token: str, payload: dict):
+    data = json.dumps(payload).encode("utf-8")
+    req = request.Request(url, data=data, method="POST")
+    req.add_header("Authorization", f"Bearer {token}")
+    req.add_header("Accept", "application/vnd.github+json")
+    req.add_header("Content-Type", "application/json")
+    try:
+        with request.urlopen(req) as resp:
+            body = resp.read().decode("utf-8")
+            return resp.status, body
+    except error.HTTPError as e:
+        body = e.read().decode("utf-8", errors="replace") if e.fp else ""
+        return e.code, body
+
+
+def parse(content: str):
+    """
+    Syntax (simple):
+      !issue owner/repo "Title" Body text ... #label1 +assignee1
+    or  !issue owner/repo Title on first line\nBody from second line ... #bug
+    Returns: dict(repo, title, body, labels[], assignees[])
+    """
+    text = content.strip()
+    if text.lower().startswith(PREFIX.lower()):
+        text = text[len(PREFIX):].strip()
+
+    # Find first owner/repo token
+    m_repo = re.search(r"\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b", text)
+    repo = m_repo.group(1) if m_repo else ""
+    if not repo:
+        return {"error": "リポジトリ (owner/repo) を含めてください: 例) !issue owner/repo \"タイトル\" 本文"}
+
+    # Remove repo from text before parsing title/body
+    text_wo_repo = (text[:m_repo.start()] + text[m_repo.end():]).strip() if m_repo else text
+
+    # Title/body parsing
+    m = re.match(r'^"([^"]+)"\s*(.*)$', text_wo_repo, flags=re.S)
+    if m:
+        title = m.group(1).strip()
+        body = m.group(2).strip()
+    else:
+        lines = text_wo_repo.splitlines()
+        title = lines[0].strip() if lines else "New Issue"
+        body = "\n".join(lines[1:]).strip()
+
+    # Extract labels (#label) and assignees (+user)
+    labels = [tok[1:].strip() for tok in re.findall(r'(#[\w\-/\.]+)', text_wo_repo)]
+    assignees = [tok[1:].strip() for tok in re.findall(r'(\+[A-Za-z0-9-]+)', text_wo_repo)]
+
+    # Clean tokens from body
+    body = re.sub(r'(#[\w\-/\.]+)', '', body)
+    body = re.sub(r'(\+[A-Za-z0-9-]+)', '', body).strip()
+
+    return {
+        "repo": repo,
+        "title": title or "New Issue",
+        "body": body or "(no body)",
+        "labels": list(dict.fromkeys(labels)),
+        "assignees": list(dict.fromkeys(assignees)),
+    }
+
+
+def build_body_with_footer(body: str, author: str, source_url: str | None):
+    parts = [body]
+    meta = []
+    if author:
+        meta.append(f"Reported via Discord by: {author}")
+    if source_url:
+        meta.append(f"Source: {source_url}")
+    if meta:
+        parts.append("\n\n---\n" + "\n".join(meta))
+    return "".join(parts)
+
+
+class Bot(discord.Client):
+    async def on_ready(self):
+        print(f"Logged in as {self.user} | prefix={PREFIX}")
+
+    async def on_message(self, message: discord.Message):
+        if message.author.bot:
+            return
+        content = (message.content or "").strip()
+        if not content.lower().startswith(PREFIX.lower()):
+            return
+
+        if not GITHUB_TOKEN:
+            await message.reply("GITHUB_TOKEN が未設定です", mention_author=False)
+            return
+
+        parsed = parse(content)
+        if "error" in parsed:
+            await message.reply(parsed["error"], mention_author=False)
+            return
+
+        repo = parsed["repo"]
+        url = f"{GITHUB_API}/repos/{repo}/issues"
+        payload = {"title": parsed["title"], "body": build_body_with_footer(parsed["body"], str(message.author), message.jump_url)}
+        if parsed["labels"]:
+            payload["labels"] = parsed["labels"]
+        if parsed["assignees"]:
+            payload["assignees"] = parsed["assignees"]
+
+        status, resp = http_post(url, GITHUB_TOKEN, payload)
+        try:
+            data = json.loads(resp) if resp else {}
+        except Exception:
+            data = {}
+        if status in (200, 201):
+            issue_url = data.get("html_url", "")
+            number = data.get("number", "?")
+            await message.reply(f"Issueを作成しました: #{number} {issue_url}", mention_author=False)
+        else:
+            await message.reply(f"作成失敗: {status}\n{resp[:1500]}", mention_author=False)
+
+
+def main():
+    if not DISCORD_TOKEN:
+        raise SystemExit("DISCORD_BOT_TOKEN が未設定です")
+    intents = discord.Intents.default()
+    intents.message_content = True
+    Bot(intents=intents).run(DISCORD_TOKEN)
+
+
+if __name__ == "__main__":
+    main()
+
diff --git a/discord-issue-bot/docker-compose.yaml b/discord-issue-bot/docker-compose.yaml
new file mode 100644
index 0000000..634c143
--- /dev/null
+++ b/discord-issue-bot/docker-compose.yaml
@@ -0,0 +1,9 @@
+services:
+  bot:
+    build: .
+    env_file:
+      - .env
+    environment:
+      - DISCORD_BOT_TOKEN
+      - GITHUB_TOKEN
+    restart: unless-stopped
diff --git a/discord-issue-bot/pyproject.toml b/discord-issue-bot/pyproject.toml
new file mode 100644
index 0000000..a290a82
--- /dev/null
+++ b/discord-issue-bot/pyproject.toml
@@ -0,0 +1,12 @@
+[project]
+name = "discord-issue-bot"
+version = "0.1.0"
+description = "Create GitHub issues directly from Discord chat"
+requires-python = ">=3.10"
+dependencies = [
+  "discord.py>=2.3.2",
+]
+
+[tool.uv]
+dev-dependencies = []
+
```
