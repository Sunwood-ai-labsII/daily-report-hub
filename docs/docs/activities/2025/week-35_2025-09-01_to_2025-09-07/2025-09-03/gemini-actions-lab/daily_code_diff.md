# 💻 Daily Code Changes

## Full Diff

```diff
diff --git a/.github/prompts/gemini-cli_prompt.ja.md b/.github/prompts/gemini-cli_prompt.ja.md
index c21bd48..f21b4e8 100644
--- a/.github/prompts/gemini-cli_prompt.ja.md
+++ b/.github/prompts/gemini-cli_prompt.ja.md
@@ -48,18 +48,27 @@ ${USER_REQUEST}
      - main へ直接コミットしない
      - PR 上の作業: そのまま `git add` → `git commit` → `git push`
      - Issue ベースの作業: `git checkout -b issue/${ISSUE_NUMBER}/<slug>` で作業ブランチを作成し push、必要に応じて PR を作成
-   - 変更点の要約を `response.md` にまとめ、コメントとして投稿します。
+   - 変更点の要約を `response.md` にまとめます。
+     - 重要: write_file ツールは絶対パスが必要です。`${GITHUB_WORKSPACE}/response.md` を使ってください。
+       例: `write_file("${GITHUB_WORKSPACE}/response.md", "<ここにあなたの応答>")`
+     - コメント投稿時も絶対パスを使用します。
+       - PR: `gh pr comment "${ISSUE_NUMBER}" --body-file "${GITHUB_WORKSPACE}/response.md"`
+       - Issue: `gh issue comment "${ISSUE_NUMBER}" --body-file "${GITHUB_WORKSPACE}/response.md"`
 
 2. PR へのコメント対応
    - コメントの意図と PR の差分・議論を把握します（`gh pr view`/`gh pr diff`）。
    - 変更や説明が求められる場合はシナリオ1と同様に計画→実装→検証→コミットを行います。
    - 質問であれば簡潔かつ根拠を示して回答します。
    - 回答や変更内容は `response.md` に記録し、PR コメントとして投稿します。
+     - `write_file("${GITHUB_WORKSPACE}/response.md", "<本文>")`
+     - `gh pr comment "${ISSUE_NUMBER}" --body-file "${GITHUB_WORKSPACE}/response.md"`
 
 3. Issue の質問への回答
    - Issue 全体の文脈を読み、必要に応じてコードを確認して正確に回答します。
    - コードやドキュメントの変更が必要なら、シナリオ1に従いブランチを切って対応します。
    - 回答は簡潔・具体的にまとめ、`response.md` としてコメント投稿します。
+     - `write_file("${GITHUB_WORKSPACE}/response.md", "<本文>")`
+     - `gh issue comment "${ISSUE_NUMBER}" --body-file "${GITHUB_WORKSPACE}/response.md"`
 
 ## ✅ ガイドライン
 
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index c6f115f..63ee7a8 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -115,8 +115,11 @@ jobs:
           # Clean up user request
           USER_REQUEST=$(echo "${USER_REQUEST}" | sed 's/.*@gemini-cli//' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
 
+          # Write outputs safely (supporting newlines/special chars)
           {
-            echo "user_request=${USER_REQUEST}"
+            echo 'user_request<<EOF'
+            echo "${USER_REQUEST}"
+            echo 'EOF'
             echo "issue_number=${ISSUE_NUMBER}"
             echo "is_pr=${IS_PR}"
           } >> "${GITHUB_OUTPUT}"
@@ -209,6 +212,7 @@ jobs:
           DESCRIPTION: '${{ steps.get_description.outputs.description }}'
           COMMENTS: '${{ steps.get_comments.outputs.comments }}'
           USER_REQUEST: '${{ steps.get_context.outputs.user_request }}'
+          GITHUB_WORKSPACE: '${{ github.workspace }}'
         run: |-
           set -euo pipefail
           TEMPLATE_PATH=".github/prompts/gemini-cli_prompt.ja.md"
@@ -216,16 +220,9 @@ jobs:
             echo "Prompt template not found: ${TEMPLATE_PATH}" >&2
             exit 1
           fi
-          # Safe variable substitution without executing content
-          EXPANDED=$(sed \
-            -e "s|\\$\\{REPOSITORY\\}|${REPOSITORY}|g" \
-            -e "s|\\$\\{EVENT_NAME\\}|${EVENT_NAME}|g" \
-            -e "s|\\$\\{ISSUE_NUMBER\\}|${ISSUE_NUMBER}|g" \
-            -e "s|\\$\\{IS_PR\\}|${IS_PR}|g" \
-            -e "s|\\$\\{DESCRIPTION\\}|${DESCRIPTION}|g" \
-            -e "s|\\$\\{COMMENTS\\}|${COMMENTS}|g" \
-            -e "s|\\$\\{USER_REQUEST\\}|${USER_REQUEST}|g" \
-            "${TEMPLATE_PATH}")
+          # Robust variable substitution using envsubst (handles braces/newlines safely)
+          # Limit substitution to specific variables to avoid accidental replacements
+          EXPANDED=$(envsubst '${REPOSITORY} ${EVENT_NAME} ${ISSUE_NUMBER} ${IS_PR} ${DESCRIPTION} ${COMMENTS} ${USER_REQUEST} ${GITHUB_WORKSPACE}' < "${TEMPLATE_PATH}")
           {
             echo "prompt<<EOF"
             echo "${EXPANDED}"
@@ -259,3 +256,68 @@ jobs:
               }
             }
           prompt: ${{ steps.read_prompt.outputs.prompt }}
+
+      - name: 'Create PR from issue changes'
+        if: |-
+          ${{ steps.get_context.outputs.is_pr == 'false' }}
+        env:
+          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          ISSUE_NUMBER: '${{ steps.get_context.outputs.issue_number }}'
+          DEFAULT_BRANCH: '${{ github.event.repository.default_branch }}'
+          REPOSITORY: '${{ github.repository }}'
+          GITHUB_WORKSPACE: '${{ github.workspace }}'
+        run: |-
+          set -euo pipefail
+
+          BRANCH="issue/${ISSUE_NUMBER}/auto-pr"
+          git fetch origin --prune
+
+          # Create or switch to the working branch
+          if git show-ref --verify --quiet "refs/heads/${BRANCH}"; then
+            git checkout "${BRANCH}"
+          else
+            git checkout -b "${BRANCH}"
+          fi
+
+          # Commit local changes if present
+          if [[ -n "$(git status --porcelain)" ]]; then
+            git add -A
+            git commit -m "🔧 chore: Auto changes for Issue #${ISSUE_NUMBER}"
+          else
+            echo "No local changes to commit."
+          fi
+
+          # Push branch (create or update)
+          if git push -u origin "${BRANCH}"; then
+            echo "Pushed branch ${BRANCH}"
+          else
+            echo "Initial push failed; attempting rebase and push..."
+            git pull --rebase origin "${BRANCH}" || true
+            git push -u origin "${BRANCH}" || git push -u --force-with-lease origin "${BRANCH}"
+          fi
+
+          # Create PR if one doesn't already exist
+          PR_NUMBER=$(gh pr list --head "${BRANCH}" --state open --json number --jq '.[0].number' || true)
+          if [[ -z "${PR_NUMBER}" ]]; then
+            if [[ -f "${GITHUB_WORKSPACE}/response.md" ]]; then
+              gh pr create \
+                --head "${BRANCH}" \
+                --base "${DEFAULT_BRANCH:-main}" \
+                --title "🔧 Fixes #${ISSUE_NUMBER}: Apply requested changes" \
+                --body-file "${GITHUB_WORKSPACE}/response.md"
+            else
+              gh pr create \
+                --head "${BRANCH}" \
+                --base "${DEFAULT_BRANCH:-main}" \
+                --title "🔧 Fixes #${ISSUE_NUMBER}: Apply requested changes" \
+                --body "✨ This PR addresses Issue #${ISSUE_NUMBER}."
+            fi
+            # Capture PR URL
+            PR_URL=$(gh pr view --json url --jq .url)
+            echo "Created PR: ${PR_URL}"
+            gh issue comment "${ISSUE_NUMBER}" --repo "${REPOSITORY}" --body "Created PR: ${PR_URL}"
+          else
+            echo "PR already exists: #${PR_NUMBER}"
+            PR_URL=$(gh pr view "${PR_NUMBER}" --json url --jq .url)
+            gh issue comment "${ISSUE_NUMBER}" --repo "${REPOSITORY}" --body "PR already exists: ${PR_URL}"
+          fi
```
