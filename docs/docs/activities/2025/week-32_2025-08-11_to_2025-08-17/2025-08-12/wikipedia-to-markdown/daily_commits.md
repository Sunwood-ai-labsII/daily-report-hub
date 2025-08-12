# 📝 Daily Commits

## ⏰ 15:36:05 - `bd6d8a1`
**Update README.md**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Tue Aug 12 15:36:05 2025 +0900
M	README.md
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Tue Aug 12 15:36:05 2025 +0900

    Update README.md

 README.md | 9 +++++----
 1 file changed, 5 insertions(+), 4 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/README.md b/README.md
index 1a1aeff..135ba54 100644
--- a/README.md
+++ b/README.md
@@ -2,10 +2,11 @@
 
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
 
```

---

## ⏰ 15:46:33 - `f19ceba`
**Update README.md**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Tue Aug 12 15:46:33 2025 +0900
M	README.md
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Tue Aug 12 15:46:33 2025 +0900

    Update README.md

 README.md | 2 ++
 1 file changed, 2 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/README.md b/README.md
index 135ba54..ae3c9b7 100644
--- a/README.md
+++ b/README.md
@@ -1,5 +1,7 @@
 <div align="center">
 
+![](https://github.com/user-attachments/assets/201c0b39-6bf7-4599-a62a-dd3e6f61e5f8)
+
 # 📚 Wikipedia to Markdown Converter
 
 ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
```

---

## ⏰ 16:26:02 - `0987c6b`
**✨ テーマ機能を独立したモジュールに分離**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:26:02 2025 +0900
A	theme.py
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:26:02 2025 +0900

    ✨ テーマ機能を独立したモジュールに分離
    
    - ZENテーマの定義をtheme.pyに移動
    - コードの可読性と保守性を向上
    - テーマ関連の設定を一元管理

 theme.py | 43 +++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 43 insertions(+)
```

### 💻 Code Changes
```diff
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

---

## ⏰ 16:26:12 - `bcca8e9`
**⬆️ Gradioバージョンを5.42.0にアップデート**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:26:12 2025 +0900
M	requirements.txt
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:26:12 2025 +0900

    ⬆️ Gradioバージョンを5.42.0にアップデート
    
    - gradio 4.44.0 → 5.42.0に更新
    - 新機能とセキュリティ修正を適用
    - 一括処理機能で必要な新機能を利用可能に

 requirements.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
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
```

---

## ⏰ 16:26:23 - `71bb538`
**🚀 Wikipedia一括処理機能を追加とUI改善**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:26:23 2025 +0900
M	app.py
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:26:23 2025 +0900

    🚀 Wikipedia一括処理機能を追加とUI改善
    
    - 複数URLの一括変換機能を実装
    - タブベースのUIに変更（単体処理/一括処理）
    - プログレスバー表示で処理状況を可視化
    - エラーハンドリングと結果表示を改善
    - テーマモジュールのインポートに変更

 app.py | 191 +++++++++++++++++++++++++++++++++++++++--------------------------
 1 file changed, 115 insertions(+), 76 deletions(-)
```

### 💻 Code Changes
```diff
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
```

---

## ⏰ 16:26:32 - `6a7896a`
**🐳 Docker環境の構築とデプロイメント設定を追加**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:26:32 2025 +0900
A	.dockerignore
A	Dockerfile
A	docker-compose.dev.yml
A	docker-compose.yml
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:26:32 2025 +0900

    🐳 Docker環境の構築とデプロイメント設定を追加
    
    - Dockerfileでコンテナ化環境を構築
    - docker-compose.ymlで本番環境設定
    - docker-compose.dev.ymlで開発環境設定
    - .dockerignoreで不要ファイルを除外

 .dockerignore          | 56 ++++++++++++++++++++++++++++++++++++++++++++++++++
 Dockerfile             | 28 +++++++++++++++++++++++++
 docker-compose.dev.yml | 26 +++++++++++++++++++++++
 docker-compose.yml     | 28 +++++++++++++++++++++++++
 4 files changed, 138 insertions(+)
```

### 💻 Code Changes
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
diff --git a/docker-compose.dev.yml b/docker-compose.dev.yml
new file mode 100644
```

---

## ⏰ 16:26:42 - `e86bf25`
**⚙️ Hugging Face自動同期ワークフローを追加**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:26:42 2025 +0900
A	.github/workflows/sync-to-hf.yml
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:26:42 2025 +0900

    ⚙️ Hugging Face自動同期ワークフローを追加
    
    - GitHub ActionsでHugging Faceへの自動デプロイ設定
    - mainブランチへのプッシュ時に自動同期
    - CI/CDパイプラインの構築

 .github/workflows/sync-to-hf.yml | 35 +++++++++++++++++++++++++++++++++++
 1 file changed, 35 insertions(+)
```

### 💻 Code Changes
```diff
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
```

---

## ⏰ 16:27:00 - `33a2ff9`
**🔀 Merge: Wikipedia一括処理機能とDocker環境構築**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Merge: f980cd9 e86bf25
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:27:00 2025 +0900
```

### 📊 Statistics
```bash
Merge: f980cd9 e86bf25
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:27:00 2025 +0900

    🔀 Merge: Wikipedia一括処理機能とDocker環境構築

 .dockerignore                    |  56 ++++++++++++
 .github/workflows/sync-to-hf.yml |  35 +++++++
 Dockerfile                       |  28 ++++++
 app.py                           | 191 +++++++++++++++++++++++----------------
 docker-compose.dev.yml           |  26 ++++++
 docker-compose.yml               |  28 ++++++
 requirements.txt                 |   2 +-
 theme.py                         |  43 +++++++++
 8 files changed, 332 insertions(+), 77 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 16:27:51 - `5e48d53`
**Merge branch 'develop'**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Merge: f19ceba 33a2ff9
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:27:51 2025 +0900
```

### 📊 Statistics
```bash
Merge: f19ceba 33a2ff9
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:27:51 2025 +0900

    Merge branch 'develop'

 .dockerignore                    |  56 ++++++++++++
 .github/workflows/sync-to-hf.yml |  35 +++++++
 Dockerfile                       |  28 ++++++
 app.py                           | 191 +++++++++++++++++++++++----------------
 docker-compose.dev.yml           |  26 ++++++
 docker-compose.yml               |  28 ++++++
 requirements.txt                 |   2 +-
 theme.py                         |  43 +++++++++
 8 files changed, 332 insertions(+), 77 deletions(-)
```

### 💻 Code Changes
```diff
```

---

