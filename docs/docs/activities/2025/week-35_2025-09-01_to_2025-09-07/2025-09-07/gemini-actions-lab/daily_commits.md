# 📝 Daily Commits

## ⏰ 12:50:56 - `32ea265`
**🗑️ README.ja.mdファイルの削除**
*by maki*

### 📋 Changed Files
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 12:50:56 2025 +0000
D	README.ja.md
```

### 📊 Statistics
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 12:50:56 2025 +0000

    🗑️ README.ja.mdファイルの削除
    
    - 日本語版READMEファイルを削除し、英語版に統合
    - ローカライゼーションの効率化のため

 README.ja.md | 171 -----------------------------------------------------------
 1 file changed, 171 deletions(-)
```

### 💻 Code Changes
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
```

---

## ⏰ 12:51:05 - `4011e0c`
**🌐 README.mdのローカライゼーション更新**
*by maki*

### 📋 Changed Files
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 12:51:05 2025 +0000
M	README.md
```

### 📊 Statistics
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 12:51:05 2025 +0000

    🌐 README.mdのローカライゼーション更新
    
    - 全セクションを日本語に翻訳
    - マークダウンバッジの更新
    - ワークフロー説明の日本語化
    - ディレクトリ構造の更新とDiscord Issue Botセクション追加

 README.md | 192 ++++++++++++++++++++++++++++++++++++--------------------------
 1 file changed, 111 insertions(+), 81 deletions(-)
```

### 💻 Code Changes
```diff
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
```

---

## ⏰ 12:51:13 - `95a01d7`
**🤖 Discord Issue Botの実装追加**
*by maki*

### 📋 Changed Files
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 12:51:13 2025 +0000
A	discord-issue-bot/Dockerfile
A	discord-issue-bot/README.md
A	discord-issue-bot/bot.py
A	discord-issue-bot/docker-compose.yaml
A	discord-issue-bot/pyproject.toml
```

### 📊 Statistics
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 12:51:13 2025 +0000

    🤖 Discord Issue Botの実装追加
    
    - DiscordからGitHub Issueを作成するボット機能実装
    - bot.py: メインのボットスクリプトと機能
    - Dockerfile: Dockerコンテナ化設定
    - pyproject.toml: Pythonプロジェクト依存関係
    - compose.yaml: ローカル開発用Docker Compose設定

 discord-issue-bot/Dockerfile          |  10 +++
 discord-issue-bot/README.md           |  42 ++++++++++
 discord-issue-bot/bot.py              | 141 ++++++++++++++++++++++++++++++++++
 discord-issue-bot/docker-compose.yaml |   7 ++
 discord-issue-bot/pyproject.toml      |  12 +++
 5 files changed, 212 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/discord-issue-bot/Dockerfile b/discord-issue-bot/Dockerfile
new file mode 100644
index 0000000..b34c26a
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
+RUN uv sync --frozen
+COPY . .
+CMD ["uv", "run", "bot.py"]
diff --git a/discord-issue-bot/README.md b/discord-issue-bot/README.md
new file mode 100644
index 0000000..663febd
--- /dev/null
+++ b/discord-issue-bot/README.md
@@ -0,0 +1,42 @@
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
+## 実装
+- `bot.py`: Discord メッセージをパースし、GitHub API (`POST /repos/{owner}/{repo}/issues`) に直接作成
+- 依存: `discord.py`
+- ビルド: `Dockerfile`（uv インストール → `uv sync` → `uv run bot.py`）
+
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
```

---

## ⏰ 12:51:32 - `703f6d0`
**🔀 Merge: READMEローカライゼーションおよびDiscordボット追加**
*by maki*

### 📋 Changed Files
```bash
Merge: 458e151 95a01d7
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 12:51:32 2025 +0000
```

### 📊 Statistics
```bash
Merge: 458e151 95a01d7
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 12:51:32 2025 +0000

    🔀 Merge: READMEローカライゼーションおよびDiscordボット追加

 README.ja.md                          | 171 ------------------------------
 README.md                             | 192 ++++++++++++++++++++--------------
 discord-issue-bot/Dockerfile          |  10 ++
 discord-issue-bot/README.md           |  42 ++++++++
 discord-issue-bot/bot.py              | 141 +++++++++++++++++++++++++
 discord-issue-bot/docker-compose.yaml |   7 ++
 discord-issue-bot/pyproject.toml      |  12 +++
 7 files changed, 323 insertions(+), 252 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 13:43:24 - `25896f1`
**📄 .env.example ファイルを追加**
*by maki*

### 📋 Changed Files
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 13:43:24 2025 +0000
A	discord-issue-bot/.env.example
```

### 📊 Statistics
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 13:43:24 2025 +0000

    📄 .env.example ファイルを追加
    
    - Docker Compose の環境ファイルテンプレートを追加
    - 設定の上書きを容易にするため .env ファイルを参照可能

 discord-issue-bot/.env.example | 7 +++++++
 1 file changed, 7 insertions(+)
```

### 💻 Code Changes
```diff
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
```

---

## ⏰ 13:43:34 - `1a1ac6c`
**🐳 Dockerfile を調整**
*by maki*

### 📋 Changed Files
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 13:43:34 2025 +0000
M	discord-issue-bot/Dockerfile
```

### 📊 Statistics
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 13:43:34 2025 +0000

    🐳 Dockerfile を調整
    
    - uv sync --frozen を uv sync に変更
    - 依存関係ロックを固定せず柔軟にインストール

 discord-issue-bot/Dockerfile | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/discord-issue-bot/Dockerfile b/discord-issue-bot/Dockerfile
index b34c26a..52331ab 100644
--- a/discord-issue-bot/Dockerfile
+++ b/discord-issue-bot/Dockerfile
@@ -5,6 +5,6 @@ ENV PYTHONDONTWRITEBYTECODE=1 \
 
 WORKDIR /app
 COPY pyproject.toml ./
-RUN uv sync --frozen
+RUN uv sync
 COPY . .
 CMD ["uv", "run", "bot.py"]
```

---

## ⏰ 13:43:44 - `26f572d`
**🔧 docker-compose.yaml を更新**
*by maki*

### 📋 Changed Files
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 13:43:44 2025 +0000
M	discord-issue-bot/docker-compose.yaml
```

### 📊 Statistics
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 13:43:44 2025 +0000

    🔧 docker-compose.yaml を更新
    
    - env_file オプションを追加
    - .env ファイルからの環境変数読み込みを有効化

 discord-issue-bot/docker-compose.yaml | 2 ++
 1 file changed, 2 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/discord-issue-bot/docker-compose.yaml b/discord-issue-bot/docker-compose.yaml
index 1751e18..634c143 100644
--- a/discord-issue-bot/docker-compose.yaml
+++ b/discord-issue-bot/docker-compose.yaml
@@ -1,6 +1,8 @@
 services:
   bot:
     build: .
+    env_file:
+      - .env
     environment:
       - DISCORD_BOT_TOKEN
       - GITHUB_TOKEN
```

---

## ⏰ 13:43:53 - `2e288c8`
**📖 README.md を大幅拡充**
*by maki*

### 📋 Changed Files
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 13:43:53 2025 +0000
M	discord-issue-bot/README.md
```

### 📊 Statistics
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 13:43:53 2025 +0000

    📖 README.md を大幅拡充
    
    - Discord チャット例を追加して利用方法を明確化
    - 特権インテントの設定手順を詳細に記載
    - トラブルシューティングセクションを追加
    - 全体的な使いやすさを向上

 discord-issue-bot/README.md | 50 +++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 50 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/discord-issue-bot/README.md b/discord-issue-bot/README.md
index 663febd..e6c2d1f 100644
--- a/discord-issue-bot/README.md
+++ b/discord-issue-bot/README.md
@@ -35,8 +35,58 @@ docker compose -f compose.yaml logs -f
 - タイトルは `"ダブルクオート"` で囲むと1行で指定可能（未指定なら1行目がタイトル、2行目以降が本文）
 - `#label` でラベル、`+user` でアサイン
 
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
 ## 実装
 - `bot.py`: Discord メッセージをパースし、GitHub API (`POST /repos/{owner}/{repo}/issues`) に直接作成
 - 依存: `discord.py`
 - ビルド: `Dockerfile`（uv インストール → `uv sync` → `uv run bot.py`）
 
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
```

---

## ⏰ 13:44:19 - `6b92cf2`
**🔀 Merge: Discord bot Docker improvements**
*by maki*

### 📋 Changed Files
```bash
Merge: 703f6d0 2e288c8
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 13:44:19 2025 +0000
```

### 📊 Statistics
```bash
Merge: 703f6d0 2e288c8
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Sep 7 13:44:19 2025 +0000

    🔀 Merge: Discord bot Docker improvements

 discord-issue-bot/.env.example        |  7 +++++
 discord-issue-bot/Dockerfile          |  2 +-
 discord-issue-bot/README.md           | 50 +++++++++++++++++++++++++++++++++++
 discord-issue-bot/docker-compose.yaml |  2 ++
 4 files changed, 60 insertions(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
```

---

