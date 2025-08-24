# 🔄 Latest Code Changes

```diff
diff --git a/README.ja.md b/README.ja.md
index 8b25a6e..8ddf803 100644
--- a/README.ja.md
+++ b/README.ja.md
@@ -1,8 +1,14 @@
-# ジェミニ・アクション・ラボ
-
 <div align="center">
-  <img src="https://img.shields.io/badge/GitHub%20Actions-AI-blue?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
-  <img src="https://img.shields.io/badge/Gemini-AI-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Gemini" />
+
+# Gemini Actions Lab
+
+<a href="./README.md"><img src="https://img.shields.io/badge/English-Readme-blue?style=for-the-badge&logo=github&logoColor=white" alt="English" /></a>
+<a href="./README.ja.md"><img src="https://img.shields.io/badge/日本語-Readme-red?style=for-the-badge&logo=github&logoColor=white" alt="日本語" /></a>
+
+![Image](https://github.com/user-attachments/assets/1e294058-a1e6-4b44-979d-f4c8f09cb8ae)
+
+<img src="https://img.shields.io/badge/GitHub%20Actions-AI-blue?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
+<img src="https://img.shields.io/badge/Gemini-AI-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Gemini" />
 </div>
 
 ---
@@ -44,7 +50,76 @@
 
 ---
 
-## 🚀 使い方
+## 📸 スクリーンショット & 例
+
+### 🤖 CLI 対話例
+Issueを作成して `@gemini-cli-jp /help` とコメントすることで、使用可能なコマンドを確認できます：
+
+\```
+@gemini-cli-jp /help
+\```
+
+AIアシスタントは、使用可能なコマンドと使用例で応答します。
+
+### 🏗️ ワークフローアーキテクチャ
+\```mermaid
+graph TD
+    A[GitHub Issue/PR] --> B[GitHub Actions トリガー]
+    B --> C[Gemini CLI ワークフロー]
+    C --> D[Gemini AI 処理]
+    D --> E[リポジトリ操作]
+    E --> F[自動応答]
+
+    G[スケジュール/定期実行] --> H[自動トリアージ]
+    H --> I[Issue管理]
+
+    J[PR作成] --> K[PRレビューワークフロー]
+    K --> L[コード解析]
+    L --> M[フィードバックと提案]
+\```
+
+### 💬 使用例
+
+**コードレビューリクエスト:**
+\```
+@gemini-cli-jp /review-pr
+このプルリクエストを確認して改善点を提案してください
+\```
+
+**Issueトリアージ:**
+\```
+@gemini-cli-jp /triage
+このIssueを分析して適切なラベルと担当者を提案してください
+\```
+
+---
+
+## 🛠️ トラブルシューティング
+
+### よくある問題
+
+**❌ ワークフローがトリガーされない:**
+- リポジトリ設定でGitHub Actionsが有効になっているか確認してください
+- リポジトリ設定でWebhook配信を確認してください
+- トリガー条件（例：コメント内の `@gemini-cli-jp`）が満たされているか確認してください
+
+**❌ Gemini API エラー:**
+- `GEMINI_API_KEY` シークレットが設定されているか確認してください
+- APIキーの権限とクォータを確認してください
+- APIキーが有効で期限切れでないか確認してください
+
+**❌ 権限エラー:**
+- ユーザーに書き込み権限があるか確認してください
+- リポジトリがプライベートかどうか確認してください（信頼できるユーザーの検出に影響します）
+
+### ヘルプの取得
+1. 同様の問題がないか [GitHub Issues](https://github.com/your-repo/issues) を確認してください
+2. 詳細なエラーログを添えて新しいIssueを作成してください
+3. 報告時にはワークフローの実行ログを含めてください
+
+---
+
+## � 使い方
 
 これらのワークフローを独自のリポジトリで使用するには、`.github/workflows`ディレクトリからワークフローファイルをコピーし、ニーズに合わせて適応させます。Gemini APIキーなどの必要なシークレットを設定する必要があります。
 
diff --git a/README.md b/README.md
index 3fff9ff..cd20ac5 100644
--- a/README.md
+++ b/README.md
@@ -1,8 +1,14 @@
+<div align="center">
+
 # Gemini Actions Lab
 
-<div align="center">
-  <img src="https://img.shields.io/badge/GitHub%20Actions-AI-blue?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
-  <img src="https://img.shields.io/badge/Gemini-AI-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Gemini" />
+<a href="./README.md"><img src="https://img.shields.io/badge/English-Readme-blue?style=for-the-badge&logo=github&logoColor=white" alt="English" /></a>
+<a href="./README.ja.md"><img src="https://img.shields.io/badge/日本語-Readme-red?style=for-the-badge&logo=github&logoColor=white" alt="日本語" /></a>
+
+![Image](https://github.com/user-attachments/assets/1e294058-a1e6-4b44-979d-f4c8f09cb8ae)
+
+<img src="https://img.shields.io/badge/GitHub%20Actions-AI-blue?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
+<img src="https://img.shields.io/badge/Gemini-AI-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Gemini" />
 </div>
 
 ---
@@ -20,43 +26,188 @@ This repository serves as a laboratory and showcase for integrating Google's Gem
 
 ## 🤖 Workflows
 
-This repository contains the following GitHub Actions workflows:
+このリポジトリは、GoogleのGemini AIをGitHub Actionsと統合するための実験室およびショーケースとして機能します。生成AIの力を利用して、さまざまなリポジトリ管理タスクを自動化する方法を示します。
+
+### 🎯 主な機能
+- **AIによる自動化**: Geminiを活用して、Issueのトリアージ、プルリクエストのレビューなどのタスクを処理します。
+- **CLIライクな対話**: Issueのコメントから直接AIアシスタントと対話します。
+- **拡張可能なワークフロー**: 独自のプロジェクトに合わせてワークフローを簡単に適応およびカスタマイズできます。
+
+---
+
+## 🤖 ワークフロー
 
-### 📄 `gemini-cli.yml`
-- **Trigger**: Issue comments.
-- **Function**: Allows users to interact with a Gemini-powered CLI assistant by creating comments on issues (e.g., `@gemini-cli /do-something`). The assistant can perform actions on the repository based on the user's request.
+このリポジトリには、以下のGitHub Actionsワークフローが含まれています：
+
+### 📄 `gemini-cli-jp.yml`
+- **トリガー**: Issueのコメント
+- **機能**: ユーザーがIssueにコメント（例：`@gemini-cli-jp /do-something`）を作成することで、Gemini搭載のCLIアシスタントと対話できるようにします。アシスタントは、ユーザーのリクエストに基づいてリポジトリでアクションを実行できます。
 
 ###  triage `gemini-issue-automated-triage.yml`
-- **Trigger**: Issue creation or edits.
-- **Function**: Automatically triages new or updated issues. It can add labels, assignees, or post comments based on the issue's content, as determined by Gemini.
+- **トリガー**: Issueの作成または編集
+- **機能**: 新規または更新されたIssueを自動的にトリアージします。Geminiによって決定されたIssueの内容に基づいて、ラベルの追加、担当者の割り当て、またはコメントの投稿ができます。
 
 ### 🕒 `gemini-issue-scheduled-triage.yml`
-- **Trigger**: Scheduled cron job.
-- **Function**: Periodically scans through open issues and performs triage tasks, such as identifying stale issues or suggesting priorities.
+- **トリガー**: スケジュールされたcronジョブ
+- **機能**: 定期的にオープンなIssueをスキャンし、古いIssueの特定や優先順位の提案などのトリアージタスクを実行します。
 
 ### 🔍 `gemini-pr-review.yml`
-- **Trigger**: Pull request creation or updates.
-- **Function**: Automatically reviews pull requests. Gemini can provide feedback on code quality, suggest improvements, or identify potential issues.
+- **トリガー**: プルリクエストの作成または更新
+- **機能**: プルリクエストを自動的にレビューします。Geminiは、コードの品質に関するフィードバックの提供、改善の提案、または潜在的な問題の特定ができます。
 
 ### 🔄 `sync-to-report-gh.yml`
-- **Trigger**: Pushes to the main branch.
-- **Function**: This is a legacy workflow from a previous template and is not actively used in this lab. It was designed to sync daily reports to a central repository.
+- **トリガー**: mainブランチへのプッシュ
+- **機能**: これは以前のテンプレートからのレガシーワークフローであり、このラボでは積極的に使用されていません。日次レポートを中央リポジトリに同期するように設計されていました。
 
 ---
 
-## 🚀 Usage
+## 📸 Screenshots & Examples
+
+### 🤖 CLI Interaction Example
+Create an issue and comment with `@gemini-cli /help` to see available commands:
+
+\```
+@gemini-cli /help
+\```
+
+The AI assistant will respond with available commands and usage examples.
+
+### 🏗️ Workflow Architecture
+\```mermaid
+graph TD
+    A[GitHub Issue/PR] --> B[GitHub Actions Trigger]
+    B --> C[Gemini CLI Workflow]
+    C --> D[Gemini AI Processing]
+    D --> E[Repository Actions]
+    E --> F[Automated Response]
+
+    G[Schedule/Cron] --> H[Automated Triage]
+    H --> I[Issue Management]
+
+    J[PR Created] --> K[PR Review Workflow]
+    K --> L[Code Analysis]
+    L --> M[Feedback & Suggestions]
+\```
+
+### 💬 Example Interactions
+
+**Code Review Request:**
+\```
+@gemini-cli /review-pr
+Please review this pull request and suggest improvements
+\```
+
+**Issue Triage:**
+\```
+@gemini-cli /triage
+Analyze this issue and suggest appropriate labels and assignees
+\```
+
+---
+
+## 🛠️ Troubleshooting
+
+### Common Issues
+
+**❌ Workflow not triggering:**
+- Check if GitHub Actions are enabled in repository settings
+- Verify webhook delivery in repository settings
+- Ensure the trigger conditions are met (e.g., `@gemini-cli` in comment)
+
+**❌ Gemini API errors:**
+- Verify `GEMINI_API_KEY` secret is configured
+- Check API key permissions and quota
+- Ensure the API key is valid and not expired
+
+**❌ Permission errors:**
+- Confirm the user has write permissions
+- Check if the repository is private (affects trusted user detection)
+
+### Getting Help
+1. Check the [GitHub Issues](https://github.com/your-repo/issues) for similar problems
+2. Create a new issue with detailed error logs
+3. Include workflow run logs when reporting issues
+
+---
+
+## 🚀 Installation & Setup
+
+### Prerequisites
+- GitHub account with repository creation permissions
+- Gemini API key from Google AI Studio
+- Basic understanding of GitHub Actions
+
+### Quick Start
+1. **Fork this repository** to your GitHub account
+2. **Configure GitHub Secrets** in your repository settings:
+   - `GEMINI_API_KEY`: Your Gemini API key
+   - `GITHUB_TOKEN`: (automatically provided)
+3. **Copy workflow files** from `.github/workflows/` to your repository
+4. **Customize workflows** according to your needs
+5. **Test the setup** by creating an issue and commenting `@gemini-cli /help`
+
+### Advanced Configuration
+For additional features, configure these optional secrets:
+- `APP_ID` and `APP_PRIVATE_KEY`: For GitHub App integration
+- `GCP_WIF_PROVIDER` and related GCP variables: For Vertex AI usage
+
+---
+
+## 🛠️ Troubleshooting
+
+### Common Issues
+
+**❌ Workflow not triggering:**
+- Check if GitHub Actions are enabled in repository settings
+- Verify webhook delivery in repository settings
+- Ensure the trigger conditions are met (e.g., `@gemini-cli` in comment)
+
+**❌ Gemini API errors:**
+- Verify `GEMINI_API_KEY` secret is configured
+- Check API key permissions and quota
+- Ensure the API key is valid and not expired
+
+**❌ Permission errors:**
+- Confirm the user has write permissions
+- Check if the repository is private (affects trusted user detection)
+
+### Getting Help
+1. Check the [GitHub Issues](https://github.com/your-repo/issues) for similar problems
+2. Create a new issue with detailed error logs
+3. Include workflow run logs when reporting issues
+
+---
+
+## 🚀 Installation & Setup
+
+### Prerequisites
+- GitHub account with repository creation permissions
+- Gemini API key from Google AI Studio
+- Basic understanding of GitHub Actions
+
+### Quick Start
+1. **Fork this repository** to your GitHub account
+2. **Configure GitHub Secrets** in your repository settings:
+   - `GEMINI_API_KEY`: Your Gemini API key
+   - `GITHUB_TOKEN`: (automatically provided)
+3. **Copy workflow files** from `.github/workflows/` to your repository
+4. **Customize workflows** according to your needs
+5. **Test the setup** by creating an issue and commenting `@gemini-cli /help`
 
-To use these workflows in your own repository, you can copy the workflow files from the `.github/workflows` directory and adapt them to your needs. You will need to configure the necessary secrets, such as your Gemini API key.
+### Advanced Configuration
+For additional features, configure these optional secrets:
+- `APP_ID` and `APP_PRIVATE_KEY`: For GitHub App integration
+- `GCP_WIF_PROVIDER` and related GCP variables: For Vertex AI usage
 
 ---
 
-## 📁 Directory Structure
+## 📁 ディレクトリ構造
 
 \```
 .
 ├── .github/
 │   └── workflows/
-│       ├── gemini-cli.yml
+│       ├── gemini-cli-jp.yml
 │       ├── gemini-issue-automated-triage.yml
 │       ├── gemini-issue-scheduled-triage.yml
 │       ├── gemini-pr-review.yml
@@ -68,10 +219,10 @@ To use these workflows in your own repository, you can copy the workflow files f
 
 ---
 
-## 📝 License
+## 📝 ライセンス
 
-This project is licensed under the terms of the [LICENSE](LICENSE) file.
+このプロジェクトは、[LICENSE](LICENSE)ファイルの条件に基づいてライセンスされています。
 
 ---
 
-© 2025 Sunwood-ai-labsII
\ No newline at end of file
+© 2025 Sunwood-ai-labsII
```
