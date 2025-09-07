# 💻 Daily Code Changes

## Full Diff

```diff
diff --git a/.github/prompts/gemini-cli_prompt.ja.md b/.github/prompts/gemini-cli_prompt.ja.md
index c21bd48..ad9e315 100644
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
 
@@ -82,3 +91,168 @@ ${USER_REQUEST}
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
+### 詳細AAR（推奨の深掘り項目）
+
+可能な限り、以下も含めて「詳細AAR」を作成してください（取得可能な情報は `gh pr view`/`gh pr diff --stat` で収集）。
+
+- 🧩 コンテキスト: 関連Issue/PR、ブランチ、背景、スコープ外
+- 🧾 変更サマリ: 変更ファイル数、追加/削除行、主要コンポーネント
+- 🛠 実装詳細: ファイル/関数単位の要点、依存関係、設計判断
+- 🧪 検証: 手動/自動テスト観点、再現/確認手順、環境情報
+- ⚠️ リスク/影響: 互換性、パフォーマンス、セキュリティ、既知の制約
+- 🔁 ロールバック: 戻し方、ガード、Feature Flag の有無
+- 🔗 リンク集: 比較URL、コミット、関連Issue、スクショ/デモ
+- 📌 フォローアップ: TODO、別Issue化、監視/計測の計画
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
+## 📋 AAR（概要）
+- 🎯 目的: Issue #${ISSUE_NUMBER} への対応PR
+- ✅ 実施: ブランチ作成・変更のコミット/プッシュ・PR作成
+- 🔍 差異: 競合はなし（あれば解決内容を記載）
+- 💡 学び: 自動PRフローの安定動作を確認
+- ▶️ 次のアクション: レビューとマージのご確認をお願いします
+
+## 🧭 詳細AAR
+- 🧩 コンテキスト: `issue/${ISSUE_NUMBER}/<slug>` → `main` へ。スコープは <対象領域> に限定。
+- 🧾 変更サマリ: `gh pr diff ${ISSUE_NUMBER} --stat` の結果を貼付
+  - 例) 1 file changed, 102 insertions(+), 4 deletions(-)
+- 🛠 実装詳細:
+  - 主要ファイル: `path/to/file`
+  - 主要変更: <要点1/要点2>
+  - 依存: <新規/更新の依存>
+- 🧪 検証: <ブラウザ/環境> で手動確認、必要に応じてテスト追加
+- ⚠️ リスク/影響: <互換/性能/セキュリティ>、既知の制約 <あれば>
+- 🔁 ロールバック: `git revert <sha>`、影響範囲が限定的で安全
+- 🔗 リンク集: PR/比較URL/コミットURL/関連Issue
+- 📌 フォローアップ: <後続タスク> を Issue 化
+
+関連: #${ISSUE_NUMBER}
+\```
+
+※ すべてのコメント・PR本文は日本語で、過度にならない範囲で適切な絵文字を使用してください。
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
+## 🧪 具体例（今回のPR想定: メモアプリの追加）
+
+以下は「feat: ✨ exampleにシンプルなHTMLのメモアプリを作成（Fixes #19, PR #20, from `issue/19/create-memo-app`）」を題材にした詳細AARの記入例です。実際の値は `gh pr view 20`/`gh pr diff 20 --stat` で取得して置き換えてください。
+
+\```
+# ✨ Fixes #19: example にシンプルなHTMLメモアプリを追加
+
+## 📋 AAR（概要）
+- 🎯 目的: example 配下に最小構成のメモアプリを追加し、テンプレ用途の UI/ローカル永続化サンプルを提供する
+- ✅ 実施: `issue/19/create-memo-app` ブランチで `example/index.html` を実装し、PR #20 を作成
+- 🔍 差異: 仕様策定時は表示のみ想定だったが、削除と編集の最小機能も追加
+- 💡 学び: `localStorage` を使うと依存ゼロで常駐不要のデモが作りやすい
+- ▶️ 次のアクション: UI 文言の再校正とアクセシビリティの簡易チェックをレビュー依頼
+
+## 🧭 詳細AAR
+- 🧩 コンテキスト: `issue/19/create-memo-app` → `main`。スコープは `example/` のみ。他パッケージに影響しない。
+- 🧾 変更サマリ:
+  - 1 file changed, 102 insertions(+), 4 deletions(-)
+  - 変更ファイル: `example/index.html`
+- 🛠 実装詳細:
+  - 追加: タイトル/本文入力、保存ボタン、メモ一覧、編集/削除操作、`localStorage` による永続化
+  - 設計: 依存ライブラリなし。バニラ JS + 最小 CSS。ID ベースのデータ構造で簡易管理。
+  - コード: `example/index.html` 内に `<script>` と `<style>` を内包
+- 🧪 検証:
+  - 手動: Chrome/Firefox/Safari で作成/編集/削除/再読込後の持続性を確認
+  - 確認手順: ファイルをローカルで開き、入力→保存→一覧表示→編集→削除→リロード
+- ⚠️ リスク/影響:
+  - 影響範囲はサンプル配下のみ。既存機能への副作用なし
+  - 既知の制約: 同期ストレージのため同時編集は非対応、XSS 対策は最小
+- 🔁 ロールバック: PR リバートまたは `git revert <commit>`。例示コンテンツの削除で完了
+- 🔗 リンク集:
+  - PR: <pr-url>（#20）/ 比較: <compare-url> / 最新コミット: <short-sha>
+  - 関連 Issue: #19
+- 📌 フォローアップ:
+  - [ ] 入力バリデーションと XSS 対策の強化
+  - [ ] UI のアクセシビリティ改善（ラベル/フォーカス順）
+
+## 🔄 Changes
+- 追加/削除行: +102 / -4
+- 変更ファイル
+  - `example/index.html`
+
+## ✅ Reviewer Checklist（推奨観点）
+- [ ] 仕様と UI の齟齬がないか
+- [ ] localStorage のキー設計/初期化/マイグレーション不要性
+- [ ] 主要操作（追加/編集/削除/永続化）の動作確認
+- [ ] 文言/アクセシビリティの観点
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
index c6f115f..1049c1b 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -30,48 +30,62 @@ permissions:
   issues: 'write'
 
 jobs:
+  # gemini-cli:
+  #   # This condition seeks to ensure the action is only run when it is triggered by a trusted user.
+  #   # For private repos, users who have access to the repo are considered trusted.
+  #   # For public repos, users who members, owners, or collaborators are considered trusted.
+  #   if: |-
+  #     github.event_name == 'workflow_dispatch' ||
+  #     (
+  #       github.event_name == 'issues' && github.event.action == 'opened' &&
+  #       contains(github.event.issue.body, '@gemini-cli') &&
+  #       !contains(github.event.issue.body, '@gemini-cli /review') &&
+  #       !contains(github.event.issue.body, '@gemini-cli /triage') &&
+  #       (
+  #         github.event.repository.private == true ||
+  #         contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.issue.author_association)
+  #       )
+  #     ) ||
+  #     (
+  #       (
+  #         github.event_name == 'issue_comment' ||
+  #         github.event_name == 'pull_request_review_comment'
+  #       ) &&
+  #       contains(github.event.comment.body, '@gemini-cli') &&
+  #       !contains(github.event.comment.body, '@gemini-cli /review') &&
+  #       !contains(github.event.comment.body, '@gemini-cli /triage') &&
+  #       (
+  #         github.event.repository.private == true ||
+  #         contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association)
+  #       )
+  #     ) ||
+  #     (
+  #       github.event_name == 'pull_request_review' &&
+  #       contains(github.event.review.body, '@gemini-cli') &&
+  #       !contains(github.event.review.body, '@gemini-cli /review') &&
+  #       !contains(github.event.review.body, '@gemini-cli /triage') &&
+  #       (
+  #         github.event.repository.private == true ||
+  #         contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.review.author_association)
+  #       )
+  #     )
+
   gemini-cli:
-    # This condition seeks to ensure the action is only run when it is triggered by a trusted user.
-    # For private repos, users who have access to the repo are considered trusted.
-    # For public repos, users who members, owners, or collaborators are considered trusted.
+    # 一時的にシンプルな条件に変更してテスト
     if: |-
-      github.event_name == 'workflow_dispatch' ||
-      (
-        github.event_name == 'issues' && github.event.action == 'opened' &&
-        contains(github.event.issue.body, '@gemini-cli') &&
-        !contains(github.event.issue.body, '@gemini-cli /review') &&
-        !contains(github.event.issue.body, '@gemini-cli /triage') &&
-        (
-          github.event.repository.private == true ||
-          contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.issue.author_association)
-        )
-      ) ||
-      (
-        (
-          github.event_name == 'issue_comment' ||
-          github.event_name == 'pull_request_review_comment'
-        ) &&
-        contains(github.event.comment.body, '@gemini-cli') &&
-        !contains(github.event.comment.body, '@gemini-cli /review') &&
-        !contains(github.event.comment.body, '@gemini-cli /triage') &&
-        (
-          github.event.repository.private == true ||
-          contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.comment.author_association)
-        )
-      ) ||
-      (
-        github.event_name == 'pull_request_review' &&
-        contains(github.event.review.body, '@gemini-cli') &&
-        !contains(github.event.review.body, '@gemini-cli /review') &&
-        !contains(github.event.review.body, '@gemini-cli /triage') &&
-        (
-          github.event.repository.private == true ||
-          contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'), github.event.review.author_association)
-        )
-      )
-    timeout-minutes: 10
+      github.event_name == 'issues' && github.event.action == 'opened' &&
+      contains(github.event.issue.body, '@gemini-cli')
+
+          timeout-minutes: 10
     runs-on: 'ubuntu-latest'
     steps:
+      - name: 'Debug Event Information'
+        run: |-
+          echo "Event Name: ${{ github.event_name }}"
+          echo "Event Action: ${{ github.event.action }}"
+          echo "Issue Author: ${{ github.event.issue.user.login }}"
+          echo "Author Association: ${{ github.event.issue.author_association }}"
+
       - name: 'Generate GitHub App Token'
         id: 'generate_token'
         if: |-
@@ -113,13 +127,18 @@ jobs:
           fi
 
           # Clean up user request
-          USER_REQUEST=$(echo "${USER_REQUEST}" | sed 's/.*@gemini-cli//' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
-
+          CLEANED_USER_REQUEST=$(echo "${USER_REQUEST}" | sed 's/.*@gemini-cli//' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
+          
+          # ⬇⬇⬇ ここからが修正箇所 ⬇⬇⬇
+          # GITHUB_OUTPUTへの書き込みをヒアドキュメント形式に変更して、特殊文字によるエラーを回避
           {
-            echo "user_request=${USER_REQUEST}"
+            echo 'user_request<<EOF'
+            echo "${CLEANED_USER_REQUEST}"
+            echo 'EOF'
             echo "issue_number=${ISSUE_NUMBER}"
             echo "is_pr=${IS_PR}"
           } >> "${GITHUB_OUTPUT}"
+          # ⬆⬆⬆ ここまでが修正箇所 ⬆⬆⬆
 
       - name: 'Set up git user for commits'
         run: |-
diff --git a/.github/workflows/gemini-issue-automated-triage.yml b/.github/workflows/gemini-issue-automated-triage.yml
index bc76c52..12875fe 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -97,11 +97,12 @@ jobs:
         with:
           github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           script: |-
-            const { data: labels } = await github.rest.issues.listLabelsForRepo({
+            const labels = await github.paginate(github.rest.issues.listLabelsForRepo, {
               owner: context.repo.owner,
               repo: context.repo.repo,
+              per_page: 100,
             });
-            const labelNames = labels.map(label => label.name);
+            const labelNames = labels.map(label => label.name).filter(Boolean);
             core.setOutput('available_labels', labelNames.join(','));
             core.info(`Found ${labelNames.length} labels: ${labelNames.join(', ')}`);
             return labelNames;
@@ -166,7 +167,7 @@ jobs:
           LABELS_OUTPUT: '${{ steps.gemini_issue_analysis.outputs.summary }}'
         uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
         with:
-          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          github-token: '${{ secrets.GH_PAT || steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           script: |-
             // Strip code block markers if present and extract JSON
             const rawLabels = process.env.LABELS_OUTPUT;
@@ -239,16 +240,57 @@ jobs:
 
             const issueNumber = parseInt(process.env.ISSUE_NUMBER);
 
+            // Track available labels and allow auto-create of missing labels using GH_PAT
+            const available = new Set(
+              (process.env.AVAILABLE_LABELS || '')
+                .split(',')
+                .map(s => s.trim())
+                .filter(Boolean)
+            );
+
             // Set labels based on triage result
             if (parsedLabels.labels_to_set && parsedLabels.labels_to_set.length > 0) {
-              await github.rest.issues.setLabels({
-                owner: context.repo.owner,
-                repo: context.repo.repo,
-                issue_number: issueNumber,
-                labels: parsedLabels.labels_to_set
-              });
-              const explanation = parsedLabels.explanation ? ` - ${parsedLabels.explanation}` : '';
-              core.info(`Successfully set labels for #${issueNumber}: ${parsedLabels.labels_to_set.join(', ')}${explanation}`);
+              const proposed = [...new Set(parsedLabels.labels_to_set.map(s => String(s).trim()).filter(Boolean))];
+
+              // Attempt to create any missing labels using the provided token
+              for (const label of proposed) {
+                if (available.has(label)) continue;
+                try {
+                  await github.rest.issues.createLabel({
+                    owner: context.repo.owner,
+                    repo: context.repo.repo,
+                    name: label,
+                    color: 'ededed',
+                    description: 'Auto-created by Gemini triage'
+                  });
+                  core.info(`Created missing label: ${label}`);
+                  available.add(label);
+                } catch (err) {
+                  // Ignore if already exists (422), otherwise log error and continue
+                  const status = err?.status || err?.response?.status;
+                  if (status === 422) {
+                    core.info(`Label already exists (race): ${label}`);
+                    available.add(label);
+                  } else {
+                    core.error(`Failed to create label '${label}': ${err}`);
+                  }
+                }
+              }
+
+              const finalLabels = proposed.filter(l => available.has(l));
+              if (finalLabels.length === 0) {
+                const explanation = parsedLabels.explanation ? ` - ${parsedLabels.explanation}` : '';
+                core.info(`No applicable labels for #${issueNumber} after creation attempts. Skipping.${explanation}`);
+              } else {
+                await github.rest.issues.addLabels({
+                  owner: context.repo.owner,
+                  repo: context.repo.repo,
+                  issue_number: issueNumber,
+                  labels: finalLabels
+                });
+                const explanation = parsedLabels.explanation ? ` - ${parsedLabels.explanation}` : '';
+                core.info(`Applied labels for #${issueNumber}: ${finalLabels.join(', ')}${explanation}`);
+              }
             } else {
               // If no labels to set, leave the issue as is
               const explanation = parsedLabels.explanation ? ` - ${parsedLabels.explanation}` : '';
diff --git a/.github/workflows/gemini-issue-scheduled-triage.yml b/.github/workflows/gemini-issue-scheduled-triage.yml
index aacbbe4..340296b 100644
--- a/.github/workflows/gemini-issue-scheduled-triage.yml
+++ b/.github/workflows/gemini-issue-scheduled-triage.yml
@@ -38,29 +38,35 @@ jobs:
 
       - name: 'Find untriaged issues'
         id: 'find_issues'
-        env:
-          GITHUB_TOKEN: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
-          GITHUB_REPOSITORY: '${{ github.repository }}'
-          GITHUB_OUTPUT: '${{ github.output }}'
-        run: |-
-          set -euo pipefail
-
-          echo '🔍 Finding issues without labels...'
-          NO_LABEL_ISSUES="$(gh issue list --repo "${GITHUB_REPOSITORY}" \
-            --search 'is:open is:issue no:label' --json number,title,body)"
-
-          echo '🏷️ Finding issues that need triage...'
-          NEED_TRIAGE_ISSUES="$(gh issue list --repo "${GITHUB_REPOSITORY}" \
-            --search 'is:open is:issue label:"status/needs-triage"' --json number,title,body)"
+        uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
+        with:
+          github-token: '${{ secrets.GH_PAT || steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          script: |-
+            const owner = context.repo.owner;
+            const repo = context.repo.repo;
 
-          echo '🔄 Merging and deduplicating issues...'
-          ISSUES="$(echo "${NO_LABEL_ISSUES}" "${NEED_TRIAGE_ISSUES}" | jq -c -s 'add | unique_by(.number)')"
+            // Fetch all open issues with pagination
+            const allOpen = await github.paginate(github.rest.issues.listForRepo, {
+              owner,
+              repo,
+              state: 'open',
+              per_page: 100,
+            });
 
-          echo '📝 Setting output for GitHub Actions...'
-          echo "issues_to_triage=${ISSUES}" >> "${GITHUB_OUTPUT}"
+            const candidates = [];
+            for (const it of allOpen) {
+              // Skip pull requests
+              if (it.pull_request) continue;
+              const labels = (it.labels || []).map(l => typeof l === 'string' ? l : l.name).filter(Boolean);
+              const hasNeedsTriage = labels.includes('status/needs-triage');
+              const hasNoLabels = labels.length === 0;
+              if (hasNoLabels || hasNeedsTriage) {
+                candidates.push({ number: it.number, title: it.title || '', body: it.body || '' });
+              }
+            }
 
-          ISSUE_COUNT="$(echo "${ISSUES}" | jq 'length')"
-          echo "✅ Found ${ISSUE_COUNT} issues to triage! 🎯"
+            core.info(`✅ Found ${candidates.length} issues to triage: ${candidates.map(i => '#' + i.number).join(', ')}`);
+            core.setOutput('issues_to_triage', JSON.stringify(candidates));
 
       - name: 'Get Repository Labels'
         id: 'get_labels'
@@ -68,11 +74,12 @@ jobs:
         with:
           github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           script: |-
-            const { data: labels } = await github.rest.issues.listLabelsForRepo({
+            const labels = await github.paginate(github.rest.issues.listLabelsForRepo, {
               owner: context.repo.owner,
               repo: context.repo.repo,
+              per_page: 100,
             });
-            const labelNames = labels.map(label => label.name);
+            const labelNames = labels.map(label => label.name).filter(Boolean);
             core.setOutput('available_labels', labelNames.join(','));
             core.info(`Found ${labelNames.length} labels: ${labelNames.join(', ')}`);
             return labelNames;
@@ -109,42 +116,38 @@ jobs:
           prompt: |-
             ## Role
 
-            You are an issue triage assistant. Analyze the GitHub issues and
-            identify the most appropriate existing labels to apply.
+            You are an issue triage assistant. Analyze ONLY the provided GitHub issues
+            and pick appropriate labels from the available labels list.
 
-            ## Steps
+            ## Inputs
+            - Available labels: "${{ env.AVAILABLE_LABELS }}"
+            - Candidate issues (JSON array): "${{ env.ISSUES_TO_TRIAGE }}"
 
-            1. Review the available labels in the environment variable: "${AVAILABLE_LABELS}".
-            2. Review the issues in the environment variable: "${ISSUES_TO_TRIAGE}".
-            3. For each issue, classify it by the appropriate labels from the available labels.
-            4. Output a JSON array of objects, each containing the issue number,
-               the labels to set, and a brief explanation. For example:
-               \```
+            ## Critical rules
+            - Output MUST be a JSON array.
+            - Every object MUST have an `issue_number` that appears in "${ISSUES_TO_TRIAGE}".
+            - Never include any issue numbers that are not in "${ISSUES_TO_TRIAGE}".
+            - If there is exactly one candidate, output exactly one object for that issue.
+            - Only choose labels from "${AVAILABLE_LABELS}".
+
+            ## Steps
+            1. Read the candidate issues from "${{ env.ISSUES_TO_TRIAGE }}".
+            2. For each candidate, select one or more labels from "${{ env.AVAILABLE_LABELS }}".
+            3. Return a JSON array with objects like:
+               \```json
                [
                  {
                    "issue_number": 123,
                    "labels_to_set": ["kind/bug", "priority/p2"],
-                   "explanation": "This is a bug report with high priority based on the error description"
-                 },
-                 {
-                   "issue_number": 456,
-                   "labels_to_set": ["kind/enhancement"],
-                   "explanation": "This is a feature request for improving the UI"
+                   "explanation": "Brief reason"
                  }
                ]
                \```
-            5. If an issue cannot be classified, do not include it in the output array.
 
-            ## Guidelines
-
-            - Only use labels that already exist in the repository
-            - Assign all applicable labels based on the issue content
-            - Reference all shell variables as "${VAR}" (with quotes and braces)
-            - Do NOT run any shell or external commands; use only the provided environment variables
-            - Do NOT attempt to execute `gh label list` or call the GitHub API to fetch labels. The full list of labels is provided in "${AVAILABLE_LABELS}".
-            - Do NOT attempt to list or fetch issues yourself. The issues to triage are provided in "${ISSUES_TO_TRIAGE}".
-            - Output only valid JSON format
-            - Do not include any explanation or additional text, just the JSON
+            ## Constraints
+            - Reference variables exactly as shown; do NOT execute any shell commands.
+            - Do NOT fetch labels or issues yourself; use the inputs above.
+            - Output only valid JSON. Do not write any additional text.
 
       - name: 'Apply Labels to Issues'
         if: |-
@@ -153,15 +156,18 @@ jobs:
         env:
           REPOSITORY: '${{ github.repository }}'
           LABELS_OUTPUT: '${{ steps.gemini_issue_analysis.outputs.summary }}'
+          AVAILABLE_LABELS: '${{ steps.get_labels.outputs.available_labels }}'
+          ISSUES_TO_TRIAGE: '${{ steps.find_issues.outputs.issues_to_triage }}'
         uses: 'actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea'
         with:
-          github-token: '${{ steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
+          github-token: '${{ secrets.GH_PAT || steps.generate_token.outputs.token || secrets.GITHUB_TOKEN }}'
           script: |-
             // Hardened JSON extraction to tolerate extra text
             const rawLabels = process.env.LABELS_OUTPUT || '';
             core.info(`Raw labels JSON: ${rawLabels}`);
 
             let parsedLabels;
+            let parseError = false;
             try {
               let jsonString = rawLabels;
 
@@ -189,10 +195,31 @@ jobs:
               }
               core.info(`Parsed labels JSON entries: ${parsedLabels.length}`);
             } catch (err) {
-              core.setFailed(`Failed to parse labels JSON from Gemini output: ${err.message}\nRaw output: ${rawLabels}`);
-              return;
+              core.warning(`Failed to parse labels JSON from Gemini output: ${err.message}. Will attempt fallback.\nRaw output: ${rawLabels}`);
+              parsedLabels = [];
+              parseError = true;
             }
 
+            // Build a set of existing labels, and auto-create missing ones using GH_PAT
+            const available = new Set(
+              (process.env.AVAILABLE_LABELS || '')
+                .split(',')
+                .map(s => s.trim())
+                .filter(Boolean)
+            );
+            core.info(`Available labels (enforced): ${[...available].join(', ')}`);
+
+            // Build a set of candidate issue numbers to enforce scope
+            let candidates = [];
+            try {
+              candidates = JSON.parse(process.env.ISSUES_TO_TRIAGE || '[]');
+            } catch {}
+            const allowed = new Set(candidates.map(c => Number(c.number)).filter(n => Number.isInteger(n)));
+            core.info(`Will only apply to candidate issues: ${[...allowed].map(n => '#' + n).join(', ')}`);
+
+            let appliedCount = 0;
+            const ignoredNonCandidates = [];
+
             for (const entry of parsedLabels) {
               const issueNumber = entry.issue_number;
               if (!issueNumber) {
@@ -200,18 +227,98 @@ jobs:
                 continue;
               }
 
+              if (!allowed.has(Number(issueNumber))) {
+                ignoredNonCandidates.push(Number(issueNumber));
+                continue;
+              }
+
               // Set labels based on triage result
               if (entry.labels_to_set && entry.labels_to_set.length > 0) {
-                await github.rest.issues.setLabels({
-                  owner: context.repo.owner,
-                  repo: context.repo.repo,
-                  issue_number: issueNumber,
-                  labels: entry.labels_to_set
-                });
-                const explanation = entry.explanation ? ` - ${entry.explanation}` : '';
-                core.info(`Successfully set labels for #${issueNumber}: ${entry.labels_to_set.join(', ')}${explanation}`);
+                const proposed = [...new Set(entry.labels_to_set.map(s => String(s).trim()).filter(Boolean))];
+
+                // Create any missing labels first
+                for (const label of proposed) {
+                  if (available.has(label)) continue;
+                  try {
+                    await github.rest.issues.createLabel({
+                      owner: context.repo.owner,
+                      repo: context.repo.repo,
+                      name: label,
+                      color: 'ededed',
+                      description: 'Auto-created by Gemini triage'
+                    });
+                    core.info(`Created missing label: ${label}`);
+                    available.add(label);
+                  } catch (err) {
+                    const status = err?.status || err?.response?.status;
+                    if (status === 422) {
+                      core.info(`Label already exists (race): ${label}`);
+                      available.add(label);
+                    } else {
+                      core.error(`Failed to create label '${label}': ${err}`);
+                    }
+                  }
+                }
+
+                const finalLabels = proposed.filter(l => available.has(l));
+                if (finalLabels.length === 0) {
+                  core.info(`Skipping #${issueNumber}: no applicable labels after creation attempts [${proposed.join(', ')}]`);
+                  continue;
+                }
+
+                try {
+                  await github.rest.issues.addLabels({
+                    owner: context.repo.owner,
+                    repo: context.repo.repo,
+                    issue_number: issueNumber,
+                    labels: finalLabels
+                  });
+                  const explanation = entry.explanation ? ` - ${entry.explanation}` : '';
+                  core.info(`Applied labels to #${issueNumber}: ${finalLabels.join(', ')}${explanation}`);
+                  appliedCount++;
+                } catch (err) {
+                  core.error(`Failed applying labels to #${issueNumber}: ${err}`);
+                }
               } else {
                 // If no labels to set, leave the issue as is
                 core.info(`No labels to set for #${issueNumber}, leaving as is`);
               }
             }
+
+            if (ignoredNonCandidates.length > 0) {
+              core.info(`Ignored non-candidate issues from model output: ${ignoredNonCandidates.map(n => '#' + n).join(', ')}`);
+            }
+
+            // Fallback: if nothing applied to candidates, add a minimal triage label
+            if ((appliedCount === 0 || parseError) && allowed.size > 0) {
+              const fallbackLabel = 'status/needs-triage';
+              try {
+                if (!available.has(fallbackLabel)) {
+                  await github.rest.issues.createLabel({
+                    owner: context.repo.owner,
+                    repo: context.repo.repo,
+                    name: fallbackLabel,
+                    color: 'ededed',
+                    description: 'Auto-created fallback triage label'
+                  });
+                  available.add(fallbackLabel);
+                  core.info(`Created fallback label: ${fallbackLabel}`);
+                }
+
+                for (const num of allowed) {
+                  try {
+                    await github.rest.issues.addLabels({
+                      owner: context.repo.owner,
+                      repo: context.repo.repo,
+                      issue_number: num,
+                      labels: [fallbackLabel]
+                    });
+                    core.info(`Applied fallback label to #${num}: ${fallbackLabel}`);
+                  } catch (err) {
+                    core.error(`Failed applying fallback label to #${num}: ${err}`);
+                  }
+                }
+              } catch (err) {
+                core.error(`Fallback labeling failed: ${err}`);
+              }
+            }
diff --git a/.github/workflows/gemini-release-notes.yml b/.github/workflows/gemini-release-notes.yml
new file mode 100644
index 0000000..9d95cd6
--- /dev/null
+++ b/.github/workflows/gemini-release-notes.yml
@@ -0,0 +1,163 @@
+name: "📝 Gemini Release Notes"
+
+on:
+  push:
+    tags:
+      - "*"
+
+permissions:
+  contents: write
+
+defaults:
+  run:
+    shell: bash
+
+jobs:
+  release-notes:
+    runs-on: ubuntu-latest
+    timeout-minutes: 5
+    steps:
+      - name: Checkout
+        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # ratchet:actions/checkout@v4
+        with:
+          fetch-depth: 0
+
+      - name: Prepare context
+        id: ctx
+        env:
+          REPOSITORY: "${{ github.repository }}"
+          TAG_NAME: "${{ github.ref_name }}"
+          GITHUB_TOKEN: "${{ secrets.GITHUB_TOKEN }}"
+        run: |
+          set -euo pipefail
+
+          TAG="${TAG_NAME}"
+          git fetch --tags --prune --force >/dev/null 2>&1 || true
+
+          # Try to get previous released tag (from Releases). Fallback to previous git tag reachable from current.
+          PREV_RELEASE_TAG="$(gh release list --limit 100 --json tagName --jq 'map(.tagName) | map(select(. != env.TAG)) | .[0]' || true)"
+          if [[ -z "${PREV_RELEASE_TAG}" || "${PREV_RELEASE_TAG}" == "null" ]]; then
+            PREV_RELEASE_TAG="$(git describe --tags --abbrev=0 "${TAG}^" 2>/dev/null || true)"
+          fi
+
+          BASE_RANGE=""
+          COMPARE_URL=""
+          if [[ -n "${PREV_RELEASE_TAG}" ]]; then
+            BASE_RANGE="${PREV_RELEASE_TAG}..${TAG}"
+            COMPARE_URL="https://github.com/${REPOSITORY}/compare/${PREV_RELEASE_TAG}...${TAG}"
+          else
+            # Initial release: include history up to the tag commit
+            BASE_RANGE="${TAG}"
+          fi
+
+          # Collect data (trim to keep prompt concise)
+          COMMITS="$(git log --no-merges --pretty=format:'- %s (%h) by %an' ${BASE_RANGE} | head -n 300 || true)"
+          CHANGED_FILES="$( ( [[ -n "${PREV_RELEASE_TAG}" ]] && git diff --name-only ${BASE_RANGE} || git ls-tree -r --name-only HEAD ) | sed 's/^/- /' | head -n 500 || true)"
+          CONTRIBUTORS="$(git log --format='%an' ${BASE_RANGE} | sort -u | sed 's/^/- /' | head -n 200 || true)"
+
+          {
+            echo "tag=${TAG}"
+            echo "prev_tag=${PREV_RELEASE_TAG}"
+            echo "compare_url=${COMPARE_URL}"
+            echo 'commits<<EOF'
+            echo "${COMMITS}"
+            echo 'EOF'
+            echo 'files<<EOF'
+            echo "${CHANGED_FILES}"
+            echo 'EOF'
+            echo 'contributors<<EOF'
+            echo "${CONTRIBUTORS}"
+            echo 'EOF'
+          } >> "$GITHUB_OUTPUT"
+
+      - name: Generate release notes with Gemini
+        id: gemini
+        uses: google-github-actions/run-gemini-cli@v0
+        env:
+          REPOSITORY: "${{ github.repository }}"
+          TAG_NAME: "${{ steps.ctx.outputs.tag }}"
+          PREV_TAG: "${{ steps.ctx.outputs.prev_tag }}"
+          COMPARE_URL: "${{ steps.ctx.outputs.compare_url }}"
+          COMMITS: "${{ steps.ctx.outputs.commits }}"
+          CHANGED_FILES: "${{ steps.ctx.outputs.files }}"
+          CONTRIBUTORS: "${{ steps.ctx.outputs.contributors }}"
+        with:
+          gemini_api_key: "${{ secrets.GEMINI_API_KEY }}"
+          gcp_workload_identity_provider: "${{ vars.GCP_WIF_PROVIDER }}"
+          gcp_project_id: "${{ vars.GOOGLE_CLOUD_PROJECT }}"
+          gcp_location: "${{ vars.GOOGLE_CLOUD_LOCATION }}"
+          gcp_service_account: "${{ vars.SERVICE_ACCOUNT_EMAIL }}"
+          use_vertex_ai: "${{ vars.GOOGLE_GENAI_USE_VERTEXAI }}"
+          use_gemini_code_assist: "${{ vars.GOOGLE_GENAI_USE_GCA }}"
+          settings: |
+            { "debug": false, "maxSessionTurns": 10, "telemetry": { "enabled": false, "target": "gcp" } }
+          prompt: |
+            あなたはリリースノート作成のエキスパートです。以下の情報から、日本語で読みやすいMarkdownのリリースノートを作成してください。
+
+            # コンテキスト
+            - リポジトリ: ${{ github.repository }}
+            - リリースタグ: ${{ steps.ctx.outputs.tag }}
+            - 前リリースタグ: ${{ steps.ctx.outputs.prev_tag }}
+            - 比較URL: ${{ steps.ctx.outputs.compare_url }}
+
+            # 変更コミット（抜粋）
+            ${{ steps.ctx.outputs.commits }}
+
+            # 変更ファイル（抜粋）
+            ${{ steps.ctx.outputs.files }}
+
+            # コントリビューター（抜粋）
+            ${{ steps.ctx.outputs.contributors }}
+
+            # 執筆方針
+            - 見出しと箇条書きを用いて簡潔に。
+            - 主な変更点(Highlights)、Breaking Changes（あれば）、改善・修正、貢献者の順でまとめる。
+            - 可能ならConventional Commitsを手掛かりに分類（feat/fix/docs/chore/refactor/perf/test 等）。
+            - コミットメッセージから重大変更を推測できる場合は「Breaking Changes」に明記。
+            - 最後に比較URLを記載。
+            - 出力はMarkdownのみ（余計な前置きや後書き、コードフェンスは不要）。
+
+            # 期待するMarkdownの構成例
+            # ${{ steps.ctx.outputs.tag }} ～このリリースノートの内容が分かるようなタイトル～
+            ## ✨ Highlights
+            - 主要な変更点の要約…
+
+            ## 💥 Breaking Changes
+            - 重大な変更点…（なければこの節は省略可）
+
+            ## 🛠 変更一覧
+            - feat: …
+            - fix: …
+            - docs: …
+            - refactor: …
+            - chore: …
+
+            ## 👥 Contributors
+            - ユーザー名一覧（抜粋）
+
+            ---
+            比較: ${{ steps.ctx.outputs.compare_url }}
+
+      - name: Write notes to file
+        run: |
+          set -euo pipefail
+          # Write without shell interpolation to avoid ${...} expansion issues
+          cat > release_notes.md << 'EOF'
+          ${{ steps.gemini.outputs.summary }}
+          EOF
+          echo "Wrote release_notes.md (size: $(wc -c < release_notes.md) bytes)"
+
+      - name: Create or update GitHub Release
+        env:
+          GITHUB_TOKEN: "${{ secrets.GITHUB_TOKEN }}"
+          TAG: "${{ steps.ctx.outputs.tag }}"
+        run: |
+          set -euo pipefail
+          if gh release view "${TAG}" >/dev/null 2>&1; then
+            gh release edit "${TAG}" --notes-file release_notes.md
+          else
+            # Mark pre-releases automatically if tag contains pre-release identifiers
+            PRERELEASE_FLAG=""
+            if [[ "${TAG}" =~ -(alpha|beta|rc) ]]; then PRERELEASE_FLAG="--prerelease"; fi
+            gh release create "${TAG}" --title "${TAG}" --notes-file release_notes.md ${PRERELEASE_FLAG}
+          fi
diff --git a/.github/workflows/imagen-generate-and-commit.yml b/.github/workflows/imagen-generate-and-commit.yml
new file mode 100644
index 0000000..a1a254c
--- /dev/null
+++ b/.github/workflows/imagen-generate-and-commit.yml
@@ -0,0 +1,153 @@
+name: "🎨 imagen4-commit-via-gemini-cli"
+
+on:
+  workflow_dispatch:
+    inputs:
+      image_prompt:
+        description: '作りたい画像のプロンプト'
+        required: true
+        default: 'A beautiful Japanese landscape with cherry blossoms and mountains'
+      model:
+        description: '画像生成モデル (imagen-4 / imagen-4-ultra / imagen-3)'
+        required: false
+        default: 'imagen-4'
+      num:
+        description: '生成枚数'
+        required: false
+        default: '2'
+      aspect_ratio:
+        description: 'アスペクト比 (例: 1:1, 16:9, 9:16)'
+        required: false
+        default: '1:1'
+      seed:
+        description: 'シード値 (オプション)'
+        required: false
+        default: ''
+
+jobs:
+  generate_and_commit:
+    runs-on: ubuntu-latest
+    
+    permissions:
+      contents: write
+      
+    steps:
+      - name: Checkout repository
+        uses: actions/checkout@v4
+        with:
+          token: ${{ secrets.GITHUB_TOKEN }}
+
+      - name: Create output directory
+        run: |
+          mkdir -p generated-images
+          echo "Created generated-images directory"
+          ls -la
+
+      - name: Generate images via Gemini CLI (+ Imagen MCP)
+        uses: google-github-actions/run-gemini-cli@v0
+        env:
+          NUM: ${{ github.event.inputs.num }}
+          PROMPT: ${{ github.event.inputs.image_prompt }}
+          AR: ${{ github.event.inputs.aspect_ratio }}
+          SEED: ${{ github.event.inputs.seed }}
+        with:
+          gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
+          gemini_model: gemini-2.5-flash
+          gemini_debug: true
+          settings: |
+            {
+              "mcpServers": {
+                "gemini-imagen": {
+                  "command": "npx",
+                  "args": ["-y", "gemini-imagen-mcp-server",
+                           "--output-dir", "generated-images",
+                           "--model", "${{ github.event.inputs.model }}"],
+                  "env": { "GEMINI_API_KEY": "${{ secrets.GEMINI_API_KEY }}" },
+                  "trust": true,
+                  "includeTools": ["generate_image"]
+                }
+              }
+            }
+          prompt: |
+            Use the @gemini-imagen.generate_image tool to generate ${{ github.event.inputs.num }} image(s)
+            from this prompt: "${{ github.event.inputs.image_prompt }}".
+            Use aspect ratio "${{ github.event.inputs.aspect_ratio }}".
+            ${{ github.event.inputs.seed != '' && format('If a seed is provided, use it: "{0}".', github.event.inputs.seed) || '' }}
+            Save files under ./generated-images and list only the filenames.
+
+      - name: Verify generated files
+        run: |
+          set -euo pipefail
+          if [ ! -d generated-images ]; then
+            echo "generated-images not found"; exit 1
+          fi
+          echo "== Generated files =="
+          ls -lh generated-images
+          cnt=$(ls -1 generated-images | wc -l)
+          if [ "$cnt" -lt 1 ]; then
+            echo "No images were generated"; exit 1
+          fi
+          echo "✅ Successfully generated $cnt file(s)"
+
+      - name: Add metadata file
+        run: |
+          cat > generated-images/metadata.json << EOF
+          {
+            "generation_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
+            "prompt": "${{ github.event.inputs.image_prompt }}",
+            "model": "${{ github.event.inputs.model }}",
+            "num_images": ${{ github.event.inputs.num }},
+            "aspect_ratio": "${{ github.event.inputs.aspect_ratio }}",
+            "seed": "${{ github.event.inputs.seed }}",
+            "workflow_run": "${{ github.run_number }}",
+            "commit_sha": "${{ github.sha }}"
+          }
+          EOF
+          echo "Created metadata file:"
+          cat generated-images/metadata.json
+
+      - name: Commit and push generated images
+        run: |
+          git config --local user.email "action@github.com"
+          git config --local user.name "GitHub Action"
+          
+          git add generated-images/
+          
+          if git diff --staged --quiet; then
+            echo "No changes to commit"
+          else
+            git commit -m "🎨 Generate images via Gemini Imagen API
+            
+            Prompt: ${{ github.event.inputs.image_prompt }}
+            Model: ${{ github.event.inputs.model }}
+            Images: ${{ github.event.inputs.num }}
+            Aspect ratio: ${{ github.event.inputs.aspect_ratio }}
+            Seed: ${{ github.event.inputs.seed }}
+            Generated at: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
+            
+            git push
+            echo "✅ Successfully committed and pushed generated images"
+          fi
+
+      - name: Upload generated images as artifacts
+        uses: actions/upload-artifact@v4
+        if: always()
+        with:
+          name: generated-images-${{ github.run_number }}
+          path: generated-images/
+          retention-days: 30
+
+      - name: Create workflow summary
+        run: |
+          echo "## 🎨 Image Generation Summary" >> $GITHUB_STEP_SUMMARY
+          echo "" >> $GITHUB_STEP_SUMMARY
+          echo "**Prompt:** ${{ github.event.inputs.image_prompt }}" >> $GITHUB_STEP_SUMMARY
+          echo "**Model:** ${{ github.event.inputs.model }}" >> $GITHUB_STEP_SUMMARY
+          echo "**Number of Images:** ${{ github.event.inputs.num }}" >> $GITHUB_STEP_SUMMARY
+          echo "**Aspect Ratio:** ${{ github.event.inputs.aspect_ratio }}" >> $GITHUB_STEP_SUMMARY
+          echo "**Seed:** ${{ github.event.inputs.seed || 'Random' }}" >> $GITHUB_STEP_SUMMARY
+          echo "" >> $GITHUB_STEP_SUMMARY
+          echo "### Generated Files" >> $GITHUB_STEP_SUMMARY
+          echo "\`\`\`" >> $GITHUB_STEP_SUMMARY
+          ls -la generated-images/ >> $GITHUB_STEP_SUMMARY
+          echo "\`\`\`" >> $GITHUB_STEP_SUMMARY
diff --git a/README.ja.md b/README.ja.md
deleted file mode 100644
index 56a17a7..0000000
--- a/README.ja.md
+++ /dev/null
@@ -1,171 +0,0 @@
-<div align="center">
-
-# Gemini Actions Lab
-
-<a href="./README.md"><img src="https://img.shields.io/badge/English-Readme-blue?style=for-the-badge&logo=github&logoColor=white" alt="English" /></a>
-<a href="./README.ja.md"><img src="https://img.shields.io/badge/日本語-Readme-red?style=for-the-badge&logo=github&logoColor=white" alt="日本語" /></a>
-
-[![💬 Gemini CLI](https://github.com/Sunwood-ai-labsII/gemini-actions-lab/actions/workflows/gemini-cli.yml/badge.svg)](https://github.com/Sunwood-ai-labsII/gemini-actions-lab/actions/workflows/gemini-cli.yml)
-
-![Image](https://github.com/user-attachments/assets/1e294058-a1e6-4b44-979d-f4c8f09cb8ae)
-
-<img src="https://img.shields.io/badge/GitHub%20Actions-AI-blue?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
-<img src="https://img.shields.io/badge/Gemini-AI-4285F4?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Gemini" />
-</div>
-
----
-
-## 📖 概要
-
-このリポジトリは、GoogleのGemini AIをGitHub Actionsと統合するための実験室およびショーケースとして機能します。生成AIの力を利用して、さまざまなリポジトリ管理タスクを自動化する方法を示します。
-
-### 🎯 主な機能
-- **AIによる自動化**: Geminiを活用して、Issueのトリアージ、プルリクエストのレビューなどのタスクを処理します。
-- **CLIライクな対話**: Issueのコメントから直接AIアシスタントと対話します。
-- **拡張可能なワークフロー**: 独自のプロジェクトに合わせてワークフローを簡単に適応およびカスタマイズできます。
-
----
-
-## 🤖 ワークフロー
-
-このリポジトリには、以下のGitHub Actionsワークフローが含まれています：
-
-### 📄 `gemini-cli-jp.yml`
-- **トリガー**: Issueのコメント
-- **機能**: ユーザーがIssueにコメント（例：`@gemini-cli-jp /do-something`）を作成することで、Gemini搭載のCLIアシスタントと対話できるようにします。アシスタントは、ユーザーのリクエストに基づいてリポジトリでアクションを実行できます。
-
-###  triage `gemini-issue-automated-triage.yml`
-- **トリガー**: Issueの作成または編集
-- **機能**: 新規または更新されたIssueを自動的にトリアージします。Geminiによって決定されたIssueの内容に基づいて、ラベルの追加、担当者の割り当て、またはコメントの投稿ができます。
-
-### 🕒 `gemini-issue-scheduled-triage.yml`
-- **トリガー**: スケジュールされたcronジョブ
-- **機能**: 定期的にオープンなIssueをスキャンし、古いIssueの特定や優先順位の提案などのトリアージタスクを実行します。
-
-### 🔍 `gemini-pr-review.yml`
-- **トリガー**: プルリクエストの作成または更新
-- **機能**: プルリクエストを自動的にレビューします。Geminiは、コードの品質に関するフィードバックの提供、改善の提案、または潜在的な問題の特定ができます。
-
-### 🔄 `sync-to-report-gh.yml`
-- **トリガー**: mainブランチへのプッシュ
-- **機能**: これは以前のテンプレートからのレガシーワークフローであり、このラボでは積極的に使用されていません。日次レポートを中央リポジトリに同期するように設計されていました。
-
----
-
-## 📸 スクリーンショットと例
-
-### 🤖 CLIの対話例
-Issueを作成し、`@gemini-cli-jp /help`とコメントして、利用可能なコマンドを確認します:
-
-\```
-@gemini-cli-jp /help
-\```
-
-AIアシスタントが利用可能なコマンドと使用例を返信します。
-
-### 🏗️ ワークフローのアーキテクチャ
-\```mermaid
-graph TD
-    A[GitHub Issue/PR] --> B[GitHub Actions トリガー]
-    B --> C[Gemini CLI ワークフロー]
-    C --> D[Gemini AI 処理]
-    D --> E[リポジトリ操作]
-    E --> F[自動応答]
-
-    G[スケジュール/Cron] --> H[自動トリアージ]
-    H --> I[Issue管理]
-
-    J[PR作成] --> K[PRレビューワークフロー]
-    K --> L[コード解析]
-    L --> M[フィードバックと提案]
-\```
-
-### 💬 対話の例
-
-**コードレビューのリクエスト:**
-\```
-@gemini-cli-jp /review-pr
-このプルリクエストをレビューし、改善点を提案してください
-\```
-
-**Issueのトリアージ:**
-\```
-@gemini-cli-jp /triage
-このIssueを分析し、適切なラベルと担当者を提案してください
-\```
-
----
-
-## 🛠️ トラブルシューティング
-
-### 一般的な問題
-
-**❌ ワークフローがトリガーされない:**
-- リポジトリの設定でGitHub Actionsが有効になっているか確認してください
-- リポジトリの設定でWebhookの配信を確認してください
-- トリガー条件（例：コメントに`@gemini-cli-jp`が含まれているか）が満たされているか確認してください
-
-**❌ Gemini APIのエラー:**
-- `GEMINI_API_KEY`シークレットが設定されているか確認してください
-- APIキーの権限とクォータを確認してください
-- APIキーが有効で期限切れでないことを確認してください
-
-**❌ 権限エラー:**
-- ユーザーに書き込み権限があることを確認してください
-- リポジトリがプライベートでないか確認してください（信頼されたユーザーの検出に影響します）
-
-### ヘルプの入手方法
-1. [GitHub Issues](https://github.com/your-repo/issues)で同様の問題がないか確認してください
-2. 詳細なエラーログを記載した新しいIssueを作成してください
-3. Issueを報告する際には、ワークフローの実行ログを含めてください
-
----
-
-## 🚀 インストールとセットアップ
-
-### 前提条件
-- リポジトリ作成権限のあるGitHubアカウント
-- Google AI StudioのGemini APIキー
-- GitHub Actionsの基本的な理解
-
-### クイックスタート
-1. **このリポジトリをフォーク**して、自分のGitHubアカウントにコピーします
-2. リポジトリの設定で**GitHubシークレットを設定**します:
-   - `GEMINI_API_KEY`: あなたのGemini APIキー
-   - `GITHUB_TOKEN`: (自動的に提供されます)
-3. `.github/workflows/`からあなたのリポジトリに**ワークフローファイルをコピー**します
-4. あなたのニーズに合わせて**ワークフローをカスタマイズ**します
-5. Issueを作成し、`@gemini-cli-jp /help`とコメントして**セットアップをテスト**します
-
-### 高度な設定
-追加機能を利用するには、これらのオプションのシークレットを設定します:
-- `APP_ID`と`APP_PRIVATE_KEY`: GitHub App連携用
-- `GCP_WIF_PROVIDER`と関連するGCP変数: Vertex AI利用のため
-
----
-
-## 📁 ディレクトリ構造
-
-\```
-.
-├── .github/
-│   └── workflows/
-│       ├── gemini-cli-jp.yml
-│       ├── gemini-issue-automated-triage.yml
-│       ├── gemini-issue-scheduled-triage.yml
-│       ├── gemini-pr-review.yml
-│       └── sync-to-report-gh.yml
-├── .gitignore
-├── LICENSE
-└── README.md
-\```
-
----
-
-## 📝 ライセンス
-
-このプロジェクトは、[LICENSE](LICENSE)ファイルの条件に基づいてライセンスされています。
-
----
-
-© 2025 Sunwood-ai-labsII
\ No newline at end of file
diff --git a/README.md b/README.md
index 6ce4bca..a4c7124 100644
--- a/README.md
+++ b/README.md
@@ -15,136 +15,136 @@
 
 ---
 
-## 📖 Overview
+## 📖 概要
 
-This repository serves as a laboratory and showcase for integrating Google's Gemini AI with GitHub Actions. It demonstrates how to automate various repository management tasks using the power of generative AI.
+このリポジトリは、GoogleのGemini AIをGitHub Actionsと統合するための実験室およびショーケースとして機能します。生成AIの力を利用して、さまざまなリポジトリ管理タスクを自動化する方法を示します。
 
-### 🎯 Key Features
-- **AI-Powered Automation**: Leverage Gemini to handle tasks like issue triage, pull request reviews, and more.
-- **CLI-like Interaction**: Interact with the AI assistant directly from issue comments.
-- **Extensible Workflows**: Easily adapt and customize the workflows for your own projects.
+### 🎯 主な機能
+- **AIによる自動化**: Geminiを活用して、Issueのトリアージ、プルリクエストのレビューなどのタスクを処理します。
+- **CLIライクな対話**: Issueのコメントから直接AIアシスタントと対話します。
+- **拡張可能なワークフロー**: 独自のプロジェクトに合わせてワークフローを簡単に適応およびカスタマイズできます。
 
 ---
 
-## 🤖 Workflows
+## 🤖 ワークフロー
 
-This repository includes the following GitHub Actions workflows:
+このリポジトリには、以下のGitHub Actionsワークフローが含まれています：
 
 ### 📄 `gemini-cli-jp.yml`
-- **Trigger**: Issue comments
-- **Function**: Allows users to interact with a Gemini-powered CLI assistant by creating comments on issues (e.g., `@gemini-cli-jp /do-something`). The assistant can then perform actions on the repository based on the user's request.
+- **トリガー**: Issueのコメント
+- **機能**: ユーザーがIssueにコメント（例：`@gemini-cli-jp /do-something`）を作成することで、Gemini搭載のCLIアシスタントと対話できるようにします。アシスタントは、ユーザーのリクエストに基づいてリポジトリでアクションを実行できます。
 
 ###  triage `gemini-issue-automated-triage.yml`
-- **Trigger**: Issue creation or edits
-- **Function**: Automatically triages new or updated issues. It can add labels, assignees, or post comments based on the issue's content as determined by Gemini.
+- **トリガー**: Issueの作成または編集
+- **機能**: 新規または更新されたIssueを自動的にトリアージします。Geminiによって決定されたIssueの内容に基づいて、ラベルの追加、担当者の割り当て、またはコメントの投稿ができます。
 
 ### 🕒 `gemini-issue-scheduled-triage.yml`
-- **Trigger**: Scheduled cron job
-- **Function**: Periodically scans open issues and performs triage tasks, such as identifying stale issues or suggesting priorities.
+- **トリガー**: スケジュールされたcronジョブ
+- **機能**: 定期的にオープンなIssueをスキャンし、古いIssueの特定や優先順位の提案などのトリアージタスクを実行します。
 
 ### 🔍 `gemini-pr-review.yml`
-- **Trigger**: Pull request creation or updates
-- **Function**: Automatically reviews pull requests. Gemini can provide feedback on code quality, suggest improvements, or identify potential issues.
+- **トリガー**: プルリクエストの作成または更新
+- **機能**: プルリクエストを自動的にレビューします。Geminiは、コードの品質に関するフィードバックの提供、改善の提案、または潜在的な問題の特定ができます。
 
 ### 🔄 `sync-to-report-gh.yml`
-- **Trigger**: Push to the main branch
-- **Function**: This is a legacy workflow from a previous template and is not actively used in this lab. It was designed to sync daily reports to a central repository.
+- **トリガー**: mainブランチへのプッシュ
+- **機能**: これは以前のテンプレートからのレガシーワークフローであり、このラボでは積極的に使用されていません。日次レポートを中央リポジトリに同期するように設計されていました。
 
 ---
 
-## 📸 Screenshots & Examples
+## 📸 スクリーンショットと例
 
-### 🤖 CLI Interaction Example
-Create an issue and comment with `@gemini-cli /help` to see available commands:
+### 🤖 CLIの対話例
+Issueを作成し、`@gemini-cli-jp /help`とコメントして、利用可能なコマンドを確認します:
 
 \```
-@gemini-cli /help
+@gemini-cli-jp /help
 \```
 
-The AI assistant will respond with available commands and usage examples.
+AIアシスタントが利用可能なコマンドと使用例を返信します。
 
-### 🏗️ Workflow Architecture
+### 🏗️ ワークフローのアーキテクチャ
 \```mermaid
 graph TD
-    A[GitHub Issue/PR] --> B[GitHub Actions Trigger]
-    B --> C[Gemini CLI Workflow]
-    C --> D[Gemini AI Processing]
-    D --> E[Repository Actions]
-    E --> F[Automated Response]
-
-    G[Schedule/Cron] --> H[Automated Triage]
-    H --> I[Issue Management]
-
-    J[PR Created] --> K[PR Review Workflow]
-    K --> L[Code Analysis]
-    L --> M[Feedback & Suggestions]
+    A[GitHub Issue/PR] --> B[GitHub Actions トリガー]
+    B --> C[Gemini CLI ワークフロー]
+    C --> D[Gemini AI 処理]
+    D --> E[リポジトリ操作]
+    E --> F[自動応答]
+
+    G[スケジュール/Cron] --> H[自動トリアージ]
+    H --> I[Issue管理]
+
+    J[PR作成] --> K[PRレビューワークフロー]
+    K --> L[コード解析]
+    L --> M[フィードバックと提案]
 \```
 
-### 💬 Example Interactions
+### 💬 対話の例
 
-**Code Review Request:**
+**コードレビューのリクエスト:**
 \```
-@gemini-cli /review-pr
-Please review this pull request and suggest improvements
+@gemini-cli-jp /review-pr
+このプルリクエストをレビューし、改善点を提案してください
 \```
 
-**Issue Triage:**
+**Issueのトリアージ:**
 \```
-@gemini-cli /triage
-Analyze this issue and suggest appropriate labels and assignees
+@gemini-cli-jp /triage
+このIssueを分析し、適切なラベルと担当者を提案してください
 \```
 
 ---
 
-## 🛠️ Troubleshooting
+## 🛠️ トラブルシューティング
 
-### Common Issues
+### 一般的な問題
 
-**❌ Workflow not triggering:**
-- Check if GitHub Actions are enabled in repository settings
-- Verify webhook delivery in repository settings
-- Ensure the trigger conditions are met (e.g., `@gemini-cli` in comment)
+**❌ ワークフローがトリガーされない:**
+- リポジトリの設定でGitHub Actionsが有効になっているか確認してください
+- リポジトリの設定でWebhookの配信を確認してください
+- トリガー条件（例：コメントに`@gemini-cli-jp`が含まれているか）が満たされているか確認してください
 
-**❌ Gemini API errors:**
-- Verify `GEMINI_API_KEY` secret is configured
-- Check API key permissions and quota
-- Ensure the API key is valid and not expired
+**❌ Gemini APIのエラー:**
+- `GEMINI_API_KEY`シークレットが設定されているか確認してください
+- APIキーの権限とクォータを確認してください
+- APIキーが有効で期限切れでないことを確認してください
 
-**❌ Permission errors:**
-- Confirm the user has write permissions
-- Check if the repository is private (affects trusted user detection)
+**❌ 権限エラー:**
+- ユーザーに書き込み権限があることを確認してください
+- リポジトリがプライベートでないか確認してください（信頼されたユーザーの検出に影響します）
 
-### Getting Help
-1. Check the [GitHub Issues](https://github.com/your-repo/issues) for similar problems
-2. Create a new issue with detailed error logs
-3. Include workflow run logs when reporting issues
+### ヘルプの入手方法
+1. [GitHub Issues](https://github.com/your-repo/issues)で同様の問題がないか確認してください
+2. 詳細なエラーログを記載した新しいIssueを作成してください
+3. Issueを報告する際には、ワークフローの実行ログを含めてください
 
 ---
 
-## 🚀 Installation & Setup
+## 🚀 インストールとセットアップ
 
-### Prerequisites
-- GitHub account with repository creation permissions
-- Gemini API key from Google AI Studio
-- Basic understanding of GitHub Actions
+### 前提条件
+- リポジトリ作成権限のあるGitHubアカウント
+- Google AI StudioのGemini APIキー
+- GitHub Actionsの基本的な理解
 
-### Quick Start
-1. **Fork this repository** to your GitHub account
-2. **Configure GitHub Secrets** in your repository settings:
-   - `GEMINI_API_KEY`: Your Gemini API key
-   - `GITHUB_TOKEN`: (automatically provided)
-3. **Copy workflow files** from `.github/workflows/` to your repository
-4. **Customize workflows** according to your needs
-5. **Test the setup** by creating an issue and commenting `@gemini-cli /help`
+### クイックスタート
+1. **このリポジトリをフォーク**して、自分のGitHubアカウントにコピーします
+2. リポジトリの設定で**GitHubシークレットを設定**します:
+   - `GEMINI_API_KEY`: あなたのGemini APIキー
+   - `GITHUB_TOKEN`: (自動的に提供されます)
+3. `.github/workflows/`からあなたのリポジトリに**ワークフローファイルをコピー**します
+4. あなたのニーズに合わせて**ワークフローをカスタマイズ**します
+5. Issueを作成し、`@gemini-cli-jp /help`とコメントして**セットアップをテスト**します
 
-### Advanced Configuration
-For additional features, configure these optional secrets:
-- `APP_ID` and `APP_PRIVATE_KEY`: For GitHub App integration
-- `GCP_WIF_PROVIDER` and related GCP variables: For Vertex AI usage
+### 高度な設定
+追加機能を利用するには、これらのオプションのシークレットを設定します:
+- `APP_ID`と`APP_PRIVATE_KEY`: GitHub App連携用
+- `GCP_WIF_PROVIDER`と関連するGCP変数: Vertex AI利用のため
 
 ---
 
-## 📁 Directory Structure
+## 📁 ディレクトリ構造
 
 \```
 .
@@ -155,6 +155,11 @@ For additional features, configure these optional secrets:
 │       ├── gemini-issue-scheduled-triage.yml
 │       ├── gemini-pr-review.yml
 │       └── sync-to-report-gh.yml
+├── discord-issue-bot/
+│   ├── Dockerfile
+│   ├── pyproject.toml
+│   ├── compose.yaml
+│   └── bot.py
 ├── .gitignore
 ├── LICENSE
 └── README.md
@@ -162,10 +167,35 @@ For additional features, configure these optional secrets:
 
 ---
 
-## 📝 License
+## 📝 ライセンス
 
-This project is licensed under the terms of the [LICENSE](LICENSE) file.
+このプロジェクトは、[LICENSE](LICENSE)ファイルの条件に基づいてライセンスされています。
 
 ---
 
-© 2025 Sunwood-ai-labsII
\ No newline at end of file
+© 2025 Sunwood-ai-labsII
+
+
+---
+
+## 🤖 Discord Issue Bot（ワークフロー不要・最小構成）
+
+- 直に GitHub REST API で Issue を作成する最小ボットです。
+- 必要な環境変数は 2 つのみ: `DISCORD_BOT_TOKEN`, `GITHUB_TOKEN`。
+
+使い方:
+\```
+export DISCORD_BOT_TOKEN=xxxx
+export GITHUB_TOKEN=ghp_xxx
+cd discord-issue-bot
+docker compose -f compose.yaml up -d --build
+\```
+
+Discord で投稿（例）:
+\```
+!issue owner/repo "バグ: 保存できない" 再現手順… #kind/bug +maki
+\```
+ルール:
+- 先頭 `!issue`、直後に `owner/repo` を含める
+- タイトルは "ダブルクオート" で囲む（未指定時は1行目をタイトル）
+- `#label` がラベル、`+user` がアサイン
diff --git a/discord-issue-bot/.env.example b/discord-issue-bot/.env.example
new file mode 100644
index 0000000..c4bf152
--- /dev/null
+++ b/discord-issue-bot/.env.example
@@ -0,0 +1,7 @@
+# Required
+DISCORD_BOT_TOKEN=your_discord_bot_token_here
+GITHUB_TOKEN=ghp_your_github_token_here
+
+# Optional
+# GITHUB_API=https://api.github.com
+# DISCORD_MESSAGE_PREFIX=!issue
diff --git a/discord-issue-bot/Dockerfile b/discord-issue-bot/Dockerfile
new file mode 100644
index 0000000..52331ab
--- /dev/null
+++ b/discord-issue-bot/Dockerfile
@@ -0,0 +1,10 @@
+FROM ghcr.io/astral-sh/uv:python3.13-bookworm
+
+ENV PYTHONDONTWRITEBYTECODE=1 \
+    PYTHONUNBUFFERED=1
+
+WORKDIR /app
+COPY pyproject.toml ./
+RUN uv sync
+COPY . .
+CMD ["uv", "run", "bot.py"]
diff --git a/discord-issue-bot/README.md b/discord-issue-bot/README.md
new file mode 100644
index 0000000..e6c2d1f
--- /dev/null
+++ b/discord-issue-bot/README.md
@@ -0,0 +1,92 @@
+# Discord Issue Bot (Simple)
+
+シンプルな Discord ボットです。Discord のチャットから直接 GitHub Issue を作成します（ワークフロー不要）。
+
+必要な環境変数は 2 つだけ:
+- `DISCORD_BOT_TOKEN`
+- `GITHUB_TOKEN`（プライベートリポの場合は `repo` 権限推奨）
+
+## 使い方
+
+1) 環境変数を設定
+
+\```bash
+export DISCORD_BOT_TOKEN=xxxx
+export GITHUB_TOKEN=ghp_xxx
+\```
+
+2) Docker で起動（uv sync により依存を自動セットアップ）
+
+\```bash
+cd discord-issue-bot
+docker compose -f compose.yaml up -d --build
+docker compose -f compose.yaml logs -f
+\```
+
+3) Discord で投稿（例）
+
+\```
+!issue owner/repo "バグ: 保存できない" 再現手順… #kind/bug #priority/p2 +maki
+\```
+
+書式:
+- プレフィックス: `!issue`
+- 最初に `owner/repo` を必ず含める
+- タイトルは `"ダブルクオート"` で囲むと1行で指定可能（未指定なら1行目がタイトル、2行目以降が本文）
+- `#label` でラベル、`+user` でアサイン
+
+### Discord でのチャット例
+
+以下は、実際に Discord 上でボットに話しかけて Issue を作成する際の例です。
+
+- 1行で完結（タイトルをダブルクオートで囲む）
+
+\```
+!issue Sunwood-ai-labsII/gemini-actions-lab "バグ: セーブできない" 再現手順を書きます。 #bug #p2 +your-github-username
+\```
+
+- 複数行で本文をしっかり書く（1行目がタイトル、2行目以降が本文）
+
+\```
+!issue Sunwood-ai-labsII/gemini-actions-lab
+エディタがクラッシュする
+特定のファイルを開いた直後にクラッシュします。
+再現手順:
+1. プロジェクトを開く
+2. settings.json を開く
+3. 5秒後にクラッシュ
+#bug #crash +your-github-username
+\```
+
+- ラベルやアサインを省略してシンプルに
+
+\```
+!issue Sunwood-ai-labsII/gemini-actions-lab "ドキュメントを更新" README の手順が古いので更新してください。
+\```
+
+ヒント:
+- 既定のプレフィックスは `!issue` です。変更したい場合は環境変数 `DISCORD_MESSAGE_PREFIX` を設定してください。
+- ボットは作成に成功すると Issue の URL を返信します。メッセージへのリンク（jump URL）は本文末尾に自動で記録されます。
+- ギルド（サーバー）内でボットがメッセージ本文を読むには、Developer Portal で「Message Content Intent」を ON にしてください（下記「Discord 設定（特権インテント）」参照）。
+
+## 実装
+- `bot.py`: Discord メッセージをパースし、GitHub API (`POST /repos/{owner}/{repo}/issues`) に直接作成
+- 依存: `discord.py`
+- ビルド: `Dockerfile`（uv インストール → `uv sync` → `uv run bot.py`）
+
+## Discord 設定（特権インテント）
+- 本ボットはメッセージ本文を読むため、Discord の「Message Content Intent（特権インテント）」が必要です。
+- 設定手順:
+  - https://discord.com/developers/applications で対象アプリを開く
+  - 左メニュー「Bot」→ Privileged Gateway Intents → 「MESSAGE CONTENT INTENT」を ON
+  - 「Save Changes」で保存
+- 反映後、コンテナを再起動してください（例: `docker compose up -d --build` または `docker-compose up --build`）。
+
+## トラブルシューティング
+- 起動時に以下のエラーが出る場合:
+  - `discord.errors.PrivilegedIntentsRequired: ... requesting privileged intents ... enable the privileged intents ...`
+  - 上記「Discord 設定（特権インテント）」の手順で「Message Content Intent」を有効化してください。
+- 応急処置（動作制限あり）:
+  - `bot.py` の `intents.message_content = True` を外す/`False` にすると接続自体は通りますが、ギルド内のメッセージ本文を読めず、本ボットのコマンドは動作しません。
+- 代替案:
+  - スラッシュコマンドに移行すると、Message Content Intent なしでも運用できます（実装変更が必要）。
diff --git a/discord-issue-bot/bot.py b/discord-issue-bot/bot.py
new file mode 100644
index 0000000..b41e924
--- /dev/null
+++ b/discord-issue-bot/bot.py
@@ -0,0 +1,141 @@
+#!/usr/bin/env python3
+import os
+import re
+import json
+from urllib import request, error
+
+import discord
+
+DISCORD_TOKEN = os.environ.get("DISCORD_BOT_TOKEN", "")
+GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_PAT")
+GITHUB_API = os.environ.get("GITHUB_API", "https://api.github.com")
+
+PREFIX = os.environ.get("DISCORD_MESSAGE_PREFIX", "!issue").strip()
+
+
+def http_post(url: str, token: str, payload: dict):
+    data = json.dumps(payload).encode("utf-8")
+    req = request.Request(url, data=data, method="POST")
+    req.add_header("Authorization", f"Bearer {token}")
+    req.add_header("Accept", "application/vnd.github+json")
+    req.add_header("Content-Type", "application/json")
+    try:
+        with request.urlopen(req) as resp:
+            body = resp.read().decode("utf-8")
+            return resp.status, body
+    except error.HTTPError as e:
+        body = e.read().decode("utf-8", errors="replace") if e.fp else ""
+        return e.code, body
+
+
+def parse(content: str):
+    """
+    Syntax (simple):
+      !issue owner/repo "Title" Body text ... #label1 +assignee1
+    or  !issue owner/repo Title on first line\nBody from second line ... #bug
+    Returns: dict(repo, title, body, labels[], assignees[])
+    """
+    text = content.strip()
+    if text.lower().startswith(PREFIX.lower()):
+        text = text[len(PREFIX):].strip()
+
+    # Find first owner/repo token
+    m_repo = re.search(r"\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b", text)
+    repo = m_repo.group(1) if m_repo else ""
+    if not repo:
+        return {"error": "リポジトリ (owner/repo) を含めてください: 例) !issue owner/repo \"タイトル\" 本文"}
+
+    # Remove repo from text before parsing title/body
+    text_wo_repo = (text[:m_repo.start()] + text[m_repo.end():]).strip() if m_repo else text
+
+    # Title/body parsing
+    m = re.match(r'^"([^"]+)"\s*(.*)$', text_wo_repo, flags=re.S)
+    if m:
+        title = m.group(1).strip()
+        body = m.group(2).strip()
+    else:
+        lines = text_wo_repo.splitlines()
+        title = lines[0].strip() if lines else "New Issue"
+        body = "\n".join(lines[1:]).strip()
+
+    # Extract labels (#label) and assignees (+user)
+    labels = [tok[1:].strip() for tok in re.findall(r'(#[\w\-/\.]+)', text_wo_repo)]
+    assignees = [tok[1:].strip() for tok in re.findall(r'(\+[A-Za-z0-9-]+)', text_wo_repo)]
+
+    # Clean tokens from body
+    body = re.sub(r'(#[\w\-/\.]+)', '', body)
+    body = re.sub(r'(\+[A-Za-z0-9-]+)', '', body).strip()
+
+    return {
+        "repo": repo,
+        "title": title or "New Issue",
+        "body": body or "(no body)",
+        "labels": list(dict.fromkeys(labels)),
+        "assignees": list(dict.fromkeys(assignees)),
+    }
+
+
+def build_body_with_footer(body: str, author: str, source_url: str | None):
+    parts = [body]
+    meta = []
+    if author:
+        meta.append(f"Reported via Discord by: {author}")
+    if source_url:
+        meta.append(f"Source: {source_url}")
+    if meta:
+        parts.append("\n\n---\n" + "\n".join(meta))
+    return "".join(parts)
+
+
+class Bot(discord.Client):
+    async def on_ready(self):
+        print(f"Logged in as {self.user} | prefix={PREFIX}")
+
+    async def on_message(self, message: discord.Message):
+        if message.author.bot:
+            return
+        content = (message.content or "").strip()
+        if not content.lower().startswith(PREFIX.lower()):
+            return
+
+        if not GITHUB_TOKEN:
+            await message.reply("GITHUB_TOKEN が未設定です", mention_author=False)
+            return
+
+        parsed = parse(content)
+        if "error" in parsed:
+            await message.reply(parsed["error"], mention_author=False)
+            return
+
+        repo = parsed["repo"]
+        url = f"{GITHUB_API}/repos/{repo}/issues"
+        payload = {"title": parsed["title"], "body": build_body_with_footer(parsed["body"], str(message.author), message.jump_url)}
+        if parsed["labels"]:
+            payload["labels"] = parsed["labels"]
+        if parsed["assignees"]:
+            payload["assignees"] = parsed["assignees"]
+
+        status, resp = http_post(url, GITHUB_TOKEN, payload)
+        try:
+            data = json.loads(resp) if resp else {}
+        except Exception:
+            data = {}
+        if status in (200, 201):
+            issue_url = data.get("html_url", "")
+            number = data.get("number", "?")
+            await message.reply(f"Issueを作成しました: #{number} {issue_url}", mention_author=False)
+        else:
+            await message.reply(f"作成失敗: {status}\n{resp[:1500]}", mention_author=False)
+
+
+def main():
+    if not DISCORD_TOKEN:
+        raise SystemExit("DISCORD_BOT_TOKEN が未設定です")
+    intents = discord.Intents.default()
+    intents.message_content = True
+    Bot(intents=intents).run(DISCORD_TOKEN)
+
+
+if __name__ == "__main__":
+    main()
+
diff --git a/discord-issue-bot/docker-compose.yaml b/discord-issue-bot/docker-compose.yaml
new file mode 100644
index 0000000..634c143
--- /dev/null
+++ b/discord-issue-bot/docker-compose.yaml
@@ -0,0 +1,9 @@
+services:
+  bot:
+    build: .
+    env_file:
+      - .env
+    environment:
+      - DISCORD_BOT_TOKEN
+      - GITHUB_TOKEN
+    restart: unless-stopped
diff --git a/discord-issue-bot/pyproject.toml b/discord-issue-bot/pyproject.toml
new file mode 100644
index 0000000..a290a82
--- /dev/null
+++ b/discord-issue-bot/pyproject.toml
@@ -0,0 +1,12 @@
+[project]
+name = "discord-issue-bot"
+version = "0.1.0"
+description = "Create GitHub issues directly from Discord chat"
+requires-python = ">=3.10"
+dependencies = [
+  "discord.py>=2.3.2",
+]
+
+[tool.uv]
+dev-dependencies = []
+
diff --git a/example/index.html b/example/index.html
new file mode 100644
index 0000000..e7103c4
--- /dev/null
+++ b/example/index.html
@@ -0,0 +1,221 @@
+<!DOCTYPE html>
+<html lang="ja">
+<head>
+    <meta charset="UTF-8">
+    <meta name="viewport" content="width=device-width, initial-scale=1.0">
+    <title>和モダン電卓</title>
+    <style>
+        :root {
+            --bg-color: #f5f5f5;
+            --frame-color: #d3c1a5;
+            --display-bg: #ffffff;
+            --display-border: #a39e93;
+            --button-bg: #ffffff;
+            --button-hover-bg: #e9e2d7;
+            --operator-bg: #d3c1a5;
+            --operator-hover-bg: #c1b094;
+            --equal-bg: #a7825a;
+            --equal-hover-bg: #8f6f4d;
+            --text-color: #333333;
+            --font-family: 'Hiragino Mincho ProN', 'MS Mincho', serif;
+        }
+
+        body {
+            background-color: var(--bg-color);
+            display: flex;
+            justify-content: center;
+            align-items: center;
+            height: 100vh;
+            margin: 0;
+            font-family: var(--font-family);
+        }
+
+        .calculator {
+            background-color: var(--frame-color);
+            border-radius: 15px;
+            padding: 25px;
+            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1), 0 6px 6px rgba(0, 0, 0, 0.15);
+            border: 2px solid #c1b094;
+        }
+
+        .display {
+            background-color: var(--display-bg);
+            border: 2px solid var(--display-border);
+            border-radius: 10px;
+            padding: 15px 20px;
+            margin-bottom: 20px;
+            text-align: right;
+            font-size: 2.8em;
+            min-height: 60px;
+            overflow-x: auto;
+            color: var(--text-color);
+            box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
+        }
+
+        .buttons {
+            display: grid;
+            grid-template-columns: repeat(4, 1fr);
+            gap: 15px;
+        }
+
+        .btn {
+            background-color: var(--button-bg);
+            border: 1px solid var(--display-border);
+            border-radius: 8px;
+            padding: 20px;
+            font-size: 1.5em;
+            cursor: pointer;
+            transition: background-color 0.2s, transform 0.1s;
+            font-family: var(--font-family);
+            color: var(--text-color);
+        }
+
+        .btn:hover {
+            background-color: var(--button-hover-bg);
+            transform: translateY(-2px);
+        }
+        
+        .btn:active {
+            transform: translateY(1px);
+        }
+
+        .operator {
+            background-color: var(--operator-bg);
+        }
+
+        .operator:hover {
+            background-color: var(--operator-hover-bg);
+        }
+
+        .equal {
+            background-color: var(--equal-bg);
+            color: white;
+            grid-column: span 2;
+        }
+
+        .equal:hover {
+            background-color: var(--equal-hover-bg);
+        }
+    </style>
+</head>
+<body>
+
+<div class="calculator">
+    <div class="display" id="display">0</div>
+    <div class="buttons">
+        <button class="btn operator" onclick="clearDisplay()">C</button>
+        <button class="btn operator" onclick="appendOperator('/')">÷</button>
+        <button class="btn operator" onclick="appendOperator('*')">×</button>
+        <button class="btn operator" onclick="deleteLast()">DEL</button>
+
+        <button class="btn" onclick="appendNumber('7')">7</button>
+        <button class="btn" onclick="appendNumber('8')">8</button>
+        <button class="btn" onclick="appendNumber('9')">9</button>
+        <button class="btn operator" onclick="appendOperator('-')">−</button>
+
+        <button class="btn" onclick="appendNumber('4')">4</button>
+        <button class="btn" onclick="appendNumber('5')">5</button>
+        <button class="btn" onclick="appendNumber('6')">6</button>
+        <button class="btn operator" onclick="appendOperator('+')">+</button>
+
+        <button class="btn" onclick="appendNumber('1')">1</button>
+        <button class="btn" onclick="appendNumber('2')">2</button>
+        <button class="btn" onclick="appendNumber('3')">3</button>
+        <button class="btn equal" onclick="calculate()">=</button>
+
+        <button class="btn" onclick="appendNumber('0')">0</button>
+        <button class="btn" onclick="appendNumber('00')">00</button>
+        <button class="btn" onclick="appendOperator('.')">.</button>
+    </div>
+</div>
+
+<script>
+    const display = document.getElementById('display');
+    let currentInput = '0';
+    let operator = null;
+    let previousInput = null;
+    let shouldResetDisplay = false;
+
+    function updateDisplay() {
+        display.textContent = currentInput;
+    }
+
+    function appendNumber(number) {
+        if (currentInput === '0' || shouldResetDisplay) {
+            currentInput = number;
+            shouldResetDisplay = false;
+        } else {
+            currentInput += number;
+        }
+        updateDisplay();
+    }
+
+    function appendOperator(op) {
+        if (shouldResetDisplay) {
+            shouldResetDisplay = false;
+        }
+        if (operator !== null) {
+            calculate();
+        }
+        previousInput = currentInput;
+        operator = op;
+        shouldResetDisplay = true;
+    }
+
+    function calculate() {
+        if (operator === null || shouldResetDisplay) {
+            return;
+        }
+        let result;
+        const prev = parseFloat(previousInput);
+        const current = parseFloat(currentInput);
+
+        switch (operator) {
+            case '+':
+                result = prev + current;
+                break;
+            case '-':
+                result = prev - current;
+                break;
+            case '*':
+                result = prev * current;
+                break;
+            case '/':
+                if (current === 0) {
+                    alert("0で割ることはできません。");
+                    clearDisplay();
+                    return;
+                }
+                result = prev / current;
+                break;
+            default:
+                return;
+        }
+        currentInput = result.toString();
+        operator = null;
+        previousInput = null;
+        shouldResetDisplay = true;
+        updateDisplay();
+    }
+
+    function clearDisplay() {
+        currentInput = '0';
+        operator = null;
+        previousInput = null;
+        shouldResetDisplay = false;
+        updateDisplay();
+    }
+
+    function deleteLast() {
+        if (shouldResetDisplay) return;
+        currentInput = currentInput.slice(0, -1);
+        if (currentInput === '') {
+            currentInput = '0';
+        }
+        updateDisplay();
+    }
+
+</script>
+
+</body>
+</html>
diff --git a/example/todo/index.html b/example/todo/index.html
new file mode 100644
index 0000000..d8355be
--- /dev/null
+++ b/example/todo/index.html
@@ -0,0 +1,22 @@
+<!DOCTYPE html>
+<html lang="ja">
+<head>
+    <meta charset="UTF-8">
+    <meta name="viewport" content="width=device-width, initial-scale=1.0">
+    <title>TODOアプリ</title>
+    <link rel="stylesheet" href="style.css">
+</head>
+<body>
+    <div class="container">
+        <h1>TODOアプリ</h1>
+        <div class="input-area">
+            <input type="text" id="todo-input" placeholder="新しいタスクを入力">
+            <button id="add-button">追加</button>
+        </div>
+        <ul id="todo-list">
+            <!-- タスクがここに追加されます -->
+        </ul>
+    </div>
+    <script src="script.js"></script>
+</body>
+</html>
\ No newline at end of file
diff --git a/example/todo/script.js b/example/todo/script.js
new file mode 100644
index 0000000..ebeb9ba
--- /dev/null
+++ b/example/todo/script.js
@@ -0,0 +1,80 @@
+document.addEventListener('DOMContentLoaded', () => {
+    const todoInput = document.getElementById('todo-input');
+    const addButton = document.getElementById('add-button');
+    const todoList = document.getElementById('todo-list');
+
+    // ローカルストレージからタスクを読み込む
+    const loadTasks = () => {
+        const tasks = JSON.parse(localStorage.getItem('todos')) || [];
+        tasks.forEach(task => createTaskElement(task.text, task.completed));
+    };
+
+    // タスクをローカルストレージに保存する
+    const saveTasks = () => {
+        const tasks = [];
+        todoList.querySelectorAll('.todo-item').forEach(item => {
+            tasks.push({
+                text: item.querySelector('span').textContent,
+                completed: item.classList.contains('completed')
+            });
+        });
+        localStorage.setItem('todos', JSON.stringify(tasks));
+    };
+
+    // タスク要素を作成する
+    const createTaskElement = (taskText, isCompleted = false) => {
+        const li = document.createElement('li');
+        li.classList.add('todo-item');
+        if (isCompleted) {
+            li.classList.add('completed');
+        }
+
+        const checkbox = document.createElement('input');
+        checkbox.type = 'checkbox';
+        checkbox.checked = isCompleted;
+        checkbox.addEventListener('change', () => {
+            li.classList.toggle('completed');
+            saveTasks();
+        });
+
+        const span = document.createElement('span');
+        span.textContent = taskText;
+
+        const deleteButton = document.createElement('button');
+        deleteButton.textContent = '削除';
+        deleteButton.classList.add('delete-button');
+        deleteButton.addEventListener('click', () => {
+            li.remove();
+            saveTasks();
+        });
+
+        li.appendChild(checkbox);
+        li.appendChild(span);
+        li.appendChild(deleteButton);
+        todoList.appendChild(li);
+    };
+
+    // タスクを追加する
+    const addTask = () => {
+        const taskText = todoInput.value.trim();
+        if (taskText === '') {
+            alert('タスクを入力してください。');
+            return;
+        }
+        createTaskElement(taskText);
+        saveTasks();
+        todoInput.value = '';
+        todoInput.focus();
+    };
+
+    // イベントリスナーを設定
+    addButton.addEventListener('click', addTask);
+    todoInput.addEventListener('keypress', (e) => {
+        if (e.key === 'Enter') {
+            addTask();
+        }
+    });
+
+    // 初期タスクを読み込む
+    loadTasks();
+});
diff --git a/example/todo/style.css b/example/todo/style.css
new file mode 100644
index 0000000..b253cf2
--- /dev/null
+++ b/example/todo/style.css
@@ -0,0 +1,97 @@
+body {
+    font-family: sans-serif;
+    background-color: #f4f4f4;
+    margin: 0;
+    padding: 0;
+    display: flex;
+    justify-content: center;
+    align-items: center;
+    min-height: 100vh;
+}
+
+.container {
+    background: #fff;
+    padding: 2rem;
+    border-radius: 8px;
+    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
+    width: 100%;
+    max-width: 500px;
+}
+
+h1 {
+    text-align: center;
+    color: #333;
+}
+
+.input-area {
+    display: flex;
+    margin-bottom: 1rem;
+}
+
+#todo-input {
+    flex-grow: 1;
+    padding: 0.5rem;
+    border: 1px solid #ddd;
+    border-radius: 4px;
+    font-size: 1rem;
+}
+
+#add-button {
+    background-color: #007bff;
+    color: white;
+    border: none;
+    padding: 0.5rem 1rem;
+    border-radius: 4px;
+    cursor: pointer;
+    margin-left: 0.5rem;
+    font-size: 1rem;
+}
+
+#add-button:hover {
+    background-color: #0056b3;
+}
+
+#todo-list {
+    list-style: none;
+    padding: 0;
+    margin: 0;
+}
+
+.todo-item {
+    display: flex;
+    align-items: center;
+    padding: 0.8rem 0.5rem;
+    border-bottom: 1px solid #eee;
+}
+
+.todo-item:last-child {
+    border-bottom: none;
+}
+
+.todo-item.completed span {
+    text-decoration: line-through;
+    color: #aaa;
+}
+
+.todo-item input[type="checkbox"] {
+    margin-right: 1rem;
+    cursor: pointer;
+}
+
+.todo-item span {
+    flex-grow: 1;
+}
+
+.delete-button {
+    background-color: #dc3545;
+    color: white;
+    border: none;
+    padding: 0.3rem 0.6rem;
+    border-radius: 4px;
+    cursor: pointer;
+    font-size: 0.9rem;
+}
+
+.delete-button:hover {
+    background-color: #c82333;
+}
diff --git a/generated-images/imagen-4_2025-09-06T11-49-47-885Z_A_beautiful_Japanese_landscape_with_cherry_blossom_1.png b/generated-images/imagen-4_2025-09-06T11-49-47-885Z_A_beautiful_Japanese_landscape_with_cherry_blossom_1.png
new file mode 100644
index 0000000..9918f0c
Binary files /dev/null and b/generated-images/imagen-4_2025-09-06T11-49-47-885Z_A_beautiful_Japanese_landscape_with_cherry_blossom_1.png differ
diff --git a/generated-images/imagen-4_2025-09-06T11-49-47-892Z_A_beautiful_Japanese_landscape_with_cherry_blossom_2.png b/generated-images/imagen-4_2025-09-06T11-49-47-892Z_A_beautiful_Japanese_landscape_with_cherry_blossom_2.png
new file mode 100644
index 0000000..d3ed6e9
Binary files /dev/null and b/generated-images/imagen-4_2025-09-06T11-49-47-892Z_A_beautiful_Japanese_landscape_with_cherry_blossom_2.png differ
diff --git a/generated-images/metadata.json b/generated-images/metadata.json
new file mode 100644
index 0000000..f54ec06
--- /dev/null
+++ b/generated-images/metadata.json
@@ -0,0 +1,10 @@
+{
+  "generation_date": "2025-09-06T11:49:51Z",
+  "prompt": "A beautiful Japanese landscape with cherry blossoms and mountains",
+  "model": "imagen-4",
+  "num_images": 2,
+  "aspect_ratio": "1:1",
+  "seed": "",
+  "workflow_run": "12",
+  "commit_sha": "b466018b57025ce0bde38ed96e71f39ea8c9b486"
+}
diff --git a/response.md b/response.md
new file mode 100644
index 0000000..9dae9d9
--- /dev/null
+++ b/response.md
@@ -0,0 +1,10 @@
+`example/index.html` を作成し、`issue/15/create-simple-html` ブランチにコミットしました。
+
+ご確認いただき、問題なければこの Issue はクローズしてください。
+
+### 計画
+- [x] `example` フォルダの作成
+- [x] `example/index.html` の作成
+- [x] 動作確認
+- [x] gitブランチの作成とコミット
+- [x] クローズ提案
```
