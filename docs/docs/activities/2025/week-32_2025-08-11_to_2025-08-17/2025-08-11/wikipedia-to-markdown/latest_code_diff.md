# 🔄 Latest Code Changes

```diff
diff --git a/README.md b/README.md
index 2b43334..1a1aeff 100644
--- a/README.md
+++ b/README.md
@@ -1,267 +1,221 @@
-
-![](https://github.com/user-attachments/assets/e8fe7c3c-a8d8-4165-86a1-86b9f433f9b3)
-
 <div align="center">
 
-# Daily Report Hub Template
+# 📚 Wikipedia to Markdown Converter
 
-<img src="https://img.shields.io/badge/GitHub%20Actions-CICD-blue?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
-<img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Bash" />
-<a href="https://github.com/Sunwood-ai-labsII/daily-report-hub">
-  <img src="https://img.shields.io/badge/daily--report--hub-PANDA-00D4AA?style=for-the-badge&logo=github&logoColor=white" alt="daily-report-hub PANDA" />
-</a>
+<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
+<img src="https://img.shields.io/badge/Gradio-4.44.0?style=for-the-badge&logo=gradio&logoColor=white" alt="Gradio" />
+<img src="https://img.shields.io/badge/BeautifulSoup-4.12.2?style=for-the-badge&logo=beautifulsoup&logoColor=white" alt="BeautifulSoup" />
+<img src="https://img.shields.io/badge/html2text-2020.1.16?style=for-the-badge&logo=html&logoColor=white" alt="html2text" />
 
 </div>
 
-
 ---
 
 ## 📖 概要
 
-このリポジトリは、**Daily Report Hubのテンプレートリポジトリ**です。このテンプレートからリポジトリを作成すると、自動で日報生成・同期機能が有効になります。
+**Wikipedia to Markdown Converter** は、Wikipediaのページをスクレイピングして、整形されたMarkdown形式に変換するWebアプリケーションです。和モダンなZENテーマを採用し、直感的な操作で簡単にコンテンツを変換できます。
 
 ### 🎯 主な用途
-- 日報自動生成機能を必要とするプロジェクトのテンプレート
-- 集約用リポジトリ（daily-report-hub）への自動同期
-- GitHub Actionsによる完全自動化されたレポート生成
+- Wikipedia記事のMarkdown化
+- コンテンツの再利用と編集
+- ドキュメント作成支援
+- 学習資料の作成
 
-### 🔄 運用方式
-このテンプレートから作成されたリポジトリは、daily-report-hub本体のワークフローから**リモート実行**されるスクリプトを使用して日報を生成・同期します。
+### 🌟 特徴
+- **日本語対応**: 文字化けしない正しい文字コード処理
+- **和モダンデザイン**: ZENテーマで美しいUI
+- **自動整形**: 不要な部分（脚注、編集リンクなど）を自動削除
+- **直感的操作**: ウェブベースで簡単に操作
 
 ---
 
-## 🚩 このテンプレートの役割
+## 🎨 デザインの特徴
+
+### ZENテーマの哲学
+- **空（くう）**: 余白を活かしたミニマルなデザイン
+- **和（わ）**: 琥珀色を基調とした和風配色
+- **簡（かん）**: 直感的でシンプルな操作
+- **禅（ぜん）**: 視覚的な静けさを追求
 
-### 🛠️ テンプレートとしての機能
-- **自動セットアップ**: 日報生成機能の自動有効化
-- **ワークフロー提供**: GitHub Actionsワークフローの自動適用
-- **同期機能**: 集約用リポジトリへの自動同期機能
-- **カスタマイズ**: 必要に応じた設定変更の容易性
+### カラースキーム
+- **プライマリ色**: `#d4a574`（琥珀色）
+- **セカンダリ色**: `#f5f2ed`（薄いベージュ）
+- **背景色**: `#ffffff`（白）
+- **テキスト色**: `#3d405b`（深い青紫）
 
-### 📦 提供される機能
-- Gitのコミット履歴・差分から日報（Markdown形式）を自動生成
-- 週単位・日単位でレポートを整理
-- 別リポジトリ（daily-report-hub）へPRベースで自動同期
-- プルリクエストの自動承認・自動マージ（設定可）
-- Docusaurus用のディレクトリ・ナビゲーション構造も自動生成
+### 日本語フォント
+- Hiragino Sans
+- Noto Sans JP
+- Yu Gothic
+- system-ui, sans-serif
 
 ---
 
-## ⚙️ ワークフロー概要
+## 🚀 使い方（クイックスタート）
+
+### 📝 アプリケーションの起動
 
-### 🔄 自動化フロー図
+```bash
+# 依存関係のインストール
+pip install requests beautifulsoup4 html2text gradio
 
-```mermaid
-graph TB
-    A[開発者のコード<br/>commit/push] --> B[GitHub Actions<br/>ワークフロー]
-    B --> C[レポート生成<br/>Markdown]
-    C --> D[ファイル同期<br/>クローン]
-    D --> E[PR作成・承認<br/>自動化可]
-    E --> F[集約リポジトリ<br/>daily-report-hub]
+# アプリケーションの実行
+python app.py

 
-### 📋 処理ステップ
+起動後、ブラウザで `http://localhost:7861` にアクセスします。
 
-1. **トリガー**: **GitHub Actions**がmainブランチへのpushやPRをトリガー
-2. **データ収集**: リモートスクリプトで
-   - 週情報の計算
-   - Git活動の分析
-   - Markdownレポートの生成
-   - Docusaurus用ディレクトリ構造の作成
-3. **同期処理**: 集約用リポジトリ（daily-report-hub）をクローンし、レポートをコピー
-4. **PR処理**: PR作成・自動承認・自動マージ（設定に応じて自動化）
+### 🔄 操作手順
 
-### ⚙️ 設定可能なオプション
+1. **URLの入力**
+   - 変換したいWikipediaページのURLを入力
+   - デフォルトでPythonのページが設定されています
 
-| 設定 | 説明 | デフォルト値 |
-|------|------|-------------|
-| `WEEK_START_DAY` | 週の開始曜日（0=日曜日, 1=月曜日, ...） | `1`（月曜日） |
-| `AUTO_APPROVE` | PR自動承認 | `true` |
-| `AUTO_MERGE` | PR自動マージ | `true` |
-| `CREATE_PR` | PR作成/直接プッシュ切り替え | `true` |
+2. **変換の実行**
+   - 「✨ 変換する」ボタンをクリック
+   - 自動でスクレイピングとMarkdown変換が実行されます
 
----
+3. **結果の利用**
+   - 生成されたMarkdownをコピーして使用
+   - 一括コピー機能付きで便利です
 
-## 📝 主な機能
+### 📋 使用例
 
-> [!NOTE]
-> このテンプレートから作成されたリポジトリでは、以下の機能が自動で有効になります。
+```python
+# サンプルURL
+https://ja.wikipedia.org/wiki/Python
+https://ja.wikipedia.org/wiki/JavaScript
+https://ja.wikipedia.org/wiki/HTML
+```
 
-### 🔄 自動実行されるスクリプト（リモート）
+---
 
-- **週情報計算**
-  週情報（週番号・開始日・終了日など）を計算し環境変数に出力
+## ⚙️ 機能詳細
 
-- **Git活動分析**
-  Gitのコミット履歴・差分を分析し、生データファイルを生成
+### 🔄 変換処理の流れ
 
-- **Markdownレポート生成**
-  生データから日報・統計・差分などのMarkdownレポートを自動生成
+1. **HTMLの取得と解析**
+   - 指定されたURLからHTMLを取得
+   - BeautifulSoupで解析し、構造を把握
 
-- **Docusaurus構造作成**
-  Docusaurus用のディレクトリ・_category_.jsonを自動生成
+2. **主要コンテンツの抽出**
+   - `mw-parser-output`クラスのコンテンツを抽出
+   - ページタイトルをH1見出しとして取得
 
-- **同期処理**
-  集約リポジトリへPR作成・自動承認・自動マージ
+3. **HTMLの事前整形**
+   - `<dt>`タグを見出しに変換
+   - 不要なタグを整理
 
----
+4. **Markdownへの変換**
+   - html2textでHTMLをMarkdownに変換
+   - レイアウトを維持した整形
 
-## 🚀 使い方（クイックスタート）
+5. **不要部分の削除**
+   - 「## 脚注」以降を削除
+   - `[編集]`リンクを削除
 
-### 📝 テンプレートからリポジトリを作成する方法
-
-> [!TIP]
-> このテンプレートから新しいリポジトリを作成すると、日報生成機能が自動で有効になります。
-
-1. **このリポジトリをテンプレートとして使用**
-   - リポジトリトップページの「Use this template」ボタンをクリック
-   - リポジトリ名を入力して「Create repository from template」をクリック
-
-2. **必要なシークレットを設定**
-   - 作成したリポジトリの「Settings」→「Secrets and variables」→「Actions」に移動
-   - 必要なシークレットを設定（下記参照）
-
-3. **自動で日報生成が開始**
-   - mainブランチにpushすると自動で日報生成＆集約リポジトリへ同期
-
-### 🌐 ワークフローの実際の動作
-
-> [!IMPORTANT]
-> 作成されたリポジトリでは、以下のワークフローが自動で実行されます：
-
-```yaml
-name: 📊 デイリーレポートハブ同期 v2.3 (YUKIHIKO PR版 - 完全リモート実行)
-on:
-  push:
-    branches: [main, master]
-  pull_request:
-    types: [opened, synchronize, closed]
-
-env:
-  WEEK_START_DAY: 1
-  AUTO_APPROVE: true
-  AUTO_MERGE: true
-  CREATE_PR: true
-  # リモートスクリプトの設定
-  SCRIPTS_BASE_URL: https://raw.githubusercontent.com/Sunwood-ai-labsII/daily-report-hub_dev/main/.github/scripts
-
-jobs:
-  sync-data:
-    runs-on: ubuntu-latest
-    steps:
-      - name: 📥 現在のリポジトリをチェックアウト
-        uses: actions/checkout@v4
-        with:
-          fetch-depth: 0
-
-      - name: 📅 週情報を計算
-        run: curl -LsSf ${SCRIPTS_BASE_URL}/calculate-week-info.sh | sh -s -- ${{ env.WEEK_START_DAY }}
-
-      - name: 🔍 Git活動を分析
-        run: curl -LsSf ${SCRIPTS_BASE_URL}/analyze-git-activity.sh | sh
-
-      - name: 📝 Markdownレポートを生成
-        run: curl -LsSf ${SCRIPTS_BASE_URL}/generate-markdown-reports.sh | sh
-
-      - name: 📂 レポートハブをクローン
-        env:
-          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
-          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
-        run: |
-          git config --global user.name "GitHub Actions Bot"
-          git config --global user.email "actions@github.com"
-          git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub
-
-      - name: 🏗️ Docusaurus構造を作成
-        run: curl -LsSf ${SCRIPTS_BASE_URL}/create-docusaurus-structure.sh | sh
-
-      - name: 🚀 YUKIHIKO権限でPR作成＆自動承認
-        env:
-          GITHUB_TOKEN_ORIGINAL: ${{ secrets.GH_PAT }}      # 承認用
-          YUKIHIKO_TOKEN: ${{ secrets.GH_PAT_YUKIHIKO }}     # PR作成用
-          GITHUB_TOKEN: ${{ secrets.GH_PAT }}              # デフォルト
-          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labsII/daily-report-hub' }}
-        run: curl -LsSf ${SCRIPTS_BASE_URL}/sync-to-hub-gh.sh | sh
-```
+6. **最終整形**
+   - タイトルと本文を結合
+   - 余分な空白を整理
 
-### 🔑 環境変数・シークレット設定
+### 🔧 技術的特徴
 
-> [!WARNING]
-> 以下のシークレットを設定しないと、日報同期機能が正常に動作しません。
+- **文字コード自動検出**: User-Agentと文字コード自動検出で日本語を正しく処理
+- **エラーハンドリング**: 無効なURL、ネットワークエラーに対応
+- **レスポンシブデザイン**: 画面サイズに合わせたレイアウト
+- **セキュリティ**: 適切なヘッダー設定でスクレイピングを安定化
 
-#### 必須シークレット
-- `GH_PAT`: GitHub Personal Access Token（リポジトリアクセス用）
-- `GH_PAT_YUKIHIKO`: YUKIHIKO権限用のToken（PR作成・承認用）
+---
 
-#### オプション環境変数（ワークフロー内で設定）
-- `REPORT_HUB_REPO`: レポートハブリポジトリ（デフォルト: `Sunwood-ai-labsII/daily-report-hub`）
-- `WEEK_START_DAY`: 週の開始曜日（0=日曜日, 1=月曜日, ..., 6=土曜日、デフォルト: 1）
-- `AUTO_APPROVE`: PR自動承認（true/false、デフォルト: true）
-- `AUTO_MERGE`: PR自動マージ（true/false、デフォルト: true）
-- `CREATE_PR`: PR作成フラグ（true=PR作成, false=直接プッシュ、デフォルト: true）
+## 📁 プロジェクト構成
 
-#### 環境変数設定例
-各環境変数の詳細な設定は、ワークフローファイル内のコメントを参照してください。
+```
+.
+├── app.py                 # メインアプリケーション
+├── requirements.txt       # 依存関係（作成が必要）
+├── .gitignore            # Git設定
+├── LICENSE               # ライセンス
+└── README.md             # このドキュメント
+```
+
+### 🔧 必要な依存関係
 
-### 📋 シークレット設定手順
+```txt
+requests>=2.31.0
+beautifulsoup4>=4.12.0
+html2text>=2020.1.16
+gradio>=4.44.0
+```
 
-> [!CAUTION]
-> シークレットの漏洩には注意してください。GitHubリポジトリ内に直接記述しないでください。
+依存関係をインストールするには：
 
-1. リポジトリの「Settings」→「Secrets and variables」→「Actions」に移動
-2. 「New repository secret」をクリックして各シークレットを追加
-3. 以下のシークレットを設定：
-   - `GH_PAT`: `repo`スコープを持つPersonal Access Token
-   - `GH_PAT_YUKIHIKO`: `repo`スコープを持つPersonal Access Token（YUKIHIKO権限用）
+```bash
+pip install -r requirements.txt
+```
 
 ---
 
-## 📁 ディレクトリ構成例
+## 🛠️ カスタマイズ
 
-> [!NOTE]
-> このテンプレートから作成されたリポジトリの基本的な構成です。
+### 🎨 テーマの変更
 
-```
-.
-├── .github/
-│   └── workflows/
-│       └── sync-to-report-gh.yml
-├── .gitignore
-├── LICENSE
-├── README.md
-└── [プロジェクト固有のファイル]
+ZENテーマのカラーやフォントを変更するには、`app.py`の`create_zen_theme()`関数を編集します。
+
+```python
+def create_zen_theme():
+    return gr.Theme(
+        primary_hue="amber",      # プライマリ色
+        secondary_hue="stone",    # セカンダリ色
+        neutral_hue="slate",      # ニュートラル色
+        # ... その他の設定
+    )

 
+### 🔧 変換ロジックの変更
+
+スクレイピングや変換のロジックを変更するには、`scrape_wikipedia_to_markdown_final()`関数を編集します。
+
 ---
 
-## 🛠️ 設定・カスタマイズ
+## 🌐 アプリケーション画面
 
-> [!TIP]
-> 必要に応じてワークフローファイルをカスタマイズできます。
+### 📱 インターフェース例
 
-- `.github/workflows/sync-to-report-gh.yml`
-  - `WEEK_START_DAY`：週の開始曜日（0=日, 1=月, ...）
-  - `AUTO_APPROVE`：PR自動承認
-  - `AUTO_MERGE`：PR自動マージ
-  - `CREATE_PR`：PR作成/直接push切替
+- **ヘッダー**: グラデーション背景で和モダンな印象
+- **入力エリア**: URL入力ボックスと変換ボタン
+- **出力エリア**: 生成されたMarkdownを表示
+- **使用例**: クイック選択用のサンプルURL
 
-- リモートスクリプトの詳細は開発リポジトリを参照
+### 🎯 ユーザビリティ
+
+- **一括コピー**: Markdownをワンクリックでコピー
+- **サンプル選択**: 代表的なWikipediaページをクイック選択
+- **リアルタイムフィードバック**: 変換中の状態を表示
+- **エラーメッセージ**: 分かりやすい日本語のエラー表示
 
 ---
 
 ## 🔗 参考リンク
 
-- [集約用日報ハブリポジトリ](https://github.com/Sunwood-ai-labsII/daily-report-hub)
-- [開発リポジトリ（スクリプトソース）](https://github.com/Sunwood-ai-labsII/daily-report-hub_dev)
-- [GitHub Actions公式ドキュメント](https://docs.github.com/ja/actions)
-- [Docusaurus公式サイト](https://docusaurus.io/ja/)
+- [Gradio公式サイト](https://www.gradio.app/)
+- [BeautifulSoup公式ドキュメント](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
+- [html2text公式サイト](https://github.com/Alir3z4/html2text)
+- [Wikipedia API](https://ja.wikipedia.org/api/rest_v1/)
 
 ---
 
 ## 📝 ライセンス
 
-このテンプレートは [LICENSE](LICENSE) に基づいて提供されています。
+このプロジェクトは [LICENSE](LICENSE) に基づいて提供されています。
+
+---
+
+## 🙏 謝辞
+
+- [Gradio](https://www.gradio.app/) - Webアプリケーションフレームワーク
+- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - HTML解析ライブラリ
+- [html2text](https://github.com/Alir3z4/html2text) - HTMLからMarkdownへの変換ツール
 
 ---
 
-© 2025 Sunwood-ai-labsII
+© 2025 Wikipedia to Markdown Converter
diff --git a/app.py b/app.py
new file mode 100644
index 0000000..8cd6fcd
--- /dev/null
+++ b/app.py
@@ -0,0 +1,207 @@
+import requests
+from bs4 import BeautifulSoup
+import html2text
+import re
+import gradio as gr
+
+# ZENテーマの作成
+def create_zen_theme():
+    return gr.Theme(
+        primary_hue="amber",
+        secondary_hue="stone",
+        neutral_hue="slate",
+        text_size="md",
+        spacing_size="lg",
+        radius_size="sm",
+        font=[
+            "Hiragino Sans",
+            "Noto Sans JP",
+            "Yu Gothic",
+            "system-ui",
+            "sans-serif"
+        ],
+        font_mono=[
+            "SF Mono",
+            "Monaco",
+            "monospace"
+        ]
+    ).set(
+        body_background_fill="#ffffff",
+        body_text_color="#3d405b",
+        button_primary_background_fill="#d4a574",
+        button_primary_background_fill_hover="#c19660",
+        button_primary_text_color="#ffffff",
+        button_secondary_background_fill="#f5f2ed",
+        button_secondary_text_color="#3d405b",
+        input_background_fill="#ffffff",
+        input_border_color="#d4c4a8",
+        input_border_color_focus="#d4a574",
+        block_background_fill="#ffffff",
+        block_border_color="#f5f2ed",
+        panel_background_fill="#ffffff",
+        panel_border_color="#f5f2ed",
+        slider_color="#d4a574",
+    )
+
+def scrape_wikipedia_to_markdown_final(url: str) -> str:
+    """
+    Wikipediaページをスクレイピングし、整形・不要部分削除を行い、
+    タイトルを付けてMarkdownに変換します。
+
+    処理フロー：
+    1. ページのタイトルをH1見出しとして取得します。
+    2. 「登場人物」などの<dt>タグを見出しに変換します。
+    3. 生成されたMarkdown文字列から「## 脚注」以降を完全に削除します。
+    4. [編集]リンクを削除します。
+    5. 最終的にタイトルと本文を結合して返します。
+
+    Args:
+        url (str): スクレイピング対象のWikipediaページのURL。
+
+    Returns:
+        str: 整形・変換された最終的なMarkdownコンテンツ。失敗した場合は空の文字列。
+    """
+    try:
+        # 1. HTMLの取得と解析
+        headers = {
+            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
+        }
+        response = requests.get(url, headers=headers)
+        response.raise_for_status()  # HTTPエラーがあれば例外を発生させる
+        response.encoding = response.apparent_encoding  # 文字コードを自動検出
+        soup = BeautifulSoup(response.text, 'html.parser')
+
+        # --- ページのタイトルを取得 ---
+        title_tag = soup.find('h1', id='firstHeading')
+        page_title = title_tag.get_text(strip=True) if title_tag else "Wikipedia ページ"
+
+        # 2. 主要コンテンツエリアの特定
+        content_div = soup.find('div', class_='mw-parser-output')
+        if not content_div:
+            return "エラー: コンテンツエリアが見つかりませんでした。"
+
+        # 3. HTMLの事前整形（登場人物などの見出し化）
+        for dt_tag in content_div.find_all('dt'):
+            h4_tag = soup.new_tag('h4')
+            h4_tag.extend(dt_tag.contents)
+            dt_tag.replace_with(h4_tag)
+
+        # 4. HTMLからMarkdownへの一次変換
+        h = html2text.HTML2Text()
+        h.body_width = 0  # テキストの折り返しを無効にする
+        full_markdown_text = h.handle(str(content_div))
+
+        # 5. 生成されたMarkdownから「## 脚注」以降を削除
+        footnote_marker = "\n## 脚注"
+        footnote_index = full_markdown_text.find(footnote_marker)
+        body_text = full_markdown_text[:footnote_index] if footnote_index != -1 else full_markdown_text
+
+        # 6. [編集]リンクを正規表現で一括削除
+        cleaned_body = re.sub(r'\[\[編集\]\(.+?\)]\n', '', body_text)
+
+        # 7. タイトルと整形後の本文を結合
+        final_markdown = f"# {page_title}\n\n{cleaned_body.strip()}"
+
+        return final_markdown
+
+    except requests.exceptions.RequestException as e:
+        return f"HTTPリクエストエラー: {e}"
+    except Exception as e:
+        return f"予期せぬエラーが発生しました: {e}"
+
+def process_wikipedia_url(url):
+    """Wikipedia URLを処理してMarkdownを生成するGradio用関数"""
+    if not url:
+        return "URLを入力してください。"
+    
+    # URLが有効かチェック
+    if not url.startswith('http'):
+        return "有効なURLを入力してください（http://またはhttps://から始まるURL）。"
+    
+    # Wikipedia URLかチェック
+    if 'wikipedia.org' not in url:
+        return "WikipediaのURLを入力してください。"
+    
+    # スクレイピングを実行
+    markdown_content = scrape_wikipedia_to_markdown_final(url)
+    
+    return markdown_content
+
+# Gradioインターフェースの作成
+def create_interface():
+    """Gradioインターフェースを作成する関数"""
+    theme = create_zen_theme()
+    
+    with gr.Blocks(theme=theme, title="Wikipedia to Markdown Converter") as demo:
+        # ヘッダー
+        gr.HTML("""
+        <div style='text-align: center; margin-bottom: 2rem; padding: 2rem; background: linear-gradient(135deg, #d4a574 0%, #ffffff 50%, #f5f2ed 100%); color: #3d405b; border-radius: 12px;'>
+            <h1 style='font-size: 3rem; margin-bottom: 0.5rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);'>📚 Wikipedia to Markdown Converter</h1>
+            <p style='font-size: 1.2rem; opacity: 0.8;'>WikipediaのURLを入力して、Markdown形式に変換します</p>
+        </div>
+        """)
+        
+        with gr.Row():
+            with gr.Column(scale=1):
+                url_input = gr.Textbox(
+                    label="🔗 Wikipedia URL",
+                    placeholder="https://ja.wikipedia.org/wiki/...",
+                    value="https://ja.wikipedia.org/wiki/Python"
+                )
+                convert_btn = gr.Button("✨ 変換する", variant="primary")
+            
+            with gr.Column(scale=1):
+                output_text = gr.Textbox(
+                    label="📝 変換されたMarkdown",
+                    lines=20,
+                    max_lines=50,
+                    show_copy_button=True
+                )
+        
+        # ボタンクリック時の処理
+        convert_btn.click(
+            fn=process_wikipedia_url,
+            inputs=url_input,
+            outputs=output_text
+        )
+        
+        # 使用例
+        gr.Examples(
+            examples=[
+                ["https://ja.wikipedia.org/wiki/Python"],
+                ["https://ja.wikipedia.org/wiki/JavaScript"],
+                ["https://ja.wikipedia.org/wiki/HTML"]
+            ],
+            inputs=url_input,
+            outputs=output_text,
+            fn=process_wikipedia_url,
+            cache_examples=False
+        )
+        
+        gr.Markdown("---")
+        gr.Markdown("### 🎯 使用方法")
+        gr.Markdown("1. 変換したいWikipediaページのURLを入力します")
+        gr.Markdown("2. 「✨ 変換する」ボタンをクリックします")
+        gr.Markdown("3. 生成されたMarkdownをコピーして使用します")
+        
+        # ZENテーマの説明
+        gr.HTML("""
+        <div style='text-align: center; margin-top: 2rem; padding: 1.5rem; background: #ffffff; border-radius: 12px;'>
+            <h3 style='color: #3d405b; margin-top: 0;'>🧘‍♀️ ZENテーマ</h3>
+            <p style='color: #8b7355;'>和モダンなデザインで、使いやすさと美しさを追求しました</p>
+        </div>
+        """)
+    
+    return demo
+
+if __name__ == "__main__":
+    # インターフェースを作成
+    demo = create_interface()
+    
+    # アプリケーションを実行
+    demo.launch(
+        server_name="0.0.0.0",
+        server_port=7861,
+        share=False,
+        debug=True
+    )
diff --git a/requirements.txt b/requirements.txt
new file mode 100644
index 0000000..30c42d3
--- /dev/null
+++ b/requirements.txt
@@ -0,0 +1,4 @@
+requests>=2.31.0
+beautifulsoup4>=4.12.0
+html2text>=2020.1.16
+gradio>=4.44.0
```
