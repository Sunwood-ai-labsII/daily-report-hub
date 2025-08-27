# 💻 Daily Code Changes

## Full Diff

```diff
diff --git a/.github/workflows/gemini-jp-cli.yml b/.github/workflows/gemini-jp-cli.yml
index 858f00e..12fe964 100644
--- a/.github/workflows/gemini-jp-cli.yml
+++ b/.github/workflows/gemini-jp-cli.yml
@@ -112,8 +112,11 @@ jobs:
           # ユーザーリクエストをクリーンアップ
           USER_REQUEST=$(echo "${USER_REQUEST}" | sed 's/.*@gemini-jp-cli//' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
 
+          # GITHUB_OUTPUTへの書き込みをheredoc形式に変更して、特殊文字によるエラーを回避
           {
-            echo "user_request=${USER_REQUEST}"
+            echo 'user_request<<EOF'
+            echo "${USER_REQUEST}"
+            echo 'EOF'
             echo "issue_number=${ISSUE_NUMBER}"
             echo "is_pr=${IS_PR}"
           } >> "${GITHUB_OUTPUT}"
@@ -148,7 +151,6 @@ jobs:
           GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           ISSUE_NUMBER: '${{ steps.get_context.outputs.issue_number }}'
           REPOSITORY: '${{ github.repository }}'
-          REQUEST_TYPE: '${{ steps.get_context.outputs.request_type }}'
         run: |-
           set -euo pipefail
           MESSAGE="@${GITHUB_ACTOR} リクエストを受け取りました。今から作業を開始します！ 🤖"
diff --git a/README.ja.md b/README.ja.md
index 8ddf803..087a0b0 100644
--- a/README.ja.md
+++ b/README.ja.md
@@ -50,18 +50,18 @@
 
 ---
 
-## 📸 スクリーンショット & 例
+## 📸 スクリーンショットと例
 
-### 🤖 CLI 対話例
-Issueを作成して `@gemini-cli-jp /help` とコメントすることで、使用可能なコマンドを確認できます：
+### 🤖 CLIの対話例
+Issueを作成し、`@gemini-cli-jp /help`とコメントして、利用可能なコマンドを確認します:
 
 \```
 @gemini-cli-jp /help
 \```
 
-AIアシスタントは、使用可能なコマンドと使用例で応答します。
+AIアシスタントが利用可能なコマンドと使用例を返信します。
 
-### 🏗️ ワークフローアーキテクチャ
+### 🏗️ ワークフローのアーキテクチャ
 \```mermaid
 graph TD
     A[GitHub Issue/PR] --> B[GitHub Actions トリガー]
@@ -70,7 +70,7 @@ graph TD
     D --> E[リポジトリ操作]
     E --> F[自動応答]
 
-    G[スケジュール/定期実行] --> H[自動トリアージ]
+    G[スケジュール/Cron] --> H[自動トリアージ]
     H --> I[Issue管理]
 
     J[PR作成] --> K[PRレビューワークフロー]
@@ -78,50 +78,67 @@ graph TD
     L --> M[フィードバックと提案]
 \```
 
-### 💬 使用例
+### 💬 対話の例
 
-**コードレビューリクエスト:**
+**コードレビューのリクエスト:**
 \```
 @gemini-cli-jp /review-pr
-このプルリクエストを確認して改善点を提案してください
+このプルリクエストをレビューし、改善点を提案してください
 \```
 
-**Issueトリアージ:**
+**Issueのトリアージ:**
 \```
 @gemini-cli-jp /triage
-このIssueを分析して適切なラベルと担当者を提案してください
+このIssueを分析し、適切なラベルと担当者を提案してください
 \```
 
 ---
 
 ## 🛠️ トラブルシューティング
 
-### よくある問題
+### 一般的な問題
 
 **❌ ワークフローがトリガーされない:**
-- リポジトリ設定でGitHub Actionsが有効になっているか確認してください
-- リポジトリ設定でWebhook配信を確認してください
-- トリガー条件（例：コメント内の `@gemini-cli-jp`）が満たされているか確認してください
+- リポジトリの設定でGitHub Actionsが有効になっているか確認してください
+- リポジトリの設定でWebhookの配信を確認してください
+- トリガー条件（例：コメントに`@gemini-cli-jp`が含まれているか）が満たされているか確認してください
 
-**❌ Gemini API エラー:**
-- `GEMINI_API_KEY` シークレットが設定されているか確認してください
+**❌ Gemini APIのエラー:**
+- `GEMINI_API_KEY`シークレットが設定されているか確認してください
 - APIキーの権限とクォータを確認してください
-- APIキーが有効で期限切れでないか確認してください
+- APIキーが有効で期限切れでないことを確認してください
 
 **❌ 権限エラー:**
-- ユーザーに書き込み権限があるか確認してください
-- リポジトリがプライベートかどうか確認してください（信頼できるユーザーの検出に影響します）
+- ユーザーに書き込み権限があることを確認してください
+- リポジトリがプライベートでないか確認してください（信頼されたユーザーの検出に影響します）
 
-### ヘルプの取得
-1. 同様の問題がないか [GitHub Issues](https://github.com/your-repo/issues) を確認してください
-2. 詳細なエラーログを添えて新しいIssueを作成してください
-3. 報告時にはワークフローの実行ログを含めてください
+### ヘルプの入手方法
+1. [GitHub Issues](https://github.com/your-repo/issues)で同様の問題がないか確認してください
+2. 詳細なエラーログを記載した新しいIssueを作成してください
+3. Issueを報告する際には、ワークフローの実行ログを含めてください
 
 ---
 
-## � 使い方
+## 🚀 インストールとセットアップ
 
-これらのワークフローを独自のリポジトリで使用するには、`.github/workflows`ディレクトリからワークフローファイルをコピーし、ニーズに合わせて適応させます。Gemini APIキーなどの必要なシークレットを設定する必要があります。
+### 前提条件
+- リポジトリ作成権限のあるGitHubアカウント
+- Google AI StudioのGemini APIキー
+- GitHub Actionsの基本的な理解
+
+### クイックスタート
+1. **このリポジトリをフォーク**して、自分のGitHubアカウントにコピーします
+2. リポジトリの設定で**GitHubシークレットを設定**します:
+   - `GEMINI_API_KEY`: あなたのGemini APIキー
+   - `GITHUB_TOKEN`: (自動的に提供されます)
+3. `.github/workflows/`からあなたのリポジトリに**ワークフローファイルをコピー**します
+4. あなたのニーズに合わせて**ワークフローをカスタマイズ**します
+5. Issueを作成し、`@gemini-cli-jp /help`とコメントして**セットアップをテスト**します
+
+### 高度な設定
+追加機能を利用するには、これらのオプションのシークレットを設定します:
+- `APP_ID`と`APP_PRIVATE_KEY`: GitHub App連携用
+- `GCP_WIF_PROVIDER`と関連するGCP変数: Vertex AI利用のため
 
 ---
 
@@ -149,4 +166,4 @@ graph TD
 
 ---
 
-© 2025 Sunwood-ai-labsII
+© 2025 Sunwood-ai-labsII
\ No newline at end of file
diff --git a/README.md b/README.md
index cd20ac5..ca6ca29 100644
--- a/README.md
+++ b/README.md
@@ -26,38 +26,27 @@ This repository serves as a laboratory and showcase for integrating Google's Gem
 
 ## 🤖 Workflows
 
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
+This repository includes the following GitHub Actions workflows:
 
 ### 📄 `gemini-cli-jp.yml`
-- **トリガー**: Issueのコメント
-- **機能**: ユーザーがIssueにコメント（例：`@gemini-cli-jp /do-something`）を作成することで、Gemini搭載のCLIアシスタントと対話できるようにします。アシスタントは、ユーザーのリクエストに基づいてリポジトリでアクションを実行できます。
+- **Trigger**: Issue comments
+- **Function**: Allows users to interact with a Gemini-powered CLI assistant by creating comments on issues (e.g., `@gemini-cli-jp /do-something`). The assistant can then perform actions on the repository based on the user's request.
 
 ###  triage `gemini-issue-automated-triage.yml`
-- **トリガー**: Issueの作成または編集
-- **機能**: 新規または更新されたIssueを自動的にトリアージします。Geminiによって決定されたIssueの内容に基づいて、ラベルの追加、担当者の割り当て、またはコメントの投稿ができます。
+- **Trigger**: Issue creation or edits
+- **Function**: Automatically triages new or updated issues. It can add labels, assignees, or post comments based on the issue's content as determined by Gemini.
 
 ### 🕒 `gemini-issue-scheduled-triage.yml`
-- **トリガー**: スケジュールされたcronジョブ
-- **機能**: 定期的にオープンなIssueをスキャンし、古いIssueの特定や優先順位の提案などのトリアージタスクを実行します。
+- **Trigger**: Scheduled cron job
+- **Function**: Periodically scans open issues and performs triage tasks, such as identifying stale issues or suggesting priorities.
 
 ### 🔍 `gemini-pr-review.yml`
-- **トリガー**: プルリクエストの作成または更新
-- **機能**: プルリクエストを自動的にレビューします。Geminiは、コードの品質に関するフィードバックの提供、改善の提案、または潜在的な問題の特定ができます。
+- **Trigger**: Pull request creation or updates
+- **Function**: Automatically reviews pull requests. Gemini can provide feedback on code quality, suggest improvements, or identify potential issues.
 
 ### 🔄 `sync-to-report-gh.yml`
-- **トリガー**: mainブランチへのプッシュ
-- **機能**: これは以前のテンプレートからのレガシーワークフローであり、このラボでは積極的に使用されていません。日次レポートを中央リポジトリに同期するように設計されていました。
+- **Trigger**: Push to the main branch
+- **Function**: This is a legacy workflow from a previous template and is not actively used in this lab. It was designed to sync daily reports to a central repository.
 
 ---
 
@@ -153,55 +142,7 @@ For additional features, configure these optional secrets:
 
 ---
 
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
-## 📁 ディレクトリ構造
+## 📁 Directory Structure
 
 \```
 .
@@ -219,10 +160,10 @@ For additional features, configure these optional secrets:
 
 ---
 
-## 📝 ライセンス
+## 📝 License
 
-このプロジェクトは、[LICENSE](LICENSE)ファイルの条件に基づいてライセンスされています。
+This project is licensed under the terms of the [LICENSE](LICENSE) file.
 
 ---
 
-© 2025 Sunwood-ai-labsII
+© 2025 Sunwood-ai-labsII
\ No newline at end of file
```
