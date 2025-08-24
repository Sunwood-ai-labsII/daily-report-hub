# 🔄 Latest Code Changes

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
+            ISSUE_NUMBER=$(echo "${EVENT_PAYLOAD}" | jq -r .issue.number)
+          elif [[ "${EVENT_NAME}" == "issue_comment" ]]; then
+            USER_REQUEST=$(echo "${EVENT_PAYLOAD}" | jq -r .comment.body)
+            ISSUE_NUMBER=$(echo "${EVENT_PAYLOAD}" | jq -r .issue.number)
+            if [[ $(echo "${EVENT_PAYLOAD}" | jq -r .issue.pull_request) != "null" ]]; then
+              IS_PR="true"
+            fi
+          elif [[ "${EVENT_NAME}" == "pull_request_review" ]]; then
+            USER_REQUEST=$(echo "${EVENT_PAYLOAD}" | jq -r .review.body)
+            ISSUE_NUMBER=$(echo "${EVENT_PAYLOAD}" | jq -r .pull_request.number)
+            IS_PR="true"
+          elif [[ "${EVENT_NAME}" == "pull_request_review_comment" ]]; then
+            USER_REQUEST=$(echo "${EVENT_PAYLOAD}" | jq -r .comment.body)
+            ISSUE_NUMBER=$(echo "${EVENT_PAYLOAD}" | jq -r .pull_request.number)
+            IS_PR="true"
+          fi
+
+          # Clean up user request
+          USER_REQUEST=$(echo "${USER_REQUEST}" | sed 's/.*@gemini-cli//' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
+
+          {
+            echo "user_request=${USER_REQUEST}"
+            echo "issue_number=${ISSUE_NUMBER}"
+            echo "is_pr=${IS_PR}"
+          } >> "${GITHUB_OUTPUT}"
+
+      - name: 'Set up git user for commits'
+        run: |-
+          git config --global user.name 'gemini-cli[bot]'
+          git config --global user.email 'gemini-cli[bot]@users.noreply.github.com'
+
+      - name: 'Checkout PR branch'
+        if: |-
+          ${{  steps.get_context.outputs.is_pr == 'true' }}
+        uses: 'actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683' # ratchet:actions/checkout@v4
+        with:
+          token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          repository: '${{ github.repository }}'
+          ref: 'refs/pull/${{ steps.get_context.outputs.issue_number }}/head'
+          fetch-depth: 0
+
+      - name: 'Checkout main branch'
+        if: |-
+          ${{  steps.get_context.outputs.is_pr == 'false' }}
+        uses: 'actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683' # ratchet:actions/checkout@v4
+        with:
+          token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          repository: '${{ github.repository }}'
+          fetch-depth: 0
+
+      - name: 'Acknowledge request'
+        env:
+          GITHUB_ACTOR: '${{ github.actor }}'
+          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          ISSUE_NUMBER: '${{ steps.get_context.outputs.issue_number }}'
+          REPOSITORY: '${{ github.repository }}'
+          REQUEST_TYPE: '${{ steps.get_context.outputs.request_type }}'
+        run: |-
+          set -euo pipefail
+          MESSAGE="@${GITHUB_ACTOR} I've received your request and I'm working on it now! 🤖"
+          if [[ -n "${MESSAGE}" ]]; then
+            gh issue comment "${ISSUE_NUMBER}" \
+              --body "${MESSAGE}" \
+              --repo "${REPOSITORY}"
+          fi
+
+      - name: 'Get description'
+        id: 'get_description'
+        env:
+          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          IS_PR: '${{ steps.get_context.outputs.is_pr }}'
+          ISSUE_NUMBER: '${{ steps.get_context.outputs.issue_number }}'
+        run: |-
+          set -euo pipefail
+          if [[ "${IS_PR}" == "true" ]]; then
+            DESCRIPTION=$(gh pr view "${ISSUE_NUMBER}" --json body --template '{{.body}}')
+          else
+            DESCRIPTION=$(gh issue view "${ISSUE_NUMBER}" --json body --template '{{.body}}')
+          fi
+          {
+            echo "description<<EOF"
+            echo "${DESCRIPTION}"
+            echo "EOF"
+          } >> "${GITHUB_OUTPUT}"
+
+      - name: 'Get comments'
+        id: 'get_comments'
+        env:
+          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          IS_PR: '${{ steps.get_context.outputs.is_pr }}'
+          ISSUE_NUMBER: '${{ steps.get_context.outputs.issue_number }}'
+        run: |-
+          set -euo pipefail
+          if [[ "${IS_PR}" == "true" ]]; then
+            COMMENTS=$(gh pr view "${ISSUE_NUMBER}" --json comments --template '{{range .comments}}{{.author.login}}: {{.body}}{{"\n"}}{{end}}')
+          else
+            COMMENTS=$(gh issue view "${ISSUE_NUMBER}" --json comments --template '{{range .comments}}{{.author.login}}: {{.body}}{{"\n"}}{{end}}')
+          fi
+          {
+            echo "comments<<EOF"
+            echo "${COMMENTS}"
+            echo "EOF"
+          } >> "${GITHUB_OUTPUT}"
+
+      - name: 'Run Gemini'
+        id: 'run_gemini'
+        uses: 'google-github-actions/run-gemini-cli@v0'
+        env:
+          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          REPOSITORY: '${{ github.repository }}'
+          USER_REQUEST: '${{ steps.get_context.outputs.user_request }}'
+          ISSUE_NUMBER: '${{ steps.get_context.outputs.issue_number }}'
+          IS_PR: '${{ steps.get_context.outputs.is_pr }}'
+        with:
+          gemini_api_key: '${{ secrets.GEMINI_API_KEY }}'
+          gcp_workload_identity_provider: '${{ vars.GCP_WIF_PROVIDER }}'
+          gcp_project_id: '${{ vars.GOOGLE_CLOUD_PROJECT }}'
+          gcp_location: '${{ vars.GOOGLE_CLOUD_LOCATION }}'
+          gcp_service_account: '${{ vars.SERVICE_ACCOUNT_EMAIL }}'
+          use_vertex_ai: '${{ vars.GOOGLE_GENAI_USE_VERTEXAI }}'
+          use_gemini_code_assist: '${{ vars.GOOGLE_GENAI_USE_GCA }}'
+          settings: |-
+            {
+              "debug": ${{ fromJSON(env.DEBUG || env.ACTIONS_STEP_DEBUG || false) }},
+              "maxSessionTurns": 50,
+              "telemetry": {
+                "enabled": false,
+                "target": "gcp"
+              }
+            }
+          prompt: |-
+            ## Role
+
+            You are a helpful AI assistant invoked via a CLI interface in a GitHub workflow. You have access to tools to interact with the repository and respond to the user.
+
+            ## Context
+
+            - **Repository**: `${{ github.repository }}`
+            - **Triggering Event**: `${{ github.event_name }}`
+            - **Issue/PR Number**: `${{ steps.get_context.outputs.issue_number }}`
+            - **Is this a PR?**: `${{ steps.get_context.outputs.is_pr }}`
+            - **Issue/PR Description**:
+            `${{ steps.get_description.outputs.description }}`
+            - **Comments**:
+            `${{ steps.get_comments.outputs.comments }}`
+
+            ## User Request
+
+            The user has sent the following request:
+            `${{ steps.get_context.outputs.user_request }}`
+
+            ## How to Respond to Issues, PR Comments, and Questions
+
+            This workflow supports three main scenarios:
+
+            1. **Creating a Fix for an Issue**
+               - Carefully read the user request and the related issue or PR description.
+               - Use available tools to gather all relevant context (e.g., `gh issue view`, `gh pr view`, `gh pr diff`, `cat`, `head`, `tail`).
+               - Identify the root cause of the problem before proceeding.
+               - **Show and maintain a plan as a checklist**:
+                 - At the very beginning, outline the steps needed to resolve the issue or address the request and post them as a checklist comment on the issue or PR (use GitHub markdown checkboxes: `- [ ] Task`).
+                 - Example:
+                   \```
+                   ### Plan
+                   - [ ] Investigate the root cause
+                   - [ ] Implement the fix in `file.py`
+                   - [ ] Add/modify tests
+                   - [ ] Update documentation
+                   - [ ] Verify the fix and close the issue
+                   \```
+                 - Use: `gh pr comment "${ISSUE_NUMBER}" --body "<plan>"` or `gh issue comment "${ISSUE_NUMBER}" --body "<plan>"` to post the initial plan.
+                 - As you make progress, keep the checklist visible and up to date by editing the same comment (check off completed tasks with `- [x]`).
+                   - To update the checklist:
+                     1. Find the comment ID for the checklist (use `gh pr comment list "${ISSUE_NUMBER}"` or `gh issue comment list "${ISSUE_NUMBER}"`).
+                     2. Edit the comment with the updated checklist:
+                        - For PRs: `gh pr comment --edit <comment-id> --body "<updated plan>"`
+                        - For Issues: `gh issue comment --edit <comment-id> --body "<updated plan>"`
+                     3. The checklist should only be maintained as a comment on the issue or PR. Do not track or update the checklist in code files.
+               - If the fix requires code changes, determine which files and lines are affected. If clarification is needed, note any questions for the user.
+               - Make the necessary code or documentation changes using the available tools (e.g., `write_file`). Ensure all changes follow project conventions and best practices. Reference all shell variables as `"${VAR}"` (with quotes and braces) to prevent errors.
+               - Run any relevant tests or checks to verify the fix works as intended. If possible, provide evidence (test output, screenshots, etc.) that the issue is resolved.
+               - **Branching and Committing**:
+                 - **NEVER commit directly to the `main` branch.**
+                 - If you are working on a **pull request** (`IS_PR` is `true`), the correct branch is already checked out. Simply commit and push to it.
+                   - `git add .`
+                   - `git commit -m "feat: <describe the change>"`
+                   - `git push`
+                 - If you are working on an **issue** (`IS_PR` is `false`), create a new branch for your changes. A good branch name would be `issue/${ISSUE_NUMBER}/<short-description>`.
+                   - `git checkout -b issue/${ISSUE_NUMBER}/my-fix`
+                   - `git add .`
+                   - `git commit -m "feat: <describe the fix>"`
+                   - `git push origin issue/${ISSUE_NUMBER}/my-fix`
+                   - After pushing, you can create a pull request: `gh pr create --title "Fixes #${ISSUE_NUMBER}: <short title>" --body "This PR addresses issue #${ISSUE_NUMBER}."`
+               - Summarize what was changed and why in a markdown file: `write_file("response.md", "<your response here>")`
+               - Post the response as a comment:
+                 - For PRs: `gh pr comment "${ISSUE_NUMBER}" --body-file response.md`
+                 - For Issues: `gh issue comment "${ISSUE_NUMBER}" --body-file response.md`
+
+            2. **Addressing Comments on a Pull Request**
+               - Read the specific comment and the context of the PR.
+               - Use tools like `gh pr view`, `gh pr diff`, and `cat` to understand the code and discussion.
+               - If the comment requests a change or clarification, follow the same process as for fixing an issue: create a checklist plan, implement, test, and commit any required changes, updating the checklist as you go.
+               - **Committing Changes**: The correct PR branch is already checked out. Simply add, commit, and push your changes.
+                 - `git add .`
+                 - `git commit -m "fix: address review comments"`
+                 - `git push`
+               - If the comment is a question, answer it directly and clearly, referencing code or documentation as needed.
+               - Document your response in `response.md` and post it as a PR comment: `gh pr comment "${ISSUE_NUMBER}" --body-file response.md`
+
+            3. **Answering Any Question on an Issue**
+               - Read the question and the full issue context using `gh issue view` and related tools.
+               - Research or analyze the codebase as needed to provide an accurate answer.
+               - If the question requires code or documentation changes, follow the fix process above, including creating and updating a checklist plan and **creating a new branch for your changes as described in section 1.**
+               - Write a clear, concise answer in `response.md` and post it as an issue comment: `gh issue comment "${ISSUE_NUMBER}" --body-file response.md`
+
+            ## Guidelines
+
+            - **Be concise and actionable.** Focus on solving the user's problem efficiently.
+            - **Always commit and push your changes if you modify code or documentation.**
+            - **If you are unsure about the fix or answer, explain your reasoning and ask clarifying questions.**
+            - **Follow project conventions and best practices.**
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
+              "coreTools": [
+                "run_shell_command(echo)"
+              ],
+              "telemetry": {
+                "enabled": false,
+                "target": "gcp"
+              }
+            }
+          prompt: |-
+            ## Role
+
+            You are an issue triage assistant. Analyze the current GitHub issue
+            and identify the most appropriate existing labels. Use the available
+            tools to gather information; do not ask for information to be
+            provided.
+
+            ## Steps
+
+            1. Review the available labels in the environment variable: "${AVAILABLE_LABELS}".
+            2. Review the issue title and body provided in the environment
+               variables: "${ISSUE_TITLE}" and "${ISSUE_BODY}".
+            3. Classify the issue by the appropriate labels from the available labels.
+            4. Output the appropriate labels for this issue in JSON format with explanation, for example:
+               \```
+               {"labels_to_set": ["kind/bug", "priority/p0"], "explanation": "This is a critical bug report affecting main functionality"}
+               \```
+            5. If the issue cannot be classified using the available labels, output:
+               \```
+               {"labels_to_set": [], "explanation": "Unable to classify this issue with available labels"}
+               \```
+
+            ## Guidelines
+
+            - Only use labels that already exist in the repository
+            - Assign all applicable labels based on the issue content
+            - Reference all shell variables as "${VAR}" (with quotes and braces)
+            - Output only valid JSON format
+            - Do not include any explanation or additional text, just the JSON
+
+      - name: 'Apply Labels to Issue'
+        if: |-
+          ${{ steps.gemini_issue_analysis.outputs.summary != '' }}
+        env:
+          REPOSITORY: '${{ github.repository }}'
+          ISSUE_NUMBER: '${{ github.event.issue.number }}'
+          LABELS_OUTPUT: '${{ steps.gemini_issue_analysis.outputs.summary }}'
+        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+        with:
+          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          script: |-
+            // Strip code block markers if present
+            const rawLabels = process.env.LABELS_OUTPUT;
+            core.info(`Raw labels JSON: ${rawLabels}`);
+            let parsedLabels;
+            try {
+              const trimmedLabels = rawLabels.replace(/^\```(?:json)?\s*/, '').replace(/\s*\```$/, '').trim();
+              parsedLabels = JSON.parse(trimmedLabels);
+              core.info(`Parsed labels JSON: ${JSON.stringify(parsedLabels)}`);
+            } catch (err) {
+              core.setFailed(`Failed to parse labels JSON from Gemini output: ${err.message}\nRaw output: ${rawLabels}`);
+              return;
+            }
+
+            const issueNumber = parseInt(process.env.ISSUE_NUMBER);
+
+            // Set labels based on triage result
+            if (parsedLabels.labels_to_set && parsedLabels.labels_to_set.length > 0) {
+              await github.rest.issues.setLabels({
+                owner: context.repo.owner,
+                repo: context.repo.repo,
+                issue_number: issueNumber,
+                labels: parsedLabels.labels_to_set
+              });
+              const explanation = parsedLabels.explanation ? ` - ${parsedLabels.explanation}` : '';
+              core.info(`Successfully set labels for #${issueNumber}: ${parsedLabels.labels_to_set.join(', ')}${explanation}`);
+            } else {
+              // If no labels to set, leave the issue as is
+              const explanation = parsedLabels.explanation ? ` - ${parsedLabels.explanation}` : '';
+              core.info(`No labels to set for #${issueNumber}, leaving as is${explanation}`);
+            }
+
+      - name: 'Post Issue Analysis Failure Comment'
+        if: |-
+          ${{ failure() && steps.gemini_issue_analysis.outcome == 'failure' }}
+        env:
+          ISSUE_NUMBER: '${{ github.event.issue.number }}'
+          RUN_URL: '${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}'
+        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+        with:
+          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          script: |-
+            github.rest.issues.createComment({
+              owner: context.repo.owner,
+              repo: context.repo.repo,
+              issue_number: parseInt(process.env.ISSUE_NUMBER),
+              body: 'There is a problem with the Gemini CLI issue triaging. Please check the [action logs](${process.env.RUN_URL}) for details.'
+            })
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
+          gcp_service_account: '${{ vars.SERVICE_ACCOUNT_EMAIL }}'
+          gemini_api_key: '${{ secrets.GEMINI_API_KEY }}'
+          use_vertex_ai: '${{ vars.GOOGLE_GENAI_USE_VERTEXAI }}'
+          use_gemini_code_assist: '${{ vars.GOOGLE_GENAI_USE_GCA }}'
+          settings: |-
+            {
+              "debug": ${{ fromJSON(env.DEBUG || env.ACTIONS_STEP_DEBUG || false) }},
+              "maxSessionTurns": 25,
+              "coreTools": [
+                "run_shell_command(echo)"
+              ],
+              "telemetry": {
+                "enabled": false,
+                "target": "gcp"
+              }
+            }
+          prompt: |-
+            ## Role
+
+            You are an issue triage assistant. Analyze the GitHub issues and
+            identify the most appropriate existing labels to apply.
+
+            ## Steps
+
+            1. Review the available labels in the environment variable: "${AVAILABLE_LABELS}".
+            2. Review the issues in the environment variable: "${ISSUES_TO_TRIAGE}".
+            3. For each issue, classify it by the appropriate labels from the available labels.
+            4. Output a JSON array of objects, each containing the issue number,
+               the labels to set, and a brief explanation. For example:
+               \```
+               [
+                 {
+                   "issue_number": 123,
+                   "labels_to_set": ["kind/bug", "priority/p2"],
+                   "explanation": "This is a bug report with high priority based on the error description"
+                 },
+                 {
+                   "issue_number": 456,
+                   "labels_to_set": ["kind/enhancement"],
+                   "explanation": "This is a feature request for improving the UI"
+                 }
+               ]
+               \```
+            5. If an issue cannot be classified, do not include it in the output array.
+
+            ## Guidelines
+
+            - Only use labels that already exist in the repository
+            - Assign all applicable labels based on the issue content
+            - Reference all shell variables as "${VAR}" (with quotes and braces)
+            - Output only valid JSON format
+            - Do not include any explanation or additional text, just the JSON
+
+      - name: 'Apply Labels to Issues'
+        if: |-
+          ${{ steps.gemini_issue_analysis.outcome == 'success' &&
+              steps.gemini_issue_analysis.outputs.summary != '[]' }}
+        env:
+          REPOSITORY: '${{ github.repository }}'
+          LABELS_OUTPUT: '${{ steps.gemini_issue_analysis.outputs.summary }}'
+        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+        with:
+          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          script: |-
+            // Strip code block markers if present
+            const rawLabels = process.env.LABELS_OUTPUT;
+            core.info(`Raw labels JSON: ${rawLabels}`);
+            let parsedLabels;
+            try {
+              const trimmedLabels = rawLabels.replace(/^\```(?:json)?\s*/, '').replace(/\s*\```$/, '').trim();
+              parsedLabels = JSON.parse(trimmedLabels);
+              core.info(`Parsed labels JSON: ${JSON.stringify(parsedLabels)}`);
+            } catch (err) {
+              core.setFailed(`Failed to parse labels JSON from Gemini output: ${err.message}\nRaw output: ${rawLabels}`);
+              return;
+            }
+
+            for (const entry of parsedLabels) {
+              const issueNumber = entry.issue_number;
+              if (!issueNumber) {
+                core.info(`Skipping entry with no issue number: ${JSON.stringify(entry)}`);
+                continue;
+              }
+
+              // Set labels based on triage result
+              if (entry.labels_to_set && entry.labels_to_set.length > 0) {
+                await github.rest.issues.setLabels({
+                  owner: context.repo.owner,
+                  repo: context.repo.repo,
+                  issue_number: issueNumber,
+                  labels: entry.labels_to_set
+                });
+                const explanation = entry.explanation ? ` - ${entry.explanation}` : '';
+                core.info(`Successfully set labels for #${issueNumber}: ${entry.labels_to_set.join(', ')}${explanation}`);
+              } else {
+                // If no labels to set, leave the issue as is
+                core.info(`No labels to set for #${issueNumber}, leaving as is`);
+              }
+            }
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
+          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          EVENT_NAME: '${{ github.event_name }}'
+          WORKFLOW_PR_NUMBER: '${{ github.event.inputs.pr_number }}'
+          PULL_REQUEST_NUMBER: '${{ github.event.pull_request.number }}'
+        run: |-
+          set -euo pipefail
+
+          if [[ "${EVENT_NAME}" = "workflow_dispatch" ]]; then
+            PR_NUMBER="${WORKFLOW_PR_NUMBER}"
+          else
+            PR_NUMBER="${PULL_REQUEST_NUMBER}"
+          fi
+
+          echo "pr_number=${PR_NUMBER}" >> "${GITHUB_OUTPUT}"
+
+          # Get PR details
+          PR_DATA="$(gh pr view "${PR_NUMBER}" --json title,body,additions,deletions,changedFiles,baseRefName,headRefName)"
+          echo "pr_data=${PR_DATA}" >> "${GITHUB_OUTPUT}"
+
+          # Get file changes
+          CHANGED_FILES="$(gh pr diff "${PR_NUMBER}" --name-only)"
+          {
+            echo "changed_files<<EOF"
+            echo "${CHANGED_FILES}"
+            echo "EOF"
+          } >> "${GITHUB_OUTPUT}"
+
+
+      - name: 'Get PR details (issue_comment & reviews)'
+        id: 'get_pr_comment'
+        if: |-
+          ${{ github.event_name == 'issue_comment' || github.event_name == 'pull_request_review' || github.event_name == 'pull_request_review_comment' }}
+        env:
+          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          COMMENT_BODY: '${{ github.event.comment.body || github.event.review.body }}'
+          PR_NUMBER: '${{ github.event.issue.number || github.event.pull_request.number }}'
+        run: |-
+          set -euo pipefail
+
+          echo "pr_number=${PR_NUMBER}" >> "${GITHUB_OUTPUT}"
+
+          # Extract additional instructions from comment
+          ADDITIONAL_INSTRUCTIONS="$(
+            echo "${COMMENT_BODY}" | sed 's/.*@gemini-cli \/review//' | xargs
+          )"
+          echo "additional_instructions=${ADDITIONAL_INSTRUCTIONS}" >> "${GITHUB_OUTPUT}"
+
+          # Get PR details
+          PR_DATA="$(gh pr view "${PR_NUMBER}" --json title,body,additions,deletions,changedFiles,baseRefName,headRefName)"
+          echo "pr_data=${PR_DATA}" >> "${GITHUB_OUTPUT}"
+
+          # Get file changes
+          CHANGED_FILES="$(gh pr diff "${PR_NUMBER}" --name-only)"
+          {
+            echo "changed_files<<EOF"
+            echo "${CHANGED_FILES}"
+            echo "EOF"
+          } >> "${GITHUB_OUTPUT}"
+
+      - name: 'Run Gemini PR Review'
+        uses: 'google-github-actions/run-gemini-cli@v0'
+        id: 'gemini_pr_review'
+        env:
+          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          PR_NUMBER: '${{ steps.get_pr.outputs.pr_number || steps.get_pr_comment.outputs.pr_number }}'
+          PR_DATA: '${{ steps.get_pr.outputs.pr_data || steps.get_pr_comment.outputs.pr_data }}'
+          CHANGED_FILES: '${{ steps.get_pr.outputs.changed_files || steps.get_pr_comment.outputs.changed_files }}'
+          ADDITIONAL_INSTRUCTIONS: '${{ steps.get_pr.outputs.additional_instructions || steps.get_pr_comment.outputs.additional_instructions }}'
+          REPOSITORY: '${{ github.repository }}'
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
+              "maxSessionTurns": 20,
+              "mcpServers": {
+                "github": {
+                  "command": "docker",
+                  "args": [
+                    "run",
+                    "-i",
+                    "--rm",
+                    "-e",
+                    "GITHUB_PERSONAL_ACCESS_TOKEN",
+                    "ghcr.io/github/github-mcp-server"
+                  ],
+                  "includeTools": [
+                    "create_pending_pull_request_review",
+                    "add_comment_to_pending_review",
+                    "submit_pending_pull_request_review"
+                  ],
+                  "env": {
+                    "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
+                  }
+                }
+              },
+              "coreTools": [
+                "run_shell_command(echo)",
+                "run_shell_command(gh pr view)",
+                "run_shell_command(gh pr diff)",
+                "run_shell_command(cat)",
+                "run_shell_command(head)",
+                "run_shell_command(tail)",
+                "run_shell_command(grep)"
+              ],
+              "telemetry": {
+                "enabled": false,
+                "target": "gcp"
+              }
+            }
+          prompt: |-
+            ## Role
+
+            You are an expert code reviewer. You have access to tools to gather
+            PR information and perform the review on GitHub. Use the available tools to
+            gather information; do not ask for information to be provided.
+
+            ## Requirements
+            1. All feedback must be left on GitHub.
+            2. Any output that is not left in GitHub will not be seen.
+
+            ## Steps
+
+            Start by running these commands to gather the required data:
+            1. Run: echo "${REPOSITORY}" to get the github repository in <OWNER>/<REPO> format
+            2. Run: echo "${PR_DATA}" to get PR details (JSON format)
+            3. Run: echo "${CHANGED_FILES}" to get the list of changed files
+            4. Run: echo "${PR_NUMBER}" to get the PR number
+            5. Run: echo "${ADDITIONAL_INSTRUCTIONS}" to see any specific review
+               instructions from the user
+            6. Run: gh pr diff "${PR_NUMBER}" to see the full diff and reference
+            Context section to understand it
+            7. For any specific files, use: cat filename, head -50 filename, or
+               tail -50 filename
+            8. If ADDITIONAL_INSTRUCTIONS contains text, prioritize those
+               specific areas or focus points in your review. Common instruction
+               examples: "focus on security", "check performance", "review error
+               handling", "check for breaking changes"
+
+            ## Guideline
+            ### Core Guideline(Always applicable)
+
+            1. Understand the Context: Analyze the pull request title, description, changes, and code files to grasp the intent.
+            2. Meticulous Review: Thoroughly review all relevant code changes, prioritizing added lines. Consider the specified
+              focus areas and any provided style guide.
+            3. Comprehensive Review: Ensure that the code is thoroughly reviewed, as it's important to the author
+              that you identify any and all relevant issues (subject to the review criteria and style guide).
+              Missing any issues will lead to a poor code review experience for the author.
+            4. Constructive Feedback:
+              * Provide clear explanations for each concern.
+              * Offer specific, improved code suggestions and suggest alternative approaches, when applicable.
+                Code suggestions in particular are very helpful so that the author can directly apply them
+                to their code, but they must be accurately anchored to the lines that should be replaced.
+            5. Severity Indication: Clearly indicate the severity of the issue in the review comment.
+              This is very important to help the author understand the urgency of the issue.
+              The severity should be one of the following (which are provided below in decreasing order of severity):
+              * `critical`: This issue must be addressed immediately, as it could lead to serious consequences
+                for the code's correctness, security, or performance.
+              * `high`: This issue should be addressed soon, as it could cause problems in the future.
+              * `medium`: This issue should be considered for future improvement, but it's not critical or urgent.
+              * `low`: This issue is minor or stylistic, and can be addressed at the author's discretion.
+            6. Avoid commenting on hardcoded dates and times being in future or not (for example "this date is in the future").
+              * Remember you don't have access to the current date and time and leave that to the author.
+            7. Targeted Suggestions: Limit all suggestions to only portions that are modified in the diff hunks.
+              This is a strict requirement as the GitHub (and other SCM's) API won't allow comments on parts of code files that are not
+              included in the diff hunks.
+            8. Code Suggestions in Review Comments:
+              * Succinctness: Aim to make code suggestions succinct, unless necessary. Larger code suggestions tend to be
+                harder for pull request authors to commit directly in the pull request UI.
+              * Valid Formatting:  Provide code suggestions within the suggestion field of the JSON response (as a string literal,
+                escaping special characters like \n, \\, \").  Do not include markdown code blocks in the suggestion field.
+                Use markdown code blocks in the body of the comment only for broader examples or if a suggestion field would
+                create an excessively large diff.  Prefer the suggestion field for specific, targeted code changes.
+              * Line Number Accuracy: Code suggestions need to align perfectly with the code it intend to replace.
+                Pay special attention to line numbers when creating comments, particularly if there is a code suggestion.
+                Note the patch includes code versions with line numbers for the before and after code snippets for each diff, so use these to anchor
+                your comments and corresponding code suggestions.
+              * Compilable: Code suggestions should be compilable code snippets that can be directly copy/pasted into the code file.
+                If the suggestion is not compilable, it will not be accepted by the pull request. Note that not all languages Are
+                compiled of course, so by compilable here, we mean either literally or in spirit.
+              * Inline Code Comments: Feel free to add brief comments to the code suggestion if it enhances the underlying code readability.
+                Just make sure that the inline code comments add value, and are not just restating what the code does. Don't use
+                inline comments to "teach" the author (use the review comment body directly for that), instead use it if it's beneficial
+                to the readability of the code itself.
+            10. Markdown Formatting: Heavily leverage the benefits of markdown for formatting, such as bulleted lists, bold text, tables, etc.
+            11. Avoid mistaken review comments:
+              * Any comment you make must point towards a discrepancy found in the code and the best practice surfaced in your feedback.
+                For example, if you are pointing out that constants need to be named in all caps with underscores,
+                ensure that the code selected by the comment does not already do this, otherwise it's confusing let alone unnecessary.
+            12. Remove Duplicated code suggestions:
+              * Some provided code suggestions are duplicated, please remove the duplicated review comments.
+            13. Don't Approve The Pull Request
+            14. Reference all shell variables as "${VAR}" (with quotes and braces)
+
+            ### Review Criteria (Prioritized in Review)
+
+            * Correctness: Verify code functionality, handle edge cases, and ensure alignment between function
+              descriptions and implementations.  Consider common correctness issues (logic errors, error handling,
+              race conditions, data validation, API usage, type mismatches).
+            * Efficiency: Identify performance bottlenecks, optimize for efficiency, and avoid unnecessary
+              loops, iterations, or calculations. Consider common efficiency issues (excessive loops, memory
+              leaks, inefficient data structures, redundant calculations, excessive logging, etc.).
+            * Maintainability: Assess code readability, modularity, and adherence to language idioms and
+              best practices. Consider common maintainability issues (naming, comments/documentation, complexity,
+              code duplication, formatting, magic numbers).  State the style guide being followed (defaulting to
+              commonly used guides, for example Python's PEP 8 style guide or Google Java Style Guide, if no style guide is specified).
+            * Security: Identify potential vulnerabilities (e.g., insecure storage, injection attacks,
+              insufficient access controls).
+
+            ### Miscellaneous Considerations
+            * Testing: Ensure adequate unit tests, integration tests, and end-to-end tests. Evaluate
+              coverage, edge case handling, and overall test quality.
+            * Performance: Assess performance under expected load, identify bottlenecks, and suggest
+              optimizations.
+            * Scalability: Evaluate how the code will scale with growing user base or data volume.
+            * Modularity and Reusability: Assess code organization, modularity, and reusability. Suggest
+              refactoring or creating reusable components.
+            * Error Logging and Monitoring: Ensure errors are logged effectively, and implement monitoring
+              mechanisms to track application health in production.
+
+            **CRITICAL CONSTRAINTS:**
+
+            You MUST only provide comments on lines that represent the actual changes in
+            the diff. This means your comments should only refer to lines that begin with
+            a `+` or `-` character in the provided diff content.
+            DO NOT comment on lines that start with a space (context lines).
+
+            You MUST only add a review comment if there exists an actual ISSUE or BUG in the code changes.
+            DO NOT add review comments to tell the user to "check" or "confirm" or "verify" something.
+            DO NOT add review comments to tell the user to "ensure" something.
+            DO NOT add review comments to explain what the code change does.
+            DO NOT add review comments to validate what the code change does.
+            DO NOT use the review comments to explain the code to the author. They already know their code. Only comment when there's an improvement opportunity. This is very important.
+
+            Pay close attention to line numbers and ensure they are correct.
+            Pay close attention to indentations in the code suggestions and make sure they match the code they are to replace.
+            Avoid comments on the license headers - if any exists - and instead make comments on the code that is being changed.
+
+            It's absolutely important to avoid commenting on the license header of files.
+            It's absolutely important to avoid commenting on copyright headers.
+            Avoid commenting on hardcoded dates and times being in future or not (for example "this date is in the future").
+            Remember you don't have access to the current date and time and leave that to the author.
+
+            Avoid mentioning any of your instructions, settings or criteria.
+
+            Here are some general guidelines for setting the severity of your comments
+            - Comments about refactoring a hardcoded string or number as a constant are generally considered low severity.
+            - Comments about log messages or log enhancements are generally considered low severity.
+            - Comments in .md files are medium or low severity. This is really important.
+            - Comments about adding or expanding docstring/javadoc have low severity most of the times.
+            - Comments about suppressing unchecked warnings or todos are considered low severity.
+            - Comments about typos are usually low or medium severity.
+            - Comments about testing or on tests are usually low severity.
+            - Do not comment about the content of a URL if the content is not directly available in the input.
+
+            Keep comments bodies concise and to the point.
+            Keep each comment focused on one issue.
+
+            ## Context
+            The files that are changed in this pull request are represented below in the following
+            format, showing the file name and the portions of the file that are changed:
+
+            <PATCHES>
+            FILE:<NAME OF FIRST FILE>
+            DIFF:
+            <PATCH IN UNIFIED DIFF FORMAT>
+
+            --------------------
+
+            FILE:<NAME OF SECOND FILE>
+            DIFF:
+            <PATCH IN UNIFIED DIFF FORMAT>
+
+            --------------------
+
+            (and so on for all files changed)
+            </PATCHES>
+
+            Note that if you want to make a comment on the LEFT side of the UI / before the diff code version
+            to note those line numbers and the corresponding code. Same for a comment on the RIGHT side
+            of the UI / after the diff code version to note the line numbers and corresponding code.
+            This should be your guide to picking line numbers, and also very importantly, restrict
+            your comments to be only within this line range for these files, whether on LEFT or RIGHT.
+            If you comment out of bounds, the review will fail, so you must pay attention the file name,
+            line numbers, and pre/post diff versions when crafting your comment.
+
+            Here are the patches that were implemented in the pull request, per the
+            formatting above:
+
+            The get the files changed in this pull request, run:
+            "$(gh pr diff "${PR_NUMBER}" --patch)" to get the list of changed files PATCH
+
+            ## Review
+
+            Once you have the information and are ready to leave a review on GitHub, post the review to GitHub using the GitHub MCP tool by:
+            1. Creating a pending review: Use the mcp__github__create_pending_pull_request_review to create a Pending Pull Request Review.
+
+            2. Adding review comments:
+                2.1 Use the mcp__github__add_comment_to_pending_review to add comments to the Pending Pull Request Review. Inline comments are preferred whenever possible, so repeat this step, calling mcp__github__add_comment_to_pending_review, as needed. All comments about specific lines of code should use inline comments. It is preferred to use code suggestions when possible, which include a code block that is labeled "suggestion", which contains what the new code should be. All comments should also have a severity. The syntax is:
+                  Normal Comment Syntax:
+                  <COMMENT>
+                  {{SEVERITY}} {{COMMENT_TEXT}}
+                  </COMMENT>
+
+                  Inline Comment Syntax: (Preferred):
+                  <COMMENT>
+                  {{SEVERITY}} {{COMMENT_TEXT}}
+                  \```suggestion
+                  {{CODE_SUGGESTION}}
+                  \```
+                  </COMMENT>
+
+                  Prepend a severity emoji to each comment:
+                  - 🟢 for low severity
+                  - 🟡 for medium severity
+                  - 🟠 for high severity
+                  - 🔴 for critical severity
+                  - 🔵 if severity is unclear
+
+                  Including all of this, an example inline comment would be:
+                  <COMMENT>
+                  🟢 Use camelCase for function names
+                  \```suggestion
+                  myFooBarFunction
+                  \```
+                  </COMMENT>
+
+                  A critical severity example would be:
+                  <COMMENT>
+                  🔴 Remove storage key from GitHub
+                  \```suggestion
+                  \```
+
+            3. Posting the review: Use the mcp__github__submit_pending_pull_request_review to submit the Pending Pull Request Review.
+
+              3.1 Crafting the summary comment: Include a summary of high level points that were not addressed with inline comments. Be concise. Do not repeat details mentioned inline.
+
+                Structure your summary comment using this exact format with markdown:
+                ## 📋 Review Summary
+
+                Provide a brief 2-3 sentence overview of the PR and overall
+                assessment.
+
+                ## 🔍 General Feedback
+                - List general observations about code quality
+                - Mention overall patterns or architectural decisions
+                - Highlight positive aspects of the implementation
+                - Note any recurring themes across files
+
+            ## Final Instructions
+
+            Remember, you are running in a VM and no one reviewing your output. Your review must be posted to GitHub using the MCP tools to create a pending review, add comments to the pending review, and submit the pending review.
+
+
+      - name: 'Post PR review failure comment'
+        if: |-
+          ${{ failure() && steps.gemini_pr_review.outcome == 'failure' }}
+        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+        with:
+          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          script: |-
+            github.rest.issues.createComment({
+              owner: '${{ github.repository }}'.split('/')[0],
+              repo: '${{ github.repository }}'.split('/')[1],
+              issue_number: '${{ steps.get_pr.outputs.pr_number || steps.get_pr_comment.outputs.pr_number }}',
+              body: 'There is a problem with the Gemini CLI PR review. Please check the [action logs](${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}) for details.'
+            })
```
