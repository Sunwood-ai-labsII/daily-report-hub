# 🔄 Latest Code Changes

```diff
diff --git a/.github/prompts/gemini-cli_prompt.ja.md b/.github/prompts/gemini-cli_prompt.ja.md
index 9fc49dc..ad9e315 100644
--- a/.github/prompts/gemini-cli_prompt.ja.md
+++ b/.github/prompts/gemini-cli_prompt.ja.md
@@ -102,6 +102,19 @@ ${USER_REQUEST}
   - 💡 学び: 得られた知見、次に活かす点
   - ▶️ 次のアクション: レビュー/追作業/検証などの依頼
 
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
 ### 進捗コメントの例
 
 \```
@@ -116,13 +129,27 @@ ${USER_REQUEST}
 ### PR本文の例（response.md 生成時）
 
 \```
-## 📋 AAR
+## 📋 AAR（概要）
 - 🎯 目的: Issue #${ISSUE_NUMBER} への対応PR
 - ✅ 実施: ブランチ作成・変更のコミット/プッシュ・PR作成
 - 🔍 差異: 競合はなし（あれば解決内容を記載）
 - 💡 学び: 自動PRフローの安定動作を確認
 - ▶️ 次のアクション: レビューとマージのご確認をお願いします
 
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
 関連: #${ISSUE_NUMBER}
 \```
 
@@ -164,6 +191,55 @@ ${USER_REQUEST}
 - 変更の背景や補足（あれば）。
 \```
 
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
 ## 📣 Issue へのPR通知コメント例
 
 \```
```
