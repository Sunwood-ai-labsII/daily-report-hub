# 🔄 Latest Code Changes

```diff
diff --git a/README.md b/README.md
index 64851e5..ef7c17b 100644
--- a/README.md
+++ b/README.md
@@ -2,234 +2,173 @@
 license: mit
 title: wikipedia to markdown
 sdk: gradio
-emoji: 📈
-colorFrom: green
-colorTo: indigo
+emoji: 📚
+colorFrom: amber
+colorTo: stone
 thumbnail: >-
   https://cdn-uploads.huggingface.co/production/uploads/64e0ef4a4c78e1eba5178d7a/vJQZ24fctExV3dax_BGU-.jpeg
 sdk_version: 5.42.0
 ---
+
 <div align="center">
 
-![](https://github.com/user-attachments/assets/201c0b39-6bf7-4599-a62a-dd3e6f61e5f8)
+![Wikipedia to Markdown Converter](https://github.com/user-attachments/assets/201c0b39-6bf7-4599-a62a-dd3e6f61e5f8)
 
 # 📚 Wikipedia to Markdown Converter
 
-![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
-![Gradio](https://img.shields.io/badge/Gradio-FF6B6B?style=for-the-badge&logo=gradio&logoColor=white)
-![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4CAF50?style=for-the-badge&logo=python&logoColor=white)
-![html2text](https://img.shields.io/badge/html2text-2196F3?style=for-the-badge&logo=html5&logoColor=white)
+*WikipediaページをMarkdown形式に変換するWebアプリケーション*
 
+[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
+[![Gradio](https://img.shields.io/badge/Gradio-5.42+-FF6B6B?style=for-the-badge&logo=gradio&logoColor=white)](https://gradio.app)
+[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
+[![Demo](https://img.shields.io/badge/🚀%20デモサイト-Live-orange?style=for-the-badge)](https://huggingface.co/spaces/MakiAi/wikipedia-to-markdown)
 
 </div>
 
 ---
 
-## 📖 概要
+## 🌟 概要
 
-**Wikipedia to Markdown Converter** は、Wikipediaのページをスクレイピングして、整形されたMarkdown形式に変換するWebアプリケーションです。和モダンなZENテーマを採用し、直感的な操作で簡単にコンテンツを変換できます。
+**Wikipedia to Markdown Converter** は、Wikipediaの記事を整形されたMarkdownドキュメントに変換するWebアプリケーションです。単体処理と一括処理に対応し、複数のダウンロード形式を提供します。
 
-### 🎯 主な用途
-- Wikipedia記事のMarkdown化
-- コンテンツの再利用と編集
-- ドキュメント作成支援
-- 学習資料の作成
+### ✨ **主要機能**
 
-### 🌟 特徴
-- **日本語対応**: 文字化けしない正しい文字コード処理
-- **和モダンデザイン**: ZENテーマで美しいUI
-- **自動整形**: 不要な部分（脚注、編集リンクなど）を自動削除
-- **直感的操作**: ウェブベースで簡単に操作
+- 🔄 **単体・一括処理** - 1つまたは複数のWikipediaページを同時変換
+- 📊 **詳細分析** - 文字数、成功率、ファイル情報を表示
+- 🗜️ **複数形式** - 個別ファイル、結合文書、ZIPダウンロード
+- 🌐 **多言語対応** - 全てのWikipedia言語版に対応
+- � **要使いやすいUI** - 直感的で美しいインターフェース
 
 ---
 
-## 🎨 デザインの特徴
+## 🚀 使い方
 
-### ZENテーマの哲学
-- **空（くう）**: 余白を活かしたミニマルなデザイン
-- **和（わ）**: 琥珀色を基調とした和風配色
-- **簡（かん）**: 直感的でシンプルな操作
-- **禅（ぜん）**: 視覚的な静けさを追求
+### �  **オンラインで試す（推奨）**
+**[🚀 デモサイトはこちら](https://huggingface.co/spaces/MakiAi/wikipedia-to-markdown)**
 
-### カラースキーム
-- **プライマリ色**: `#d4a574`（琥珀色）
-- **セカンダリ色**: `#f5f2ed`（薄いベージュ）
-- **背景色**: `#ffffff`（白）
-- **テキスト色**: `#3d405b`（深い青紫）
+### 💻 **ローカルで実行**
 
-### 日本語フォント
-- Hiragino Sans
-- Noto Sans JP
-- Yu Gothic
-- system-ui, sans-serif
+\```bash
+# リポジトリをクローン
+git clone https://github.com/your-username/wikipedia-to-markdown.git
+cd wikipedia-to-markdown
 
----
+# 依存関係をインストール
+pip install -r requirements.txt
 
-## 🚀 使い方（クイックスタート）
+# アプリケーションを起動
+python app.py
+\```
 
-### 📝 アプリケーションの起動
+### 🐳 **Dockerで実行**
 
 \```bash
-# 依存関係のインストール
-pip install requests beautifulsoup4 html2text gradio
+# Docker Composeを使用
+docker-compose up -d
 
-# アプリケーションの実行
-python app.py
+# ブラウザで http://localhost:7860 にアクセス
 \```
 
-起動後、ブラウザで `http://localhost:7861` にアクセスします。
-
-### 🔄 操作手順
-
-1. **URLの入力**
-   - 変換したいWikipediaページのURLを入力
-   - デフォルトでPythonのページが設定されています
+---
 
-2. **変換の実行**
-   - 「✨ 変換する」ボタンをクリック
-   - 自動でスクレイピングとMarkdown変換が実行されます
+## 📋 操作方法
 
-3. **結果の利用**
-   - 生成されたMarkdownをコピーして使用
-   - 一括コピー機能付きで便利です
+### 🔗 **単体処理**
+1. WikipediaのURLを入力
+2. 「✨ 変換する」ボタンをクリック
+3. 生成されたMarkdownをコピーまたはダウンロード
 
-### 📋 使用例
+### 📚 **一括処理**
+1. 複数のURLを1行に1つずつ入力
+2. 「🚀 一括変換する」ボタンをクリック
+3. 処理結果を確認し、必要な形式でダウンロード
 
-\```python
-# サンプルURL
-https://ja.wikipedia.org/wiki/Python
-https://ja.wikipedia.org/wiki/JavaScript
-https://ja.wikipedia.org/wiki/HTML
+### 📊 **処理結果の表示例**
+\```
+============================================================
+📊 処理結果サマリー
+============================================================
+🔗 処理対象URL数: 3
+✅ 成功: 2
+❌ 失敗: 1
+
+✅ 処理成功: https://ja.wikipedia.org/wiki/Python
+   📄 ページタイトル: Python
+   📊 文字数: 15,432 文字
+   💾 ファイル名: Python.md
 \```
 
 ---
 
-## ⚙️ 機能詳細
-
-### 🔄 変換処理の流れ
-
-1. **HTMLの取得と解析**
-   - 指定されたURLからHTMLを取得
-   - BeautifulSoupで解析し、構造を把握
-
-2. **主要コンテンツの抽出**
-   - `mw-parser-output`クラスのコンテンツを抽出
-   - ページタイトルをH1見出しとして取得
-
-3. **HTMLの事前整形**
-   - `<dt>`タグを見出しに変換
-   - 不要なタグを整理
+## 📦 ダウンロード形式
 
-4. **Markdownへの変換**
-   - html2textでHTMLをMarkdownに変換
-   - レイアウトを維持した整形
+| 形式 | 説明 | 用途 |
+|------|------|------|
+| **📄 個別ファイル** | 各ページを別々のMarkdownファイル | 個別編集・管理 |
+| **📚 結合文書** | 全ページを1つのファイルに結合 | 一括閲覧・印刷 |
+| **🗜️ ZIPアーカイブ** | 全ファイルを圧縮してまとめて | 大量ファイルの管理 |
 
-5. **不要部分の削除**
-   - 「## 脚注」以降を削除
-   - `[編集]`リンクを削除
+---
 
-6. **最終整形**
-   - タイトルと本文を結合
-   - 余分な空白を整理
+## 🔧 技術仕様
 
-### 🔧 技術的特徴
+### **使用技術**
+- **Python 3.8+** - メイン言語
+- **Gradio** - Webインターフェース
+- **BeautifulSoup4** - HTML解析
+- **html2text** - Markdown変換
+- **Requests** - HTTP通信
 
-- **文字コード自動検出**: User-Agentと文字コード自動検出で日本語を正しく処理
-- **エラーハンドリング**: 無効なURL、ネットワークエラーに対応
-- **レスポンシブデザイン**: 画面サイズに合わせたレイアウト
-- **セキュリティ**: 適切なヘッダー設定でスクレイピングを安定化
+### **処理フロー**
+1. **URL検証** - 入力URLの妥当性チェック
+2. **HTML取得** - Wikipediaページの取得
+3. **コンテンツ抽出** - 主要コンテンツの抽出
+4. **クリーンアップ** - 不要部分（脚注、編集リンク等）の削除
+5. **Markdown変換** - 整形されたMarkdownに変換
+6. **ファイル生成** - 各種形式でのファイル出力
 
 ---
 
 ## 📁 プロジェクト構成
 
 \```
-.
-├── app.py                 # メインアプリケーション
-├── requirements.txt       # 依存関係（作成が必要）
-├── .gitignore            # Git設定
-├── LICENSE               # ライセンス
-└── README.md             # このドキュメント
-\```
-
-### 🔧 必要な依存関係
-
-\```txt
-requests>=2.31.0
-beautifulsoup4>=4.12.0
-html2text>=2020.1.16
-gradio>=4.44.0
-\```
-
-依存関係をインストールするには：
-
-\```bash
-pip install -r requirements.txt
+wikipedia-to-markdown/
+├── app.py                    # メインアプリケーション
+├── theme.py                  # UIテーマ設定
+├── requirements.txt          # Python依存関係
+├── docker-compose.yml        # Docker設定
+├── .github/workflows/        # CI/CD設定
+└── README.md                 # このファイル
 \```
 
 ---
 
 ## 🛠️ カスタマイズ
 
-### 🎨 テーマの変更
-
-ZENテーマのカラーやフォントを変更するには、`app.py`の`create_zen_theme()`関数を編集します。
-
-\```python
-def create_zen_theme():
-    return gr.Theme(
-        primary_hue="amber",      # プライマリ色
-        secondary_hue="stone",    # セカンダリ色
-        neutral_hue="slate",      # ニュートラル色
-        # ... その他の設定
-    )
-\```
-
-### 🔧 変換ロジックの変更
+### **テーマ変更**
+`theme.py`を編集してUIの色やスタイルを変更できます。
 
-スクレイピングや変換のロジックを変更するには、`scrape_wikipedia_to_markdown_final()`関数を編集します。
+### **処理ロジック拡張**
+`app.py`の`scrape_wikipedia_to_markdown_final()`関数を編集して、変換処理をカスタマイズできます。
 
 ---
 
-## 🌐 アプリケーション画面
+## 📄 ライセンス
 
-### 📱 インターフェース例
-
-- **ヘッダー**: グラデーション背景で和モダンな印象
-- **入力エリア**: URL入力ボックスと変換ボタン
-- **出力エリア**: 生成されたMarkdownを表示
-- **使用例**: クイック選択用のサンプルURL
-
-### 🎯 ユーザビリティ
-
-- **一括コピー**: Markdownをワンクリックでコピー
-- **サンプル選択**: 代表的なWikipediaページをクイック選択
-- **リアルタイムフィードバック**: 変換中の状態を表示
-- **エラーメッセージ**: 分かりやすい日本語のエラー表示
+このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。
 
 ---
 
-## 🔗 参考リンク
+## 🤝 コントリビューション
 
-- [Gradio公式サイト](https://www.gradio.app/)
-- [BeautifulSoup公式ドキュメント](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
-- [html2text公式サイト](https://github.com/Alir3z4/html2text)
-- [Wikipedia API](https://ja.wikipedia.org/api/rest_v1/)
+バグ報告や機能提案は[GitHub Issues](https://github.com/your-username/wikipedia-to-markdown/issues)でお願いします。
 
 ---
 
-## 📝 ライセンス
-
-このプロジェクトは [LICENSE](LICENSE) に基づいて提供されています。
-
----
-
-## 🙏 謝辞
+<div align="center">
 
-- [Gradio](https://www.gradio.app/) - Webアプリケーションフレームワーク
-- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - HTML解析ライブラリ
-- [html2text](https://github.com/Alir3z4/html2text) - HTMLからMarkdownへの変換ツール
+**🌟 このプロジェクトが役に立ったらスターをお願いします！**
 
----
+*© 2025 Wikipedia to Markdown Converter*
 
-© 2025 Wikipedia to Markdown Converter
\ No newline at end of file
+</div>
\ No newline at end of file
diff --git a/app.py b/app.py
index 47f32ac..cd88a94 100644
--- a/app.py
+++ b/app.py
@@ -6,6 +6,7 @@ import gradio as gr
 from theme import create_zen_theme
 import tempfile
 import os
+import zipfile
 from urllib.parse import urlparse, unquote
 
 def scrape_wikipedia_to_markdown_final(url: str) -> str:
@@ -103,6 +104,24 @@ def create_download_file(content, filename):
         print(f"ファイル作成エラー: {e}")
         return None
 
+def create_zip_file(file_paths, zip_filename="wikipedia_export.zip"):
+    """複数のファイルをZIP形式でまとめる関数"""
+    try:
+        temp_dir = tempfile.gettempdir()
+        zip_path = os.path.join(temp_dir, zip_filename)
+        
+        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
+            for file_path in file_paths:
+                if os.path.exists(file_path):
+                    # ファイル名のみを取得してZIPに追加
+                    filename = os.path.basename(file_path)
+                    zipf.write(file_path, filename)
+        
+        return zip_path
+    except Exception as e:
+        print(f"ZIP作成エラー: {e}")
+        return None
+
 def process_wikipedia_url(url):
     """Wikipedia URLを処理してMarkdownを生成するGradio用関数"""
     if not url:
@@ -130,18 +149,19 @@ def process_wikipedia_url(url):
 def process_multiple_urls(urls_text, progress=gr.Progress()):
     """複数のWikipedia URLを一括処理してMarkdownを生成する関数"""
     if not urls_text.strip():
-        return "URLリストを入力してください。", None, []
+        return "URLリストを入力してください。", None, [], None
     
     # URLリストを行ごとに分割
     urls = [url.strip() for url in urls_text.strip().split('\n') if url.strip()]
     
     if not urls:
-        return "有効なURLが見つかりませんでした。", None, []
+        return "有効なURLが見つかりませんでした。", None, [], None
     
     results = []
     all_content = []
     individual_files = []
     total_urls = len(urls)
+    success_count = 0
     
     for i, url in enumerate(urls):
         progress((i + 1) / total_urls, f"処理中: {i + 1}/{total_urls}")
@@ -159,21 +179,45 @@ def process_multiple_urls(urls_text, progress=gr.Progress()):
         try:
             markdown_content = scrape_wikipedia_to_markdown_final(url)
             if markdown_content.startswith("エラー:") or markdown_content.startswith("HTTP"):
-                results.append(f"❌ 処理失敗: {url}\n{markdown_content}")
+                results.append(f"❌ 処理失敗: {url}\n   エラー: {markdown_content}")
             else:
-                results.append(f"✅ 処理成功: {url}\n\n{markdown_content}")
+                # ページタイトルを抽出
+                title_match = re.match(r'^# (.+)', markdown_content)
+                page_title = title_match.group(1) if title_match else "不明なページ"
+                
+                # 文字数とファイル情報を表示
+                char_count = len(markdown_content)
+                filename = get_filename_from_url(url)
+                
+                results.append(f"✅ 処理成功: {url}")
+                results.append(f"   📄 ページタイトル: {page_title}")
+                results.append(f"   📊 文字数: {char_count:,} 文字")
+                results.append(f"   💾 ファイル名: {filename}")
+                
                 all_content.append(markdown_content)
+                success_count += 1
                 
                 # 個別ファイルを作成
-                filename = get_filename_from_url(url)
                 file_path = create_download_file(markdown_content, filename)
                 if file_path:
                     individual_files.append(file_path)
         except Exception as e:
-            results.append(f"❌ 処理エラー: {url}\nエラー内容: {str(e)}")
+            results.append(f"❌ 処理エラー: {url}")
+            results.append(f"   エラー内容: {str(e)}")
+    
+    # サマリー情報を追加
+    summary = [
+        "=" * 60,
+        "📊 処理結果サマリー",
+        "=" * 60,
+        f"🔗 処理対象URL数: {total_urls}",
+        f"✅ 成功: {success_count}",
+        f"❌ 失敗: {total_urls - success_count}",
+        ""
+    ]
     
     # 結果を結合
-    final_result = "\n\n" + "="*80 + "\n\n".join(results)
+    final_result = "\n".join(summary + results)
     
     # 一括ダウンロード用ファイルを作成
     batch_file_path = None
@@ -181,7 +225,12 @@ def process_multiple_urls(urls_text, progress=gr.Progress()):
         combined_content = "\n\n" + "="*80 + "\n\n".join(all_content)
         batch_file_path = create_download_file(combined_content, "wikipedia_batch_export.md")
     
-    return final_result, batch_file_path, individual_files
+    # ZIPファイルを作成
+    zip_file_path = None
+    if individual_files:
+        zip_file_path = create_zip_file(individual_files, "wikipedia_export.zip")
+    
+    return final_result, batch_file_path, individual_files, zip_file_path
 
 # Gradioインターフェースの作成
 def create_interface():
@@ -276,6 +325,10 @@ def create_interface():
                             label="📥 全体をまとめてダウンロード",
                             visible=False
                         )
+                        zip_download_file = gr.File(
+                            label="🗜️ ZIPファイルでダウンロード",
+                            visible=False
+                        )
                         
                         # 個別ダウンロードエリア
                         individual_downloads = gr.Column(visible=False)
@@ -289,7 +342,7 @@ def create_interface():
                 
                 # 一括処理ボタンクリック時の処理
                 def update_batch_output(urls_text):
-                    content, batch_file_path, individual_files = process_multiple_urls(urls_text)
+                    content, batch_file_path, individual_files, zip_file_path = process_multiple_urls(urls_text)
                     
                     # 戻り値のリストを準備
                     outputs = [content]
@@ -300,6 +353,12 @@ def create_interface():
                     else:
                         outputs.append(gr.update(visible=False))
                     
+                    # ZIPダウンロードファイル
+                    if zip_file_path:
+                        outputs.append(gr.update(value=zip_file_path, visible=True))
+                    else:
+                        outputs.append(gr.update(visible=False))
+                    
                     # 個別ダウンロードエリアの表示/非表示
                     if individual_files:
                         outputs.append(gr.update(visible=True))
@@ -321,7 +380,8 @@ def create_interface():
                     inputs=urls_input,
                     outputs=[
                         batch_output_text, 
-                        batch_download_file, 
+                        batch_download_file,
+                        zip_download_file,
                         individual_downloads,
                         individual_file_1,
                         individual_file_2,
@@ -344,8 +404,9 @@ def create_interface():
         gr.Markdown("- 生成されたMarkdownは右側のテキストエリアからコピーできます")
         gr.Markdown("- **📥 ダウンロード機能**: 変換が成功すると、マークダウンファイルとして直接ダウンロードできます")
         gr.Markdown("  - 単体処理: ページ名に基づいたファイル名で個別ダウンロード")
-        gr.Markdown("  - 一括処理: 各URLごとの個別ダウンロード + 全体をまとめた一括ダウンロード")
+        gr.Markdown("  - 一括処理: 各URLごとの個別ダウンロード + 全体をまとめた一括ダウンロード + **🗜️ ZIPファイル**")
         gr.Markdown("  - 個別ダウンロード: 成功した各ページを個別のファイルとしてダウンロード可能（最大5つまで表示）")
+        gr.Markdown("  - **ZIPダウンロード**: 複数のMarkdownファイルを1つのZIPファイルにまとめてダウンロード")
         
         # ZENテーマの説明
         gr.HTML("""
```
