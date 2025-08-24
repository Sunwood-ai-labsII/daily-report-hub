# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-jp-cli.yml b/.github/workflows/gemini-jp-cli.yml
index fc52afb..aa80b79 100644
--- a/.github/workflows/gemini-jp-cli.yml
+++ b/.github/workflows/gemini-jp-cli.yml
@@ -31,14 +31,11 @@ permissions:
 
 jobs:
   gemini-cli-jp:
-    # この条件は信頼できるユーザーによってアクションがトリガーされた場合のみ実行されるようにします。
-    # プライベートリポジトリの場合、リポジトリにアクセスできるユーザーは信頼できるとみなされます。
-    # パブリックリポジトリの場合、メンバー、オーナー、またはコラボレーターが信頼できるとみなされます。
     if: |-
       github.event_name == 'workflow_dispatch' ||
       (
         github.event_name == 'issues' && github.event.action == 'opened' &&
-        contains(github.event.issue.body, '@gemini-jp-cli') &&
+        (contains(github.event.issue.body, '@gemini-jp-cli') || contains(github.event.issue.body, '@gemini-cli-jp')) &&
         !contains(github.event.issue.body, '@gemini-jp-cli /review') &&
         !contains(github.event.issue.body, '@gemini-jp-cli /triage') &&
         (
@@ -51,7 +48,7 @@ jobs:
           github.event_name == 'issue_comment' ||
           github.event_name == 'pull_request_review_comment'
         ) &&
-        contains(github.event.comment.body, '@gemini-jp-cli') &&
+        (contains(github.event.comment.body, '@gemini-jp-cli') || contains(github.event.comment.body, '@gemini-cli-jp')) &&
         !contains(github.event.comment.body, '@gemini-jp-cli /review') &&
         !contains(github.event.comment.body, '@gemini-jp-cli /triage') &&
         (
@@ -61,7 +58,7 @@ jobs:
       ) ||
       (
         github.event_name == 'pull_request_review' &&
-        contains(github.event.review.body, '@gemini-jp-cli') &&
+        (contains(github.event.review.body, '@gemini-jp-cli') || contains(github.event.review.body, '@gemini-cli-jp')) &&
         !contains(github.event.review.body, '@gemini-jp-cli /review') &&
         !contains(github.event.review.body, '@gemini-jp-cli /triage') &&
         (
@@ -128,91 +125,43 @@ jobs:
 
             try {
               if (context.eventName === 'issues') {
-                console.log('処理中: Issues イベント');
                 rawBody = context.payload.issue.body || '';
-                userRequest = rawBody;
-                issueNumber = context.payload.issue.number.toString();
-                issueTitle = context.payload.issue.title || '';
-                console.log(`Issue #${issueNumber}: "${issueTitle}"`);
-                console.log(`Issue Body 長さ: ${rawBody.length}`);
-                console.log(`Issue Body (最初の200文字): "${rawBody.substring(0, 200)}${rawBody.length > 200 ? '...' : ''}"`);
-                
               } else if (context.eventName === 'issue_comment') {
-                console.log('処理中: Issue Comment イベント');
                 rawBody = context.payload.comment.body || '';
-                userRequest = rawBody;
+              } else if (context.eventName === 'pull_request_review') {
+                rawBody = context.payload.review.body || '';
+              } else if (context.eventName === 'pull_request_review_comment') {
+                rawBody = context.payload.comment.body || '';
+              }
+
+              if (context.eventName === 'issues' || context.eventName === 'issue_comment') {
                 issueNumber = context.payload.issue.number.toString();
                 issueTitle = context.payload.issue.title || '';
-                console.log(`Comment on Issue #${issueNumber}: "${issueTitle}"`);
-                console.log(`Comment Body 長さ: ${rawBody.length}`);
-                console.log(`Comment Body (最初の200文字): "${rawBody.substring(0, 200)}${rawBody.length > 200 ? '...' : ''}"`);
-                
                 if (context.payload.issue.pull_request) {
                   isPR = true;
-                  console.log('これはPRのコメントです');
                 }
-                
-              } else if (context.eventName === 'pull_request_review') {
-                console.log('処理中: PR Review イベント');
-                rawBody = context.payload.review.body || '';
-                userRequest = rawBody;
-                issueNumber = context.payload.pull_request.number.toString();
-                issueTitle = context.payload.pull_request.title || '';
-                isPR = true;
-                console.log(`Review on PR #${issueNumber}: "${issueTitle}"`);
-                console.log(`Review Body 長さ: ${rawBody.length}`);
-                console.log(`Review Body (最初の200文字): "${rawBody.substring(0, 200)}${rawBody.length > 200 ? '...' : ''}"`);
-                
-              } else if (context.eventName === 'pull_request_review_comment') {
-                console.log('処理中: PR Review Comment イベント');
-                rawBody = context.payload.comment.body || '';
-                userRequest = rawBody;
+              } else if (context.eventName === 'pull_request_review' || context.eventName === 'pull_request_review_comment') {
                 issueNumber = context.payload.pull_request.number.toString();
                 issueTitle = context.payload.pull_request.title || '';
                 isPR = true;
-                console.log(`PR Comment on PR #${issueNumber}: "${issueTitle}"`);
-                console.log(`PR Comment Body 長さ: ${rawBody.length}`);
-                console.log(`PR Comment Body (最初の200文字): "${rawBody.substring(0, 200)}${rawBody.length > 200 ? '...' : ''}"`);
               }
 
-              console.log('=== 処理前の値 ===');
-              console.log(`Raw Body: "${rawBody}"`);
-              console.log(`User Request (処理前): "${userRequest}"`);
-              console.log(`Issue Number: "${issueNumber}"`);
-              console.log(`Issue Title: "${issueTitle}"`);
-              console.log(`Is PR: ${isPR}`);
+              userRequest = rawBody;
 
-              // @gemini-jp-cli を含んでいるかチェック
-              if (userRequest.includes('@gemini-jp-cli')) {
-                console.log('@gemini-jp-cli が見つかりました');
-                // ユーザーリクエストをクリーンアップ
-                const mentionIndex = userRequest.indexOf('@gemini-jp-cli');
-                userRequest = userRequest.substring(mentionIndex + '@gemini-jp-cli'.length).trim();
-                console.log(`クリーンアップ後: "${userRequest}"`);
+              // @gemini-jp-cli or @gemini-cli-jp を探して削除
+              const mentionJpCli = '@gemini-jp-cli';
+              const mentionCliJp = '@gemini-cli-jp';
+              
+              let mentionIndex = userRequest.indexOf(mentionJpCli);
+              if (mentionIndex !== -1) {
+                userRequest = userRequest.substring(mentionIndex + mentionJpCli.length).trim();
               } else {
-                console.log('警告: @gemini-jp-cli が見つかりません');
-                // メンションなしでも処理を続行（デバッグ目的）
-                console.log('デバッグモード: メンションなしでも処理を続行');
-              }
-
-              // 空文字チェック
-              if (!userRequest) {
-                console.log('警告: USER_REQUEST が空です');
-                userRequest = rawBody ? `元の内容: ${rawBody}` : '内容が空です - デバッグが必要';
-              }
-
-              if (!issueNumber || issueNumber === '0') {
-                console.error('エラー: ISSUE_NUMBER が空です');
-                issueNumber = '0';
+                mentionIndex = userRequest.indexOf(mentionCliJp);
+                if (mentionIndex !== -1) {
+                  userRequest = userRequest.substring(mentionIndex + mentionCliJp.length).trim();
+                }
               }
-
-              console.log('=== 最終的な出力値 ===');
-              console.log(`Final User Request: "${userRequest}"`);
-              console.log(`Final Issue Number: "${issueNumber}"`);
-              console.log(`Final Issue Title: "${issueTitle}"`);
-              console.log(`Final Is PR: ${isPR}`);
-
-              // 後続のステップで使用するために出力
+              
               core.setOutput('user_request', userRequest);
               core.setOutput('issue_number', issueNumber);
               core.setOutput('issue_title', issueTitle);
@@ -220,27 +169,28 @@ jobs:
               core.setOutput('raw_body', rawBody);
 
             } catch (error) {
-              console.error('コンテキスト取得中にエラーが発生:', error.message);
-              console.error('スタックトレース:', error.stack);
-              
-              // エラー時のフォールバック値を設定
+              core.setFailed(`コンテキスト取得中にエラーが発生: ${error.message}`);
               core.setOutput('user_request', 'エラーが発生しました');
               core.setOutput('issue_number', '0');
               core.setOutput('issue_title', 'エラー');
               core.setOutput('is_pr', 'false');
               core.setOutput('raw_body', '');
-              
-              throw error;
             }
 
       - name: '🐛 デバッグ: 取得したコンテキストを確認'
-        run: |-
+        env:
+          USER_REQUEST: ${{ steps.get_context.outputs.user_request }}
+          ISSUE_NUMBER: ${{ steps.get_context.outputs.issue_number }}
+          ISSUE_TITLE: ${{ steps.get_context.outputs.issue_title }}
+          IS_PR: ${{ steps.get_context.outputs.is_pr }}
+          RAW_BODY: ${{ steps.get_context.outputs.raw_body }}
+        run: |
           echo "=== 取得されたコンテキスト ==="
-          echo "User Request: '${{ steps.get_context.outputs.user_request }}'"
-          echo "Issue Number: '${{ steps.get_context.outputs.issue_number }}'"
-          echo "Issue Title: '${{ steps.get_context.outputs.issue_title }}'"
-          echo "Is PR: '${{ steps.get_context.outputs.is_pr }}'"
-          echo "Raw Body: '${{ steps.get_context.outputs.raw_body }}'"
+          echo "User Request: '$USER_REQUEST'"
+          echo "Issue Number: '$ISSUE_NUMBER'"
+          echo "Issue Title: '$ISSUE_TITLE'"
+          echo "Is PR: '$IS_PR'"
+          echo "Raw Body: '$RAW_BODY'"
 
       - name: 'コミット用のgitユーザーを設定'
         run: |-
@@ -250,7 +200,7 @@ jobs:
       - name: 'PRブランチをチェックアウト'
         if: |-
           ${{  steps.get_context.outputs.is_pr == 'true' }}
-        uses: 'actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683' # ratchet:actions/checkout@v4
+        uses: 'actions/checkout@v4'
         with:
           token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           repository: '${{ github.repository }}'
@@ -260,7 +210,7 @@ jobs:
       - name: 'メインブランチをチェックアウト'
         if: |-
           ${{  steps.get_context.outputs.is_pr == 'false' }}
-        uses: 'actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683' # ratchet:actions/checkout@v4
+        uses: 'actions/checkout@v4'
         with:
           token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           repository: '${{ github.repository }}'
@@ -272,16 +222,17 @@ jobs:
           GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           ISSUE_NUMBER: '${{ steps.get_context.outputs.issue_number }}'
           REPOSITORY: '${{ github.repository }}'
-          REQUEST_TYPE: '${{ steps.get_context.outputs.request_type }}'
+          USER_REQUEST: '${{ steps.get_context.outputs.user_request }}'
+          RAW_BODY: '${{ steps.get_context.outputs.raw_body }}'
         run: |-
           set -euo pipefail
           MESSAGE="@${GITHUB_ACTOR} リクエストを受け取りました。今から作業を開始します！ 🤖
 
           デバッグ情報:
-          - ユーザーリクエスト: '${{ steps.get_context.outputs.user_request }}'
+          - ユーザーリクエスト: '${USER_REQUEST}'
           - Issue/PR番号: ${ISSUE_NUMBER}
           - イベント種類: ${{ github.event_name }}
-          - 生データ: '${{ steps.get_context.outputs.raw_body }}'"
+          - 生データ: '${RAW_BODY}'"
           
           if [[ -n "${MESSAGE}" ]]; then
             if [[ "${{ steps.get_context.outputs.is_pr }}" == "true" ]]; then
@@ -297,102 +248,64 @@ jobs:
 
       - name: '説明を取得'
         id: 'get_description'
-        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+        uses: 'actions/github-script@v7'
         with:
           github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           script: |-
-            console.log('=== 説明取得開始 ===');
             const isPR = '${{ steps.get_context.outputs.is_pr }}' === 'true';
             const issueNumber = parseInt('${{ steps.get_context.outputs.issue_number }}');
-            
-            console.log(`Is PR: ${isPR}`);
-            console.log(`Issue Number: ${issueNumber}`);
-            
             let description = '';
-            
             try {
               if (isPR) {
-                console.log('PR情報を取得中...');
                 const { data: pr } = await github.rest.pulls.get({
-                  owner: context.repo.owner,
-                  repo: context.repo.repo,
-                  pull_number: issueNumber
+                  owner: context.repo.owner, repo: context.repo.repo, pull_number: issueNumber
                 });
                 description = pr.body || '';
-                console.log(`PR title: "${pr.title}"`);
               } else {
-                console.log('Issue情報を取得中...');
                 const { data: issue } = await github.rest.issues.get({
-                  owner: context.repo.owner,
-                  repo: context.repo.repo,
-                  issue_number: issueNumber
+                  owner: context.repo.owner, repo: context.repo.repo, issue_number: issueNumber
                 });
                 description = issue.body || '';
-                console.log(`Issue title: "${issue.title}"`);
               }
-              
-              console.log(`取得した説明の長さ: ${description.length}`);
-              console.log(`取得した説明 (最初の200文字): "${description.substring(0, 200)}${description.length > 200 ? '...' : ''}"`);
-              
-              core.setOutput('description', description);
-              
             } catch (error) {
-              console.error(`${isPR ? 'PR' : 'Issue'}情報の取得に失敗:`, error.message);
               description = `${isPR ? 'PR' : 'Issue'}情報の取得に失敗: ${error.message}`;
-              core.setOutput('description', description);
             }
+            core.setOutput('description', description);
 
       - name: 'コメントを取得'
         id: 'get_comments'
-        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+        uses: 'actions/github-script@v7'
         with:
           github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           script: |-
-            console.log('=== コメント取得開始 ===');
-            const isPR = '${{ steps.get_context.outputs.is_pr }}' === 'true';
             const issueNumber = parseInt('${{ steps.get_context.outputs.issue_number }}');
-            
             let comments = '';
-            
             try {
-              if (isPR) {
-                console.log('PRコメントを取得中...');
-                const { data: commentsList } = await github.rest.issues.listComments({
-                  owner: context.repo.owner,
-                  repo: context.repo.repo,
-                  issue_number: issueNumber
-                });
-                comments = commentsList.map(comment => `${comment.user.login}: ${comment.body}`).join('\n');
-              } else {
-                console.log('Issueコメントを取得中...');
-                const { data: commentsList } = await github.rest.issues.listComments({
-                  owner: context.repo.owner,
-                  repo: context.repo.repo,
-                  issue_number: issueNumber
-                });
-                comments = commentsList.map(comment => `${comment.user.login}: ${comment.body}`).join('\n');
-              }
-              
-              console.log(`取得したコメント数: ${comments.split('\n').filter(line => line.trim()).length}`);
-              console.log(`コメント内容 (最初の500文字): "${comments.substring(0, 500)}${comments.length > 500 ? '...' : ''}"`);
-              
-              core.setOutput('comments', comments);
-              
+              const { data: commentsList } = await github.rest.issues.listComments({
+                owner: context.repo.owner, repo: context.repo.repo, issue_number: issueNumber
+              });
+              comments = commentsList.map(comment => `${comment.user.login}: ${comment.body}`).join('\n');
             } catch (error) {
-              console.error(`${isPR ? 'PR' : 'Issue'}コメントの取得に失敗:`, error.message);
-              comments = `${isPR ? 'PR' : 'Issue'}コメントの取得に失敗: ${error.message}`;
-              core.setOutput('comments', comments);
+              comments = `コメントの取得に失敗: ${error.message}`;
             }
+            core.setOutput('comments', comments);
 
       - name: '🐛 デバッグ: 最終データを確認'
-        run: |-
+        env:
+          USER_REQUEST: ${{ steps.get_context.outputs.user_request }}
+          ISSUE_NUMBER: ${{ steps.get_context.outputs.issue_number }}
+          ISSUE_TITLE: ${{ steps.get_context.outputs.issue_title }}
+          DESCRIPTION: ${{ steps.get_description.outputs.description }}
+          COMMENTS: ${{ steps.get_comments.outputs.comments }}
+          IS_PR: ${{ steps.get_context.outputs.is_pr }}
+        run: |
           echo "=== 最終データ確認 ==="
-          echo "User Request: '${{ steps.get_context.outputs.user_request }}'"
-          echo "Issue Number: '${{ steps.get_context.outputs.issue_number }}'"
-          echo "Issue Title: '${{ steps.get_context.outputs.issue_title }}'"
-          echo "Description Length: $(echo '${{ steps.get_description.outputs.description }}' | wc -c)"
-          echo "Comments Length: $(echo '${{ steps.get_comments.outputs.comments }}' | wc -c)"
-          echo "Is PR: '${{ steps.get_context.outputs.is_pr }}'"
+          echo "User Request: '$USER_REQUEST'"
+          echo "Issue Number: '$ISSUE_NUMBER'"
+          echo "Issue Title: '$ISSUE_TITLE'"
+          echo "Description Length: $(echo "$DESCRIPTION" | wc -c)"
+          echo "Comments Length: $(echo "$COMMENTS" | wc -c)"
+          echo "Is PR: '$IS_PR'"
 
       - name: 'Geminiを実行'
         id: 'run_gemini'
@@ -413,27 +326,17 @@ jobs:
           use_gemini_code_assist: '${{ vars.GOOGLE_GENAI_USE_GCA }}'
           settings: |-
             {
-              "debug": ${{ fromJSON(env.DEBUG || env.ACTIONS_STEP_DEBUG || true) }},
+              "debug": true,
               "maxSessionTurns": 50,
-              "telemetry": {
-                "enabled": false,
-                "target": "gcp"
-              }
+              "telemetry": { "enabled": false }
             }
           prompt: |-
             ## デバッグ情報
-            
             - **生のBody**: `${{ steps.get_context.outputs.raw_body }}`
             - **処理されたユーザーリクエスト**: `${{ steps.get_context.outputs.user_request }}`
-            - **Issue Body文字数**: 詳細はログを確認してください
-            - **コメント文字数**: 詳細はログを確認してください
-
             ## 役割
-
             あなたはGitHubワークフローのCLIインターフェース経由で呼び出される親切なAIアシスタントです。リポジトリとやり取りし、ユーザーに応答するためのツールを使用できます。
-
             ## コンテキスト
-
             - **リポジトリ**: `${{ github.repository }}`
             - **トリガーイベント**: `${{ github.event_name }}`
             - **Issue/PR番号**: `${{ steps.get_context.outputs.issue_number }}`
@@ -443,89 +346,14 @@ jobs:
             `${{ steps.get_description.outputs.description }}`
             - **コメント**:
             `${{ steps.get_comments.outputs.comments }}`
-
             ## ユーザーリクエスト
-
             ユーザーから以下のリクエストが送信されました：
             `${{ steps.get_context.outputs.user_request }}`
-
-            **注意**: もしユーザーリクエストが空または「内容が空です - デバッグが必要」の場合、以下の手順でデバッグしてください：
-
-            1. 生のBody内容を確認: `${{ steps.get_context.outputs.raw_body }}`
-            2. Issue/PR情報を再確認
-            3. GitHubのAPIレスポンスをチェック
-            4. ユーザーに問題を報告し、直接メンションまたはコメントを求める
-
-            ## Issue、PRコメント、質問への応答方法
-
-            このワークフローは3つの主要なシナリオをサポートしています：
-
-            1. **Issueの修正を作成**
-               - ユーザーリクエストと関連するIssueまたはPRの説明を注意深く読んでください。
-               - 利用可能なツールを使用してすべての関連コンテキストを収集してください（例：`gh issue view`、`gh pr view`、`gh pr diff`、`cat`、`head`、`tail`）。
-               - 先に進む前に問題の根本原因を特定してください。
-               - **チェックリストとして計画を表示し維持してください**：
-                 - 最初に、Issueまたはリクエストを解決するために必要なステップを概説し、IssueまたはPRにチェックリストコメントとして投稿してください（GitHubマークダウンのチェックボックスを使用：`- [ ] タスク`）。
-                 - 例：
-                   \```
-                   ### 計画
-                   - [ ] 根本原因の調査
-                   - [ ] `file.py`での修正の実装
-                   - [ ] テストの追加/修正
-                   - [ ] ドキュメントの更新
-                   - [ ] 修正の確認とIssueのクローズ
-                   \```
-                 - 使用：`gh pr comment "${ISSUE_NUMBER}" --body "<plan>"`または`gh issue comment "${ISSUE_NUMBER}" --body "<plan>"`で初期計画を投稿。
-                 - 進捗に応じて、同じコメントを編集してチェックリストを最新かつ見やすく保ってください（完了したタスクに`- [x]`をチェック）。
-                   - チェックリストを更新するには：
-                     1. チェックリストのコメントIDを見つけます（`gh pr comment list "${ISSUE_NUMBER}"`または`gh issue comment list "${ISSUE_NUMBER}"`を使用）。
-                     2. 更新されたチェックリストでコメントを編集します：
-                        - PRの場合：`gh pr comment --edit <comment-id> --body "<updated plan>"`
-                        - Issueの場合：`gh issue comment --edit <comment-id> --body "<updated plan>"`
-                     3. チェックリストはIssueまたはPRのコメントとしてのみ維持されるべきです。コードファイルでチェックリストを追跡または更新しないでください。
-               - 修正にコードの変更が必要な場合は、影響を受けるファイルと行を特定してください。明確化が必要な場合は、ユーザーへの質問をメモしてください。
-               - 利用可能なツール（例：`write_file`）を使用して必要なコードまたはドキュメントの変更を行ってください。すべての変更がプロジェクトの規約とベストプラクティスに従っていることを確認してください。エラーを防ぐため、すべてのシェル変数を`"${VAR}"`（引用符と波括弧付き）として参照してください。
-               - 修正が意図通りに動作することを確認するために、関連するテストまたはチェックを実行してください。可能であれば、Issueが解決されたという証拠（テスト出力、スクリーンショットなど）を提供してください。
-               - **ブランチ作成とコミット**：
-                 - **決して`main`ブランチに直接コミットしないでください。**
-                 - **プルリクエスト**（`IS_PR`が`true`）で作業している場合、正しいブランチは既にチェックアウトされています。単純にコミットしてプッシュしてください。
-                   - `git add .`
-                   - `git commit -m "feat: <変更の説明>"`
-                   - `git push`
-                 - **Issue**（`IS_PR`が`false`）で作業している場合、変更のための新しいブランチを作成してください。適切なブランチ名は`issue/${ISSUE_NUMBER}/<短い説明>`です。
-                   - `git checkout -b issue/${ISSUE_NUMBER}/my-fix`
-                   - `git add .`
-                   - `git commit -m "feat: <修正の説明>"`
-                   - `git push origin issue/${ISSUE_NUMBER}/my-fix`
-                   - プッシュ後、プルリクエストを作成できます：`gh pr create --title "Fixes #${ISSUE_NUMBER}: <短いタイトル>" --body "このPRはIssue #${ISSUE_NUMBER}に対処します。"`
-               - マークダウンファイルで何が変更され、その理由を要約してください：`write_file("response.md", "<ここにあなたの応答>")`
-               - 応答をコメントとして投稿：
-                 - PRの場合：`gh pr comment "${ISSUE_NUMBER}" --body-file response.md`
-                 - Issueの場合：`gh issue comment "${ISSUE_NUMBER}" --body-file response.md`
-
-            2. **プルリクエストのコメントに対処**
-               - 特定のコメントとPRのコンテキストを読んでください。
-               - `gh pr view`、`gh pr diff`、`cat`などのツールを使用してコードと議論を理解してください。
-               - コメントが変更や明確化を求めている場合、Issueの修正と同じプロセスに従ってください：チェックリスト計画を作成し、実装し、テストし、必要な変更をコミットし、進行に応じてチェックリストを更新してください。
-               - **変更のコミット**：正しいPRブランチは既にチェックアウトされています。単純に変更を追加、コミット、プッシュしてください。
-                 - `git add .`
-                 - `git commit -m "fix: レビューコメントに対処"`
-                 - `git push`
-               - コメントが質問の場合、必要に応じてコードまたはドキュメントを参照して、直接的かつ明確に答えてください。
-               - `response.md`で応答を文書化し、PRコメントとして投稿：`gh pr comment "${ISSUE_NUMBER}" --body-file response.md`
-
-            3. **Issueの任意の質問に答える**
-               - `gh issue view`および関連ツールを使用して、質問と完全なIssueコンテキストを読んでください。
-               - 正確な回答を提供するために、必要に応じてコードベースを研究または分析してください。
-               - 質問にコードまたはドキュメントの変更が必要な場合、上記の修正プロセスに従い、チェックリスト計画の作成と更新、および**セクション1で説明されている変更のための新しいブランチの作成**を含めてください。
-               - `response.md`で明確で簡潔な回答を書き、Issueコメントとして投稿：`gh issue comment "${ISSUE_NUMBER}" --body-file response.md`
-
-            ## ガイドライン
-
-            - **簡潔で実行可能であること。** ユーザーの問題を効率的に解決することに焦点を当ててください。
-            - **コードまたはドキュメントを修正した場合は、常に変更をコミットしてプッシュしてください。**
-            - **修正や回答について不明な場合は、あなたの推論を説明し、明確化の質問をしてください。**
-            - **プロジェクトの規約とベストプラクティスに従ってください。**
-            - **もしissue bodyまたはユーザーリクエストが空の場合、デバッグ情報を使用して問題を分析し、ユーザーに報告してください。**
-
-            すべての応答とコメントは日本語で行ってください。
+            ## 指示
+            あなたは熟練したソフトウェアエンジニアとして振る舞い、提供されたツールを使用してユーザーのリクエストを解決してください。
+            - **計画の提示**: 最初に、問題を解決するためのステップをチェックリスト形式でコメントしてください。(`gh issue comment` または `gh pr comment` を使用)
+            - **ブランチ管理**: `main`ブランチには直接コミットしないでください。Issueの場合は `issue/${{ steps.get_context.outputs.issue_number }}/<短い説明>` のような新しいブランチを作成してください。PRの場合は、チェックアウト済みのブランチで作業してください。
+            - **コードの変更**: `write_file` ツールを使用してコードを修正します。
+            - **コミットとプッシュ**: 変更をコミットし、適切なブランチにプッシュしてください。
+            - **応答**: 完了したら、行った変更の概要をコメントで報告してください。
+            - **言語**: すべての応答は日本語で行ってください。
```
