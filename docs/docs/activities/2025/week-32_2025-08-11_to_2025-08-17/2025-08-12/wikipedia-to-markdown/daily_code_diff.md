# 💻 Daily Code Changes

## Full Diff

```diff
diff --git a/.dockerignore b/.dockerignore
new file mode 100644
index 0000000..c5ba6c0
--- /dev/null
+++ b/.dockerignore
@@ -0,0 +1,56 @@
+# Git関連
+.git
+.gitignore
+
+# Python関連
+__pycache__/
+*.py[cod]
+*$py.class
+*.so
+.Python
+build/
+develop-eggs/
+dist/
+downloads/
+eggs/
+.eggs/
+lib/
+lib64/
+parts/
+sdist/
+var/
+wheels/
+*.egg-info/
+.installed.cfg
+*.egg
+
+# 仮想環境
+venv/
+env/
+ENV/
+
+# IDE関連
+.vscode/
+.idea/
+*.swp
+*.swo
+
+# OS関連
+.DS_Store
+Thumbs.db
+
+# ログファイル
+*.log
+
+# 一時ファイル
+*.tmp
+*.temp
+
+# Docker関連
+Dockerfile*
+docker-compose*
+.dockerignore
+
+# ドキュメント
+README.md
+LICENSE
\ No newline at end of file
diff --git a/.github/workflows/sync-to-hf.yml b/.github/workflows/sync-to-hf.yml
new file mode 100644
index 0000000..5879e47
--- /dev/null
+++ b/.github/workflows/sync-to-hf.yml
@@ -0,0 +1,32 @@
+name: Sync to Hugging Face
+
+on:
+  push:
+    branches:
+      - main
+      - master
+  workflow_dispatch:
+
+jobs:
+  sync-to-hf:
+    runs-on: ubuntu-latest
+    steps:
+      - name: Checkout repository
+        uses: actions/checkout@v4
+        with:
+          fetch-depth: 0
+          lfs: true
+
+      - name: Push to Hugging Face Hub
+        env:
+          HF_TOKEN: ${{ secrets.HF_TOKEN }}
+        run: |
+          # Git設定
+          git config --global user.email "action@github.com"
+          git config --global user.name "GitHub Action"
+          
+          # Hugging Face Hubにリモートを追加
+          git remote add hf https://huggingface.co/spaces/MakiAi/wikipedia-to-markdown
+          
+          # 強制プッシュでHugging Faceに同期
+          git push --force https://user:$HF_TOKEN@huggingface.co/spaces/MakiAi/wikipedia-to-markdown HEAD:main
diff --git a/Dockerfile b/Dockerfile
new file mode 100644
index 0000000..9021fbf
--- /dev/null
+++ b/Dockerfile
@@ -0,0 +1,28 @@
+# Python 3.11をベースイメージとして使用
+FROM python:3.11-slim
+
+# 作業ディレクトリを設定
+WORKDIR /app
+
+# システムパッケージの更新とクリーンアップ
+RUN apt-get update && apt-get install -y \
+    && rm -rf /var/lib/apt/lists/*
+
+# 依存関係ファイルをコピー
+COPY requirements.txt .
+
+# Python依存関係をインストール
+RUN pip install --no-cache-dir -r requirements.txt
+
+# アプリケーションファイルをコピー
+COPY . .
+
+# ポート7861を公開
+EXPOSE 7861
+
+# 非rootユーザーを作成してセキュリティを向上
+RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
+USER appuser
+
+# アプリケーションを起動
+CMD ["python", "app.py"]
\ No newline at end of file
diff --git a/README.md b/README.md
index 1a1aeff..64851e5 100644
--- a/README.md
+++ b/README.md
@@ -1,11 +1,25 @@
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
 
+![](https://github.com/user-attachments/assets/201c0b39-6bf7-4599-a62a-dd3e6f61e5f8)
+
 # 📚 Wikipedia to Markdown Converter
 
-<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
-<img src="https://img.shields.io/badge/Gradio-4.44.0?style=for-the-badge&logo=gradio&logoColor=white" alt="Gradio" />
-<img src="https://img.shields.io/badge/BeautifulSoup-4.12.2?style=for-the-badge&logo=beautifulsoup&logoColor=white" alt="BeautifulSoup" />
-<img src="https://img.shields.io/badge/html2text-2020.1.16?style=for-the-badge&logo=html&logoColor=white" alt="html2text" />
+![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
+![Gradio](https://img.shields.io/badge/Gradio-FF6B6B?style=for-the-badge&logo=gradio&logoColor=white)
+![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4CAF50?style=for-the-badge&logo=python&logoColor=white)
+![html2text](https://img.shields.io/badge/html2text-2196F3?style=for-the-badge&logo=html5&logoColor=white)
+
 
 </div>
 
@@ -218,4 +232,4 @@ def create_zen_theme():
 
 ---
 
-© 2025 Wikipedia to Markdown Converter
+© 2025 Wikipedia to Markdown Converter
\ No newline at end of file
diff --git a/app.py b/app.py
index 8cd6fcd..47f32ac 100644
--- a/app.py
+++ b/app.py
@@ -3,45 +3,10 @@ from bs4 import BeautifulSoup
 import html2text
 import re
 import gradio as gr
-
-# ZENテーマの作成
-def create_zen_theme():
-    return gr.Theme(
-        primary_hue="amber",
-        secondary_hue="stone",
-        neutral_hue="slate",
-        text_size="md",
-        spacing_size="lg",
-        radius_size="sm",
-        font=[
-            "Hiragino Sans",
-            "Noto Sans JP",
-            "Yu Gothic",
-            "system-ui",
-            "sans-serif"
-        ],
-        font_mono=[
-            "SF Mono",
-            "Monaco",
-            "monospace"
-        ]
-    ).set(
-        body_background_fill="#ffffff",
-        body_text_color="#3d405b",
-        button_primary_background_fill="#d4a574",
-        button_primary_background_fill_hover="#c19660",
-        button_primary_text_color="#ffffff",
-        button_secondary_background_fill="#f5f2ed",
-        button_secondary_text_color="#3d405b",
-        input_background_fill="#ffffff",
-        input_border_color="#d4c4a8",
-        input_border_color_focus="#d4a574",
-        block_background_fill="#ffffff",
-        block_border_color="#f5f2ed",
-        panel_background_fill="#ffffff",
-        panel_border_color="#f5f2ed",
-        slider_color="#d4a574",
-    )
+from theme import create_zen_theme
+import tempfile
+import os
+from urllib.parse import urlparse, unquote
 
 def scrape_wikipedia_to_markdown_final(url: str) -> str:
     """
@@ -109,23 +74,114 @@ def scrape_wikipedia_to_markdown_final(url: str) -> str:
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
+
+def process_multiple_urls(urls_text, progress=gr.Progress()):
+    """複数のWikipedia URLを一括処理してMarkdownを生成する関数"""
+    if not urls_text.strip():
+        return "URLリストを入力してください。", None, []
+    
+    # URLリストを行ごとに分割
+    urls = [url.strip() for url in urls_text.strip().split('\n') if url.strip()]
+    
+    if not urls:
+        return "有効なURLが見つかりませんでした。", None, []
+    
+    results = []
+    all_content = []
+    individual_files = []
+    total_urls = len(urls)
+    
+    for i, url in enumerate(urls):
+        progress((i + 1) / total_urls, f"処理中: {i + 1}/{total_urls}")
+        
+        # URLの検証
+        if not url.startswith('http'):
+            results.append(f"❌ 無効なURL: {url}")
+            continue
+            
+        if 'wikipedia.org' not in url:
+            results.append(f"❌ Wikipedia以外のURL: {url}")
+            continue
+        
+        # スクレイピング実行
+        try:
+            markdown_content = scrape_wikipedia_to_markdown_final(url)
+            if markdown_content.startswith("エラー:") or markdown_content.startswith("HTTP"):
+                results.append(f"❌ 処理失敗: {url}\n{markdown_content}")
+            else:
+                results.append(f"✅ 処理成功: {url}\n\n{markdown_content}")
+                all_content.append(markdown_content)
+                
+                # 個別ファイルを作成
+                filename = get_filename_from_url(url)
+                file_path = create_download_file(markdown_content, filename)
+                if file_path:
+                    individual_files.append(file_path)
+        except Exception as e:
+            results.append(f"❌ 処理エラー: {url}\nエラー内容: {str(e)}")
+    
+    # 結果を結合
+    final_result = "\n\n" + "="*80 + "\n\n".join(results)
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
@@ -141,48 +197,155 @@ def create_interface():
         </div>
         """)
         
-        with gr.Row():
-            with gr.Column(scale=1):
-                url_input = gr.Textbox(
-                    label="🔗 Wikipedia URL",
-                    placeholder="https://ja.wikipedia.org/wiki/...",
-                    value="https://ja.wikipedia.org/wiki/Python"
+        # タブの作成
+        with gr.Tabs():
+            # 単体処理タブ
+            with gr.TabItem("🔗 単体処理"):
+                with gr.Row():
+                    with gr.Column(scale=1):
+                        url_input = gr.Textbox(
+                            label="🔗 Wikipedia URL",
+                            placeholder="https://ja.wikipedia.org/wiki/...",
+                            value="https://ja.wikipedia.org/wiki/Python"
+                        )
+                        convert_btn = gr.Button("✨ 変換する", variant="primary")
+                    
+                    with gr.Column(scale=1):
+                        output_text = gr.Textbox(
+                            label="📝 変換されたMarkdown",
+                            lines=20,
+                            max_lines=50,
+                            show_copy_button=True
+                        )
+                        download_file = gr.File(
+                            label="📥 マークダウンファイルをダウンロード",
+                            visible=False
+                        )
+                
+                # ボタンクリック時の処理
+                def update_single_output(url):
+                    content, file_path = process_wikipedia_url(url)
+                    if file_path:
+                        return content, gr.update(value=file_path, visible=True)
+                    else:
+                        return content, gr.update(visible=False)
+                
+                convert_btn.click(
+                    fn=update_single_output,
+                    inputs=url_input,
+                    outputs=[output_text, download_file]
+                )
+                
+                # 使用例
+                def example_process(url):
+                    content, _ = process_wikipedia_url(url)
+                    return content
+                
+                gr.Examples(
+                    examples=[
+                        ["https://ja.wikipedia.org/wiki/Python"],
+                        ["https://ja.wikipedia.org/wiki/JavaScript"],
+                        ["https://ja.wikipedia.org/wiki/HTML"]
+                    ],
+                    inputs=url_input,
+                    outputs=output_text,
+                    fn=example_process,
+                    cache_examples=False
                 )
-                convert_btn = gr.Button("✨ 変換する", variant="primary")
             
-            with gr.Column(scale=1):
-                output_text = gr.Textbox(
-                    label="📝 変換されたMarkdown",
-                    lines=20,
-                    max_lines=50,
-                    show_copy_button=True
+            # 一括処理タブ
+            with gr.TabItem("📋 一括処理"):
+                with gr.Row():
+                    with gr.Column(scale=1):
+                        urls_input = gr.Textbox(
+                            label="📋 Wikipedia URLリスト（1行に1つずつ）",
+                            placeholder="https://ja.wikipedia.org/wiki/Python\nhttps://ja.wikipedia.org/wiki/JavaScript\nhttps://ja.wikipedia.org/wiki/HTML",
+                            lines=10,
+                            value="https://ja.wikipedia.org/wiki/Python\nhttps://ja.wikipedia.org/wiki/JavaScript"
+                        )
+                        batch_convert_btn = gr.Button("🚀 一括変換する", variant="primary")
+                    
+                    with gr.Column(scale=1):
+                        batch_output_text = gr.Textbox(
+                            label="📝 一括変換結果",
+                            lines=15,
+                            max_lines=30,
+                            show_copy_button=True
+                        )
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
+                
+                # 一括処理ボタンクリック時の処理
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
+                batch_convert_btn.click(
+                    fn=update_batch_output,
+                    inputs=urls_input,
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
-        
-        # ボタンクリック時の処理
-        convert_btn.click(
-            fn=process_wikipedia_url,
-            inputs=url_input,
-            outputs=output_text
-        )
-        
-        # 使用例
-        gr.Examples(
-            examples=[
-                ["https://ja.wikipedia.org/wiki/Python"],
-                ["https://ja.wikipedia.org/wiki/JavaScript"],
-                ["https://ja.wikipedia.org/wiki/HTML"]
-            ],
-            inputs=url_input,
-            outputs=output_text,
-            fn=process_wikipedia_url,
-            cache_examples=False
-        )
+                
+                gr.Markdown("### 💡 一括処理の使い方")
+                gr.Markdown("1. テキストエリアに変換したいWikipediaのURLを1行に1つずつ入力します")
+                gr.Markdown("2. 「🚀 一括変換する」ボタンをクリックします")
+                gr.Markdown("3. 処理の進行状況が表示され、完了後に結果が表示されます")
+                gr.Markdown("4. 各URLの処理結果（成功/失敗）が明確に表示されます")
         
         gr.Markdown("---")
-        gr.Markdown("### 🎯 使用方法")
-        gr.Markdown("1. 変換したいWikipediaページのURLを入力します")
-        gr.Markdown("2. 「✨ 変換する」ボタンをクリックします")
-        gr.Markdown("3. 生成されたMarkdownをコピーして使用します")
+        gr.Markdown("### 🎯 基本的な使用方法")
+        gr.Markdown("- **単体処理**: 1つのWikipediaページを変換したい場合")
+        gr.Markdown("- **一括処理**: 複数のWikipediaページを一度に変換したい場合")
+        gr.Markdown("- 生成されたMarkdownは右側のテキストエリアからコピーできます")
+        gr.Markdown("- **📥 ダウンロード機能**: 変換が成功すると、マークダウンファイルとして直接ダウンロードできます")
+        gr.Markdown("  - 単体処理: ページ名に基づいたファイル名で個別ダウンロード")
+        gr.Markdown("  - 一括処理: 各URLごとの個別ダウンロード + 全体をまとめた一括ダウンロード")
+        gr.Markdown("  - 個別ダウンロード: 成功した各ページを個別のファイルとしてダウンロード可能（最大5つまで表示）")
         
         # ZENテーマの説明
         gr.HTML("""
@@ -201,7 +364,7 @@ if __name__ == "__main__":
     # アプリケーションを実行
     demo.launch(
         server_name="0.0.0.0",
-        server_port=7861,
+        server_port=7860,
         share=False,
         debug=True
     )
diff --git a/docker-compose.dev.yml b/docker-compose.dev.yml
new file mode 100644
index 0000000..6e6047b
--- /dev/null
+++ b/docker-compose.dev.yml
@@ -0,0 +1,25 @@
+version: '3.8'
+
+services:
+  wikipedia-converter-dev:
+    build:
+      context: .
+      dockerfile: Dockerfile
+    ports:
+      - "7861:7860"
+    environment:
+      - PYTHONUNBUFFERED=1
+      - GRADIO_SERVER_NAME=0.0.0.0
+      - GRADIO_SERVER_PORT=7861
+    volumes:
+      # 開発時にコードの変更をリアルタイムで反映
+      - .:/app
+      - /app/__pycache__
+    restart: unless-stopped
+    command: python app.py
+    networks:
+      - wikipedia-dev-network
+
+networks:
+  wikipedia-dev-network:
+    driver: bridge
\ No newline at end of file
diff --git a/docker-compose.yml b/docker-compose.yml
new file mode 100644
index 0000000..212066c
--- /dev/null
+++ b/docker-compose.yml
@@ -0,0 +1,27 @@
+version: '3.8'
+
+services:
+  wikipedia-converter:
+    build:
+      context: .
+      dockerfile: Dockerfile
+    ports:
+      - "7861:7860"
+    environment:
+      - PYTHONUNBUFFERED=1
+    # volumes:
+      # 開発時にコードの変更を反映させたい場合はコメントアウト
+      # - .:/app
+    restart: unless-stopped
+    healthcheck:
+      test: ["CMD", "curl", "-f", "http://localhost:7861"]
+      interval: 30s
+      timeout: 10s
+      retries: 3
+      start_period: 40s
+    networks:
+      - wikipedia-network
+
+networks:
+  wikipedia-network:
+    driver: bridge
\ No newline at end of file
diff --git a/requirements.txt b/requirements.txt
index 30c42d3..0304013 100644
--- a/requirements.txt
+++ b/requirements.txt
@@ -1,4 +1,4 @@
 requests>=2.31.0
 beautifulsoup4>=4.12.0
 html2text>=2020.1.16
-gradio>=4.44.0
+gradio>=5.42.0
diff --git a/theme.py b/theme.py
new file mode 100644
index 0000000..d0bc5f1
--- /dev/null
+++ b/theme.py
@@ -0,0 +1,44 @@
+import gradio as gr
+
+def create_zen_theme():
+    """
+    ZENテーマの作成
+    和モダンなデザインで、使いやすさと美しさを追求したテーマ
+    """
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
+        block_border_color="#e8e2d5",
+        block_border_width="3px",
+        panel_background_fill="#ffffff",
+        panel_border_color="#e8e2d5",
+        slider_color="#d4a574",
+    )
\ No newline at end of file
```
