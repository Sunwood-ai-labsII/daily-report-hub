# 💻 Daily Code Changes

## Full Diff

```diff
diff --git a/.github/prompts/gemini-cli_prompt.ja.md b/.github/prompts/gemini-cli_prompt.ja.md
index ad9e315..2dac199 100644
--- a/.github/prompts/gemini-cli_prompt.ja.md
+++ b/.github/prompts/gemini-cli_prompt.ja.md
@@ -92,167 +92,177 @@ ${USER_REQUEST}
   - コミット例: `feat: ✨ CLI に --dry-run を追加`
   - PRタイトル例: `📝 ドキュメント: README にセットアップ手順を追記`
 
-## 🧭 進捗・PRのレポート方針（AAR + 絵文字）
+## 🧭 進捗・PRのレポート方針（AON + 絵文字）
+
+- 進捗コメントや PR の本文は、読みやすいマークダウンと絵文字を用い、**Agent Ops Note (AON)** 形式で記載してください。
+- AON 構成:
+  - **Task ID / Owner / 日時**
+  - **TL;DR**（2〜3行：ねらい → 主要アクション → 成果/影響）
+  - 🎯 1. コンテキスト & 目的
+  - 📝 2. 計画（Plan）
+  - 🔧 3. 実行内容（Do）
+  - ✅ 4. 成果 & 検証（Check）
+  - 💡 5. 意思決定（Act）
+  - 🚧 6. 課題・リスク・次アクション
+  - 🔥 7. 障害/逸脱があった場合のみ：ポストモーテム
+
+### 進捗コメントの例（AON形式）
 
-- 進捗コメントや PR の本文は、読みやすいマークダウンと絵文字を用い、AAR（After Action Review）形式で記載してください。
-- AAR 構成:
-  - 🎯 目的: 何を達成するための作業か
-  - ✅ 実施: 実際に行ったこと（具体的なコマンド/変更内容）
-  - 🔍 差異: 期待と実績のギャップ、想定外事項
-  - 💡 学び: 得られた知見、次に活かす点
-  - ▶️ 次のアクション: レビュー/追作業/検証などの依頼
+\```
+# Agent Ops Note (AON)
+- **Task:** Issue #${ISSUE_NUMBER} / Agent / $(date +"%Y-%m-%d %H:%M")
+- **TL;DR:** Issue #${ISSUE_NUMBER} の簡易HTML作成要求 → `example/index.html` 実装・コミット → サンプルアプリ提供完了
 
-### 詳細AAR（推奨の深掘り項目）
+## 🎯 1. コンテキスト & 目的
+- Issue #${ISSUE_NUMBER} でサンプル用HTMLアプリの作成依頼
+- 目標: テンプレート用途の最小構成UIを提供
 
-可能な限り、以下も含めて「詳細AAR」を作成してください（取得可能な情報は `gh pr view`/`gh pr diff --stat` で収集）。
+## 📝 2. 計画（Plan）
+- 依存ライブラリなしのバニラJS + HTML構成
+- localStorage で永続化、CRUD操作を含む
 
-- 🧩 コンテキスト: 関連Issue/PR、ブランチ、背景、スコープ外
-- 🧾 変更サマリ: 変更ファイル数、追加/削除行、主要コンポーネント
-- 🛠 実装詳細: ファイル/関数単位の要点、依存関係、設計判断
-- 🧪 検証: 手動/自動テスト観点、再現/確認手順、環境情報
-- ⚠️ リスク/影響: 互換性、パフォーマンス、セキュリティ、既知の制約
-- 🔁 ロールバック: 戻し方、ガード、Feature Flag の有無
-- 🔗 リンク集: 比較URL、コミット、関連Issue、スクショ/デモ
-- 📌 フォローアップ: TODO、別Issue化、監視/計測の計画
+## 🔧 3. 実行内容（Do）
+- `example/index.html` を新規作成（102行追加）
+- タイトル/本文入力、保存・編集・削除機能を実装
+- Git: add → commit → push 完了
 
-### 進捗コメントの例
+## ✅ 4. 成果 & 検証（Check）
+- 期待通りの動作を確認（Chrome/Firefox でテスト）
+- 成果物: `example/index.html`（シングルファイル構成）
 
-\```
-## 📋 AAR 進捗報告
-- 🎯 目的: Issue #${ISSUE_NUMBER} の簡易HTML作成
-- ✅ 実施: `example/index.html` を作成し、チェックリストを更新
-- 🔍 差異: とくになし
-- 💡 学び: 相対パスではなく絶対パスでの `write_file` が必要
-- ▶️ 次のアクション: 内容レビューのお願い
+## 💡 5. 意思決定（Act）
+- 依存ゼロの構成を採用し、デプロイ不要のサンプルとした
+
+## 🚧 6. 課題・リスク・次アクション
+- 次: 内容レビューをお願いします
+- リスク: XSS対策は最小限（サンプル用途のため）
 \```
 
-### PR本文の例（response.md 生成時）
+### PR本文の例（AON形式）
 
 \```
-## 📋 AAR（概要）
-- 🎯 目的: Issue #${ISSUE_NUMBER} への対応PR
-- ✅ 実施: ブランチ作成・変更のコミット/プッシュ・PR作成
-- 🔍 差異: 競合はなし（あれば解決内容を記載）
-- 💡 学び: 自動PRフローの安定動作を確認
-- ▶️ 次のアクション: レビューとマージのご確認をお願いします
-
-## 🧭 詳細AAR
-- 🧩 コンテキスト: `issue/${ISSUE_NUMBER}/<slug>` → `main` へ。スコープは <対象領域> に限定。
-- 🧾 変更サマリ: `gh pr diff ${ISSUE_NUMBER} --stat` の結果を貼付
-  - 例) 1 file changed, 102 insertions(+), 4 deletions(-)
-- 🛠 実装詳細:
-  - 主要ファイル: `path/to/file`
-  - 主要変更: <要点1/要点2>
-  - 依存: <新規/更新の依存>
-- 🧪 検証: <ブラウザ/環境> で手動確認、必要に応じてテスト追加
-- ⚠️ リスク/影響: <互換/性能/セキュリティ>、既知の制約 <あれば>
-- 🔁 ロールバック: `git revert <sha>`、影響範囲が限定的で安全
-- 🔗 リンク集: PR/比較URL/コミットURL/関連Issue
-- 📌 フォローアップ: <後続タスク> を Issue 化
+# Agent Ops Note (AON)
+- **Task:** PR #${ISSUE_NUMBER} / Agent / $(date +"%Y-%m-%d %H:%M")
+- **TL;DR:** Issue #${ISSUE_NUMBER} 対応 → ブランチ作成・実装・PR作成 → レビュー待ち
+
+## 🎯 1. コンテキスト & 目的
+- Issue #${ISSUE_NUMBER} への対応PR
+- 背景: <背景説明>
+- 目標: <達成したいこと>
+
+## 📝 2. 計画（Plan）
+- `issue/${ISSUE_NUMBER}/<slug>` ブランチで作業
+- 対象ファイル: <変更予定ファイル>
+- 進め方: <簡単な手順>
+
+## 🔧 3. 実行内容（Do）
+- ブランチ作成: `git checkout -b issue/${ISSUE_NUMBER}/<slug>`
+- 変更ファイル: `<file1>`, `<file2>`
+- Git操作: add → commit → push → PR作成
+
+## ✅ 4. 成果 & 検証（Check）
+- 変更統計: `gh pr diff ${ISSUE_NUMBER} --stat` の結果
+  - 例) 2 files changed, 120 insertions(+), 15 deletions(-)
+- テスト結果: <手動/自動テストの結果>
+- 成果物リンク: 
+  - ブランチ: <branch-url>
+  - 比較: <compare-url>
+  - コミット: <commit-url>
+
+## 💡 5. 意思決定（Act）
+- <重要な設計判断や方針決定を1行で>
+
+## 🚧 6. 課題・リスク・次アクション
+- 次アクション: レビューとマージのご確認をお願いします
+- リスク: <あれば記載>
+- 未解決: <あれば記載>
 
 関連: #${ISSUE_NUMBER}
 \```
 
-※ すべてのコメント・PR本文は日本語で、過度にならない範囲で適切な絵文字を使用してください。
-
 ## 📝 PRレポート（本文）テンプレート例
 
-以下の構成で、読みやすいレポート形式のPR本文を作成してください。
-
 タイトル例（推奨）:
 - `🔧 Fixes #${ISSUE_NUMBER}: 変更の要約`
 
-本文テンプレート:
-\```
-# 🔧 Fixes #${ISSUE_NUMBER}
-
-## 📋 AAR
-- 🎯 目的: Issue #${ISSUE_NUMBER} のリクエスト対応
-- ✅ 実施: 何をどのブランチで、どのファイルを、どう変更したか
-- 🔍 差異: 期待と実績のギャップや想定外（あれば）
-- 💡 学び: 次に活かせる知見
-- ▶️ 次のアクション: レビュー観点・確認依頼
-
-## 🔄 Changes
-- ブランチ: <branch-url>
-- 比較: <compare-url>
-- 最新コミット: <short-sha>
-- 変更ファイル:
-  - `path/to/file1`
-  - `path/to/file2`
-
-## ✅ Reviewer Checklist
-- [ ] 内容の妥当性
-- [ ] 表記ゆれ/誤字の確認
-- [ ] 追加・変更ファイルの確認
-- [ ] 必要に応じたテスト/動作確認
-
-## 📝 Details
-- 変更の背景や補足（あれば）。
-\```
+本文は上記のAON形式を使用してください。
 
 ## 🧪 具体例（今回のPR想定: メモアプリの追加）
 
-以下は「feat: ✨ exampleにシンプルなHTMLのメモアプリを作成（Fixes #19, PR #20, from `issue/19/create-memo-app`）」を題材にした詳細AARの記入例です。実際の値は `gh pr view 20`/`gh pr diff 20 --stat` で取得して置き換えてください。
-
 \```
-# ✨ Fixes #19: example にシンプルなHTMLメモアプリを追加
-
-## 📋 AAR（概要）
-- 🎯 目的: example 配下に最小構成のメモアプリを追加し、テンプレ用途の UI/ローカル永続化サンプルを提供する
-- ✅ 実施: `issue/19/create-memo-app` ブランチで `example/index.html` を実装し、PR #20 を作成
-- 🔍 差異: 仕様策定時は表示のみ想定だったが、削除と編集の最小機能も追加
-- 💡 学び: `localStorage` を使うと依存ゼロで常駐不要のデモが作りやすい
-- ▶️ 次のアクション: UI 文言の再校正とアクセシビリティの簡易チェックをレビュー依頼
-
-## 🧭 詳細AAR
-- 🧩 コンテキスト: `issue/19/create-memo-app` → `main`。スコープは `example/` のみ。他パッケージに影響しない。
-- 🧾 変更サマリ:
-  - 1 file changed, 102 insertions(+), 4 deletions(-)
-  - 変更ファイル: `example/index.html`
-- 🛠 実装詳細:
-  - 追加: タイトル/本文入力、保存ボタン、メモ一覧、編集/削除操作、`localStorage` による永続化
-  - 設計: 依存ライブラリなし。バニラ JS + 最小 CSS。ID ベースのデータ構造で簡易管理。
-  - コード: `example/index.html` 内に `<script>` と `<style>` を内包
-- 🧪 検証:
-  - 手動: Chrome/Firefox/Safari で作成/編集/削除/再読込後の持続性を確認
-  - 確認手順: ファイルをローカルで開き、入力→保存→一覧表示→編集→削除→リロード
-- ⚠️ リスク/影響:
-  - 影響範囲はサンプル配下のみ。既存機能への副作用なし
-  - 既知の制約: 同期ストレージのため同時編集は非対応、XSS 対策は最小
-- 🔁 ロールバック: PR リバートまたは `git revert <commit>`。例示コンテンツの削除で完了
-- 🔗 リンク集:
-  - PR: <pr-url>（#20）/ 比較: <compare-url> / 最新コミット: <short-sha>
-  - 関連 Issue: #19
-- 📌 フォローアップ:
-  - [ ] 入力バリデーションと XSS 対策の強化
-  - [ ] UI のアクセシビリティ改善（ラベル/フォーカス順）
-
-## 🔄 Changes
-- 追加/削除行: +102 / -4
-- 変更ファイル
-  - `example/index.html`
-
-## ✅ Reviewer Checklist（推奨観点）
-- [ ] 仕様と UI の齟齬がないか
-- [ ] localStorage のキー設計/初期化/マイグレーション不要性
+# Agent Ops Note (AON)
+- **Task:** PR #20 (Issue #19) / Agent / 2024-01-15 14:30
+- **TL;DR:** Issueで要求されたHTMLメモアプリ → example/index.html実装・機能追加 → レビュー待ち状態
+
+## 🎯 1. コンテキスト & 目的
+- Issue #19: example 配下に最小構成のメモアプリ追加要求
+- 目標: テンプレート用途の UI/ローカル永続化サンプルを提供
+
+## 📝 2. 計画（Plan）
+- `issue/19/create-memo-app` ブランチで作業
+- 依存ライブラリなし、バニラJS + 最小CSS
+- localStorage による永続化でCRUD操作を実装
+
+## 🔧 3. 実行内容（Do）
+- ブランチ作成・切り替え
+- `example/index.html` を新規作成（102行追加、4行削除）
+- 機能実装: タイトル/本文入力、保存ボタン、メモ一覧、編集/削除操作
+- Git: add → commit → push → PR #20 作成
+
+## ✅ 4. 成果 & 検証（Check）
+- 期待: 基本表示機能のみ → 実測: CRUD操作まで含む完全版
+- 動作確認: Chrome/Firefox/Safari で確認済み
+- 変更統計: 1 file changed, 102 insertions(+), 4 deletions(-)
+- 成果物:
+  - PR: #20
+  - ブランチ: issue/19/create-memo-app
+  - 比較: <compare-url>
+  - 最新コミット: <short-sha>
+
+## 💡 5. 意思決定（Act）
+- 仕様策定時は表示のみ想定だったが、削除と編集の最小機能も追加してより実用的にした
+
+## 🚧 6. 課題・リスク・次アクション
+- 次アクション: UI文言の再校正とアクセシビリティの簡易チェックをレビュー依頼
+- リスク: XSS対策は最小限（同期ストレージのため同時編集非対応）
+- フォローアップ: 
+  - [ ] 入力バリデーションとXSS対策の強化
+  - [ ] UIのアクセシビリティ改善（ラベル/フォーカス順）
+
+## Reviewer Checklist（推奨観点）
+- [ ] 仕様とUIの齟齬がないか
+- [ ] localStorage のキー設計/初期化適切性
 - [ ] 主要操作（追加/編集/削除/永続化）の動作確認
 - [ ] 文言/アクセシビリティの観点
+
+関連: #19
 \```
 
-## 📣 Issue へのPR通知コメント例
+## 📣 Issue へのPR通知コメント例（AON形式）
 
 \```
-🎉 PR を作成しました: <pr-url>
+# Agent Ops Note (AON)
+- **Task:** Issue #${ISSUE_NUMBER} PR作成通知 / Agent / $(date +"%Y-%m-%d %H:%M")
+- **TL;DR:** Issue対応完了 → PR作成・リンク提供 → レビュー依頼
+
+## 🎯 1. コンテキスト & 目的
+- Issue #${ISSUE_NUMBER} の対応PR作成完了
 
-## 📋 AAR
-- 🎯 目的: Issue #${ISSUE_NUMBER} の対応PR作成
-- ✅ 実施: ブランチ(<branch-name>)作成・コミット/プッシュ・PR作成
-- ▶️ 次のアクション: レビューをお願いします
+## 🔧 3. 実行内容（Do）
+- ブランチ: <branch-name> 作成・コミット/プッシュ
+- PR作成: <pr-url>
 
-- ブランチ: <branch-url>
-- 比較: <compare-url>
-- 最新コミット: <short-sha>
+## ✅ 4. 成果 & 検証（Check）
+- 成果物:
+  - PR: <pr-url>
+  - ブランチ: <branch-url>
+  - 比較: <compare-url>
+  - 最新コミット: <short-sha>
+
+## 🚧 6. 課題・リスク・次アクション
+- 次アクション: レビューをお願いします
+
+🎉 PR を作成しました: <pr-url>
 \```
 
-> メモ: 本ワークフローでは `response.md` を `${GITHUB_WORKSPACE}/response.md` に生成し、必要に応じてPR本文の「Details」として取り込む運用を推奨します。
+> メモ: 本ワークフローでは `response.md` を `${GITHUB_WORKSPACE}/response.md` に生成し、AON形式でのレポート内容をPR本文として活用する運用を推奨します。
diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index 12875fe..861d0d6 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -2,9 +2,7 @@ name: '🏷️ Gemini Automated Issue Triage'
 
 on:
   issues:
-    types:
-      - 'opened'
-      - 'reopened'
+    types: [opened, reopened]
   workflow_dispatch:
     inputs:
       issue_number:
@@ -12,304 +10,110 @@ on:
         required: true
         type: 'number'
 
-concurrency:
-  group: '${{ github.workflow }}-${{ github.event.issue.number || github.event.inputs.issue_number }}'
-  cancel-in-progress: true
-
-defaults:
-  run:
-    shell: 'bash'
-
 permissions:
-  contents: 'read'
-  id-token: 'write'
-  issues: 'write'
-  statuses: 'write'
+  contents: read
+  issues: write
+  id-token: write
 
 jobs:
-  triage-issue:
-    if: |-
-      github.event_name == 'issues' ||
-      github.event_name == 'workflow_dispatch' ||
-      (
-        github.event_name == 'issue_comment' &&
-        contains(github.event.comment.body, '@gemini-cli /triage') &&
-        contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association)
-      )
-    timeout-minutes: 5
-    runs-on: 'ubuntu-latest'
+  triage:
+    runs-on: ubuntu-latest
     steps:
-      - name: 'Checkout repository'
-        uses: 'actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683' # ratchet:actions/checkout@v4
-
-      - name: 'Generate GitHub App Token'
-        id: 'generate_token'
-        if: |-
-          ${{ vars.APP_ID }}
-        uses: 'actions/create-github-app-token@df432ceedc7162793a195dd1713ff69aefc7379e' # ratchet:actions/create-github-app-token@v2
-        with:
-          app-id: '${{ vars.APP_ID }}'
-          private-key: '${{ secrets.APP_PRIVATE_KEY }}'
-
-      - name: 'Get Issue Information'
-        id: 'get_issue'
-        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+      - name: 'Get Issue Info'
+        id: issue
+        env:
+          INPUT_ISSUE_NUMBER: ${{ github.event.inputs.issue_number }}
+        uses: actions/github-script@v7
         with:
-          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           script: |
-            let issueNumber, issueTitle, issueBody;
-            
+            let issue;
             if (context.eventName === 'workflow_dispatch') {
-              // 手動実行の場合はinputから取得
-              issueNumber = parseInt('${{ github.event.inputs.issue_number }}');
-              console.log(`Manual dispatch for issue #${issueNumber}`);
-              
-              // APIでissue情報を取得
-              const { data: issue } = await github.rest.issues.get({
+              const issueNumber = parseInt(process.env.INPUT_ISSUE_NUMBER);
+              const { data } = await github.rest.issues.get({
                 owner: context.repo.owner,
                 repo: context.repo.repo,
                 issue_number: issueNumber
               });
-              
-              issueTitle = issue.title;
-              issueBody = issue.body || '';
+              issue = data;
             } else {
-              // 通常のイベントの場合
-              issueNumber = context.payload.issue.number;
-              issueTitle = context.payload.issue.title;
-              issueBody = context.payload.issue.body || '';
+              issue = context.payload.issue;
             }
             
-            console.log(`Event name: ${context.eventName}`);
-            console.log(`Issue number: ${issueNumber}`);
-            console.log(`Issue title: '${issueTitle}'`);
-            console.log(`Issue body length: ${issueBody.length}`);
-            console.log(`Issue body preview: '${issueBody.substring(0, 200)}${issueBody.length > 200 ? '...' : ''}'`);
-            
-            // 後続のステップで使用するために出力
-            core.setOutput('issue_number', issueNumber);
-            core.setOutput('issue_title', issueTitle);
-            core.setOutput('issue_body', issueBody);
+            core.setOutput('number', issue.number);
+            core.setOutput('title', issue.title);
+            core.setOutput('body', issue.body || '');
 
-      - name: 'Get Repository Labels'
-        id: 'get_labels'
-        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+      - name: 'Get Labels'
+        id: labels
+        uses: actions/github-script@v7
         with:
-          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          script: |-
+          script: |
             const labels = await github.paginate(github.rest.issues.listLabelsForRepo, {
               owner: context.repo.owner,
-              repo: context.repo.repo,
-              per_page: 100,
+              repo: context.repo.repo
             });
-            const labelNames = labels.map(label => label.name).filter(Boolean);
-            core.setOutput('available_labels', labelNames.join(','));
-            core.info(`Found ${labelNames.length} labels: ${labelNames.join(', ')}`);
+            const labelNames = labels.map(l => l.name).join(', ');
+            core.setOutput('available', labelNames);
             return labelNames;
 
-      - name: 'Run Gemini Issue Analysis'
-        uses: 'google-github-actions/run-gemini-cli@v0'
-        id: 'gemini_issue_analysis'
+      - name: 'Analyze with Gemini'
+        uses: google-github-actions/run-gemini-cli@v0
+        id: gemini
         env:
-          GITHUB_TOKEN: '' # Do not pass any auth token here since this runs on untrusted inputs
-          ISSUE_TITLE: '${{ steps.get_issue.outputs.issue_title }}'
-          ISSUE_BODY: '${{ steps.get_issue.outputs.issue_body }}'
-          ISSUE_NUMBER: '${{ steps.get_issue.outputs.issue_number }}'
-          REPOSITORY: '${{ github.repository }}'
-          AVAILABLE_LABELS: '${{ steps.get_labels.outputs.available_labels }}'
+          ISSUE_TITLE: ${{ steps.issue.outputs.title }}
+          ISSUE_BODY: ${{ steps.issue.outputs.body }}
+          AVAILABLE_LABELS: ${{ steps.labels.outputs.available }}
         with:
-          gemini_cli_version: '${{ vars.GEMINI_CLI_VERSION }}'
-          gcp_workload_identity_provider: '${{ vars.GCP_WIF_PROVIDER }}'
-          gcp_project_id: '${{ vars.GOOGLE_CLOUD_PROJECT }}'
-          gcp_location: '${{ vars.GOOGLE_CLOUD_LOCATION }}'
-          gcp_service_account: '${{ vars.SERVICE_ACCOUNT_EMAIL }}'
-          gemini_api_key: '${{ secrets.GEMINI_API_KEY }}'
-          use_vertex_ai: '${{ vars.GOOGLE_GENAI_USE_VERTEXAI }}'
-          use_gemini_code_assist: '${{ vars.GOOGLE_GENAI_USE_GCA }}'
-          settings: |-
-            {
-              "debug": true,
-              "maxSessionTurns": 25,
-              "coreTools": [],
-              "telemetry": {
-                "enabled": false,
-                "target": "gcp"
-              }
-            }
-          prompt: |-
-            You are an issue triage assistant. Analyze the GitHub issue and suggest appropriate labels.
-
-            Repository: ${REPOSITORY}
-            Issue Number: ${ISSUE_NUMBER}
-            Issue Title: "${ISSUE_TITLE}"
-            Issue Body: "${ISSUE_BODY}"
+          gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
+          prompt: |
+            Issue Title: ${ISSUE_TITLE}
+            Issue Body: ${ISSUE_BODY}
             Available Labels: ${AVAILABLE_LABELS}
-
-            Please analyze this issue carefully and suggest appropriate labels from the available labels list.
             
-            Important: Respond with ONLY the JSON object, no additional text or explanations before or after.
-
-            Constraints:
-            - Do NOT run any shell or external commands; use only the provided environment variables
-            - Do NOT attempt to execute `gh label list` or call the GitHub API to fetch labels. The available labels are already provided in "${AVAILABLE_LABELS}".
-
-            Output format (JSON only):
-            {"labels_to_set": ["label1", "label2"], "explanation": "reasoning for these labels"}
-
-            If the issue content appears to be empty or placeholder text, still try to categorize it based on any available information.
+            Select appropriate labels for this GitHub issue. Use this XML format:
+            <labels>
+            <label>example</label>
+            <label>kind/task</label>
+            </labels>
 
-      - name: 'Apply Labels to Issue'
-        if: |-
-          ${{ steps.gemini_issue_analysis.outputs.summary != '' }}
+      - name: 'Apply Labels'
         env:
-          REPOSITORY: '${{ github.repository }}'
-          ISSUE_NUMBER: '${{ steps.get_issue.outputs.issue_number }}'
-          LABELS_OUTPUT: '${{ steps.gemini_issue_analysis.outputs.summary }}'
-        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+          GEMINI_OUTPUT: ${{ steps.gemini.outputs.summary }}
+          ISSUE_NUMBER: ${{ steps.issue.outputs.number }}
+        uses: actions/github-script@v7
         with:
-          github-token: '${{ secrets.GH_PAT || steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          script: |-
-            // Strip code block markers if present and extract JSON
-            const rawLabels = process.env.LABELS_OUTPUT;
-            core.info(`Raw labels output: ${rawLabels}`);
-            
-            let parsedLabels;
-            try {
-              // 改良されたJSON抽出ロジック
-              let jsonString = rawLabels;
-              
-              // 1. \```json \``` ブロックを抽出
-              const jsonBlockMatch = jsonString.match(/\```json\s*([\s\S]*?)\s*\```/);
-              if (jsonBlockMatch) {
-                jsonString = jsonBlockMatch[1].trim();
-                core.info(`Extracted JSON from json code block: ${jsonString}`);
-              } else {
-                // 2. \``` \``` ブロックを抽出（json指定なし）
-                const codeBlockMatch = jsonString.match(/\```\s*([\s\S]*?)\s*\```/);
-                if (codeBlockMatch) {
-                  jsonString = codeBlockMatch[1].trim();
-                  core.info(`Extracted JSON from code block: ${jsonString}`);
-                } else {
-                  // 3. { で始まって } で終わる部分を抽出
-                  const jsonObjectMatch = jsonString.match(/(\{[\s\S]*\})/);
-                  if (jsonObjectMatch) {
-                    jsonString = jsonObjectMatch[1].trim();
-                    core.info(`Extracted JSON object: ${jsonString}`);
-                  } else {
-                    // 4. [ で始まって ] で終わる部分を抽出（配列の場合）
-                    const jsonArrayMatch = jsonString.match(/(\[[\s\S]*\])/);
-                    if (jsonArrayMatch) {
-                      // 配列が返された場合は、最初の要素を使用（単一issue用）
-                      const arrayData = JSON.parse(jsonArrayMatch[1].trim());
-                      if (Array.isArray(arrayData) && arrayData.length > 0) {
-                        // 現在のissue番号に一致するものを探す
-                        const currentIssueNumber = parseInt(process.env.ISSUE_NUMBER);
-                        const matchingIssue = arrayData.find(item => item.issue_number === currentIssueNumber);
-                        if (matchingIssue) {
-                          parsedLabels = {
-                            labels_to_set: matchingIssue.labels_to_set,
-                            explanation: matchingIssue.explanation
-                          };
-                        } else {
-                          // 一致するissue番号がない場合は最初の要素を使用
-                          const firstItem = arrayData[0];
-                          parsedLabels = {
-                            labels_to_set: firstItem.labels_to_set,
-                            explanation: firstItem.explanation
-                          };
-                        }
-                        core.info(`Successfully parsed from array: ${JSON.stringify(parsedLabels)}`);
-                      }
-                    } else {
-                      // 5. フォールバック: そのままパース
-                      core.info(`Using fallback - trying to parse as-is`);
-                    }
-                  }
-                }
-              }
-              
-              // まだparsedLabelsが設定されていない場合、通常のJSONパースを試行
-              if (!parsedLabels) {
-                parsedLabels = JSON.parse(jsonString);
-                core.info(`Successfully parsed labels JSON: ${JSON.stringify(parsedLabels)}`);
-              }
-            } catch (err) {
-              core.setFailed(`Failed to parse labels JSON from Gemini output: ${err.message}\nRaw output: ${rawLabels}`);
-              return;
-            }
-
+          script: |
+            const output = process.env.GEMINI_OUTPUT;
             const issueNumber = parseInt(process.env.ISSUE_NUMBER);
-
-            // Track available labels and allow auto-create of missing labels using GH_PAT
-            const available = new Set(
-              (process.env.AVAILABLE_LABELS || '')
-                .split(',')
-                .map(s => s.trim())
-                .filter(Boolean)
-            );
-
-            // Set labels based on triage result
-            if (parsedLabels.labels_to_set && parsedLabels.labels_to_set.length > 0) {
-              const proposed = [...new Set(parsedLabels.labels_to_set.map(s => String(s).trim()).filter(Boolean))];
-
-              // Attempt to create any missing labels using the provided token
-              for (const label of proposed) {
-                if (available.has(label)) continue;
-                try {
-                  await github.rest.issues.createLabel({
-                    owner: context.repo.owner,
-                    repo: context.repo.repo,
-                    name: label,
-                    color: 'ededed',
-                    description: 'Auto-created by Gemini triage'
-                  });
-                  core.info(`Created missing label: ${label}`);
-                  available.add(label);
-                } catch (err) {
-                  // Ignore if already exists (422), otherwise log error and continue
-                  const status = err?.status || err?.response?.status;
-                  if (status === 422) {
-                    core.info(`Label already exists (race): ${label}`);
-                    available.add(label);
-                  } else {
-                    core.error(`Failed to create label '${label}': ${err}`);
-                  }
-                }
-              }
-
-              const finalLabels = proposed.filter(l => available.has(l));
-              if (finalLabels.length === 0) {
-                const explanation = parsedLabels.explanation ? ` - ${parsedLabels.explanation}` : '';
-                core.info(`No applicable labels for #${issueNumber} after creation attempts. Skipping.${explanation}`);
-              } else {
-                await github.rest.issues.addLabels({
-                  owner: context.repo.owner,
-                  repo: context.repo.repo,
-                  issue_number: issueNumber,
-                  labels: finalLabels
-                });
-                const explanation = parsedLabels.explanation ? ` - ${parsedLabels.explanation}` : '';
-                core.info(`Applied labels for #${issueNumber}: ${finalLabels.join(', ')}${explanation}`);
-              }
+            
+            console.log('Gemini output:', output);
+            
+            let labels = [];
+            
+            // XMLタグから正規表現でラベルを抽出
+            const labelMatches = output.match(/<label>(.*?)<\/label>/g);
+            if (labelMatches) {
+              labels = labelMatches.map(match => 
+                match.replace(/<\/?label>/g, '').trim()
+              ).filter(label => label.length > 0);
+              console.log('Extracted labels from XML:', labels);
             } else {
-              // If no labels to set, leave the issue as is
-              const explanation = parsedLabels.explanation ? ` - ${parsedLabels.explanation}` : '';
-              core.info(`No labels to set for #${issueNumber}, leaving as is${explanation}`);
+              console.log('No XML labels found, using fallback');
+            }
+            
+            // フォールバック: needs-triage のみ
+            if (labels.length === 0) {
+              console.log('No labels extracted, applying needs-triage');
+              labels = ['needs-triage'];
+            }
+            
+            // ラベル適用
+            if (labels.length > 0) {
+              await github.rest.issues.addLabels({
+                owner: context.repo.owner,
+                repo: context.repo.repo,
+                issue_number: issueNumber,
+                labels: labels
+              });
+              console.log(`Applied labels: ${labels.join(', ')}`);
             }
-
-      - name: 'Post Issue Analysis Failure Comment'
-        if: |-
-          ${{ failure() && steps.gemini_issue_analysis.outcome == 'failure' }}
-        env:
-          ISSUE_NUMBER: '${{ steps.get_issue.outputs.issue_number }}'
-          RUN_URL: '${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}'
-        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
-        with:
-          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          script: |-
-            github.rest.issues.createComment({
-              owner: context.repo.owner,
-              repo: context.repo.repo,
-              issue_number: parseInt(process.env.ISSUE_NUMBER),
-              body: `There is a problem with the Gemini CLI issue triaging. Please check the [action logs](${process.env.RUN_URL}) for details.`
-            })
```
