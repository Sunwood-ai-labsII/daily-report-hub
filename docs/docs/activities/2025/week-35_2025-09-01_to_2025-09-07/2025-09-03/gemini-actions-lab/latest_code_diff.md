# 🔄 Latest Code Changes

```diff
diff --git a/.github/prompts/gemini-cli_prompt.ja.md b/.github/prompts/gemini-cli_prompt.ja.md
index f21b4e8..7b852cf 100644
--- a/.github/prompts/gemini-cli_prompt.ja.md
+++ b/.github/prompts/gemini-cli_prompt.ja.md
@@ -91,3 +91,39 @@ ${USER_REQUEST}
     - 🔒 security: セキュリティ
   - コミット例: `feat: ✨ CLI に --dry-run を追加`
   - PRタイトル例: `📝 ドキュメント: README にセットアップ手順を追記`
+
+## 🧭 進捗・PRのレポート方針（AAR + 絵文字）
+
+- 進捗コメントや PR の本文は、読みやすいマークダウンと絵文字を用い、AAR（After Action Review）形式で記載してください。
+- AAR 構成:
+  - 🎯 目的: 何を達成するための作業か
+  - ✅ 実施: 実際に行ったこと（具体的なコマンド/変更内容）
+  - 🔍 差異: 期待と実績のギャップ、想定外事項
+  - 💡 学び: 得られた知見、次に活かす点
+  - ▶️ 次のアクション: レビュー/追作業/検証などの依頼
+
+### 進捗コメントの例
+
+\```
+## 📋 AAR 進捗報告
+- 🎯 目的: Issue #${ISSUE_NUMBER} の簡易HTML作成
+- ✅ 実施: `example/index.html` を作成し、チェックリストを更新
+- 🔍 差異: とくになし
+- 💡 学び: 相対パスではなく絶対パスでの `write_file` が必要
+- ▶️ 次のアクション: 内容レビューのお願い
+\```
+
+### PR本文の例（response.md 生成時）
+
+\```
+## 📋 AAR
+- 🎯 目的: Issue #${ISSUE_NUMBER} への対応PR
+- ✅ 実施: ブランチ作成・変更のコミット/プッシュ・PR作成
+- 🔍 差異: 競合はなし（あれば解決内容を記載）
+- 💡 学び: 自動PRフローの安定動作を確認
+- ▶️ 次のアクション: レビューとマージのご確認をお願いします
+
+関連: #${ISSUE_NUMBER}
+\```
+
+※ すべてのコメント・PR本文は日本語で、過度にならない範囲で適切な絵文字を使用してください。
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 63ee7a8..1c076d0 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -306,18 +306,47 @@ jobs:
                 --title "🔧 Fixes #${ISSUE_NUMBER}: Apply requested changes" \
                 --body-file "${GITHUB_WORKSPACE}/response.md"
             else
+              PR_BODY_FILE=$(mktemp)
+              cat > "${PR_BODY_FILE}" <<EOF
+            ## 📋 AAR
+            - 🎯 目的: Issue #${ISSUE_NUMBER} のリクエストへの対応PRを作成
+            - ✅ 実施: ブランチ作成・変更のコミット/プッシュ・PR作成を自動実行
+            - 🔍 差異: 特になし（自動化フローで標準対応）
+            - 💡 学び: 自動PRフローの確認と安定動作
+            - ▶️ 次のアクション: レビューとマージのご確認をお願いします
+
+            関連: #${ISSUE_NUMBER}
+EOF
               gh pr create \
                 --head "${BRANCH}" \
                 --base "${DEFAULT_BRANCH:-main}" \
                 --title "🔧 Fixes #${ISSUE_NUMBER}: Apply requested changes" \
-                --body "✨ This PR addresses Issue #${ISSUE_NUMBER}."
+                --body-file "${PR_BODY_FILE}"
             fi
             # Capture PR URL
             PR_URL=$(gh pr view --json url --jq .url)
             echo "Created PR: ${PR_URL}"
-            gh issue comment "${ISSUE_NUMBER}" --repo "${REPOSITORY}" --body "Created PR: ${PR_URL}"
+            AAR_COMMENT_FILE=$(mktemp)
+            cat > "${AAR_COMMENT_FILE}" <<EOF
+            🎉 PR を作成しました: ${PR_URL}
+
+            ## 📋 AAR
+            - 🎯 目的: Issue #${ISSUE_NUMBER} の対応PR作成
+            - ✅ 実施: ブランチ(${BRANCH})作成・コミット/プッシュ・PR作成
+            - ▶️ 次のアクション: レビューをお願いします
+EOF
+            gh issue comment "${ISSUE_NUMBER}" --repo "${REPOSITORY}" --body-file "${AAR_COMMENT_FILE}"
           else
             echo "PR already exists: #${PR_NUMBER}"
             PR_URL=$(gh pr view "${PR_NUMBER}" --json url --jq .url)
-            gh issue comment "${ISSUE_NUMBER}" --repo "${REPOSITORY}" --body "PR already exists: ${PR_URL}"
+            AAR_COMMENT_FILE=$(mktemp)
+            cat > "${AAR_COMMENT_FILE}" <<EOF
+            ℹ️ 既存のPRがあります: ${PR_URL}
+
+            ## 📋 AAR
+            - 🎯 目的: Issue #${ISSUE_NUMBER} の対応PR確認
+            - ✅ 実施: 既存PR (#${PR_NUMBER}) を確認し、リンクを共有
+            - ▶️ 次のアクション: レビューをお願いします
+EOF
+            gh issue comment "${ISSUE_NUMBER}" --repo "${REPOSITORY}" --body-file "${AAR_COMMENT_FILE}"
           fi
```
