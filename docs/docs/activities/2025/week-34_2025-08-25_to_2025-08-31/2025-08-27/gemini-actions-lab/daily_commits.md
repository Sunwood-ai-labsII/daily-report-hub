# 📝 Daily Commits

## ⏰ 23:51:24 - `4d85a9d`
**Update gemini-jp-cli.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Wed Aug 27 23:51:24 2025 +0900
M	.github/workflows/gemini-jp-cli.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Wed Aug 27 23:51:24 2025 +0900

    Update gemini-jp-cli.yml

 .github/workflows/gemini-jp-cli.yml | 6 ++++--
 1 file changed, 4 insertions(+), 2 deletions(-)
```

### 💻 Code Changes
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
```

---

## ⏰ 14:54:28 - `068da05`
**docs: READMEの日本語と英語の混在を修正**
*by gemini-cli-jp[bot]*

### 📋 Changed Files
```bash
Author: gemini-cli-jp[bot] <gemini-cli-jp[bot]@users.noreply.github.com>
Date:   Wed Aug 27 14:54:28 2025 +0000
M	README.ja.md
M	README.md
```

### 📊 Statistics
```bash
Author: gemini-cli-jp[bot] <gemini-cli-jp[bot]@users.noreply.github.com>
Date:   Wed Aug 27 14:54:28 2025 +0000

    docs: READMEの日本語と英語の混在を修正

 README.ja.md | 71 ++++++++++++++++++++++++++++++------------------
 README.md    | 89 ++++++++++--------------------------------------------------
 2 files changed, 59 insertions(+), 101 deletions(-)
```

### 💻 Code Changes
```diff
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
 
```

---

