# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 63671e6..18c798c 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -76,7 +76,7 @@ jobs:
       github.event_name == 'issues' && github.event.action == 'opened' &&
       contains(github.event.issue.body, '@gemini-cli')
 
-    timeout-minutes: 10
+          timeout-minutes: 10
     runs-on: 'ubuntu-latest'
     steps:
       - name: 'Debug Event Information'
@@ -129,8 +129,8 @@ jobs:
           # Clean up user request
           CLEANED_USER_REQUEST=$(echo "${USER_REQUEST}" | sed 's/.*@gemini-cli//' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
           
-          # ⬇⬇⬇ ここを修正 ⬇⬇⬇
-          # GITHUB_OUTPUTへの書き込みをヒアドキュメント形式に変更
+          # ⬇⬇⬇ ここからが修正箇所 ⬇⬇⬇
+          # GITHUB_OUTPUTへの書き込みをヒアドキュメント形式に変更して、特殊文字によるエラーを回避
           {
             echo 'user_request<<EOF'
             echo "${CLEANED_USER_REQUEST}"
@@ -138,6 +138,7 @@ jobs:
             echo "issue_number=${ISSUE_NUMBER}"
             echo "is_pr=${IS_PR}"
           } >> "${GITHUB_OUTPUT}"
+          # ⬆⬆⬆ ここまでが修正箇所 ⬆⬆⬆
 
       - name: 'Set up git user for commits'
         run: |-
diff --git a/README.md b/README.md
index a4c7124..bed190c 100644
--- a/README.md
+++ b/README.md
@@ -167,35 +167,21 @@ graph TD
 
 ---
 
-## 📝 ライセンス
 
-このプロジェクトは、[LICENSE](LICENSE)ファイルの条件に基づいてライセンスされています。
 
----
+## 🤖 Discord Issue Bot
 
-© 2025 Sunwood-ai-labsII
+Discord から直接 GitHub Issue を作成する最小ボットの詳細なドキュメントは、以下を参照してください。
 
+- ドキュメント: [discord-issue-bot/README.md](discord-issue-bot/README.md)
 
----
+## 📝 ライセンス
+
+このプロジェクトは、[LICENSE](LICENSE)ファイルの条件に基づいてライセンスされています。
 
-## 🤖 Discord Issue Bot（ワークフロー不要・最小構成）
+---
 
-- 直に GitHub REST API で Issue を作成する最小ボットです。
-- 必要な環境変数は 2 つのみ: `DISCORD_BOT_TOKEN`, `GITHUB_TOKEN`。
+© 2025 Sunwood-ai-labsII
 
-使い方:
-\```
-export DISCORD_BOT_TOKEN=xxxx
-export GITHUB_TOKEN=ghp_xxx
-cd discord-issue-bot
-docker compose -f compose.yaml up -d --build
-\```
 
-Discord で投稿（例）:
-\```
-!issue owner/repo "バグ: 保存できない" 再現手順… #kind/bug +maki
-\```
-ルール:
-- 先頭 `!issue`、直後に `owner/repo` を含める
-- タイトルは "ダブルクオート" で囲む（未指定時は1行目をタイトル）
-- `#label` がラベル、`+user` がアサイン
+---
\ No newline at end of file
diff --git a/memo.md b/memo.md
new file mode 100644
index 0000000..4d041c1
--- /dev/null
+++ b/memo.md
@@ -0,0 +1,8 @@
+!issue Sunwood-ai-labsII/gemini-actions-lab
+
+サンプルアプリの作成
+
+@gemini-cli exampleフォルダにTODOアプリを作成して
+
+#example #demo
+
```
