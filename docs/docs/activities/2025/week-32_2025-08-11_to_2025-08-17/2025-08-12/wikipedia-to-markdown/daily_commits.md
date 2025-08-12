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

## ⏰ 16:30:14 - `fb02556`
**Update sync-to-hf.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Tue Aug 12 16:30:14 2025 +0900
M	.github/workflows/sync-to-hf.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Tue Aug 12 16:30:14 2025 +0900

    Update sync-to-hf.yml

 .github/workflows/sync-to-hf.yml | 7 ++-----
 1 file changed, 2 insertions(+), 5 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-hf.yml b/.github/workflows/sync-to-hf.yml
index a64c4cb..5879e47 100644
--- a/.github/workflows/sync-to-hf.yml
+++ b/.github/workflows/sync-to-hf.yml
@@ -21,15 +21,12 @@ jobs:
         env:
           HF_TOKEN: ${{ secrets.HF_TOKEN }}
         run: |
-          # リポジトリ名を取得
-          REPO_NAME="${GITHUB_REPOSITORY##*/}"
-          
           # Git設定
           git config --global user.email "action@github.com"
           git config --global user.name "GitHub Action"
           
           # Hugging Face Hubにリモートを追加
-          git remote add hf https://huggingface.co/spaces/${{ github.repository_owner }}/${REPO_NAME}
+          git remote add hf https://huggingface.co/spaces/MakiAi/wikipedia-to-markdown
           
           # 強制プッシュでHugging Faceに同期
-          git push --force https://user:$HF_TOKEN@huggingface.co/spaces/${{ github.repository_owner }}/${REPO_NAME} HEAD:main
\ No newline at end of file
+          git push --force https://user:$HF_TOKEN@huggingface.co/spaces/MakiAi/wikipedia-to-markdown HEAD:main
```

---

## ⏰ 16:39:15 - `0742d0c`
**📝 Hugging Face Spaces用のメタデータを追加**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:39:15 2025 +0900
M	README.md
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:39:15 2025 +0900

    📝 Hugging Face Spaces用のメタデータを追加
    
    - license: MIT
    - sdk: gradio (v5.42.0)
    - emoji: 📈
    - colorFrom/To: green to indigo
    - thumbnail画像を設定

 README.md | 13 ++++++++++++-
 1 file changed, 12 insertions(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/README.md b/README.md
index 1a1aeff..d9adc40 100644
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
 
 # 📚 Wikipedia to Markdown Converter
@@ -218,4 +229,4 @@ def create_zen_theme():
 
 ---
 
-© 2025 Wikipedia to Markdown Converter
+© 2025 Wikipedia to Markdown Converter
\ No newline at end of file
```

---

## ⏰ 16:39:25 - `c5c12c8`
**🔧 GitHub Actions ワークフローを修正**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:39:25 2025 +0900
M	.github/workflows/sync-to-hf.yml
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:39:25 2025 +0900

    🔧 GitHub Actions ワークフローを修正
    
    - 動的なリポジトリ名取得を削除
    - MakiAi/wikipedia-to-markdownに固定
    - コードの簡素化とメンテナンス性向上

 .github/workflows/sync-to-hf.yml | 7 ++-----
 1 file changed, 2 insertions(+), 5 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-hf.yml b/.github/workflows/sync-to-hf.yml
index a64c4cb..e0446a3 100644
--- a/.github/workflows/sync-to-hf.yml
+++ b/.github/workflows/sync-to-hf.yml
@@ -21,15 +21,12 @@ jobs:
         env:
           HF_TOKEN: ${{ secrets.HF_TOKEN }}
         run: |
-          # リポジトリ名を取得
-          REPO_NAME="${GITHUB_REPOSITORY##*/}"
-          
           # Git設定
           git config --global user.email "action@github.com"
           git config --global user.name "GitHub Action"
           
           # Hugging Face Hubにリモートを追加
-          git remote add hf https://huggingface.co/spaces/${{ github.repository_owner }}/${REPO_NAME}
+          git remote add hf https://huggingface.co/spaces/MakiAi/wikipedia-to-markdown
           
           # 強制プッシュでHugging Faceに同期
-          git push --force https://user:$HF_TOKEN@huggingface.co/spaces/${{ github.repository_owner }}/${REPO_NAME} HEAD:main
\ No newline at end of file
+          git push --force https://user:$HF_TOKEN@huggingface.co/spaces/MakiAi/wikipedia-to-markdown HEAD:main
\ No newline at end of file
```

---

## ⏰ 16:39:35 - `7fc65f6`
**🔧 アプリケーションポート番号を修正**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:39:35 2025 +0900
M	app.py
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:39:35 2025 +0900

    🔧 アプリケーションポート番号を修正
    
    - server_port: 7861 → 7860
    - Hugging Face Spacesの標準ポートに合わせて変更
    - デプロイメント環境との整合性を確保

 app.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/app.py b/app.py
index ebcd4d9..81ea80c 100644
--- a/app.py
+++ b/app.py
@@ -240,7 +240,7 @@ if __name__ == "__main__":
     # アプリケーションを実行
     demo.launch(
         server_name="0.0.0.0",
-        server_port=7861,
+        server_port=7860,
         share=False,
         debug=True
     )
```

---

## ⏰ 16:39:44 - `e592f99`
**🐳 Docker設定を最適化**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:39:44 2025 +0900
M	docker-compose.dev.yml
M	docker-compose.yml
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:39:44 2025 +0900

    🐳 Docker設定を最適化
    
    - ポートマッピング: 7861:7861 → 7861:7860
    - container_nameを削除してDocker Composeの自動命名を使用
    - 設定の簡素化とポータビリティ向上

 docker-compose.dev.yml | 3 +--
 docker-compose.yml     | 3 +--
 2 files changed, 2 insertions(+), 4 deletions(-)
```

### 💻 Code Changes
```diff
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
```

---

## ⏰ 16:39:53 - `cc0259d`
**🎨 テーマのボーダースタイルを改善**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:39:53 2025 +0900
M	theme.py
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:39:53 2025 +0900

    🎨 テーマのボーダースタイルを改善
    
    - block_border_color: #f5f2ed → #e8e2d5
    - panel_border_color: #f5f2ed → #e8e2d5
    - block_border_width: 1pxを明示的に設定
    - より洗練されたビジュアルデザインに調整

 theme.py | 5 +++--
 1 file changed, 3 insertions(+), 2 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/theme.py b/theme.py
index 64ecd56..168f3d2 100644
--- a/theme.py
+++ b/theme.py
@@ -36,8 +36,9 @@ def create_zen_theme():
         input_border_color="#d4c4a8",
         input_border_color_focus="#d4a574",
         block_background_fill="#ffffff",
-        block_border_color="#f5f2ed",
+        block_border_color="#e8e2d5",
+        block_border_width="1px",
         panel_background_fill="#ffffff",
-        panel_border_color="#f5f2ed",
+        panel_border_color="#e8e2d5",
         slider_color="#d4a574",
     )
\ No newline at end of file
```

---

## ⏰ 16:40:12 - `a45f672`
**🔀 Merge: Hugging Face Spacesデプロイメント設定の最適化**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Merge: 33a2ff9 cc0259d
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:40:12 2025 +0900
```

### 📊 Statistics
```bash
Merge: 33a2ff9 cc0259d
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:40:12 2025 +0900

    🔀 Merge: Hugging Face Spacesデプロイメント設定の最適化
    
    - Hugging Face Spacesメタデータの追加
    - GitHub Actionsワークフローの修正
    - ポート設定の統一化 (7860)
    - Docker設定の簡素化
    - テーマデザインの改善

 .github/workflows/sync-to-hf.yml |  7 ++-----
 README.md                        | 13 ++++++++++++-
 app.py                           |  2 +-
 docker-compose.dev.yml           |  3 +--
 docker-compose.yml               |  3 +--
 theme.py                         |  5 +++--
 6 files changed, 20 insertions(+), 13 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 16:57:20 - `ca43a39`
**✨ Wikipediaマークダウン変換にファイルダウンロード機能を追加**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:57:20 2025 +0900
M	app.py
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:57:20 2025 +0900

    ✨ Wikipediaマークダウン変換にファイルダウンロード機能を追加
    
    - URLからファイル名を自動生成する機能を実装
    - 単体処理でのマークダウンファイル直接ダウンロード機能
    - 一括処理での個別ファイル + 全体まとめファイルダウンロード機能
    - 一時ファイル作成とファイルパス管理機能を追加

 app.py | 152 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++------
 1 file changed, 138 insertions(+), 14 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/app.py b/app.py
index 81ea80c..47f32ac 100644
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
```

---

## ⏰ 16:57:29 - `61fa8f3`
**🎨 UIテーマのブロック境界線を調整**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:57:29 2025 +0900
M	theme.py
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:57:29 2025 +0900

    🎨 UIテーマのブロック境界線を調整
    
    - ブロック境界線の幅を1pxから3pxに変更
    - より明確な視覚的区切りを提供してユーザビリティを向上

 theme.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/theme.py b/theme.py
index 168f3d2..d0bc5f1 100644
--- a/theme.py
+++ b/theme.py
@@ -37,7 +37,7 @@ def create_zen_theme():
         input_border_color_focus="#d4a574",
         block_background_fill="#ffffff",
         block_border_color="#e8e2d5",
-        block_border_width="1px",
+        block_border_width="3px",
         panel_background_fill="#ffffff",
         panel_border_color="#e8e2d5",
         slider_color="#d4a574",
```

---

## ⏰ 16:57:42 - `164b49b`
**🔀 Merge: Wikipediaマークダウン変換アプリにファイルダウンロード機能とUI改善を追加**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Merge: a45f672 61fa8f3
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:57:42 2025 +0900
```

### 📊 Statistics
```bash
Merge: a45f672 61fa8f3
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Tue Aug 12 16:57:42 2025 +0900

    🔀 Merge: Wikipediaマークダウン変換アプリにファイルダウンロード機能とUI改善を追加

 app.py   | 152 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++------
 theme.py |   2 +-
 2 files changed, 139 insertions(+), 15 deletions(-)
```

### 💻 Code Changes
```diff
```

---

