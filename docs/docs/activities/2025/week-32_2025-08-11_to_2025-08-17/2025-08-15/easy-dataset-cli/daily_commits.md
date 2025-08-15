# 📝 Daily Commits

## ⏰ 12:36:26 - `d8aa5b3`
**Initial commit**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Fri Aug 15 12:36:26 2025 +0900
A	.SourceSageignore
A	.github/workflows/sync-to-report-gh.yml
A	.gitignore
A	LICENSE
A	README.md
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Fri Aug 15 12:36:26 2025 +0900

    Initial commit

 .SourceSageignore                       |  54 +++++++
 .github/workflows/sync-to-report-gh.yml |  52 +++++++
 .gitignore                              | 208 +++++++++++++++++++++++++
 LICENSE                                 |  21 +++
 README.md                               | 267 ++++++++++++++++++++++++++++++++
 5 files changed, 602 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/.SourceSageignore b/.SourceSageignore
new file mode 100644
index 0000000..a029c83
--- /dev/null
+++ b/.SourceSageignore
@@ -0,0 +1,54 @@
+# バージョン管理システム関連
+.git/
+.gitignore
+
+# キャッシュファイル
+__pycache__/
+.pytest_cache/
+**/__pycache__/**
+*.pyc
+
+# ビルド・配布関連
+build/
+dist/
+*.egg-info/
+
+# 一時ファイル・出力
+output/
+output.md
+test_output/
+.SourceSageAssets/
+.SourceSageAssetsDemo/
+
+# アセット
+*.png
+*.svg
+*.jpg
+*.jepg
+assets/
+
+# その他
+LICENSE
+example/
+package-lock.json
+.DS_Store
+
+# 特定のディレクトリを除外
+tests/temp/
+docs/drafts/
+
+# パターンの例外（除外対象から除外）
+!docs/important.md
+!.github/workflows/
+repository_summary.md
+
+# Terraform関連
+.terraform
+*.terraform.lock.hcl
+*.backup
+*.tfstate
+
+# Python仮想環境
+venv
+.venv
+
diff --git a/.github/workflows/sync-to-report-gh.yml b/.github/workflows/sync-to-report-gh.yml
new file mode 100644
index 0000000..6dc1edd
--- /dev/null
+++ b/.github/workflows/sync-to-report-gh.yml
@@ -0,0 +1,52 @@
+name: 📊 デイリーレポートハブ同期 v2.3 (YUKIHIKO PR版 - 完全リモート実行)
+on:
+  push:
+    branches: [main, master]
+  pull_request:
+    types: [opened, synchronize, closed]
+
+env:
+  WEEK_START_DAY: 1
+  AUTO_APPROVE: true
+  AUTO_MERGE: true  
+  CREATE_PR: true
+  # リモートスクリプトの設定
+  SCRIPTS_BASE_URL: https://raw.githubusercontent.com/Sunwood-ai-labsII/daily-report-hub_dev/main/.github/scripts
+
+jobs:
+  sync-data:
+    runs-on: ubuntu-latest
+    steps:
+      - name: 📥 現在のリポジトリをチェックアウト
+        uses: actions/checkout@v4
+        with:
+          fetch-depth: 0
+
+      - name: 📅 週情報を計算
+        run: curl -LsSf ${SCRIPTS_BASE_URL}/calculate-week-info.sh | sh -s -- ${{ env.WEEK_START_DAY }}
+
+      - name: 🔍 Git活動を分析
+        run: curl -LsSf ${SCRIPTS_BASE_URL}/analyze-git-activity.sh | sh
+
+      - name: 📝 Markdownレポートを生成
+        run: curl -LsSf ${SCRIPTS_BASE_URL}/generate-markdown-reports.sh | sh
+
+      - name: 📂 レポートハブをクローン
```

---

## ⏰ 12:58:25 - `68cc12e`
**📝 READMEをEasy Dataset CLIプロジェクト用に完全書き換え**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 12:58:25 2025 +0900
M	README.md
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 12:58:25 2025 +0900

    📝 READMEをEasy Dataset CLIプロジェクト用に完全書き換え
    
    - Daily Report Hub TemplateからEasy Dataset CLIの説明に変更
    - インストール方法、使用方法、コマンドオプションを詳細に記載
    - GA定義ファイルの形式とサポートするLLMモデルの情報を追加

 README.md | 335 +++++++++++++++++++++-----------------------------------------
 1 file changed, 110 insertions(+), 225 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/README.md b/README.md
index 2b43334..27bea1e 100644
--- a/README.md
+++ b/README.md
@@ -1,267 +1,152 @@
+# Easy Dataset CLI
 
-![](https://github.com/user-attachments/assets/e8fe7c3c-a8d8-4165-86a1-86b9f433f9b3)
+テキストファイルからQ&Aペアを生成するシンプルなCLIツールです。LLMを使用してGenre-Audienceペアに基づいた多様なQ&Aデータセットを作成し、Genre別のXMLファイルとして出力します。
 
-<div align="center">
+## 特徴
 
-# Daily Report Hub Template
+- **シンプル**: データベース不要、マークダウンでGA定義
+- **柔軟**: 複数のGenre-Audienceペアに対応
+- **安定**: LLMからの直接XML出力で信頼性向上
+- **効率的**: テキスト分割とバッチ処理で大きなファイルにも対応
 
-<img src="https://img.shields.io/badge/GitHub%20Actions-CICD-blue?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
-<img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Bash" />
-<a href="https://github.com/Sunwood-ai-labsII/daily-report-hub">
-  <img src="https://img.shields.io/badge/daily--report--hub-PANDA-00D4AA?style=for-the-badge&logo=github&logoColor=white" alt="daily-report-hub PANDA" />
-</a>
+## インストール
 
-</div>
+\```bash
+# 仮想環境の作成（推奨）
+python -m venv venv
+source venv/bin/activate  # Linux/macOS
+# または
+venv\Scripts\activate     # Windows
 
-
----
-
-## 📖 概要
-
-このリポジトリは、**Daily Report Hubのテンプレートリポジトリ**です。このテンプレートからリポジトリを作成すると、自動で日報生成・同期機能が有効になります。
-
-### 🎯 主な用途
-- 日報自動生成機能を必要とするプロジェクトのテンプレート
-- 集約用リポジトリ（daily-report-hub）への自動同期
-- GitHub Actionsによる完全自動化されたレポート生成
-
-### 🔄 運用方式
-このテンプレートから作成されたリポジトリは、daily-report-hub本体のワークフローから**リモート実行**されるスクリプトを使用して日報を生成・同期します。
-
----
-
-## 🚩 このテンプレートの役割
-
-### 🛠️ テンプレートとしての機能
-- **自動セットアップ**: 日報生成機能の自動有効化
-- **ワークフロー提供**: GitHub Actionsワークフローの自動適用
-- **同期機能**: 集約用リポジトリへの自動同期機能
-- **カスタマイズ**: 必要に応じた設定変更の容易性
-
-### 📦 提供される機能
-- Gitのコミット履歴・差分から日報（Markdown形式）を自動生成
-- 週単位・日単位でレポートを整理
-- 別リポジトリ（daily-report-hub）へPRベースで自動同期
-- プルリクエストの自動承認・自動マージ（設定可）
-- Docusaurus用のディレクトリ・ナビゲーション構造も自動生成
-
----
-
-## ⚙️ ワークフロー概要
-
-### 🔄 自動化フロー図
-
-\```mermaid
-graph TB
-    A[開発者のコード<br/>commit/push] --> B[GitHub Actions<br/>ワークフロー]
-    B --> C[レポート生成<br/>Markdown]
-    C --> D[ファイル同期<br/>クローン]
-    D --> E[PR作成・承認<br/>自動化可]
-    E --> F[集約リポジトリ<br/>daily-report-hub]
+# 依存関係のインストール
+pip install -e .
 \```
 
-### 📋 処理ステップ
-
-1. **トリガー**: **GitHub Actions**がmainブランチへのpushやPRをトリガー
-2. **データ収集**: リモートスクリプトで
-   - 週情報の計算
-   - Git活動の分析
-   - Markdownレポートの生成
-   - Docusaurus用ディレクトリ構造の作成
-3. **同期処理**: 集約用リポジトリ（daily-report-hub）をクローンし、レポートをコピー
-4. **PR処理**: PR作成・自動承認・自動マージ（設定に応じて自動化）
-
-### ⚙️ 設定可能なオプション
+## 使用方法
 
-| 設定 | 説明 | デフォルト値 |
-|------|------|-------------|
-| `WEEK_START_DAY` | 週の開始曜日（0=日曜日, 1=月曜日, ...） | `1`（月曜日） |
```

---

## ⏰ 12:58:40 - `fefc013`
**⚙️ プロジェクト設定ファイルを追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 12:58:40 2025 +0900
A	pyproject.toml
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 12:58:40 2025 +0900

    ⚙️ プロジェクト設定ファイルを追加
    
    - pyproject.tomlでPythonプロジェクトの依存関係とメタデータを定義
    - CLIツールのエントリーポイントとパッケージ情報を設定
    - 開発・実行に必要なライブラリの依存関係を明記

 pyproject.toml | 20 ++++++++++++++++++++
 1 file changed, 20 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/pyproject.toml b/pyproject.toml
new file mode 100644
index 0000000..d9b2651
--- /dev/null
+++ b/pyproject.toml
@@ -0,0 +1,20 @@
+[project]
+name = "easy-dataset-cli"
+version = "1.0.0"
+description = "A simple CLI tool to generate QA pairs from a text file using LLMs and GA pairs, outputting genre-specific XML files."
+dependencies = [
+    "typer[all]",          # CLIフレームワーク
+    "rich",                # リッチなコンソール出力
+    "litellm",             # LLM連携ライブラリ
+    "langchain-text-splitters", # テキスト分割用
+    "mistune",             # マークダウン解析用ライブラリ
+    "python-dotenv"        # .env ファイル読み込み用
+]
+
+[project.scripts]
+# "easy-dataset" コマンドで "easy_dataset_cli.main:app" を実行するよう設定
+easy-dataset = "easy_dataset_cli.main:app"
+
+[build-system]
+requires = ["setuptools>=61.0"]
+build-backend = "setuptools.build_meta"
\ No newline at end of file
```

---

## ⏰ 12:59:22 - `8b05bb7`
**✨ Easy Dataset CLIのコア機能を実装**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 12:59:22 2025 +0900
A	easy_dataset_cli/__init__.py
A	easy_dataset_cli/core.py
A	easy_dataset_cli/main.py
A	easy_dataset_cli/prompts.py
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 12:59:22 2025 +0900

    ✨ Easy Dataset CLIのコア機能を実装
    
    - main.py: Clickベースのコマンドラインインターフェースを実装
    - core.py: Q&Aペア生成とGA定義作成のメインロジックを実装
    - prompts.py: LLM用のプロンプトテンプレートを定義
    - __init__.py: パッケージ初期化ファイルを追加

 easy_dataset_cli/__init__.py |   1 +
 easy_dataset_cli/core.py     | 198 +++++++++++++++++++++++++++++++++++++++++++
 easy_dataset_cli/main.py     | 174 +++++++++++++++++++++++++++++++++++++
 easy_dataset_cli/prompts.py  |  80 +++++++++++++++++
 4 files changed, 453 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/easy_dataset_cli/__init__.py b/easy_dataset_cli/__init__.py
new file mode 100644
index 0000000..799b835
--- /dev/null
+++ b/easy_dataset_cli/__init__.py
@@ -0,0 +1 @@
+# easy_dataset_cli package
\ No newline at end of file
diff --git a/easy_dataset_cli/core.py b/easy_dataset_cli/core.py
new file mode 100644
index 0000000..0ed3e97
--- /dev/null
+++ b/easy_dataset_cli/core.py
@@ -0,0 +1,198 @@
+# easy_dataset_cli/core.py
+"""コアロジック: テキスト分割、Q&A生成、XML変換"""
+
+import os
+import xml.etree.ElementTree as ET
+from xml.dom import minidom
+from collections import defaultdict
+from pathlib import Path
+from typing import List, Dict
+import mistune
+from langchain_text_splitters import RecursiveCharacterTextSplitter
+from litellm import completion
+from rich.console import Console
+from dotenv import load_dotenv
+
+from .prompts import QA_GENERATION_PROMPT_WITH_GA_JA, GA_DEFINITION_GENERATION_PROMPT_JA
+
+# .envファイルを読み込む
+load_dotenv()
+
+console = Console()
+
+
+def parse_ga_file(file_path: Path) -> List[Dict[str, Dict[str, str]]]:
+    """マークダウンファイルからGAペアのリストを解析する"""
+    text = file_path.read_text(encoding="utf-8")
+    pairs = []
+    sections = text.split('---')
+    
+    for section in sections:
+        if not section.strip():
+            continue
+
+        ast = mistune.create_markdown(renderer=None)(section)
+        genre = {"title": "", "description": ""}
+        audience = {"title": "", "description": ""}
+        current_type = None
+
+        for node in ast:
+            if node['type'] == 'heading':
+                header_text = "".join(child['text'] for child in node['children'])
+                if 'genre' in header_text.lower():
+                    current_type = 'genre'
+                    genre['title'] = header_text.replace('Genre:', '').strip()
+                elif 'audience' in header_text.lower():
+                    current_type = 'audience'
+                    audience['title'] = header_text.replace('Audience:', '').strip()
+            elif node['type'] == 'paragraph':
+                description = "".join(child['text'] for child in node['children'])
+                if current_type == 'genre':
+                    genre['description'] = description
+                elif current_type == 'audience':
+                    audience['description'] = description
+
+        if genre['title'] and audience['title']:
+            pairs.append({"genre": genre, "audience": audience})
+    
+    return pairs
+
+
+def split_text(text: str, chunk_size: int, chunk_overlap: int) -> List[str]:
+    """LangChainのTextSplitterを使ってテキストをチャンクに分割する"""
+    text_splitter = RecursiveCharacterTextSplitter(
+        chunk_size=chunk_size,
+        chunk_overlap=chunk_overlap,
+        length_function=len,
+        is_separator_regex=False,
+    )
+    docs = text_splitter.create_documents([text])
+    return [doc.page_content for doc in docs]
+
+
+def generate_qa_for_chunk_with_ga(
+    chunk: str, model: str, ga_pair: Dict[str, Dict[str, str]]
+) -> List[Dict[str, str]]:
+    """litellmを使い、1つのチャンクと1つのGAペアからQ&Aペアのリストを生成する"""
+    prompt = QA_GENERATION_PROMPT_WITH_GA_JA.format(
+        context=chunk,
+        genre_title=ga_pair['genre']['title'],
+        genre_description=ga_pair['genre']['description'],
+        audience_title=ga_pair['audience']['title'],
+        audience_description=ga_pair['audience']['description'],
+    )
+
+    messages = [
+        {"role": "system", "content": "あなたは、XML形式で厳密に出力する優秀なアシスタントです。"},
```

---

## ⏰ 12:59:32 - `70b2de0`
**📚 サンプルファイルとGA定義例を追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 12:59:32 2025 +0900
A	example/input/Touhou_Chireiden.md
A	example/input/sample_document.txt
A	example/input/sample_ga_definition.md
A	example/output/ga-definitions.md
A	example/output/ga_definitions.md
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 12:59:32 2025 +0900

    📚 サンプルファイルとGA定義例を追加
    
    - example/ga_definitions.md: Genre-Audienceペアの定義例を追加
    - example/input/: 実際のテキストファイルサンプルを配置
    - ユーザーが実際の使用方法を理解できるリファレンス実装を提供

 example/input/Touhou_Chireiden.md     | 203 ++++++++++++++++++++++++++++++++++
 example/input/sample_document.txt     |  14 +++
 example/input/sample_ga_definition.md |  21 ++++
 example/output/ga-definitions.md      |  25 +++++
 example/output/ga_definitions.md      |  29 +++++
 5 files changed, 292 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/example/input/Touhou_Chireiden.md b/example/input/Touhou_Chireiden.md
new file mode 100644
index 0000000..80f2304
--- /dev/null
+++ b/example/input/Touhou_Chireiden.md
@@ -0,0 +1,203 @@
+# 東方地霊殿 〜 Subterranean Animism.
+
+東方地霊殿 〜 Subterranean Animism.ジャンル|  [弾幕系シューティング](/wiki/%E5%BC%BE%E5%B9%95%E7%B3%BB%E3%82%B7%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0 "弾幕系シューティング")ゲーム  
+---|---  
+対応機種|  [Windows](/wiki/Microsoft_Windows "Microsoft Windows") [2000](/wiki/Microsoft_Windows_2000 "Microsoft Windows 2000")/[XP](/wiki/Microsoft_Windows_XP "Microsoft Windows XP")  
+開発元|  [上海アリス幻樂団](/wiki/%E4%B8%8A%E6%B5%B7%E3%82%A2%E3%83%AA%E3%82%B9%E5%B9%BB%E6%A8%82%E5%9B%A3 "上海アリス幻樂団")  
+発売元|  [上海アリス幻樂団](/wiki/%E4%B8%8A%E6%B5%B7%E3%82%A2%E3%83%AA%E3%82%B9%E5%B9%BB%E6%A8%82%E5%9B%A3 "上海アリス幻樂団")  
+シリーズ|  [東方Project](/wiki/%E6%9D%B1%E6%96%B9Project "東方Project")  
+バージョン|  1.00a（2008年8月16日）  
+人数|  1人  
+メディア|  [CD-ROM](/wiki/CD-ROM "CD-ROM")  
+発売日|  2008年8月16日  
+2020年6月6日（[Steam](/wiki/Steam "Steam")版）  
+必要環境|  CPU: [Pentium](/wiki/Intel_Pentium_\(1993%E5%B9%B4\) "Intel Pentium \(1993年\)")以降 1GHz以上 推奨  
+[DirectX](/wiki/Microsoft_DirectX "Microsoft DirectX"): 9.0以上  
+[HDD空き容量](/wiki/%E3%83%8F%E3%83%BC%E3%83%89%E3%83%87%E3%82%A3%E3%82%B9%E3%82%AF%E3%83%89%E3%83%A9%E3%82%A4%E3%83%96 "ハードディスクドライブ"): 600MB 以上  
+[メモリ](/wiki/%E4%B8%BB%E8%A8%98%E6%86%B6%E8%A3%85%E7%BD%AE "主記憶装置"): 256MB 以上  
+アスペクト比|  4:3  
+解像度|  640×480（標準）  
+その他|  [同人ゲーム](/wiki/%E5%90%8C%E4%BA%BA%E3%82%B2%E3%83%BC%E3%83%A0 "同人ゲーム")（[インディーズゲーム](/wiki/%E3%82%A4%E3%83%B3%E3%83%87%E3%82%A3%E3%83%BC%E3%82%BA%E3%82%B2%E3%83%BC%E3%83%A0 "インディーズゲーム")）  
+[テンプレートを表示](/wiki/Template:%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E3%82%B2%E3%83%BC%E3%83%A0 "Template:コンピュータゲーム")  
+  
+『**東方地霊殿 〜 Subterranean Animism.** 』（とうほうちれいでん サブタレイニアン・アニミズム）とは、[同人サークル](/wiki/%E5%90%8C%E4%BA%BA%E3%82%B5%E3%83%BC%E3%82%AF%E3%83%AB "同人サークル")「[上海アリス幻樂団](/wiki/%E4%B8%8A%E6%B5%B7%E3%82%A2%E3%83%AA%E3%82%B9%E5%B9%BB%E6%A8%82%E5%9B%A3 "上海アリス幻樂団")」制作の[弾幕系シューティング](/wiki/%E5%BC%BE%E5%B9%95%E7%B3%BB%E3%82%B7%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0 "弾幕系シューティング")ゲームであり、[東方Project](/wiki/%E6%9D%B1%E6%96%B9Project "東方Project")の第11弾にあたる作品である。 
+
+本作は、2008年5月25日開催の[同人イベント](/wiki/%E5%90%8C%E4%BA%BA%E8%AA%8C%E5%8D%B3%E5%A3%B2%E4%BC%9A "同人誌即売会")「[博麗神社例大祭](/wiki/%E5%8D%9A%E9%BA%97%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD "博麗神社例大祭")5」にて体験版CD-ROMが販売され、6月29日に上海アリス幻樂団のウェブサイトでWeb体験版が公開され、8月16日開催の同人イベント「[コミックマーケット](/wiki/%E3%82%B3%E3%83%9F%E3%83%83%E3%82%AF%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%83%E3%83%88 "コミックマーケット")74」にて完成版が販売された。後に[同人ショップ](/wiki/%E5%90%8C%E4%BA%BA%E3%82%B7%E3%83%A7%E3%83%83%E3%83%97 "同人ショップ")での[委託販売](/wiki/%E5%A7%94%E8%A8%97%E8%B2%A9%E5%A3%B2 "委託販売")も行なわれている。雑誌『[キャラ☆メル](/wiki/%E3%82%AD%E3%83%A3%E3%83%A9%E2%98%86%E3%83%A1%E3%83%AB "キャラ☆メル")』Vol.5（2008年6月25日発売）の付属CD-ROMにも体験版が収録されている。 
+
+また、本作は2020年6月6日にSteamにて配信された[1]。 
+
+本作のあらすじにおける冬季の話としては過去より、旧作においては冬コミ(C53·C55)にて発表された事がしばしばあったものの、予定通りに夏季に頒布された作品でもある｡ 
+
+本項では、以降は『地霊殿』と称することとする。その他の本項で使用されている東方Project関連の略称については、[東方Project#凡例](/wiki/%E6%9D%B1%E6%96%B9Project#凡例 "東方Project")を参照。 
+
+## システム
+
+
+→「[東方Project § 基本システム](/wiki/%E6%9D%B1%E6%96%B9Project#基本システム "東方Project")」も参照
+
+機体性能の異なる「[博麗霊夢](/wiki/%E5%8D%9A%E9%BA%97%E9%9C%8A%E5%A4%A2 "博麗霊夢")」「[霧雨魔理沙](/wiki/%E9%9C%A7%E9%9B%A8%E9%AD%94%E7%90%86%E6%B2%99 "霧雨魔理沙")」の2種類の自機から1つ選択し、その後それぞれ3種類ある武器タイプ（装備）からいずれかを選択する。本作では「自機が妖怪のパートナーのひとりと組み、地上に残るその妖怪の力を借りながら地下に潜る」という設定になっており、武器タイプの選択はパートナーの選択と同義である。パートナーとなる妖怪は、霊夢が「[八雲紫](/wiki/%E5%85%AB%E9%9B%B2%E7%B4%AB "八雲紫")」「[伊吹萃香](/wiki/%E4%BC%8A%E5%90%B9%E8%90%83%E9%A6%99 "伊吹萃香")」「[射命丸文](/wiki/%E5%B0%84%E5%91%BD%E4%B8%B8%E6%96%87 "射命丸文")」、魔理沙が「[アリス・マーガトロイド](/wiki/%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%BB%E3%83%9E%E3%83%BC%E3%82%AC%E3%83%88%E3%83%AD%E3%82%A4%E3%83%89 "アリス・マーガトロイド")」「[パチュリー・ノーレッジ](/wiki/%E3%83%91%E3%83%81%E3%83%A5%E3%83%AA%E3%83%BC%E3%83%BB%E3%83%8E%E3%83%BC%E3%83%AC%E3%83%83%E3%82%B8 "パチュリー・ノーレッジ")」「[河城にとり](/wiki/%E6%B2%B3%E5%9F%8E%E3%81%AB%E3%81%A8%E3%82%8A "河城にとり")」の各3名[1]。敵や敵弾に当たるとミスとなり残機が1つ減った上でその場で復活する。全ての残機を失うと[ゲームオーバー](/wiki/%E3%82%B2%E3%83%BC%E3%83%A0%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC "ゲームオーバー")となるが、[コンティニュー](/wiki/%E3%82%B2%E3%83%BC%E3%83%A0%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC "ゲームオーバー")すればそのステージの最初から復活しゲームを続行可能。コンテニューしないで6[面](/wiki/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8_\(%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E3%82%B2%E3%83%BC%E3%83%A0\) "ステージ \(コンピュータゲーム\)")（最終面）の[ボス](/wiki/%E3%83%9C%E3%82%B9%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC "ボスキャラクター")を倒すとエンディングになる。難易度Normal以上でコンティニューせずにクリアすれば、全1面のExtraステージが追加される。 
+
+本作では、アイテム「残機の欠片」を一定数集めることでエクステンドする[2][1]。「残機の欠片」は、ボス戦にてミスをせず（ボムは使用可）に既定の敵ライフを削ると出現する。 
+
+#### 交信強度
+
+    [![](//upload.wikimedia.org/wikipedia/commons/9/96/Mobile_phone_signal.png)](/wiki/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB:Mobile_phone_signal.png)一般的な携帯電話の通信強度アイコンの例。『地霊殿』でのそれとは若干デザインが異なる。
+    本作には**交信強度** というパラメータが存在する[2]。点アイテム入手時の得点は交信強度によって補正されるため、スコア稼ぎの際に影響を与えるパラメータとなっている。
+    交信強度は、画面左下に[携帯電話](/wiki/%E6%90%BA%E5%B8%AF%E9%9B%BB%E8%A9%B1 "携帯電話")の受信強度のアイコンのような形で表示される[2]。交信強度は[アイテム自動蒐集](/wiki/%E6%9D%B1%E6%96%B9Project#アイテム "東方Project")が発動するラインよりも上まで移動するか、[敵弾にかする](/wiki/%E6%9D%B1%E6%96%B9Project#当たり判定 "東方Project")ことで増加し、前者の場合は一瞬で最大値まで増加する。交信強度は増加する行動をとらないと減少が始まるが、最大になっているときは一定時間は減少しない。
+    交信強度が最大の時には、アイテム自動蒐集が発生する。すなわち、敵弾にかすることで通信強度を最大に出来れば、画面上部に行かなくてもアイテム自動蒐集が可能である。
+    交信強度の最大値は初期値は1.00だが、かすり回数が100の倍数に達するごとに0.01ずつ上昇する。
+    ゲーム中での設定では、地下に潜る霊夢や魔理沙と、地上にいるサポート妖怪との交信強度を示すものとされている。
+
+#### 得点最大値
+
+    本作では点アイテム入手時の最大値が、交信強度の近く、画面左下に数字で表示されている。基本的には最大得点値と交信強度の値の[積](/wiki/%E7%A9%8D "積")が、点アイテム取得時の実際の点数となる。
+    この値は、敵を倒したときに放出される「得点最大値増加アイテム」を入手することで増加するとされている。
+
+## あらすじ
+
+
+雪の降る冬のある日、博麗神社の近くに突如高温の[間欠泉](/wiki/%E9%96%93%E6%AC%A0%E6%B3%89 "間欠泉")が噴出した[1]。博麗神社の巫女である[博麗霊夢](/wiki/%E5%8D%9A%E9%BA%97%E9%9C%8A%E5%A4%A2 "博麗霊夢")は、[温泉](/wiki/%E6%B8%A9%E6%B3%89 "温泉")になれば参拝客が増えるはずだと喜んでいたが、温泉水とともに地底の悪霊まで湧き出る[1]。霊夢は慌てたものの、地霊は大人しかったため、温泉を取り異変を解決しようとは思わなかった[2]。しかし、魔女のパチュリー・ノーレッジは地下の妖怪や地霊が表に出ることに危険を感じ、古い妖怪である八雲紫に相談する。地底には地底のルールがあり、地上の妖怪が地底に干渉することは好ましくないとの判断から、紫はパチュリーに霊夢たち人間を地底へ送り出すことを約束し、妖怪たちはそれを遠隔サポートすることとなった[1]。 
+
+地底に潜った霊夢たちは、間欠泉の原因が妖怪の霊烏路空の仕業であることを突き止める。地上の神々から強力な[核融合](/wiki/%E6%A0%B8%E8%9E%8D%E5%90%88 "核融合")の力（間欠泉はその熱による副次的なもの）を手に入れた空は地上の侵略を企んでいたが、霊夢たちに懲らしめられ、改心した。しかし空の核融合の力はそのままだったため、地霊は止まったが間欠泉が止むことはなかった。 
+
+後に霊夢たちは、空の話から、空に力を授けたのは守矢神社の神々ではないかと疑い、真相を確かめるために守矢神社へ向かう。そこで、守矢の1柱である洩矢諏訪子から事の顛末を聞くことになる。 
+
+## 登場人物
+
+
+→「[東方Projectの登場人物](/wiki/%E6%9D%B1%E6%96%B9Project%E3%81%AE%E7%99%BB%E5%A0%B4%E4%BA%BA%E7%89%A9 "東方Projectの登場人物")」および「[幻想郷](/wiki/%E5%B9%BB%E6%83%B3%E9%83%B7 "幻想郷")」も参照
+
+### 新規の登場人物
+
+
+ここでは、『地霊殿』が初出の登場人物を解説する。 
+
+#### キスメ
+
+    [釣瓶落とし](/wiki/%E9%87%A3%E7%93%B6%E8%90%BD%E3%81%A8%E3%81%97 "釣瓶落とし")。狭い所が好きな妖怪で、釣瓶の中に入った状態で登場する。外見に反して凶暴な妖怪であり、近づく人間の首を問答無用で刈り取り、そのまま桶に入れて持ち去ってしまうとされる[3]。さらに「文々。新聞」にも、彼女と思われる釣瓶落としが起こした怪事件が掲載されている[4]。
+
+#### 黒谷 ヤマメ（くろだに やまめ）
+
+    [土蜘蛛](/wiki/%E5%9C%9F%E8%9C%98%E8%9B%9B "土蜘蛛")。蜘蛛の姿をした妖怪。**病気を操る程度の能力** を持っている。彼女に遭遇した人間は高い頻度で重度の熱病を発症するという[5]。
+    妖怪の山の麓にある地底へと続く風穴や旧都の周辺に住んでいる。人間にとっては危険な妖怪だが、性格は明るく親密になれば楽しい相手で地下の妖怪たちの人気者であり、『地霊殿』作中では洞窟に乗り込んだ霊夢たちにも気さくな口調で話しかけている。また、戦うことを厭わず好戦的だが、大勢の人間を相手にすれば勝ち目がないことも理解している。
+    建築が得意とされ、地上の妖怪からの依頼を受けて夜の間に地上に現れ、一晩のうちに建築作業を行い、再び地底へと戻っていくという[5]。河童の河城にとりからは「河を汚す」という理由で嫌われている[6]。
+
+#### 水橋 パルスィ（みずはし パルスィ）
+
+    [橋姫](/wiki/%E6%A9%8B%E5%A7%AB "橋姫")。地上と地下を結ぶ縦穴の番人で、穴を通過する者を見守る役割を持つ。非常に嫉妬深い性格で、『地霊殿』作中では地上の支援妖怪から「嫉妬の妖怪」や「下賤な妖怪」と呼ばれる。霊夢や魔理沙に対して、一方的に「妬ましい」と言いながら攻撃を仕掛けてくる。
+    『求聞口授』によれば、彼女の本質は「嫉妬の感情」そのものであり、他人の嫉妬心を煽ることでその生活が崩壊する様を見るのを喜びとしている。また、他者から嫉妬を受けたり、あるいは彼女自身が他者に嫉妬する場合にも力を得ることができる。意地の悪い性格であり、直接、相対している際には普通に明るく会話をするが、裏ではその相手の陰口を叩いたり逆恨みしたりするため、嫌われることが多い。ただし、旧地獄には嫌われ者同士の仲間も多いという[7]。
+
+#### 星熊 勇儀（ほしぐま ゆうぎ）
+
+    旧都に住む[鬼](/wiki/%E9%AC%BC "鬼")。額に一本の赤い角が生えており、角の上面には黄色い星のマークがついている。『地霊殿』では体操服の上部分に半透明のスカートを着用しているが、黄昏フロンティア作品では肩と胸をはだけさせた着物姿で登場している。
+    『地霊殿』では、地底に現れた博麗霊夢や霧雨魔理沙に興味を持ち、力試しと称して対戦する。酒を一滴もこぼさずに戦うルールを自分に課して、遊びながら戦っている[8]。対戦後は異変に関する情報を提供し、地霊殿へ案内する。
+    かつては妖怪の山に住んでおり、伊吹萃香らとともに「山の四天王」と呼ばれ、天狗や河童を従え一大社会を築いていた。しかし、人間との関係の悪化を憂い、同じく地上に嫌気の差した他の鬼たちと共に、突然姿を消す。その後、地獄の「経営のスリム化」の一環として切り捨てられ、廃墟となった旧地獄跡に移り住み、同じくその能力の危険性などから忌み嫌われた他の妖怪たちと共に地下都市を再建する。後に、地上の賢者との間に「地上と地底の妖怪同士の相互不可侵」「旧地獄の怨霊の管理」などの約束を結び自治を認められ、現在に至る。
```

---

## ⏰ 12:59:58 - `76c8e92`
**🔧 .gitignoreにuv.lockを追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 12:59:58 2025 +0900
M	.gitignore
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 12:59:58 2025 +0900

    🔧 .gitignoreにuv.lockを追加
    
    - uv.lockファイルをGit管理から除外
    - 依存関係のロックファイルは環境固有のため除外対象に設定

 .gitignore | 1 +
 1 file changed, 1 insertion(+)
```

### 💻 Code Changes
```diff
diff --git a/.gitignore b/.gitignore
index 16c3c78..ca9a856 100644
--- a/.gitignore
+++ b/.gitignore
@@ -206,3 +206,4 @@ marimo/_static/
 marimo/_lsp/
 __marimo__/
 .SourceSageAssets/
+uv.lock
```

---

## ⏰ 13:00:17 - `2d64370`
**🔀 Merge: Easy Dataset CLI初期実装完了**
*by Maki*

### 📋 Changed Files
```bash
Merge: d8aa5b3 76c8e92
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:00:17 2025 +0900
```

### 📊 Statistics
```bash
Merge: d8aa5b3 76c8e92
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:00:17 2025 +0900

    🔀 Merge: Easy Dataset CLI初期実装完了
    
    - READMEの完全書き換え（Daily Report Hub → Easy Dataset CLI）
    - プロジェクト設定ファイル（pyproject.toml）の追加
    - CLIコア機能の実装（main.py, core.py, prompts.py）
    - サンプルファイルとGA定義例の追加
    - .gitignore設定の更新

 .gitignore                            |   1 +
 README.md                             | 335 +++++++++++-----------------------
 easy_dataset_cli/__init__.py          |   1 +
 easy_dataset_cli/core.py              | 198 ++++++++++++++++++++
 easy_dataset_cli/main.py              | 174 ++++++++++++++++++
 easy_dataset_cli/prompts.py           |  80 ++++++++
 example/input/Touhou_Chireiden.md     | 203 ++++++++++++++++++++
 example/input/sample_document.txt     |  14 ++
 example/input/sample_ga_definition.md |  21 +++
 example/output/ga-definitions.md      |  25 +++
 example/output/ga_definitions.md      |  29 +++
 pyproject.toml                        |  20 ++
 12 files changed, 876 insertions(+), 225 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 13:42:31 - `4e7fae4`
**✨ プロンプトシステムの外部ファイル化**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:42:31 2025 +0900
M	easy_dataset_cli/prompts.py
A	easy_dataset_cli/prompts/ga_definition_generation.md
A	easy_dataset_cli/prompts/qa_generation.md
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:42:31 2025 +0900

    ✨ プロンプトシステムの外部ファイル化
    
    - プロンプトテンプレートをマークダウンファイルに分離
    - prompts.pyをテンプレート読み込み機能に変更
    - qa_generation.mdとga_definition_generation.mdを追加
    - 保守性と可読性の向上

 easy_dataset_cli/prompts.py                        | 89 +++++-----------------
 .../prompts/ga_definition_generation.md            | 47 ++++++++++++
 easy_dataset_cli/prompts/qa_generation.md          | 46 +++++++++++
 3 files changed, 110 insertions(+), 72 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/easy_dataset_cli/prompts.py b/easy_dataset_cli/prompts.py
index 6d4cc26..5b2c825 100644
--- a/easy_dataset_cli/prompts.py
+++ b/easy_dataset_cli/prompts.py
@@ -1,80 +1,25 @@
 # easy_dataset_cli/prompts.py
-"""LLMプロンプト定義"""
+"""LLMプロンプト定義とマークダウンファイル読み込み"""
 
-QA_GENERATION_PROMPT_WITH_GA_JA = """# 役割: Q&Aペア生成の専門家（体裁・読者対応版）
+from pathlib import Path
 
-あなたは、与えられた文章から高品質な質問と回答のペアを作成する専門家です。特に、指定された「体裁」と「読者」に合わせてスタイルを調整する能力に長けています。
 
-# 指示:
-1.  与えられた「文章」を注意深く読んでください。
-2.  指定された「目標とする体裁」と「目標とする読者」の役割になりきってください。
-3.  文章に書かれている情報**のみ**に基づいて、複数のユニークで洞察に富んだQ&Aペアを生成してください。
-4.  質問のスタイルと複雑さは、「目標とする読者」の視点に合わせてください。
-5.  回答のスタイル、トーン、詳細さは、「目標とする体裁」に合わせてください。
+def load_prompt_template(template_name: str) -> str:
+    """プロンプトテンプレートをマークダウンファイルから読み込む"""
+    prompt_dir = Path(__file__).parent / "prompts"
+    template_path = prompt_dir / f"{template_name}.md"
+    
+    if not template_path.exists():
+        raise FileNotFoundError(f"プロンプトテンプレートが見つかりません: {template_path}")
+    
+    return template_path.read_text(encoding="utf-8")
 
-# 目標とする体裁:
-{genre_title}
-{genre_description}
 
-# 目標とする読者:
-{audience_title}
-{audience_description}
+def get_qa_generation_prompt() -> str:
+    """Q&A生成プロンプトを取得"""
+    return load_prompt_template("qa_generation")
 
-# 文章:
----
-{context}
----
 
-# 出力形式:
-**必ず**、ルート要素が `<QAPairs>` である単一の有効なXMLとして応答してください。XML以外の説明文は一切含めないでください。
-各Q&Aペアは `<Pair>` タグで囲み、その中に `<Question>` と `<Answer>` タグを含めてください。
-
-# 出力例:
-<QAPairs>
-<Pair>
-<Question>ミトコンドリアの主な機能は何ですか？</Question>
-<Answer>ミトコンドリアの主な機能は、細胞のエネルギー通貨であるアデノシン三リン酸（ATP）の大部分を生成することです。</Answer>
-</Pair>
-<Pair>
-<Question>ATPは細胞内でどのように利用されますか？</Question>
-<Answer>ATPは細胞内の様々な化学反応のエネルギー源として利用されます。</Answer>
-</Pair>
-</QAPairs>
-
-それでは、Q&Aペアの生成を開始してください。"""
-
-
-GA_DEFINITION_GENERATION_PROMPT_JA = """# 役割: GA（Genre-Audience）ペア定義の専門家
-
-あなたは、与えられた文章の内容を分析し、最適なGenre（体裁）とAudience（読者）のペアを提案する専門家です。
-
-# 指示:
-1. 与えられた文章の内容、トピック、専門性レベルを分析してください。
-2. この文章から質問と回答のペアを生成する際に最適となる3-5個のGenre-Audienceペアを提案してください。
-3. 各Genreは異なる文体・形式（学術論文、技術ブログ、教科書、FAQ、対話形式など）を表現してください。
-4. 各Audienceは異なる知識レベル・立場（初心者、学生、専門家、実務者など）を表現してください。
-5. 文章の内容に適したペアを選択し、多様性を確保してください。
-
-# 文章:
----
-{context}
----
-
-# 出力形式:
-**必ず**、以下の形式のMarkdownとして出力してください。各ペアは `---` で区切ってください。
-
-# Genre: [体裁名]
-[体裁の詳細説明]
-
-# Audience: [読者名]
-[読者の詳細説明]
-
----
-
-# Genre: [体裁名2]
-[体裁の詳細説明2]
-
-# Audience: [読者名2]
-[読者の詳細説明2]
-
-それでは、最適なGA定義の生成を開始してください。"""
\ No newline at end of file
```

---

## ⏰ 13:42:43 - `6756ec8`
**🔧 GA定義生成のXML対応とエラーハンドリング強化**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:42:43 2025 +0900
M	easy_dataset_cli/core.py
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:42:43 2025 +0900

    🔧 GA定義生成のXML対応とエラーハンドリング強化
    
    - GA定義生成をXML形式に変更
    - XMLパース失敗時のフォールバック機能追加
    - parse_ga_definitions_from_xml関数の実装
    - 手動テキスト解析機能の追加
    - ログ出力とrawレスポンス保存機能

 easy_dataset_cli/core.py | 369 ++++++++++++++++++++++++++++++++++++++++++++---
 1 file changed, 345 insertions(+), 24 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/easy_dataset_cli/core.py b/easy_dataset_cli/core.py
index 0ed3e97..c9db332 100644
--- a/easy_dataset_cli/core.py
+++ b/easy_dataset_cli/core.py
@@ -13,7 +13,7 @@ from litellm import completion
 from rich.console import Console
 from dotenv import load_dotenv
 
-from .prompts import QA_GENERATION_PROMPT_WITH_GA_JA, GA_DEFINITION_GENERATION_PROMPT_JA
+from .prompts import get_qa_generation_prompt, get_ga_definition_generation_prompt
 
 # .envファイルを読み込む
 load_dotenv()
@@ -22,9 +22,74 @@ console = Console()
 
 
 def parse_ga_file(file_path: Path) -> List[Dict[str, Dict[str, str]]]:
-    """マークダウンファイルからGAペアのリストを解析する"""
+    """XMLファイルからGAペアのリストを解析する"""
     text = file_path.read_text(encoding="utf-8")
     pairs = []
+    console.print(f"[dim]GAファイルを読み込み中: {file_path}[/dim]")
+    console.print(f"[dim]ファイル内容長: {len(text)} 文字[/dim]")
+    
+    try:
+        # XMLから<GADefinitions>部分を抽出
+        xml_start = text.find("<GADefinitions>")
+        xml_end = text.rfind("</GADefinitions>")
+        console.print(f"[dim]XML開始位置: {xml_start}, 終了位置: {xml_end}[/dim]")
+        
+        if xml_start != -1 and xml_end != -1:
+            clean_xml = text[xml_start: xml_end + len("</GADefinitions>")]
+            console.print(f"[dim]抽出されたXML長: {len(clean_xml)} 文字[/dim]")
+            
+            root = ET.fromstring(clean_xml)
+            pair_nodes = root.findall('Pair')
+            console.print(f"[dim]見つかったPairノード数: {len(pair_nodes)}[/dim]")
+            
+            for i, pair_node in enumerate(pair_nodes):
+                genre_node = pair_node.find('Genre')
+                audience_node = pair_node.find('Audience')
+                
+                if genre_node is not None and audience_node is not None:
+                    genre_title_node = genre_node.find('Title')
+                    genre_desc_node = genre_node.find('Description')
+                    audience_title_node = audience_node.find('Title')
+                    audience_desc_node = audience_node.find('Description')
+                    
+                    has_all = all([
+                        genre_title_node is not None and genre_title_node.text and genre_title_node.text.strip(),
+                        genre_desc_node is not None and genre_desc_node.text and genre_desc_node.text.strip(),
+                        audience_title_node is not None and audience_title_node.text and audience_title_node.text.strip(),
+                        audience_desc_node is not None and audience_desc_node.text and audience_desc_node.text.strip()
+                    ])
+                    
+                    console.print(f"[dim]Pair {i+1}: {'✓' if has_all else '✗'} {genre_title_node.text if genre_title_node is not None else 'None'}[/dim]")
+                    
+                    if has_all:
+                        pairs.append({
+                            "genre": {
+                                "title": genre_title_node.text.strip(),
+                                "description": genre_desc_node.text.strip()
+                            },
+                            "audience": {
+                                "title": audience_title_node.text.strip(),
+                                "description": audience_desc_node.text.strip()
+                            }
+                        })
+        
+        # XMLが見つからない場合は従来のマークダウン形式で解析を試行
+        if not pairs:
+            console.print("[yellow]XMLからペアが見つからないため、マークダウン形式で再試行[/yellow]")
+            pairs = parse_ga_markdown_fallback(text)
+            
+    except ET.ParseError as e:
+        console.print(f"[yellow]XML解析エラー: {e}[/yellow]")
+        # XML解析に失敗した場合はマークダウン形式で解析を試行
+        pairs = parse_ga_markdown_fallback(text)
+    
+    console.print(f"[dim]最終的に解析されたペア数: {len(pairs)}[/dim]")
+    return pairs
+
+
+def parse_ga_markdown_fallback(text: str) -> List[Dict[str, Dict[str, str]]]:
+    """マークダウンファイルからGAペアのリストを解析する（フォールバック）"""
+    pairs = []
     sections = text.split('---')
     
     for section in sections:
@@ -71,19 +136,21 @@ def split_text(text: str, chunk_size: int, chunk_overlap: int) -> List[str]:
 
 
 def generate_qa_for_chunk_with_ga(
-    chunk: str, model: str, ga_pair: Dict[str, Dict[str, str]]
+    chunk: str, model: str, ga_pair: Dict[str, Dict[str, str]], logs_dir: Path = None, num_qa_pairs: int = None
 ) -> List[Dict[str, str]]:
     """litellmを使い、1つのチャンクと1つのGAペアからQ&Aペアのリストを生成する"""
-    prompt = QA_GENERATION_PROMPT_WITH_GA_JA.format(
+    prompt_template = get_qa_generation_prompt()
+    prompt = prompt_template.format(
```

---

## ⏰ 13:42:55 - `b34b8a0`
**🚀 CLIインターフェースの機能拡張**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:42:55 2025 +0900
M	easy_dataset_cli/main.py
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:42:55 2025 +0900

    🚀 CLIインターフェースの機能拡張
    
    - create-gaコマンドの出力ディレクトリ対応
    - num_ga_pairsとnum_qa_pairsオプション追加
    - ディレクトリ構造の自動作成機能
    - Genreごとのマークダウンファイル保存
    - ログディレクトリでのrawレスポンス管理

 easy_dataset_cli/main.py | 83 ++++++++++++++++++++++++++++++++++++++----------
 1 file changed, 66 insertions(+), 17 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/easy_dataset_cli/main.py b/easy_dataset_cli/main.py
index b15f7a6..28adbaf 100644
--- a/easy_dataset_cli/main.py
+++ b/easy_dataset_cli/main.py
@@ -13,7 +13,10 @@ from .core import (
     parse_ga_file,
     generate_qa_for_chunk_with_ga,
     convert_to_xml_by_genre,
-    generate_ga_definitions
+    generate_ga_definitions,
+    parse_ga_definitions_from_xml,
+    save_ga_definitions_by_genre,
+    create_output_directories
 )
 
 # .envファイルを読み込む
@@ -37,29 +40,64 @@ def create_ga(
         exists=True, dir_okay=False, readable=True,
         help="GAペアの定義を生成するための元のテキストファイル。"
     )],
-    output_path: Annotated[Path, typer.Option(
-        "--output", "-o", writable=True,
-        help="生成されたGAペア定義（Markdown）を保存するファイルパス。"
+    output_dir: Annotated[Path, typer.Option(
+        "--output-dir", "-o", file_okay=False, dir_okay=True, writable=True,
+        help="生成されたGAペア定義ファイルを保存するディレクトリ。"
     )],
     model: Annotated[str, typer.Option(
         "--model", "-m",
         help="GAペア定義の生成に使用するLLMモデル名。"
     )] = "openrouter/openai/gpt-4o",
+    num_ga_pairs: Annotated[int, typer.Option(
+        "--num-ga-pairs", "-g",
+        help="生成するGAペアの数。指定しない場合はLLMが適切な数を決定します。"
+    )] = None,
 ):
-    """元の文章を分析し、GAペア定義のMarkdownファイルを生成します。"""
+    """元の文章を分析し、GAペア定義をXML形式で生成し、Genreごとにマークダウンファイルに保存します。"""
     console.print(f"ファイルを読み込んでいます: [cyan]{file_path}[/cyan]")
 
     try:
         text = file_path.read_text(encoding="utf-8")
+        console.print(f"[dim]読み込んだテキスト長: {len(text)} 文字[/dim]")
+
+        console.print("[bold green]LLMに最適なGAペアを提案させています...[/bold green]")
+        xml_content = generate_ga_definitions(text, model=model, num_ga_pairs=num_ga_pairs)
+
+        # 出力ディレクトリ構造を作成
+        dirs = create_output_directories(output_dir)
+        console.print(f"[dim]出力ディレクトリを作成しました: ga/, logs/, qa/[/dim]")
+        
+        # LLMのrawレスポンスをlogsディレクトリに保存
+        raw_file_path = dirs["logs"] / "raw.md"
+        raw_file_path.write_text(xml_content, encoding="utf-8")
+        console.print(f"[green]✓[/green] LLMのrawレスポンスを保存しました: [cyan]{raw_file_path}[/cyan]")
+
+        console.print("[bold green]XMLからGAペアを解析しています...[/bold green]")
+        # XMLからGAペアを解析
+        ga_pairs = parse_ga_definitions_from_xml(xml_content)
+        
+        if not ga_pairs:
+            console.print("[bold red]有効なGAペアが生成されませんでした。[/bold red]")
+            console.print("[yellow]生成されたXMLの内容を確認してください:[/yellow]")
+            console.print(xml_content)
+            raise typer.Exit(code=1)
 
-        with console.status("[bold green]LLMに最適なGAペアを提案させています..."):
-            markdown_content = generate_ga_definitions(text, model=model)
+        # 元のXMLファイルをgaディレクトリに保存（クリーンなXMLのみ）
+        xml_file_path = dirs["ga"] / "ga_definitions.xml"
+        # XMLタグ部分のみを抽出して保存
+        xml_start = xml_content.find("<GADefinitions>")
+        xml_end = xml_content.rfind("</GADefinitions>")
+        if xml_start != -1 and xml_end != -1:
+            clean_xml = xml_content[xml_start: xml_end + len("</GADefinitions>")]
+            xml_file_path.write_text(clean_xml, encoding="utf-8")
+            console.print(f"[green]✓[/green] GA定義XMLファイルを保存しました: [cyan]{xml_file_path}[/cyan]")
 
-        output_path.write_text(markdown_content, encoding="utf-8")
+        # Genreごとにマークダウンファイルをgaディレクトリに保存
+        save_ga_definitions_by_genre(ga_pairs, dirs["ga"])
 
         console.print(
-            f"\n[bold green]✓[/bold green] GAペア定義ファイルを "
-            f"[cyan]{output_path}[/cyan] に正常に保存しました。"
+            f"\n[bold green]✓[/bold green] {len(ga_pairs)}個のGAペアを "
+            f"[cyan]{dirs['ga']}[/cyan] に保存しました。"
         )
         console.print(
             "[yellow]ヒント: 生成されたファイルをレビューし、必要に応じて編集してから "
@@ -81,7 +119,7 @@ def generate(
     )],
     ga_file: Annotated[Path, typer.Option(
         "--ga-file", "-g", exists=True, dir_okay=False, readable=True,
-        help="Genre-Audienceペアを定義したMarkdownファイルへのパス。"
+        help="Genre-Audienceペアを定義したXMLまたはMarkdownファイルへのパス。gaディレクトリのga_definitions.xmlを推奨。"
     )],
     output_dir: Annotated[Path, typer.Option(
         "--output-dir", "-o", file_okay=False, dir_okay=True, writable=True,
@@ -97,6 +135,10 @@ def generate(
```

---

## ⏰ 13:43:05 - `a3909a0`
**📦 ユーティリティ機能の追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:43:05 2025 +0900
A	easy_dataset_cli/utils.py
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:43:05 2025 +0900

    📦 ユーティリティ機能の追加
    
    - utils.pyファイルの新規作成
    - 共通機能の分離とモジュール化
    - コードの再利用性向上

 easy_dataset_cli/utils.py | 42 ++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 42 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/easy_dataset_cli/utils.py b/easy_dataset_cli/utils.py
new file mode 100644
index 0000000..9256725
--- /dev/null
+++ b/easy_dataset_cli/utils.py
@@ -0,0 +1,42 @@
+# easy_dataset_cli/utils.py
+"""ユーティリティ関数"""
+
+import xml.etree.ElementTree as ET
+from xml.dom import minidom
+from pathlib import Path
+from typing import List, Dict
+from .core import parse_ga_markdown_fallback
+
+
+def convert_markdown_ga_to_xml(markdown_file: Path, xml_file: Path) -> None:
+    """マークダウン形式のGA定義ファイルをXML形式に変換する"""
+    text = markdown_file.read_text(encoding="utf-8")
+    ga_pairs = parse_ga_markdown_fallback(text)
+    
+    if not ga_pairs:
+        raise ValueError("有効なGAペアが見つかりませんでした")
+    
+    # XMLを構築
+    root = ET.Element("GADefinitions")
+    
+    for pair in ga_pairs:
+        pair_elem = ET.SubElement(root, "Pair")
+        
+        genre_elem = ET.SubElement(pair_elem, "Genre")
+        genre_title_elem = ET.SubElement(genre_elem, "Title")
+        genre_title_elem.text = pair['genre']['title']
+        genre_desc_elem = ET.SubElement(genre_elem, "Description")
+        genre_desc_elem.text = pair['genre']['description']
+        
+        audience_elem = ET.SubElement(pair_elem, "Audience")
+        audience_title_elem = ET.SubElement(audience_elem, "Title")
+        audience_title_elem.text = pair['audience']['title']
+        audience_desc_elem = ET.SubElement(audience_elem, "Description")
+        audience_desc_elem.text = pair['audience']['description']
+    
+    # 整形されたXMLとして保存
+    rough_string = ET.tostring(root, 'utf-8')
+    reparsed = minidom.parseString(rough_string)
+    xml_content = reparsed.toprettyxml(indent="  ")
+    
+    xml_file.write_text(xml_content, encoding="utf-8")
\ No newline at end of file
```

---

## ⏰ 13:43:17 - `88b68f5`
**🗑️ サンプルファイルの整理とディレクトリ構造改善**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:43:17 2025 +0900
R100	example/input/Touhou_Chireiden.md	example/input/documents/Touhou_Chireiden.md
R100	example/input/sample_document.txt	example/input/documents/sample_document.txt
R100	example/input/sample_ga_definition.md	example/input/documents/sample_ga_definition.md
A	example/input/documents/test_short.md
D	example/output/ga-definitions.md
D	example/output/ga_definitions.md
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:43:17 2025 +0900

    🗑️ サンプルファイルの整理とディレクトリ構造改善
    
    - 古いサンプルファイルの削除
    - example/input/documents/ディレクトリの追加
    - プロジェクト構造のクリーンアップ
    - 新しいディレクトリ構造への対応

 example/input/{ => documents}/Touhou_Chireiden.md  |  0
 example/input/{ => documents}/sample_document.txt  |  0
 .../input/{ => documents}/sample_ga_definition.md  |  0
 example/input/documents/test_short.md              | 16 ++++++++++++
 example/output/ga-definitions.md                   | 25 -------------------
 example/output/ga_definitions.md                   | 29 ----------------------
 6 files changed, 16 insertions(+), 54 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/example/input/Touhou_Chireiden.md b/example/input/documents/Touhou_Chireiden.md
similarity index 100%
rename from example/input/Touhou_Chireiden.md
rename to example/input/documents/Touhou_Chireiden.md
diff --git a/example/input/sample_document.txt b/example/input/documents/sample_document.txt
similarity index 100%
rename from example/input/sample_document.txt
rename to example/input/documents/sample_document.txt
diff --git a/example/input/sample_ga_definition.md b/example/input/documents/sample_ga_definition.md
similarity index 100%
rename from example/input/sample_ga_definition.md
rename to example/input/documents/sample_ga_definition.md
diff --git a/example/input/documents/test_short.md b/example/input/documents/test_short.md
new file mode 100644
index 0000000..4907c11
--- /dev/null
+++ b/example/input/documents/test_short.md
@@ -0,0 +1,16 @@
+# テストドキュメント
+
+## 概要
+これは短いテストドキュメントです。Q&A生成のテスト用に作成されました。
+
+## 内容
+このドキュメントには以下の情報が含まれています：
+- テストの目的
+- 簡単な説明
+- 基本的な情報
+
+## 詳細
+テストドキュメントは、システムが正常に動作することを確認するために使用されます。短い内容なので、処理時間も短縮されます。
+
+## まとめ
+このテストにより、Q&A生成システムの基本機能を検証できます。
diff --git a/example/output/ga-definitions.md b/example/output/ga-definitions.md
deleted file mode 100644
index d566352..0000000
--- a/example/output/ga-definitions.md
+++ /dev/null
@@ -1,25 +0,0 @@
-以下に「東方地霊殿 〜 Subterranean Animism.」に関する3つのGenre-Audienceペアを提案します。
-
----
-
-# Genre: FAQ
-ユーザーがゲームに関する特定の質問に素早くアクセスできるような形式で、よくある質問に対する回答を簡潔にまとめる。
-
-# Audience: 初心者ゲーマー
-東方Projectや弾幕系シューティングゲームを初めてプレイする人々。ゲームの基本的な情報や攻略のヒントが欲しい。
-
----
-
-# Genre: テクニカルガイド
-ゲームシステム、必要環境、インストール方法などの技術的な詳細を説明する形式。特に技術的な詳細に焦点を当てる。
-
-# Audience: PCゲーミング愛好者
-PCでのゲームプレイに慣れているが、特に東方シリーズに関する技術的な詳細とトラブルシューティングガイドが求められる愛好者。
-
----
-
-# Genre: 学術論文
-ゲームの世界観、キャラクター、物語構成について深く分析し、詳細に記述する形式。ストーリーやキャラクターの背景を探究する。
-
-# Audience: ゲームデザイン学生
-ストーリーやキャラクターの構築、世界観の設定について学んでいる学生。ゲームデザインにおけるテーマと物語の意義を理解したい。
\ No newline at end of file
diff --git a/example/output/ga_definitions.md b/example/output/ga_definitions.md
deleted file mode 100644
index 17de7f3..0000000
--- a/example/output/ga_definitions.md
+++ /dev/null
@@ -1,29 +0,0 @@
-# Genre: 学術論文
-学術的で厳密な表現を用い、専門用語を正確に使用し、論理的で客観的な回答を提供します。引用や根拠を重視し、研究者間での議論に適した形式で情報を整理します。
-
-# Audience: 大学生
-大学レベルの知識を持つ学習者向けに、基礎概念から応用まで段階的に説明します。専門用語は使用しますが、適切な説明を加えて理解を促進します。
-
----
-
-# Genre: 技術ブログ
-実践的で親しみやすい表現を用い、具体例やコード例を交えて説明します。読者の関心を引く工夫を凝らし、実務に役立つ情報を提供します。
-
-# Audience: エンジニア
-実務経験のある開発者向けに、実装の詳細や最適化のポイントを重視した内容を提供します。技術的な深掘りと実践的なアドバイスを含めます。
-
----
-
-# Genre: 教科書
-体系的で網羅的な説明を行い、学習の順序を考慮した構成で知識を整理します。定義、例、練習問題を含む教育的なアプローチを採用します。
-
-# Audience: 初心者
-プログラミングや技術分野の初学者向けに、基本概念から丁寧に解説します。専門用語は最小限に抑え、分かりやすい例を多用します。
-
----
-
-# Genre: FAQ
-よくある質問と回答の形式で、簡潔で実用的な情報を提供します。問題解決に焦点を当て、すぐに使える答えを提示します。
-
-# Audience: 実務者
```

---

## ⏰ 13:43:27 - `a1dd9f6`
**🔧 .gitignoreファイルの更新**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:43:27 2025 +0900
M	.gitignore
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:43:27 2025 +0900

    🔧 .gitignoreファイルの更新
    
    - 新しいディレクトリ構造に対応
    - 不要なファイルの除外設定追加
    - プロジェクト管理の改善

 .gitignore | 1 +
 1 file changed, 1 insertion(+)
```

### 💻 Code Changes
```diff
diff --git a/.gitignore b/.gitignore
index ca9a856..ba4f0f5 100644
--- a/.gitignore
+++ b/.gitignore
@@ -207,3 +207,4 @@ marimo/_lsp/
 __marimo__/
 .SourceSageAssets/
 uv.lock
+example/output/structured/logs/
```

---

## ⏰ 13:43:48 - `f4292b4`
**🔀 Merge: プロンプトシステムリファクタリングとXML対応機能**
*by Maki*

### 📋 Changed Files
```bash
Merge: 2d64370 a1dd9f6
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:43:48 2025 +0900
```

### 📊 Statistics
```bash
Merge: 2d64370 a1dd9f6
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:43:48 2025 +0900

    🔀 Merge: プロンプトシステムリファクタリングとXML対応機能
    
    - プロンプトテンプレートの外部ファイル化
    - GA定義生成のXML形式対応
    - エラーハンドリングとフォールバック機能強化
    - CLIインターフェースの機能拡張
    - ディレクトリ構造の改善とファイル整理

 .gitignore                                         |   1 +
 easy_dataset_cli/core.py                           | 369 +++++++++++++++++++--
 easy_dataset_cli/main.py                           |  83 ++++-
 easy_dataset_cli/prompts.py                        |  89 +----
 .../prompts/ga_definition_generation.md            |  47 +++
 easy_dataset_cli/prompts/qa_generation.md          |  46 +++
 easy_dataset_cli/utils.py                          |  42 +++
 example/input/{ => documents}/Touhou_Chireiden.md  |   0
 example/input/{ => documents}/sample_document.txt  |   0
 .../input/{ => documents}/sample_ga_definition.md  |   0
 example/input/documents/test_short.md              |  16 +
 example/output/ga-definitions.md                   |  25 --
 example/output/ga_definitions.md                   |  29 --
 13 files changed, 580 insertions(+), 167 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 13:51:58 - `dc2aa8f`
**Merge branch 'develop'**
*by Maki*

### 📋 Changed Files
```bash
Merge: d8aa5b3 f4292b4
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:51:58 2025 +0900
```

### 📊 Statistics
```bash
Merge: d8aa5b3 f4292b4
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 13:51:58 2025 +0900

    Merge branch 'develop'

 .gitignore                                         |   2 +
 README.md                                          | 335 +++++--------
 easy_dataset_cli/__init__.py                       |   1 +
 easy_dataset_cli/core.py                           | 519 +++++++++++++++++++++
 easy_dataset_cli/main.py                           | 223 +++++++++
 easy_dataset_cli/prompts.py                        |  25 +
 .../prompts/ga_definition_generation.md            |  47 ++
 easy_dataset_cli/prompts/qa_generation.md          |  46 ++
 easy_dataset_cli/utils.py                          |  42 ++
 example/input/documents/Touhou_Chireiden.md        | 203 ++++++++
 example/input/documents/sample_document.txt        |  14 +
 example/input/documents/sample_ga_definition.md    |  21 +
 example/input/documents/test_short.md              |  16 +
 pyproject.toml                                     |  20 +
 14 files changed, 1289 insertions(+), 225 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 14:28:29 - `2d451e0`
**✨ モジュラーアーキテクチャの実装**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 14:28:29 2025 +0900
A	easy_dataset_cli/file_utils.py
A	easy_dataset_cli/ga_parser.py
A	easy_dataset_cli/qa_generator.py
A	easy_dataset_cli/text_splitter.py
A	easy_dataset_cli/xml_utils.py
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 14:28:29 2025 +0900

    ✨ モジュラーアーキテクチャの実装
    
    - file_utils.py: ファイル操作とディレクトリ管理機能を分離
    - ga_parser.py: GA定義ファイルの解析機能を独立化
    - qa_generator.py: Q&A生成ロジックを専用モジュールに分離
    - text_splitter.py: テキスト分割機能を独立したモジュールに
    - xml_utils.py: XML処理機能を専用モジュールに分離

 easy_dataset_cli/file_utils.py    |  59 +++++++++++
 easy_dataset_cli/ga_parser.py     | 182 +++++++++++++++++++++++++++++++++
 easy_dataset_cli/qa_generator.py  | 209 ++++++++++++++++++++++++++++++++++++++
 easy_dataset_cli/text_splitter.py |  17 ++++
 easy_dataset_cli/xml_utils.py     | 154 ++++++++++++++++++++++++++++
 5 files changed, 621 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/easy_dataset_cli/file_utils.py b/easy_dataset_cli/file_utils.py
new file mode 100644
index 0000000..f42280a
--- /dev/null
+++ b/easy_dataset_cli/file_utils.py
@@ -0,0 +1,59 @@
+# easy_dataset_cli/file_utils.py
+"""ファイル操作関連のユーティリティ"""
+
+from pathlib import Path
+from typing import Dict, List
+from collections import defaultdict
+from rich.console import Console
+
+console = Console()
+
+
+def create_output_directories(base_dir: Path) -> Dict[str, Path]:
+    """出力用のディレクトリ構造を作成する"""
+    directories = {
+        "base": base_dir,
+        "ga": base_dir / "ga",
+        "logs": base_dir / "logs",
+        "qa": base_dir / "qa"
+    }
+
+    for dir_path in directories.values():
+        dir_path.mkdir(parents=True, exist_ok=True)
+
+    return directories
+
+
+def save_ga_definitions_by_genre(ga_pairs: List[Dict[str, Dict[str, str]]], ga_dir: Path) -> None:
+    """GAペアをGenreごとにマークダウンファイルに保存する"""
+    genre_groups = defaultdict(list)
+
+    # Genreごとにグループ化
+    for pair in ga_pairs:
+        genre_title = pair['genre']['title']
+        genre_groups[genre_title].append(pair)
+
+    # 各Genreごとにファイルを作成
+    for genre_title, pairs in genre_groups.items():
+        # ファイル名に使用できない文字を置換
+        safe_filename = "".join(c for c in genre_title if c.isalnum() or c in (' ', '-', '_')).rstrip()
+        safe_filename = safe_filename.replace(' ', '_').lower()
+
+        file_path = ga_dir / f"ga_definitions_{safe_filename}.md"
+
+        content = f"# {genre_title}\n\n"
+
+        for pair in pairs:
+            content += f"## Genre: {pair['genre']['title']}\n"
+            content += f"{pair['genre']['description']}\n\n"
+            content += f"## Audience: {pair['audience']['title']}\n"
+            content += f"{pair['audience']['description']}\n\n"
+            content += "---\n\n"
+
+        file_path.write_text(content, encoding="utf-8")
+        console.print(f"[green]GA定義を保存しました:[/green] {file_path}")
+
+
+def sanitize_filename(name: str) -> str:
+    """ファイル名として安全な文字列に変換する"""
+    return "".join(c for c in name if c.isalnum() or c in (' ', '_', '-')).rstrip()
diff --git a/easy_dataset_cli/ga_parser.py b/easy_dataset_cli/ga_parser.py
new file mode 100644
index 0000000..fb9aa16
--- /dev/null
+++ b/easy_dataset_cli/ga_parser.py
@@ -0,0 +1,182 @@
+# easy_dataset_cli/ga_parser.py
+"""GA定義の解析関連機能"""
+
+import xml.etree.ElementTree as ET
+from pathlib import Path
+from typing import List, Dict
+import mistune
+from rich.console import Console
+
+console = Console()
+
+
+def parse_ga_file(file_path: Path) -> List[Dict[str, Dict[str, str]]]:
+    """XMLファイルからGAペアのリストを解析する"""
+    text = file_path.read_text(encoding="utf-8")
+    pairs = []
+    console.print(f"[dim]GAファイルを読み込み中: {file_path}[/dim]")
+    console.print(f"[dim]ファイル内容長: {len(text)} 文字[/dim]")
+
+    try:
+        # XMLから<GADefinitions>部分を抽出
+        xml_start = text.find("<GADefinitions>")
+        xml_end = text.rfind("</GADefinitions>")
+        console.print(f"[dim]XML開始位置: {xml_start}, 終了位置: {xml_end}[/dim]")
+
+        if xml_start != -1 and xml_end != -1:
+            clean_xml = text[xml_start: xml_end + len("</GADefinitions>")]
+            console.print(f"[dim]抽出されたXML長: {len(clean_xml)} 文字[/dim]")
+
```

---

## ⏰ 14:28:45 - `186a7d6`
**✨ 全文コンテキスト対応プロンプトテンプレートを追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 14:28:45 2025 +0900
A	easy_dataset_cli/prompts/qa_generation_with_fulltext.md
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 14:28:45 2025 +0900

    ✨ 全文コンテキスト対応プロンプトテンプレートを追加
    
    - qa_generation_with_fulltext.md: 全文をコンテキストとして含めるQ&A生成用プロンプト
    - より文脈を理解した高品質なQ&Aペア生成を可能にする
    - チャンクと全文の両方を活用した生成ロジックに対応

 .../prompts/qa_generation_with_fulltext.md         | 52 ++++++++++++++++++++++
 1 file changed, 52 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/easy_dataset_cli/prompts/qa_generation_with_fulltext.md b/easy_dataset_cli/prompts/qa_generation_with_fulltext.md
new file mode 100644
index 0000000..a41ae1f
--- /dev/null
+++ b/easy_dataset_cli/prompts/qa_generation_with_fulltext.md
@@ -0,0 +1,52 @@
+# 役割: Q&Aペア生成の専門家（全文+チャンク対応版）
+
+あなたは、与えられた文章から高品質な質問と回答のペアを作成する専門家です。特に、指定された「体裁」と「読者」に合わせてスタイルを調整する能力に長けています。
+
+## 指示:
+1. 与えられた「全文」と「チャンク」を注意深く読んでください。
+2. 指定された「目標とする体裁」と「目標とする読者」の役割になりきってください。
+3. **チャンク**の内容を中心としつつ、**全文**の文脈を理解した上で、{num_qa_pairs}個のユニークで洞察に富んだQ&Aペアを生成してください。
+4. 質問のスタイルと複雑さは、「目標とする読者」の視点に合わせてください。
+5. 回答のスタイル、トーン、詳細さは、「目標とする体裁」に合わせてください。
+6. **重要**: 質問と回答は主に「チャンク」の内容に基づいて作成し、「全文」は文脈理解のための補助情報として活用してください。
+
+## 目標とする体裁:
+{genre_title}
+{genre_description}
+
+## 目標とする読者:
+{audience_title}
+{audience_description}
+
+## 全文（文脈理解用）:
+---
+{full_text}
+---
+
+## チャンク（QA生成対象）:
+---
+{chunk}
+---
+
+## 出力形式:
+**必ず**、ルート要素が `<QAPairs>` である単一の有効なXMLとして応答してください。XML以外の説明文は一切含めないでください。
+各Q&Aペアは `<Pair>` タグで囲み、その中に `<Question>` と `<Answer>` タグを含めてください。
+
+**重要**: XMLの特殊文字（&, <, >, ", '）は適切にエスケープしてください（例：& → &amp;, < → &lt;）。
+回答文に改行を含めず、一行で記述してください。
+
+## 出力例:
+\```xml
+<QAPairs>
+<Pair>
+<Question>ミトコンドリアの主な機能は何ですか？</Question>
+<Answer>ミトコンドリアの主な機能は、細胞のエネルギー通貨であるアデノシン三リン酸（ATP）の大部分を生成することです。</Answer>
+</Pair>
+<Pair>
+<Question>ATPは細胞内でどのように利用されますか？</Question>
+<Answer>ATPは細胞内の様々な化学反応のエネルギー源として利用されます。</Answer>
+</Pair>
+</QAPairs>
+\```
+
+それでは、Q&Aペアの生成を開始してください。
```

---

## ⏰ 14:28:58 - `6bab4e6`
**🔧 core.pyをモジュラーアーキテクチャに対応**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 14:28:58 2025 +0900
M	easy_dataset_cli/core.py
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 14:28:58 2025 +0900

    🔧 core.pyをモジュラーアーキテクチャに対応
    
    - 560行のモノリシックなコードを43行の統合インターフェースに簡素化
    - 各機能を専用モジュールから再エクスポートする構造に変更
    - 後方互換性を維持しながらコードの保守性を大幅に向上
    - 機能別モジュール分割により開発効率とテスト容易性を改善

 easy_dataset_cli/core.py | 560 ++++-------------------------------------------
 1 file changed, 42 insertions(+), 518 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/easy_dataset_cli/core.py b/easy_dataset_cli/core.py
index c9db332..2599497 100644
--- a/easy_dataset_cli/core.py
+++ b/easy_dataset_cli/core.py
@@ -1,519 +1,43 @@
 # easy_dataset_cli/core.py
-"""コアロジック: テキスト分割、Q&A生成、XML変換"""
-
-import os
-import xml.etree.ElementTree as ET
-from xml.dom import minidom
-from collections import defaultdict
-from pathlib import Path
-from typing import List, Dict
-import mistune
-from langchain_text_splitters import RecursiveCharacterTextSplitter
-from litellm import completion
-from rich.console import Console
-from dotenv import load_dotenv
-
-from .prompts import get_qa_generation_prompt, get_ga_definition_generation_prompt
-
-# .envファイルを読み込む
-load_dotenv()
-
-console = Console()
-
-
-def parse_ga_file(file_path: Path) -> List[Dict[str, Dict[str, str]]]:
-    """XMLファイルからGAペアのリストを解析する"""
-    text = file_path.read_text(encoding="utf-8")
-    pairs = []
-    console.print(f"[dim]GAファイルを読み込み中: {file_path}[/dim]")
-    console.print(f"[dim]ファイル内容長: {len(text)} 文字[/dim]")
-    
-    try:
-        # XMLから<GADefinitions>部分を抽出
-        xml_start = text.find("<GADefinitions>")
-        xml_end = text.rfind("</GADefinitions>")
-        console.print(f"[dim]XML開始位置: {xml_start}, 終了位置: {xml_end}[/dim]")
-        
-        if xml_start != -1 and xml_end != -1:
-            clean_xml = text[xml_start: xml_end + len("</GADefinitions>")]
-            console.print(f"[dim]抽出されたXML長: {len(clean_xml)} 文字[/dim]")
-            
-            root = ET.fromstring(clean_xml)
-            pair_nodes = root.findall('Pair')
-            console.print(f"[dim]見つかったPairノード数: {len(pair_nodes)}[/dim]")
-            
-            for i, pair_node in enumerate(pair_nodes):
-                genre_node = pair_node.find('Genre')
-                audience_node = pair_node.find('Audience')
-                
-                if genre_node is not None and audience_node is not None:
-                    genre_title_node = genre_node.find('Title')
-                    genre_desc_node = genre_node.find('Description')
-                    audience_title_node = audience_node.find('Title')
-                    audience_desc_node = audience_node.find('Description')
-                    
-                    has_all = all([
-                        genre_title_node is not None and genre_title_node.text and genre_title_node.text.strip(),
-                        genre_desc_node is not None and genre_desc_node.text and genre_desc_node.text.strip(),
-                        audience_title_node is not None and audience_title_node.text and audience_title_node.text.strip(),
-                        audience_desc_node is not None and audience_desc_node.text and audience_desc_node.text.strip()
-                    ])
-                    
-                    console.print(f"[dim]Pair {i+1}: {'✓' if has_all else '✗'} {genre_title_node.text if genre_title_node is not None else 'None'}[/dim]")
-                    
-                    if has_all:
-                        pairs.append({
-                            "genre": {
-                                "title": genre_title_node.text.strip(),
-                                "description": genre_desc_node.text.strip()
-                            },
-                            "audience": {
-                                "title": audience_title_node.text.strip(),
-                                "description": audience_desc_node.text.strip()
-                            }
-                        })
-        
-        # XMLが見つからない場合は従来のマークダウン形式で解析を試行
-        if not pairs:
-            console.print("[yellow]XMLからペアが見つからないため、マークダウン形式で再試行[/yellow]")
-            pairs = parse_ga_markdown_fallback(text)
-            
-    except ET.ParseError as e:
-        console.print(f"[yellow]XML解析エラー: {e}[/yellow]")
-        # XML解析に失敗した場合はマークダウン形式で解析を試行
-        pairs = parse_ga_markdown_fallback(text)
-    
-    console.print(f"[dim]最終的に解析されたペア数: {len(pairs)}[/dim]")
-    return pairs
-
-
-def parse_ga_markdown_fallback(text: str) -> List[Dict[str, Dict[str, str]]]:
-    """マークダウンファイルからGAペアのリストを解析する（フォールバック）"""
-    pairs = []
-    sections = text.split('---')
-    
-    for section in sections:
```

---

## ⏰ 14:29:16 - `a24a0d9`
**🚀 CLIインターフェースに全文コンテキスト機能を追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 14:29:16 2025 +0900
M	easy_dataset_cli/main.py
M	easy_dataset_cli/prompts.py
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 14:29:16 2025 +0900

    🚀 CLIインターフェースに全文コンテキスト機能を追加
    
    - --use-fulltextオプションを追加し、全文をコンテキストとして含めるQ&A生成に対応
    - デフォルトのGAペア数とQ&Aペア数を設定し、ユーザビリティを向上
    - デフォルトモデルをgpt-oss-120bに変更してコスト効率を改善
    - 全文モード使用時の警告表示とコスト注意喚起を実装
    - prompts.pyに全文対応プロンプト読み込み機能を追加

 easy_dataset_cli/main.py    | 50 +++++++++++++++++++++++++++++++--------------
 easy_dataset_cli/prompts.py |  5 +++++
 2 files changed, 40 insertions(+), 15 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/easy_dataset_cli/main.py b/easy_dataset_cli/main.py
index 28adbaf..6d7e897 100644
--- a/easy_dataset_cli/main.py
+++ b/easy_dataset_cli/main.py
@@ -12,11 +12,13 @@ from .core import (
     split_text,
     parse_ga_file,
     generate_qa_for_chunk_with_ga,
+    generate_qa_for_chunk_with_ga_and_fulltext,
     convert_to_xml_by_genre,
     generate_ga_definitions,
     parse_ga_definitions_from_xml,
     save_ga_definitions_by_genre,
-    create_output_directories
+    create_output_directories,
+    sanitize_filename
 )
 
 # .envファイルを読み込む
@@ -29,11 +31,6 @@ app = typer.Typer(
 console = Console()
 
 
-def sanitize_filename(name: str) -> str:
-    """ファイル名として安全な文字列に変換する"""
-    return "".join(c for c in name if c.isalnum() or c in (' ', '_', '-')).rstrip()
-
-
 @app.command()
 def create_ga(
     file_path: Annotated[Path, typer.Argument(
@@ -47,11 +44,11 @@ def create_ga(
     model: Annotated[str, typer.Option(
         "--model", "-m",
         help="GAペア定義の生成に使用するLLMモデル名。"
-    )] = "openrouter/openai/gpt-4o",
+    )] = "openrouter/openai/gpt-oss-120b",
     num_ga_pairs: Annotated[int, typer.Option(
         "--num-ga-pairs", "-g",
         help="生成するGAペアの数。指定しない場合はLLMが適切な数を決定します。"
-    )] = None,
+    )] = 5,
 ):
     """元の文章を分析し、GAペア定義をXML形式で生成し、Genreごとにマークダウンファイルに保存します。"""
     console.print(f"ファイルを読み込んでいます: [cyan]{file_path}[/cyan]")
@@ -138,9 +135,17 @@ def generate(
     num_qa_pairs: Annotated[int, typer.Option(
         "--num-qa-pairs", "-q",
         help="各チャンク・GAペアの組み合わせで生成するQ&Aペアの数。指定しない場合はLLMが適切な数を決定します。"
-    )] = None,
+    )] = 10,
+    use_fulltext: Annotated[bool, typer.Option(
+        "--use-fulltext", "-f",
+        help="全文をコンテキストとして含めてQA生成を行います。より文脈を理解したQAが生成されますが、処理時間とコストが増加します。"
+    )] = False,
 ):
-    """テキストファイルとGA定義からQ&Aペアを生成し、Genre別のXMLファイルとして出力します。"""
+    """テキストファイルとGA定義からQ&Aペアを生成し、Genre別のXMLファイルとして出力します。
+    
+    --use-fulltextオプションを使用すると、各チャンクの処理時に全文をコンテキストとして含めることで、
+    より文脈を理解した高品質なQ&Aペアを生成できます。ただし、処理時間とAPIコストが増加します。
+    """
     try:
         console.print(f"ファイルを読み込んでいます: [cyan]{file_path}[/cyan]")
         text = file_path.read_text(encoding="utf-8")
@@ -167,16 +172,31 @@ def generate(
             dirs = create_output_directories(output_dir)
             console.print(f"[dim]出力ディレクトリを作成しました: ga/, logs/, qa/[/dim]")
 
+        # 全文使用の場合は警告を表示
+        if use_fulltext:
+            console.print("[yellow]⚠ 全文コンテキストモードが有効です。処理時間とコストが増加する可能性があります。[/yellow]")
+            console.print(f"[dim]全文長: {len(text)} 文字[/dim]")
+
         with Progress(console=console) as progress:
             task = progress.add_task("[green]Q&Aペアを生成中...", total=total_tasks)
 
             for chunk in chunks:
                 for ga_pair in ga_pairs:
-                    qa_pairs = generate_qa_for_chunk_with_ga(
-                        chunk, model=model, ga_pair=ga_pair, 
-                        logs_dir=dirs["logs"] if dirs else None,
-                        num_qa_pairs=num_qa_pairs
-                    )
+                    if use_fulltext:
+                        qa_pairs = generate_qa_for_chunk_with_ga_and_fulltext(
+                            chunk=chunk,
+                            full_text=text,
+                            model=model,
+                            ga_pair=ga_pair,
+                            logs_dir=dirs["logs"] if dirs else None,
+                            num_qa_pairs=num_qa_pairs
+                        )
+                    else:
+                        qa_pairs = generate_qa_for_chunk_with_ga(
+                            chunk, model=model, ga_pair=ga_pair,
+                            logs_dir=dirs["logs"] if dirs else None,
+                            num_qa_pairs=num_qa_pairs
+                        )
 
```

---

## ⏰ 14:29:29 - `409055d`
**📚 ドキュメントと設定ファイルを更新**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 14:29:29 2025 +0900
A	.env.example
M	.gitignore
M	README.md
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 14:29:29 2025 +0900

    📚 ドキュメントと設定ファイルを更新
    
    - README.mdを大幅にリニューアル：モダンなデザインとバッジを追加
    - 実行例とコマンドオプションの詳細説明を充実
    - 新しいワークフローと全文コンテキスト機能の説明を追加
    - .gitignoreにexample/output/を追加してサンプル出力を除外
    - .env.exampleを追加して環境変数設定の参考を提供

 .env.example |   1 +
 .gitignore   |   1 +
 README.md    | 240 ++++++++++++++++++++++++++++++++++++++++-------------------
 3 files changed, 166 insertions(+), 76 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.env.example b/.env.example
new file mode 100644
index 0000000..f946b7a
--- /dev/null
+++ b/.env.example
@@ -0,0 +1 @@
+OPENROUTER_API_KEY=sk-or-xxxx
diff --git a/.gitignore b/.gitignore
index ba4f0f5..04ce1f8 100644
--- a/.gitignore
+++ b/.gitignore
@@ -208,3 +208,4 @@ __marimo__/
 .SourceSageAssets/
 uv.lock
 example/output/structured/logs/
+example/output/
diff --git a/README.md b/README.md
index 27bea1e..1c0dd88 100644
--- a/README.md
+++ b/README.md
@@ -1,15 +1,29 @@
-# Easy Dataset CLI
+<div align="center">
 
-テキストファイルからQ&Aペアを生成するシンプルなCLIツールです。LLMを使用してGenre-Audienceペアに基づいた多様なQ&Aデータセットを作成し、Genre別のXMLファイルとして出力します。
+# 🚀 Easy Dataset CLI
 
-## 特徴
+<p align="center">
+  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
+  <img src="https://img.shields.io/badge/CLI-Typer-green.svg" alt="CLI Framework">
+  <img src="https://img.shields.io/badge/LLM-OpenAI%20%7C%20OpenRouter-orange.svg" alt="LLM Support">
+  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
+</p>
 
-- **シンプル**: データベース不要、マークダウンでGA定義
-- **柔軟**: 複数のGenre-Audienceペアに対応
-- **安定**: LLMからの直接XML出力で信頼性向上
-- **効率的**: テキスト分割とバッチ処理で大きなファイルにも対応
+<p align="center">
+  テキストファイルからQ&Aペアを生成するシンプルなCLIツール<br>
+  LLMを使用してGenre-Audienceペアに基づいた多様なQ&Aデータセットを作成し、Genre別のXMLファイルとして出力します
+</p>
 
-## インストール
+</div>
+
+## ✨ 特徴
+
+- **🎯 シンプル**: データベース不要、マークダウンでGA定義
+- **🔄 柔軟**: 複数のGenre-Audienceペアに対応
+- **🛡️ 安定**: LLMからの直接XML出力で信頼性向上
+- **⚡ 効率的**: テキスト分割とバッチ処理で大きなファイルにも対応
+
+## 📦 インストール
 
 \```bash
 # 仮想環境の作成（推奨）
@@ -22,9 +36,9 @@ venv\Scripts\activate     # Windows
 pip install -e .
 \```
 
-## 使用方法
+## 🚀 使用方法
 
-### 新しいワークフロー（推奨）
+### 📋 基本的なワークフロー
 
 1. **GAペア定義ファイルの自動生成**
 \```bash
@@ -32,121 +46,195 @@ pip install -e .
 export OPENAI_API_KEY="your-api-key-here"
 
 # 元の文章からGAペア定義を自動生成
-easy-dataset create-ga sample_document.txt --output ga-definitions.md
-\```
-
-2. **（任意）生成されたGA定義のレビュー・編集**
-\```bash
-# テキストエディタで内容を確認・修正
-notepad ga-definitions.md  # Windows
-# または
-nano ga-definitions.md     # Linux/macOS
+uv run easy-dataset create-ga .\example\input\documents\sample_document.txt --output-dir .\example\output\sample_document --num-ga-pairs 10
 \```
 
-3. **Q&Aペアの生成**
+2. **Q&Aペアの生成**
 \```bash
 # GAペア定義を使ってQ&Aペアを生成
-easy-dataset generate sample_document.txt --ga-file ga-definitions.md --output-dir ./results
+uv run easy-dataset generate .\example\input\documents\sample_document.txt --ga-file .\example\output\sample_document\ga\ga_definitions.xml --output-dir .\example\output\sample_document\ --chunk-size 500
 \```
 
-### 従来の方法（手動でGA定義を作成）
-
-\```bash
-# 手動で作成したGA定義ファイルを使用
-easy-dataset generate sample_document.txt --ga-file sample_ga_definition.md --output-dir ./results
+### 💻 実行例
```

---

## ⏰ 14:29:53 - `8883931`
**🔀 Merge: モジュラーアーキテクチャリファクタリングと全文コンテキスト機能の実装**
*by Maki*

### 📋 Changed Files
```bash
Merge: f4292b4 409055d
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 14:29:53 2025 +0900
```

### 📊 Statistics
```bash
Merge: f4292b4 409055d
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 14:29:53 2025 +0900

    🔀 Merge: モジュラーアーキテクチャリファクタリングと全文コンテキスト機能の実装
    
    - コードベースを機能別モジュールに分割してメンテナンス性を向上
    - 全文コンテキストを活用した高品質Q&A生成機能を追加
    - CLIインターフェースの改善とドキュメントの充実
    - 新しいプロンプトテンプレートと設定ファイルの追加

 .env.example                                       |   1 +
 .gitignore                                         |   1 +
 README.md                                          | 240 ++++++---
 easy_dataset_cli/core.py                           | 560 ++-------------------
 easy_dataset_cli/file_utils.py                     |  59 +++
 easy_dataset_cli/ga_parser.py                      | 182 +++++++
 easy_dataset_cli/main.py                           |  50 +-
 easy_dataset_cli/prompts.py                        |   5 +
 .../prompts/qa_generation_with_fulltext.md         |  52 ++
 easy_dataset_cli/qa_generator.py                   | 209 ++++++++
 easy_dataset_cli/text_splitter.py                  |  17 +
 easy_dataset_cli/xml_utils.py                      | 154 ++++++
 12 files changed, 921 insertions(+), 609 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 15:09:09 - `4b14de5`
**📁 SourceSageignoreにuv.lockを追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:09:09 2025 +0900
M	.SourceSageignore
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:09:09 2025 +0900

    📁 SourceSageignoreにuv.lockを追加

 .SourceSageignore | 1 +
 1 file changed, 1 insertion(+)
```

### 💻 Code Changes
```diff
diff --git a/.SourceSageignore b/.SourceSageignore
index a029c83..ac8bce0 100644
--- a/.SourceSageignore
+++ b/.SourceSageignore
@@ -52,3 +52,4 @@ repository_summary.md
 venv
 .venv
 
+uv.lock
```

---

## ⏰ 15:09:23 - `3dec5e7`
**🔑 .env.exampleにHUGGINGFACE_TOKENを追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:09:23 2025 +0900
M	.env.example
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:09:23 2025 +0900

    🔑 .env.exampleにHUGGINGFACE_TOKENを追加

 .env.example | 1 +
 1 file changed, 1 insertion(+)
```

### 💻 Code Changes
```diff
diff --git a/.env.example b/.env.example
index f946b7a..72d7c7d 100644
--- a/.env.example
+++ b/.env.example
@@ -1 +1,2 @@
 OPENROUTER_API_KEY=sk-or-xxxx
+HUGGINGFACE_TOKEN=hf_xxxx
```

---

## ⏰ 15:09:35 - `e0bc23d`
**📦 pyproject.tomlの依存関係とPythonバージョン要件を更新**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:09:35 2025 +0900
M	pyproject.toml
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:09:35 2025 +0900

    📦 pyproject.tomlの依存関係とPythonバージョン要件を更新

 pyproject.toml | 9 ++++++---
 1 file changed, 6 insertions(+), 3 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/pyproject.toml b/pyproject.toml
index d9b2651..d5d958e 100644
--- a/pyproject.toml
+++ b/pyproject.toml
@@ -2,13 +2,16 @@
 name = "easy-dataset-cli"
 version = "1.0.0"
 description = "A simple CLI tool to generate QA pairs from a text file using LLMs and GA pairs, outputting genre-specific XML files."
+requires-python = ">=3.9"
 dependencies = [
-    "typer[all]",          # CLIフレームワーク
+    "typer",               # CLIフレームワーク
     "rich",                # リッチなコンソール出力
     "litellm",             # LLM連携ライブラリ
     "langchain-text-splitters", # テキスト分割用
     "mistune",             # マークダウン解析用ライブラリ
-    "python-dotenv"        # .env ファイル読み込み用
+    "python-dotenv",       # .env ファイル読み込み用
+    "huggingface-hub",     # Hugging Face Hub API
+    "datasets"             # Hugging Face Datasets
 ]
 
 [project.scripts]
@@ -17,4 +20,4 @@ easy-dataset = "easy_dataset_cli.main:app"
 
 [build-system]
 requires = ["setuptools>=61.0"]
-build-backend = "setuptools.build_meta"
\ No newline at end of file
+build-backend = "setuptools.build_meta"
```

---

## ⏰ 15:09:45 - `f2d45d8`
**🔧 core.pyにAlpaca変換・アップロード機能のインポートを追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:09:45 2025 +0900
M	easy_dataset_cli/core.py
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:09:45 2025 +0900

    🔧 core.pyにAlpaca変換・アップロード機能のインポートを追加

 easy_dataset_cli/core.py | 12 +++++++++++-
 1 file changed, 11 insertions(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/easy_dataset_cli/core.py b/easy_dataset_cli/core.py
index 2599497..056452b 100644
--- a/easy_dataset_cli/core.py
+++ b/easy_dataset_cli/core.py
@@ -18,6 +18,11 @@ from .file_utils import (
     save_ga_definitions_by_genre,
     sanitize_filename
 )
+from .alpaca_converter import (
+    convert_all_xml_to_alpaca,
+    upload_to_huggingface,
+    create_dataset_card
+)
 
 # 後方互換性のため、すべての関数を再エクスポート
 __all__ = [
@@ -39,5 +44,10 @@ __all__ = [
     # ファイル操作
     'create_output_directories',
     'save_ga_definitions_by_genre',
-    'sanitize_filename'
+    'sanitize_filename',
+    
+    # アルパカ変換・アップロード
+    'convert_all_xml_to_alpaca',
+    'upload_to_huggingface',
+    'create_dataset_card'
 ]
```

---

## ⏰ 15:09:56 - `26c8f59`
**💻 main.pyにAlpaca形式とHugging Face統合のコマンドを追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:09:56 2025 +0900
M	easy_dataset_cli/main.py
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:09:56 2025 +0900

    💻 main.pyにAlpaca形式とHugging Face統合のコマンドを追加

 easy_dataset_cli/main.py | 126 ++++++++++++++++++++++++++++++++++++++++++++++-
 1 file changed, 125 insertions(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/easy_dataset_cli/main.py b/easy_dataset_cli/main.py
index 6d7e897..7d4e41d 100644
--- a/easy_dataset_cli/main.py
+++ b/easy_dataset_cli/main.py
@@ -18,7 +18,10 @@ from .core import (
     parse_ga_definitions_from_xml,
     save_ga_definitions_by_genre,
     create_output_directories,
-    sanitize_filename
+    sanitize_filename,
+    convert_all_xml_to_alpaca,
+    upload_to_huggingface,
+    create_dataset_card
 )
 
 # .envファイルを読み込む
@@ -140,6 +143,26 @@ def generate(
         "--use-fulltext", "-f",
         help="全文をコンテキストとして含めてQA生成を行います。より文脈を理解したQAが生成されますが、処理時間とコストが増加します。"
     )] = False,
+    export_alpaca: Annotated[bool, typer.Option(
+        "--export-alpaca", "-a",
+        help="生成されたQ&AペアをAlpaca形式のJSONファイルとして出力します。"
+    )] = False,
+    upload_hf: Annotated[bool, typer.Option(
+        "--upload-hf", "-u",
+        help="生成されたデータセットをHugging Face Hubにアップロードします。"
+    )] = False,
+    hf_repo_name: Annotated[str, typer.Option(
+        "--hf-repo-name", "-r",
+        help="Hugging Face Hubのリポジトリ名（例: username/dataset-name）"
+    )] = "",
+    hf_token: Annotated[str, typer.Option(
+        "--hf-token", "-t",
+        help="Hugging Face APIトークン（環境変数HUGGINGFACE_TOKENからも取得可能）"
+    )] = "",
+    hf_private: Annotated[bool, typer.Option(
+        "--hf-private",
+        help="Hugging Faceリポジトリをプライベートにします。"
+    )] = False,
 ):
     """テキストファイルとGA定義からQ&Aペアを生成し、Genre別のXMLファイルとして出力します。
     
@@ -228,6 +251,33 @@ def generate(
                 console.print(f"  - [green]✓[/green] {output_file_path.name}")
 
             console.print("\n[bold green]すべてのファイルの保存が完了しました。[/bold green]")
+            
+            # アルパカ形式でのエクスポート
+            if export_alpaca:
+                console.print("\n[bold blue]Alpaca形式のJSONファイルを生成中...[/bold blue]")
+                alpaca_file = dirs["base"] / "dataset_alpaca.json"
+                alpaca_data = convert_all_xml_to_alpaca(dirs["qa"], alpaca_file)
+                
+                # データセットカードを生成
+                readme_file = dirs["base"] / "README.md"
+                create_dataset_card(alpaca_data, readme_file, "Generated QA Dataset")
+                
+                # Hugging Face Hubにアップロード
+                if upload_hf:
+                    if not hf_repo_name:
+                        console.print("[bold red]--hf-repo-nameが指定されていません！[/bold red]")
+                        console.print("[yellow]例: --hf-repo-name username/my-qa-dataset[/yellow]")
+                    else:
+                        console.print(f"\n[bold blue]Hugging Face Hubにアップロード中...[/bold blue]")
+                        success = upload_to_huggingface(
+                            dataset_data=alpaca_data,
+                            repo_name=hf_repo_name,
+                            hf_token=hf_token if hf_token else None,
+                            private=hf_private,
+                            commit_message=f"Upload QA dataset with {len(alpaca_data)} entries"
+                        )
+                        if not success:
+                            console.print("[bold red]Hugging Faceアップロードに失敗しました[/bold red]")
         else:
             console.print("\n--- 生成されたQ&Aペア (Genre別XML) ---")
             for genre, xml_content in xml_outputs_by_genre.items():
@@ -239,5 +289,79 @@ def generate(
         raise typer.Exit(code=1)
 
 
+@app.command()
+def convert_to_alpaca(
+    qa_dir: Annotated[Path, typer.Argument(
+        exists=True, dir_okay=True, readable=True,
+        help="XMLファイルが保存されているqaディレクトリへのパス。"
+    )],
+    output_file: Annotated[Path, typer.Option(
+        "--output-file", "-o", file_okay=True, dir_okay=False,
+        help="出力するAlpaca形式JSONファイルのパス。"
+    )] = None,
+    upload_hf: Annotated[bool, typer.Option(
+        "--upload-hf", "-u",
+        help="生成されたデータセットをHugging Face Hubにアップロードします。"
+    )] = False,
+    hf_repo_name: Annotated[str, typer.Option(
+        "--hf-repo-name", "-r",
+        help="Hugging Face Hubのリポジトリ名（例: username/dataset-name）"
+    )] = "",
+    hf_token: Annotated[str, typer.Option(
```

---

## ⏰ 15:10:07 - `bb83856`
**📚 README.mdにAlpaca形式対応とHugging Face統合機能を追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:10:07 2025 +0900
M	README.md
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:10:07 2025 +0900

    📚 README.mdにAlpaca形式対応とHugging Face統合機能を追加

 README.md | 251 +++++++++++++++++++++++++++++++++++++++++---------------------
 1 file changed, 168 insertions(+), 83 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/README.md b/README.md
index 1c0dd88..30adc2e 100644
--- a/README.md
+++ b/README.md
@@ -3,15 +3,18 @@
 # 🚀 Easy Dataset CLI
 
 <p align="center">
-  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
+  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python Version">
   <img src="https://img.shields.io/badge/CLI-Typer-green.svg" alt="CLI Framework">
   <img src="https://img.shields.io/badge/LLM-OpenAI%20%7C%20OpenRouter-orange.svg" alt="LLM Support">
-  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
+  <img src="https://img.shields.io/badge/Format-Alpaca%20%7C%20XML-purple.svg" alt="Output Format">
+  <img src="https://img.shields.io/badge/🤗-Hugging%20Face-yellow.svg" alt="Hugging Face">
+  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
 </p>
 
 <p align="center">
   テキストファイルからQ&Aペアを生成するシンプルなCLIツール<br>
-  LLMを使用してGenre-Audienceペアに基づいた多様なQ&Aデータセットを作成し、Genre別のXMLファイルとして出力します
+  LLMを使用してGenre-Audienceペアに基づいた多様なQ&Aデータセットを作成し、<br>
+  <strong>Alpaca形式JSON</strong>やGenre別XMLファイルとして出力、<strong>Hugging Face Hub</strong>への直接アップロードも対応
 </p>
 
 </div>
@@ -22,6 +25,10 @@
 - **🔄 柔軟**: 複数のGenre-Audienceペアに対応
 - **🛡️ 安定**: LLMからの直接XML出力で信頼性向上
 - **⚡ 効率的**: テキスト分割とバッチ処理で大きなファイルにも対応
+- **🦙 Alpaca対応**: 生成されたQ&AペアをAlpaca形式のJSONで出力
+- **🤗 HF統合**: Hugging Face Hubへの直接アップロード機能
+- **📊 データセットカード**: 自動的なREADME.md生成でデータセット情報を整理
+- **🔄 変換機能**: 既存XMLファイルからAlpaca形式への変換コマンド
 
 ## 📦 インストール
 
@@ -55,82 +62,39 @@ uv run easy-dataset create-ga .\example\input\documents\sample_document.txt --ou
 uv run easy-dataset generate .\example\input\documents\sample_document.txt --ga-file .\example\output\sample_document\ga\ga_definitions.xml --output-dir .\example\output\sample_document\ --chunk-size 500
 \```
 
-### 💻 実行例
-
-\```powershell
-PS C:\Prj\easy-dataset-cli> uv run easy-dataset --help
-Usage: easy-dataset [OPTIONS] COMMAND [ARGS]...
-
-テキストファイルからQ&Aペアを生成するシンプルなCLIツール。
-
-╭─ Options ──────────────────────────────────────────────────────────────────╮
-│ --install-completion            Install completion for the current shell.  │
-│ --show-completion               Show completion for the current shell.      │
-│ --help                -h        Show this message and exit.                │
-╰────────────────────────────────────────────────────────────────────────────╯
-
-╭─ Commands ─────────────────────────────────────────────────────────────────╮
-│ create-ga   元の文章を分析し、GAペア定義をXML形式で生成し、Genreごとに     │
-│             マークダウンファイルに保存します。                             │
-│ generate    テキストファイルとGA定義からQ&Aペアを生成し、Genre別の        │
-│             XMLファイルとして出力します。                                  │
-╰────────────────────────────────────────────────────────────────────────────╯
-
-PS C:\Prj\easy-dataset-cli> uv run easy-dataset create-ga .\example\input\documents\sample_document.txt --output-dir .\example\output\sample_document --num-ga-pairs 10
-ファイルを読み込んでいます: example\input\documents\sample_document.txt
-読み込んだテキスト長: 545 文字
-LLMに最適なGAペアを提案させています...
-コンテキスト長: 545 文字
-LLMレスポンス長: 2534 文字
-出力ディレクトリを作成しました: ga/, logs/, qa/
-✓ LLMのrawレスポンスを保存しました: example\output\sample_document\logs\raw.md
-XMLからGAペアを解析しています...
-見つかったPairノード数: 10
-✓ 学術論文 x コンピュータサイエンス研究者
-✓ 技術ブログ x プログラミング初心者
-✓ 教科書 x 大学生
-✓ FAQ x 実務開発者
-✓ 対話形式の記事 x 中高生
-✓ 専門技術書 x データサイエンティスト
-✓ ケーススタディ x ITプロジェクトマネージャー
-✓ オンラインコース教材 x 社会人学習者
-✓ 雑誌記事 x テック愛好者
-✓ ワークショップ資料 x 教育者
-✓ GA定義XMLファイルを保存しました: example\output\sample_document\ga\ga_definitions.xml
-GA定義を保存しました: example\output\sample_document\ga\ga_definitions_学術論文.md
-GA定義を保存しました: example\output\sample_document\ga\ga_definitions_技術ブログ.md
-GA定義を保存しました: example\output\sample_document\ga\ga_definitions_教科書.md
-GA定義を保存しました: example\output\sample_document\ga\ga_definitions_faq.md
-GA定義を保存しました: example\output\sample_document\ga\ga_definitions_対話形式の記事.md
-GA定義を保存しました: example\output\sample_document\ga\ga_definitions_専門技術書.md
-GA定義を保存しました: example\output\sample_document\ga\ga_definitions_ケーススタディ.md
-GA定義を保存しました: example\output\sample_document\ga\ga_definitions_オンラインコース教材.md
-GA定義を保存しました: example\output\sample_document\ga\ga_definitions_雑誌記事.md
-GA定義を保存しました: example\output\sample_document\ga\ga_definitions_ワークショップ資料.md
-✓ 10個のGAペアを example\output\sample_document\ga に保存しました。
-ヒント: 生成されたファイルをレビューし、必要に応じて編集してから `generate` コマンドで使用してください。
-
-PS C:\Prj\easy-dataset-cli> uv run easy-dataset generate .\example\input\documents\sample_document.txt --ga-file .\example\output\sample_document\ga\ga_definitions.xml --output-dir .\example\output\sample_document\ --chunk-size 500
-ファイルを読み込んでいます: example\input\documents\sample_document.txt
-GAペアを解析しています: example\output\sample_document\ga\ga_definitions.xml
-10 個のGAペアを見つけました。
```

---

## ⏰ 15:10:20 - `1484866`
**🔧 alpaca_converter.pyを追加 - XMLからAlpaca形式変換とHugging Faceアップロード機能を実装**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:10:20 2025 +0900
A	easy_dataset_cli/alpaca_converter.py
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:10:20 2025 +0900

    🔧 alpaca_converter.pyを追加 - XMLからAlpaca形式変換とHugging Faceアップロード機能を実装

 easy_dataset_cli/alpaca_converter.py | 222 +++++++++++++++++++++++++++++++++++
 1 file changed, 222 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/easy_dataset_cli/alpaca_converter.py b/easy_dataset_cli/alpaca_converter.py
new file mode 100644
index 0000000..bb1437a
--- /dev/null
+++ b/easy_dataset_cli/alpaca_converter.py
@@ -0,0 +1,222 @@
+# easy_dataset_cli/alpaca_converter.py
+"""アルパカデータセット形式への変換とHugging Faceアップロード機能"""
+
+import json
+import xml.etree.ElementTree as ET
+from pathlib import Path
+from typing import List, Dict, Optional
+from rich.console import Console
+from huggingface_hub import HfApi, create_repo
+from datasets import Dataset
+import os
+
+console = Console()
+
+def xml_to_alpaca_format(xml_file_path: Path) -> List[Dict[str, str]]:
+    """XMLファイルをアルパカ形式のデータに変換する"""
+    alpaca_data = []
+    
+    try:
+        tree = ET.parse(xml_file_path)
+        root = tree.getroot()
+        
+        genre = root.get('genre', 'Unknown')
+        
+        for pair in root.findall('Pair'):
+            audience_elem = pair.find('Audience')
+            question_elem = pair.find('Question')
+            answer_elem = pair.find('Answer')
+            
+            if all([audience_elem is not None, question_elem is not None, answer_elem is not None]):
+                audience = audience_elem.text or ""
+                question = question_elem.text or ""
+                answer = answer_elem.text or ""
+                
+                # アルパカ形式に変換
+                alpaca_entry = {
+                    "instruction": question,
+                    "input": "",  # アルパカ形式では通常空文字
+                    "output": answer,
+                    "genre": genre,
+                    "audience": audience
+                }
+                alpaca_data.append(alpaca_entry)
+                
+    except ET.ParseError as e:
+        console.print(f"[bold red]XMLファイルの解析エラー:[/bold red] {e}")
+    except Exception as e:
+        console.print(f"[bold red]予期しないエラー:[/bold red] {e}")
+    
+    return alpaca_data
+
+def convert_all_xml_to_alpaca(qa_dir: Path, output_file: Path) -> List[Dict[str, str]]:
+    """QAディレクトリ内のすべてのXMLファイルをアルパカ形式に変換"""
+    all_alpaca_data = []
+    
+    xml_files = list(qa_dir.glob("*.xml"))
+    
+    if not xml_files:
+        console.print(f"[yellow]XMLファイルが見つかりません: {qa_dir}[/yellow]")
+        return all_alpaca_data
+    
+    console.print(f"[green]{len(xml_files)}個のXMLファイルを変換中...[/green]")
+    
+    for xml_file in xml_files:
+        console.print(f"[dim]変換中: {xml_file.name}[/dim]")
+        alpaca_data = xml_to_alpaca_format(xml_file)
+        all_alpaca_data.extend(alpaca_data)
+        console.print(f"[green]✓[/green] {len(alpaca_data)}個のエントリを追加")
+    
+    # JSONファイルに保存
+    with open(output_file, 'w', encoding='utf-8') as f:
+        json.dump(all_alpaca_data, f, ensure_ascii=False, indent=2)
+    
+    console.print(f"[bold green]✓[/bold green] 合計{len(all_alpaca_data)}個のエントリを "
+                  f"[cyan]{output_file}[/cyan] に保存しました")
+    
+    return all_alpaca_data
+
+def upload_to_huggingface(
+    dataset_data: List[Dict[str, str]], 
+    repo_name: str, 
+    hf_token: Optional[str] = None,
+    private: bool = False,
+    commit_message: str = "Upload alpaca dataset"
+) -> bool:
+    """Hugging Face Hubにデータセットをアップロード"""
+    
+    if not hf_token:
+        hf_token = os.getenv("HUGGINGFACE_TOKEN")
+        if not hf_token:
+            console.print("[bold red]HUGGINGFACE_TOKENが設定されていません！[/bold red]")
+            console.print("[yellow]環境変数またはコマンドライン引数でトークンを指定してください[/yellow]")
+            return False
+    
```

---

## ⏰ 15:10:43 - `1fb94de`
**🔀 Merge: Alpaca形式対応とHugging Face統合機能**
*by Maki*

### 📋 Changed Files
```bash
Merge: 8883931 1484866
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:10:43 2025 +0900
```

### 📊 Statistics
```bash
Merge: 8883931 1484866
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:10:43 2025 +0900

    🔀 Merge: Alpaca形式対応とHugging Face統合機能

 .SourceSageignore                    |   1 +
 .env.example                         |   1 +
 README.md                            | 251 +++++++++++++++++++++++------------
 easy_dataset_cli/alpaca_converter.py | 222 +++++++++++++++++++++++++++++++
 easy_dataset_cli/core.py             |  12 +-
 easy_dataset_cli/main.py             | 126 +++++++++++++++++-
 pyproject.toml                       |   9 +-
 7 files changed, 534 insertions(+), 88 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 15:34:20 - `83ef261`
**🎨 README.mdにバナー画像を追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:34:20 2025 +0900
M	README.md
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:34:20 2025 +0900

    🎨 README.mdにバナー画像を追加

 README.md | 13 +++++++++++++
 1 file changed, 13 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/README.md b/README.md
index 30adc2e..49e8d17 100644
--- a/README.md
+++ b/README.md
@@ -1,5 +1,7 @@
 <div align="center">
 
+![](https://github.com/user-attachments/assets/865632a4-911f-4de4-867d-c65cef365d79)
+
 # 🚀 Easy Dataset CLI
 
 <p align="center">
@@ -323,3 +325,14 @@ size_categories:
 ## 📜 ライセンス
 
 MIT License
+
+## 🔗 参考情報
+
+本プロジェクトは以下のOSSと論文を参考に開発されています：
+
+### 📦 参考OSS
+- **[Easy Dataset](https://github.com/ConardLi/easy-dataset)**
+
+### 📄 参考論文
+- **[Dataset Generation for Instruction Tuning](https://arxiv.org/html/2507.04009v1)**
+
```

---

## ⏰ 15:34:41 - `69f3484`
**🔧 alpaca_converter.pyにREADMEアップロード機能を追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:34:41 2025 +0900
M	easy_dataset_cli/alpaca_converter.py
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:34:41 2025 +0900

    🔧 alpaca_converter.pyにREADMEアップロード機能を追加

 easy_dataset_cli/alpaca_converter.py | 22 +++++++++++++++++++---
 1 file changed, 19 insertions(+), 3 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/easy_dataset_cli/alpaca_converter.py b/easy_dataset_cli/alpaca_converter.py
index bb1437a..0a148ea 100644
--- a/easy_dataset_cli/alpaca_converter.py
+++ b/easy_dataset_cli/alpaca_converter.py
@@ -77,11 +77,12 @@ def convert_all_xml_to_alpaca(qa_dir: Path, output_file: Path) -> List[Dict[str,
     return all_alpaca_data
 
 def upload_to_huggingface(
-    dataset_data: List[Dict[str, str]], 
-    repo_name: str, 
+    dataset_data: List[Dict[str, str]],
+    repo_name: str,
     hf_token: Optional[str] = None,
     private: bool = False,
-    commit_message: str = "Upload alpaca dataset"
+    commit_message: str = "Upload alpaca dataset",
+    readme_file: Optional[Path] = None
 ) -> bool:
     """Hugging Face Hubにデータセットをアップロード"""
     
@@ -120,6 +121,21 @@ def upload_to_huggingface(
             private=private
         )
         
+        # README.mdが指定されている場合はアップロード
+        if readme_file and readme_file.exists():
+            try:
+                api.upload_file(
+                    path_or_fileobj=readme_file,
+                    path_in_repo="README.md",
+                    repo_id=repo_name,
+                    repo_type="dataset",
+                    commit_message=f"Update README.md",
+                    token=hf_token
+                )
+                console.print(f"[green]✓[/green] README.mdをアップロードしました!")
+            except Exception as readme_error:
+                console.print(f"[yellow]README.mdアップロードの警告: {readme_error}[/yellow]")
+        
         console.print(f"[bold green]✓[/bold green] データセットをアップロードしました!")
         console.print(f"[cyan]https://huggingface.co/datasets/{repo_name}[/cyan]")
         
```

---

## ⏰ 15:34:52 - `c8a00e7`
**🔧 main.pyにREADMEファイル渡し処理を追加**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:34:52 2025 +0900
M	easy_dataset_cli/main.py
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:34:52 2025 +0900

    🔧 main.pyにREADMEファイル渡し処理を追加

 easy_dataset_cli/main.py | 6 ++++--
 1 file changed, 4 insertions(+), 2 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/easy_dataset_cli/main.py b/easy_dataset_cli/main.py
index 7d4e41d..6f62532 100644
--- a/easy_dataset_cli/main.py
+++ b/easy_dataset_cli/main.py
@@ -274,7 +274,8 @@ def generate(
                             repo_name=hf_repo_name,
                             hf_token=hf_token if hf_token else None,
                             private=hf_private,
-                            commit_message=f"Upload QA dataset with {len(alpaca_data)} entries"
+                            commit_message=f"Upload QA dataset with {len(alpaca_data)} entries",
+                            readme_file=readme_file
                         )
                         if not success:
                             console.print("[bold red]Hugging Faceアップロードに失敗しました[/bold red]")
@@ -349,7 +350,8 @@ def convert_to_alpaca(
                 repo_name=hf_repo_name,
                 hf_token=hf_token if hf_token else None,
                 private=hf_private,
-                commit_message=f"Upload converted QA dataset with {len(alpaca_data)} entries"
+                commit_message=f"Upload converted QA dataset with {len(alpaca_data)} entries",
+                readme_file=readme_file
             )
             
             if not success:
```

---

## ⏰ 15:35:11 - `13b8c4c`
**🔀 Merge: README改善機能**
*by Maki*

### 📋 Changed Files
```bash
Merge: 1fb94de c8a00e7
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:35:11 2025 +0900
```

### 📊 Statistics
```bash
Merge: 1fb94de c8a00e7
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:35:11 2025 +0900

    🔀 Merge: README改善機能

 README.md                            | 13 +++++++++++++
 easy_dataset_cli/alpaca_converter.py | 22 +++++++++++++++++++---
 easy_dataset_cli/main.py             |  6 ++++--
 3 files changed, 36 insertions(+), 5 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 15:35:51 - `33b27e1`
**Merge branch 'develop'**
*by Maki*

### 📋 Changed Files
```bash
Merge: dc2aa8f 13b8c4c
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:35:51 2025 +0900
```

### 📊 Statistics
```bash
Merge: dc2aa8f 13b8c4c
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:35:51 2025 +0900

    Merge branch 'develop'

 .SourceSageignore                                  |   1 +
 .env.example                                       |   2 +
 .gitignore                                         |   1 +
 README.md                                          | 324 +++++++++---
 easy_dataset_cli/alpaca_converter.py               | 238 +++++++++
 easy_dataset_cli/core.py                           | 570 ++-------------------
 easy_dataset_cli/file_utils.py                     |  59 +++
 easy_dataset_cli/ga_parser.py                      | 182 +++++++
 easy_dataset_cli/main.py                           | 176 ++++++-
 easy_dataset_cli/prompts.py                        |   5 +
 .../prompts/qa_generation_with_fulltext.md         |  52 ++
 easy_dataset_cli/qa_generator.py                   | 209 ++++++++
 easy_dataset_cli/text_splitter.py                  |  17 +
 easy_dataset_cli/xml_utils.py                      | 154 ++++++
 pyproject.toml                                     |   9 +-
 15 files changed, 1394 insertions(+), 605 deletions(-)
```

### 💻 Code Changes
```diff
```

---

## ⏰ 15:48:08 - `f38813f`
**✨ README.mdのバッジ表記を改善**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:48:08 2025 +0900
M	README.md
```

### 📊 Statistics
```bash
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:48:08 2025 +0900

    ✨ README.mdのバッジ表記を改善
    
    - バッジの記述形式をimgタグからMarkdown形式に変更
    - Hugging Faceバッジに絵文字を追加
    - 可読性と保守性を向上

 README.md | 14 ++++++++------
 1 file changed, 8 insertions(+), 6 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/README.md b/README.md
index 49e8d17..0946c9a 100644
--- a/README.md
+++ b/README.md
@@ -5,12 +5,14 @@
 # 🚀 Easy Dataset CLI
 
 <p align="center">
-  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python Version">
-  <img src="https://img.shields.io/badge/CLI-Typer-green.svg" alt="CLI Framework">
-  <img src="https://img.shields.io/badge/LLM-OpenAI%20%7C%20OpenRouter-orange.svg" alt="LLM Support">
-  <img src="https://img.shields.io/badge/Format-Alpaca%20%7C%20XML-purple.svg" alt="Output Format">
-  <img src="https://img.shields.io/badge/🤗-Hugging%20Face-yellow.svg" alt="Hugging Face">
-  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
+
+  ![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)
+  ![CLI Framework](https://img.shields.io/badge/CLI-Typer-green.svg)
+  ![LLM Support](https://img.shields.io/badge/LLM-OpenAI%20%7C%20OpenRouter-orange.svg)
+  ![Output Format](https://img.shields.io/badge/Format-Alpaca%20%7C%20XML-purple.svg)
+  ![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow.svg)
+  ![License](https://img.shields.io/badge/License-MIT-green.svg)
+  
 </p>
 
 <p align="center">
```

---

## ⏰ 15:48:26 - `0a18942`
**🔀 Merge: README.mdのバッジ表記改善**
*by Maki*

### 📋 Changed Files
```bash
Merge: 13b8c4c f38813f
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:48:26 2025 +0900
```

### 📊 Statistics
```bash
Merge: 13b8c4c f38813f
Author: Maki <sunwood.ai.labs@gmail.com>
Date:   Fri Aug 15 15:48:26 2025 +0900

    🔀 Merge: README.mdのバッジ表記改善

 README.md | 14 ++++++++------
 1 file changed, 8 insertions(+), 6 deletions(-)
```

### 💻 Code Changes
```diff
```

---

