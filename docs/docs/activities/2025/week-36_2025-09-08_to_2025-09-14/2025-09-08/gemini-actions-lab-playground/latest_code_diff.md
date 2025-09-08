# 🔄 Latest Code Changes

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
+
     steps:
-      - name: 'Debug Event Information'
-        run: |-
+      - name: Debug Event Information
+        run: |
           echo "Event Name: ${{ github.event_name }}"
           echo "Event Action: ${{ github.event.action }}"
           echo "Issue Author: ${{ github.event.issue.user.login }}"
           echo "Author Association: ${{ github.event.issue.author_association }}"
 
-      - name: 'Generate GitHub App Token'
-        id: 'generate_token'
-        if: |-
-          ${{ vars.APP_ID }}
-        uses: 'actions/create-github-app-token@df432ceedc7162793a195dd1713ff69aefc7379e' # ratchet:actions/create-github-app-token@v2
+      - name: Generate GitHub App Token (optional)
+        id: generate_token
+        if: ${{ vars.APP_ID }}
+        uses: actions/create-github-app-token@df432ceedc7162793a195dd1713ff69aefc7379e # v2 pinned
         with:
-          app-id: '${{ vars.APP_ID }}'
-          private-key: '${{ secrets.APP_PRIVATE_KEY }}'
+          app-id: ${{ vars.APP_ID }}
+          private-key: ${{ secrets.APP_PRIVATE_KEY }}
 
-      - name: 'Get context from event'
-        id: 'get_context'
+      - name: Get context from event
+        id: get_context
         env:
-          EVENT_NAME: '${{ github.event_name }}'
-          EVENT_PAYLOAD: '${{ toJSON(github.event) }}'
-        run: |-
+          EVENT_NAME: ${{ github.event_name }}
+          EVENT_PAYLOAD: ${{ toJSON(github.event) }}
+        run: |
           set -euo pipefail
-
           USER_REQUEST=""
           ISSUE_NUMBER=""
           IS_PR="false"
@@ -126,11 +82,8 @@ jobs:
             IS_PR="true"
           fi
 
-          # Clean up user request
           CLEANED_USER_REQUEST=$(echo "${USER_REQUEST}" | sed 's/.*@gemini-cli//' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
-          
-          # ⬇⬇⬇ ここからが修正箇所 ⬇⬇⬇
-          # GITHUB_OUTPUTへの書き込みをヒアドキュメント形式に変更して、特殊文字によるエラーを回避
+
           {
             echo 'user_request<<EOF'
             echo "${CLEANED_USER_REQUEST}"
@@ -138,55 +91,48 @@ jobs:
             echo "issue_number=${ISSUE_NUMBER}"
             echo "is_pr=${IS_PR}"
           } >> "${GITHUB_OUTPUT}"
-          # ⬆⬆⬆ ここまでが修正箇所 ⬆⬆⬆
 
-      - name: 'Set up git user for commits'
-        run: |-
+      - name: Set up git user for commits
+        run: |
           git config --global user.name 'gemini-cli[bot]'
           git config --global user.email 'gemini-cli[bot]@users.noreply.github.com'
 
-      - name: 'Checkout PR branch'
-        if: |-
-          ${{  steps.get_context.outputs.is_pr == 'true' }}
-        uses: 'actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683' # ratchet:actions/checkout@v4
+      - name: Checkout PR branch
+        if: ${{ steps.get_context.outputs.is_pr == 'true' }}
+        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4 pinned
         with:
-          token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          repository: '${{ github.repository }}'
-          ref: 'refs/pull/${{ steps.get_context.outputs.issue_number }}/head'
+          token: ${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}
+          repository: ${{ github.repository }}
+          ref: refs/pull/${{ steps.get_context.outputs.issue_number }}/head
           fetch-depth: 0
 
-      - name: 'Checkout main branch'
-        if: |-
-          ${{  steps.get_context.outputs.is_pr == 'false' }}
-        uses: 'actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683' # ratchet:actions/checkout@v4
+      - name: Checkout main branch
+        if: ${{ steps.get_context.outputs.is_pr == 'false' }}
+        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4 pinned
         with:
-          token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          repository: '${{ github.repository }}'
+          token: ${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}
+          repository: ${{ github.repository }}
           fetch-depth: 0
 
-      - name: 'Acknowledge request'
+      - name: Acknowledge request
         env:
-          GITHUB_ACTOR: '${{ github.actor }}'
-          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          ISSUE_NUMBER: '${{ steps.get_context.outputs.issue_number }}'
-          REPOSITORY: '${{ github.repository }}'
-          REQUEST_TYPE: '${{ steps.get_context.outputs.request_type }}'
-        run: |-
+          GITHUB_ACTOR: ${{ github.actor }}
+          GITHUB_TOKEN: ${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}
+          ISSUE_NUMBER: ${{ steps.get_context.outputs.issue_number }}
+          REPOSITORY: ${{ github.repository }}
+        run: |
           set -euo pipefail
-          MESSAGE="@${GITHUB_ACTOR} I've received your request and I'm working on it now! 🤖"
-          if [[ -n "${MESSAGE}" ]]; then
-            gh issue comment "${ISSUE_NUMBER}" \
-              --body "${MESSAGE}" \
-              --repo "${REPOSITORY}"
-          fi
+          gh issue comment "${ISSUE_NUMBER}" \
+            --body "@${GITHUB_ACTOR} 受け取りました。処理を開始します 🤖" \
+            --repo "${REPOSITORY}"
 
-      - name: 'Get description'
-        id: 'get_description'
+      - name: Get description
+        id: get_description
         env:
-          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          IS_PR: '${{ steps.get_context.outputs.is_pr }}'
-          ISSUE_NUMBER: '${{ steps.get_context.outputs.issue_number }}'
-        run: |-
+          GITHUB_TOKEN: ${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}
+          IS_PR: ${{ steps.get_context.outputs.is_pr }}
+          ISSUE_NUMBER: ${{ steps.get_context.outputs.issue_number }}
+        run: |
           set -euo pipefail
           if [[ "${IS_PR}" == "true" ]]; then
             DESCRIPTION=$(gh pr view "${ISSUE_NUMBER}" --json body --template '{{.body}}')
@@ -199,13 +145,13 @@ jobs:
             echo "EOF"
           } >> "${GITHUB_OUTPUT}"
 
-      - name: 'Get comments'
-        id: 'get_comments'
+      - name: Get comments
+        id: get_comments
         env:
-          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          IS_PR: '${{ steps.get_context.outputs.is_pr }}'
-          ISSUE_NUMBER: '${{ steps.get_context.outputs.issue_number }}'
-        run: |-
+          GITHUB_TOKEN: ${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}
+          IS_PR: ${{ steps.get_context.outputs.is_pr }}
+          ISSUE_NUMBER: ${{ steps.get_context.outputs.issue_number }}
+        run: |
           set -euo pipefail
           if [[ "${IS_PR}" == "true" ]]; then
             COMMENTS=$(gh pr view "${ISSUE_NUMBER}" --json comments --template '{{range .comments}}{{.author.login}}: {{.body}}{{"\n"}}{{end}}')
@@ -218,17 +164,17 @@ jobs:
             echo "EOF"
           } >> "${GITHUB_OUTPUT}"
 
-      - name: 'Read prompt from file (JA)'
-        id: 'read_prompt'
+      - name: Read prompt from file (JA)
+        id: read_prompt
         env:
-          REPOSITORY: '${{ github.repository }}'
-          EVENT_NAME: '${{ github.event_name }}'
-          ISSUE_NUMBER: '${{ steps.get_context.outputs.issue_number }}'
-          IS_PR: '${{ steps.get_context.outputs.is_pr }}'
-          DESCRIPTION: '${{ steps.get_description.outputs.description }}'
-          COMMENTS: '${{ steps.get_comments.outputs.comments }}'
-          USER_REQUEST: '${{ steps.get_context.outputs.user_request }}'
-        run: |-
+          REPOSITORY: ${{ github.repository }}
+          EVENT_NAME: ${{ github.event_name }}
+          ISSUE_NUMBER: ${{ steps.get_context.outputs.issue_number }}
+          IS_PR: ${{ steps.get_context.outputs.is_pr }}
+          DESCRIPTION: ${{ steps.get_description.outputs.description }}
+          COMMENTS: ${{ steps.get_comments.outputs.comments }}
+          USER_REQUEST: ${{ steps.get_context.outputs.user_request }}
+        run: |
           set -euo pipefail
           TEMPLATE_PATH=".github/prompts/gemini-cli_prompt.ja.md"
           if [[ ! -f "${TEMPLATE_PATH}" ]]; then
@@ -236,7 +182,6 @@ jobs:
             exit 1
           fi
 
-          # sedの代わりにperlを使用して、改行を含む変数を安全に置換
           EXPANDED=$(perl -p -e '
             s/\$\{REPOSITORY\}/$ENV{REPOSITORY}/g;
             s/\$\{EVENT_NAME\}/$ENV{EVENT_NAME}/g;
@@ -253,30 +198,33 @@ jobs:
             echo "EOF"
           } >> "${GITHUB_OUTPUT}"
 
-      - name: 'Run Gemini'
-        id: 'run_gemini'
-        uses: 'google-github-actions/run-gemini-cli@v0'
-        env:
-          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          REPOSITORY: '${{ github.repository }}'
-          USER_REQUEST: '${{ steps.get_context.outputs.user_request }}'
-          ISSUE_NUMBER: '${{ steps.get_context.outputs.issue_number }}'
-          IS_PR: '${{ steps.get_context.outputs.is_pr }}'
+      - name: Run Gemini (pinned + explicit model)
+        id: run_gemini
+        uses: google-github-actions/run-gemini-cli@v0.1.12  # ← アクションをピン留め
+        # ↑↑ 必要なら v0 固定でもOKだが、マイナーの既知安定版を明示推奨
         with:
-          gemini_api_key: '${{ secrets.GEMINI_API_KEY }}'
-          gcp_workload_identity_provider: '${{ vars.GCP_WIF_PROVIDER }}'
-          gcp_project_id: '${{ vars.GOOGLE_CLOUD_PROJECT }}'
-          gcp_location: '${{ vars.GOOGLE_CLOUD_LOCATION }}'
-          gcp_service_account: '${{ vars.SERVICE_ACCOUNT_EMAIL }}'
-          use_vertex_ai: '${{ vars.GOOGLE_GENAI_USE_VERTEXAI }}'
-          use_gemini_code_assist: '${{ vars.GOOGLE_GENAI_USE_GCA }}'
-          settings: |-
+          # ---- 重要：CLI バージョンを固定して回帰を遮断 ----
+          gemini_cli_version: '0.3.3'                  # ← 直近で動いた版に固定（例）
+          # ---- 認証/モデルは“入力”として明示（env 依存しない）----
+          gemini_api_key: ${{ secrets.GEMINI_API_KEY }} # Vertex を使わない場合は必須
+          gemini_model: 'gemini-2.5-pro'              # ← 明示的に指定（必要に応じて pro へ）
+          gemini_debug: true                            # 追加ログで原因特定しやすく
+          # Vertex / GCA を使う構成なら以下を有効化
+          gcp_workload_identity_provider: ${{ vars.GCP_WIF_PROVIDER }}
+          gcp_project_id: ${{ vars.GOOGLE_CLOUD_PROJECT }}
+          gcp_location: ${{ vars.GOOGLE_CLOUD_LOCATION }}
+          gcp_service_account: ${{ vars.SERVICE_ACCOUNT_EMAIL }}
+          use_vertex_ai: ${{ vars.GOOGLE_GENAI_USE_VERTEXAI }}
+          use_gemini_code_assist: ${{ vars.GOOGLE_GENAI_USE_GCA }}
+          settings: |
             {
-              "debug": ${{ fromJSON(env.DEBUG || env.ACTIONS_STEP_DEBUG || false) }},
+              "debug": true,
               "maxSessionTurns": 50,
-              "telemetry": {
-                "enabled": false,
-                "target": "gcp"
-              }
+              "telemetry": { "enabled": false, "target": "gcp" }
             }
           prompt: ${{ steps.read_prompt.outputs.prompt }}
+
+      - name: Fail clearly when secrets are missing
+        if: ${{ failure() && (secrets.GEMINI_API_KEY == '' && (vars.GOOGLE_GENAI_USE_VERTEXAI != 'true')) }}
+        run: |
+          echo "::error:: GEMINI_API_KEY が未設定です（Vertex AI を使わない構成の場合は必須）。" && exit 1
```
