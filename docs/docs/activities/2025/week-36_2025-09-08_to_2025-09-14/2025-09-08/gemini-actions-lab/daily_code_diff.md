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
index 12875fe..bf0bf84 100644
--- a/.github/workflows/gemini-issue-automated-triage.yml
+++ b/.github/workflows/gemini-issue-automated-triage.yml
@@ -137,26 +137,44 @@ jobs:
               }
             }
           prompt: |-
-            You are an issue triage assistant. Analyze the GitHub issue and suggest appropriate labels.
+            You are an expert GitHub issue triage assistant. Your task is to analyze the provided issue and suggest appropriate labels.
 
+            **ISSUE DETAILS:**
             Repository: ${REPOSITORY}
             Issue Number: ${ISSUE_NUMBER}
-            Issue Title: "${ISSUE_TITLE}"
-            Issue Body: "${ISSUE_BODY}"
-            Available Labels: ${AVAILABLE_LABELS}
+            Title: "${ISSUE_TITLE}"
+            Body: "${ISSUE_BODY}"
 
-            Please analyze this issue carefully and suggest appropriate labels from the available labels list.
+            **AVAILABLE LABELS:**
+            ${AVAILABLE_LABELS}
+
+            **INSTRUCTIONS:**
+            1. Carefully analyze the issue title and body content
+            2. Select appropriate labels from the available labels list
+            3. If no existing labels are suitable, suggest new labels that would be helpful
+            4. Provide a brief explanation for your label choices
+
+            **CRITICAL: You must respond with ONLY a valid JSON object in this exact format:**
             
-            Important: Respond with ONLY the JSON object, no additional text or explanations before or after.
+            {
+              "labels_to_set": ["label1", "label2"],
+              "explanation": "Brief explanation of why these labels were chosen"
+            }
 
-            Constraints:
-            - Do NOT run any shell or external commands; use only the provided environment variables
-            - Do NOT attempt to execute `gh label list` or call the GitHub API to fetch labels. The available labels are already provided in "${AVAILABLE_LABELS}".
+            **RULES:**
+            - Response must be valid JSON only
+            - No additional text before or after the JSON
+            - No markdown code blocks
+            - No explanatory text outside the JSON
+            - If unsure, choose the most general applicable labels
+            - If no labels apply, use empty array: []
 
-            Output format (JSON only):
-            {"labels_to_set": ["label1", "label2"], "explanation": "reasoning for these labels"}
+            **EXAMPLES:**
+            Bug report: {"labels_to_set": ["bug"], "explanation": "Issue reports unexpected behavior"}
+            Feature request: {"labels_to_set": ["enhancement"], "explanation": "User requesting new functionality"}
+            Documentation: {"labels_to_set": ["documentation"], "explanation": "Related to documentation updates"}
 
-            If the issue content appears to be empty or placeholder text, still try to categorize it based on any available information.
+            Analyze the issue now and respond with the JSON:
 
       - name: 'Apply Labels to Issue'
         if: |-
@@ -175,67 +193,93 @@ jobs:
             
             let parsedLabels;
             try {
-              // 改良されたJSON抽出ロジック
-              let jsonString = rawLabels;
+              // 改良されたJSON抽出および検証ロジック
+              let jsonString = rawLabels.trim();
               
-              // 1. \```json \``` ブロックを抽出
-              const jsonBlockMatch = jsonString.match(/\```json\s*([\s\S]*?)\s*\```/);
-              if (jsonBlockMatch) {
-                jsonString = jsonBlockMatch[1].trim();
-                core.info(`Extracted JSON from json code block: ${jsonString}`);
+              // まず、生の出力がJSONかどうかをチェック
+              if (!jsonString.startsWith('{') && !jsonString.startsWith('[')) {
+                // JSONではない場合、フォールバック処理
+                core.warning(`Output is not JSON format: ${jsonString}`);
+                
+                // 基本的なフォールバック: 空のラベル配列を返す
+                parsedLabels = {
+                  labels_to_set: [],
+                  explanation: `Failed to parse Gemini output: ${jsonString.substring(0, 100)}...`
+                };
               } else {
-                // 2. \``` \``` ブロックを抽出（json指定なし）
-                const codeBlockMatch = jsonString.match(/\```\s*([\s\S]*?)\s*\```/);
-                if (codeBlockMatch) {
-                  jsonString = codeBlockMatch[1].trim();
-                  core.info(`Extracted JSON from code block: ${jsonString}`);
+                // 1. \```json \``` ブロックを抽出
+                const jsonBlockMatch = jsonString.match(/\```json\s*([\s\S]*?)\s*\```/);
+                if (jsonBlockMatch) {
+                  jsonString = jsonBlockMatch[1].trim();
+                  core.info(`Extracted JSON from json code block: ${jsonString}`);
                 } else {
-                  // 3. { で始まって } で終わる部分を抽出
-                  const jsonObjectMatch = jsonString.match(/(\{[\s\S]*\})/);
-                  if (jsonObjectMatch) {
-                    jsonString = jsonObjectMatch[1].trim();
-                    core.info(`Extracted JSON object: ${jsonString}`);
+                  // 2. \``` \``` ブロックを抽出（json指定なし）
+                  const codeBlockMatch = jsonString.match(/\```\s*([\s\S]*?)\s*\```/);
+                  if (codeBlockMatch) {
+                    jsonString = codeBlockMatch[1].trim();
+                    core.info(`Extracted JSON from code block: ${jsonString}`);
                   } else {
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
+                    // 3. { で始まって } で終わる部分を抽出
+                    const jsonObjectMatch = jsonString.match(/(\{[\s\S]*\})/);
+                    if (jsonObjectMatch) {
+                      jsonString = jsonObjectMatch[1].trim();
+                      core.info(`Extracted JSON object: ${jsonString}`);
+                    } else {
+                      // 4. [ で始まって ] で終わる部分を抽出（配列の場合）
+                      const jsonArrayMatch = jsonString.match(/(\[[\s\S]*\])/);
+                      if (jsonArrayMatch) {
+                        // 配列が返された場合は、最初の要素を使用（単一issue用）
+                        const arrayData = JSON.parse(jsonArrayMatch[1].trim());
+                        if (Array.isArray(arrayData) && arrayData.length > 0) {
+                          // 現在のissue番号に一致するものを探す
+                          const currentIssueNumber = parseInt(process.env.ISSUE_NUMBER);
+                          const matchingIssue = arrayData.find(item => item.issue_number === currentIssueNumber);
+                          if (matchingIssue) {
+                            parsedLabels = {
+                              labels_to_set: matchingIssue.labels_to_set,
+                              explanation: matchingIssue.explanation
+                            };
+                          } else {
+                            // 一致するissue番号がない場合は最初の要素を使用
+                            const firstItem = arrayData[0];
+                            parsedLabels = {
+                              labels_to_set: firstItem.labels_to_set,
+                              explanation: firstItem.explanation
+                            };
+                          }
+                          core.info(`Successfully parsed from array: ${JSON.stringify(parsedLabels)}`);
                         }
-                        core.info(`Successfully parsed from array: ${JSON.stringify(parsedLabels)}`);
                       }
-                    } else {
-                      // 5. フォールバック: そのままパース
-                      core.info(`Using fallback - trying to parse as-is`);
                     }
                   }
                 }
-              }
-              
-              // まだparsedLabelsが設定されていない場合、通常のJSONパースを試行
-              if (!parsedLabels) {
-                parsedLabels = JSON.parse(jsonString);
-                core.info(`Successfully parsed labels JSON: ${JSON.stringify(parsedLabels)}`);
+                
+                // まだparsedLabelsが設定されていない場合、通常のJSONパースを試行
+                if (!parsedLabels) {
+                  parsedLabels = JSON.parse(jsonString);
+                  core.info(`Successfully parsed labels JSON: ${JSON.stringify(parsedLabels)}`);
+                }
+                
+                // 結果の検証
+                if (!parsedLabels.labels_to_set) {
+                  parsedLabels.labels_to_set = [];
+                }
+                if (!Array.isArray(parsedLabels.labels_to_set)) {
+                  parsedLabels.labels_to_set = [];
+                }
+                if (!parsedLabels.explanation) {
+                  parsedLabels.explanation = "No explanation provided";
+                }
               }
             } catch (err) {
-              core.setFailed(`Failed to parse labels JSON from Gemini output: ${err.message}\nRaw output: ${rawLabels}`);
-              return;
+              core.warning(`Failed to parse labels JSON from Gemini output: ${err.message}`);
+              core.info(`Raw output: ${rawLabels}`);
+              
+              // フォールバック: 空のラベル配列を使用
+              parsedLabels = {
+                labels_to_set: [],
+                explanation: `Parsing failed: ${err.message}`
+              };
             }
 
             const issueNumber = parseInt(process.env.ISSUE_NUMBER);
```
