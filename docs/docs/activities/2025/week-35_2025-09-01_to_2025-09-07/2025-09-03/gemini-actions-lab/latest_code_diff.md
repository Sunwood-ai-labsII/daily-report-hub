# 🔄 Latest Code Changes

```diff
diff --git a/.github/prompts/gemini-cli_prompt.ja.md b/.github/prompts/gemini-cli_prompt.ja.md
index 7b852cf..9fc49dc 100644
--- a/.github/prompts/gemini-cli_prompt.ja.md
+++ b/.github/prompts/gemini-cli_prompt.ja.md
@@ -127,3 +127,56 @@ ${USER_REQUEST}
 \```
 
 ※ すべてのコメント・PR本文は日本語で、過度にならない範囲で適切な絵文字を使用してください。
+
+## 📝 PRレポート（本文）テンプレート例
+
+以下の構成で、読みやすいレポート形式のPR本文を作成してください。
+
+タイトル例（推奨）:
+- `🔧 Fixes #${ISSUE_NUMBER}: 変更の要約`
+
+本文テンプレート:
+\```
+# 🔧 Fixes #${ISSUE_NUMBER}
+
+## 📋 AAR
+- 🎯 目的: Issue #${ISSUE_NUMBER} のリクエスト対応
+- ✅ 実施: 何をどのブランチで、どのファイルを、どう変更したか
+- 🔍 差異: 期待と実績のギャップや想定外（あれば）
+- 💡 学び: 次に活かせる知見
+- ▶️ 次のアクション: レビュー観点・確認依頼
+
+## 🔄 Changes
+- ブランチ: <branch-url>
+- 比較: <compare-url>
+- 最新コミット: <short-sha>
+- 変更ファイル:
+  - `path/to/file1`
+  - `path/to/file2`
+
+## ✅ Reviewer Checklist
+- [ ] 内容の妥当性
+- [ ] 表記ゆれ/誤字の確認
+- [ ] 追加・変更ファイルの確認
+- [ ] 必要に応じたテスト/動作確認
+
+## 📝 Details
+- 変更の背景や補足（あれば）。
+\```
+
+## 📣 Issue へのPR通知コメント例
+
+\```
+🎉 PR を作成しました: <pr-url>
+
+## 📋 AAR
+- 🎯 目的: Issue #${ISSUE_NUMBER} の対応PR作成
+- ✅ 実施: ブランチ(<branch-name>)作成・コミット/プッシュ・PR作成
+- ▶️ 次のアクション: レビューをお願いします
+
+- ブランチ: <branch-url>
+- 比較: <compare-url>
+- 最新コミット: <short-sha>
+\```
+
+> メモ: 本ワークフローでは `response.md` を `${GITHUB_WORKSPACE}/response.md` に生成し、必要に応じてPR本文の「Details」として取り込む運用を推奨します。
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index c8b04ba..979f1f2 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -256,97 +256,3 @@ jobs:
               }
             }
           prompt: ${{ steps.read_prompt.outputs.prompt }}
-
-      - name: 'Create PR from issue changes'
-        if: |-
-          ${{ steps.get_context.outputs.is_pr == 'false' }}
-        env:
-          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          ISSUE_NUMBER: '${{ steps.get_context.outputs.issue_number }}'
-          DEFAULT_BRANCH: '${{ github.event.repository.default_branch }}'
-          REPOSITORY: '${{ github.repository }}'
-          GITHUB_WORKSPACE: '${{ github.workspace }}'
-        run: |-
-          set -euo pipefail
-
-          BRANCH="issue/${ISSUE_NUMBER}/auto-pr"
-          git fetch origin --prune
-
-          # Create or switch to the working branch
-          if git show-ref --verify --quiet "refs/heads/${BRANCH}"; then
-            git checkout "${BRANCH}"
-          else
-            git checkout -b "${BRANCH}"
-          fi
-
-          # Commit local changes if present
-          if [[ -n "$(git status --porcelain)" ]]; then
-            git add -A
-            git commit -m "🔧 chore: Auto changes for Issue #${ISSUE_NUMBER}"
-          else
-            echo "No local changes to commit."
-          fi
-
-          # Push branch (create or update)
-          if git push -u origin "${BRANCH}"; then
-            echo "Pushed branch ${BRANCH}"
-          else
-            echo "Initial push failed; attempting rebase and push..."
-            git pull --rebase origin "${BRANCH}" || true
-            git push -u origin "${BRANCH}" || git push -u --force-with-lease origin "${BRANCH}"
-          fi
-
-          # Create PR if one doesn't already exist
-          PR_NUMBER=$(gh pr list --head "${BRANCH}" --state open --json number --jq '.[0].number' || true)
-          if [[ -z "${PR_NUMBER}" ]]; then
-            if [[ -f "${GITHUB_WORKSPACE}/response.md" ]]; then
-              gh pr create \
-                --head "${BRANCH}" \
-                --base "${DEFAULT_BRANCH:-main}" \
-                --title "🔧 Fixes #${ISSUE_NUMBER}: Apply requested changes" \
-                --body-file "${GITHUB_WORKSPACE}/response.md"
-            else
-              PR_BODY_FILE=$(mktemp)
-              cat > "${PR_BODY_FILE}" <<EOF
-              ## 📋 AAR
-              - 🎯 目的: Issue #${ISSUE_NUMBER} のリクエストへの対応PRを作成
-              - ✅ 実施: ブランチ作成・変更のコミット/プッシュ・PR作成を自動実行
-              - 🔍 差異: 特になし（自動化フローで標準対応）
-              - 💡 学び: 自動PRフローの確認と安定動作
-              - ▶️ 次のアクション: レビューとマージのご確認をお願いします
-
-              関連: #${ISSUE_NUMBER}
-              EOF
-              gh pr create \
-                --head "${BRANCH}" \
-                --base "${DEFAULT_BRANCH:-main}" \
-                --title "🔧 Fixes #${ISSUE_NUMBER}: Apply requested changes" \
-                --body-file "${PR_BODY_FILE}"
-            fi
-            # Capture PR URL
-            PR_URL=$(gh pr view --json url --jq .url)
-            echo "Created PR: ${PR_URL}"
-            AAR_COMMENT_FILE=$(mktemp)
-            cat > "${AAR_COMMENT_FILE}" <<EOF
-            🎉 PR を作成しました: ${PR_URL}
-
-            ## 📋 AAR
-            - 🎯 目的: Issue #${ISSUE_NUMBER} の対応PR作成
-            - ✅ 実施: ブランチ(${BRANCH})作成・コミット/プッシュ・PR作成
-            - ▶️ 次のアクション: レビューをお願いします
-            EOF
-            gh issue comment "${ISSUE_NUMBER}" --repo "${REPOSITORY}" --body-file "${AAR_COMMENT_FILE}"
-          else
-            echo "PR already exists: #${PR_NUMBER}"
-            PR_URL=$(gh pr view "${PR_NUMBER}" --json url --jq .url)
-            AAR_COMMENT_FILE=$(mktemp)
-            cat > "${AAR_COMMENT_FILE}" <<EOF
-            ℹ️ 既存のPRがあります: ${PR_URL}
-
-            ## 📋 AAR
-            - 🎯 目的: Issue #${ISSUE_NUMBER} の対応PR確認
-            - ✅ 実施: 既存PR (#${PR_NUMBER}) を確認し、リンクを共有
-            - ▶️ 次のアクション: レビューをお願いします
-            EOF
-            gh issue comment "${ISSUE_NUMBER}" --repo "${REPOSITORY}" --body-file "${AAR_COMMENT_FILE}"
-          fi
```
