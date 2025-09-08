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

## ⏰ 22:59:50 - `518aa5a`
**Update gemini-issue-automated-triage.yml**
*by Yukihiko.F@sunwood.ai.labs*

### 📋 Changed Files
```bash
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 22:59:50 2025 +0900
M	.github/workflows/gemini-issue-automated-triage.yml
```

### 📊 Statistics
```bash
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 22:59:50 2025 +0900

    Update gemini-issue-automated-triage.yml

 .../workflows/gemini-issue-automated-triage.yml    | 99 ++++++++++++++--------
 1 file changed, 62 insertions(+), 37 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index a532d09..cb45ff5 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -42,25 +42,24 @@ jobs:
             core.setOutput('title', issue.title || '');
             core.setOutput('body', issue.body || '');
 
-      - name: Get Labels
+      - name: Get Labels (existing in repo)
         id: labels
         uses: actions/github-script@v7
         with:
           script: |
             const labels = await github.paginate(github.rest.issues.listLabelsForRepo, {
               owner: context.repo.owner,
-              repo: context.repo.repo
+              repo: context.repo.repo,
+              per_page: 100
             });
             const names = labels.map(l => l.name);
             core.setOutput('available', names.join(','));
-            return names.join(',');
 
       - name: Analyze with Gemini
         id: gemini
         uses: google-github-actions/run-gemini-cli@v0
         with:
           gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
-          # ← ここは ${{ ... }} で式展開するのがポイント
           prompt: |
             You are a GitHub issue triage assistant.
             Issue Title: ${{ steps.issue.outputs.title }}
@@ -68,65 +67,92 @@ jobs:
             ---
             ${{ steps.issue.outputs.body }}
             ---
-            Available Labels (comma-separated): ${{ steps.labels.outputs.available }}
+            Existing Labels: ${{ steps.labels.outputs.available }}
+
+            Task:
+            - Suggest 1–3 labels that best categorize this issue.
+            - Prefer existing labels when a good match exists.
+            - If no existing label is a good match, you MAY propose new ones.
+            - New labels must be short, kebab-case (lowercase, hyphen-separated), no spaces or emojis.
+            - Output EXACTLY this XML (no extra text):
 
-            Task: Choose the MOST relevant labels from the available list only.
-            Return EXACTLY this XML (no prose, no markdown):
             <labels>
-            <label>label-1</label>
-            <label>label-2</label>
+              <label>first-label</label>
+              <label>second-label</label>
             </labels>
 
-
-      - name: Apply Labels
+      - name: Apply (create if missing) and Add Labels
         uses: actions/github-script@v7
         env:
           GEMINI_OUTPUT: ${{ steps.gemini.outputs.text || steps.gemini.outputs.summary }}
           ISSUE_NUMBER: ${{ steps.issue.outputs.number }}
+          EXISTING: ${{ steps.labels.outputs.available }}
         with:
           script: |
             const raw = process.env.GEMINI_OUTPUT || '';
-            const issueNumber = parseInt(process.env.ISSUE_NUMBER);
-      
+            const issueNumber = parseInt(process.env.ISSUE_NUMBER || '0', 10);
+            const existing = (process.env.EXISTING || '').split(',').map(s => s.trim()).filter(Boolean);
+
             console.log('Gemini output:', raw);
-      
-            let labels = [];
+
+            // 1) XMLから<label>…</label>を抽出
             const matches = raw.match(/<label>(.*?)<\/label>/gis);
-            if (matches) {
-              labels = matches
-                .map(m => m.replace(/<\/?label>/gi, '').trim())
-                .filter(Boolean);
-              console.log('Extracted labels from XML:', labels);
-            } else {
+            if (!matches) {
               throw new Error('❌ Gemini output に <label> タグが見つかりませんでした');
             }
-      
-            // ラベルごとに存在チェック → 無ければ作成
+
+            // 2) ラベル名の正規化（kebab-case & 不要文字除去）
+            const toKebab = (s) => {
+              return s
+                .toLowerCase()
+                .replace(/[_\s]+/g, '-')      // 空白/アンダーをハイフンへ
+                .replace(/[^a-z0-9-]/g, '')   // 英数とハイフン以外除去
+                .replace(/-+/g, '-')          // 連続ハイフンを1つに
+                .replace(/^-|-$/g, '');       // 先頭/末尾のハイフン除去
+            };
+
```

---

## ⏰ 23:29:40 - `26991f6`
**Update gemini-cli.yml**
*by Yukihiko.F@sunwood.ai.labs*

### 📋 Changed Files
```bash
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 23:29:40 2025 +0900
M	.github/workflows/gemini-cli.yml
```

### 📊 Statistics
```bash
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 23:29:40 2025 +0900

    Update gemini-cli.yml

 .github/workflows/gemini-cli.yml | 252 ++++++++++++++++-----------------------
 1 file changed, 100 insertions(+), 152 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 8473f12..3d6fc1f 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -2,107 +2,63 @@ name: '💬 Gemini CLI'
 
 on:
   pull_request_review_comment:
-    types:
-      - 'created'
+    types: [created]
   pull_request_review:
-    types:
-      - 'submitted'
+    types: [submitted]
   issue_comment:
-    types:
-      - 'created'
+    types: [created]
   issues:
-    types:
-      - 'opened'
+    types: [opened]
 
 concurrency:
-  group: '${{ github.workflow }}-${{ github.event.issue.number }}'
+  group: '${{ github.workflow }}-${{ github.event.issue.number || github.run_id }}'
+  # ↑ issues 以外でも安全に動くようにフォールバックを追加
   cancel-in-progress: |-
     ${{ github.event.sender.type == 'User' && ( github.event.issue.author_association == 'OWNER' || github.event.issue.author_association == 'MEMBER' || github.event.issue.author_association == 'COLLABORATOR') }}
 
 defaults:
   run:
-    shell: 'bash'
+    shell: bash
 
 permissions:
-  contents: 'write'
-  id-token: 'write'
-  pull-requests: 'write'
-  issues: 'write'
+  contents: write
+  id-token: write
+  pull-requests: write
+  issues: write
 
 jobs:
-  # gemini-cli:
-  #   # This condition seeks to ensure the action is only run when it is triggered by a trusted user.
-  #   # For private repos, users who have access to the repo are considered trusted.
-  #   # For public repos, users who members, owners, or collaborators are considered trusted.
-  #   if: |-
-  #     github.event_name == 'workflow_dispatch' ||
-  #     (
-  #       github.event_name == 'issues' && github.event.action == 'opened' &&
-  #       contains(github.event.issue.body, '@gemini-cli') &&
-  #       !contains(github.event.issue.body, '@gemini-cli /review') &&
-  #       !contains(github.event.issue.body, '@gemini-cli /triage') &&
-  #       (
-  #         github.event.repository.private == true ||
-  #         contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.issue.author_association)
-  #       )
-  #     ) ||
-  #     (
-  #       (
-  #         github.event_name == 'issue_comment' ||
-  #         github.event_name == 'pull_request_review_comment'
-  #       ) &&
-  #       contains(github.event.comment.body, '@gemini-cli') &&
-  #       !contains(github.event.comment.body, '@gemini-cli /review') &&
-  #       !contains(github.event.comment.body, '@gemini-cli /triage') &&
-  #       (
-  #         github.event.repository.private == true ||
-  #         contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association)
-  #       )
-  #     ) ||
-  #     (
-  #       github.event_name == 'pull_request_review' &&
-  #       contains(github.event.review.body, '@gemini-cli') &&
-  #       !contains(github.event.review.body, '@gemini-cli /review') &&
-  #       !contains(github.event.review.body, '@gemini-cli /triage') &&
-  #       (
-  #         github.event.repository.private == true ||
-  #         contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.review.author_association)
-  #       )
-  #     )
-
   gemini-cli:
-    # 一時的にシンプルな条件に変更してテスト
-    if: |-
-      github.event_name == 'issues' && github.event.action == 'opened' &&
+    # まずは簡易条件でテスト。必要なら元の複合条件へ戻せます
+    if: >-
+      github.event_name == 'issues' &&
+      github.event.action == 'opened' &&
       contains(github.event.issue.body, '@gemini-cli')
-
     timeout-minutes: 10
-    runs-on: 'ubuntu-latest'
+    runs-on: ubuntu-latest
```

---

## ⏰ 23:32:21 - `37dcb84`
**Update gemini-cli.yml**
*by Yukihiko.F@sunwood.ai.labs*

### 📋 Changed Files
```bash
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 23:32:21 2025 +0900
M	.github/workflows/gemini-cli.yml
```

### 📊 Statistics
```bash
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 23:32:21 2025 +0900

    Update gemini-cli.yml

 .github/workflows/gemini-cli.yml | 11 +++++++++--
 1 file changed, 9 insertions(+), 2 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 3d6fc1f..b25cac0 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -225,6 +225,13 @@ jobs:
           prompt: ${{ steps.read_prompt.outputs.prompt }}
 
       - name: Fail clearly when secrets are missing
-        if: ${{ failure() && (secrets.GEMINI_API_KEY == '' && (vars.GOOGLE_GENAI_USE_VERTEXAI != 'true')) }}
+        if: ${{ failure() }}
+        env:
+          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
+          USE_VERTEX_AI: ${{ vars.GOOGLE_GENAI_USE_VERTEXAI }}
         run: |
-          echo "::error:: GEMINI_API_KEY が未設定です（Vertex AI を使わない構成の場合は必須）。" && exit 1
+          set -euo pipefail
+          if [[ "${USE_VERTEX_AI}" != "true" && -z "${GEMINI_API_KEY}" ]]; then
+            echo "::error:: GEMINI_API_KEY が未設定です（Vertex AI を使わない構成では必須）。"
+            exit 1
+          fi
```

---

## ⏰ 23:35:22 - `147fbdf`
**Update gemini-cli.yml**
*by Yukihiko.F@sunwood.ai.labs*

### 📋 Changed Files
```bash
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 23:35:22 2025 +0900
M	.github/workflows/gemini-cli.yml
```

### 📊 Statistics
```bash
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 23:35:22 2025 +0900

    Update gemini-cli.yml

 .github/workflows/gemini-cli.yml | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index b25cac0..5881a57 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -204,7 +204,7 @@ jobs:
         # ↑↑ 必要なら v0 固定でもOKだが、マイナーの既知安定版を明示推奨
         with:
           # ---- 重要：CLI バージョンを固定して回帰を遮断 ----
-          gemini_cli_version: '0.3.3'                  # ← 直近で動いた版に固定（例）
+          gemini_cli_version: '0.3.4'                  # ← 直近で動いた版に固定（例）
           # ---- 認証/モデルは“入力”として明示（env 依存しない）----
           gemini_api_key: ${{ secrets.GEMINI_API_KEY }} # Vertex を使わない場合は必須
           gemini_model: 'gemini-2.5-pro'              # ← 明示的に指定（必要に応じて pro へ）
```

---

## ⏰ 23:37:43 - `444d528`
**Update gemini-cli.yml**
*by Yukihiko.F@sunwood.ai.labs*

### 📋 Changed Files
```bash
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 23:37:43 2025 +0900
M	.github/workflows/gemini-cli.yml
```

### 📊 Statistics
```bash
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 23:37:43 2025 +0900

    Update gemini-cli.yml

 .github/workflows/gemini-cli.yml | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 5881a57..87bda35 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -204,7 +204,7 @@ jobs:
         # ↑↑ 必要なら v0 固定でもOKだが、マイナーの既知安定版を明示推奨
         with:
           # ---- 重要：CLI バージョンを固定して回帰を遮断 ----
-          gemini_cli_version: '0.3.4'                  # ← 直近で動いた版に固定（例）
+          gemini_cli_version: '0.4.0-preview.2'                  # ← 直近で動いた版に固定（例）
           # ---- 認証/モデルは“入力”として明示（env 依存しない）----
           gemini_api_key: ${{ secrets.GEMINI_API_KEY }} # Vertex を使わない場合は必須
           gemini_model: 'gemini-2.5-pro'              # ← 明示的に指定（必要に応じて pro へ）
```

---

