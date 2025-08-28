# 📝 Daily Commits

## ⏰ 19:23:54 - `a601f74`
**Initial commit**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Thu Aug 28 19:23:54 2025 +0900
A	.SourceSageignore
A	.github/workflows/gemini-cli.yml
A	.github/workflows/gemini-issue-automated-triage.yml
A	.github/workflows/gemini-issue-scheduled-triage.yml
A	.github/workflows/gemini-jp-cli.yml
A	.github/workflows/gemini-pr-review.yml
A	.github/workflows/sync-to-report-gh.yml
A	.gitignore
A	LICENSE
A	README.ja.md
A	README.md
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Thu Aug 28 19:23:54 2025 +0900

    Initial commit

 .SourceSageignore                                  |  54 +++
 .github/workflows/gemini-cli.yml                   | 315 ++++++++++++++
 .../workflows/gemini-issue-automated-triage.yml    | 271 ++++++++++++
 .../workflows/gemini-issue-scheduled-triage.yml    | 193 +++++++++
 .github/workflows/gemini-jp-cli.yml                | 319 ++++++++++++++
 .github/workflows/gemini-pr-review.yml             | 468 +++++++++++++++++++++
 .github/workflows/sync-to-report-gh.yml            |  52 +++
 .gitignore                                         | 209 +++++++++
 LICENSE                                            |  21 +
 README.ja.md                                       | 169 ++++++++
 README.md                                          | 169 ++++++++
 11 files changed, 2240 insertions(+)
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
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
new file mode 100644
index 0000000..41cf37c
--- /dev/null
+++ b/.github/workflows/gemini-cli.yml
@@ -0,0 +1,315 @@
+name: '💬 Gemini CLI'
+
+on:
+  pull_request_review_comment:
+    types:
+      - 'created'
+  pull_request_review:
+    types:
+      - 'submitted'
+  issue_comment:
+    types:
+      - 'created'
+
+concurrency:
+  group: '${{ github.workflow }}-${{ github.event.issue.number }}'
+  cancel-in-progress: |-
+    ${{ github.event.sender.type == 'User' && ( github.event.issue.author_association == 'OWNER' || github.event.issue.author_association == 'MEMBER' || github.event.issue.author_association == 'COLLABORATOR') }}
+
+defaults:
+  run:
+    shell: 'bash'
+
+permissions:
+  contents: 'write'
+  id-token: 'write'
+  pull-requests: 'write'
+  issues: 'write'
+
+jobs:
+  gemini-cli:
+    # This condition seeks to ensure the action is only run when it is triggered by a trusted user.
+    # For private repos, users who have access to the repo are considered trusted.
+    # For public repos, users who members, owners, or collaborators are considered trusted.
+    if: |-
```

---

## ⏰ 10:28:31 - `c851c49`
**feat: Create initial files for prompt books app**
*by gemini-cli-jp[bot]*

### 📋 Changed Files
```bash
Author: gemini-cli-jp[bot] <gemini-cli-jp[bot]@users.noreply.github.com>
Date:   Thu Aug 28 10:28:31 2025 +0000
A	index.html
A	script.js
A	style.css
```

### 📊 Statistics
```bash
Author: gemini-cli-jp[bot] <gemini-cli-jp[bot]@users.noreply.github.com>
Date:   Thu Aug 28 10:28:31 2025 +0000

    feat: Create initial files for prompt books app

 index.html | 16 ++++++++++++++++
 script.js  |  1 +
 style.css  |  8 ++++++++
 3 files changed, 25 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/index.html b/index.html
new file mode 100644
index 0000000..55cb102
--- /dev/null
+++ b/index.html
@@ -0,0 +1,16 @@
+<!DOCTYPE html>
+<html lang="ja">
+<head>
+    <meta charset="UTF-8">
+    <meta name="viewport" content="width=device-width, initial-scale=1.0">
+    <title>Prompt Books</title>
+    <link rel="stylesheet" href="style.css">
+</head>
+<body>
+    <h1>Prompt Books</h1>
+
+    <div id="app"></div>
+
+    <script src="script.js"></script>
+</body>
+</html>
\ No newline at end of file
diff --git a/script.js b/script.js
new file mode 100644
index 0000000..8938b43
--- /dev/null
+++ b/script.js
@@ -0,0 +1 @@
+console.log("Hello from script.js!");
\ No newline at end of file
diff --git a/style.css b/style.css
new file mode 100644
index 0000000..f302add
--- /dev/null
+++ b/style.css
@@ -0,0 +1,8 @@
+body {
+    font-family: sans-serif;
+}
+
+#app {
+    width: 80%;
+    margin: 0 auto;
+}
\ No newline at end of file
```

---

## ⏰ 19:32:19 - `f162e70`
**Merge pull request #2 from Sunwood-ai-labsII/issue/1/create-prompt-books-app**
*by Maki*

### 📋 Changed Files
```bash
Merge: a601f74 c851c49
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Thu Aug 28 19:32:19 2025 +0900
```

### 📊 Statistics
```bash
Merge: a601f74 c851c49
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Thu Aug 28 19:32:19 2025 +0900

    Merge pull request #2 from Sunwood-ai-labsII/issue/1/create-prompt-books-app
    
    Fixes #1: Create prompt books app

 index.html | 16 ++++++++++++++++
 script.js  |  1 +
 style.css  |  8 ++++++++
 3 files changed, 25 insertions(+)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 10:39:30 - `8a64e63`
**feat: Implement prompt books application**
*by gemini-cli-jp[bot]*

### 📋 Changed Files
```bash
Author: gemini-cli-jp[bot] <gemini-cli-jp[bot]@users.noreply.github.com>
Date:   Thu Aug 28 10:39:30 2025 +0000
M	README.ja.md
M	README.md
M	index.html
A	plan.md
M	script.js
M	style.css
```

### 📊 Statistics
```bash
Author: gemini-cli-jp[bot] <gemini-cli-jp[bot]@users.noreply.github.com>
Date:   Thu Aug 28 10:39:30 2025 +0000

    feat: Implement prompt books application

 README.ja.md | 170 +++++------------------------------------------------------
 README.md    | 170 +++++------------------------------------------------------
 index.html   |  11 ++--
 plan.md      |   6 +++
 script.js    |  50 +++++++++++++++++-
 style.css    |  38 +++++++++++--
 6 files changed, 125 insertions(+), 320 deletions(-)
```

### 💻 Code Changes
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
```

---

