# 💻 Daily Code Changes

## Full Diff

```diff
commit 3665236842b1f332e840c0d1c9f562fd976bae68
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Sun Aug 24 15:50:04 2025 +0900

    Update gemini-jp-cli.yml

diff --git a/.github/workflows/gemini-jp-cli.yml b/.github/workflows/gemini-jp-cli.yml
index f9a7772..5188cfe 100644
--- a/.github/workflows/gemini-jp-cli.yml
+++ b/.github/workflows/gemini-jp-cli.yml
@@ -72,6 +72,33 @@ jobs:
     timeout-minutes: 10
     runs-on: 'ubuntu-latest'
     steps:
+      - name: '🐛 デバッグ: イベント情報を出力'
+        run: |-
+          echo "=== イベント詳細 ==="
+          echo "Event Name: ${{ github.event_name }}"
+          echo "Event Action: ${{ github.event.action }}"
+          echo "Repository: ${{ github.repository }}"
+          echo "Actor: ${{ github.actor }}"
+          echo ""
+          echo "=== Issue情報 ==="
+          echo "Issue Number: ${{ github.event.issue.number || 'N/A' }}"
+          echo "Issue Title: ${{ github.event.issue.title || 'N/A' }}"
+          echo "Issue Body Length: ${{ length(github.event.issue.body || '') }}"
+          echo "Issue Author: ${{ github.event.issue.user.login || 'N/A' }}"
+          echo "Issue Association: ${{ github.event.issue.author_association || 'N/A' }}"
+          echo ""
+          echo "=== Comment情報 ==="
+          echo "Comment Body Length: ${{ length(github.event.comment.body || '') }}"
+          echo "Comment Author: ${{ github.event.comment.user.login || 'N/A' }}"
+          echo "Comment Association: ${{ github.event.comment.author_association || 'N/A' }}"
+          echo ""
+          echo "=== PR Review情報 ==="
+          echo "Review Body Length: ${{ length(github.event.review.body || '') }}"
+          echo "PR Number: ${{ github.event.pull_request.number || 'N/A' }}"
+          echo ""
+          echo "=== 完全なイベントペイロード ==="
+          echo '${{ toJSON(github.event) }}'
+
       - name: 'GitHub App トークンを生成'
         id: 'generate_token'
         if: |-
@@ -83,43 +110,137 @@ jobs:
 
       - name: 'イベントからコンテキストを取得'
         id: 'get_context'
-        env:
-          EVENT_NAME: '${{ github.event_name }}'
-          EVENT_PAYLOAD: '${{ toJSON(github.event) }}'
-        run: |-
-          set -euo pipefail
+        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+        with:
+          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          script: |-
+            console.log('=== コンテキスト取得開始 ===');
+            console.log(`Event Name: ${context.eventName}`);
+            console.log(`Event Action: ${context.payload.action || 'N/A'}`);
+            console.log(`Repository: ${context.repo.owner}/${context.repo.repo}`);
+            console.log(`Actor: ${context.actor}`);
 
-          USER_REQUEST=""
-          ISSUE_NUMBER=""
-          IS_PR="false"
-
-          if [[ "${EVENT_NAME}" == "issues" ]]; then
-            USER_REQUEST=$(echo "${EVENT_PAYLOAD}" | jq -r .issue.body)
-            ISSUE_NUMBER=$(echo "${EVENT_PAYLOAD}" | jq -r .issue.number)
-          elif [[ "${EVENT_NAME}" == "issue_comment" ]]; then
-            USER_REQUEST=$(echo "${EVENT_PAYLOAD}" | jq -r .comment.body)
-            ISSUE_NUMBER=$(echo "${EVENT_PAYLOAD}" | jq -r .issue.number)
-            if [[ $(echo "${EVENT_PAYLOAD}" | jq -r .issue.pull_request) != "null" ]]; then
-              IS_PR="true"
-            fi
-          elif [[ "${EVENT_NAME}" == "pull_request_review" ]]; then
-            USER_REQUEST=$(echo "${EVENT_PAYLOAD}" | jq -r .review.body)
-            ISSUE_NUMBER=$(echo "${EVENT_PAYLOAD}" | jq -r .pull_request.number)
-            IS_PR="true"
-          elif [[ "${EVENT_NAME}" == "pull_request_review_comment" ]]; then
-            USER_REQUEST=$(echo "${EVENT_PAYLOAD}" | jq -r .comment.body)
-            ISSUE_NUMBER=$(echo "${EVENT_PAYLOAD}" | jq -r .pull_request.number)
-            IS_PR="true"
-          fi
+            let userRequest = '';
+            let issueNumber = '';
+            let isPR = false;
+            let rawBody = '';
+            let issueTitle = '';
+
+            try {
+              if (context.eventName === 'issues') {
+                console.log('処理中: Issues イベント');
+                rawBody = context.payload.issue.body || '';
+                userRequest = rawBody;
+                issueNumber = context.payload.issue.number.toString();
+                issueTitle = context.payload.issue.title || '';
+                console.log(`Issue #${issueNumber}: "${issueTitle}"`);
+                console.log(`Issue Body 長さ: ${rawBody.length}`);
+                console.log(`Issue Body (最初の200文字): "${rawBody.substring(0, 200)}${rawBody.length > 200 ? '...' : ''}"`);
+                
+              } else if (context.eventName === 'issue_comment') {
+                console.log('処理中: Issue Comment イベント');
+                rawBody = context.payload.comment.body || '';
+                userRequest = rawBody;
+                issueNumber = context.payload.issue.number.toString();
+                issueTitle = context.payload.issue.title || '';
+                console.log(`Comment on Issue #${issueNumber}: "${issueTitle}"`);
+                console.log(`Comment Body 長さ: ${rawBody.length}`);
+                console.log(`Comment Body (最初の200文字): "${rawBody.substring(0, 200)}${rawBody.length > 200 ? '...' : ''}"`);
+                
+                if (context.payload.issue.pull_request) {
+                  isPR = true;
+                  console.log('これはPRのコメントです');
+                }
+                
+              } else if (context.eventName === 'pull_request_review') {
+                console.log('処理中: PR Review イベント');
+                rawBody = context.payload.review.body || '';
+                userRequest = rawBody;
+                issueNumber = context.payload.pull_request.number.toString();
+                issueTitle = context.payload.pull_request.title || '';
+                isPR = true;
+                console.log(`Review on PR #${issueNumber}: "${issueTitle}"`);
+                console.log(`Review Body 長さ: ${rawBody.length}`);
+                console.log(`Review Body (最初の200文字): "${rawBody.substring(0, 200)}${rawBody.length > 200 ? '...' : ''}"`);
+                
+              } else if (context.eventName === 'pull_request_review_comment') {
+                console.log('処理中: PR Review Comment イベント');
+                rawBody = context.payload.comment.body || '';
+                userRequest = rawBody;
+                issueNumber = context.payload.pull_request.number.toString();
+                issueTitle = context.payload.pull_request.title || '';
+                isPR = true;
+                console.log(`PR Comment on PR #${issueNumber}: "${issueTitle}"`);
+                console.log(`PR Comment Body 長さ: ${rawBody.length}`);
+                console.log(`PR Comment Body (最初の200文字): "${rawBody.substring(0, 200)}${rawBody.length > 200 ? '...' : ''}"`);
+              }
 
-          # ユーザーリクエストをクリーンアップ
-          USER_REQUEST=$(echo "${USER_REQUEST}" | sed 's/.*@gemini-jp-cli//' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
+              console.log('=== 処理前の値 ===');
+              console.log(`Raw Body: "${rawBody}"`);
+              console.log(`User Request (処理前): "${userRequest}"`);
+              console.log(`Issue Number: "${issueNumber}"`);
+              console.log(`Issue Title: "${issueTitle}"`);
+              console.log(`Is PR: ${isPR}`);
 
-          {
-            echo "user_request=${USER_REQUEST}"
-            echo "issue_number=${ISSUE_NUMBER}"
-            echo "is_pr=${IS_PR}"
-          } >> "${GITHUB_OUTPUT}"
+              // @gemini-jp-cli を含んでいるかチェック
+              if (userRequest.includes('@gemini-jp-cli')) {
+                console.log('@gemini-jp-cli が見つかりました');
+                // ユーザーリクエストをクリーンアップ
+                const mentionIndex = userRequest.indexOf('@gemini-jp-cli');
+                userRequest = userRequest.substring(mentionIndex + '@gemini-jp-cli'.length).trim();
+                console.log(`クリーンアップ後: "${userRequest}"`);
+              } else {
+                console.log('警告: @gemini-jp-cli が見つかりません');
+                // メンションなしでも処理を続行（デバッグ目的）
+                console.log('デバッグモード: メンションなしでも処理を続行');
+              }
+
+              // 空文字チェック
+              if (!userRequest) {
+                console.log('警告: USER_REQUEST が空です');
+                userRequest = rawBody ? `元の内容: ${rawBody}` : '内容が空です - デバッグが必要';
+              }
+
+              if (!issueNumber || issueNumber === '0') {
+                console.error('エラー: ISSUE_NUMBER が空です');
+                issueNumber = '0';
+              }
+
+              console.log('=== 最終的な出力値 ===');
+              console.log(`Final User Request: "${userRequest}"`);
+              console.log(`Final Issue Number: "${issueNumber}"`);
+              console.log(`Final Issue Title: "${issueTitle}"`);
+              console.log(`Final Is PR: ${isPR}`);
+
+              // 後続のステップで使用するために出力
+              core.setOutput('user_request', userRequest);
+              core.setOutput('issue_number', issueNumber);
+              core.setOutput('issue_title', issueTitle);
+              core.setOutput('is_pr', isPR.toString());
+              core.setOutput('raw_body', rawBody);
+
+            } catch (error) {
+              console.error('コンテキスト取得中にエラーが発生:', error.message);
+              console.error('スタックトレース:', error.stack);
+              
+              // エラー時のフォールバック値を設定
+              core.setOutput('user_request', 'エラーが発生しました');
+              core.setOutput('issue_number', '0');
+              core.setOutput('issue_title', 'エラー');
+              core.setOutput('is_pr', 'false');
+              core.setOutput('raw_body', '');
+              
+              throw error;
+            }
+
+      - name: '🐛 デバッグ: 取得したコンテキストを確認'
+        run: |-
+          echo "=== 取得されたコンテキスト ==="
+          echo "User Request: '${{ steps.get_context.outputs.user_request }}'"
+          echo "Issue Number: '${{ steps.get_context.outputs.issue_number }}'"
+          echo "Issue Title: '${{ steps.get_context.outputs.issue_title }}'"
+          echo "Is PR: '${{ steps.get_context.outputs.is_pr }}'"
+          echo "Raw Body: '${{ steps.get_context.outputs.raw_body }}'"
 
       - name: 'コミット用のgitユーザーを設定'
         run: |-
@@ -154,50 +275,124 @@ jobs:
           REQUEST_TYPE: '${{ steps.get_context.outputs.request_type }}'
         run: |-
           set -euo pipefail
-          MESSAGE="@${GITHUB_ACTOR} リクエストを受け取りました。今から作業を開始します！ 🤖"
+          MESSAGE="@${GITHUB_ACTOR} リクエストを受け取りました。今から作業を開始します！ 🤖
+
+          デバッグ情報:
+          - ユーザーリクエスト: '${{ steps.get_context.outputs.user_request }}'
+          - Issue/PR番号: ${ISSUE_NUMBER}
+          - イベント種類: ${{ github.event_name }}
+          - 生データ: '${{ steps.get_context.outputs.raw_body }}'"
+          
           if [[ -n "${MESSAGE}" ]]; then
-            gh issue comment "${ISSUE_NUMBER}" \
-              --body "${MESSAGE}" \
-              --repo "${REPOSITORY}"
+            if [[ "${{ steps.get_context.outputs.is_pr }}" == "true" ]]; then
+              gh pr comment "${ISSUE_NUMBER}" \
+                --body "${MESSAGE}" \
+                --repo "${REPOSITORY}"
+            else
+              gh issue comment "${ISSUE_NUMBER}" \
+                --body "${MESSAGE}" \
+                --repo "${REPOSITORY}"
+            fi
           fi
 
       - name: '説明を取得'
         id: 'get_description'
-        env:
-          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          IS_PR: '${{ steps.get_context.outputs.is_pr }}'
-          ISSUE_NUMBER: '${{ steps.get_context.outputs.issue_number }}'
-        run: |-
-          set -euo pipefail
-          if [[ "${IS_PR}" == "true" ]]; then
-            DESCRIPTION=$(gh pr view "${ISSUE_NUMBER}" --json body --template '{{.body}}')
-          else
-            DESCRIPTION=$(gh issue view "${ISSUE_NUMBER}" --json body --template '{{.body}}')
-          fi
-          {
-            echo "description<<EOF"
-            echo "${DESCRIPTION}"
-            echo "EOF"
-          } >> "${GITHUB_OUTPUT}"
+        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+        with:
+          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          script: |-
+            console.log('=== 説明取得開始 ===');
+            const isPR = '${{ steps.get_context.outputs.is_pr }}' === 'true';
+            const issueNumber = parseInt('${{ steps.get_context.outputs.issue_number }}');
+            
+            console.log(`Is PR: ${isPR}`);
+            console.log(`Issue Number: ${issueNumber}`);
+            
+            let description = '';
+            
+            try {
+              if (isPR) {
+                console.log('PR情報を取得中...');
+                const { data: pr } = await github.rest.pulls.get({
+                  owner: context.repo.owner,
+                  repo: context.repo.repo,
+                  pull_number: issueNumber
+                });
+                description = pr.body || '';
+                console.log(`PR title: "${pr.title}"`);
+              } else {
+                console.log('Issue情報を取得中...');
+                const { data: issue } = await github.rest.issues.get({
+                  owner: context.repo.owner,
+                  repo: context.repo.repo,
+                  issue_number: issueNumber
+                });
+                description = issue.body || '';
+                console.log(`Issue title: "${issue.title}"`);
+              }
+              
+              console.log(`取得した説明の長さ: ${description.length}`);
+              console.log(`取得した説明 (最初の200文字): "${description.substring(0, 200)}${description.length > 200 ? '...' : ''}"`);
+              
+              core.setOutput('description', description);
+              
+            } catch (error) {
+              console.error(`${isPR ? 'PR' : 'Issue'}情報の取得に失敗:`, error.message);
+              description = `${isPR ? 'PR' : 'Issue'}情報の取得に失敗: ${error.message}`;
+              core.setOutput('description', description);
+            }
 
       - name: 'コメントを取得'
         id: 'get_comments'
-        env:
-          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          IS_PR: '${{ steps.get_context.outputs.is_pr }}'
-          ISSUE_NUMBER: '${{ steps.get_context.outputs.issue_number }}'
+        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+        with:
+          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          script: |-
+            console.log('=== コメント取得開始 ===');
+            const isPR = '${{ steps.get_context.outputs.is_pr }}' === 'true';
+            const issueNumber = parseInt('${{ steps.get_context.outputs.issue_number }}');
+            
+            let comments = '';
+            
+            try {
+              if (isPR) {
+                console.log('PRコメントを取得中...');
+                const { data: commentsList } = await github.rest.issues.listComments({
+                  owner: context.repo.owner,
+                  repo: context.repo.repo,
+                  issue_number: issueNumber
+                });
+                comments = commentsList.map(comment => `${comment.user.login}: ${comment.body}`).join('\n');
+              } else {
+                console.log('Issueコメントを取得中...');
+                const { data: commentsList } = await github.rest.issues.listComments({
+                  owner: context.repo.owner,
+                  repo: context.repo.repo,
+                  issue_number: issueNumber
+                });
+                comments = commentsList.map(comment => `${comment.user.login}: ${comment.body}`).join('\n');
+              }
+              
+              console.log(`取得したコメント数: ${comments.split('\n').filter(line => line.trim()).length}`);
+              console.log(`コメント内容 (最初の500文字): "${comments.substring(0, 500)}${comments.length > 500 ? '...' : ''}"`);
+              
+              core.setOutput('comments', comments);
+              
+            } catch (error) {
+              console.error(`${isPR ? 'PR' : 'Issue'}コメントの取得に失敗:`, error.message);
+              comments = `${isPR ? 'PR' : 'Issue'}コメントの取得に失敗: ${error.message}`;
+              core.setOutput('comments', comments);
+            }
+
+      - name: '🐛 デバッグ: 最終データを確認'
         run: |-
-          set -euo pipefail
-          if [[ "${IS_PR}" == "true" ]]; then
-            COMMENTS=$(gh pr view "${ISSUE_NUMBER}" --json comments --template '{{range .comments}}{{.author.login}}: {{.body}}{{"\n"}}{{end}}')
-          else
-            COMMENTS=$(gh issue view "${ISSUE_NUMBER}" --json comments --template '{{range .comments}}{{.author.login}}: {{.body}}{{"\n"}}{{end}}')
-          fi
-          {
-            echo "comments<<EOF"
-            echo "${COMMENTS}"
-            echo "EOF"
-          } >> "${GITHUB_OUTPUT}"
+          echo "=== 最終データ確認 ==="
+          echo "User Request: '${{ steps.get_context.outputs.user_request }}'"
+          echo "Issue Number: '${{ steps.get_context.outputs.issue_number }}'"
+          echo "Issue Title: '${{ steps.get_context.outputs.issue_title }}'"
+          echo "Description Length: ${{ length(steps.get_description.outputs.description) }}"
+          echo "Comments Length: ${{ length(steps.get_comments.outputs.comments) }}"
+          echo "Is PR: '${{ steps.get_context.outputs.is_pr }}'"
 
       - name: 'Geminiを実行'
         id: 'run_gemini'
@@ -218,7 +413,7 @@ jobs:
           use_gemini_code_assist: '${{ vars.GOOGLE_GENAI_USE_GCA }}'
           settings: |-
             {
-              "debug": ${{ fromJSON(env.DEBUG || env.ACTIONS_STEP_DEBUG || false) }},
+              "debug": ${{ fromJSON(env.DEBUG || env.ACTIONS_STEP_DEBUG || true) }},
               "maxSessionTurns": 50,
               "telemetry": {
                 "enabled": false,
@@ -226,6 +421,13 @@ jobs:
               }
             }
           prompt: |-
+            ## デバッグ情報
+            
+            - **生のBody**: `${{ steps.get_context.outputs.raw_body }}`
+            - **処理されたユーザーリクエスト**: `${{ steps.get_context.outputs.user_request }}`
+            - **Issue Body長さ**: ${{ length(steps.get_description.outputs.description) }}文字
+            - **コメント長さ**: ${{ length(steps.get_comments.outputs.comments) }}文字
+
             ## 役割
 
             あなたはGitHubワークフローのCLIインターフェース経由で呼び出される親切なAIアシスタントです。リポジトリとやり取りし、ユーザーに応答するためのツールを使用できます。
@@ -235,6 +437,7 @@ jobs:
             - **リポジトリ**: `${{ github.repository }}`
             - **トリガーイベント**: `${{ github.event_name }}`
             - **Issue/PR番号**: `${{ steps.get_context.outputs.issue_number }}`
+            - **Issue/PRタイトル**: `${{ steps.get_context.outputs.issue_title }}`
             - **これはPRですか？**: `${{ steps.get_context.outputs.is_pr }}`
             - **Issue/PRの説明**:
             `${{ steps.get_description.outputs.description }}`
@@ -246,6 +449,13 @@ jobs:
             ユーザーから以下のリクエストが送信されました：
             `${{ steps.get_context.outputs.user_request }}`
 
+            **注意**: もしユーザーリクエストが空または「内容が空です - デバッグが必要」の場合、以下の手順でデバッグしてください：
+
+            1. 生のBody内容を確認: `${{ steps.get_context.outputs.raw_body }}`
+            2. Issue/PR情報を再確認
+            3. GitHubのAPIレスポンスをチェック
+            4. ユーザーに問題を報告し、直接メンションまたはコメントを求める
+
             ## Issue、PRコメント、質問への応答方法
 
             このワークフローは3つの主要なシナリオをサポートしています：
@@ -316,5 +526,6 @@ jobs:
             - **コードまたはドキュメントを修正した場合は、常に変更をコミットしてプッシュしてください。**
             - **修正や回答について不明な場合は、あなたの推論を説明し、明確化の質問をしてください。**
             - **プロジェクトの規約とベストプラクティスに従ってください。**
+            - **もしissue bodyまたはユーザーリクエストが空の場合、デバッグ情報を使用して問題を分析し、ユーザーに報告してください。**
 
             すべての応答とコメントは日本語で行ってください。
```
