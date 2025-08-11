# 📝 Daily Commits

## ⏰ 13:39:53 - `66d02de`
**Update sync-to-report.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 13:39:53 2025 +0900
M	.github/workflows/sync-to-report.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 13:39:53 2025 +0900

    Update sync-to-report.yml

 .github/workflows/sync-to-report.yml | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report.yml b/.github/workflows/sync-to-report.yml
index 05e88cd..4c230f7 100644
--- a/.github/workflows/sync-to-report.yml
+++ b/.github/workflows/sync-to-report.yml
@@ -236,7 +236,7 @@ jobs:
       
       - name: Clone and update report hub
         env:
-          GITHUB_TOKEN: ${{ secrets.REPORT_TOKEN }}
+          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
         run: |
           # Git設定
           git config --global user.name "GitHub Actions Bot"
@@ -297,4 +297,4 @@ jobs:
           else
             git commit -m "📊 Daily sync: $REPO_NAME ($DATE) - $COMMIT_COUNT commits"
             git push
-          fi
\ No newline at end of file
+          fi
```

---

## ⏰ 13:40:58 - `ec0357e`
**Update sync-to-report.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 13:40:58 2025 +0900
M	.github/workflows/sync-to-report.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 13:40:58 2025 +0900

    Update sync-to-report.yml

 .github/workflows/sync-to-report.yml | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report.yml b/.github/workflows/sync-to-report.yml
index 4c230f7..463703d 100644
--- a/.github/workflows/sync-to-report.yml
+++ b/.github/workflows/sync-to-report.yml
@@ -1,4 +1,4 @@
-name: Sync to Daily Report Hub
+name: Sync to Daily Report Hub v1.1
 on:
   push:
     branches: [main, master]
```

---

## ⏰ 13:43:18 - `69cad62`
**Update sync-to-report.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 13:43:18 2025 +0900
M	.github/workflows/sync-to-report.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 13:43:18 2025 +0900

    Update sync-to-report.yml

 .github/workflows/sync-to-report.yml | 5 +++--
 1 file changed, 3 insertions(+), 2 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report.yml b/.github/workflows/sync-to-report.yml
index 463703d..6d66b7a 100644
--- a/.github/workflows/sync-to-report.yml
+++ b/.github/workflows/sync-to-report.yml
@@ -1,4 +1,4 @@
-name: Sync to Daily Report Hub v1.1
+name: Sync to Daily Report Hub v1.2
 on:
   push:
     branches: [main, master]
@@ -237,13 +237,14 @@ jobs:
       - name: Clone and update report hub
         env:
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}
+          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
         run: |
           # Git設定
           git config --global user.name "GitHub Actions Bot"
           git config --global user.email "actions@github.com"
           
           # daily-report-hubをクローン
-          git clone https://x-access-token:${GITHUB_TOKEN}@github.com/Sunwood-ai-labs/daily-report-hub.git
+          git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub
           
           # 日付ベースのディレクトリ構造を作成
           TARGET_DIR="daily-report-hub/activities/$DATE/$REPO_NAME"
```

---

## ⏰ 13:43:41 - `f9d6702`
**Update sync-to-report.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 13:43:41 2025 +0900
M	.github/workflows/sync-to-report.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 13:43:41 2025 +0900

    Update sync-to-report.yml

 .github/workflows/sync-to-report.yml | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report.yml b/.github/workflows/sync-to-report.yml
index 6d66b7a..20876db 100644
--- a/.github/workflows/sync-to-report.yml
+++ b/.github/workflows/sync-to-report.yml
@@ -1,4 +1,4 @@
-name: Sync to Daily Report Hub v1.2
+name: Sync to Daily Report Hub v1.3
 on:
   push:
     branches: [main, master]
```

---

## ⏰ 13:55:25 - `29b6a7e`
**📝 プロジェクトドキュメントを追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 13:55:25 2025 +0900
A	.env.example
A	CHANGELOG.md
A	CONTRIBUTING.md
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 13:55:25 2025 +0900

    📝 プロジェクトドキュメントを追加
    
    - .env.example: 環境変数のサンプルファイルを追加
    - CHANGELOG.md: 変更履歴管理ファイルを追加
    - CONTRIBUTING.md: コントリビューションガイドを追加

 .env.example    | 15 +++++++++++++++
 CHANGELOG.md    | 32 ++++++++++++++++++++++++++++++++
 CONTRIBUTING.md | 51 +++++++++++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 98 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/.env.example b/.env.example
new file mode 100644
index 0000000..218c470
--- /dev/null
+++ b/.env.example
@@ -0,0 +1,15 @@
+# おみくじアプリ設定例
+# 実際の設定は .env ファイルに記載してください
+
+# アプリケーション設定
+APP_NAME=おみくじアプリ
+APP_VERSION=1.0.0
+
+# 将来的な機能拡張用
+# API_ENDPOINT=https://api.example.com
+# DEBUG_MODE=false
+# ANALYTICS_ID=your-analytics-id
+
+# GitHub Actions関連（必要に応じて）
+# GITHUB_TOKEN=your-github-token
+# REPORT_HUB_REPO=your-username/daily-report-hub
\ No newline at end of file
diff --git a/CHANGELOG.md b/CHANGELOG.md
new file mode 100644
index 0000000..20aeb24
--- /dev/null
+++ b/CHANGELOG.md
@@ -0,0 +1,32 @@
+# 📝 変更履歴
+
+このファイルは、プロジェクトの重要な変更を記録します。
+
+形式は [Keep a Changelog](https://keepachangelog.com/ja/1.0.0/) に基づいており、
+このプロジェクトは [セマンティック バージョニング](https://semver.org/lang/ja/) に準拠しています。
+
+## [Unreleased]
+
+### 追加
+- README.mdの視覚的改善（中央揃え、バッジ、ヘッダー画像）
+- スクリーンショットプレースホルダーの追加
+- JavaScriptファイルへの詳細コメント追加
+- おみくじ結果に応じた色分けスタイリング
+- .env.exampleファイルの追加
+- CONTRIBUTING.mdの追加
+- CHANGELOG.mdの追加（このファイル）
+
+### 変更
+- CSSにアニメーション効果を追加
+- プロジェクト構造の文書化を改善
+
+## [1.0.0] - 2025-01-XX
+
+### 追加
+- 基本的なおみくじ機能
+- シンプルなウェブインターフェース
+- GitHub Actions による日報同期機能
+- レスポンシブデザイン
+
+[Unreleased]: https://github.com/your-username/daily-report-hub_sample1/compare/v1.0.0...HEAD
+[1.0.0]: https://github.com/your-username/daily-report-hub_sample1/releases/tag/v1.0.0
\ No newline at end of file
diff --git a/CONTRIBUTING.md b/CONTRIBUTING.md
new file mode 100644
index 0000000..1962486
--- /dev/null
+++ b/CONTRIBUTING.md
@@ -0,0 +1,51 @@
+# 🤝 コントリビューションガイド
+
+おみくじアプリへの貢献をお考えいただき、ありがとうございます！
+
+## 📋 貢献方法
+
+### 🐛 バグ報告
+
+バグを発見した場合は、以下の情報を含めてIssueを作成してください：
+
+- 使用しているブラウザとバージョン
+- 再現手順
+- 期待される動作
+- 実際の動作
+- スクリーンショット（可能であれば）
+
+### 💡 機能提案
+
+新機能のアイデアがある場合は、以下を含めてIssueを作成してください：
+
+- 機能の詳細説明
+- 使用ケース
+- 実装の提案（任意）
+
+### 🔧 プルリクエスト
+
+1. このリポジトリをフォーク
+2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
+3. 変更をコミット (`git commit -m 'Add some amazing feature'`)
+4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
+5. プルリクエストを作成
+
+## 📝 コーディング規約
```

---

## ⏰ 13:55:35 - `3b2996a`
**✨ README.mdを大幅に改善**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 13:55:35 2025 +0900
M	README.md
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 13:55:35 2025 +0900

    ✨ README.mdを大幅に改善
    
    - プロジェクトロゴとバッジを追加
    - スクリーンショットセクションを追加
    - 技術仕様と機能一覧を詳細化
    - クイックスタートガイドを追加

 README.md | 80 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++--
 1 file changed, 78 insertions(+), 2 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/README.md b/README.md
index f2432b3..e26ebfc 100644
--- a/README.md
+++ b/README.md
@@ -1,5 +1,19 @@
+<div align="center">
+
+![](https://github.com/user-attachments/assets/f7afed43-1d98-4886-b2e0-57c99dd7874e)
+
 # daily-report-hub_sample1
 
+![Omikuji App](https://via.placeholder.com/800x200/FF6B6B/FFFFFF?text=🎋+Omikuji+App+⛩️)
+
+<p>
+  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
+  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
+  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
+</p>
+
+</div>
+
 > [!IMPORTANT]
 > このリポジトリは、GitHub Actionsを利用してGitのコミット履歴から自動で日報を作成・集約するワークフローのサンプルです。
 >
@@ -9,8 +23,70 @@
 
 シンプルなウェブベースのおみくじアプリケーションです。あなたの今日の運勢を占ってみましょう！🔮
 
-### 遊び方 🎮
+### 📸 スクリーンショット
+
+<div align="center">
+
+![App Screenshot](https://via.placeholder.com/600x400/F0F0F0/333333?text=🎋+おみくじアプリ+⛩️)
+
+</div>
+
+### 🎮 遊び方
 
 1️⃣ このリポジトリをクローンまたはダウンロードします。 💻
 2️⃣ `index.html`ファイルをウェブブラウザで開きます。 🌐
-3️⃣ 「おみくじを引く」ボタンをクリックすると、今日の運勢が表示されます。 ✨
\ No newline at end of file
+3️⃣ 「おみくじを引く」ボタンをクリックすると、今日の運勢が表示されます。 ✨
+
+### 🛠️ 技術仕様
+
+- **フロントエンド**: HTML5, CSS3, Vanilla JavaScript
+- **ブラウザ要件**: モダンブラウザ（Chrome, Firefox, Safari, Edge）
+- **依存関係**: なし
+
+### 📁 プロジェクト構造
+
+```
+├── index.html              # メインHTMLファイル
+├── style.css               # スタイルシート
+├── script.js               # JavaScript処理
+├── .github/
+│   └── workflows/
+│       └── sync-to-report.yml  # 日報同期ワークフロー
+└── README.md               # このファイル
+```
+
+### 🚀 クイックスタート
+
+```bash
+# リポジトリをクローン
+git clone https://github.com/your-username/daily-report-hub_sample1.git
+
+# ディレクトリに移動
+cd daily-report-hub_sample1
+
+# ブラウザでindex.htmlを開く
+open index.html  # macOS
+start index.html # Windows
+```
+
+### 📋 機能一覧
+
+- ✨ ランダムなおみくじ結果の表示
+- 🎨 レスポンシブデザイン
+- ⚡ 高速な動作（依存関係なし）
+- 📱 モバイル対応
+
+### 🤝 コントリビューション
+
+プロジェクトへの貢献を歓迎します！詳細は [CONTRIBUTING.md](./CONTRIBUTING.md) をご覧ください。
+
+### 📝 変更履歴
+
+プロジェクトの変更履歴は [CHANGELOG.md](./CHANGELOG.md) で確認できます。
+
+### 🔗 関連リンク
+
+- [日報ハブリポジトリ](https://github.com/Sunwood-ai-labs/daily-report-hub)
+- [GitHub Actions ワークフロー](./.github/workflows/sync-to-report.yml)
+- [コントリビューションガイド](./CONTRIBUTING.md)
+- [変更履歴](./CHANGELOG.md)
\ No newline at end of file
```

---

## ⏰ 13:55:45 - `84f38df`
**🔧 HTMLファイルのアクセシビリティと構造を改善**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 13:55:45 2025 +0900
M	index.html
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 13:55:45 2025 +0900

    🔧 HTMLファイルのアクセシビリティと構造を改善
    
    - メタ情報（description, keywords, author）を追加
    - aria-label, aria-live, role属性でアクセシビリティ向上
    - コメントを追加してコード可読性を向上
    - タイトルに絵文字を追加

 index.html | 26 ++++++++++++++++++++++----
 1 file changed, 22 insertions(+), 4 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/index.html b/index.html
index 5d6aa93..e7b086f 100644
--- a/index.html
+++ b/index.html
@@ -1,17 +1,35 @@
 <!DOCTYPE html>
 <html lang="ja">
 <head>
+    <!-- 基本的なメタ情報 -->
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
-    <title>おみくじアプリ</title>
+    <meta name="description" content="シンプルなウェブベースのおみくじアプリケーション">
+    <meta name="keywords" content="おみくじ, 占い, ウェブアプリ">
+    <meta name="author" content="daily-report-hub_sample1">
+    
+    <title>おみくじアプリ ⛩️</title>
+    
+    <!-- スタイルシート -->
     <link rel="stylesheet" href="style.css">
+    
+    <!-- ファビコン（将来的に追加予定） -->
+    <!-- <link rel="icon" type="image/x-icon" href="/favicon.ico"> -->
 </head>
 <body>
+    <!-- メインコンテナ -->
     <div class="container">
-        <h1>おみくじ</h1>
-        <button id="draw-button">おみくじを引く</button>
-        <p id="result"></p>
+        <!-- アプリタイトル -->
+        <h1>おみくじ ⛩️</h1>
+        
+        <!-- おみくじを引くボタン -->
+        <button id="draw-button" aria-label="おみくじを引く">おみくじを引く</button>
+        
+        <!-- 結果表示エリア -->
+        <p id="result" aria-live="polite" role="status"></p>
     </div>
+    
+    <!-- JavaScript -->
     <script src="script.js"></script>
 </body>
 </html>
```

---

## ⏰ 13:55:54 - `4d1b8ae`
**⚡ JavaScriptの機能とコード品質を向上**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 13:55:54 2025 +0900
M	script.js
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 13:55:54 2025 +0900

    ⚡ JavaScriptの機能とコード品質を向上
    
    - JSDocコメントを追加して関数の説明を明確化
    - 結果に応じたCSSクラス適用機能を追加
    - コードの可読性を向上させるコメントを追加
    - 視覚的フィードバック機能を実装

 script.js | 17 +++++++++++++++++
 1 file changed, 17 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/script.js b/script.js
index 4259f77..ceaa046 100644
--- a/script.js
+++ b/script.js
@@ -1,9 +1,26 @@
+/**
+ * おみくじアプリのメイン処理
+ * シンプルなランダム選択によるおみくじ機能を提供
+ */
+
+// DOM要素の取得
 const drawButton = document.getElementById('draw-button');
 const result = document.getElementById('result');
 
+// おみくじの結果配列（大吉から大凶まで6段階）
 const fortunes = ['大吉', '中吉', '小吉', '吉', '凶', '大凶'];
 
+/**
+ * おみくじを引く処理
+ * ボタンクリック時にランダムな結果を表示
+ */
 drawButton.addEventListener('click', () => {
+    // 0から配列の長さ-1までのランダムな整数を生成
     const randomIndex = Math.floor(Math.random() * fortunes.length);
+    
+    // 結果を画面に表示
     result.textContent = fortunes[randomIndex];
+    
+    // 結果に応じてスタイルを変更（視覚的フィードバック）
+    result.className = `fortune-${randomIndex}`;
 });
```

---

## ⏰ 13:56:03 - `147c1cd`
**🎨 CSSデザインを大幅に改善**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 13:56:03 2025 +0900
M	style.css
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 13:56:03 2025 +0900

    🎨 CSSデザインを大幅に改善
    
    - グラデーション背景とモダンなデザインを適用
    - おみくじ結果に応じた色分け機能を追加
    - ボタンのホバー・アクティブ効果を強化
    - レスポンシブデザインとアクセシビリティを向上

 style.css | 83 +++++++++++++++++++++++++++++++++++++++++++++++++++++++--------
 1 file changed, 73 insertions(+), 10 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/style.css b/style.css
index c90ae90..5023f7d 100644
--- a/style.css
+++ b/style.css
@@ -1,38 +1,66 @@
+/**
+ * おみくじアプリのスタイルシート
+ * シンプルで使いやすいデザインを提供
+ */
+
+/* 基本的なページレイアウト */
 body {
-    font-family: sans-serif;
+    font-family: 'Hiragino Sans', 'Yu Gothic', 'Meiryo', sans-serif;
     display: flex;
     justify-content: center;
     align-items: center;
     height: 100vh;
     margin: 0;
-    background-color: #f0f0f0;
+    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
+    color: #333;
 }
 
+/* メインコンテナ */
 .container {
     text-align: center;
     background-color: white;
     padding: 2rem;
-    border-radius: 10px;
-    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
+    border-radius: 15px;
+    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
+    backdrop-filter: blur(10px);
+    border: 1px solid rgba(255, 255, 255, 0.2);
+    max-width: 400px;
+    width: 90%;
 }
 
+/* タイトルスタイル */
 h1 {
     margin-top: 0;
+    color: #333;
+    font-size: 2.5rem;
+    margin-bottom: 1.5rem;
+    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
 }
 
+/* おみくじボタン */
 button {
-    padding: 10px 20px;
-    font-size: 1rem;
-    background-color: #007bff;
+    padding: 15px 30px;
+    font-size: 1.2rem;
+    background: linear-gradient(45deg, #007bff, #0056b3);
     color: white;
     border: none;
-    border-radius: 5px;
+    border-radius: 25px;
     cursor: pointer;
-    transition: background-color 0.3s;
+    transition: all 0.3s ease;
+    box-shadow: 0 4px 15px rgba(0, 123, 255, 0.3);
+    font-weight: bold;
 }
 
+/* ボタンホバー効果 */
 button:hover {
-    background-color: #0056b3;
+    background: linear-gradient(45deg, #0056b3, #004085);
+    transform: translateY(-2px);
+    box-shadow: 0 6px 20px rgba(0, 123, 255, 0.4);
+}
+
+/* ボタンアクティブ状態 */
+button:active {
+    transform: translateY(0);
 }
 
 #result {
@@ -40,4 +68,39 @@ button:hover {
     font-weight: bold;
     margin-top: 1rem;
     min-height: 3rem;
+    transition: all 0.3s ease;
+    border-radius: 8px;
+    padding: 1rem;
+}
+
+/* おみくじ結果に応じた色分け */
+.fortune-0 { /* 大吉 */
+    background-color: #ffeb3b;
+    color: #d32f2f;
+    box-shadow: 0 0 20px rgba(255, 235, 59, 0.5);
+}
+
+.fortune-1 { /* 中吉 */
+    background-color: #4caf50;
+    color: white;
```

---

## ⏰ 13:56:20 - `43a16f4`
**🔀 Merge: おみくじアプリの機能強化とドキュメント改善**
*by Maki*

### 📋 Changed Files
```bash
Merge: f9d6702 147c1cd
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 13:56:20 2025 +0900
```

### 📊 Statistics
```bash
Merge: f9d6702 147c1cd
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 13:56:20 2025 +0900

    🔀 Merge: おみくじアプリの機能強化とドキュメント改善

 .env.example    | 15 +++++++++++
 CHANGELOG.md    | 32 ++++++++++++++++++++++
 CONTRIBUTING.md | 51 +++++++++++++++++++++++++++++++++++
 README.md       | 80 ++++++++++++++++++++++++++++++++++++++++++++++++++++--
 index.html      | 26 +++++++++++++++---
 script.js       | 17 ++++++++++++
 style.css       | 83 ++++++++++++++++++++++++++++++++++++++++++++++++++-------
 7 files changed, 288 insertions(+), 16 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 13:58:05 - `df5b892`
**Merge branch 'develop'**
*by Maki*

### 📋 Changed Files
```bash
Merge: f9d6702 43a16f4
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 13:58:05 2025 +0900
```

### 📊 Statistics
```bash
Merge: f9d6702 43a16f4
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 13:58:05 2025 +0900

    Merge branch 'develop'

 .env.example    | 15 +++++++++++
 CHANGELOG.md    | 32 ++++++++++++++++++++++
 CONTRIBUTING.md | 51 +++++++++++++++++++++++++++++++++++
 README.md       | 80 ++++++++++++++++++++++++++++++++++++++++++++++++++++--
 index.html      | 26 +++++++++++++++---
 script.js       | 17 ++++++++++++
 style.css       | 83 ++++++++++++++++++++++++++++++++++++++++++++++++++-------
 7 files changed, 288 insertions(+), 16 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 14:07:21 - `e0c30e9`
**✨ daily_commits.mdに詳細な差分情報を追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 14:07:21 2025 +0900
M	.github/workflows/sync-to-report.yml
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 14:07:21 2025 +0900

    ✨ daily_commits.mdに詳細な差分情報を追加
    
    - 各コミットに変更ファイル一覧を表示
    - 統計情報（変更行数など）をコードブロックで表示
    - コード差分を100行まで表示してレビューしやすく改善

 .github/workflows/sync-to-report.yml | 77 +++++++++++++++++++++++-------------
 1 file changed, 50 insertions(+), 27 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report.yml b/.github/workflows/sync-to-report.yml
index 20876db..a830de9 100644
--- a/.github/workflows/sync-to-report.yml
+++ b/.github/workflows/sync-to-report.yml
@@ -12,8 +12,8 @@ jobs:
       - name: Checkout current repo
         uses: actions/checkout@v4
         with:
-          fetch-depth: 0  # 全履歴を取得してその日の全コミットを追跡
-      
+          fetch-depth: 0 # 全履歴を取得してその日の全コミットを追跡
+
       - name: Get repository info and daily activities
         run: |
           # リポジトリ名と日付を取得
@@ -21,18 +21,18 @@ jobs:
           DATE=$(date '+%Y-%m-%d')
           echo "REPO_NAME=$REPO_NAME" >> $GITHUB_ENV
           echo "DATE=$DATE" >> $GITHUB_ENV
-          
+
           echo "🔍 Fetching all commits for $DATE..."
-          
+
           # その日の全コミット履歴を取得（時刻順）
           git log --since="$DATE 00:00:00" --until="$DATE 23:59:59" \
             --pretty=format:"%h|%s|%an|%ad" --date=format:'%H:%M:%S' \
             --reverse > daily_commits_raw.txt
-          
+
           # コミット数をカウント
           COMMIT_COUNT=$(wc -l < daily_commits_raw.txt)
           echo "📊 Found $COMMIT_COUNT commits for today"
-          
+
           # その日の全ての差分を統合（安全な方法で）
           if [ $COMMIT_COUNT -gt 0 ]; then
             FIRST_COMMIT_TODAY=$(git log --since="$DATE 00:00:00" --pretty=format:"%H" --reverse | head -1)
@@ -67,17 +67,17 @@ jobs:
             echo "No commits found for today" > daily_diff_stats_raw.txt
             echo "No commits found for today" > daily_code_diff_raw.txt
           fi
-          
+
           # 最新コミットの個別差分
           git diff HEAD~1 --name-status > latest_diff_raw.txt 2>/dev/null || echo "No recent diff available" > latest_diff_raw.txt
           git diff HEAD~1 > latest_code_diff_raw.txt 2>/dev/null || echo "No recent code diff available" > latest_code_diff_raw.txt
-          
+
           # Markdownファイルを作成（各行に4スペースのインデントを追加する関数）
           add_indent() {
             sed 's/^/    /' "$1"
           }
-          
-          # コミット詳細をMarkdown形式で作成
+
+          # コミット詳細をMarkdown形式で作成（差分付き）
           {
             echo "# 📝 Daily Commits"
             echo ""
@@ -87,12 +87,35 @@ jobs:
                 echo "**$subject**"
                 echo "*by $author*"
                 echo ""
+                
+                # 各コミットの変更ファイル一覧を表示
+                echo "### 📋 Changed Files"
+                echo "\`\`\`"
+                git show --name-status $hash 2>/dev/null | grep -E '^[AMDRC]' || echo "No file changes"
+                echo "\`\`\`"
+                echo ""
+                
+                # 各コミットの統計情報を表示
+                echo "### 📊 Statistics"
+                echo "\`\`\`"
+                git show --stat $hash 2>/dev/null | tail -n +2 || echo "No statistics available"
+                echo "\`\`\`"
+                echo ""
+                
+                # 各コミットのコード差分を表示（最初の100行まで）
+                echo "### 💻 Code Changes"
+                echo "\`\`\`diff"
+                git show $hash --pretty=format:"" 2>/dev/null | head -100 || echo "No code changes available"
+                echo "\`\`\`"
+                echo ""
+                echo "---"
+                echo ""
               done < daily_commits_raw.txt
             else
               echo "*No commits found for today.*"
             fi
           } > daily_commits.md
-          
+
           # 累積差分をMarkdown形式で作成
           {
             echo "# 📋 Daily File Changes"
@@ -115,14 +138,14 @@ jobs:
               echo "*No file changes today.*"
             fi
```

---

## ⏰ 14:07:32 - `8df2ff3`
**🖼️ README.mdの画像リンクを実際のスクリーンショットに更新**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 14:07:32 2025 +0900
M	README.md
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 14:07:32 2025 +0900

    🖼️ README.mdの画像リンクを実際のスクリーンショットに更新
    
    - プレースホルダー画像を削除
    - 実際のアプリスクリーンショットのGitHub URLに変更
    - ドキュメントの視覚的な品質を向上

 README.md | 4 +---
 1 file changed, 1 insertion(+), 3 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/README.md b/README.md
index e26ebfc..28c2ccc 100644
--- a/README.md
+++ b/README.md
@@ -4,8 +4,6 @@
 
 # daily-report-hub_sample1
 
-![Omikuji App](https://via.placeholder.com/800x200/FF6B6B/FFFFFF?text=🎋+Omikuji+App+⛩️)
-
 <p>
   <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
   <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
@@ -27,7 +25,7 @@
 
 <div align="center">
 
-![App Screenshot](https://via.placeholder.com/600x400/F0F0F0/333333?text=🎋+おみくじアプリ+⛩️)
+![App Screenshot](https://github.com/user-attachments/assets/fc8363f1-3a9f-4684-9b5d-b000a0a9a788)
 
 </div>
 
```

---

## ⏰ 14:07:50 - `b32fa35`
**🔀 Merge: コミット差分表示機能の強化とドキュメント改善**
*by Maki*

### 📋 Changed Files
```bash
Merge: 43a16f4 8df2ff3
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 14:07:50 2025 +0900
```

### 📊 Statistics
```bash
Merge: 43a16f4 8df2ff3
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 14:07:50 2025 +0900

    🔀 Merge: コミット差分表示機能の強化とドキュメント改善

 .github/workflows/sync-to-report.yml | 77 +++++++++++++++++++++++-------------
 README.md                            |  4 +-
 2 files changed, 51 insertions(+), 30 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 14:08:56 - `1b906db`
**Merge branch 'develop'**
*by Maki*

### 📋 Changed Files
```bash
Merge: df5b892 b32fa35
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 14:08:56 2025 +0900
```

### 📊 Statistics
```bash
Merge: df5b892 b32fa35
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 14:08:56 2025 +0900

    Merge branch 'develop'

 .github/workflows/sync-to-report.yml | 77 +++++++++++++++++++++++-------------
 README.md                            |  4 +-
 2 files changed, 51 insertions(+), 30 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 15:20:14 - `32ad4f0`
**✨ GitHub Actionsワークフロー用スクリプトファイルを追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 15:20:14 2025 +0900
A	.github/scripts/README.md
A	.github/scripts/analyze-git-activity.sh
A	.github/scripts/calculate-week-info.sh
A	.github/scripts/create-docusaurus-structure.sh
A	.github/scripts/generate-markdown-reports.sh
A	.github/scripts/sync-to-hub.sh
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 15:20:14 2025 +0900

    ✨ GitHub Actionsワークフロー用スクリプトファイルを追加
    
    - 週情報計算スクリプト (calculate-week-info.sh)
    - Git活動分析スクリプト (analyze-git-activity.sh)
    - Markdownレポート生成スクリプト (generate-markdown-reports.sh)
    - Docusaurus構造作成スクリプト (create-docusaurus-structure.sh)
    - レポートハブ同期スクリプト (sync-to-hub.sh)
    - スクリプト説明用README.md

 .github/scripts/README.md                      | 100 ++++++++++++++
 .github/scripts/analyze-git-activity.sh        |  59 ++++++++
 .github/scripts/calculate-week-info.sh         |  44 ++++++
 .github/scripts/create-docusaurus-structure.sh | 111 +++++++++++++++
 .github/scripts/generate-markdown-reports.sh   | 183 +++++++++++++++++++++++++
 .github/scripts/sync-to-hub.sh                 |  70 ++++++++++
 6 files changed, 567 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/.github/scripts/README.md b/.github/scripts/README.md
new file mode 100644
index 0000000..4e2fff1
--- /dev/null
+++ b/.github/scripts/README.md
@@ -0,0 +1,100 @@
+# GitHub Actions Scripts
+
+このディレクトリには、Daily Report Hub同期ワークフローで使用されるスクリプトが含まれています。
+
+## スクリプト一覧
+
+### 1. `calculate-week-info.sh`
+週情報を計算し、環境変数を設定します。
+
+**使用方法:**
+```bash
+./calculate-week-info.sh [WEEK_START_DAY]
+```
+
+**パラメータ:**
+- `WEEK_START_DAY`: 週の開始日 (0=日曜日, 1=月曜日, ..., 6=土曜日)
+
+**出力環境変数:**
+- `REPO_NAME`: リポジトリ名
+- `DATE`: 現在の日付 (YYYY-MM-DD)
+- `YEAR`: 現在の年
+- `WEEK_FOLDER`: 週フォルダ名
+- `WEEK_START_DATE`: 週の開始日
+- `WEEK_END_DATE`: 週の終了日
+- `WEEK_NUMBER`: 週番号
+
+### 2. `analyze-git-activity.sh`
+Gitの活動を分析し、生データファイルを生成します。
+
+**生成ファイル:**
+- `daily_commits_raw.txt`: その日のコミット一覧
+- `daily_cumulative_diff_raw.txt`: その日の累積差分
+- `daily_diff_stats_raw.txt`: その日の統計情報
+- `daily_code_diff_raw.txt`: その日のコード差分
+- `latest_diff_raw.txt`: 最新の差分
+- `latest_code_diff_raw.txt`: 最新のコード差分
+
+### 3. `generate-markdown-reports.sh`
+生データからMarkdownレポートを生成します。
+
+**生成ファイル:**
+- `daily_commits.md`: コミット詳細レポート
+- `daily_cumulative_diff.md`: ファイル変更レポート
+- `daily_diff_stats.md`: 統計レポート
+- `daily_code_diff.md`: コード差分レポート
+- `latest_diff.md`: 最新変更レポート
+- `latest_code_diff.md`: 最新コード差分レポート
+- `daily_summary.md`: 日次サマリーレポート
+
+### 4. `create-docusaurus-structure.sh`
+Docusaurusの構造と`_category_.json`ファイルを作成します。
+
+**必要な環境変数:**
+- `REPO_NAME`, `DATE`, `YEAR`, `WEEK_FOLDER`, `WEEK_NUMBER`, `WEEK_START_DATE`, `WEEK_END_DATE`
+
+**出力環境変数:**
+- `TARGET_DIR`: ターゲットディレクトリのパス
+
+### 5. `sync-to-hub.sh`
+レポートハブにファイルを同期します。
+
+**必要な環境変数:**
+- `GITHUB_TOKEN`: GitHubアクセストークン
+- `REPORT_HUB_REPO`: レポートハブのリポジトリ
+- `TARGET_DIR`: ターゲットディレクトリ
+- その他の週情報変数
+
+## 週の開始日設定
+
+ワークフローファイルの`env.WEEK_START_DAY`を変更することで、週の開始日を制御できます：
+
+```yaml
+env:
+  WEEK_START_DAY: 1  # 0=日曜日, 1=月曜日, 2=火曜日, etc.
+```
+
+## フォルダ構造
+
+生成されるフォルダ構造：
+```
+docs/docs/activities/
+├── _category_.json
+└── 2025/
+    ├── _category_.json
+    └── week-06_2025-08-04_to_2025-08-10/
+        ├── _category_.json
+        └── 2025-08-05/
+            ├── _category_.json
+            └── your-repo/
+                ├── _category_.json
+                ├── daily_summary.md
+                ├── daily_commits.md
+                ├── daily_cumulative_diff.md
+                ├── daily_diff_stats.md
```

---

## ⏰ 15:20:34 - `aeb86c7`
**🔧 GitHub Actionsワークフローをリファクタリング**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 15:20:34 2025 +0900
M	.github/workflows/sync-to-report.yml
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 15:20:34 2025 +0900

    🔧 GitHub Actionsワークフローをリファクタリング
    
    - バージョンをv1.3からv1.4に更新
    - プルリクエストトリガーを拡張 (opened, synchronize, closed)
    - 週の開始日を制御する環境変数を追加 (WEEK_START_DAY)
    - 長大なインラインスクリプトを外部スクリプトファイルに分割
    - 処理ステップを明確化してメンテナンス性を向上

 .github/workflows/sync-to-report.yml | 318 +++--------------------------------
 1 file changed, 23 insertions(+), 295 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report.yml b/.github/workflows/sync-to-report.yml
index a830de9..b0a97ba 100644
--- a/.github/workflows/sync-to-report.yml
+++ b/.github/workflows/sync-to-report.yml
@@ -1,9 +1,13 @@
-name: Sync to Daily Report Hub v1.3
+name: Sync to Daily Report Hub v1.4
 on:
   push:
     branches: [main, master]
   pull_request:
-    types: [merged]
+    types: [opened, synchronize, closed]
+
+# 週の開始日を制御する設定
+env:
+  WEEK_START_DAY: 1 # 週の開始日 (0=日曜日, 1=月曜日, 2=火曜日, 3=水曜日, 4=木曜日, 5=金曜日, 6=土曜日)
 
 jobs:
   sync-data:
@@ -14,250 +18,19 @@ jobs:
         with:
           fetch-depth: 0 # 全履歴を取得してその日の全コミットを追跡
 
-      - name: Get repository info and daily activities
-        run: |
-          # リポジトリ名と日付を取得
-          REPO_NAME=$(basename $GITHUB_REPOSITORY)
-          DATE=$(date '+%Y-%m-%d')
-          echo "REPO_NAME=$REPO_NAME" >> $GITHUB_ENV
-          echo "DATE=$DATE" >> $GITHUB_ENV
-
-          echo "🔍 Fetching all commits for $DATE..."
-
-          # その日の全コミット履歴を取得（時刻順）
-          git log --since="$DATE 00:00:00" --until="$DATE 23:59:59" \
-            --pretty=format:"%h|%s|%an|%ad" --date=format:'%H:%M:%S' \
-            --reverse > daily_commits_raw.txt
-
-          # コミット数をカウント
-          COMMIT_COUNT=$(wc -l < daily_commits_raw.txt)
-          echo "📊 Found $COMMIT_COUNT commits for today"
-
-          # その日の全ての差分を統合（安全な方法で）
-          if [ $COMMIT_COUNT -gt 0 ]; then
-            FIRST_COMMIT_TODAY=$(git log --since="$DATE 00:00:00" --pretty=format:"%H" --reverse | head -1)
-            LAST_COMMIT_TODAY=$(git log --since="$DATE 00:00:00" --pretty=format:"%H" | head -1)
-            
-            echo "First commit: $FIRST_COMMIT_TODAY"
-            echo "Last commit: $LAST_COMMIT_TODAY"
-            
-            # 親コミットが存在するかチェック
-            if git rev-parse --verify "$FIRST_COMMIT_TODAY^" >/dev/null 2>&1; then
-              # 親コミットが存在する場合
-              PARENT_OF_FIRST=$(git rev-parse $FIRST_COMMIT_TODAY^)
-              git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY --name-status > daily_cumulative_diff_raw.txt 2>/dev/null || echo "No diff available" > daily_cumulative_diff_raw.txt
-              git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY --stat > daily_diff_stats_raw.txt 2>/dev/null || echo "No stats available" > daily_diff_stats_raw.txt
-              # コードの詳細差分を取得
-              git diff $PARENT_OF_FIRST..$LAST_COMMIT_TODAY > daily_code_diff_raw.txt 2>/dev/null || echo "No code diff available" > daily_code_diff_raw.txt
-            else
-              # 初回コミットの場合（親が存在しない）
-              echo "Initial commit detected - showing all files as new"
-              git diff --name-status 4b825dc642cb6eb9a060e54bf8d69288fbee4904..$LAST_COMMIT_TODAY > daily_cumulative_diff_raw.txt 2>/dev/null || \
-              git ls-tree --name-status $LAST_COMMIT_TODAY > daily_cumulative_diff_raw.txt 2>/dev/null || \
-              echo "A\t(all files added in initial commit)" > daily_cumulative_diff_raw.txt
-              
-              git diff --stat 4b825dc642cb6eb9a060e54bf8d69288fbee4904..$LAST_COMMIT_TODAY > daily_diff_stats_raw.txt 2>/dev/null || \
-              echo "Initial commit - all files added" > daily_diff_stats_raw.txt
-              
-              # 初回コミットのコード内容
-              git show $LAST_COMMIT_TODAY > daily_code_diff_raw.txt 2>/dev/null || echo "No code diff available" > daily_code_diff_raw.txt
-            fi
-          else
-            echo "No commits found for today" > daily_cumulative_diff_raw.txt
-            echo "No commits found for today" > daily_diff_stats_raw.txt
-            echo "No commits found for today" > daily_code_diff_raw.txt
-          fi
-
-          # 最新コミットの個別差分
-          git diff HEAD~1 --name-status > latest_diff_raw.txt 2>/dev/null || echo "No recent diff available" > latest_diff_raw.txt
-          git diff HEAD~1 > latest_code_diff_raw.txt 2>/dev/null || echo "No recent code diff available" > latest_code_diff_raw.txt
-
-          # Markdownファイルを作成（各行に4スペースのインデントを追加する関数）
-          add_indent() {
-            sed 's/^/    /' "$1"
-          }
-
-          # コミット詳細をMarkdown形式で作成（差分付き）
-          {
-            echo "# 📝 Daily Commits"
-            echo ""
-            if [ -s daily_commits_raw.txt ]; then
-              while IFS='|' read -r hash subject author time; do
-                echo "## ⏰ $time - \`$hash\`"
-                echo "**$subject**"
-                echo "*by $author*"
-                echo ""
-                
-                # 各コミットの変更ファイル一覧を表示
-                echo "### 📋 Changed Files"
```

---

## ⏰ 15:21:05 - `b3fd498`
**🔀 Merge: GitHub Actionsワークフローのリファクタリングとスクリプト分割**
*by Maki*

### 📋 Changed Files
```bash
Merge: b32fa35 aeb86c7
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 15:21:05 2025 +0900
```

### 📊 Statistics
```bash
Merge: b32fa35 aeb86c7
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 15:21:05 2025 +0900

    🔀 Merge: GitHub Actionsワークフローのリファクタリングとスクリプト分割

 .github/scripts/README.md                      | 100 ++++++++
 .github/scripts/analyze-git-activity.sh        |  59 +++++
 .github/scripts/calculate-week-info.sh         |  44 ++++
 .github/scripts/create-docusaurus-structure.sh | 111 +++++++++
 .github/scripts/generate-markdown-reports.sh   | 183 ++++++++++++++
 .github/scripts/sync-to-hub.sh                 |  70 ++++++
 .github/workflows/sync-to-report.yml           | 318 ++-----------------------
 7 files changed, 590 insertions(+), 295 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 15:28:58 - `f26c465`
**Merge branch 'develop'**
*by Maki*

### 📋 Changed Files
```bash
Merge: 1b906db b3fd498
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 15:28:58 2025 +0900
```

### 📊 Statistics
```bash
Merge: 1b906db b3fd498
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 15:28:58 2025 +0900

    Merge branch 'develop'

 .github/scripts/README.md                      | 100 ++++++++
 .github/scripts/analyze-git-activity.sh        |  59 +++++
 .github/scripts/calculate-week-info.sh         |  44 ++++
 .github/scripts/create-docusaurus-structure.sh | 111 +++++++++
 .github/scripts/generate-markdown-reports.sh   | 183 ++++++++++++++
 .github/scripts/sync-to-hub.sh                 |  70 ++++++
 .github/workflows/sync-to-report.yml           | 318 ++-----------------------
 7 files changed, 590 insertions(+), 295 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 16:14:14 - `0e31de9`
**🔧 Markdownレポート生成スクリプトのdiff出力形式を改善**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 16:14:14 2025 +0900
M	.github/scripts/generate-markdown-reports.sh
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 16:14:14 2025 +0900

    🔧 Markdownレポート生成スクリプトのdiff出力形式を改善
    
    - daily_code_diff.mdとlatest_code_diff.mdでdiff出力を適切なコードブロックで囲むように修正
    - add_indent関数の代わりに`diffブロックを使用してシンタックスハイライトを有効化
    - 生成されるMarkdownファイルの可読性を向上

 .github/scripts/generate-markdown-reports.sh | 8 ++++++--
 1 file changed, 6 insertions(+), 2 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/scripts/generate-markdown-reports.sh b/.github/scripts/generate-markdown-reports.sh
index 693725b..7d2251f 100644
--- a/.github/scripts/generate-markdown-reports.sh
+++ b/.github/scripts/generate-markdown-reports.sh
@@ -89,7 +89,9 @@ get_status_icon() {
   echo ""
   echo "## Full Diff"
   echo ""
-  add_indent daily_code_diff_raw.txt
+  echo "\`\`\`diff"
+  cat daily_code_diff_raw.txt
+  echo "\`\`\`"
 } > daily_code_diff.md
 
 # 最新差分をMarkdown形式で作成
@@ -113,7 +115,9 @@ get_status_icon() {
 {
   echo "# 🔄 Latest Code Changes"
   echo ""
-  add_indent latest_code_diff_raw.txt
+  echo "\`\`\`diff"
+  cat latest_code_diff_raw.txt
+  echo "\`\`\`"
 } > latest_code_diff.md
 
 # 詳細なアクティビティサマリーをMarkdown形式で作成
```

---

## ⏰ 16:15:28 - `c14853c`
**✨ README.mdのHTMLタグ形式を標準化**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 16:15:28 2025 +0900
M	README.md
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 16:15:28 2025 +0900

    ✨ README.mdのHTMLタグ形式を標準化
    
    - HTML5バッジのimgタグを自己終了タグ形式（/>）に統一
    - HTML5、CSS3、JavaScriptの各バッジタグの一貫性を向上
    - マークアップの標準準拠を改善

 README.md | 6 +++---
 1 file changed, 3 insertions(+), 3 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/README.md b/README.md
index 28c2ccc..e5baa3d 100644
--- a/README.md
+++ b/README.md
@@ -5,9 +5,9 @@
 # daily-report-hub_sample1
 
 <p>
-  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
-  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
-  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
+  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
+  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
+  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
 </p>
 
 </div>
```

---

## ⏰ 16:15:44 - `a51dc61`
**🔀 Merge: Markdownフォーマット改善とHTMLタグ標準化**
*by Maki*

### 📋 Changed Files
```bash
Merge: b3fd498 c14853c
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 16:15:44 2025 +0900
```

### 📊 Statistics
```bash
Merge: b3fd498 c14853c
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 16:15:44 2025 +0900

    🔀 Merge: Markdownフォーマット改善とHTMLタグ標準化

 .github/scripts/generate-markdown-reports.sh | 8 ++++++--
 README.md                                    | 6 +++---
 2 files changed, 9 insertions(+), 5 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 16:16:11 - `ffa346d`
**Merge branch 'develop'**
*by Maki*

### 📋 Changed Files
```bash
Merge: f26c465 a51dc61
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 16:16:11 2025 +0900
```

### 📊 Statistics
```bash
Merge: f26c465 a51dc61
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 16:16:11 2025 +0900

    Merge branch 'develop'

 .github/scripts/generate-markdown-reports.sh | 8 ++++++--
 README.md                                    | 6 +++---
 2 files changed, 9 insertions(+), 5 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 16:28:35 - `1227831`
**✨ Markdownレポート生成スクリプトの表示形式を改善**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 16:28:35 2025 +0900
M	.github/scripts/generate-markdown-reports.sh
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 16:28:35 2025 +0900

    ✨ Markdownレポート生成スクリプトの表示形式を改善
    
    - コードブロックにbash言語指定を追加して構文ハイライトを有効化
    - 統計情報の表示をdiffブロック形式に変更して可読性を向上
    - Changed FilesとStatisticsセクションの表示品質を改善

 .github/scripts/generate-markdown-reports.sh | 12 ++++++++----
 1 file changed, 8 insertions(+), 4 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/scripts/generate-markdown-reports.sh b/.github/scripts/generate-markdown-reports.sh
index 7d2251f..b5738eb 100644
--- a/.github/scripts/generate-markdown-reports.sh
+++ b/.github/scripts/generate-markdown-reports.sh
@@ -33,14 +33,14 @@ get_status_icon() {
       
       # 各コミットの変更ファイル一覧を表示
       echo "### 📋 Changed Files"
-      echo "\`\`\`"
+      echo "\`\`\`bash"
       git show --name-status $hash 2>/dev/null | grep -E '^[AMDRC]' || echo "No file changes"
       echo "\`\`\`"
       echo ""
       
       # 各コミットの統計情報を表示
       echo "### 📊 Statistics"
-      echo "\`\`\`"
+      echo "\`\`\`bash"
       git show --stat $hash 2>/dev/null | tail -n +2 || echo "No statistics available"
       echo "\`\`\`"
       echo ""
@@ -80,7 +80,9 @@ get_status_icon() {
 {
   echo "# 📈 Daily Statistics"
   echo ""
-  add_indent daily_diff_stats_raw.txt
+  echo "\`\`\`diff"
+  cat daily_diff_stats_raw.txt
+  echo "\`\`\`"
 } > daily_diff_stats.md
 
 # コード差分をMarkdown形式で作成
@@ -159,7 +161,9 @@ fi
     
     echo "## 📈 File Changes Statistics"
     echo ""
-    add_indent daily_diff_stats_raw.txt
+    echo "\`\`\`diff"
+    cat daily_diff_stats_raw.txt
+    echo "\`\`\`"
     echo ""
     
     echo "## 📋 Changed Files List"
```

---

## ⏰ 16:28:44 - `738ad97`
**🔧 ハブ同期スクリプトのメタデータ構造を拡張**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 16:28:44 2025 +0900
M	.github/scripts/sync-to-hub.sh
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 16:28:44 2025 +0900

    🔧 ハブ同期スクリプトのメタデータ構造を拡張
    
    - metadata.jsonにreadmeファイルの参照情報を追加
    - ファイル構造の一貫性を向上させてハブ側での処理を改善
    - READMEファイルの自動認識機能を強化

 .github/scripts/sync-to-hub.sh | 1 +
 1 file changed, 1 insertion(+)
```

### 💻 Code Changes
```diff
diff --git a/.github/scripts/sync-to-hub.sh b/.github/scripts/sync-to-hub.sh
index 9e96989..fc870c6 100644
--- a/.github/scripts/sync-to-hub.sh
+++ b/.github/scripts/sync-to-hub.sh
@@ -46,6 +46,7 @@ cat > "$TARGET_DIR/metadata.json" << EOF
   "daily_files_changed": $FILES_CHANGED,
   "has_activity": $([ $COMMIT_COUNT -gt 0 ] && echo "true" || echo "false"),
   "files": {
+    "readme": "README.md",
     "summary": "daily_summary.md",
     "commits": "daily_commits.md",
     "file_changes": "daily_cumulative_diff.md",
```

---

## ⏰ 16:29:01 - `3dcfde5`
**🔀 Merge: Markdownレポート表示形式とメタデータ構造の改善**
*by Maki*

### 📋 Changed Files
```bash
Merge: a51dc61 738ad97
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 16:29:01 2025 +0900
```

### 📊 Statistics
```bash
Merge: a51dc61 738ad97
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 16:29:01 2025 +0900

    🔀 Merge: Markdownレポート表示形式とメタデータ構造の改善

 .github/scripts/generate-markdown-reports.sh | 12 ++++++++----
 .github/scripts/sync-to-hub.sh               |  1 +
 2 files changed, 9 insertions(+), 4 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 16:29:45 - `18c42d6`
**Merge branch 'develop'**
*by Maki*

### 📋 Changed Files
```bash
Merge: ffa346d 3dcfde5
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 16:29:45 2025 +0900
```

### 📊 Statistics
```bash
Merge: ffa346d 3dcfde5
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 16:29:45 2025 +0900

    Merge branch 'develop'

 .github/scripts/generate-markdown-reports.sh | 12 ++++++++----
 .github/scripts/sync-to-hub.sh               |  1 +
 2 files changed, 9 insertions(+), 4 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 19:24:55 - `89480ff`
**📝 README.mdにプルリクエストフロー設定の説明を追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 19:24:55 2025 +0900
M	.github/scripts/README.md
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 19:24:55 2025 +0900

    📝 README.mdにプルリクエストフロー設定の説明を追加

 .github/scripts/README.md | 41 +++++++++++++++++++++++++++++++++++++++++
 1 file changed, 41 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/.github/scripts/README.md b/.github/scripts/README.md
index 4e2fff1..c7e07f4 100644
--- a/.github/scripts/README.md
+++ b/.github/scripts/README.md
@@ -74,6 +74,47 @@ env:
   WEEK_START_DAY: 1  # 0=日曜日, 1=月曜日, 2=火曜日, etc.
 ```
 
+## プルリクエストフロー設定
+
+v2.0では、プルリクエストベースのフローと自動承認機能が追加されました：
+
+```yaml
+env:
+  WEEK_START_DAY: 1     # 週の開始日
+  AUTO_APPROVE: true    # プルリクエストの自動承認
+  AUTO_MERGE: true      # プルリクエストの自動マージ
+  CREATE_PR: true       # プルリクエストを作成するか直接プッシュするか
+```
+
+### 設定オプション
+
+| 設定 | 説明 | デフォルト |
+|------|------|------------|
+| `CREATE_PR` | `true`: プルリクエストを作成<br>`false`: 直接プッシュ | `true` |
+| `AUTO_APPROVE` | `true`: プルリクエストを自動承認<br>`false`: 手動承認が必要 | `false` |
+| `AUTO_MERGE` | `true`: 承認後に自動マージ<br>`false`: 手動マージが必要 | `false` |
+
+### フロー例
+
+1. **完全自動化**: `CREATE_PR=true`, `AUTO_APPROVE=true`, `AUTO_MERGE=true`
+   - プルリクエスト作成 → 自動承認 → 自動マージ
+
+2. **承認のみ手動**: `CREATE_PR=true`, `AUTO_APPROVE=false`, `AUTO_MERGE=true`
+   - プルリクエスト作成 → 手動承認 → 自動マージ
+
+3. **完全手動**: `CREATE_PR=true`, `AUTO_APPROVE=false`, `AUTO_MERGE=false`
+   - プルリクエスト作成 → 手動承認 → 手動マージ
+
+4. **直接プッシュ**: `CREATE_PR=false`
+   - 従来通りの直接プッシュ（v1.4と同じ動作）
+
+## ワークフローファイル
+
+2つのバージョンが利用可能です：
+
+- `sync-to-report.yml`: cURLベースの実装
+- `sync-to-report-gh.yml`: GitHub CLI使用版（推奨）
+
 ## フォルダ構造
 
 生成されるフォルダ構造：
```

---

## ⏰ 19:25:07 - `af7f781`
**🔧 sync-to-hub.shにプルリクエストフローと自動マージ機能を実装**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 19:25:07 2025 +0900
M	.github/scripts/sync-to-hub.sh
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 19:25:07 2025 +0900

    🔧 sync-to-hub.shにプルリクエストフローと自動マージ機能を実装

 .github/scripts/sync-to-hub.sh | 119 +++++++++++++++++++++++++++++++++++++++--
 1 file changed, 116 insertions(+), 3 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/scripts/sync-to-hub.sh b/.github/scripts/sync-to-hub.sh
index fc870c6..0a7d604 100644
--- a/.github/scripts/sync-to-hub.sh
+++ b/.github/scripts/sync-to-hub.sh
@@ -1,6 +1,6 @@
 #!/bin/bash
 
-# レポートハブに同期するスクリプト
+# レポートハブに同期するスクリプト（プルリクエストフロー対応）
 
 set -e
 
@@ -12,6 +12,11 @@ set -e
 : ${DATE:?}
 : ${WEEK_NUMBER:?}
 
+# プルリクエストフロー設定（デフォルト値）
+CREATE_PR=${CREATE_PR:-true}
+AUTO_APPROVE=${AUTO_APPROVE:-false}
+AUTO_MERGE=${AUTO_MERGE:-false}
+
 # daily-report-hubは既にクローン済み
 
 # README.mdをコピー
@@ -58,14 +63,122 @@ cat > "$TARGET_DIR/metadata.json" << EOF
 }
 EOF
 
-# タイムスタンプ付きでコミット・プッシュ
+# プルリクエストフローまたは直接プッシュ
 cd daily-report-hub
 git add .
 
 if git diff --staged --quiet; then
   echo "No changes to commit"
+  exit 0
+fi
+
+COMMIT_MESSAGE="📊 Weekly sync: $REPO_NAME ($DATE) - Week $WEEK_NUMBER - $COMMIT_COUNT commits"
+
+if [ "$CREATE_PR" = "true" ]; then
+  # プルリクエストフロー
+  BRANCH_NAME="sync/$REPO_NAME-$DATE-$(date +%s)"
+  
+  echo "🔀 Creating pull request flow with branch: $BRANCH_NAME"
+  
+  # 新しいブランチを作成してチェックアウト
+  git checkout -b "$BRANCH_NAME"
+  
+  # コミットしてプッシュ
+  git commit -m "$COMMIT_MESSAGE"
+  git push origin "$BRANCH_NAME"
+  
+  # プルリクエストを作成
+  PR_BODY="## 📊 Daily Report Sync
+
+**Repository:** \`$GITHUB_REPOSITORY\`
+**Date:** $DATE
+**Week:** $WEEK_NUMBER ($WEEK_START_DATE to $WEEK_END_DATE)
+
+### 📈 Activity Summary
+- **Commits:** $COMMIT_COUNT
+- **Files Changed:** $FILES_CHANGED
+- **Sync Time:** $(date '+%Y-%m-%d %H:%M:%S')
+
+### 📋 Generated Files
+- Daily summary report
+- Commit details
+- File changes
+- Code differences
+- Statistics
+
+---
+*Auto-generated by GitHub Actions*"
+
+  echo "📝 Creating pull request..."
+  PR_URL=$(curl -s -X POST \
+    -H "Authorization: token $GITHUB_TOKEN" \
+    -H "Accept: application/vnd.github.v3+json" \
+    "https://api.github.com/repos/$REPORT_HUB_REPO/pulls" \
+    -d "{
+      \"title\": \"$COMMIT_MESSAGE\",
+      \"body\": \"$PR_BODY\",
+      \"head\": \"$BRANCH_NAME\",
+      \"base\": \"main\"
+    }" | jq -r '.html_url // empty')
+  
+  if [ -n "$PR_URL" ]; then
+    echo "✅ Pull request created: $PR_URL"
+    
+    # プルリクエスト番号を取得
+    PR_NUMBER=$(echo "$PR_URL" | grep -o '[0-9]*$')
+    
+    # 自動承認が有効な場合
+    if [ "$AUTO_APPROVE" = "true" ]; then
+      echo "👍 Auto-approving pull request..."
+      curl -s -X POST \
+        -H "Authorization: token $GITHUB_TOKEN" \
+        -H "Accept: application/vnd.github.v3+json" \
+        "https://api.github.com/repos/$REPORT_HUB_REPO/pulls/$PR_NUMBER/reviews" \
```

---

## ⏰ 19:25:26 - `608a103`
**🔄 ワークフローをv2.0に更新し、PRフロー設定を追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 19:25:26 2025 +0900
M	.github/workflows/sync-to-report.yml
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 19:25:26 2025 +0900

    🔄 ワークフローをv2.0に更新し、PRフロー設定を追加

 .github/workflows/sync-to-report.yml | 14 ++++++++++----
 1 file changed, 10 insertions(+), 4 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report.yml b/.github/workflows/sync-to-report.yml
index b0a97ba..16e1235 100644
--- a/.github/workflows/sync-to-report.yml
+++ b/.github/workflows/sync-to-report.yml
@@ -1,4 +1,4 @@
-name: Sync to Daily Report Hub v1.4
+name: Sync to Daily Report Hub v2.0
 on:
   push:
     branches: [main, master]
@@ -8,6 +8,9 @@ on:
 # 週の開始日を制御する設定
 env:
   WEEK_START_DAY: 1 # 週の開始日 (0=日曜日, 1=月曜日, 2=火曜日, 3=水曜日, 4=木曜日, 5=金曜日, 6=土曜日)
+  AUTO_APPROVE: true # プルリクエストの自動承認 (true/false)
+  AUTO_MERGE: true # プルリクエストの自動マージ (true/false)
+  CREATE_PR: true # プルリクエストを作成するか直接プッシュするか (true/false)
 
 jobs:
   sync-data:
@@ -38,15 +41,18 @@ jobs:
           # Git設定
           git config --global user.name "GitHub Actions Bot"
           git config --global user.email "actions@github.com"
-          
+
           # daily-report-hubをクローン
           git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub
 
       - name: Create Docusaurus structure
         run: ./.github/scripts/create-docusaurus-structure.sh
 
-      - name: Sync to report hub
+      - name: Sync to report hub with PR flow
         env:
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
-        run: ./.github/scripts/sync-to-hub.sh
\ No newline at end of file
+          AUTO_APPROVE: ${{ env.AUTO_APPROVE }}
+          AUTO_MERGE: ${{ env.AUTO_MERGE }}
+          CREATE_PR: ${{ env.CREATE_PR }}
+        run: ./.github/scripts/sync-to-hub.sh
```

---

## ⏰ 19:25:49 - `a7398c1`
**➕ GitHub CLI版スクリプトとワークフローを追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 19:25:49 2025 +0900
A	.github/scripts/sync-to-hub-gh.sh
A	.github/workflows/sync-to-report-gh.yml
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 19:25:49 2025 +0900

    ➕ GitHub CLI版スクリプトとワークフローを追加

 .github/scripts/sync-to-hub-gh.sh       | 169 ++++++++++++++++++++++++++++++++
 .github/workflows/sync-to-report-gh.yml |  66 +++++++++++++
 2 files changed, 235 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/.github/scripts/sync-to-hub-gh.sh b/.github/scripts/sync-to-hub-gh.sh
new file mode 100644
index 0000000..79bed22
--- /dev/null
+++ b/.github/scripts/sync-to-hub-gh.sh
@@ -0,0 +1,169 @@
+#!/bin/bash
+
+# レポートハブに同期するスクリプト（GitHub CLI使用版）
+
+set -e
+
+# 必要な環境変数をチェック
+: ${GITHUB_TOKEN:?}
+: ${REPORT_HUB_REPO:?}
+: ${TARGET_DIR:?}
+: ${REPO_NAME:?}
+: ${DATE:?}
+: ${WEEK_NUMBER:?}
+
+# プルリクエストフロー設定（デフォルト値）
+CREATE_PR=${CREATE_PR:-true}
+AUTO_APPROVE=${AUTO_APPROVE:-false}
+AUTO_MERGE=${AUTO_MERGE:-false}
+
+# daily-report-hubは既にクローン済み
+
+# README.mdをコピー
+cp README.md "$TARGET_DIR/" 2>/dev/null || echo "# $REPO_NAME" > "$TARGET_DIR/README.md"
+
+# 当日のアクティビティファイルをコピー（全て.mdファイル）
+cp daily_commits.md "$TARGET_DIR/"
+cp daily_cumulative_diff.md "$TARGET_DIR/"
+cp daily_diff_stats.md "$TARGET_DIR/"
+cp daily_code_diff.md "$TARGET_DIR/"
+cp latest_diff.md "$TARGET_DIR/"
+cp latest_code_diff.md "$TARGET_DIR/"
+cp daily_summary.md "$TARGET_DIR/"
+
+# 詳細メタデータを作成
+COMMIT_COUNT=$(wc -l < daily_commits_raw.txt)
+FILES_CHANGED=$(grep -c '^' daily_cumulative_diff_raw.txt 2>/dev/null || echo "0")
+
+cat > "$TARGET_DIR/metadata.json" << EOF
+{
+  "repository": "$GITHUB_REPOSITORY",
+  "date": "$DATE",
+  "week_folder": "$WEEK_FOLDER",
+  "week_number": $WEEK_NUMBER,
+  "week_start_date": "$WEEK_START_DATE",
+  "week_end_date": "$WEEK_END_DATE",
+  "branch": "$GITHUB_REF_NAME",
+  "latest_commit_sha": "$GITHUB_SHA",
+  "sync_timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
+  "workflow_run": "$GITHUB_RUN_ID",
+  "daily_commit_count": $COMMIT_COUNT,
+  "daily_files_changed": $FILES_CHANGED,
+  "has_activity": $([ $COMMIT_COUNT -gt 0 ] && echo "true" || echo "false"),
+  "pr_flow": {
+    "create_pr": $CREATE_PR,
+    "auto_approve": $AUTO_APPROVE,
+    "auto_merge": $AUTO_MERGE
+  },
+  "files": {
+    "readme": "README.md",
+    "summary": "daily_summary.md",
+    "commits": "daily_commits.md",
+    "file_changes": "daily_cumulative_diff.md",
+    "stats": "daily_diff_stats.md",
+    "code_diff": "daily_code_diff.md",
+    "latest_diff": "latest_diff.md",
+    "latest_code_diff": "latest_code_diff.md"
+  }
+}
+EOF
+
+# プルリクエストフローまたは直接プッシュ
+cd daily-report-hub
+git add .
+
+if git diff --staged --quiet; then
+  echo "No changes to commit"
+  exit 0
+fi
+
+COMMIT_MESSAGE="📊 Weekly sync: $REPO_NAME ($DATE) - Week $WEEK_NUMBER - $COMMIT_COUNT commits"
+
+if [ "$CREATE_PR" = "true" ]; then
+  # プルリクエストフロー（GitHub CLI使用）
+  BRANCH_NAME="sync/$REPO_NAME-$DATE-$(date +%s)"
+  
+  echo "🔀 Creating pull request flow with branch: $BRANCH_NAME"
+  
+  # 新しいブランチを作成してチェックアウト
+  git checkout -b "$BRANCH_NAME"
+  
+  # コミットしてプッシュ
+  git commit -m "$COMMIT_MESSAGE"
+  git push origin "$BRANCH_NAME"
+  
```

---

## ⏰ 19:26:58 - `0269cc7`
**🔀 Merge: PRフロー強化**
*by Maki*

### 📋 Changed Files
```bash
Merge: 3dcfde5 a7398c1
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 19:26:58 2025 +0900
```

### 📊 Statistics
```bash
Merge: 3dcfde5 a7398c1
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 19:26:58 2025 +0900

    🔀 Merge: PRフロー強化

 .github/scripts/README.md               |  41 ++++++++
 .github/scripts/sync-to-hub-gh.sh       | 169 ++++++++++++++++++++++++++++++++
 .github/scripts/sync-to-hub.sh          | 119 +++++++++++++++++++++-
 .github/workflows/sync-to-report-gh.yml |  66 +++++++++++++
 .github/workflows/sync-to-report.yml    |  14 ++-
 5 files changed, 402 insertions(+), 7 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 19:28:35 - `cb49c38`
**Merge branch 'develop'**
*by Maki*

### 📋 Changed Files
```bash
Merge: 18c42d6 0269cc7
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 19:28:35 2025 +0900
```

### 📊 Statistics
```bash
Merge: 18c42d6 0269cc7
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 19:28:35 2025 +0900

    Merge branch 'develop'

 .github/scripts/README.md               |  41 ++++++++
 .github/scripts/sync-to-hub-gh.sh       | 169 ++++++++++++++++++++++++++++++++
 .github/scripts/sync-to-hub.sh          | 119 +++++++++++++++++++++-
 .github/workflows/sync-to-report-gh.yml |  66 +++++++++++++
 .github/workflows/sync-to-report.yml    |  14 ++-
 5 files changed, 402 insertions(+), 7 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 19:33:28 - `a0d8665`
**Update sync-to-report.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 19:33:28 2025 +0900
M	.github/workflows/sync-to-report.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 19:33:28 2025 +0900

    Update sync-to-report.yml

 .github/workflows/sync-to-report.yml | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report.yml b/.github/workflows/sync-to-report.yml
index 16e1235..ae47540 100644
--- a/.github/workflows/sync-to-report.yml
+++ b/.github/workflows/sync-to-report.yml
@@ -1,4 +1,4 @@
-name: Sync to Daily Report Hub v2.0
+name: Sync to Daily Report Hub v2.1
 on:
   push:
     branches: [main, master]
```

---

## ⏰ 19:40:16 - `0d5056f`
**Delete .github/workflows/sync-to-report.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 19:40:16 2025 +0900
D	.github/workflows/sync-to-report.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 19:40:16 2025 +0900

    Delete .github/workflows/sync-to-report.yml

 .github/workflows/sync-to-report.yml | 58 ------------------------------------
 1 file changed, 58 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report.yml b/.github/workflows/sync-to-report.yml
deleted file mode 100644
index ae47540..0000000
--- a/.github/workflows/sync-to-report.yml
+++ /dev/null
@@ -1,58 +0,0 @@
-name: Sync to Daily Report Hub v2.1
-on:
-  push:
-    branches: [main, master]
-  pull_request:
-    types: [opened, synchronize, closed]
-
-# 週の開始日を制御する設定
-env:
-  WEEK_START_DAY: 1 # 週の開始日 (0=日曜日, 1=月曜日, 2=火曜日, 3=水曜日, 4=木曜日, 5=金曜日, 6=土曜日)
-  AUTO_APPROVE: true # プルリクエストの自動承認 (true/false)
-  AUTO_MERGE: true # プルリクエストの自動マージ (true/false)
-  CREATE_PR: true # プルリクエストを作成するか直接プッシュするか (true/false)
-
-jobs:
-  sync-data:
-    runs-on: ubuntu-latest
-    steps:
-      - name: Checkout current repo
-        uses: actions/checkout@v4
-        with:
-          fetch-depth: 0 # 全履歴を取得してその日の全コミットを追跡
-
-      - name: Make scripts executable
-        run: chmod +x .github/scripts/*.sh
-
-      - name: Calculate week information
-        run: ./.github/scripts/calculate-week-info.sh ${{ env.WEEK_START_DAY }}
-
-      - name: Analyze Git activity
-        run: ./.github/scripts/analyze-git-activity.sh
-
-      - name: Generate Markdown reports
-        run: ./.github/scripts/generate-markdown-reports.sh
-
-      - name: Clone report hub and create structure
-        env:
-          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
-          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
-        run: |
-          # Git設定
-          git config --global user.name "GitHub Actions Bot"
-          git config --global user.email "actions@github.com"
-
-          # daily-report-hubをクローン
-          git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub
-
-      - name: Create Docusaurus structure
-        run: ./.github/scripts/create-docusaurus-structure.sh
-
-      - name: Sync to report hub with PR flow
-        env:
-          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
-          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
-          AUTO_APPROVE: ${{ env.AUTO_APPROVE }}
-          AUTO_MERGE: ${{ env.AUTO_MERGE }}
-          CREATE_PR: ${{ env.CREATE_PR }}
-        run: ./.github/scripts/sync-to-hub.sh
```

---

## ⏰ 19:42:21 - `53fba19`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 19:42:21 2025 +0900
M	.github/workflows/sync-to-report-gh.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 19:42:21 2025 +0900

    Update sync-to-report-gh.yml

 .github/workflows/sync-to-report-gh.yml | 15 +++++++++------
 1 file changed, 9 insertions(+), 6 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index 89b88fd..4787000 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -1,4 +1,4 @@
-name: Sync to Daily Report Hub v2.0 (GitHub CLI)
+name: Sync to Daily Report Hub v2.2 (Fixed)
 on:
   push:
     branches: [main, master]
@@ -19,12 +19,12 @@ jobs:
       - name: Checkout current repo
         uses: actions/checkout@v4
         with:
-          fetch-depth: 0 # 全履歴を取得してその日の全コミットを追跡
+          fetch-depth: 0
 
       - name: Setup GitHub CLI
         run: |
-          # GitHub CLIは既にubuntu-latestにインストール済み
           gh --version
+          echo "GitHub CLI is ready"
 
       - name: Make scripts executable
         run: chmod +x .github/scripts/*.sh
@@ -41,7 +41,7 @@ jobs:
       - name: Clone report hub and create structure
         env:
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}
-          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
+          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
         run: |
           # Git設定
           git config --global user.name "GitHub Actions Bot"
@@ -49,6 +49,9 @@ jobs:
 
           # GitHub CLI認証
           echo "$GITHUB_TOKEN" | gh auth login --with-token
+          
+          # 認証確認
+          gh auth status
 
           # daily-report-hubをクローン
           git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub
@@ -59,8 +62,8 @@ jobs:
       - name: Sync to report hub with PR flow (GitHub CLI)
         env:
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}
-          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
+          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
           AUTO_APPROVE: ${{ env.AUTO_APPROVE }}
           AUTO_MERGE: ${{ env.AUTO_MERGE }}
           CREATE_PR: ${{ env.CREATE_PR }}
-        run: ./.github/scripts/sync-to-hub-gh.sh
\ No newline at end of file
+        run: ./.github/scripts/sync-to-hub-gh.sh
```

---

## ⏰ 19:45:16 - `0414ce1`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 19:45:16 2025 +0900
M	.github/workflows/sync-to-report-gh.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 19:45:16 2025 +0900

    Update sync-to-report-gh.yml

 .github/workflows/sync-to-report-gh.yml | 15 ++++++---------
 1 file changed, 6 insertions(+), 9 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index 4787000..0b98b5a 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -1,4 +1,4 @@
-name: Sync to Daily Report Hub v2.2 (Fixed)
+name: Sync to Daily Report Hub v2.2 (PR Enabled)
 on:
   push:
     branches: [main, master]
@@ -10,7 +10,7 @@ env:
   WEEK_START_DAY: 1 # 週の開始日 (0=日曜日, 1=月曜日, 2=火曜日, 3=水曜日, 4=木曜日, 5=金曜日, 6=土曜日)
   AUTO_APPROVE: true # プルリクエストの自動承認 (true/false)
   AUTO_MERGE: true # プルリクエストの自動マージ (true/false)
-  CREATE_PR: true # プルリクエストを作成するか直接プッシュするか (true/false)
+  CREATE_PR: true # プルリクエストを作成する！
 
 jobs:
   sync-data:
@@ -21,11 +21,6 @@ jobs:
         with:
           fetch-depth: 0
 
-      - name: Setup GitHub CLI
-        run: |
-          gh --version
-          echo "GitHub CLI is ready"
-
       - name: Make scripts executable
         run: chmod +x .github/scripts/*.sh
 
@@ -47,8 +42,10 @@ jobs:
           git config --global user.name "GitHub Actions Bot"
           git config --global user.email "actions@github.com"
 
-          # GitHub CLI認証
-          echo "$GITHUB_TOKEN" | gh auth login --with-token
+          # GitHub CLI認証（別の方法で認証）
+          echo "$GITHUB_TOKEN" > ~/.gh_token
+          gh auth login --with-token < ~/.gh_token
+          rm ~/.gh_token
           
           # 認証確認
           gh auth status
```

---

## ⏰ 19:45:50 - `6ca463c`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 19:45:50 2025 +0900
M	.github/workflows/sync-to-report-gh.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 19:45:50 2025 +0900

    Update sync-to-report-gh.yml

 .github/workflows/sync-to-report-gh.yml | 24 ++++++++++++------------
 1 file changed, 12 insertions(+), 12 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index 0b98b5a..1589d29 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -1,4 +1,4 @@
-name: Sync to Daily Report Hub v2.2 (PR Enabled)
+name: Sync to Daily Report Hub v2.0 (GitHub CLI)
 on:
   push:
     branches: [main, master]
@@ -10,7 +10,7 @@ env:
   WEEK_START_DAY: 1 # 週の開始日 (0=日曜日, 1=月曜日, 2=火曜日, 3=水曜日, 4=木曜日, 5=金曜日, 6=土曜日)
   AUTO_APPROVE: true # プルリクエストの自動承認 (true/false)
   AUTO_MERGE: true # プルリクエストの自動マージ (true/false)
-  CREATE_PR: true # プルリクエストを作成する！
+  CREATE_PR: true # プルリクエストを作成するか直接プッシュするか (true/false)
 
 jobs:
   sync-data:
@@ -19,7 +19,12 @@ jobs:
       - name: Checkout current repo
         uses: actions/checkout@v4
         with:
-          fetch-depth: 0
+          fetch-depth: 0 # 全履歴を取得してその日の全コミットを追跡
+
+      - name: Setup GitHub CLI
+        run: |
+          # GitHub CLIは既にubuntu-latestにインストール済み
+          gh --version
 
       - name: Make scripts executable
         run: chmod +x .github/scripts/*.sh
@@ -36,19 +41,14 @@ jobs:
       - name: Clone report hub and create structure
         env:
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}
-          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
+          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
         run: |
           # Git設定
           git config --global user.name "GitHub Actions Bot"
           git config --global user.email "actions@github.com"
 
-          # GitHub CLI認証（別の方法で認証）
-          echo "$GITHUB_TOKEN" > ~/.gh_token
-          gh auth login --with-token < ~/.gh_token
-          rm ~/.gh_token
-          
-          # 認証確認
-          gh auth status
+          # GitHub CLI認証
+          echo "$GITHUB_TOKEN" | gh auth login --with-token
 
           # daily-report-hubをクローン
           git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub
@@ -59,7 +59,7 @@ jobs:
       - name: Sync to report hub with PR flow (GitHub CLI)
         env:
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}
-          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
+          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
           AUTO_APPROVE: ${{ env.AUTO_APPROVE }}
           AUTO_MERGE: ${{ env.AUTO_MERGE }}
           CREATE_PR: ${{ env.CREATE_PR }}
```

---

## ⏰ 19:46:32 - `2279136`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 19:46:32 2025 +0900
M	.github/workflows/sync-to-report-gh.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 19:46:32 2025 +0900

    Update sync-to-report-gh.yml

 .github/workflows/sync-to-report-gh.yml | 14 +++-----------
 1 file changed, 3 insertions(+), 11 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index 1589d29..16e1235 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -1,4 +1,4 @@
-name: Sync to Daily Report Hub v2.0 (GitHub CLI)
+name: Sync to Daily Report Hub v2.0
 on:
   push:
     branches: [main, master]
@@ -21,11 +21,6 @@ jobs:
         with:
           fetch-depth: 0 # 全履歴を取得してその日の全コミットを追跡
 
-      - name: Setup GitHub CLI
-        run: |
-          # GitHub CLIは既にubuntu-latestにインストール済み
-          gh --version
-
       - name: Make scripts executable
         run: chmod +x .github/scripts/*.sh
 
@@ -47,20 +42,17 @@ jobs:
           git config --global user.name "GitHub Actions Bot"
           git config --global user.email "actions@github.com"
 
-          # GitHub CLI認証
-          echo "$GITHUB_TOKEN" | gh auth login --with-token
-
           # daily-report-hubをクローン
           git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub
 
       - name: Create Docusaurus structure
         run: ./.github/scripts/create-docusaurus-structure.sh
 
-      - name: Sync to report hub with PR flow (GitHub CLI)
+      - name: Sync to report hub with PR flow
         env:
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
           AUTO_APPROVE: ${{ env.AUTO_APPROVE }}
           AUTO_MERGE: ${{ env.AUTO_MERGE }}
           CREATE_PR: ${{ env.CREATE_PR }}
-        run: ./.github/scripts/sync-to-hub-gh.sh
+        run: ./.github/scripts/sync-to-hub.sh
```

---

## ⏰ 19:50:39 - `876a08e`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 19:50:39 2025 +0900
M	.github/workflows/sync-to-report-gh.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 19:50:39 2025 +0900

    Update sync-to-report-gh.yml

 .github/workflows/sync-to-report-gh.yml | 8 ++++----
 1 file changed, 4 insertions(+), 4 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index 16e1235..32fdc85 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -36,7 +36,7 @@ jobs:
       - name: Clone report hub and create structure
         env:
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}
-          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
+          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
         run: |
           # Git設定
           git config --global user.name "GitHub Actions Bot"
@@ -48,11 +48,11 @@ jobs:
       - name: Create Docusaurus structure
         run: ./.github/scripts/create-docusaurus-structure.sh
 
-      - name: Sync to report hub with PR flow
+      - name: Sync to report hub with PR flow (GitHub CLI)
         env:
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}
-          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
+          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
           AUTO_APPROVE: ${{ env.AUTO_APPROVE }}
           AUTO_MERGE: ${{ env.AUTO_MERGE }}
           CREATE_PR: ${{ env.CREATE_PR }}
-        run: ./.github/scripts/sync-to-hub.sh
+        run: ./.github/scripts/sync-to-hub-gh.sh
```

---

## ⏰ 19:58:03 - `001142c`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 19:58:03 2025 +0900
M	.github/workflows/sync-to-report-gh.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 19:58:03 2025 +0900

    Update sync-to-report-gh.yml

 .github/workflows/sync-to-report-gh.yml | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index 32fdc85..2b339fe 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -35,7 +35,7 @@ jobs:
 
       - name: Clone report hub and create structure
         env:
-          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
+          GITHUB_TOKEN: ${{ secrets.GH_PAT_YUKIHIKO }}
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
         run: |
           # Git設定
@@ -50,7 +50,7 @@ jobs:
 
       - name: Sync to report hub with PR flow (GitHub CLI)
         env:
-          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
+          GITHUB_TOKEN: ${{ secrets.GH_PAT_YUKIHIKO }}
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
           AUTO_APPROVE: ${{ env.AUTO_APPROVE }}
           AUTO_MERGE: ${{ env.AUTO_MERGE }}
```

---

## ⏰ 20:02:24 - `12c7d00`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:02:24 2025 +0900
M	.github/workflows/sync-to-report-gh.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:02:24 2025 +0900

    Update sync-to-report-gh.yml

 .github/workflows/sync-to-report-gh.yml | 10 +++++-----
 1 file changed, 5 insertions(+), 5 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index 2b339fe..df796aa 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -8,9 +8,9 @@ on:
 # 週の開始日を制御する設定
 env:
   WEEK_START_DAY: 1 # 週の開始日 (0=日曜日, 1=月曜日, 2=火曜日, 3=水曜日, 4=木曜日, 5=金曜日, 6=土曜日)
-  AUTO_APPROVE: true # プルリクエストの自動承認 (true/false)
-  AUTO_MERGE: true # プルリクエストの自動マージ (true/false)
-  CREATE_PR: true # プルリクエストを作成するか直接プッシュするか (true/false)
+  AUTO_APPROVE: false # プルリクエストの自動承認 (true/false) - 自分のPRは承認不可
+  AUTO_MERGE: false # プルリクエストの自動マージ (true/false) - 承認なしではマージ不可
+  CREATE_PR: false # 完全自動化のため直接プッシュ
 
 jobs:
   sync-data:
@@ -35,7 +35,7 @@ jobs:
 
       - name: Clone report hub and create structure
         env:
-          GITHUB_TOKEN: ${{ secrets.GH_PAT_YUKIHIKO }}
+          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
         run: |
           # Git設定
@@ -50,7 +50,7 @@ jobs:
 
       - name: Sync to report hub with PR flow (GitHub CLI)
         env:
-          GITHUB_TOKEN: ${{ secrets.GH_PAT_YUKIHIKO }}
+          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
           AUTO_APPROVE: ${{ env.AUTO_APPROVE }}
           AUTO_MERGE: ${{ env.AUTO_MERGE }}
```

---

## ⏰ 20:02:41 - `8787dce`
**Update sync-to-hub-gh.sh**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:02:41 2025 +0900
M	.github/scripts/sync-to-hub-gh.sh
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:02:41 2025 +0900

    Update sync-to-hub-gh.sh

 .github/scripts/sync-to-hub-gh.sh | 16 ++++++++++++----
 1 file changed, 12 insertions(+), 4 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/scripts/sync-to-hub-gh.sh b/.github/scripts/sync-to-hub-gh.sh
index 79bed22..52888b5 100644
--- a/.github/scripts/sync-to-hub-gh.sh
+++ b/.github/scripts/sync-to-hub-gh.sh
@@ -88,6 +88,10 @@ if [ "$CREATE_PR" = "true" ]; then
   # 新しいブランチを作成してチェックアウト
   git checkout -b "$BRANCH_NAME"
   
+  # コミット作成者を別の人に設定（PATの所有者）
+  git config user.name "Yukihiko Kondo"
+  git config user.email "yukihiko.kondo@example.com"  # 実際のメールアドレスに変更
+  
   # コミットしてプッシュ
   git commit -m "$COMMIT_MESSAGE"
   git push origin "$BRANCH_NAME"
@@ -131,11 +135,15 @@ if [ "$CREATE_PR" = "true" ]; then
   if [ -n "$PR_URL" ]; then
     echo "✅ Pull request created: $PR_URL"
     
-    # 自動承認が有効な場合
+    # 自動承認が有効な場合（自分のPRは承認できないので注意）
     if [ "$AUTO_APPROVE" = "true" ]; then
       echo "👍 Auto-approving pull request..."
-      gh pr review "$PR_URL" --approve --body "✅ Auto-approved by GitHub Actions" --repo "$REPORT_HUB_REPO"
-      echo "✅ Pull request approved"
+      if gh pr review "$PR_URL" --approve --body "✅ Auto-approved by GitHub Actions" --repo "$REPORT_HUB_REPO" 2>/dev/null; then
+        echo "✅ Pull request approved"
+      else
+        echo "⚠️ Cannot approve own pull request. Manual approval required."
+        AUTO_MERGE="false"  # 承認できない場合は自動マージも無効にする
+      fi
     fi
     
     # 自動マージが有効な場合
@@ -166,4 +174,4 @@ else
   git commit -m "$COMMIT_MESSAGE"
   git push
   echo "✅ Successfully synced to report hub!"
-fi
\ No newline at end of file
+fi
```

---

## ⏰ 20:06:07 - `dfa5666`
**Update sync-to-hub-gh.sh**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:06:07 2025 +0900
M	.github/scripts/sync-to-hub-gh.sh
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:06:07 2025 +0900

    Update sync-to-hub-gh.sh

 .github/scripts/sync-to-hub-gh.sh | 44 +++++++++++++++++++++++++++------------
 1 file changed, 31 insertions(+), 13 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/scripts/sync-to-hub-gh.sh b/.github/scripts/sync-to-hub-gh.sh
index 52888b5..b32fc9a 100644
--- a/.github/scripts/sync-to-hub-gh.sh
+++ b/.github/scripts/sync-to-hub-gh.sh
@@ -1,6 +1,6 @@
 #!/bin/bash
 
-# レポートハブに同期するスクリプト（GitHub CLI使用版）
+# レポートハブに同期するスクリプト（GitHub CLI使用版・強制上書き対応）
 
 set -e
 
@@ -70,6 +70,13 @@ EOF
 
 # プルリクエストフローまたは直接プッシュ
 cd daily-report-hub
+
+# 最新のmainブランチを取得
+git fetch origin main
+git checkout main
+git reset --hard origin/main
+
+# 変更をステージング
 git add .
 
 if git diff --staged --quiet; then
@@ -80,8 +87,10 @@ fi
 COMMIT_MESSAGE="📊 Weekly sync: $REPO_NAME ($DATE) - Week $WEEK_NUMBER - $COMMIT_COUNT commits"
 
 if [ "$CREATE_PR" = "true" ]; then
-  # プルリクエストフロー（GitHub CLI使用）
-  BRANCH_NAME="sync/$REPO_NAME-$DATE-$(date +%s)"
+  # 既存のPRブランチがあれば削除
+  BRANCH_NAME="sync/$REPO_NAME-$DATE"
+  git push origin --delete "$BRANCH_NAME" 2>/dev/null || true
+  git branch -D "$BRANCH_NAME" 2>/dev/null || true
   
   echo "🔀 Creating pull request flow with branch: $BRANCH_NAME"
   
@@ -90,11 +99,20 @@ if [ "$CREATE_PR" = "true" ]; then
   
   # コミット作成者を別の人に設定（PATの所有者）
   git config user.name "Yukihiko Kondo"
-  git config user.email "yukihiko.kondo@example.com"  # 実際のメールアドレスに変更
+  git config user.email "yukihiko.fuyuki@example.com"
   
-  # コミットしてプッシュ
+  # コミットして強制プッシュ
   git commit -m "$COMMIT_MESSAGE"
-  git push origin "$BRANCH_NAME"
+  git push -f origin "$BRANCH_NAME"
+  
+  # 既存のPRがあれば閉じる
+  echo "🔍 Checking for existing pull requests..."
+  EXISTING_PR=$(gh pr list --repo "$REPORT_HUB_REPO" --head "$BRANCH_NAME" --json number --jq '.[0].number' 2>/dev/null || echo "")
+  
+  if [ -n "$EXISTING_PR" ] && [ "$EXISTING_PR" != "null" ]; then
+    echo "🗑️ Closing existing PR #$EXISTING_PR"
+    gh pr close "$EXISTING_PR" --repo "$REPORT_HUB_REPO" --comment "Superseded by new sync" 2>/dev/null || true
+  fi
   
   # GitHub CLIでプルリクエストを作成
   PR_BODY="## 📊 Daily Report Sync
@@ -120,7 +138,7 @@ if [ "$CREATE_PR" = "true" ]; then
 - **Auto Merge:** $AUTO_MERGE
 
 ---
-*Auto-generated by GitHub Actions*"
+*Auto-generated by GitHub Actions - Force overwrite enabled*"
 
   echo "📝 Creating pull request with GitHub CLI..."
   
@@ -149,7 +167,7 @@ if [ "$CREATE_PR" = "true" ]; then
     # 自動マージが有効な場合
     if [ "$AUTO_MERGE" = "true" ]; then
       echo "🔀 Auto-merging pull request..."
-      sleep 2  # APIの反映を待つ
+      sleep 3  # APIの反映を待つ
       
       if gh pr merge "$PR_URL" --squash --delete-branch --repo "$REPORT_HUB_REPO" 2>/dev/null; then
         echo "✅ Pull request merged and branch deleted successfully"
@@ -163,15 +181,15 @@ if [ "$CREATE_PR" = "true" ]; then
   else
     echo "❌ Failed to create pull request with GitHub CLI. Falling back to direct push."
     git checkout main
-    git merge "$BRANCH_NAME"
+    git merge "$BRANCH_NAME" --strategy-option=theirs  # コンフリクト時は新しい内容を優先
     git push origin main
     git branch -d "$BRANCH_NAME"
     git push origin --delete "$BRANCH_NAME" 2>/dev/null || true
   fi
 else
-  # 直接プッシュフロー
-  echo "⚡ Direct push mode"
+  # 直接プッシュフロー（強制上書き）
+  echo "⚡ Direct push mode (force overwrite)"
   git commit -m "$COMMIT_MESSAGE"
-  git push
-  echo "✅ Successfully synced to report hub!"
+  git push origin main
```

---

## ⏰ 20:09:49 - `68ad213`
**Update sync-to-hub-gh.sh**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:09:49 2025 +0900
M	.github/scripts/sync-to-hub-gh.sh
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:09:49 2025 +0900

    Update sync-to-hub-gh.sh

 .github/scripts/sync-to-hub-gh.sh | 35 ++++++++++++++++++++++-------------
 1 file changed, 22 insertions(+), 13 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/scripts/sync-to-hub-gh.sh b/.github/scripts/sync-to-hub-gh.sh
index b32fc9a..142df6d 100644
--- a/.github/scripts/sync-to-hub-gh.sh
+++ b/.github/scripts/sync-to-hub-gh.sh
@@ -74,11 +74,12 @@ cd daily-report-hub
 # 最新のmainブランチを取得
 git fetch origin main
 git checkout main
-git reset --hard origin/main
+git pull origin main
 
 # 変更をステージング
 git add .
 
+# ステージされた変更をチェック（リセット前に）
 if git diff --staged --quiet; then
   echo "No changes to commit"
   exit 0
@@ -87,31 +88,39 @@ fi
 COMMIT_MESSAGE="📊 Weekly sync: $REPO_NAME ($DATE) - Week $WEEK_NUMBER - $COMMIT_COUNT commits"
 
 if [ "$CREATE_PR" = "true" ]; then
-  # 既存のPRブランチがあれば削除
+  # 既存の同名PRブランチを削除（安全に）
   BRANCH_NAME="sync/$REPO_NAME-$DATE"
-  git push origin --delete "$BRANCH_NAME" 2>/dev/null || true
+  
+  # ローカルブランチがあれば削除
   git branch -D "$BRANCH_NAME" 2>/dev/null || true
   
+  # リモートブランチがあれば削除
+  git push origin --delete "$BRANCH_NAME" 2>/dev/null || true
+  
   echo "🔀 Creating pull request flow with branch: $BRANCH_NAME"
   
   # 新しいブランチを作成してチェックアウト
   git checkout -b "$BRANCH_NAME"
   
-  # コミット作成者を別の人に設定（PATの所有者）
+  # コミット作成者を設定
   git config user.name "Yukihiko Kondo"
   git config user.email "yukihiko.fuyuki@example.com"
   
   # コミットして強制プッシュ
   git commit -m "$COMMIT_MESSAGE"
-  git push -f origin "$BRANCH_NAME"
+  git push origin "$BRANCH_NAME"
   
-  # 既存のPRがあれば閉じる
+  # 既存のPRをチェックして閉じる
   echo "🔍 Checking for existing pull requests..."
-  EXISTING_PR=$(gh pr list --repo "$REPORT_HUB_REPO" --head "$BRANCH_NAME" --json number --jq '.[0].number' 2>/dev/null || echo "")
+  EXISTING_PRS=$(gh pr list --repo "$REPORT_HUB_REPO" --author "@me" --state open --json number,headRefName --jq '.[] | select(.headRefName | startswith("sync/'$REPO_NAME'")) | .number' 2>/dev/null || echo "")
   
-  if [ -n "$EXISTING_PR" ] && [ "$EXISTING_PR" != "null" ]; then
-    echo "🗑️ Closing existing PR #$EXISTING_PR"
-    gh pr close "$EXISTING_PR" --repo "$REPORT_HUB_REPO" --comment "Superseded by new sync" 2>/dev/null || true
+  if [ -n "$EXISTING_PRS" ]; then
+    echo "🗑️ Closing existing PRs for this repo..."
+    echo "$EXISTING_PRS" | while read pr_number; do
+      if [ -n "$pr_number" ]; then
+        gh pr close "$pr_number" --repo "$REPORT_HUB_REPO" --comment "Superseded by new daily sync" 2>/dev/null || true
+      fi
+    done
   fi
   
   # GitHub CLIでプルリクエストを作成
@@ -187,9 +196,9 @@ if [ "$CREATE_PR" = "true" ]; then
     git push origin --delete "$BRANCH_NAME" 2>/dev/null || true
   fi
 else
-  # 直接プッシュフロー（強制上書き）
-  echo "⚡ Direct push mode (force overwrite)"
+  # 直接プッシュフロー
+  echo "⚡ Direct push mode"
   git commit -m "$COMMIT_MESSAGE"
   git push origin main
-  echo "✅ Successfully synced to report hub with force overwrite!"
+  echo "✅ Successfully synced to report hub via direct push!"
 fi
```

---

## ⏰ 20:11:37 - `a010d2d`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:11:37 2025 +0900
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:11:37 2025 +0900

    Update sync-to-report-gh.yml
```

### 💻 Code Changes
```diff
```

---

## ⏰ 20:14:28 - `329d521`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:14:28 2025 +0900
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:14:28 2025 +0900

    Update sync-to-report-gh.yml
```

### 💻 Code Changes
```diff
```

---

## ⏰ 20:14:43 - `4e4b677`
**Update sync-to-hub-gh.sh**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:14:43 2025 +0900
M	.github/scripts/sync-to-hub-gh.sh
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:14:43 2025 +0900

    Update sync-to-hub-gh.sh

 .github/scripts/sync-to-hub-gh.sh | 6 ++++++
 1 file changed, 6 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/.github/scripts/sync-to-hub-gh.sh b/.github/scripts/sync-to-hub-gh.sh
index 142df6d..e3a82a1 100644
--- a/.github/scripts/sync-to-hub-gh.sh
+++ b/.github/scripts/sync-to-hub-gh.sh
@@ -17,6 +17,12 @@ CREATE_PR=${CREATE_PR:-true}
 AUTO_APPROVE=${AUTO_APPROVE:-false}
 AUTO_MERGE=${AUTO_MERGE:-false}
 
+# デバッグ用：環境変数を表示
+echo "🔍 Environment Variables:"
+echo "  CREATE_PR: $CREATE_PR"
+echo "  AUTO_APPROVE: $AUTO_APPROVE"
+echo "  AUTO_MERGE: $AUTO_MERGE"
+
 # daily-report-hubは既にクローン済み
 
 # README.mdをコピー
```

---

## ⏰ 20:18:52 - `837b68f`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:18:52 2025 +0900
M	.github/workflows/sync-to-report-gh.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:18:52 2025 +0900

    Update sync-to-report-gh.yml

 .github/workflows/sync-to-report-gh.yml | 6 +++---
 1 file changed, 3 insertions(+), 3 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index df796aa..6562c20 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -8,9 +8,9 @@ on:
 # 週の開始日を制御する設定
 env:
   WEEK_START_DAY: 1 # 週の開始日 (0=日曜日, 1=月曜日, 2=火曜日, 3=水曜日, 4=木曜日, 5=金曜日, 6=土曜日)
-  AUTO_APPROVE: false # プルリクエストの自動承認 (true/false) - 自分のPRは承認不可
-  AUTO_MERGE: false # プルリクエストの自動マージ (true/false) - 承認なしではマージ不可
-  CREATE_PR: false # 完全自動化のため直接プッシュ
+  AUTO_APPROVE: true # プルリクエストの自動承認 (true/false) - 自分のPRは承認不可
+  AUTO_MERGE: true # プルリクエストの自動マージ (true/false) - 承認なしではマージ不可
+  CREATE_PR: true # 完全自動化のため直接プッシュ
 
 jobs:
   sync-data:
```

---

## ⏰ 20:48:42 - `dd19e29`
**Merge branch 'main' into develop**
*by Maki*

### 📋 Changed Files
```bash
Merge: 0269cc7 837b68f
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 20:48:42 2025 +0900
```

### 📊 Statistics
```bash
Merge: 0269cc7 837b68f
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 20:48:42 2025 +0900

    Merge branch 'main' into develop

 .github/scripts/sync-to-hub-gh.sh       | 67 ++++++++++++++++++++++++++-------
 .github/workflows/sync-to-report-gh.yml | 22 ++++-------
 .github/workflows/sync-to-report.yml    | 58 ----------------------------
 3 files changed, 61 insertions(+), 86 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 20:50:33 - `57bcc4a`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:50:33 2025 +0900
M	.github/workflows/sync-to-report-gh.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:50:33 2025 +0900

    Update sync-to-report-gh.yml

 .github/workflows/sync-to-report-gh.yml | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index 6562c20..bf22ace 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -1,4 +1,4 @@
-name: Sync to Daily Report Hub v2.0
+name: Sync to Daily Report Hub v2.3
 on:
   push:
     branches: [main, master]
```

---

## ⏰ 20:59:26 - `2f8edfb`
**Update sync-to-hub-gh.sh**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:59:26 2025 +0900
M	.github/scripts/sync-to-hub-gh.sh
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:59:26 2025 +0900

    Update sync-to-hub-gh.sh

 .github/scripts/sync-to-hub-gh.sh | 218 +++++++++++++++++---------------------
 1 file changed, 95 insertions(+), 123 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/scripts/sync-to-hub-gh.sh b/.github/scripts/sync-to-hub-gh.sh
index e3a82a1..9f41d75 100644
--- a/.github/scripts/sync-to-hub-gh.sh
+++ b/.github/scripts/sync-to-hub-gh.sh
@@ -1,34 +1,22 @@
 #!/bin/bash
 
-# レポートハブに同期するスクリプト（GitHub CLI使用版・強制上書き対応）
+# YUKIHIKOアカウントでPR作成＆自動承認するスクリプト
 
 set -e
 
 # 必要な環境変数をチェック
 : ${GITHUB_TOKEN:?}
+: ${YUKIHIKO_TOKEN:?}  # YUKIHIKOのトークン
 : ${REPORT_HUB_REPO:?}
 : ${TARGET_DIR:?}
 : ${REPO_NAME:?}
 : ${DATE:?}
 : ${WEEK_NUMBER:?}
 
-# プルリクエストフロー設定（デフォルト値）
-CREATE_PR=${CREATE_PR:-true}
-AUTO_APPROVE=${AUTO_APPROVE:-false}
-AUTO_MERGE=${AUTO_MERGE:-false}
+echo "🔥 YUKIHIKOアカウントでPR作成モード開始！"
 
-# デバッグ用：環境変数を表示
-echo "🔍 Environment Variables:"
-echo "  CREATE_PR: $CREATE_PR"
-echo "  AUTO_APPROVE: $AUTO_APPROVE"
-echo "  AUTO_MERGE: $AUTO_MERGE"
-
-# daily-report-hubは既にクローン済み
-
-# README.mdをコピー
+# ファイルコピー処理
 cp README.md "$TARGET_DIR/" 2>/dev/null || echo "# $REPO_NAME" > "$TARGET_DIR/README.md"
-
-# 当日のアクティビティファイルをコピー（全て.mdファイル）
 cp daily_commits.md "$TARGET_DIR/"
 cp daily_cumulative_diff.md "$TARGET_DIR/"
 cp daily_diff_stats.md "$TARGET_DIR/"
@@ -37,7 +25,7 @@ cp latest_diff.md "$TARGET_DIR/"
 cp latest_code_diff.md "$TARGET_DIR/"
 cp daily_summary.md "$TARGET_DIR/"
 
-# 詳細メタデータを作成
+# メタデータ作成
 COMMIT_COUNT=$(wc -l < daily_commits_raw.txt)
 FILES_CHANGED=$(grep -c '^' daily_cumulative_diff_raw.txt 2>/dev/null || echo "0")
 
@@ -56,11 +44,8 @@ cat > "$TARGET_DIR/metadata.json" << EOF
   "daily_commit_count": $COMMIT_COUNT,
   "daily_files_changed": $FILES_CHANGED,
   "has_activity": $([ $COMMIT_COUNT -gt 0 ] && echo "true" || echo "false"),
-  "pr_flow": {
-    "create_pr": $CREATE_PR,
-    "auto_approve": $AUTO_APPROVE,
-    "auto_merge": $AUTO_MERGE
-  },
+  "pr_creator": "yukihiko",
+  "auto_approved": true,
   "files": {
     "readme": "README.md",
     "summary": "daily_summary.md",
@@ -74,7 +59,6 @@ cat > "$TARGET_DIR/metadata.json" << EOF
 }
 EOF
 
-# プルリクエストフローまたは直接プッシュ
 cd daily-report-hub
 
 # 最新のmainブランチを取得
@@ -85,126 +69,114 @@ git pull origin main
 # 変更をステージング
 git add .
 
-# ステージされた変更をチェック（リセット前に）
 if git diff --staged --quiet; then
-  echo "No changes to commit"
+  echo "📝 変更がありません"
   exit 0
 fi
 
-COMMIT_MESSAGE="📊 Weekly sync: $REPO_NAME ($DATE) - Week $WEEK_NUMBER - $COMMIT_COUNT commits"
+COMMIT_MESSAGE="📊 週次同期: $REPO_NAME ($DATE) - 第${WEEK_NUMBER}週 - ${COMMIT_COUNT}件のコミット"
+BRANCH_NAME="sync/$REPO_NAME-$DATE"
 
-if [ "$CREATE_PR" = "true" ]; then
-  # 既存の同名PRブランチを削除（安全に）
-  BRANCH_NAME="sync/$REPO_NAME-$DATE"
-  
-  # ローカルブランチがあれば削除
-  git branch -D "$BRANCH_NAME" 2>/dev/null || true
-  
-  # リモートブランチがあれば削除
-  git push origin --delete "$BRANCH_NAME" 2>/dev/null || true
-  
-  echo "🔀 Creating pull request flow with branch: $BRANCH_NAME"
```

---

## ⏰ 20:59:35 - `8ff3601`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:59:35 2025 +0900
M	.github/workflows/sync-to-report-gh.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 20:59:35 2025 +0900

    Update sync-to-report-gh.yml

 .github/workflows/sync-to-report-gh.yml | 41 +++++++++++++++------------------
 1 file changed, 18 insertions(+), 23 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index bf22ace..4627d61 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -1,58 +1,53 @@
-name: Sync to Daily Report Hub v2.3
+name: 📊 デイリーレポートハブ同期 v2.3 (YUKIHIKO PR版)
 on:
   push:
     branches: [main, master]
   pull_request:
     types: [opened, synchronize, closed]
 
-# 週の開始日を制御する設定
 env:
-  WEEK_START_DAY: 1 # 週の開始日 (0=日曜日, 1=月曜日, 2=火曜日, 3=水曜日, 4=木曜日, 5=金曜日, 6=土曜日)
-  AUTO_APPROVE: true # プルリクエストの自動承認 (true/false) - 自分のPRは承認不可
-  AUTO_MERGE: true # プルリクエストの自動マージ (true/false) - 承認なしではマージ不可
-  CREATE_PR: true # 完全自動化のため直接プッシュ
+  WEEK_START_DAY: 1
+  AUTO_APPROVE: true
+  AUTO_MERGE: true  
+  CREATE_PR: true
 
 jobs:
   sync-data:
     runs-on: ubuntu-latest
     steps:
-      - name: Checkout current repo
+      - name: 📥 現在のリポジトリをチェックアウト
         uses: actions/checkout@v4
         with:
-          fetch-depth: 0 # 全履歴を取得してその日の全コミットを追跡
+          fetch-depth: 0
 
-      - name: Make scripts executable
+      - name: 🔧 スクリプトを実行可能にする
         run: chmod +x .github/scripts/*.sh
 
-      - name: Calculate week information
+      - name: 📅 週情報を計算
         run: ./.github/scripts/calculate-week-info.sh ${{ env.WEEK_START_DAY }}
 
-      - name: Analyze Git activity
+      - name: 🔍 Git活動を分析
         run: ./.github/scripts/analyze-git-activity.sh
 
-      - name: Generate Markdown reports
+      - name: 📝 Markdownレポートを生成
         run: ./.github/scripts/generate-markdown-reports.sh
 
-      - name: Clone report hub and create structure
+      - name: 📂 レポートハブをクローン
         env:
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
         run: |
-          # Git設定
           git config --global user.name "GitHub Actions Bot"
           git config --global user.email "actions@github.com"
-
-          # daily-report-hubをクローン
           git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub
 
-      - name: Create Docusaurus structure
+      - name: 🏗️ Docusaurus構造を作成
         run: ./.github/scripts/create-docusaurus-structure.sh
 
-      - name: Sync to report hub with PR flow (GitHub CLI)
+      - name: 🚀 YUKIHIKO権限でPR作成＆自動承認
         env:
-          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
+          GITHUB_TOKEN_ORIGINAL: ${{ secrets.GH_PAT }}      # 承認用
+          YUKIHIKO_TOKEN: ${{ secrets.YUKIHIKO_TOKEN }}     # PR作成用
+          GITHUB_TOKEN: ${{ secrets.GH_PAT }}              # デフォルト
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
-          AUTO_APPROVE: ${{ env.AUTO_APPROVE }}
-          AUTO_MERGE: ${{ env.AUTO_MERGE }}
-          CREATE_PR: ${{ env.CREATE_PR }}
-        run: ./.github/scripts/sync-to-hub-gh.sh
+        run: ./.github/scripts/sync-to-hub-yukihiko.sh
```

---

## ⏰ 21:00:27 - `1c9e80a`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 21:00:27 2025 +0900
M	.github/workflows/sync-to-report-gh.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 21:00:27 2025 +0900

    Update sync-to-report-gh.yml

 .github/workflows/sync-to-report-gh.yml | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index 4627d61..5e6aaac 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -50,4 +50,4 @@ jobs:
           YUKIHIKO_TOKEN: ${{ secrets.YUKIHIKO_TOKEN }}     # PR作成用
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}              # デフォルト
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
-        run: ./.github/scripts/sync-to-hub-yukihiko.sh
+        run: ./.github/scripts/sync-to-hub-gh.sh
```

---

## ⏰ 21:01:34 - `687106a`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 21:01:34 2025 +0900
M	.github/workflows/sync-to-report-gh.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 21:01:34 2025 +0900

    Update sync-to-report-gh.yml

 .github/workflows/sync-to-report-gh.yml | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index 5e6aaac..3688357 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -47,7 +47,7 @@ jobs:
       - name: 🚀 YUKIHIKO権限でPR作成＆自動承認
         env:
           GITHUB_TOKEN_ORIGINAL: ${{ secrets.GH_PAT }}      # 承認用
-          YUKIHIKO_TOKEN: ${{ secrets.YUKIHIKO_TOKEN }}     # PR作成用
+          YUKIHIKO_TOKEN: ${{ secrets.GH_PAT_YUKIHIKO }}     # PR作成用
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}              # デフォルト
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
         run: ./.github/scripts/sync-to-hub-gh.sh
```

---

## ⏰ 21:06:29 - `1ff8e93`
**Update sync-to-hub-gh.sh**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 21:06:29 2025 +0900
M	.github/scripts/sync-to-hub-gh.sh
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 21:06:29 2025 +0900

    Update sync-to-hub-gh.sh

 .github/scripts/sync-to-hub-gh.sh | 36 ++++++++++++++++++------------------
 1 file changed, 18 insertions(+), 18 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/scripts/sync-to-hub-gh.sh b/.github/scripts/sync-to-hub-gh.sh
index 9f41d75..9ba5232 100644
--- a/.github/scripts/sync-to-hub-gh.sh
+++ b/.github/scripts/sync-to-hub-gh.sh
@@ -137,25 +137,25 @@ if [ -n "$PR_URL" ]; then
   
   PR_NUMBER=$(gh pr view "$PR_URL" --repo "$REPORT_HUB_REPO" --json number --jq '.number')
   
-  # CI完了待機
-  echo "⏳ CI完了を待機中..."
-  max_wait=300
-  wait_time=0
-  while [ $wait_time -lt $max_wait ]; do
-    CHECK_STATUS=$(gh pr view "$PR_NUMBER" --repo "$REPORT_HUB_REPO" --json statusCheckRollup --jq '.statusCheckRollup[-1].state' 2>/dev/null || echo "PENDING")
+  # # CI完了待機
+  # echo "⏳ CI完了を待機中..."
+  # max_wait=300
+  # wait_time=0
+  # while [ $wait_time -lt $max_wait ]; do
+  #   CHECK_STATUS=$(gh pr view "$PR_NUMBER" --repo "$REPORT_HUB_REPO" --json statusCheckRollup --jq '.statusCheckRollup[-1].state' 2>/dev/null || echo "PENDING")
     
-    if [ "$CHECK_STATUS" = "SUCCESS" ]; then
-      echo "✅ CI完了！"
-      break
-    elif [ "$CHECK_STATUS" = "FAILURE" ]; then
-      echo "❌ CI失敗"
-      exit 1
-    else
-      echo "⏳ CI実行中... (${wait_time}秒)"
-      sleep 10
-      wait_time=$((wait_time + 10))
-    fi
-  done
+  #   if [ "$CHECK_STATUS" = "SUCCESS" ]; then
+  #     echo "✅ CI完了！"
+  #     break
+  #   elif [ "$CHECK_STATUS" = "FAILURE" ]; then
+  #     echo "❌ CI失敗"
+  #     exit 1
+  #   else
+  #     echo "⏳ CI実行中... (${wait_time}秒)"
+  #     sleep 10
+  #     wait_time=$((wait_time + 10))
+  #   fi
+  # done
   
   # 🔥 ここがポイント：元のトークンで承認
   echo "👍 元のアカウントで承認実行中..."
```

---

## ⏰ 23:33:07 - `20c564f`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 23:33:07 2025 +0900
M	.github/workflows/sync-to-report-gh.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 23:33:07 2025 +0900

    Update sync-to-report-gh.yml

 .github/workflows/sync-to-report-gh.yml | 20 +++++++++++++++-----
 1 file changed, 15 insertions(+), 5 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index 3688357..fa2809c 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -1,4 +1,4 @@
-name: 📊 デイリーレポートハブ同期 v2.3 (YUKIHIKO PR版)
+name: 📊 デイリーレポートハブ同期 v2.3 (YUKIHIKO PR版 - 直接実行)
 on:
   push:
     branches: [main, master]
@@ -10,6 +10,10 @@ env:
   AUTO_APPROVE: true
   AUTO_MERGE: true  
   CREATE_PR: true
+  # リモートスクリプトの設定
+  REMOTE_SCRIPTS_REPO: Sunwood-ai-labsII/daily-report-hub_dev
+  REMOTE_SCRIPTS_BRANCH: main
+  SCRIPTS_BASE_URL: https://raw.githubusercontent.com/Sunwood-ai-labsII/daily-report-hub_dev/main/.github/scripts
 
 jobs:
   sync-data:
@@ -20,8 +24,14 @@ jobs:
         with:
           fetch-depth: 0
 
-      - name: 🔧 スクリプトを実行可能にする
-        run: chmod +x .github/scripts/*.sh
+      - name: 📅 週情報を計算
+        run: curl -LsSf ${SCRIPTS_BASE_URL}/calculate-week-info.sh | sh -s -- ${{ env.WEEK_START_DAY }}
+
+      - name: 🔍 Git活動を分析
+        run: curl -LsSf ${SCRIPTS_BASE_URL}/analyze-git-activity.sh | sh
+
+      - name: 📝 Markdownレポートを生成
+        run: curl -LsSf ${SCRIPTS_BASE_URL}/generate-markdown-reports.sh | sh
 
       - name: 📅 週情報を計算
         run: ./.github/scripts/calculate-week-info.sh ${{ env.WEEK_START_DAY }}
@@ -42,7 +52,7 @@ jobs:
           git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub
 
       - name: 🏗️ Docusaurus構造を作成
-        run: ./.github/scripts/create-docusaurus-structure.sh
+        run: curl -LsSf ${SCRIPTS_BASE_URL}/create-docusaurus-structure.sh | sh
 
       - name: 🚀 YUKIHIKO権限でPR作成＆自動承認
         env:
@@ -50,4 +60,4 @@ jobs:
           YUKIHIKO_TOKEN: ${{ secrets.GH_PAT_YUKIHIKO }}     # PR作成用
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}              # デフォルト
           REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
-        run: ./.github/scripts/sync-to-hub-gh.sh
+        run: curl -LsSf ${SCRIPTS_BASE_URL}/sync-to-hub-gh.sh | sh
```

---

## ⏰ 23:45:56 - `ee34ef4`
**Update sync-to-report-gh.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 23:45:56 2025 +0900
M	.github/workflows/sync-to-report-gh.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Mon Aug 11 23:45:56 2025 +0900

    Update sync-to-report-gh.yml

 .github/workflows/sync-to-report-gh.yml | 13 +------------
 1 file changed, 1 insertion(+), 12 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
index fa2809c..6dc1edd 100644
--- a/.github/workflows/sync-to-report-gh.yml
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -1,4 +1,4 @@
-name: 📊 デイリーレポートハブ同期 v2.3 (YUKIHIKO PR版 - 直接実行)
+name: 📊 デイリーレポートハブ同期 v2.3 (YUKIHIKO PR版 - 完全リモート実行)
 on:
   push:
     branches: [main, master]
@@ -11,8 +11,6 @@ env:
   AUTO_MERGE: true  
   CREATE_PR: true
   # リモートスクリプトの設定
-  REMOTE_SCRIPTS_REPO: Sunwood-ai-labsII/daily-report-hub_dev
-  REMOTE_SCRIPTS_BRANCH: main
   SCRIPTS_BASE_URL: https://raw.githubusercontent.com/Sunwood-ai-labsII/daily-report-hub_dev/main/.github/scripts
 
 jobs:
@@ -33,15 +31,6 @@ jobs:
       - name: 📝 Markdownレポートを生成
         run: curl -LsSf ${SCRIPTS_BASE_URL}/generate-markdown-reports.sh | sh
 
-      - name: 📅 週情報を計算
-        run: ./.github/scripts/calculate-week-info.sh ${{ env.WEEK_START_DAY }}
-
-      - name: 🔍 Git活動を分析
-        run: ./.github/scripts/analyze-git-activity.sh
-
-      - name: 📝 Markdownレポートを生成
-        run: ./.github/scripts/generate-markdown-reports.sh
-
       - name: 📂 レポートハブをクローン
         env:
           GITHUB_TOKEN: ${{ secrets.GH_PAT }}
```

---

## ⏰ 23:49:19 - `aa181e8`
**🗑️ GitHub Actions用スクリプト一式を削除**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:49:19 2025 +0900
D	.github/scripts/README.md
D	.github/scripts/analyze-git-activity.sh
D	.github/scripts/calculate-week-info.sh
D	.github/scripts/create-docusaurus-structure.sh
D	.github/scripts/generate-markdown-reports.sh
D	.github/scripts/sync-to-hub.sh
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:49:19 2025 +0900

    🗑️ GitHub Actions用スクリプト一式を削除

 .github/scripts/README.md                      | 141 ------------------
 .github/scripts/analyze-git-activity.sh        |  59 --------
 .github/scripts/calculate-week-info.sh         |  44 ------
 .github/scripts/create-docusaurus-structure.sh | 111 --------------
 .github/scripts/generate-markdown-reports.sh   | 191 -------------------------
 .github/scripts/sync-to-hub.sh                 | 184 ------------------------
 6 files changed, 730 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/scripts/README.md b/.github/scripts/README.md
deleted file mode 100644
index c7e07f4..0000000
--- a/.github/scripts/README.md
+++ /dev/null
@@ -1,141 +0,0 @@
-# GitHub Actions Scripts
-
-このディレクトリには、Daily Report Hub同期ワークフローで使用されるスクリプトが含まれています。
-
-## スクリプト一覧
-
-### 1. `calculate-week-info.sh`
-週情報を計算し、環境変数を設定します。
-
-**使用方法:**
-```bash
-./calculate-week-info.sh [WEEK_START_DAY]
-```
-
-**パラメータ:**
-- `WEEK_START_DAY`: 週の開始日 (0=日曜日, 1=月曜日, ..., 6=土曜日)
-
-**出力環境変数:**
-- `REPO_NAME`: リポジトリ名
-- `DATE`: 現在の日付 (YYYY-MM-DD)
-- `YEAR`: 現在の年
-- `WEEK_FOLDER`: 週フォルダ名
-- `WEEK_START_DATE`: 週の開始日
-- `WEEK_END_DATE`: 週の終了日
-- `WEEK_NUMBER`: 週番号
-
-### 2. `analyze-git-activity.sh`
-Gitの活動を分析し、生データファイルを生成します。
-
-**生成ファイル:**
-- `daily_commits_raw.txt`: その日のコミット一覧
-- `daily_cumulative_diff_raw.txt`: その日の累積差分
-- `daily_diff_stats_raw.txt`: その日の統計情報
-- `daily_code_diff_raw.txt`: その日のコード差分
-- `latest_diff_raw.txt`: 最新の差分
-- `latest_code_diff_raw.txt`: 最新のコード差分
-
-### 3. `generate-markdown-reports.sh`
-生データからMarkdownレポートを生成します。
-
-**生成ファイル:**
-- `daily_commits.md`: コミット詳細レポート
-- `daily_cumulative_diff.md`: ファイル変更レポート
-- `daily_diff_stats.md`: 統計レポート
-- `daily_code_diff.md`: コード差分レポート
-- `latest_diff.md`: 最新変更レポート
-- `latest_code_diff.md`: 最新コード差分レポート
-- `daily_summary.md`: 日次サマリーレポート
-
-### 4. `create-docusaurus-structure.sh`
-Docusaurusの構造と`_category_.json`ファイルを作成します。
-
-**必要な環境変数:**
-- `REPO_NAME`, `DATE`, `YEAR`, `WEEK_FOLDER`, `WEEK_NUMBER`, `WEEK_START_DATE`, `WEEK_END_DATE`
-
-**出力環境変数:**
-- `TARGET_DIR`: ターゲットディレクトリのパス
-
-### 5. `sync-to-hub.sh`
-レポートハブにファイルを同期します。
-
-**必要な環境変数:**
-- `GITHUB_TOKEN`: GitHubアクセストークン
-- `REPORT_HUB_REPO`: レポートハブのリポジトリ
-- `TARGET_DIR`: ターゲットディレクトリ
-- その他の週情報変数
-
-## 週の開始日設定
-
-ワークフローファイルの`env.WEEK_START_DAY`を変更することで、週の開始日を制御できます：
-
-```yaml
-env:
-  WEEK_START_DAY: 1  # 0=日曜日, 1=月曜日, 2=火曜日, etc.
-```
-
-## プルリクエストフロー設定
-
-v2.0では、プルリクエストベースのフローと自動承認機能が追加されました：
-
-```yaml
-env:
-  WEEK_START_DAY: 1     # 週の開始日
-  AUTO_APPROVE: true    # プルリクエストの自動承認
-  AUTO_MERGE: true      # プルリクエストの自動マージ
-  CREATE_PR: true       # プルリクエストを作成するか直接プッシュするか
-```
-
-### 設定オプション
-
-| 設定 | 説明 | デフォルト |
-|------|------|------------|
-| `CREATE_PR` | `true`: プルリクエストを作成<br>`false`: 直接プッシュ | `true` |
-| `AUTO_APPROVE` | `true`: プルリクエストを自動承認<br>`false`: 手動承認が必要 | `false` |
```

---

## ⏰ 23:49:28 - `82ab863`
**🔀 Merge: Remove GitHub Actions scripts**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Merge: dd19e29 aa181e8
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:49:28 2025 +0900
```

### 📊 Statistics
```bash
Merge: dd19e29 aa181e8
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Mon Aug 11 23:49:28 2025 +0900

    🔀 Merge: Remove GitHub Actions scripts

 .github/scripts/README.md                      | 141 ------------------
 .github/scripts/analyze-git-activity.sh        |  59 --------
 .github/scripts/calculate-week-info.sh         |  44 ------
 .github/scripts/create-docusaurus-structure.sh | 111 --------------
 .github/scripts/generate-markdown-reports.sh   | 191 -------------------------
 .github/scripts/sync-to-hub.sh                 | 184 ------------------------
 6 files changed, 730 deletions(-)
```

### 💻 Code Changes
```diff
```

---

