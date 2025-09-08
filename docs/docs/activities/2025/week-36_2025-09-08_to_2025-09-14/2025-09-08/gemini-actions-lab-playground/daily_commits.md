# 📝 Daily Commits

## ⏰ 22:44:39 - `2386425`
**Initial commit**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Sep 8 22:44:39 2025 +0900
A	.SourceSageignore
A	.github/prompts/gemini-cli_prompt.ja.md
A	.github/workflows/gemini-cli.yml
A	.github/workflows/gemini-issue-automated-triage.yml
A	.github/workflows/gemini-issue-scheduled-triage.yml
A	.github/workflows/gemini-jp-cli.yml
A	.github/workflows/gemini-pr-review.yml
A	.github/workflows/gemini-release-notes.yml
A	.github/workflows/imagen-generate-and-commit.yml
A	.github/workflows/sync-to-report-gh.yml
A	.gitignore
A	LICENSE
A	README.md
A	discord-issue-bot/.env.example
A	discord-issue-bot/Dockerfile
A	discord-issue-bot/README.md
A	discord-issue-bot/bot.py
A	discord-issue-bot/docker-compose.yaml
A	discord-issue-bot/pyproject.toml
A	example/index.html
A	example/todo/index.html
A	example/todo/script.js
A	example/todo/style.css
A	generated-images/imagen-4_2025-09-06T11-49-47-885Z_A_beautiful_Japanese_landscape_with_cherry_blossom_1.png
A	generated-images/imagen-4_2025-09-06T11-49-47-892Z_A_beautiful_Japanese_landscape_with_cherry_blossom_2.png
A	generated-images/metadata.json
A	memo.md
A	response.md
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Sep 8 22:44:39 2025 +0900

    Initial commit

 .SourceSageignore                                  |  54 +++
 .github/prompts/gemini-cli_prompt.ja.md            | 268 ++++++++++++
 .github/workflows/gemini-cli.yml                   | 282 +++++++++++++
 .../workflows/gemini-issue-automated-triage.yml    | 137 ++++++
 .../workflows/gemini-issue-scheduled-triage.yml    | 324 ++++++++++++++
 .github/workflows/gemini-jp-cli.yml                | 340 +++++++++++++++
 .github/workflows/gemini-pr-review.yml             | 468 +++++++++++++++++++++
 .github/workflows/gemini-release-notes.yml         | 163 +++++++
 .github/workflows/imagen-generate-and-commit.yml   | 153 +++++++
 .github/workflows/sync-to-report-gh.yml            |  52 +++
 .gitignore                                         | 209 +++++++++
 LICENSE                                            |  21 +
 README.md                                          | 187 ++++++++
 discord-issue-bot/.env.example                     |   7 +
 discord-issue-bot/Dockerfile                       |  10 +
 discord-issue-bot/README.md                        |  92 ++++
 discord-issue-bot/bot.py                           | 141 +++++++
 discord-issue-bot/docker-compose.yaml              |   9 +
 discord-issue-bot/pyproject.toml                   |  12 +
 example/index.html                                 | 221 ++++++++++
 example/todo/index.html                            |  20 +
 example/todo/script.js                             |  72 ++++
 example/todo/style.css                             |  88 ++++
 ...ul_Japanese_landscape_with_cherry_blossom_1.png | Bin 0 -> 2289651 bytes
 ...ul_Japanese_landscape_with_cherry_blossom_2.png | Bin 0 -> 1824554 bytes
 generated-images/metadata.json                     |  10 +
 memo.md                                            |   8 +
 response.md                                        |  10 +
 28 files changed, 3358 insertions(+)
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
diff --git a/.github/prompts/gemini-cli_prompt.ja.md b/.github/prompts/gemini-cli_prompt.ja.md
new file mode 100644
index 0000000..2dac199
--- /dev/null
+++ b/.github/prompts/gemini-cli_prompt.ja.md
@@ -0,0 +1,268 @@
+## 🤖 役割
+
+あなたは GitHub Actions のワークフロー内で CLI として呼び出される、親切で実務的な AI アシスタントです。リポジトリに対する読み書きや、ユーザーへの返信に必要な各種ツールを安全に使ってタスクを進めます。
+
+## 📋 コンテキスト
+
+- リポジトリ: ${REPOSITORY}
+- トリガーイベント: ${EVENT_NAME}
+- Issue/PR 番号: ${ISSUE_NUMBER}
+- PR かどうか: ${IS_PR}
+- Issue/PR の説明:
+${DESCRIPTION}
+- コメント一覧:
+${COMMENTS}
+
+## 🗣 ユーザーリクエスト
+
+ユーザーからのリクエスト:
+${USER_REQUEST}
+
+## 🚀 対応ポリシー（Issue、PR コメント、質問）
+
+このワークフローは主に以下の 3 シナリオを想定しています。
+
+1. Issue の修正を実装する
+   - リクエスト内容と Issue/PR の説明を丁寧に読み、背景を把握します。
+   - `gh issue view`、`gh pr view`、`gh pr diff`、`cat`、`head`、`tail` などで必要な情報を収集します。
+   - 着手前に必ず原因を特定します（根本原因に対処）。
+   - 最初に「計画チェックリスト」をコメントで提示し、進捗に応じて更新します。
+     例:
+     \```
+     ### 計画
+     - [ ] 根本原因の調査
+     - [ ] 対象ファイルの修正実装
```

---

## ⏰ 13:55:19 - `1bf0fc8`
**feat: ✨ Create TODO App in example/demo003**
*by gemini-cli[bot]*

### 📋 Changed Files
```bash
Author: gemini-cli[bot] <gemini-cli[bot]@users.noreply.github.com>
Date:   Mon Sep 8 13:55:19 2025 +0000
A	example/demo003/index.html
A	example/demo003/script.js
A	example/demo003/style.css
```

### 📊 Statistics
```bash
Author: gemini-cli[bot] <gemini-cli[bot]@users.noreply.github.com>
Date:   Mon Sep 8 13:55:19 2025 +0000

    feat: ✨ Create TODO App in example/demo003

 example/demo003/index.html | 20 +++++++++++
 example/demo003/script.js  | 54 ++++++++++++++++++++++++++++++
 example/demo003/style.css  | 82 ++++++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 156 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/example/demo003/index.html b/example/demo003/index.html
new file mode 100644
index 0000000..28df4a9
--- /dev/null
+++ b/example/demo003/index.html
@@ -0,0 +1,20 @@
+<!DOCTYPE html>
+<html lang="en">
+<head>
+    <meta charset="UTF-8">
+    <meta name="viewport" content="width=device-width, initial-scale=1.0">
+    <title>TODO App</title>
+    <link rel="stylesheet" href="style.css">
+</head>
+<body>
+    <div class="container">
+        <h1>TODO App</h1>
+        <form id="todo-form">
+            <input type="text" id="todo-input" placeholder="Add a new task..." autocomplete="off">
+            <button type="submit">Add</button>
+        </form>
+        <ul id="todo-list"></ul>
+    </div>
+    <script src="script.js"></script>
+</body>
+</html>
\ No newline at end of file
diff --git a/example/demo003/script.js b/example/demo003/script.js
new file mode 100644
index 0000000..d0001f2
--- /dev/null
+++ b/example/demo003/script.js
@@ -0,0 +1,54 @@
+document.addEventListener('DOMContentLoaded', () => {
+    const todoForm = document.getElementById('todo-form');
+    const todoInput = document.getElementById('todo-input');
+    const todoList = document.getElementById('todo-list');
+
+    // Load todos from local storage
+    const todos = JSON.parse(localStorage.getItem('todos')) || [];
+
+    const saveTodos = () => {
+        localStorage.setItem('todos', JSON.stringify(todos));
+    };
+
+    const renderTodos = () => {
+        todoList.innerHTML = '';
+        todos.forEach((todo, index) => {
+            const li = document.createElement('li');
+            li.textContent = todo.text;
+            if (todo.completed) {
+                li.classList.add('completed');
+            }
+
+            li.addEventListener('click', () => {
+                todos[index].completed = !todos[index].completed;
+                saveTodos();
+                renderTodos();
+            });
+
+            const deleteButton = document.createElement('button');
+            deleteButton.textContent = 'Delete';
+            deleteButton.addEventListener('click', (e) => {
+                e.stopPropagation();
+                todos.splice(index, 1);
+                saveTodos();
+                renderTodos();
+            });
+
+            li.appendChild(deleteButton);
+            todoList.appendChild(li);
+        });
+    };
+
+    todoForm.addEventListener('submit', (e) => {
+        e.preventDefault();
+        const newTodoText = todoInput.value.trim();
+        if (newTodoText !== '') {
+            todos.push({ text: newTodoText, completed: false });
+            saveTodos();
+            renderTodos();
+            todoInput.value = '';
+        }
+    });
+
+    renderTodos();
+});
\ No newline at end of file
diff --git a/example/demo003/style.css b/example/demo003/style.css
new file mode 100644
index 0000000..57e8f67
--- /dev/null
+++ b/example/demo003/style.css
@@ -0,0 +1,82 @@
+body {
+    font-family: sans-serif;
+    background-color: #f4f4f4;
+    margin: 0;
+    display: flex;
+    justify-content: center;
```

---

## ⏰ 22:56:31 - `ca9d57e`
**Merge pull request #3 from Sunwood-ai-labsII/issue/2/create-todo-app**
*by Yukihiko.F@sunwood.ai.labs*

### 📋 Changed Files
```bash
Merge: 2386425 1bf0fc8
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 22:56:31 2025 +0900
```

### 📊 Statistics
```bash
Merge: 2386425 1bf0fc8
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 22:56:31 2025 +0900

    Merge pull request #3 from Sunwood-ai-labsII/issue/2/create-todo-app
    
    feat: ✨ Create TODO App

 example/demo003/index.html | 20 +++++++++++
 example/demo003/script.js  | 54 ++++++++++++++++++++++++++++++
 example/demo003/style.css  | 82 ++++++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 156 insertions(+)
```

### 💻 Code Changes
```diff
```

---

