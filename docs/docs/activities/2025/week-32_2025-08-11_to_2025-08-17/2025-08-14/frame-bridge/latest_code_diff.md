# 🔄 Latest Code Changes

```diff
diff --git a/.gitignore b/.gitignore
index 16c3c78..5580869 100644
--- a/.gitignore
+++ b/.gitignore
@@ -206,3 +206,8 @@ marimo/_static/
 marimo/_lsp/
 __marimo__/
 .SourceSageAssets/
+assets/*.mp4
+uv.lock
+assets/example/REI/input/*.mp4
+assets/example/REI/output/*.mp4
+assets/example/REI/output/batch_report.txt
diff --git a/Dockerfile b/Dockerfile
index 9021fbf..bd72ebe 100644
--- a/Dockerfile
+++ b/Dockerfile
@@ -4,8 +4,18 @@ FROM python:3.11-slim
 # 作業ディレクトリを設定
 WORKDIR /app
 
-# システムパッケージの更新とクリーンアップ
+# システムパッケージの更新とOpenCV用ライブラリをインストール
 RUN apt-get update && apt-get install -y \
+    libglib2.0-0 \
+    libsm6 \
+    libxext6 \
+    libxrender-dev \
+    libgomp1 \
+    libglib2.0-0 \
+    libgtk-3-0 \
+    libavcodec-dev \
+    libavformat-dev \
+    libswscale-dev \
     && rm -rf /var/lib/apt/lists/*
 
 # 依存関係ファイルをコピー
diff --git a/README.md b/README.md
index 9edb370..5793df9 100644
--- a/README.md
+++ b/README.md
@@ -2,9 +2,9 @@
 license: mit
 title: frame bridge
 sdk: gradio
-emoji: 🏆
-colorFrom: red
-colorTo: indigo
+emoji: 🎬
+colorFrom: purple
+colorTo: blue
 thumbnail: >-
   https://cdn-uploads.huggingface.co/production/uploads/64e0ef4a4c78e1eba5178d7a/BZfofcX1vEF7kwWQ0i-uB.png
 sdk_version: 5.42.0
@@ -14,14 +14,15 @@ sdk_version: 5.42.0
 
 ![frame-bridge](https://github.com/user-attachments/assets/05977e5b-3e63-4ed2-a5f6-74ada8943994)
 
-# 📚 Wikipedia to Markdown Converter
+# 🎬 Frame Bridge
 
-*WikipediaページをMarkdown形式に変換するWebアプリケーション*
+*2つの動画を最適なフレームで自動結合するAIアプリケーション*
 
 [![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
+[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)
 [![Gradio](https://img.shields.io/badge/Gradio-5.42+-FF6B6B?style=for-the-badge&logo=gradio&logoColor=white)](https://gradio.app)
 [![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
-[![Demo](https://img.shields.io/badge/🚀%20デモサイト-Live-orange?style=for-the-badge)](https://huggingface.co/spaces/MakiAi/wikipedia-to-markdown)
+[![Demo](https://img.shields.io/badge/🚀%20デモサイト-Live-orange?style=for-the-badge)](https://huggingface.co/spaces/MakiAi/frame-bridge)
 
 </div>
 
@@ -29,29 +30,29 @@ sdk_version: 5.42.0
 
 ## 🌟 概要
 
-**Wikipedia to Markdown Converter** は、Wikipediaの記事を整形されたMarkdownドキュメントに変換するWebアプリケーションです。単体処理と一括処理に対応し、複数のダウンロード形式を提供します。
+**Frame Bridge** は、2つの動画を視覚的に最適なフレームで自動結合するAIアプリケーションです。SSIM（構造的類似性指標）を使用して、動画1の終了部分と動画2の開始部分から最も類似したフレームを検出し、スムーズな動画結合を実現します。
 
 ### ✨ **主要機能**
 
-- 🔄 **単体・一括処理** - 1つまたは複数のWikipediaページを同時変換
-- 📊 **詳細分析** - 文字数、成功率、ファイル情報を表示
-- 🗜️ **複数形式** - 個別ファイル、結合文書、ZIPダウンロード
-- 🌐 **多言語対応** - 全てのWikipedia言語版に対応
-- � **要使いやすいUI** - 直感的で美しいインターフェース
+- 🤖 **AI自動分析** - SSIM技術による高精度フレーム類似度計算
+- 🎯 **最適接続点検出** - 動画間の最も自然な結合点を自動検出
+- 📊 **リアルタイム分析** - 動画情報の即座表示と詳細分析
+- 🎬 **スムーズ結合** - 視覚的に自然な動画結合を実現
+- 🖼️ **接続フレーム表示** - 結合に使用されるフレームの可視化
 
 ---
 
 ## 🚀 使い方
 
-### �  **オンラインで試す（推奨）**
-**[🚀 デモサイトはこちら](https://huggingface.co/spaces/MakiAi/wikipedia-to-markdown)**
+### 🌐 **オンラインで試す（推奨）**
+**[🚀 デモサイトはこちら](https://huggingface.co/spaces/MakiAi/frame-bridge)**
 
 ### 💻 **ローカルで実行**
 
 \```bash
 # リポジトリをクローン
-git clone https://github.com/your-username/wikipedia-to-markdown.git
-cd wikipedia-to-markdown
+git clone https://github.com/Sunwood-ai-labsII/frame-bridge.git
+cd frame-bridge
 
 # 依存関係をインストール
 pip install -r requirements.txt
@@ -73,40 +74,34 @@ docker-compose up -d
 
 ## 📋 操作方法
 
-### 🔗 **単体処理**
-1. WikipediaのURLを入力
-2. 「✨ 変換する」ボタンをクリック
-3. 生成されたMarkdownをコピーまたはダウンロード
+### 🎬 **動画結合の手順**
+1. **動画1（前半）** をアップロード
+2. **動画2（後半）** をアップロード  
+3. 「🌉 フレームブリッジ実行」ボタンをクリック
+4. AI分析結果と結合された動画をダウンロード
 
-### 📚 **一括処理**
-1. 複数のURLを1行に1つずつ入力
-2. 「🚀 一括変換する」ボタンをクリック
-3. 処理結果を確認し、必要な形式でダウンロード
-
-### 📊 **処理結果の表示例**
+### 📊 **分析結果の表示例**
 \```
-============================================================
-📊 処理結果サマリー
-============================================================
-🔗 処理対象URL数: 3
-✅ 成功: 2
-❌ 失敗: 1
-
-✅ 処理成功: https://ja.wikipedia.org/wiki/Python
-   📄 ページタイトル: Python
-   📊 文字数: 15,432 文字
-   💾 ファイル名: Python.md
+🎬 動画結合完了！
+
+📊 分析結果:
+• フレーム類似度: 0.847
+• 接続品質: 優秀
+• 結合情報:
+  • 動画1の最適な終了フレームを検出
+  • 動画2の最適な開始フレームを検出
+  • スムーズな接続を実現
 \```
 
 ---
 
-## 📦 ダウンロード形式
+## 🎯 技術的特徴
 
-| 形式 | 説明 | 用途 |
+| 技術 | 説明 | 効果 |
 |------|------|------|
-| **📄 個別ファイル** | 各ページを別々のMarkdownファイル | 個別編集・管理 |
-| **📚 結合文書** | 全ページを1つのファイルに結合 | 一括閲覧・印刷 |
-| **🗜️ ZIPアーカイブ** | 全ファイルを圧縮してまとめて | 大量ファイルの管理 |
+| **SSIM分析** | 構造的類似性指標による高精度フレーム比較 | 視覚的に自然な結合点検出 |
+| **自動最適化** | AI による最適接続フレーム自動検出 | 手動編集不要 |
+| **リアルタイム分析** | 動画アップロード時の即座情報表示 | 効率的なワークフロー |
 
 ---
 
@@ -114,25 +109,28 @@ docker-compose up -d
 
 ### **使用技術**
 - **Python 3.8+** - メイン言語
+- **OpenCV** - 動画処理・フレーム抽出
+- **scikit-image** - SSIM計算
 - **Gradio** - Webインターフェース
-- **BeautifulSoup4** - HTML解析
+- **NumPy** - 数値計算
+- **Pillow** - 画像処理
 - **html2text** - Markdown変換
 - **Requests** - HTTP通信
 
 ### **処理フロー**
-1. **URL検証** - 入力URLの妥当性チェック
-2. **HTML取得** - Wikipediaページの取得
-3. **コンテンツ抽出** - 主要コンテンツの抽出
-4. **クリーンアップ** - 不要部分（脚注、編集リンク等）の削除
-5. **Markdown変換** - 整形されたMarkdownに変換
-6. **ファイル生成** - 各種形式でのファイル出力
+1. **動画アップロード** - 2つの動画ファイルをアップロード
+2. **フレーム抽出** - 各動画から代表フレームを抽出
+3. **類似度計算** - SSIM技術による高精度フレーム比較
+4. **最適点検出** - 最も類似度の高い接続フレームを特定
+5. **動画結合** - 検出された最適点で動画を結合
+6. **結果出力** - 結合動画と分析結果を提供
 
 ---
 
 ## 📁 プロジェクト構成
 
 \```
-wikipedia-to-markdown/
+frame-bridge/
 ├── app.py                    # メインアプリケーション
 ├── theme.py                  # UIテーマ設定
 ├── requirements.txt          # Python依存関係
@@ -148,8 +146,11 @@ wikipedia-to-markdown/
 ### **テーマ変更**
 `theme.py`を編集してUIの色やスタイルを変更できます。
 
-### **処理ロジック拡張**
-`app.py`の`scrape_wikipedia_to_markdown_final()`関数を編集して、変換処理をカスタマイズできます。
+### **アルゴリズム調整**
+`app.py`の`find_best_connection_frames()`関数を編集して、フレーム分析ロジックをカスタマイズできます。
+
+### **類似度閾値調整**
+SSIM計算の精度や比較フレーム数を調整して、結合品質を最適化できます。
 
 ---
 
@@ -161,7 +162,7 @@ wikipedia-to-markdown/
 
 ## 🤝 コントリビューション
 
-バグ報告や機能提案は[GitHub Issues](https://github.com/your-username/wikipedia-to-markdown/issues)でお願いします。
+バグ報告や機能提案は[GitHub Issues](https://github.com/Sunwood-ai-labsII/frame-bridge/issues)でお願いします。
 
 ---
 
@@ -169,6 +170,6 @@ wikipedia-to-markdown/
 
 **🌟 このプロジェクトが役に立ったらスターをお願いします！**
 
-*© 2025 Wikipedia to Markdown Converter*
+*© 2025 Frame Bridge - AI Video Merger*
 
 </div>
diff --git a/app.py b/app.py
index cd88a94..deb494d 100644
--- a/app.py
+++ b/app.py
@@ -1,418 +1,273 @@
-import requests
-from bs4 import BeautifulSoup
-import html2text
-import re
 import gradio as gr
 from theme import create_zen_theme
-import tempfile
+from src.frame_bridge import FrameBridge, BatchProcessor
 import os
-import zipfile
-from urllib.parse import urlparse, unquote
 
-def scrape_wikipedia_to_markdown_final(url: str) -> str:
-    """
-    Wikipediaページをスクレイピングし、整形・不要部分削除を行い、
-    タイトルを付けてMarkdownに変換します。
+# Frame Bridge インスタンスを作成
+frame_bridge = FrameBridge(exclude_edge_frames=True)
+batch_processor = BatchProcessor(exclude_edge_frames=True)
 
-    処理フロー：
-    1. ページのタイトルをH1見出しとして取得します。
-    2. 「登場人物」などの<dt>タグを見出しに変換します。
-    3. 生成されたMarkdown文字列から「## 脚注」以降を完全に削除します。
-    4. [編集]リンクを削除します。
-    5. 最終的にタイトルと本文を結合して返します。
-
-    Args:
-        url (str): スクレイピング対象のWikipediaページのURL。
-
-    Returns:
-        str: 整形・変換された最終的なMarkdownコンテンツ。失敗した場合は空の文字列。
-    """
-    try:
-        # 1. HTMLの取得と解析
-        headers = {
-            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
-        }
-        response = requests.get(url, headers=headers)
-        response.raise_for_status()  # HTTPエラーがあれば例外を発生させる
-        response.encoding = response.apparent_encoding  # 文字コードを自動検出
-        soup = BeautifulSoup(response.text, 'html.parser')
-
-        # --- ページのタイトルを取得 ---
-        title_tag = soup.find('h1', id='firstHeading')
-        page_title = title_tag.get_text(strip=True) if title_tag else "Wikipedia ページ"
-
-        # 2. 主要コンテンツエリアの特定
-        content_div = soup.find('div', class_='mw-parser-output')
-        if not content_div:
-            return "エラー: コンテンツエリアが見つかりませんでした。"
-
-        # 3. HTMLの事前整形（登場人物などの見出し化）
-        for dt_tag in content_div.find_all('dt'):
-            h4_tag = soup.new_tag('h4')
-            h4_tag.extend(dt_tag.contents)
-            dt_tag.replace_with(h4_tag)
-
-        # 4. HTMLからMarkdownへの一次変換
-        h = html2text.HTML2Text()
-        h.body_width = 0  # テキストの折り返しを無効にする
-        full_markdown_text = h.handle(str(content_div))
-
-        # 5. 生成されたMarkdownから「## 脚注」以降を削除
-        footnote_marker = "\n## 脚注"
-        footnote_index = full_markdown_text.find(footnote_marker)
-        body_text = full_markdown_text[:footnote_index] if footnote_index != -1 else full_markdown_text
-
-        # 6. [編集]リンクを正規表現で一括削除
-        cleaned_body = re.sub(r'\[\[編集\]\(.+?\)]\n', '', body_text)
-
-        # 7. タイトルと整形後の本文を結合
-        final_markdown = f"# {page_title}\n\n{cleaned_body.strip()}"
-
-        return final_markdown
-
-    except requests.exceptions.RequestException as e:
-        return f"HTTPリクエストエラー: {e}"
-    except Exception as e:
-        return f"予期せぬエラーが発生しました: {e}"
-
-def get_filename_from_url(url):
-    """URLからファイル名を生成する関数"""
-    try:
-        # URLからページ名を抽出
-        parsed_url = urlparse(url)
-        page_name = parsed_url.path.split('/')[-1]
-        # URLデコード
-        page_name = unquote(page_name)
-        # ファイル名として使用できない文字を置換
-        safe_filename = re.sub(r'[<>:"/\\|?*]', '_', page_name)
-        return f"{safe_filename}.md"
-    except:
-        return "wikipedia_page.md"
+def process_sample_videos():
+    """サンプル動画を処理する関数"""
+    video1_path = "examples/assets/example/REI/input/REI-001.mp4"
+    video2_path = "examples/assets/example/REI/input/REI-002.mp4"
+    
+    if not os.path.exists(video1_path) or not os.path.exists(video2_path):
+        return "サンプル動画ファイルが見つかりません。", None, None, None, 0.0
+    
+    return frame_bridge.process_video_bridge(video1_path, video2_path)
 
-def create_download_file(content, filename):
-    """ダウンロード用の一時ファイルを作成する関数"""
+def process_batch_videos(input_folder, output_folder, mode, filename):
+    """バッチ動画処理関数"""
+    if not input_folder or not os.path.exists(input_folder):
+        return "入力フォルダが指定されていないか、存在しません。", None
+    
+    if not output_folder:
+        output_folder = "output"
+    
     try:
-        # 一時ディレクトリにファイルを作成
-        temp_dir = tempfile.gettempdir()
-        file_path = os.path.join(temp_dir, filename)
+        # バッチプロセッサを初期化
+        processor = BatchProcessor(output_dir=output_folder, exclude_edge_frames=True)
         
-        with open(file_path, 'w', encoding='utf-8') as f:
-            f.write(content)
+        if mode == "順次結合":
+            success, final_output, results = processor.process_sequential_merge(input_folder, filename or "merged_sequence.mp4")
+            if success:
+                report = processor.generate_report(results)
+                return f"✅ 順次結合完了!\n📁 出力: {final_output}\n\n{report}", final_output
+            else:
+                return "❌ 順次結合に失敗しました", None
         
-        return file_path
+        elif mode == "ペア結合":
+            success, output_files, results = processor.process_pairwise_merge(input_folder)
+            if success:
+                report = processor.generate_report(results)
+                # 最初の出力ファイルを返す（複数ある場合）
+                first_output = output_files[0] if output_files else None
+                return f"✅ ペア結合完了!\n📁 出力ファイル数: {len(output_files)}\n\n{report}", first_output
+            else:
+                return "❌ ペア結合に失敗しました", None
+    
     except Exception as e:
-        print(f"ファイル作成エラー: {e}")
-        return None
+        return f"処理エラー: {str(e)}", None
 
-def create_zip_file(file_paths, zip_filename="wikipedia_export.zip"):
-    """複数のファイルをZIP形式でまとめる関数"""
+def process_video_bridge(video1, video2, progress=gr.Progress()):
+    """2つの動画を分析して最適な結合点を見つけ、結合する関数"""
+    if video1 is None or video2 is None:
+        return "2つの動画ファイルをアップロードしてください。", None, None, None, None
+    
     try:
-        temp_dir = tempfile.gettempdir()
-        zip_path = os.path.join(temp_dir, zip_filename)
+        progress(0.1, "動画を分析中...")
         
-        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
-            for file_path in file_paths:
-                if os.path.exists(file_path):
-                    # ファイル名のみを取得してZIPに追加
-                    filename = os.path.basename(file_path)
-                    zipf.write(file_path, filename)
+        result_text, output_path, frame1_path, frame2_path, similarity = frame_bridge.process_video_bridge(video1, video2)
         
-        return zip_path
-    except Exception as e:
-        print(f"ZIP作成エラー: {e}")
-        return None
-
-def process_wikipedia_url(url):
-    """Wikipedia URLを処理してMarkdownを生成するGradio用関数"""
-    if not url:
-        return "URLを入力してください。", None
-    
-    # URLが有効かチェック
-    if not url.startswith('http'):
-        return "有効なURLを入力してください（http://またはhttps://から始まるURL）。", None
-    
-    # Wikipedia URLかチェック
-    if 'wikipedia.org' not in url:
-        return "WikipediaのURLを入力してください。", None
-    
-    # スクレイピングを実行
-    markdown_content = scrape_wikipedia_to_markdown_final(url)
-    
-    # ダウンロード用ファイルを作成
-    if not markdown_content.startswith("エラー:") and not markdown_content.startswith("HTTP"):
-        filename = get_filename_from_url(url)
-        file_path = create_download_file(markdown_content, filename)
-        return markdown_content, file_path
-    else:
-        return markdown_content, None
-
-def process_multiple_urls(urls_text, progress=gr.Progress()):
-    """複数のWikipedia URLを一括処理してMarkdownを生成する関数"""
-    if not urls_text.strip():
-        return "URLリストを入力してください。", None, [], None
-    
-    # URLリストを行ごとに分割
-    urls = [url.strip() for url in urls_text.strip().split('\n') if url.strip()]
-    
-    if not urls:
-        return "有効なURLが見つかりませんでした。", None, [], None
-    
-    results = []
-    all_content = []
-    individual_files = []
-    total_urls = len(urls)
-    success_count = 0
-    
-    for i, url in enumerate(urls):
-        progress((i + 1) / total_urls, f"処理中: {i + 1}/{total_urls}")
+        progress(1.0, "完了！")
         
-        # URLの検証
-        if not url.startswith('http'):
-            results.append(f"❌ 無効なURL: {url}")
-            continue
-            
-        if 'wikipedia.org' not in url:
-            results.append(f"❌ Wikipedia以外のURL: {url}")
-            continue
+        return result_text, output_path, frame1_path, frame2_path, similarity
         
-        # スクレイピング実行
-        try:
-            markdown_content = scrape_wikipedia_to_markdown_final(url)
-            if markdown_content.startswith("エラー:") or markdown_content.startswith("HTTP"):
-                results.append(f"❌ 処理失敗: {url}\n   エラー: {markdown_content}")
-            else:
-                # ページタイトルを抽出
-                title_match = re.match(r'^# (.+)', markdown_content)
-                page_title = title_match.group(1) if title_match else "不明なページ"
-                
-                # 文字数とファイル情報を表示
-                char_count = len(markdown_content)
-                filename = get_filename_from_url(url)
-                
-                results.append(f"✅ 処理成功: {url}")
-                results.append(f"   📄 ページタイトル: {page_title}")
-                results.append(f"   📊 文字数: {char_count:,} 文字")
-                results.append(f"   💾 ファイル名: {filename}")
-                
-                all_content.append(markdown_content)
-                success_count += 1
-                
-                # 個別ファイルを作成
-                file_path = create_download_file(markdown_content, filename)
-                if file_path:
-                    individual_files.append(file_path)
-        except Exception as e:
-            results.append(f"❌ 処理エラー: {url}")
-            results.append(f"   エラー内容: {str(e)}")
-    
-    # サマリー情報を追加
-    summary = [
-        "=" * 60,
-        "📊 処理結果サマリー",
-        "=" * 60,
-        f"🔗 処理対象URL数: {total_urls}",
-        f"✅ 成功: {success_count}",
-        f"❌ 失敗: {total_urls - success_count}",
-        ""
-    ]
-    
-    # 結果を結合
-    final_result = "\n".join(summary + results)
-    
-    # 一括ダウンロード用ファイルを作成
-    batch_file_path = None
-    if all_content:
-        combined_content = "\n\n" + "="*80 + "\n\n".join(all_content)
-        batch_file_path = create_download_file(combined_content, "wikipedia_batch_export.md")
-    
-    # ZIPファイルを作成
-    zip_file_path = None
-    if individual_files:
-        zip_file_path = create_zip_file(individual_files, "wikipedia_export.zip")
-    
-    return final_result, batch_file_path, individual_files, zip_file_path
+    except Exception as e:
+        return f"処理エラー: {str(e)}", None, None, None, None
+
+def analyze_video_details(video_path):
+    """動画の詳細情報を分析する関数"""
+    if video_path is None:
+        return ""
+    return frame_bridge.processor.analyze_video_details(video_path)
 
 # Gradioインターフェースの作成
 def create_interface():
     """Gradioインターフェースを作成する関数"""
     theme = create_zen_theme()
     
-    with gr.Blocks(theme=theme, title="Wikipedia to Markdown Converter") as demo:
+    with gr.Blocks(theme=theme, title="Frame Bridge - 動画フレーム結合アプリ") as demo:
         # ヘッダー
         gr.HTML("""
         <div style='text-align: center; margin-bottom: 2rem; padding: 2rem; background: linear-gradient(135deg, #d4a574 0%, #ffffff 50%, #f5f2ed 100%); color: #3d405b; border-radius: 12px;'>
-            <h1 style='font-size: 3rem; margin-bottom: 0.5rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);'>📚 Wikipedia to Markdown Converter</h1>
-            <p style='font-size: 1.2rem; opacity: 0.8;'>WikipediaのURLを入力して、Markdown形式に変換します</p>
+            <h1 style='font-size: 3rem; margin-bottom: 0.5rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);'>🎬 Frame Bridge</h1>
+            <p style='font-size: 1.2rem; opacity: 0.8;'>2つの動画を最適なフレームで自動結合するAIアプリ</p>
         </div>
         """)
         
         # タブの作成
         with gr.Tabs():
             # 単体処理タブ
-            with gr.TabItem("🔗 単体処理"):
+            with gr.TabItem("🎥 単体処理"):
                 with gr.Row():
                     with gr.Column(scale=1):
-                        url_input = gr.Textbox(
-                            label="🔗 Wikipedia URL",
-                            placeholder="https://ja.wikipedia.org/wiki/...",
-                            value="https://ja.wikipedia.org/wiki/Python"
+                        gr.Markdown("### 📹 動画アップロード")
+                        video1_input = gr.Video(
+                            label="🎥 動画1（前半）",
+                            height=300
+                        )
+                        video1_info = gr.Textbox(
+                            label="📊 動画1の情報",
+                            lines=6,
+                            interactive=False
+                        )
+                        
+                        video2_input = gr.Video(
+                            label="🎥 動画2（後半）",
+                            height=300
+                        )
+                        video2_info = gr.Textbox(
+                            label="📊 動画2の情報",
+                            lines=6,
+                            interactive=False
                         )
-                        convert_btn = gr.Button("✨ 変換する", variant="primary")
+                        
+                        bridge_btn = gr.Button("🌉 フレームブリッジ実行", variant="primary", size="lg")
+                        sample_btn = gr.Button("🎬 サンプル動画で試す", variant="secondary", size="lg")
                     
                     with gr.Column(scale=1):
-                        output_text = gr.Textbox(
-                            label="📝 変換されたMarkdown",
-                            lines=20,
-                            max_lines=50,
+                        gr.Markdown("### 🎯 結合結果")
+                        result_text = gr.Textbox(
+                            label="📝 分析結果",
+                            lines=10,
                             show_copy_button=True
                         )
-                        download_file = gr.File(
-                            label="📥 マークダウンファイルをダウンロード",
-                            visible=False
+                        
+                        merged_video = gr.Video(
+                            label="🎬 結合された動画",
+                            height=300
+                        )
+                        
+                        # 接続フレーム表示
+                        with gr.Row():
+                            connection_frame1 = gr.Image(
+                                label="🔗 動画1の接続フレーム",
+                                height=200
+                            )
+                            connection_frame2 = gr.Image(
+                                label="🔗 動画2の接続フレーム", 
+                                height=200
+                            )
+                        
+                        similarity_score = gr.Number(
+                            label="📈 フレーム類似度スコア",
+                            precision=3
                         )
-                
-                # ボタンクリック時の処理
-                def update_single_output(url):
-                    content, file_path = process_wikipedia_url(url)
-                    if file_path:
-                        return content, gr.update(value=file_path, visible=True)
-                    else:
-                        return content, gr.update(visible=False)
-                
-                convert_btn.click(
-                    fn=update_single_output,
-                    inputs=url_input,
-                    outputs=[output_text, download_file]
-                )
-                
-                # 使用例
-                def example_process(url):
-                    content, _ = process_wikipedia_url(url)
-                    return content
-                
-                gr.Examples(
-                    examples=[
-                        ["https://ja.wikipedia.org/wiki/Python"],
-                        ["https://ja.wikipedia.org/wiki/JavaScript"],
-                        ["https://ja.wikipedia.org/wiki/HTML"]
-                    ],
-                    inputs=url_input,
-                    outputs=output_text,
-                    fn=example_process,
-                    cache_examples=False
-                )
             
-            # 一括処理タブ
-            with gr.TabItem("📋 一括処理"):
+            # バッチ処理タブ
+            with gr.TabItem("📁 バッチ処理"):
                 with gr.Row():
                     with gr.Column(scale=1):
-                        urls_input = gr.Textbox(
-                            label="📋 Wikipedia URLリスト（1行に1つずつ）",
-                            placeholder="https://ja.wikipedia.org/wiki/Python\nhttps://ja.wikipedia.org/wiki/JavaScript\nhttps://ja.wikipedia.org/wiki/HTML",
-                            lines=10,
-                            value="https://ja.wikipedia.org/wiki/Python\nhttps://ja.wikipedia.org/wiki/JavaScript"
+                        gr.Markdown("### 📂 フォルダ指定")
+                        input_folder = gr.Textbox(
+                            label="📥 入力フォルダパス",
+                            placeholder="例: examples/assets/example/REI/input",
+                            value="examples/assets/example/REI/input"
+                        )
+                        output_folder = gr.Textbox(
+                            label="📤 出力フォルダパス",
+                            placeholder="例: examples/assets/example/REI/output",
+                            value="examples/assets/example/REI/output"
+                        )
+                        
+                        processing_mode = gr.Radio(
+                            label="🔄 処理モード",
+                            choices=["順次結合", "ペア結合"],
+                            value="順次結合",
+                            info="順次結合: 全動画を1つに結合 / ペア結合: 2つずつペアで結合"
+                        )
+                        
+                        output_filename = gr.Textbox(
+                            label="📄 出力ファイル名 (順次結合のみ)",
+                            placeholder="REI_merged_sequence.mp4",
+                            value="REI_merged_sequence.mp4"
                         )
-                        batch_convert_btn = gr.Button("🚀 一括変換する", variant="primary")
+                        
+                        batch_btn = gr.Button("🚀 バッチ処理実行", variant="primary", size="lg")
                     
                     with gr.Column(scale=1):
-                        batch_output_text = gr.Textbox(
-                            label="📝 一括変換結果",
+                        gr.Markdown("### 📊 処理結果")
+                        batch_result = gr.Textbox(
+                            label="📝 バッチ処理結果",
                             lines=15,
-                            max_lines=30,
                             show_copy_button=True
                         )
-                        batch_download_file = gr.File(
-                            label="📥 全体をまとめてダウンロード",
-                            visible=False
-                        )
-                        zip_download_file = gr.File(
-                            label="🗜️ ZIPファイルでダウンロード",
-                            visible=False
-                        )
                         
-                        # 個別ダウンロードエリア
-                        individual_downloads = gr.Column(visible=False)
-                        with individual_downloads:
-                            gr.Markdown("### 📥 個別ダウンロード")
-                            individual_file_1 = gr.File(label="", visible=False)
-                            individual_file_2 = gr.File(label="", visible=False)
-                            individual_file_3 = gr.File(label="", visible=False)
-                            individual_file_4 = gr.File(label="", visible=False)
-                            individual_file_5 = gr.File(label="", visible=False)
+                        batch_output = gr.Video(
+                            label="🎬 出力動画（プレビュー）",
+                            height=300
+                        )
+
+        
+                # 動画情報の自動更新
+                def update_video1_info(video):
+                    if video is None:
+                        return ""
+                    return analyze_video_details(video)
                 
-                # 一括処理ボタンクリック時の処理
-                def update_batch_output(urls_text):
-                    content, batch_file_path, individual_files, zip_file_path = process_multiple_urls(urls_text)
-                    
-                    # 戻り値のリストを準備
-                    outputs = [content]
-                    
-                    # 一括ダウンロードファイル
-                    if batch_file_path:
-                        outputs.append(gr.update(value=batch_file_path, visible=True))
-                    else:
-                        outputs.append(gr.update(visible=False))
-                    
-                    # ZIPダウンロードファイル
-                    if zip_file_path:
-                        outputs.append(gr.update(value=zip_file_path, visible=True))
-                    else:
-                        outputs.append(gr.update(visible=False))
-                    
-                    # 個別ダウンロードエリアの表示/非表示
-                    if individual_files:
-                        outputs.append(gr.update(visible=True))
-                    else:
-                        outputs.append(gr.update(visible=False))
-                    
-                    # 個別ファイル（最大5つまで表示）
-                    for i in range(5):
-                        if i < len(individual_files):
-                            filename = os.path.basename(individual_files[i])
-                            outputs.append(gr.update(value=individual_files[i], visible=True, label=f"📄 {filename}"))
-                        else:
-                            outputs.append(gr.update(visible=False))
-                    
-                    return outputs
+                def update_video2_info(video):
+                    if video is None:
+                        return ""
+                    return analyze_video_details(video)
                 
-                batch_convert_btn.click(
-                    fn=update_batch_output,
-                    inputs=urls_input,
-                    outputs=[
-                        batch_output_text, 
-                        batch_download_file,
-                        zip_download_file,
-                        individual_downloads,
-                        individual_file_1,
-                        individual_file_2,
-                        individual_file_3,
-                        individual_file_4,
-                        individual_file_5
-                    ]
+                video1_input.change(
+                    fn=update_video1_info,
+                    inputs=video1_input,
+                    outputs=video1_info
                 )
                 
-                gr.Markdown("### 💡 一括処理の使い方")
-                gr.Markdown("1. テキストエリアに変換したいWikipediaのURLを1行に1つずつ入力します")
-                gr.Markdown("2. 「🚀 一括変換する」ボタンをクリックします")
-                gr.Markdown("3. 処理の進行状況が表示され、完了後に結果が表示されます")
-                gr.Markdown("4. 各URLの処理結果（成功/失敗）が明確に表示されます")
+                video2_input.change(
+                    fn=update_video2_info,
+                    inputs=video2_input,
+                    outputs=video2_info
+                )
+                
+                # メイン処理
+                bridge_btn.click(
+                    fn=process_video_bridge,
+                    inputs=[video1_input, video2_input],
+                    outputs=[result_text, merged_video, connection_frame1, connection_frame2, similarity_score]
+                )
+                
+                # サンプル動画処理
+                sample_btn.click(
+                    fn=process_sample_videos,
+                    inputs=[],
+                    outputs=[result_text, merged_video, connection_frame1, connection_frame2, similarity_score]
+                )
+                
+                # バッチ処理
+                batch_btn.click(
+                    fn=process_batch_videos,
+                    inputs=[input_folder, output_folder, processing_mode, output_filename],
+                    outputs=[batch_result, batch_output]
+                )
         
+        # 使用方法の説明
         gr.Markdown("---")
-        gr.Markdown("### 🎯 基本的な使用方法")
-        gr.Markdown("- **単体処理**: 1つのWikipediaページを変換したい場合")
-        gr.Markdown("- **一括処理**: 複数のWikipediaページを一度に変換したい場合")
-        gr.Markdown("- 生成されたMarkdownは右側のテキストエリアからコピーできます")
-        gr.Markdown("- **📥 ダウンロード機能**: 変換が成功すると、マークダウンファイルとして直接ダウンロードできます")
-        gr.Markdown("  - 単体処理: ページ名に基づいたファイル名で個別ダウンロード")
-        gr.Markdown("  - 一括処理: 各URLごとの個別ダウンロード + 全体をまとめた一括ダウンロード + **🗜️ ZIPファイル**")
-        gr.Markdown("  - 個別ダウンロード: 成功した各ページを個別のファイルとしてダウンロード可能（最大5つまで表示）")
-        gr.Markdown("  - **ZIPダウンロード**: 複数のMarkdownファイルを1つのZIPファイルにまとめてダウンロード")
+        gr.Markdown("### 🎯 使用方法")
+        
+        with gr.Tabs():
+            with gr.TabItem("🎥 単体処理"):
+                gr.Markdown("1. **動画1（前半）**: 結合したい最初の動画をアップロード")
+                gr.Markdown("2. **動画2（後半）**: 結合したい2番目の動画をアップロード")
+                gr.Markdown("3. **フレームブリッジ実行**: AIが最適な接続点を自動検出して結合")
+                gr.Markdown("4. **サンプル動画で試す**: assetsフォルダのサンプル動画で機能をテスト")
+            
+            with gr.TabItem("📁 バッチ処理"):
+                gr.Markdown("1. **入力フォルダ**: 動画ファイルが格納されたフォルダパスを指定")
+                gr.Markdown("2. **出力フォルダ**: 結合結果を保存するフォルダパスを指定")
+                gr.Markdown("3. **処理モード選択**:")
+                gr.Markdown("   - **順次結合**: フォルダ内の全動画を名前順に1つの動画に結合")
+                gr.Markdown("   - **ペア結合**: 動画を2つずつペアにして結合（複数の出力ファイル）")
+                gr.Markdown("4. **出力ファイル名**: 順次結合の場合の最終ファイル名を指定")
+                gr.Markdown("5. **バッチ処理実行**: 指定した設定で一括処理を開始")
+        
+        gr.Markdown("### 🔬 技術的特徴")
+        gr.Markdown("- **SSIM（構造的類似性指標）**: フレーム間の視覚的類似度を高精度で計算")
+        gr.Markdown("- **自動最適化**: 動画1の終了部分と動画2の開始部分から最適な接続点を検出")
+        gr.Markdown("- **スムーズな結合**: 視覚的に自然な動画結合を実現")
+        gr.Markdown("- **バッチ処理**: 複数動画の自動処理とレポート生成")
+        gr.Markdown("- **ファイル名ソート**: 自然順序でのファイル名ソートによる正確な順序処理")
         
         # ZENテーマの説明
         gr.HTML("""
         <div style='text-align: center; margin-top: 2rem; padding: 1.5rem; background: #ffffff; border-radius: 12px;'>
             <h3 style='color: #3d405b; margin-top: 0;'>🧘‍♀️ ZENテーマ</h3>
-            <p style='color: #8b7355;'>和モダンなデザインで、使いやすさと美しさを追求しました</p>
+            <p style='color: #8b7355;'>和モダンなデザインで、直感的な動画編集体験を提供</p>
+            <p style='color: #8b7355; font-size: 0.9rem;'>単体処理とバッチ処理の両方に対応した高機能動画結合アプリ</p>
         </div>
         """)
     
diff --git a/pyproject.toml b/pyproject.toml
new file mode 100644
index 0000000..7ca8550
--- /dev/null
+++ b/pyproject.toml
@@ -0,0 +1,163 @@
+[build-system]
+requires = ["setuptools>=61.0", "wheel"]
+build-backend = "setuptools.build_meta"
+
+[project]
+name = "frame-bridge"
+version = "1.0.0"
+description = "AI-powered video frame bridging application using SSIM technology"
+readme = "README.md"
+license = {text = "MIT"}
+authors = [
+    {name = "Sunwood AI Labs", email = "info@sunwood-ai-labs.com"}
+]
+maintainers = [
+    {name = "Sunwood AI Labs", email = "info@sunwood-ai-labs.com"}
+]
+keywords = [
+    "video-processing",
+    "ai",
+    "computer-vision",
+    "gradio",
+    "opencv",
+    "ssim",
+    "frame-analysis",
+    "video-editing"
+]
+classifiers = [
+    "Development Status :: 4 - Beta",
+    "Intended Audience :: Developers",
+    "Intended Audience :: End Users/Desktop",
+    "License :: OSI Approved :: MIT License",
+    "Operating System :: OS Independent",
+    "Programming Language :: Python :: 3",
+
+    "Programming Language :: Python :: 3.10",
+    "Programming Language :: Python :: 3.11",
+    "Topic :: Multimedia :: Video",
+    "Topic :: Multimedia :: Video :: Display",
+    "Topic :: Scientific/Engineering :: Artificial Intelligence",
+    "Topic :: Scientific/Engineering :: Image Processing",
+]
+requires-python = ">=3.10"
+dependencies = [
+    "opencv-python>=4.8.0",
+    "numpy>=1.24.0",
+    "pillow>=10.0.0",
+    "gradio>=5.42.0",
+    "scikit-image>=0.21.0",
+]
+
+[project.optional-dependencies]
+dev = [
+    "pytest>=7.0.0",
+    "pytest-cov>=4.0.0",
+    "black>=23.0.0",
+    "flake8>=6.0.0",
+    "mypy>=1.0.0",
+    "pre-commit>=3.0.0",
+]
+docs = [
+    "sphinx>=6.0.0",
+    "sphinx-rtd-theme>=1.2.0",
+    "myst-parser>=1.0.0",
+]
+
+[project.urls]
+Homepage = "https://github.com/Sunwood-ai-labsII/frame-bridge"
+Repository = "https://github.com/Sunwood-ai-labsII/frame-bridge.git"
+Documentation = "https://github.com/Sunwood-ai-labsII/frame-bridge#readme"
+"Bug Tracker" = "https://github.com/Sunwood-ai-labsII/frame-bridge/issues"
+"Demo Site" = "https://huggingface.co/spaces/MakiAi/frame-bridge"
+
+[project.scripts]
+frame-bridge = "app:main"
+frame-bridge-test = "test_sample:main"
+frame-bridge-batch = "batch_test:main"
+
+[tool.setuptools.packages.find]
+where = ["."]
+include = ["*"]
+exclude = ["tests*", "docs*", ".github*"]
+
+[tool.setuptools.package-data]
+"*" = ["*.md", "*.txt", "*.yml", "*.yaml"]
+
+[tool.black]
+line-length = 88
+target-version = ['py38', 'py39', 'py310', 'py311']
+include = '\.pyi?$'
+extend-exclude = '''
+/(
+  # directories
+  \.eggs
+  | \.git
+  | \.hg
+  | \.mypy_cache
+  | \.tox
+  | \.venv
+  | build
+  | dist
+)/
+'''
+
+[tool.mypy]
+python_version = "3.8"
+warn_return_any = true
+warn_unused_configs = true
+disallow_untyped_defs = true
+disallow_incomplete_defs = true
+check_untyped_defs = true
+disallow_untyped_decorators = true
+no_implicit_optional = true
+warn_redundant_casts = true
+warn_unused_ignores = true
+warn_no_return = true
+warn_unreachable = true
+strict_equality = true
+
+[tool.pytest.ini_options]
+minversion = "7.0"
+addopts = "-ra -q --strict-markers --strict-config"
+testpaths = ["tests"]
+python_files = ["test_*.py", "*_test.py"]
+python_classes = ["Test*"]
+python_functions = ["test_*"]
+
+[tool.coverage.run]
+source = ["."]
+omit = [
+    "tests/*",
+    "setup.py",
+    "*/site-packages/*",
+    ".venv/*",
+    "venv/*",
+]
+
+[tool.coverage.report]
+exclude_lines = [
+    "pragma: no cover",
+    "def __repr__",
+    "if self.debug:",
+    "if settings.DEBUG",
+    "raise AssertionError",
+    "raise NotImplementedError",
+    "if 0:",
+    "if __name__ == .__main__.:",
+    "class .*\\bProtocol\\):",
+    "@(abc\\.)?abstractmethod",
+]
+
+[tool.flake8]
+max-line-length = 88
+extend-ignore = ["E203", "W503"]
+exclude = [
+    ".git",
+    "__pycache__",
+    "docs/source/conf.py",
+    "old",
+    "build",
+    "dist",
+    ".venv",
+    "venv",
+]
\ No newline at end of file
diff --git a/requirements.txt b/requirements.txt
index 0304013..884f121 100644
--- a/requirements.txt
+++ b/requirements.txt
@@ -1,4 +1,5 @@
-requests>=2.31.0
-beautifulsoup4>=4.12.0
-html2text>=2020.1.16
+opencv-python>=4.8.0
+numpy>=1.24.0
+pillow>=10.0.0
 gradio>=5.42.0
+scikit-image>=0.21.0
diff --git a/scripts/show_structure.py b/scripts/show_structure.py
new file mode 100644
index 0000000..218c552
--- /dev/null
+++ b/scripts/show_structure.py
@@ -0,0 +1,58 @@
+"""
+Frame Bridge - Project Structure Display
+プロジェクト構造を表示するスクリプト
+"""
+
+import os
+from pathlib import Path
+
+def show_tree(directory, prefix="", max_depth=3, current_depth=0):
+    """ディレクトリツリーを表示"""
+    if current_depth > max_depth:
+        return
+    
+    directory = Path(directory)
+    if not directory.exists():
+        return
+    
+    items = sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
+    
+    for i, item in enumerate(items):
+        is_last = i == len(items) - 1
+        current_prefix = "└── " if is_last else "├── "
+        
+        if item.is_dir():
+            print(f"{prefix}{current_prefix}{item.name}/")
+            extension = "    " if is_last else "│   "
+            show_tree(item, prefix + extension, max_depth, current_depth + 1)
+        else:
+            print(f"{prefix}{current_prefix}{item.name}")
+
+def main():
+    """メイン処理"""
+    print("🎬 Frame Bridge - プロジェクト構造")
+    print("=" * 60)
+    
+    # プロジェクトルートから表示
+    project_root = Path(__file__).parent.parent
+    os.chdir(project_root)
+    
+    print("📁 プロジェクト構造:")
+    print("frame-bridge/")
+    show_tree(".", max_depth=3)
+    
+    print("\n" + "=" * 60)
+    print("📊 主要コンポーネント:")
+    print("• src/frame_bridge/     - メインライブラリ")
+    print("• scripts/              - 実行スクリプト")
+    print("• tests/                - テストファイル")
+    print("• examples/             - サンプルデータ")
+    print("• docs/                 - ドキュメント")
+    
+    print("\n🎯 新機能:")
+    print("• エッジフレーム除外オプション")
+    print("• 最適化されたフォルダ構造")
+    print("• 設定管理システム")
+
+if __name__ == "__main__":
+    main()
\ No newline at end of file
diff --git a/src/frame_bridge/__init__.py b/src/frame_bridge/__init__.py
new file mode 100644
index 0000000..19144ea
--- /dev/null
+++ b/src/frame_bridge/__init__.py
@@ -0,0 +1,20 @@
+"""
+Frame Bridge - AI-powered video frame bridging application
+2つの動画を最適なフレームで自動結合するAIアプリケーション
+"""
+
+__version__ = "1.0.0"
+__author__ = "Sunwood AI Labs"
+__email__ = "info@sunwood-ai-labs.com"
+
+from .video_processor import VideoProcessor, FrameBridge
+from .batch_processor import BatchProcessor
+
+__all__ = [
+    "VideoProcessor",
+    "FrameBridge", 
+    "BatchProcessor",
+    "__version__",
+    "__author__",
+    "__email__"
+]
\ No newline at end of file
diff --git a/src/frame_bridge/batch_processor.py b/src/frame_bridge/batch_processor.py
new file mode 100644
index 0000000..d808640
--- /dev/null
+++ b/src/frame_bridge/batch_processor.py
@@ -0,0 +1,311 @@
+"""
+Frame Bridge - Batch Processing Module
+フォルダ内の動画ファイルを順次結合するバッチ処理モジュール
+"""
+
+import os
+import glob
+import logging
+from pathlib import Path
+from typing import List, Tuple, Optional
+from .video_processor import FrameBridge
+
+# ログ設定
+logging.basicConfig(level=logging.INFO)
+logger = logging.getLogger(__name__)
+
+
+class BatchProcessor:
+    """バッチ処理を行うクラス"""
+    
+    def __init__(self, output_dir: str = "output", exclude_edge_frames: bool = True):
+        """
+        初期化
+        
+        Args:
+            output_dir: 出力ディレクトリ
+            exclude_edge_frames: 最初と最後のフレームを除外するかどうか
+        """
+        self.frame_bridge = FrameBridge(exclude_edge_frames=exclude_edge_frames)
+        self.output_dir = Path(output_dir)
+        self.output_dir.mkdir(exist_ok=True)
+        self.exclude_edge_frames = exclude_edge_frames
+        
+        # サポートする動画形式
+        self.supported_formats = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm']
+    
+    def get_video_files(self, input_dir: str) -> List[str]:
+        """
+        指定ディレクトリから動画ファイルを取得し、名前順にソート
+        
+        Args:
+            input_dir: 入力ディレクトリ
+            
+        Returns:
+            ソートされた動画ファイルのリスト
+        """
+        input_path = Path(input_dir)
+        if not input_path.exists():
+            logger.error(f"入力ディレクトリが存在しません: {input_dir}")
+            return []
+        
+        video_files = []
+        for ext in self.supported_formats:
+            pattern = str(input_path / f"*{ext}")
+            video_files.extend(glob.glob(pattern))
+        
+        # ファイル名でソート（自然順序）
+        video_files.sort(key=lambda x: os.path.basename(x).lower())
+        
+        logger.info(f"検出された動画ファイル数: {len(video_files)}")
+        for i, file in enumerate(video_files):
+            logger.info(f"  {i+1}. {os.path.basename(file)}")
+        
+        return video_files
+    
+    def process_sequential_merge(self, input_dir: str, output_filename: str = "merged_sequence.mp4") -> Tuple[bool, str, List[dict]]:
+        """
+        フォルダ内の動画を順次結合
+        
+        Args:
+            input_dir: 入力ディレクトリ
+            output_filename: 出力ファイル名
+            
+        Returns:
+            Tuple[成功フラグ, 最終出力パス, 処理結果リスト]
+        """
+        video_files = self.get_video_files(input_dir)
+        
+        if len(video_files) < 2:
+            return False, "", [{"error": "結合には最低2つの動画ファイルが必要です"}]
+        
+        results = []
+        current_video = video_files[0]
+        
+        logger.info(f"順次結合処理開始: {len(video_files)}個のファイル")
+        
+        for i in range(1, len(video_files)):
+            next_video = video_files[i]
+            
+            logger.info(f"結合 {i}/{len(video_files)-1}: {os.path.basename(current_video)} + {os.path.basename(next_video)}")
+            
+            # 中間出力ファイル名
+            if i == len(video_files) - 1:
+                # 最後の結合は最終ファイル名
+                temp_output = self.output_dir / output_filename
+            else:
+                # 中間ファイル
+                temp_output = self.output_dir / f"temp_merge_{i}.mp4"
+            
+            # 結合処理
+            result_text, output_path, frame1_path, frame2_path, similarity = self.frame_bridge.process_video_bridge(
+                current_video, next_video
+            )
+            
+            if output_path and os.path.exists(output_path):
+                # 結果を指定の場所に移動
+                import shutil
+                shutil.move(output_path, str(temp_output))
+                
+                result_info = {
+                    "step": i,
+                    "video1": os.path.basename(current_video),
+                    "video2": os.path.basename(next_video),
+                    "similarity": similarity,
+                    "output": str(temp_output),
+                    "success": True
+                }
+                
+                # 次のループでは結合結果を使用
+                current_video = str(temp_output)
+                
+                logger.info(f"結合完了 {i}/{len(video_files)-1}: 類似度 {similarity:.3f}")
+            else:
+                result_info = {
+                    "step": i,
+                    "video1": os.path.basename(current_video),
+                    "video2": os.path.basename(next_video),
+                    "error": result_text,
+                    "success": False
+                }
+                logger.error(f"結合失敗 {i}/{len(video_files)-1}: {result_text}")
+            
+            results.append(result_info)
+            
+            # 中間ファイルのクリーンアップ（最後以外）
+            if i > 1 and i < len(video_files) - 1:
+                prev_temp = self.output_dir / f"temp_merge_{i-1}.mp4"
+                if prev_temp.exists():
+                    prev_temp.unlink()
+        
+        final_output = self.output_dir / output_filename
+        success = final_output.exists()
+        
+        if success:
+            logger.info(f"全結合処理完了: {final_output}")
+            logger.info(f"最終ファイルサイズ: {final_output.stat().st_size / (1024*1024):.1f} MB")
+        
+        return success, str(final_output), results
+    
+    def process_pairwise_merge(self, input_dir: str) -> Tuple[bool, List[str], List[dict]]:
+        """
+        フォルダ内の動画をペアワイズで結合
+        
+        Args:
+            input_dir: 入力ディレクトリ
+            
+        Returns:
+            Tuple[成功フラグ, 出力ファイルリスト, 処理結果リスト]
+        """
+        video_files = self.get_video_files(input_dir)
+        
+        if len(video_files) < 2:
+            return False, [], [{"error": "結合には最低2つの動画ファイルが必要です"}]
+        
+        results = []
+        output_files = []
+        
+        logger.info(f"ペアワイズ結合処理開始: {len(video_files)}個のファイル")
+        
+        # ペアごとに処理
+        for i in range(0, len(video_files) - 1, 2):
+            video1 = video_files[i]
+            video2 = video_files[i + 1] if i + 1 < len(video_files) else None
+            
+            if video2 is None:
+                # 奇数個の場合、最後のファイルはそのままコピー
+                import shutil
+                output_name = f"single_{os.path.basename(video1)}"
+                output_path = self.output_dir / output_name
+                shutil.copy2(video1, output_path)
+                output_files.append(str(output_path))
+                
+                results.append({
+                    "pair": i // 2 + 1,
+                    "video1": os.path.basename(video1),
+                    "video2": None,
+                    "action": "copied",
+                    "output": str(output_path),
+                    "success": True
+                })
+                continue
+            
+            logger.info(f"ペア {i//2 + 1}: {os.path.basename(video1)} + {os.path.basename(video2)}")
+            
+            # 出力ファイル名
+            output_name = f"merged_pair_{i//2 + 1}_{os.path.basename(video1).split('.')[0]}_{os.path.basename(video2).split('.')[0]}.mp4"
+            output_path = self.output_dir / output_name
+            
+            # 結合処理
+            result_text, temp_output, frame1_path, frame2_path, similarity = self.frame_bridge.process_video_bridge(
+                video1, video2
+            )
+            
+            if temp_output and os.path.exists(temp_output):
+                # 結果を指定の場所に移動
+                import shutil
+                shutil.move(temp_output, str(output_path))
+                output_files.append(str(output_path))
+                
+                result_info = {
+                    "pair": i // 2 + 1,
+                    "video1": os.path.basename(video1),
+                    "video2": os.path.basename(video2),
+                    "similarity": similarity,
+                    "output": str(output_path),
+                    "success": True
+                }
+                
+                logger.info(f"ペア結合完了 {i//2 + 1}: 類似度 {similarity:.3f}")
+            else:
+                result_info = {
+                    "pair": i // 2 + 1,
+                    "video1": os.path.basename(video1),
+                    "video2": os.path.basename(video2),
+                    "error": result_text,
+                    "success": False
+                }
+                logger.error(f"ペア結合失敗 {i//2 + 1}: {result_text}")
+            
+            results.append(result_info)
+        
+        success = len(output_files) > 0
+        logger.info(f"ペアワイズ結合完了: {len(output_files)}個のファイル出力")
+        
+        return success, output_files, results
+    
+    def generate_report(self, results: List[dict], output_path: str = None) -> str:
+        """
+        処理結果のレポートを生成
+        
+        Args:
+            results: 処理結果リスト
+            output_path: レポート出力パス
+            
+        Returns:
+            レポート文字列
+        """
+        report_lines = [
+            "🎬 Frame Bridge - バッチ処理レポート",
+            "=" * 60,
+            f"📅 処理日時: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
+            f"📊 総処理数: {len(results)}",
+            ""
+        ]
+        
+        success_count = sum(1 for r in results if r.get('success', False))
+        report_lines.extend([
+            f"✅ 成功: {success_count}",
+            f"❌ 失敗: {len(results) - success_count}",
+            ""
+        ])
+        
+        # 詳細結果
+        for i, result in enumerate(results, 1):
+            if result.get('success', False):
+                if 'similarity' in result:
+                    quality = self._evaluate_quality(result['similarity'])
+                    report_lines.extend([
+                        f"📋 処理 {i}: ✅ 成功",
+                        f"   📹 動画1: {result.get('video1', 'N/A')}",
+                        f"   📹 動画2: {result.get('video2', 'N/A')}",
+                        f"   📈 類似度: {result['similarity']:.3f} ({quality})",
+                        f"   📁 出力: {os.path.basename(result.get('output', 'N/A'))}",
+                        ""
+                    ])
+                else:
+                    report_lines.extend([
+                        f"📋 処理 {i}: ✅ {result.get('action', '処理完了')}",
+                        f"   📹 ファイル: {result.get('video1', 'N/A')}",
+                        f"   📁 出力: {os.path.basename(result.get('output', 'N/A'))}",
+                        ""
+                    ])
+            else:
+                report_lines.extend([
+                    f"📋 処理 {i}: ❌ 失敗",
+                    f"   📹 動画1: {result.get('video1', 'N/A')}",
+                    f"   📹 動画2: {result.get('video2', 'N/A')}",
+                    f"   ⚠️ エラー: {result.get('error', '不明なエラー')}",
+                    ""
+                ])
+        
+        report_text = "\n".join(report_lines)
+        
+        # ファイルに保存
+        if output_path:
+            with open(output_path, 'w', encoding='utf-8') as f:
+                f.write(report_text)
+            logger.info(f"レポート保存: {output_path}")
+        
+        return report_text
+    
+    def _evaluate_quality(self, similarity: float) -> str:
+        """類似度から品質を評価"""
+        if similarity > 0.8:
+            return "優秀"
+        elif similarity > 0.6:
+            return "良好"
+        elif similarity > 0.4:
+            return "普通"
+        else:
+            return "要確認"
\ No newline at end of file
diff --git a/src/frame_bridge/config.py b/src/frame_bridge/config.py
new file mode 100644
index 0000000..a51c7bd
--- /dev/null
+++ b/src/frame_bridge/config.py
@@ -0,0 +1,46 @@
+"""
+Frame Bridge - Configuration Module
+設定管理モジュール
+"""
+
+from dataclasses import dataclass
+from typing import List
+
+
+@dataclass
+class VideoProcessorConfig:
+    """VideoProcessor設定クラス"""
+    similarity_threshold: float = 0.3
+    exclude_edge_frames: bool = True
+    num_frames_video1: int = 30  # 動画1から抽出するフレーム数
+    num_frames_video2: int = 10  # 動画2から抽出するフレーム数
+    comparison_frames: int = 3   # 動画2の比較対象フレーム数
+
+
+@dataclass
+class BatchProcessorConfig:
+    """BatchProcessor設定クラス"""
+    output_dir: str = "output"
+    exclude_edge_frames: bool = True
+    supported_formats: List[str] = None
+    
+    def __post_init__(self):
+        if self.supported_formats is None:
+            self.supported_formats = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm']
+
+
+@dataclass
+class AppConfig:
+    """アプリケーション全体設定クラス"""
+    video_processor: VideoProcessorConfig = None
+    batch_processor: BatchProcessorConfig = None
+    
+    def __post_init__(self):
+        if self.video_processor is None:
+            self.video_processor = VideoProcessorConfig()
+        if self.batch_processor is None:
+            self.batch_processor = BatchProcessorConfig()
+
+
+# デフォルト設定
+DEFAULT_CONFIG = AppConfig()
\ No newline at end of file
diff --git a/src/frame_bridge/video_processor.py b/src/frame_bridge/video_processor.py
new file mode 100644
index 0000000..85d78c8
--- /dev/null
+++ b/src/frame_bridge/video_processor.py
@@ -0,0 +1,399 @@
+"""
+Frame Bridge - Video Processing Module
+2つの動画を最適なフレームで結合するための処理モジュール
+"""
+
+import cv2
+import numpy as np
+from PIL import Image
+import tempfile
+import os
+from skimage.metrics import structural_similarity as ssim
+from typing import Tuple, List, Optional, Union
+import logging
+
+# ログ設定
+logging.basicConfig(level=logging.INFO)
+logger = logging.getLogger(__name__)
+
+
+class VideoProcessor:
+    """動画処理を行うメインクラス"""
+    
+    def __init__(self, similarity_threshold: float = 0.3, exclude_edge_frames: bool = True):
+        """
+        初期化
+        
+        Args:
+            similarity_threshold: フレーム類似度の閾値
+            exclude_edge_frames: 最初と最後のフレームを除外するかどうか
+        """
+        self.similarity_threshold = similarity_threshold
+        self.exclude_edge_frames = exclude_edge_frames
+        
+    def extract_frames(self, video_path: str, num_frames: int = 20) -> Tuple[Optional[List], Optional[str]]:
+        """
+        動画からフレームを抽出する
+        
+        Args:
+            video_path: 動画ファイルのパス
+            num_frames: 抽出するフレーム数
+            
+        Returns:
+            Tuple[フレームリスト, エラーメッセージ]
+        """
+        try:
+            cap = cv2.VideoCapture(video_path)
+            if not cap.isOpened():
+                return None, f"動画ファイルを開けませんでした: {video_path}"
+            
+            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
+            if total_frames == 0:
+                return None, "動画にフレームが見つかりませんでした"
+            
+            logger.info(f"動画 {video_path}: 総フレーム数 {total_frames}")
+            
+            frames = []
+            # 最初と最後のフレームを含む等間隔でフレームを抽出
+            frame_indices = np.linspace(0, total_frames-1, num_frames, dtype=int)
+            
+            for frame_idx in frame_indices:
+                cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
+                ret, frame = cap.read()
+                if ret:
+                    # BGR to RGB変換
+                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
+                    frames.append((frame_idx, frame_rgb))
+            
+            cap.release()
+            logger.info(f"フレーム抽出完了: {len(frames)}フレーム")
+            return frames, None
+            
+        except Exception as e:
+            logger.error(f"フレーム抽出エラー: {e}")
+            return None, f"フレーム抽出エラー: {str(e)}"
+
+    def calculate_frame_similarity(self, frame1: np.ndarray, frame2: np.ndarray) -> float:
+        """
+        2つのフレーム間の類似度を計算する
+        
+        Args:
+            frame1: 比較フレーム1
+            frame2: 比較フレーム2
+            
+        Returns:
+            類似度スコア (0.0-1.0)
+        """
+        try:
+            # グレースケールに変換
+            gray1 = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
+            gray2 = cv2.cvtColor(frame2, cv2.COLOR_RGB2GRAY)
+            
+            # 同じサイズにリサイズ
+            h, w = min(gray1.shape[0], gray2.shape[0]), min(gray1.shape[1], gray2.shape[1])
+            gray1 = cv2.resize(gray1, (w, h))
+            gray2 = cv2.resize(gray2, (w, h))
+            
+            # SSIM（構造的類似性指標）を計算
+            similarity = ssim(gray1, gray2)
+            return max(0.0, similarity)  # 負の値を0にクリップ
+            
+        except Exception as e:
+            logger.error(f"類似度計算エラー: {e}")
+            return 0.0
+
+    def find_best_connection_frames(self, video1_path: str, video2_path: str) -> Tuple[Optional[np.ndarray], Optional[np.ndarray], float, Optional[str], Tuple[int, int]]:
+        """
+        2つの動画の最適な接続フレームを見つける
+        動画2の最初のフレームと動画1の全フレームから最も類似したフレームを探索
+        
+        Args:
+            video1_path: 動画1のパス
+            video2_path: 動画2のパス
+            
+        Returns:
+            Tuple[最適フレーム1, 最適フレーム2, 類似度, エラーメッセージ, フレームインデックス]
+        """
+        try:
+            # 各動画からフレームを抽出
+            frames1, error1 = self.extract_frames(video1_path, 30)  # より多くのフレームを抽出
+            if error1:
+                return None, None, 0.0, error1, (0, 0)
+            
+            frames2, error2 = self.extract_frames(video2_path, 10)  # 動画2は少なめでOK
+            if error2:
+                return None, None, 0.0, error2, (0, 0)
+            
+            # エッジフレーム除外オプションの適用
+            if self.exclude_edge_frames:
+                # 最初と最後のフレームを除外
+                frames1_filtered = frames1[1:-1] if len(frames1) > 2 else frames1
+                frames2_filtered = frames2[1:-1] if len(frames2) > 2 else frames2
+                logger.info(f"エッジフレーム除外: 動画1 {len(frames1)} → {len(frames1_filtered)}フレーム, 動画2 {len(frames2)} → {len(frames2_filtered)}フレーム")
+            else:
+                frames1_filtered = frames1
+                frames2_filtered = frames2
+                logger.info("エッジフレーム除外: 無効")
+            
+            # 動画2の最初の数フレームを基準にする（より高精度な探索）
+            video2_start_frames = frames2_filtered[:3]  # 動画2の最初の3フレーム（エッジ除外後）
+            
+            best_similarity = -1
+            best_frame1 = None
+            best_frame2 = None
+            best_indices = (0, 0)
+            
+            logger.info(f"フレーム類似度分析開始: 動画2の最初の{len(video2_start_frames)}フレームと動画1の{len(frames1_filtered)}フレームを比較...")
+            
+            # 動画2の各開始フレームについて、動画1の全フレームと比較
+            for j, (idx2, frame2) in enumerate(video2_start_frames):
+                logger.info(f"動画2のフレーム[{idx2}]との比較開始...")
+                
+                for i, (idx1, frame1) in enumerate(frames1_filtered):
+                    similarity = self.calculate_frame_similarity(frame1, frame2)
+                    logger.info(f"  動画1[{idx1}] vs 動画2[{idx2}]: 類似度 {similarity:.3f}")
+                    
+                    if similarity > best_similarity:
+                        best_similarity = similarity
+                        best_frame1 = frame1
+                        best_frame2 = frame2
+                        best_indices = (idx1, idx2)
+                        logger.info(f"  🌟 新しい最高類似度: {similarity:.3f} (動画1[{idx1}] → 動画2[{idx2}])")
+            
+            logger.info(f"最適接続点検出完了: 類似度 {best_similarity:.3f}")
+            logger.info(f"最適結合点: 動画1のフレーム[{best_indices[0]}] → 動画2のフレーム[{best_indices[1]}]")
+            
+            return best_frame1, best_frame2, best_similarity, None, best_indices
+            
+        except Exception as e:
+            logger.error(f"フレーム比較エラー: {e}")
+            return None, None, 0.0, f"フレーム比較エラー: {str(e)}", (0, 0)
+
+    def create_merged_video(self, video1_path: str, video2_path: str, cut_frame1: int, cut_frame2: int, output_path: str) -> Tuple[bool, Optional[str]]:
+        """
+        2つの動画を指定されたフレームで結合する
+        
+        Args:
+            video1_path: 動画1のパス
+            video2_path: 動画2のパス
+            cut_frame1: 動画1のカットフレーム
+            cut_frame2: 動画2のカットフレーム
+            output_path: 出力パス
+            
+        Returns:
+            Tuple[成功フラグ, エラーメッセージ]
+        """
+        try:
+            # 動画1を読み込み
+            cap1 = cv2.VideoCapture(video1_path)
+            if not cap1.isOpened():
+                return False, "動画1を開けませんでした"
+            
+            # 動画2を読み込み
+            cap2 = cv2.VideoCapture(video2_path)
+            if not cap2.isOpened():
+                cap1.release()
+                return False, "動画2を開けませんでした"
+            
+            # 動画の情報を取得
+            fps1 = cap1.get(cv2.CAP_PROP_FPS)
+            width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
+            height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
+            
+            logger.info(f"動画1情報: {width1}x{height1}, {fps1}fps")
+            
+            # 出力動画の設定（最初の動画の設定を使用）
+            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
+            out = cv2.VideoWriter(output_path, fourcc, fps1, (width1, height1))
+            
+            # 動画1の最初からcut_frame1まで
+            frame_count = 0
+            while frame_count <= cut_frame1:
+                ret, frame = cap1.read()
+                if not ret:
+                    break
+                out.write(frame)
+                frame_count += 1
+            
+            logger.info(f"動画1から {frame_count} フレームを結合")
+            
+            # 動画2のcut_frame2から最後まで
+            cap2.set(cv2.CAP_PROP_POS_FRAMES, cut_frame2)
+            frame_count2 = 0
+            while True:
+                ret, frame = cap2.read()
+                if not ret:
+                    break
+                # サイズを動画1に合わせる
+                if frame.shape[:2] != (height1, width1):
+                    frame = cv2.resize(frame, (width1, height1))
+                out.write(frame)
+                frame_count2 += 1
+            
+            logger.info(f"動画2から {frame_count2} フレームを結合")
+            
+            # リソースを解放
+            cap1.release()
+            cap2.release()
+            out.release()
+            
+            logger.info(f"動画結合完了: {output_path}")
+            return True, None
+            
+        except Exception as e:
+            logger.error(f"動画結合エラー: {e}")
+            return False, f"動画結合エラー: {str(e)}"
+
+    def save_frame_as_image(self, frame: np.ndarray, filename: str) -> Optional[str]:
+        """
+        フレームを画像として保存する
+        
+        Args:
+            frame: 保存するフレーム
+            filename: ファイル名
+            
+        Returns:
+            保存されたファイルのパス
+        """
+        try:
+            temp_dir = tempfile.gettempdir()
+            file_path = os.path.join(temp_dir, filename)
+            
+            # PIL Imageに変換して保存
+            pil_image = Image.fromarray(frame)
+            pil_image.save(file_path)
+            
+            logger.info(f"フレーム画像保存: {file_path}")
+            return file_path
+            
+        except Exception as e:
+            logger.error(f"画像保存エラー: {e}")
+            return None
+
+    def analyze_video_details(self, video_path: str) -> str:
+        """
+        動画の詳細情報を分析する
+        
+        Args:
+            video_path: 動画ファイルのパス
+            
+        Returns:
+            動画情報の文字列
+        """
+        try:
+            cap = cv2.VideoCapture(video_path)
+            if not cap.isOpened():
+                return "動画を開けませんでした"
+            
+            fps = cap.get(cv2.CAP_PROP_FPS)
+            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
+            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
+            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
+            duration = frame_count / fps if fps > 0 else 0
+            
+            cap.release()
+            
+            return f"""📹 動画情報:
+• 解像度: {width} x {height}
+• フレームレート: {fps:.2f} FPS
+• 総フレーム数: {frame_count}
+• 再生時間: {duration:.2f} 秒
+• ファイルサイズ: {os.path.getsize(video_path) / (1024*1024):.1f} MB"""
+            
+        except Exception as e:
+            logger.error(f"動画分析エラー: {e}")
+            return f"動画分析エラー: {str(e)}"
+
+
+class FrameBridge:
+    """Frame Bridge メインクラス"""
+    
+    def __init__(self, exclude_edge_frames: bool = True):
+        """
+        初期化
+        
+        Args:
+            exclude_edge_frames: 最初と最後のフレームを除外するかどうか
+        """
+        self.processor = VideoProcessor(exclude_edge_frames=exclude_edge_frames)
+    
+    def process_video_bridge(self, video1_path: str, video2_path: str) -> Tuple[str, Optional[str], Optional[str], Optional[str], float]:
+        """
+        2つの動画を分析して最適な結合点を見つけ、結合する
+        
+        Args:
+            video1_path: 動画1のパス
+            video2_path: 動画2のパス
+            
+        Returns:
+            Tuple[結果テキスト, 結合動画パス, フレーム1パス, フレーム2パス, 類似度]
+        """
+        if not video1_path or not video2_path:
+            return "2つの動画ファイルが必要です。", None, None, None, 0.0
+        
+        if not os.path.exists(video1_path) or not os.path.exists(video2_path):
+            return "指定された動画ファイルが見つかりません。", None, None, None, 0.0
+        
+        try:
+            logger.info("動画分析開始...")
+            
+            # 最適な接続フレームを見つける
+            frame1, frame2, similarity, error, indices = self.processor.find_best_connection_frames(video1_path, video2_path)
+            
+            if error:
+                return f"エラー: {error}", None, None, None, 0.0
+            
+            logger.info("最適な接続点を検出しました")
+            
+            # フレームを画像として保存
+            frame1_path = self.processor.save_frame_as_image(frame1, "connection_frame1.png")
+            frame2_path = self.processor.save_frame_as_image(frame2, "connection_frame2.png")
+            
+            logger.info("動画結合開始...")
+            
+            # 結合動画を作成
+            temp_dir = tempfile.gettempdir()
+            output_path = os.path.join(temp_dir, "merged_video.mp4")
+            
+            # 最適なフレームで結合
+            success, merge_error = self.processor.create_merged_video(
+                video1_path, video2_path, indices[0], indices[1], output_path
+            )
+            
+            if not success:
+                return f"動画結合エラー: {merge_error}", None, None, None, similarity
+            
+            # 品質評価
+            quality = self._evaluate_quality(similarity)
+            
+            result_text = f"""🎬 動画結合完了！
+
+📊 分析結果:
+• フレーム類似度: {similarity:.3f}
+• 接続品質: {quality}
+• 結合フレーム: 動画1[{indices[0]}] → 動画2[{indices[1]}]
+
+💡 結合情報:
+• 動画1の最適な終了フレームを検出
+• 動画2の最適な開始フレームを検出
+• スムーズな接続を実現
+
+📁 出力ファイル: {os.path.basename(output_path)}"""
+            
+            logger.info("処理完了")
+            return result_text, output_path, frame1_path, frame2_path, similarity
+            
+        except Exception as e:
+            logger.error(f"処理エラー: {e}")
+            return f"処理エラー: {str(e)}", None, None, None, 0.0
+    
+    def _evaluate_quality(self, similarity: float) -> str:
+        """類似度から品質を評価"""
+        if similarity > 0.8:
+            return "優秀 🌟"
+        elif similarity > 0.6:
+            return "良好 ✅"
+        elif similarity > 0.4:
+            return "普通 ⚡"
+        else:
+            return "要確認 ⚠️"
\ No newline at end of file
diff --git a/tests/batch_test.py b/tests/batch_test.py
new file mode 100644
index 0000000..b81b58b
--- /dev/null
+++ b/tests/batch_test.py
@@ -0,0 +1,96 @@
+"""
+Frame Bridge - バッチ処理テスト用スクリプト
+フォルダ内の動画ファイルを順次結合するテストスクリプト
+"""
+
+import os
+import sys
+import argparse
+from pathlib import Path
+import sys
+sys.path.append('..')
+from src.frame_bridge import BatchProcessor
+
+def main():
+    """メイン処理"""
+    parser = argparse.ArgumentParser(description="Frame Bridge - バッチ動画結合")
+    parser.add_argument("--input", "-i", default="examples/assets/example/REI/input", help="入力フォルダ (デフォルト: examples/assets/example/REI/input)")
+    parser.add_argument("--output", "-o", default="examples/assets/example/REI/output", help="出力フォルダ (デフォルト: examples/assets/example/REI/output)")
+    parser.add_argument("--exclude-edge", action="store_true", default=True, help="最初と最後のフレームを除外 (デフォルト: True)")
+    parser.add_argument("--include-edge", action="store_true", help="最初と最後のフレームを含める")
+    parser.add_argument("--mode", "-m", choices=["sequential", "pairwise"], default="sequential", 
+                       help="結合モード: sequential(順次結合) または pairwise(ペア結合)")
+    parser.add_argument("--filename", "-f", default="merged_sequence.mp4", help="出力ファイル名 (sequentialモードのみ)")
+    
+    args = parser.parse_args()
+    
+    print("🎬 Frame Bridge - バッチ処理テスト")
+    print("=" * 60)
+    print(f"📁 入力フォルダ: {args.input}")
+    print(f"📁 出力フォルダ: {args.output}")
+    print(f"🔄 処理モード: {args.mode}")
+    if args.mode == "sequential":
+        print(f"📄 出力ファイル名: {args.filename}")
+    print()
+    
+    # 入力フォルダの存在チェック
+    if not os.path.exists(args.input):
+        print(f"❌ 入力フォルダが見つかりません: {args.input}")
+        return
+    
+    # エッジフレーム除外設定
+    exclude_edge_frames = not args.include_edge if args.include_edge else args.exclude_edge
+    
+    print(f"🎯 エッジフレーム除外: {'有効' if exclude_edge_frames else '無効'}")
+    print()
+    
+    # バッチプロセッサを初期化
+    processor = BatchProcessor(output_dir=args.output, exclude_edge_frames=exclude_edge_frames)
+    
+    # 動画ファイルの確認
+    video_files = processor.get_video_files(args.input)
+    if len(video_files) < 2:
+        print("❌ 結合には最低2つの動画ファイルが必要です")
+        return
+    
+    print(f"✅ 検出された動画ファイル: {len(video_files)}個")
+    for i, file in enumerate(video_files):
+        print(f"  {i+1}. {os.path.basename(file)}")
+    print()
+    
+    # 処理モードに応じて実行
+    if args.mode == "sequential":
+        print("🔄 順次結合処理を開始...")
+        success, final_output, results = processor.process_sequential_merge(args.input, args.filename)
+        
+        if success:
+            print(f"✅ 順次結合完了!")
+            print(f"📁 最終出力: {final_output}")
+            print(f"📊 ファイルサイズ: {os.path.getsize(final_output) / (1024*1024):.1f} MB")
+        else:
+            print("❌ 順次結合に失敗しました")
+    
+    elif args.mode == "pairwise":
+        print("🔄 ペアワイズ結合処理を開始...")
+        success, output_files, results = processor.process_pairwise_merge(args.input)
+        
+        if success:
+            print(f"✅ ペアワイズ結合完了!")
+            print(f"📁 出力ファイル数: {len(output_files)}")
+            for i, file in enumerate(output_files):
+                size_mb = os.path.getsize(file) / (1024*1024)
+                print(f"  {i+1}. {os.path.basename(file)} ({size_mb:.1f} MB)")
+        else:
+            print("❌ ペアワイズ結合に失敗しました")
+    
+    # レポート生成
+    print("\n" + "=" * 60)
+    print("📋 処理レポート:")
+    report_path = Path(args.output) / "batch_report.txt"
+    report = processor.generate_report(results, str(report_path))
+    print(report)
+    
+    print("🎉 バッチ処理完了！")
+
+if __name__ == "__main__":
+    main()
\ No newline at end of file
diff --git a/tests/test_sample.py b/tests/test_sample.py
new file mode 100644
index 0000000..d8a51d9
--- /dev/null
+++ b/tests/test_sample.py
@@ -0,0 +1,72 @@
+"""
+Frame Bridge - サンプル動画テスト用スクリプト
+指定されたサンプル動画でFrame Bridgeの機能をテストします
+"""
+
+import os
+import sys
+import sys
+sys.path.append('..')
+from src.frame_bridge import FrameBridge
+
+def main():
+    """メイン処理"""
+    print("🎬 Frame Bridge - サンプル動画テスト")
+    print("=" * 50)
+    
+    # サンプル動画のパス
+    video1_path = "examples/assets/example/REI/input/REI-001.mp4"
+    video2_path = "examples/assets/example/REI/input/REI-002.mp4"
+    
+    # ファイル存在チェック
+    if not os.path.exists(video1_path):
+        print(f"❌ 動画1が見つかりません: {video1_path}")
+        return
+    
+    if not os.path.exists(video2_path):
+        print(f"❌ 動画2が見つかりません: {video2_path}")
+        return
+    
+    print(f"✅ 動画1: {video1_path}")
+    print(f"✅ 動画2: {video2_path}")
+    print()
+    
+    # Frame Bridge インスタンスを作成（エッジフレーム除外有効）
+    frame_bridge = FrameBridge(exclude_edge_frames=True)
+    print(f"🎯 エッジフレーム除外: 有効")
+    
+    # 動画情報を表示
+    print("📊 動画1の詳細情報:")
+    print(frame_bridge.processor.analyze_video_details(video1_path))
+    print()
+    
+    print("📊 動画2の詳細情報:")
+    print(frame_bridge.processor.analyze_video_details(video2_path))
+    print()
+    
+    # フレーム結合処理を実行
+    print("🔄 フレーム結合処理を開始...")
+    result_text, output_path, frame1_path, frame2_path, similarity = frame_bridge.process_video_bridge(
+        video1_path, video2_path
+    )
+    
+    print("\n" + "=" * 50)
+    print("📋 処理結果:")
+    print(result_text)
+    
+    if output_path and os.path.exists(output_path):
+        print(f"\n✅ 結合動画が作成されました: {output_path}")
+        print(f"📁 ファイルサイズ: {os.path.getsize(output_path) / (1024*1024):.1f} MB")
+    
+    if frame1_path and os.path.exists(frame1_path):
+        print(f"🖼️ 接続フレーム1: {frame1_path}")
+    
+    if frame2_path and os.path.exists(frame2_path):
+        print(f"🖼️ 接続フレーム2: {frame2_path}")
+    
+    print(f"\n📈 最終類似度スコア: {similarity:.3f}")
+    
+    print("\n🎉 テスト完了！")
+
+if __name__ == "__main__":
+    main()
\ No newline at end of file
```
