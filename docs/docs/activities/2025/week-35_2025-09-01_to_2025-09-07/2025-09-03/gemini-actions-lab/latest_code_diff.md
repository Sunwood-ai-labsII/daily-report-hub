# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 1c076d0..c8b04ba 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -308,15 +308,15 @@ jobs:
             else
               PR_BODY_FILE=$(mktemp)
               cat > "${PR_BODY_FILE}" <<EOF
-            ## 📋 AAR
-            - 🎯 目的: Issue #${ISSUE_NUMBER} のリクエストへの対応PRを作成
-            - ✅ 実施: ブランチ作成・変更のコミット/プッシュ・PR作成を自動実行
-            - 🔍 差異: 特になし（自動化フローで標準対応）
-            - 💡 学び: 自動PRフローの確認と安定動作
-            - ▶️ 次のアクション: レビューとマージのご確認をお願いします
+              ## 📋 AAR
+              - 🎯 目的: Issue #${ISSUE_NUMBER} のリクエストへの対応PRを作成
+              - ✅ 実施: ブランチ作成・変更のコミット/プッシュ・PR作成を自動実行
+              - 🔍 差異: 特になし（自動化フローで標準対応）
+              - 💡 学び: 自動PRフローの確認と安定動作
+              - ▶️ 次のアクション: レビューとマージのご確認をお願いします
 
-            関連: #${ISSUE_NUMBER}
-EOF
+              関連: #${ISSUE_NUMBER}
+              EOF
               gh pr create \
                 --head "${BRANCH}" \
                 --base "${DEFAULT_BRANCH:-main}" \
@@ -334,7 +334,7 @@ EOF
             - 🎯 目的: Issue #${ISSUE_NUMBER} の対応PR作成
             - ✅ 実施: ブランチ(${BRANCH})作成・コミット/プッシュ・PR作成
             - ▶️ 次のアクション: レビューをお願いします
-EOF
+            EOF
             gh issue comment "${ISSUE_NUMBER}" --repo "${REPOSITORY}" --body-file "${AAR_COMMENT_FILE}"
           else
             echo "PR already exists: #${PR_NUMBER}"
@@ -347,6 +347,6 @@ EOF
             - 🎯 目的: Issue #${ISSUE_NUMBER} の対応PR確認
             - ✅ 実施: 既存PR (#${PR_NUMBER}) を確認し、リンクを共有
             - ▶️ 次のアクション: レビューをお願いします
-EOF
+            EOF
             gh issue comment "${ISSUE_NUMBER}" --repo "${REPOSITORY}" --body-file "${AAR_COMMENT_FILE}"
           fi
```
