# 🔄 Latest Code Changes

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
index 0000000..a64c4cb
--- /dev/null
+++ b/.github/workflows/sync-to-hf.yml
@@ -0,0 +1,35 @@
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
+          # リポジトリ名を取得
+          REPO_NAME="${GITHUB_REPOSITORY##*/}"
+          
+          # Git設定
+          git config --global user.email "action@github.com"
+          git config --global user.name "GitHub Action"
+          
+          # Hugging Face Hubにリモートを追加
+          git remote add hf https://huggingface.co/spaces/${{ github.repository_owner }}/${REPO_NAME}
+          
+          # 強制プッシュでHugging Faceに同期
+          git push --force https://user:$HF_TOKEN@huggingface.co/spaces/${{ github.repository_owner }}/${REPO_NAME} HEAD:main
\ No newline at end of file
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
diff --git a/app.py b/app.py
index 8cd6fcd..ebcd4d9 100644
--- a/app.py
+++ b/app.py
@@ -3,45 +3,7 @@ from bs4 import BeautifulSoup
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
 
 def scrape_wikipedia_to_markdown_final(url: str) -> str:
     """
@@ -127,6 +89,46 @@ def process_wikipedia_url(url):
     
     return markdown_content
 
+def process_multiple_urls(urls_text, progress=gr.Progress()):
+    """複数のWikipedia URLを一括処理してMarkdownを生成する関数"""
+    if not urls_text.strip():
+        return "URLリストを入力してください。"
+    
+    # URLリストを行ごとに分割
+    urls = [url.strip() for url in urls_text.strip().split('\n') if url.strip()]
+    
+    if not urls:
+        return "有効なURLが見つかりませんでした。"
+    
+    results = []
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
+        except Exception as e:
+            results.append(f"❌ 処理エラー: {url}\nエラー内容: {str(e)}")
+    
+    # 結果を結合
+    final_result = "\n\n" + "="*80 + "\n\n".join(results)
+    return final_result
+
 # Gradioインターフェースの作成
 def create_interface():
     """Gradioインターフェースを作成する関数"""
@@ -141,48 +143,85 @@ def create_interface():
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
+                
+                # ボタンクリック時の処理
+                convert_btn.click(
+                    fn=process_wikipedia_url,
+                    inputs=url_input,
+                    outputs=output_text
+                )
+                
+                # 使用例
+                gr.Examples(
+                    examples=[
+                        ["https://ja.wikipedia.org/wiki/Python"],
+                        ["https://ja.wikipedia.org/wiki/JavaScript"],
+                        ["https://ja.wikipedia.org/wiki/HTML"]
+                    ],
+                    inputs=url_input,
+                    outputs=output_text,
+                    fn=process_wikipedia_url,
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
+                            lines=20,
+                            max_lines=50,
+                            show_copy_button=True
+                        )
+                
+                # 一括処理ボタンクリック時の処理
+                batch_convert_btn.click(
+                    fn=process_multiple_urls,
+                    inputs=urls_input,
+                    outputs=batch_output_text
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
         
         # ZENテーマの説明
         gr.HTML("""
diff --git a/docker-compose.dev.yml b/docker-compose.dev.yml
new file mode 100644
index 0000000..19669ff
--- /dev/null
+++ b/docker-compose.dev.yml
@@ -0,0 +1,26 @@
+version: '3.8'
+
+services:
+  wikipedia-converter-dev:
+    build:
+      context: .
+      dockerfile: Dockerfile
+    container_name: wikipedia-to-markdown-dev
+    ports:
+      - "7861:7861"
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
index 0000000..349a04c
--- /dev/null
+++ b/docker-compose.yml
@@ -0,0 +1,28 @@
+version: '3.8'
+
+services:
+  wikipedia-converter:
+    build:
+      context: .
+      dockerfile: Dockerfile
+    container_name: wikipedia-to-markdown
+    ports:
+      - "7861:7861"
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
index 0000000..64ecd56
--- /dev/null
+++ b/theme.py
@@ -0,0 +1,43 @@
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
+        block_border_color="#f5f2ed",
+        panel_background_fill="#ffffff",
+        panel_border_color="#f5f2ed",
+        slider_color="#d4a574",
+    )
\ No newline at end of file
```
