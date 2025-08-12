# 🔄 Latest Code Changes

```diff
diff --git a/README.md b/README.md
index ae3c9b7..64851e5 100644
--- a/README.md
+++ b/README.md
@@ -1,3 +1,14 @@
+---
+license: mit
+title: wikipedia to markdown
+sdk: gradio
+emoji: 📈
+colorFrom: green
+colorTo: indigo
+thumbnail: >-
+  https://cdn-uploads.huggingface.co/production/uploads/64e0ef4a4c78e1eba5178d7a/vJQZ24fctExV3dax_BGU-.jpeg
+sdk_version: 5.42.0
+---
 <div align="center">
 
 ![](https://github.com/user-attachments/assets/201c0b39-6bf7-4599-a62a-dd3e6f61e5f8)
@@ -221,4 +232,4 @@ def create_zen_theme():
 
 ---
 
-© 2025 Wikipedia to Markdown Converter
+© 2025 Wikipedia to Markdown Converter
\ No newline at end of file
diff --git a/app.py b/app.py
index ebcd4d9..47f32ac 100644
--- a/app.py
+++ b/app.py
@@ -4,6 +4,9 @@ import html2text
 import re
 import gradio as gr
 from theme import create_zen_theme
+import tempfile
+import os
+from urllib.parse import urlparse, unquote
 
 def scrape_wikipedia_to_markdown_final(url: str) -> str:
     """
@@ -71,36 +74,73 @@ def scrape_wikipedia_to_markdown_final(url: str) -> str:
     except Exception as e:
         return f"予期せぬエラーが発生しました: {e}"
 
+def get_filename_from_url(url):
+    """URLからファイル名を生成する関数"""
+    try:
+        # URLからページ名を抽出
+        parsed_url = urlparse(url)
+        page_name = parsed_url.path.split('/')[-1]
+        # URLデコード
+        page_name = unquote(page_name)
+        # ファイル名として使用できない文字を置換
+        safe_filename = re.sub(r'[<>:"/\\|?*]', '_', page_name)
+        return f"{safe_filename}.md"
+    except:
+        return "wikipedia_page.md"
+
+def create_download_file(content, filename):
+    """ダウンロード用の一時ファイルを作成する関数"""
+    try:
+        # 一時ディレクトリにファイルを作成
+        temp_dir = tempfile.gettempdir()
+        file_path = os.path.join(temp_dir, filename)
+        
+        with open(file_path, 'w', encoding='utf-8') as f:
+            f.write(content)
+        
+        return file_path
+    except Exception as e:
+        print(f"ファイル作成エラー: {e}")
+        return None
+
 def process_wikipedia_url(url):
     """Wikipedia URLを処理してMarkdownを生成するGradio用関数"""
     if not url:
-        return "URLを入力してください。"
+        return "URLを入力してください。", None
     
     # URLが有効かチェック
     if not url.startswith('http'):
-        return "有効なURLを入力してください（http://またはhttps://から始まるURL）。"
+        return "有効なURLを入力してください（http://またはhttps://から始まるURL）。", None
     
     # Wikipedia URLかチェック
     if 'wikipedia.org' not in url:
-        return "WikipediaのURLを入力してください。"
+        return "WikipediaのURLを入力してください。", None
     
     # スクレイピングを実行
     markdown_content = scrape_wikipedia_to_markdown_final(url)
     
-    return markdown_content
+    # ダウンロード用ファイルを作成
+    if not markdown_content.startswith("エラー:") and not markdown_content.startswith("HTTP"):
+        filename = get_filename_from_url(url)
+        file_path = create_download_file(markdown_content, filename)
+        return markdown_content, file_path
+    else:
+        return markdown_content, None
 
 def process_multiple_urls(urls_text, progress=gr.Progress()):
     """複数のWikipedia URLを一括処理してMarkdownを生成する関数"""
     if not urls_text.strip():
-        return "URLリストを入力してください。"
+        return "URLリストを入力してください。", None, []
     
     # URLリストを行ごとに分割
     urls = [url.strip() for url in urls_text.strip().split('\n') if url.strip()]
     
     if not urls:
-        return "有効なURLが見つかりませんでした。"
+        return "有効なURLが見つかりませんでした。", None, []
     
     results = []
+    all_content = []
+    individual_files = []
     total_urls = len(urls)
     
     for i, url in enumerate(urls):
@@ -122,12 +162,26 @@ def process_multiple_urls(urls_text, progress=gr.Progress()):
                 results.append(f"❌ 処理失敗: {url}\n{markdown_content}")
             else:
                 results.append(f"✅ 処理成功: {url}\n\n{markdown_content}")
+                all_content.append(markdown_content)
+                
+                # 個別ファイルを作成
+                filename = get_filename_from_url(url)
+                file_path = create_download_file(markdown_content, filename)
+                if file_path:
+                    individual_files.append(file_path)
         except Exception as e:
             results.append(f"❌ 処理エラー: {url}\nエラー内容: {str(e)}")
     
     # 結果を結合
     final_result = "\n\n" + "="*80 + "\n\n".join(results)
-    return final_result
+    
+    # 一括ダウンロード用ファイルを作成
+    batch_file_path = None
+    if all_content:
+        combined_content = "\n\n" + "="*80 + "\n\n".join(all_content)
+        batch_file_path = create_download_file(combined_content, "wikipedia_batch_export.md")
+    
+    return final_result, batch_file_path, individual_files
 
 # Gradioインターフェースの作成
 def create_interface():
@@ -163,15 +217,30 @@ def create_interface():
                             max_lines=50,
                             show_copy_button=True
                         )
+                        download_file = gr.File(
+                            label="📥 マークダウンファイルをダウンロード",
+                            visible=False
+                        )
                 
                 # ボタンクリック時の処理
+                def update_single_output(url):
+                    content, file_path = process_wikipedia_url(url)
+                    if file_path:
+                        return content, gr.update(value=file_path, visible=True)
+                    else:
+                        return content, gr.update(visible=False)
+                
                 convert_btn.click(
-                    fn=process_wikipedia_url,
+                    fn=update_single_output,
                     inputs=url_input,
-                    outputs=output_text
+                    outputs=[output_text, download_file]
                 )
                 
                 # 使用例
+                def example_process(url):
+                    content, _ = process_wikipedia_url(url)
+                    return content
+                
                 gr.Examples(
                     examples=[
                         ["https://ja.wikipedia.org/wiki/Python"],
@@ -180,7 +249,7 @@ def create_interface():
                     ],
                     inputs=url_input,
                     outputs=output_text,
-                    fn=process_wikipedia_url,
+                    fn=example_process,
                     cache_examples=False
                 )
             
@@ -199,16 +268,67 @@ def create_interface():
                     with gr.Column(scale=1):
                         batch_output_text = gr.Textbox(
                             label="📝 一括変換結果",
-                            lines=20,
-                            max_lines=50,
+                            lines=15,
+                            max_lines=30,
                             show_copy_button=True
                         )
+                        batch_download_file = gr.File(
+                            label="📥 全体をまとめてダウンロード",
+                            visible=False
+                        )
+                        
+                        # 個別ダウンロードエリア
+                        individual_downloads = gr.Column(visible=False)
+                        with individual_downloads:
+                            gr.Markdown("### 📥 個別ダウンロード")
+                            individual_file_1 = gr.File(label="", visible=False)
+                            individual_file_2 = gr.File(label="", visible=False)
+                            individual_file_3 = gr.File(label="", visible=False)
+                            individual_file_4 = gr.File(label="", visible=False)
+                            individual_file_5 = gr.File(label="", visible=False)
                 
                 # 一括処理ボタンクリック時の処理
+                def update_batch_output(urls_text):
+                    content, batch_file_path, individual_files = process_multiple_urls(urls_text)
+                    
+                    # 戻り値のリストを準備
+                    outputs = [content]
+                    
+                    # 一括ダウンロードファイル
+                    if batch_file_path:
+                        outputs.append(gr.update(value=batch_file_path, visible=True))
+                    else:
+                        outputs.append(gr.update(visible=False))
+                    
+                    # 個別ダウンロードエリアの表示/非表示
+                    if individual_files:
+                        outputs.append(gr.update(visible=True))
+                    else:
+                        outputs.append(gr.update(visible=False))
+                    
+                    # 個別ファイル（最大5つまで表示）
+                    for i in range(5):
+                        if i < len(individual_files):
+                            filename = os.path.basename(individual_files[i])
+                            outputs.append(gr.update(value=individual_files[i], visible=True, label=f"📄 {filename}"))
+                        else:
+                            outputs.append(gr.update(visible=False))
+                    
+                    return outputs
+                
                 batch_convert_btn.click(
-                    fn=process_multiple_urls,
+                    fn=update_batch_output,
                     inputs=urls_input,
-                    outputs=batch_output_text
+                    outputs=[
+                        batch_output_text, 
+                        batch_download_file, 
+                        individual_downloads,
+                        individual_file_1,
+                        individual_file_2,
+                        individual_file_3,
+                        individual_file_4,
+                        individual_file_5
+                    ]
                 )
                 
                 gr.Markdown("### 💡 一括処理の使い方")
@@ -222,6 +342,10 @@ def create_interface():
         gr.Markdown("- **単体処理**: 1つのWikipediaページを変換したい場合")
         gr.Markdown("- **一括処理**: 複数のWikipediaページを一度に変換したい場合")
         gr.Markdown("- 生成されたMarkdownは右側のテキストエリアからコピーできます")
+        gr.Markdown("- **📥 ダウンロード機能**: 変換が成功すると、マークダウンファイルとして直接ダウンロードできます")
+        gr.Markdown("  - 単体処理: ページ名に基づいたファイル名で個別ダウンロード")
+        gr.Markdown("  - 一括処理: 各URLごとの個別ダウンロード + 全体をまとめた一括ダウンロード")
+        gr.Markdown("  - 個別ダウンロード: 成功した各ページを個別のファイルとしてダウンロード可能（最大5つまで表示）")
         
         # ZENテーマの説明
         gr.HTML("""
@@ -240,7 +364,7 @@ if __name__ == "__main__":
     # アプリケーションを実行
     demo.launch(
         server_name="0.0.0.0",
-        server_port=7861,
+        server_port=7860,
         share=False,
         debug=True
     )
diff --git a/docker-compose.dev.yml b/docker-compose.dev.yml
index 19669ff..6e6047b 100644
--- a/docker-compose.dev.yml
+++ b/docker-compose.dev.yml
@@ -5,9 +5,8 @@ services:
     build:
       context: .
       dockerfile: Dockerfile
-    container_name: wikipedia-to-markdown-dev
     ports:
-      - "7861:7861"
+      - "7861:7860"
     environment:
       - PYTHONUNBUFFERED=1
       - GRADIO_SERVER_NAME=0.0.0.0
diff --git a/docker-compose.yml b/docker-compose.yml
index 349a04c..212066c 100644
--- a/docker-compose.yml
+++ b/docker-compose.yml
@@ -5,9 +5,8 @@ services:
     build:
       context: .
       dockerfile: Dockerfile
-    container_name: wikipedia-to-markdown
     ports:
-      - "7861:7861"
+      - "7861:7860"
     environment:
       - PYTHONUNBUFFERED=1
     # volumes:
diff --git a/theme.py b/theme.py
index 64ecd56..d0bc5f1 100644
--- a/theme.py
+++ b/theme.py
@@ -36,8 +36,9 @@ def create_zen_theme():
         input_border_color="#d4c4a8",
         input_border_color_focus="#d4a574",
         block_background_fill="#ffffff",
-        block_border_color="#f5f2ed",
+        block_border_color="#e8e2d5",
+        block_border_width="3px",
         panel_background_fill="#ffffff",
-        panel_border_color="#f5f2ed",
+        panel_border_color="#e8e2d5",
         slider_color="#d4a574",
     )
\ No newline at end of file
```
