# 📝 Daily Commits

## ⏰ 11:27:17 - `adaab4e`
**Initial commit**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sun Aug 24 11:27:17 2025 +0900
A	.SourceSageignore
A	.github/workflows/sync-to-report-gh.yml
A	.gitignore
A	LICENSE
A	README.md
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sun Aug 24 11:27:17 2025 +0900

    Initial commit

 .SourceSageignore                       |  54 +++++++
 .github/workflows/sync-to-report-gh.yml |  52 +++++++
 .gitignore                              | 208 +++++++++++++++++++++++++
 LICENSE                                 |  21 +++
 README.md                               | 267 ++++++++++++++++++++++++++++++++
 5 files changed, 602 insertions(+)
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
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
new file mode 100644
index 0000000..6dc1edd
--- /dev/null
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -0,0 +1,52 @@
+name: 📊 デイリーレポートハブ同期 v2.3 (YUKIHIKO PR版 - 完全リモート実行)
+on:
+  push:
+    branches: [main, master]
+  pull_request:
+    types: [opened, synchronize, closed]
+
+env:
+  WEEK_START_DAY: 1
+  AUTO_APPROVE: true
+  AUTO_MERGE: true  
+  CREATE_PR: true
+  # リモートスクリプトの設定
+  SCRIPTS_BASE_URL: https://raw.githubusercontent.com/Sunwood-ai-labsII/daily-report-hub_dev/main/.github/scripts
+
+jobs:
+  sync-data:
+    runs-on: ubuntu-latest
+    steps:
+      - name: 📥 現在のリポジトリをチェックアウト
+        uses: actions/checkout@v4
+        with:
+          fetch-depth: 0
+
+      - name: 📅 週情報を計算
+        run: curl -LsSf ${SCRIPTS_BASE_URL}/calculate-week-info.sh | sh -s -- ${{ env.WEEK_START_DAY }}
+
+      - name: 🔍 Git活動を分析
+        run: curl -LsSf ${SCRIPTS_BASE_URL}/analyze-git-activity.sh | sh
+
+      - name: 📝 Markdownレポートを生成
+        run: curl -LsSf ${SCRIPTS_BASE_URL}/generate-markdown-reports.sh | sh
+
+      - name: 📂 レポートハブをクローン
```

---

## ⏰ 02:37:26 - `6815732`
**🤖 PRレビューワークフローの追加**
*by maki*

### 📋 Changed Files
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Aug 24 02:37:26 2025 +0000
A	.github/workflows/gemini-pr-review.yml
```

### 📊 Statistics
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Aug 24 02:37:26 2025 +0000

    🤖 PRレビューワークフローの追加
    
    - Gemini AIを活用したプルリクエスト自動レビューの実装
    - MCPサーバーを使用したGitHub連携機能
    - セキュリティとパフォーマンスに配慮した詳細な設定
    - 信頼されたユーザーのみ実行可能に設定

 .github/workflows/gemini-pr-review.yml | 468 +++++++++++++++++++++++++++++++++
 1 file changed, 468 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/gemini-pr-review.yml b/.github/workflows/gemini-pr-review.yml
new file mode 100644
index 0000000..3b5bb9b
--- /dev/null
+++ b/.github/workflows/gemini-pr-review.yml
@@ -0,0 +1,468 @@
+name: '🧐 Gemini Pull Request Review'
+
+on:
+  pull_request:
+    types:
+      - 'opened'
+      - 'reopened'
+  issue_comment:
+    types:
+      - 'created'
+  pull_request_review_comment:
+    types:
+      - 'created'
+  pull_request_review:
+    types:
+      - 'submitted'
+  workflow_dispatch:
+    inputs:
+      pr_number:
+        description: 'PR number to review'
+        required: true
+        type: 'number'
+
+concurrency:
+  group: '${{ github.workflow }}-${{ github.head_ref || github.ref }}'
+  cancel-in-progress: true
+
+defaults:
+  run:
+    shell: 'bash'
+
+permissions:
+  contents: 'read'
+  id-token: 'write'
+  issues: 'write'
+  pull-requests: 'write'
+  statuses: 'write'
+
+jobs:
+  review-pr:
+    # This condition seeks to ensure the action is only run when it is triggered by a trusted user.
+    # For private repos, users who have access to the repo are considered trusted.
+    # For public repos, users who members, owners, or collaborators are considered trusted.
+    if: |-
+      github.event_name == 'workflow_dispatch' ||
+      (
+        github.event_name == 'pull_request' &&
+        (
+          github.event.repository.private == true ||
+          contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.pull_request.author_association)
+        )
+      ) ||
+      (
+        (
+          (
+            github.event_name == 'issue_comment' &&
+            github.event.issue.pull_request
+          ) ||
+          github.event_name == 'pull_request_review_comment'
+        ) &&
+        contains(github.event.comment.body, '@gemini-cli /review') &&
+        (
+          github.event.repository.private == true ||
+          contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association)
+        )
+      ) ||
+      (
+        github.event_name == 'pull_request_review' &&
+        contains(github.event.review.body, '@gemini-cli /review') &&
+        (
+          github.event.repository.private == true ||
+          contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.review.author_association)
+        )
+      )
+    timeout-minutes: 5
+    runs-on: 'ubuntu-latest'
+    steps:
+      - name: 'Checkout PR code'
+        uses: 'actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683' # ratchet:actions/checkout@v4
+
+      - name: 'Generate GitHub App Token'
+        id: 'generate_token'
+        if: |-
+          ${{ vars.APP_ID }}
+        uses: 'actions/create-github-app-token@df432ceedc7162793a195dd1713ff69aefc7379e' # ratchet:actions/create-github-app-token@v2
+        with:
+          app-id: '${{ vars.APP_ID }}'
+          private-key: '${{ secrets.APP_PRIVATE_KEY }}'
+
+      - name: 'Get PR details (pull_request & workflow_dispatch)'
+        id: 'get_pr'
+        if: |-
+          ${{ github.event_name == 'pull_request' || github.event_name == 'workflow_dispatch' }}
+        env:
```

---

## ⏰ 02:37:39 - `2f890e1`
**💬 Gemini CLIワークフローの追加**
*by maki*

### 📋 Changed Files
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Aug 24 02:37:39 2025 +0000
A	.github/workflows/gemini-cli.yml
```

### 📊 Statistics
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Aug 24 02:37:39 2025 +0000

    💬 Gemini CLIワークフローの追加
    
    - GitHub issueやPRでのGemini AIとの対話機能の実装
    - 信頼されたユーザーのみ利用可能なセキュリティ設定
    - PRブランチでの直接コミットとプッシュ機能
    - タスク管理のためのチェックリスト機能

 .github/workflows/gemini-cli.yml | 315 +++++++++++++++++++++++++++++++++++++++
 1 file changed, 315 insertions(+)
```

### 💻 Code Changes
```diff
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
+      github.event_name == 'workflow_dispatch' ||
+      (
+        github.event_name == 'issues' && github.event.action == 'opened' &&
+        contains(github.event.issue.body, '@gemini-cli') &&
+        !contains(github.event.issue.body, '@gemini-cli /review') &&
+        !contains(github.event.issue.body, '@gemini-cli /triage') &&
+        (
+          github.event.repository.private == true ||
+          contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.issue.author_association)
+        )
+      ) ||
+      (
+        (
+          github.event_name == 'issue_comment' ||
+          github.event_name == 'pull_request_review_comment'
+        ) &&
+        contains(github.event.comment.body, '@gemini-cli') &&
+        !contains(github.event.comment.body, '@gemini-cli /review') &&
+        !contains(github.event.comment.body, '@gemini-cli /triage') &&
+        (
+          github.event.repository.private == true ||
+          contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association)
+        )
+      ) ||
+      (
+        github.event_name == 'pull_request_review' &&
+        contains(github.event.review.body, '@gemini-cli') &&
+        !contains(github.event.review.body, '@gemini-cli /review') &&
+        !contains(github.event.review.body, '@gemini-cli /triage') &&
+        (
+          github.event.repository.private == true ||
+          contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.review.author_association)
+        )
+      )
+    timeout-minutes: 10
+    runs-on: 'ubuntu-latest'
+    steps:
+      - name: 'Generate GitHub App Token'
+        id: 'generate_token'
+        if: |-
+          ${{ vars.APP_ID }}
+        uses: 'actions/create-github-app-token@df432ceedc7162793a195dd1713ff69aefc7379e' # ratchet:actions/create-github-app-token@v2
+        with:
+          app-id: '${{ vars.APP_ID }}'
+          private-key: '${{ secrets.APP_PRIVATE_KEY }}'
+
+      - name: 'Get context from event'
+        id: 'get_context'
+        env:
+          EVENT_NAME: '${{ github.event_name }}'
+          EVENT_PAYLOAD: '${{ toJSON(github.event) }}'
+        run: |-
+          set -euo pipefail
+
+          USER_REQUEST=""
+          ISSUE_NUMBER=""
+          IS_PR="false"
+
+          if [[ "${EVENT_NAME}" == "issues" ]]; then
+            USER_REQUEST=$(echo "${EVENT_PAYLOAD}" | jq -r .issue.body)
```

---

## ⏰ 02:37:53 - `2941ac4`
**🏷️ Issue自動トリアージワークフローの追加**
*by maki*

### 📋 Changed Files
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Aug 24 02:37:53 2025 +0000
A	.github/workflows/gemini-issue-automated-triage.yml
```

### 📊 Statistics
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Aug 24 02:37:53 2025 +0000

    🏷️ Issue自動トリアージワークフローの追加
    
    - 新規作成されたGitHub issueの自動分類機能の実装
    - 既存のラベルに基づいたインテリジェントなラベル付け
    - 信頼されたユーザーのみ実行可能なセキュリティ設定
    - ワークフロー実行時の詳細なログとエラーハンドリング

 .../workflows/gemini-issue-automated-triage.yml    | 191 +++++++++++++++++++++
 1 file changed, 191 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
new file mode 100644
index 0000000..375bc0e
--- /dev/null
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -0,0 +1,191 @@
+name: '🏷️ Gemini Automated Issue Triage'
+
+on:
+  issues:
+    types:
+      - 'opened'
+      - 'reopened'
+  issue_comment:
+    types:
+      - 'created'
+  workflow_dispatch:
+    inputs:
+      issue_number:
+        description: 'issue number to triage'
+        required: true
+        type: 'number'
+
+concurrency:
+  group: '${{ github.workflow }}-${{ github.event.issue.number }}'
+  cancel-in-progress: true
+
+defaults:
+  run:
+    shell: 'bash'
+
+permissions:
+  contents: 'read'
+  id-token: 'write'
+  issues: 'write'
+  statuses: 'write'
+
+jobs:
+  triage-issue:
+    if: |-
+      github.event_name == 'issues' ||
+      github.event_name == 'workflow_dispatch' ||
+      (
+        github.event_name == 'issue_comment' &&
+        contains(github.event.comment.body, '@gemini-cli /triage') &&
+        contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association)
+      )
+    timeout-minutes: 5
+    runs-on: 'ubuntu-latest'
+    steps:
+      - name: 'Checkout repository'
+        uses: 'actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683' # ratchet:actions/checkout@v4
+
+      - name: 'Generate GitHub App Token'
+        id: 'generate_token'
+        if: |-
+          ${{ vars.APP_ID }}
+        uses: 'actions/create-github-app-token@df432ceedc7162793a195dd1713ff69aefc7379e' # ratchet:actions/create-github-app-token@v2
+        with:
+          app-id: '${{ vars.APP_ID }}'
+          private-key: '${{ secrets.APP_PRIVATE_KEY }}'
+
+      - name: 'Get Repository Labels'
+        id: 'get_labels'
+        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+        with:
+          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          script: |-
+            const { data: labels } = await github.rest.issues.listLabelsForRepo({
+              owner: context.repo.owner,
+              repo: context.repo.repo,
+            });
+            const labelNames = labels.map(label => label.name);
+            core.setOutput('available_labels', labelNames.join(','));
+            core.info(`Found ${labelNames.length} labels: ${labelNames.join(', ')}`);
+            return labelNames;
+
+      - name: 'Run Gemini Issue Analysis'
+        uses: 'google-github-actions/run-gemini-cli@v0'
+        id: 'gemini_issue_analysis'
+        env:
+          GITHUB_TOKEN: '' # Do not pass any auth token here since this runs on untrusted inputs
+          ISSUE_TITLE: '${{ github.event.issue.title }}'
+          ISSUE_BODY: '${{ github.event.issue.body }}'
+          ISSUE_NUMBER: '${{ github.event.issue.number }}'
+          REPOSITORY: '${{ github.repository }}'
+          AVAILABLE_LABELS: '${{ steps.get_labels.outputs.available_labels }}'
+        with:
+          gemini_cli_version: '${{ vars.GEMINI_CLI_VERSION }}'
+          gcp_workload_identity_provider: '${{ vars.GCP_WIF_PROVIDER }}'
+          gcp_project_id: '${{ vars.GOOGLE_CLOUD_PROJECT }}'
+          gcp_location: '${{ vars.GOOGLE_CLOUD_LOCATION }}'
+          gcp_service_account: '${{ vars.SERVICE_ACCOUNT_EMAIL }}'
+          gemini_api_key: '${{ secrets.GEMINI_API_KEY }}'
+          use_vertex_ai: '${{ vars.GOOGLE_GENAI_USE_VERTEXAI }}'
+          use_gemini_code_assist: '${{ vars.GOOGLE_GENAI_USE_GCA }}'
+          settings: |-
+            {
+              "debug": ${{ fromJSON(env.DEBUG || env.ACTIONS_STEP_DEBUG || false) }},
+              "maxSessionTurns": 25,
```

---

## ⏰ 02:38:06 - `950a670`
**📋 Issue定期トリアージワークフローの追加**
*by maki*

### 📋 Changed Files
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Aug 24 02:38:06 2025 +0000
A	.github/workflows/gemini-issue-scheduled-triage.yml
```

### 📊 Statistics
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Aug 24 02:38:06 2025 +0000

    📋 Issue定期トリアージワークフローの追加
    
    - 1時間ごとに実行される定期的なissueトリアージ機能
    - ラベルのないissueや「status/needs-triage」ラベルのissueを自動処理
    - 複数のissueを一括で処理する効率的な実装
    - 詳細なログとエラーハンドリング機能

 .../workflows/gemini-issue-scheduled-triage.yml    | 193 +++++++++++++++++++++
 1 file changed, 193 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/gemini-issue-scheduled-triage.yml b/.github/workflows/gemini-issue-scheduled-triage.yml
new file mode 100644
index 0000000..878dc72
--- /dev/null
+++ b/.github/workflows/gemini-issue-scheduled-triage.yml
@@ -0,0 +1,193 @@
+name: '📋 Gemini Scheduled Issue Triage'
+
+on:
+  schedule:
+    - cron: '0 * * * *' # Runs every hour
+  workflow_dispatch:
+
+concurrency:
+  group: '${{ github.workflow }}'
+  cancel-in-progress: true
+
+defaults:
+  run:
+    shell: 'bash'
+
+permissions:
+  contents: 'read'
+  id-token: 'write'
+  issues: 'write'
+  statuses: 'write'
+
+jobs:
+  triage-issues:
+    timeout-minutes: 5
+    runs-on: 'ubuntu-latest'
+    steps:
+      - name: 'Checkout repository'
+        uses: 'actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683' # ratchet:actions/checkout@v4
+
+      - name: 'Generate GitHub App Token'
+        id: 'generate_token'
+        if: |-
+          ${{ vars.APP_ID }}
+        uses: 'actions/create-github-app-token@df432ceedc7162793a195dd1713ff69aefc7379e' # ratchet:actions/create-github-app-token@v2
+        with:
+          app-id: '${{ vars.APP_ID }}'
+          private-key: '${{ secrets.APP_PRIVATE_KEY }}'
+
+      - name: 'Find untriaged issues'
+        id: 'find_issues'
+        env:
+          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          GITHUB_REPOSITORY: '${{ github.repository }}'
+          GITHUB_OUTPUT: '${{ github.output }}'
+        run: |-
+          set -euo pipefail
+
+          echo '🔍 Finding issues without labels...'
+          NO_LABEL_ISSUES="$(gh issue list --repo "${GITHUB_REPOSITORY}" \
+            --search 'is:open is:issue no:label' --json number,title,body)"
+
+          echo '🏷️ Finding issues that need triage...'
+          NEED_TRIAGE_ISSUES="$(gh issue list --repo "${GITHUB_REPOSITORY}" \
+            --search 'is:open is:issue label:"status/needs-triage"' --json number,title,body)"
+
+          echo '🔄 Merging and deduplicating issues...'
+          ISSUES="$(echo "${NO_LABEL_ISSUES}" "${NEED_TRIAGE_ISSUES}" | jq -c -s 'add | unique_by(.number)')"
+
+          echo '📝 Setting output for GitHub Actions...'
+          echo "issues_to_triage=${ISSUES}" >> "${GITHUB_OUTPUT}"
+
+          ISSUE_COUNT="$(echo "${ISSUES}" | jq 'length')"
+          echo "✅ Found ${ISSUE_COUNT} issues to triage! 🎯"
+
+      - name: 'Get Repository Labels'
+        id: 'get_labels'
+        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+        with:
+          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          script: |-
+            const { data: labels } = await github.rest.issues.listLabelsForRepo({
+              owner: context.repo.owner,
+              repo: context.repo.repo,
+            });
+            const labelNames = labels.map(label => label.name);
+            core.setOutput('available_labels', labelNames.join(','));
+            core.info(`Found ${labelNames.length} labels: ${labelNames.join(', ')}`);
+            return labelNames;
+
+      - name: 'Run Gemini Issue Analysis'
+        if: |-
+          ${{ steps.find_issues.outputs.issues_to_triage != '[]' }}
+        uses: 'google-github-actions/run-gemini-cli@v0'
+        id: 'gemini_issue_analysis'
+        env:
+          GITHUB_TOKEN: '' # Do not pass any auth token here since this runs on untrusted inputs
+          ISSUES_TO_TRIAGE: '${{ steps.find_issues.outputs.issues_to_triage }}'
+          REPOSITORY: '${{ github.repository }}'
+          AVAILABLE_LABELS: '${{ steps.get_labels.outputs.available_labels }}'
+        with:
+          gemini_cli_version: '${{ vars.GEMINI_CLI_VERSION }}'
+          gcp_workload_identity_provider: '${{ vars.GCP_WIF_PROVIDER }}'
+          gcp_project_id: '${{ vars.GOOGLE_CLOUD_PROJECT }}'
+          gcp_location: '${{ vars.GOOGLE_CLOUD_LOCATION }}'
```

---

## ⏰ 02:43:27 - `e8bbae0`
**🔀 Gemini GitHub自動化機能の統合**
*by maki*

### 📋 Changed Files
```bash
Merge: adaab4e 950a670
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Aug 24 02:43:27 2025 +0000
```

### 📊 Statistics
```bash
Merge: adaab4e 950a670
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Aug 24 02:43:27 2025 +0000

    🔀 Gemini GitHub自動化機能の統合
    
    - 🤖 PRレビューワークフロー
    - 💬 Gemini CLIワークフロー
    - 🏷️ Issue自動トリアージワークフロー
    - 📋 Issue定期トリアージワークフロー
    
    これらのワークフローにより、Gemini AIを活用した高度なGitHub自動化機能が利用可能になります。

 .github/workflows/gemini-cli.yml                   | 315 ++++++++++++++
 .../workflows/gemini-issue-automated-triage.yml    | 191 +++++++++
 .../workflows/gemini-issue-scheduled-triage.yml    | 193 +++++++++
 .github/workflows/gemini-pr-review.yml             | 468 +++++++++++++++++++++
 4 files changed, 1167 insertions(+)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 02:45:33 - `b953168`
**Merge branch 'develop'**
*by maki*

### 📋 Changed Files
```bash
Merge: adaab4e e8bbae0
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Aug 24 02:45:33 2025 +0000
```

### 📊 Statistics
```bash
Merge: adaab4e e8bbae0
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Sun Aug 24 02:45:33 2025 +0000

    Merge branch 'develop'

 .github/workflows/gemini-cli.yml                   | 315 ++++++++++++++
 .../workflows/gemini-issue-automated-triage.yml    | 191 +++++++++
 .../workflows/gemini-issue-scheduled-triage.yml    | 193 +++++++++
 .github/workflows/gemini-pr-review.yml             | 468 +++++++++++++++++++++
 4 files changed, 1167 insertions(+)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 12:01:07 - `97af745`
**Update gemini-issue-automated-triage.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sun Aug 24 12:01:07 2025 +0900
M	.github/workflows/gemini-issue-automated-triage.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sun Aug 24 12:01:07 2025 +0900

    Update gemini-issue-automated-triage.yml

 .../workflows/gemini-issue-automated-triage.yml    | 78 ++++++++++++----------
 1 file changed, 43 insertions(+), 35 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index 375bc0e..49d20e3 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -101,35 +101,21 @@ jobs:
               }
             }
           prompt: |-
-            ## Role
-
-            You are an issue triage assistant. Analyze the current GitHub issue
-            and identify the most appropriate existing labels. Use the available
-            tools to gather information; do not ask for information to be
-            provided.
-
-            ## Steps
-
-            1. Review the available labels in the environment variable: "${AVAILABLE_LABELS}".
-            2. Review the issue title and body provided in the environment
-               variables: "${ISSUE_TITLE}" and "${ISSUE_BODY}".
-            3. Classify the issue by the appropriate labels from the available labels.
-            4. Output the appropriate labels for this issue in JSON format with explanation, for example:
-               \```
-               {"labels_to_set": ["kind/bug", "priority/p0"], "explanation": "This is a critical bug report affecting main functionality"}
-               \```
-            5. If the issue cannot be classified using the available labels, output:
-               \```
-               {"labels_to_set": [], "explanation": "Unable to classify this issue with available labels"}
-               \```
-
-            ## Guidelines
-
-            - Only use labels that already exist in the repository
-            - Assign all applicable labels based on the issue content
-            - Reference all shell variables as "${VAR}" (with quotes and braces)
-            - Output only valid JSON format
-            - Do not include any explanation or additional text, just the JSON
+            You are an issue triage assistant. Analyze the GitHub issue and output ONLY valid JSON.
+
+            Available labels: ${AVAILABLE_LABELS}
+            Issue title: ${ISSUE_TITLE}
+            Issue body: ${ISSUE_BODY}
+
+            IMPORTANT: Output ONLY the JSON response, no explanations or additional text.
+
+            Required JSON format:
+            {"labels_to_set": ["label1", "label2"], "explanation": "brief explanation"}
+
+            If no appropriate labels exist, output:
+            {"labels_to_set": [], "explanation": "No suitable labels found"}
+
+            JSON response:
 
       - name: 'Apply Labels to Issue'
         if: |-
@@ -142,14 +128,36 @@ jobs:
         with:
           github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           script: |-
-            // Strip code block markers if present
+            // Strip code block markers if present and extract JSON
             const rawLabels = process.env.LABELS_OUTPUT;
-            core.info(`Raw labels JSON: ${rawLabels}`);
+            core.info(`Raw labels output: ${rawLabels}`);
+            
             let parsedLabels;
             try {
-              const trimmedLabels = rawLabels.replace(/^\```(?:json)?\s*/, '').replace(/\s*\```$/, '').trim();
-              parsedLabels = JSON.parse(trimmedLabels);
-              core.info(`Parsed labels JSON: ${JSON.stringify(parsedLabels)}`);
+              // JSONブロックを抽出するための正規表現
+              const jsonMatch = rawLabels.match(/\```json\s*([\s\S]*?)\s*\```/);
+              
+              let jsonString;
+              if (jsonMatch) {
+                // \```json \``` ブロックが見つかった場合
+                jsonString = jsonMatch[1].trim();
+                core.info(`Extracted JSON from code block: ${jsonString}`);
+              } else {
+                // JSONブロックがない場合、{ で始まる最初の行を探す
+                const lines = rawLabels.split('\n');
+                const jsonLine = lines.find(line => line.trim().startsWith('{'));
+                if (jsonLine) {
+                  jsonString = jsonLine.trim();
+                  core.info(`Extracted JSON from line: ${jsonString}`);
+                } else {
+                  // フォールバック: 元の方法
+                  jsonString = rawLabels.replace(/^\```(?:json)?\s*/, '').replace(/\s*\```$/, '').trim();
+                  core.info(`Using fallback extraction: ${jsonString}`);
+                }
+              }
+              
+              parsedLabels = JSON.parse(jsonString);
+              core.info(`Successfully parsed labels JSON: ${JSON.stringify(parsedLabels)}`);
             } catch (err) {
               core.setFailed(`Failed to parse labels JSON from Gemini output: ${err.message}\nRaw output: ${rawLabels}`);
               return;
@@ -187,5 +195,5 @@ jobs:
               owner: context.repo.owner,
               repo: context.repo.repo,
```

---

