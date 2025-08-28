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

