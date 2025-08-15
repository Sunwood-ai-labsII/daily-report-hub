# 🔄 Latest Code Changes

```diff
diff --git a/.gitignore b/.gitignore
index 16c3c78..ba4f0f5 100644
--- a/.gitignore
+++ b/.gitignore
@@ -206,3 +206,5 @@ marimo/_static/
 marimo/_lsp/
 __marimo__/
 .SourceSageAssets/
+uv.lock
+example/output/structured/logs/
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
-| `AUTO_APPROVE` | PR自動承認 | `true` |
-| `AUTO_MERGE` | PR自動マージ | `true` |
-| `CREATE_PR` | PR作成/直接プッシュ切り替え | `true` |
-
----
+### 新しいワークフロー（推奨）
 
-## 📝 主な機能
+1. **GAペア定義ファイルの自動生成**
+\```bash
+# 環境変数にAPIキーを設定
+export OPENAI_API_KEY="your-api-key-here"
 
-> [!NOTE]
-> このテンプレートから作成されたリポジトリでは、以下の機能が自動で有効になります。
+# 元の文章からGAペア定義を自動生成
+easy-dataset create-ga sample_document.txt --output ga-definitions.md
+\```
 
-### 🔄 自動実行されるスクリプト（リモート）
+2. **（任意）生成されたGA定義のレビュー・編集**
+\```bash
+# テキストエディタで内容を確認・修正
+notepad ga-definitions.md  # Windows
+# または
+nano ga-definitions.md     # Linux/macOS
+\```
 
-- **週情報計算**
-  週情報（週番号・開始日・終了日など）を計算し環境変数に出力
+3. **Q&Aペアの生成**
+\```bash
+# GAペア定義を使ってQ&Aペアを生成
+easy-dataset generate sample_document.txt --ga-file ga-definitions.md --output-dir ./results
+\```
 
-- **Git活動分析**
-  Gitのコミット履歴・差分を分析し、生データファイルを生成
+### 従来の方法（手動でGA定義を作成）
 
-- **Markdownレポート生成**
-  生データから日報・統計・差分などのMarkdownレポートを自動生成
+\```bash
+# 手動で作成したGA定義ファイルを使用
+easy-dataset generate sample_document.txt --ga-file sample_ga_definition.md --output-dir ./results
+\```
 
-- **Docusaurus構造作成**
-  Docusaurus用のディレクトリ・_category_.jsonを自動生成
+### コマンドオプション
 
-- **同期処理**
-  集約リポジトリへPR作成・自動承認・自動マージ
+#### create-ga コマンド
+\```bash
+easy-dataset create-ga [OPTIONS] FILE_PATH
 
----
+Arguments:
+  FILE_PATH  GAペアの定義を生成するための元のテキストファイル
 
-## 🚀 使い方（クイックスタート）
-
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
-\```yaml
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
+Options:
+  -o, --output PATH    生成されたGAペア定義を保存するファイルパス [required]
+  -m, --model TEXT     GAペア定義の生成に使用するLLMモデル [default: gpt-4o]
+  -h, --help           ヘルプを表示
 \```
 
-### 🔑 環境変数・シークレット設定
+#### generate コマンド
+\```bash
+easy-dataset generate [OPTIONS] FILE_PATH
 
-> [!WARNING]
-> 以下のシークレットを設定しないと、日報同期機能が正常に動作しません。
+Arguments:
+  FILE_PATH  元のテキストファイルへのパス
 
-#### 必須シークレット
-- `GH_PAT`: GitHub Personal Access Token（リポジトリアクセス用）
-- `GH_PAT_YUKIHIKO`: YUKIHIKO権限用のToken（PR作成・承認用）
-
-#### オプション環境変数（ワークフロー内で設定）
-- `REPORT_HUB_REPO`: レポートハブリポジトリ（デフォルト: `Sunwood-ai-labsII/daily-report-hub`）
-- `WEEK_START_DAY`: 週の開始曜日（0=日曜日, 1=月曜日, ..., 6=土曜日、デフォルト: 1）
-- `AUTO_APPROVE`: PR自動承認（true/false、デフォルト: true）
-- `AUTO_MERGE`: PR自動マージ（true/false、デフォルト: true）
-- `CREATE_PR`: PR作成フラグ（true=PR作成, false=直接プッシュ、デフォルト: true）
+Options:
+  -g, --ga-file PATH        Genre-Audienceペアを定義したMarkdownファイル [required]
+  -o, --output-dir PATH     XMLファイルの出力ディレクトリ（省略時はコンソール出力）
+  -m, --model TEXT          Q&Aペアの生成に使用するLLMモデル [default: gpt-4o]
+  --chunk-size INTEGER      テキストチャンクの最大サイズ [default: 2000]
+  --chunk-overlap INTEGER   チャンク間のオーバーラップサイズ [default: 200]
+  -h, --help                ヘルプを表示
+\```
 
-#### 環境変数設定例
-各環境変数の詳細な設定は、ワークフローファイル内のコメントを参照してください。
+## GA定義ファイルの形式
 
-### 📋 シークレット設定手順
+Genre-Audienceペアをマークダウン形式で定義します：
 
-> [!CAUTION]
-> シークレットの漏洩には注意してください。GitHubリポジトリ内に直接記述しないでください。
+\```markdown
+# Genre: 学術論文
+学術的で厳密な表現を用い、専門用語を正確に使用し、論理的で客観的な回答を提供します。
 
-1. リポジトリの「Settings」→「Secrets and variables」→「Actions」に移動
-2. 「New repository secret」をクリックして各シークレットを追加
-3. 以下のシークレットを設定：
-   - `GH_PAT`: `repo`スコープを持つPersonal Access Token
-   - `GH_PAT_YUKIHIKO`: `repo`スコープを持つPersonal Access Token（YUKIHIKO権限用）
+# Audience: 大学生
+大学レベルの知識を持つ学習者向けに、基礎概念から応用まで段階的に説明します。
 
 ---
 
-## 📁 ディレクトリ構成例
-
-> [!NOTE]
-> このテンプレートから作成されたリポジトリの基本的な構成です。
+# Genre: 技術ブログ
+実践的で親しみやすい表現を用い、具体例やコード例を交えて説明します。
 
-\```
-.
-├── .github/
-│   └── workflows/
-│       └── sync-to-report-gh.yml
-├── .gitignore
-├── LICENSE
-├── README.md
-└── [プロジェクト固有のファイル]
+# Audience: エンジニア
+実務経験のある開発者向けに、実装の詳細や最適化のポイントを重視した内容を提供します。
 \```
 
----
+## 出力形式
 
-## 🛠️ 設定・カスタマイズ
+各GenreごとにXMLファイルが生成されます：
 
-> [!TIP]
-> 必要に応じてワークフローファイルをカスタマイズできます。
-
-- `.github/workflows/sync-to-report-gh.yml`
-  - `WEEK_START_DAY`：週の開始曜日（0=日, 1=月, ...）
-  - `AUTO_APPROVE`：PR自動承認
-  - `AUTO_MERGE`：PR自動マージ
-  - `CREATE_PR`：PR作成/直接push切替
-
-- リモートスクリプトの詳細は開発リポジトリを参照
-
----
+\```xml
+<?xml version="1.0" ?>
+<QAPairs genre="学術論文">
+  <Pair>
+    <Audience>大学生</Audience>
+    <Question>Pythonの設計哲学における主要な特徴は何ですか？</Question>
+    <Answer>Pythonの設計哲学は「読みやすさ」を重視しており、シンプルで理解しやすい構文が特徴です。</Answer>
+  </Pair>
+</QAPairs>
+\```
 
-## 🔗 参考リンク
+## サポートするLLMモデル
 
-- [集約用日報ハブリポジトリ](https://github.com/Sunwood-ai-labsII/daily-report-hub)
-- [開発リポジトリ（スクリプトソース）](https://github.com/Sunwood-ai-labsII/daily-report-hub_dev)
-- [GitHub Actions公式ドキュメント](https://docs.github.com/ja/actions)
-- [Docusaurus公式サイト](https://docusaurus.io/ja/)
+### OpenAI（直接）
+\```bash
+export OPENAI_API_KEY="sk-..."
+easy-dataset generate document.txt -g ga.md -m gpt-4o
+\```
 
----
+### OpenRouter経由
+\```bash
+export OPENROUTER_API_KEY="sk-or-v1-..."
+easy-dataset generate document.txt -g ga.md -m gpt-4o  # 自動でopenai/gpt-4oに変換
+easy-dataset generate document.txt -g ga.md -m claude-3-sonnet  # 自動でanthropic/claude-3-sonnetに変換
+\```
 
-## 📝 ライセンス
+### その他のプロバイダー
+- Anthropic: `claude-3-opus`, `claude-3-sonnet`, `claude-3-haiku`
+- Ollama: `ollama/llama3`, `ollama/mistral`
+- その他litellmがサポートするすべてのモデル
 
-このテンプレートは [LICENSE](LICENSE) に基づいて提供されています。
+### 推奨モデル
+- **高品質**: `gpt-4o`, `claude-3-opus`
+- **バランス**: `gpt-4`, `claude-3-sonnet`
+- **高速**: `gpt-3.5-turbo`, `claude-3-haiku`
 
----
+## ライセンス
 
-© 2025 Sunwood-ai-labsII
+MIT License
\ No newline at end of file
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
index 0000000..c9db332
--- /dev/null
+++ b/easy_dataset_cli/core.py
@@ -0,0 +1,519 @@
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
+from .prompts import get_qa_generation_prompt, get_ga_definition_generation_prompt
+
+# .envファイルを読み込む
+load_dotenv()
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
+    chunk: str, model: str, ga_pair: Dict[str, Dict[str, str]], logs_dir: Path = None, num_qa_pairs: int = None
+) -> List[Dict[str, str]]:
+    """litellmを使い、1つのチャンクと1つのGAペアからQ&Aペアのリストを生成する"""
+    prompt_template = get_qa_generation_prompt()
+    prompt = prompt_template.format(
+        context=chunk,
+        genre_title=ga_pair['genre']['title'],
+        genre_description=ga_pair['genre']['description'],
+        audience_title=ga_pair['audience']['title'],
+        audience_description=ga_pair['audience']['description'],
+        num_qa_pairs=num_qa_pairs if num_qa_pairs is not None else "複数の"
+    )
+
+    messages = [
+        {"role": "system", "content": "あなたは、XML形式で厳密に出力する優秀なアシスタントです。XMLの特殊文字（&, <, >, \", '）は適切にエスケープし、改行は含めずに出力してください。"},
+        {"role": "user", "content": prompt}
+    ]
+
+    # OpenRouter用の環境変数設定
+    os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY", "")
+    
+    try:
+        response = completion(model=model, messages=messages)
+        xml_content = response.choices[0].message.content
+        
+        # rawレスポンスを保存（オプション）
+        if logs_dir:
+            genre_safe = "".join(c for c in ga_pair['genre']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
+            audience_safe = "".join(c for c in ga_pair['audience']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
+            raw_filename = f"qa_raw_{genre_safe}_{audience_safe}.md"
+            raw_file_path = logs_dir / raw_filename
+            raw_file_path.write_text(xml_content, encoding="utf-8")
+        
+        qa_pairs = []
+
+        # LLMからの出力には余分なテキストが含まれることがあるため、XML部分のみを抽出
+        xml_start = xml_content.find("<QAPairs>")
+        xml_end = xml_content.rfind("</QAPairs>")
+
+        if xml_start != -1 and xml_end != -1:
+            clean_xml = xml_content[xml_start: xml_end + len("</QAPairs>")]
+            
+            try:
+                root = ET.fromstring(clean_xml)
+
+                for pair_node in root.findall('Pair'):
+                    question_node = pair_node.find('Question')
+                    answer_node = pair_node.find('Answer')
+
+                    if question_node is not None and answer_node is not None:
+                        qa_pairs.append({
+                            "question": question_node.text or "",
+                            "answer": answer_node.text or ""
+                        })
+            
+            except ET.ParseError:
+                # XMLパースに失敗した場合、手動でテキスト解析
+                console.print(f"[yellow]XMLパースエラー、手動解析を試行中...[/yellow]")
+                qa_pairs = parse_qa_from_text_fallback(clean_xml)
+
+        return qa_pairs
+
+    except ET.ParseError as parse_error:
+        console.print(
+            f"[bold red]LLMが生成したXMLの解析に失敗しました:[/bold red] {parse_error}"
+        )
+        console.print(f"[dim]受信したテキスト: {xml_content[:200]}...[/dim]")
+        return []
+    except Exception as general_error:
+        console.print(
+            f"[bold red]チャンクとGAペアからのQ&A生成中にエラーが発生しました:[/bold red] "
+            f"{general_error}"
+        )
+        console.print(
+            f"[dim]Genre: {ga_pair['genre']['title']}, "
+            f"Audience: {ga_pair['audience']['title']}[/dim]"
+        )
+        return []
+
+
+def generate_ga_definitions(text_content: str, model: str, num_ga_pairs: int = None) -> str:
+    """litellmを使い、元の文章からGAペア定義のXMLを生成する"""
+    # LLMに渡すテキストは長すぎるとコストや性能に影響するため、先頭部分に限定する
+    context = text_content[:8000]
+    console.print(f"[dim]コンテキスト長: {len(context)} 文字[/dim]")
+
+    prompt_template = get_ga_definition_generation_prompt()
+    prompt = prompt_template.format(
+        context=context,
+        num_ga_pairs=num_ga_pairs if num_ga_pairs is not None else "3-5個の"
+    )
+
+    messages = [
+        {"role": "system", "content": "あなたは、XML形式で厳密に出力する優秀なアシスタントです。"},
+        {"role": "user", "content": prompt}
+    ]
+
+    # OpenRouter用の環境変数設定
+    api_key = os.getenv("OPENROUTER_API_KEY", "")
+    if not api_key:
+        console.print("[bold red]OPENROUTER_API_KEYが設定されていません！[/bold red]")
+        raise ValueError("OPENROUTER_API_KEYが必要です")
+    
+    os.environ["OPENROUTER_API_KEY"] = api_key
+    
+    # OpenRouterのモデル名に変換（必要に応じて）
+    if "openrouter" not in model and not model.startswith("openrouter/"):
+        if model.startswith("gpt-"):
+            model = f"openrouter/openai/{model}"
+        elif model.startswith("claude-"):
+            model = f"openrouter/anthropic/{model}"
+        else:
+            # デフォルトでopenrouterプレフィックスを追加
+            model = f"openrouter/{model}"
+
+    try:
+        response = completion(model=model, messages=messages)
+        xml_content = response.choices[0].message.content
+        console.print(f"[dim]LLMレスポンス長: {len(xml_content)} 文字[/dim]")
+        return xml_content
+    except Exception as error:
+        console.print(f"[bold red]GA定義の生成中にエラーが発生しました:[/bold red] {error}")
+        raise
+
+
+def parse_ga_definitions_from_xml(xml_content: str) -> List[Dict[str, Dict[str, str]]]:
+    """XML形式のGA定義からGAペアのリストを解析する"""
+    pairs = []
+    
+    try:
+        # XMLタグから<GADefinitions>部分を抽出（マークダウンコードブロックを無視）
+        xml_start = xml_content.find("<GADefinitions>")
+        xml_end = xml_content.rfind("</GADefinitions>")
+        
+        if xml_start != -1 and xml_end != -1:
+            clean_xml = xml_content[xml_start: xml_end + len("</GADefinitions>")]
+            
+            # XMLの特殊文字をエスケープ
+            import html
+            clean_xml = html.unescape(clean_xml)
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
+                    # より詳細なチェック
+                    has_genre_title = genre_title_node is not None and genre_title_node.text and genre_title_node.text.strip()
+                    has_genre_desc = genre_desc_node is not None and genre_desc_node.text and genre_desc_node.text.strip()
+                    has_audience_title = audience_title_node is not None and audience_title_node.text and audience_title_node.text.strip()
+                    has_audience_desc = audience_desc_node is not None and audience_desc_node.text and audience_desc_node.text.strip()
+                    
+                    if all([has_genre_title, has_genre_desc, has_audience_title, has_audience_desc]):
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
+                        console.print(f"[green]✓[/green] {genre_title_node.text.strip()} x {audience_title_node.text.strip()}")
+                    else:
+                        console.print(f"[yellow]⚠[/yellow] Pair {i+1}: 必要な要素が不足")
+                else:
+                    console.print(f"[yellow]⚠[/yellow] Pair {i+1}: GenreまたはAudienceノードが見つからない")
+        else:
+            console.print("[yellow]GADefinitionsタグが見つかりませんでした[/yellow]")
+                        
+    except ET.ParseError as parse_error:
+        console.print(f"[bold red]GA定義XMLの解析に失敗しました:[/bold red] {parse_error}")
+        console.print(f"[dim]問題のあるXML: {xml_content[xml_start:xml_start+200] if xml_start != -1 else xml_content[:200]}...[/dim]")
+        
+        # XMLエラーの場合、手動でテキスト解析を試行
+        console.print("[yellow]手動解析を試行中...[/yellow]")
+        pairs = parse_ga_from_text_fallback(xml_content)
+        
+    except Exception as e:
+        console.print(f"[bold red]予期しないエラー:[/bold red] {e}")
+    
+    return pairs
+
+
+def parse_ga_from_text_fallback(content: str) -> List[Dict[str, Dict[str, str]]]:
+    """XMLパースに失敗した場合のフォールバック：テキストから直接解析"""
+    pairs = []
+    
+    try:
+        # <Pair>タグで分割
+        pair_sections = content.split('<Pair>')
+        
+        for section in pair_sections[1:]:  # 最初の要素は空なのでスキップ
+            if '</Pair>' not in section:
+                continue
+                
+            pair_content = section.split('</Pair>')[0]
+            
+            # Title要素を抽出
+            genre_title = extract_text_between_tags(pair_content, 'Genre', 'Title')
+            genre_desc = extract_text_between_tags(pair_content, 'Genre', 'Description')
+            audience_title = extract_text_between_tags(pair_content, 'Audience', 'Title')
+            audience_desc = extract_text_between_tags(pair_content, 'Audience', 'Description')
+            
+            if all([genre_title, genre_desc, audience_title, audience_desc]):
+                pairs.append({
+                    "genre": {
+                        "title": genre_title.strip(),
+                        "description": genre_desc.strip()
+                    },
+                    "audience": {
+                        "title": audience_title.strip(),
+                        "description": audience_desc.strip()
+                    }
+                })
+                console.print(f"[green]✓[/green] (手動解析) {genre_title} x {audience_title}")
+    
+    except Exception as e:
+        console.print(f"[red]手動解析も失敗:[/red] {e}")
+    
+    return pairs
+
+
+def extract_text_between_tags(content: str, parent_tag: str, child_tag: str) -> str:
+    """指定されたタグ間のテキストを抽出"""
+    try:
+        # 親タグ内を探す
+        parent_start = content.find(f'<{parent_tag}>')
+        parent_end = content.find(f'</{parent_tag}>')
+        
+        if parent_start == -1 or parent_end == -1:
+            return ""
+            
+        parent_content = content[parent_start:parent_end]
+        
+        # 子タグ内のテキストを抽出
+        child_start = parent_content.find(f'<{child_tag}>')
+        child_end = parent_content.find(f'</{child_tag}>')
+        
+        if child_start == -1 or child_end == -1:
+            return ""
+            
+        return parent_content[child_start + len(f'<{child_tag}>'):child_end]
+    
+    except Exception:
+        return ""
+
+
+def parse_qa_from_text_fallback(content: str) -> List[Dict[str, str]]:
+    """Q&A XMLパースに失敗した場合のフォールバック：テキストから直接解析"""
+    qa_pairs = []
+    
+    try:
+        # <Pair>タグで分割
+        pair_sections = content.split('<Pair>')
+        
+        for section in pair_sections[1:]:  # 最初の要素は空なのでスキップ
+            if '</Pair>' not in section:
+                continue
+                
+            pair_content = section.split('</Pair>')[0]
+            
+            # Question と Answer を抽出
+            question = extract_simple_tag_content(pair_content, 'Question')
+            answer = extract_simple_tag_content(pair_content, 'Answer')
+            
+            if question and answer:
+                qa_pairs.append({
+                    "question": question.strip(),
+                    "answer": answer.strip()
+                })
+                console.print(f"[green]✓[/green] (手動解析) Q&A追加")
+    
+    except Exception as e:
+        console.print(f"[red]Q&A手動解析も失敗:[/red] {e}")
+    
+    return qa_pairs
+
+
+def extract_simple_tag_content(content: str, tag: str) -> str:
+    """シンプルなタグ内のテキストを抽出"""
+    try:
+        start_tag = f'<{tag}>'
+        end_tag = f'</{tag}>'
+        
+        start_pos = content.find(start_tag)
+        end_pos = content.find(end_tag)
+        
+        if start_pos == -1 or end_pos == -1:
+            return ""
+            
+        return content[start_pos + len(start_tag):end_pos]
+    
+    except Exception:
+        return ""
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
+def convert_to_xml_by_genre(all_qa_pairs: List[Dict[str, str]]) -> Dict[str, str]:
+    """Q&AペアのリストをGenreごとにグループ化し、整形されたXML文字列の辞書に変換する"""
+    grouped_by_genre = defaultdict(list)
+
+    for item in all_qa_pairs:
+        grouped_by_genre[item["genre"]].append(item)
+
+    xml_outputs = {}
+    for genre, pairs in grouped_by_genre.items():
+        root = ET.Element("QAPairs")
+        root.set("genre", genre)
+
+        for item in pairs:
+            pair_elem = ET.SubElement(root, "Pair")
+
+            audience_elem = ET.SubElement(pair_elem, "Audience")
+            audience_elem.text = item["audience"]
+
+            question_elem = ET.SubElement(pair_elem, "Question")
+            question_elem.text = item["question"]
+
+            answer_elem = ET.SubElement(pair_elem, "Answer")
+            answer_elem.text = item["answer"]
+
+        rough_string = ET.tostring(root, 'utf-8')
+        reparsed = minidom.parseString(rough_string)
+        xml_outputs[genre] = reparsed.toprettyxml(indent="  ")
+
+    return xml_outputs
diff --git a/easy_dataset_cli/main.py b/easy_dataset_cli/main.py
new file mode 100644
index 0000000..28adbaf
--- /dev/null
+++ b/easy_dataset_cli/main.py
@@ -0,0 +1,223 @@
+# easy_dataset_cli/main.py
+"""CLIエントリーポイント"""
+
+from pathlib import Path
+from typing_extensions import Annotated
+import typer
+from rich.console import Console
+from rich.progress import Progress
+from dotenv import load_dotenv
+
+from .core import (
+    split_text,
+    parse_ga_file,
+    generate_qa_for_chunk_with_ga,
+    convert_to_xml_by_genre,
+    generate_ga_definitions,
+    parse_ga_definitions_from_xml,
+    save_ga_definitions_by_genre,
+    create_output_directories
+)
+
+# .envファイルを読み込む
+load_dotenv()
+
+app = typer.Typer(
+    help="テキストファイルからQ&Aペアを生成するシンプルなCLIツール。",
+    context_settings={"help_option_names": ["-h", "--help"]}
+)
+console = Console()
+
+
+def sanitize_filename(name: str) -> str:
+    """ファイル名として安全な文字列に変換する"""
+    return "".join(c for c in name if c.isalnum() or c in (' ', '_', '-')).rstrip()
+
+
+@app.command()
+def create_ga(
+    file_path: Annotated[Path, typer.Argument(
+        exists=True, dir_okay=False, readable=True,
+        help="GAペアの定義を生成するための元のテキストファイル。"
+    )],
+    output_dir: Annotated[Path, typer.Option(
+        "--output-dir", "-o", file_okay=False, dir_okay=True, writable=True,
+        help="生成されたGAペア定義ファイルを保存するディレクトリ。"
+    )],
+    model: Annotated[str, typer.Option(
+        "--model", "-m",
+        help="GAペア定義の生成に使用するLLMモデル名。"
+    )] = "openrouter/openai/gpt-4o",
+    num_ga_pairs: Annotated[int, typer.Option(
+        "--num-ga-pairs", "-g",
+        help="生成するGAペアの数。指定しない場合はLLMが適切な数を決定します。"
+    )] = None,
+):
+    """元の文章を分析し、GAペア定義をXML形式で生成し、Genreごとにマークダウンファイルに保存します。"""
+    console.print(f"ファイルを読み込んでいます: [cyan]{file_path}[/cyan]")
+
+    try:
+        text = file_path.read_text(encoding="utf-8")
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
+
+        # 元のXMLファイルをgaディレクトリに保存（クリーンなXMLのみ）
+        xml_file_path = dirs["ga"] / "ga_definitions.xml"
+        # XMLタグ部分のみを抽出して保存
+        xml_start = xml_content.find("<GADefinitions>")
+        xml_end = xml_content.rfind("</GADefinitions>")
+        if xml_start != -1 and xml_end != -1:
+            clean_xml = xml_content[xml_start: xml_end + len("</GADefinitions>")]
+            xml_file_path.write_text(clean_xml, encoding="utf-8")
+            console.print(f"[green]✓[/green] GA定義XMLファイルを保存しました: [cyan]{xml_file_path}[/cyan]")
+
+        # Genreごとにマークダウンファイルをgaディレクトリに保存
+        save_ga_definitions_by_genre(ga_pairs, dirs["ga"])
+
+        console.print(
+            f"\n[bold green]✓[/bold green] {len(ga_pairs)}個のGAペアを "
+            f"[cyan]{dirs['ga']}[/cyan] に保存しました。"
+        )
+        console.print(
+            "[yellow]ヒント: 生成されたファイルをレビューし、必要に応じて編集してから "
+            "`generate` コマンドで使用してください。[/yellow]"
+        )
+
+    except Exception as e:
+        console.print(
+            f"[bold red]GA定義ファイルの生成中にエラーが発生しました:[/bold red] {e}"
+        )
+        raise typer.Exit(code=1)
+
+
+@app.command()
+def generate(
+    file_path: Annotated[Path, typer.Argument(
+        exists=True, dir_okay=False, readable=True,
+        help="元のテキストファイルへのパス。"
+    )],
+    ga_file: Annotated[Path, typer.Option(
+        "--ga-file", "-g", exists=True, dir_okay=False, readable=True,
+        help="Genre-Audienceペアを定義したXMLまたはMarkdownファイルへのパス。gaディレクトリのga_definitions.xmlを推奨。"
+    )],
+    output_dir: Annotated[Path, typer.Option(
+        "--output-dir", "-o", file_okay=False, dir_okay=True, writable=True,
+        help="生成されたXMLファイルを保存するディレクトリ。指定しない場合はコンソールに出力します。"
+    )] = None,
+    model: Annotated[str, typer.Option(
+        "--model", "-m",
+        help="Q&Aペアの生成に使用するLLMモデル名。"
+    )] = "openrouter/openai/gpt-oss-120b",
+    chunk_size: Annotated[int, typer.Option(
+        help="テキストチャンクの最大サイズ。"
+    )] = 2000,
+    chunk_overlap: Annotated[int, typer.Option(
+        help="チャンク間のオーバーラップサイズ。"
+    )] = 200,
+    num_qa_pairs: Annotated[int, typer.Option(
+        "--num-qa-pairs", "-q",
+        help="各チャンク・GAペアの組み合わせで生成するQ&Aペアの数。指定しない場合はLLMが適切な数を決定します。"
+    )] = None,
+):
+    """テキストファイルとGA定義からQ&Aペアを生成し、Genre別のXMLファイルとして出力します。"""
+    try:
+        console.print(f"ファイルを読み込んでいます: [cyan]{file_path}[/cyan]")
+        text = file_path.read_text(encoding="utf-8")
+
+        console.print(f"GAペアを解析しています: [cyan]{ga_file}[/cyan]")
+        ga_pairs = parse_ga_file(ga_file)
+
+        if not ga_pairs:
+            console.print("[bold red]有効なGAペアが定義ファイルに見つかりませんでした。[/bold red]")
+            raise typer.Exit(code=1)
+
+        console.print(f"[green]{len(ga_pairs)}[/green] 個のGAペアを見つけました。")
+
+        console.print("テキストをチャンクに分割しています...")
+        chunks = split_text(text, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
+        console.print(f"[green]{len(chunks)}[/green] 個のチャンクを作成しました。")
+
+        all_qa_pairs_with_ga = []
+        total_tasks = len(chunks) * len(ga_pairs)
+        
+        # 出力ディレクトリがある場合は構造を作成
+        dirs = None
+        if output_dir:
+            dirs = create_output_directories(output_dir)
+            console.print(f"[dim]出力ディレクトリを作成しました: ga/, logs/, qa/[/dim]")
+
+        with Progress(console=console) as progress:
+            task = progress.add_task("[green]Q&Aペアを生成中...", total=total_tasks)
+
+            for chunk in chunks:
+                for ga_pair in ga_pairs:
+                    qa_pairs = generate_qa_for_chunk_with_ga(
+                        chunk, model=model, ga_pair=ga_pair, 
+                        logs_dir=dirs["logs"] if dirs else None,
+                        num_qa_pairs=num_qa_pairs
+                    )
+
+                    for pair in qa_pairs:
+                        all_qa_pairs_with_ga.append({
+                            "genre": ga_pair['genre']['title'],
+                            "audience": ga_pair['audience']['title'],
+                            "question": pair['question'],
+                            "answer": pair['answer'],
+                        })
+
+                    progress.update(
+                        task, advance=1,
+                        description=f"Genre: {ga_pair['genre']['title']}"
+                    )
+
+        console.print(
+            f"\n合計 [bold green]{len(all_qa_pairs_with_ga)}[/bold green] "
+            "個のQ&Aペアを生成しました。"
+        )
+
+        xml_outputs_by_genre = convert_to_xml_by_genre(all_qa_pairs_with_ga)
+
+        if dirs:
+            console.print(f"XMLファイルを [cyan]{dirs['qa']}[/cyan] に保存しています...")
+
+            for genre, xml_content in xml_outputs_by_genre.items():
+                safe_genre_name = sanitize_filename(genre)
+                output_file_path = dirs["qa"] / f"{safe_genre_name}.xml"
+                output_file_path.write_text(xml_content, encoding="utf-8")
+                console.print(f"  - [green]✓[/green] {output_file_path.name}")
+
+            console.print("\n[bold green]すべてのファイルの保存が完了しました。[/bold green]")
+        else:
+            console.print("\n--- 生成されたQ&Aペア (Genre別XML) ---")
+            for genre, xml_content in xml_outputs_by_genre.items():
+                console.print(f"\n[bold yellow]## Genre: {genre} ##[/bold yellow]")
+                console.print(xml_content, overflow="fold")
+    
+    except Exception as e:
+        console.print(f"[bold red]エラーが発生しました:[/bold red] {e}")
+        raise typer.Exit(code=1)
+
+
+if __name__ == "__main__":
+    app()
diff --git a/easy_dataset_cli/prompts.py b/easy_dataset_cli/prompts.py
new file mode 100644
index 0000000..5b2c825
--- /dev/null
+++ b/easy_dataset_cli/prompts.py
@@ -0,0 +1,25 @@
+# easy_dataset_cli/prompts.py
+"""LLMプロンプト定義とマークダウンファイル読み込み"""
+
+from pathlib import Path
+
+
+def load_prompt_template(template_name: str) -> str:
+    """プロンプトテンプレートをマークダウンファイルから読み込む"""
+    prompt_dir = Path(__file__).parent / "prompts"
+    template_path = prompt_dir / f"{template_name}.md"
+    
+    if not template_path.exists():
+        raise FileNotFoundError(f"プロンプトテンプレートが見つかりません: {template_path}")
+    
+    return template_path.read_text(encoding="utf-8")
+
+
+def get_qa_generation_prompt() -> str:
+    """Q&A生成プロンプトを取得"""
+    return load_prompt_template("qa_generation")
+
+
+def get_ga_definition_generation_prompt() -> str:
+    """GA定義生成プロンプトを取得"""
+    return load_prompt_template("ga_definition_generation")
diff --git a/easy_dataset_cli/prompts/ga_definition_generation.md b/easy_dataset_cli/prompts/ga_definition_generation.md
new file mode 100644
index 0000000..757afcd
--- /dev/null
+++ b/easy_dataset_cli/prompts/ga_definition_generation.md
@@ -0,0 +1,47 @@
+# 役割: GA（Genre-Audience）ペア定義の専門家
+
+あなたは、与えられた文章の内容を分析し、最適なGenre（体裁）とAudience（読者）のペアを提案する専門家です。
+
+## 指示:
+1. 与えられた文章の内容、トピック、専門性レベルを分析してください。
+2. この文章から質問と回答のペアを生成する際に最適となる{num_ga_pairs}個のGenre-Audienceペアを提案してください。
+3. 各Genreは異なる文体・形式（学術論文、技術ブログ、教科書、FAQ、対話形式など）を表現してください。
+4. 各Audienceは異なる知識レベル・立場（初心者、学生、専門家、実務者など）を表現してください。
+5. 文章の内容に適したペアを選択し、多様性を確保してください。
+
+## 文章:
+---
+{context}
+---
+
+## 出力形式:
+**必ず**、ルート要素が `<GADefinitions>` である単一の有効なXMLとして応答してください。XML以外の説明文は一切含めないでください。
+各GAペアは `<Pair>` タグで囲み、その中に `<Genre>` と `<Audience>` タグを含めてください。
+
+## 出力例:
+\```xml
+<GADefinitions>
+<Pair>
+<Genre>
+<Title>FAQ</Title>
+<Description>ユーザーがゲームに関する特定の質問に素早くアクセスできるような形式で、よくある質問に対する回答を簡潔にまとめる。</Description>
+</Genre>
+<Audience>
+<Title>初心者ゲーマー</Title>
+<Description>東方Projectや弾幕系シューティングゲームを初めてプレイする人々。ゲームの基本的な情報や攻略のヒントが欲しい。</Description>
+</Audience>
+</Pair>
+<Pair>
+<Genre>
+<Title>テクニカルガイド</Title>
+<Description>ゲームシステム、必要環境、インストール方法などの技術的な詳細を説明する形式。特に技術的な詳細に焦点を当てる。</Description>
+</Genre>
+<Audience>
+<Title>PCゲーミング愛好者</Title>
+<Description>PCでのゲームプレイに慣れているが、特に東方シリーズに関する技術的な詳細とトラブルシューティングガイドが求められる愛好者。</Description>
+</Audience>
+</Pair>
+</GADefinitions>
+\```
+
+それでは、最適なGA定義の生成を開始してください。
diff --git a/easy_dataset_cli/prompts/qa_generation.md b/easy_dataset_cli/prompts/qa_generation.md
new file mode 100644
index 0000000..e51c26f
--- /dev/null
+++ b/easy_dataset_cli/prompts/qa_generation.md
@@ -0,0 +1,46 @@
+# 役割: Q&Aペア生成の専門家（体裁・読者対応版）
+
+あなたは、与えられた文章から高品質な質問と回答のペアを作成する専門家です。特に、指定された「体裁」と「読者」に合わせてスタイルを調整する能力に長けています。
+
+## 指示:
+1. 与えられた「文章」を注意深く読んでください。
+2. 指定された「目標とする体裁」と「目標とする読者」の役割になりきってください。
+3. 文章に書かれている情報**のみ**に基づいて、{num_qa_pairs}個のユニークで洞察に富んだQ&Aペアを生成してください。
+4. 質問のスタイルと複雑さは、「目標とする読者」の視点に合わせてください。
+5. 回答のスタイル、トーン、詳細さは、「目標とする体裁」に合わせてください。
+
+## 目標とする体裁:
+{genre_title}
+{genre_description}
+
+## 目標とする読者:
+{audience_title}
+{audience_description}
+
+## 文章:
+---
+{context}
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
diff --git a/example/input/documents/Touhou_Chireiden.md b/example/input/documents/Touhou_Chireiden.md
new file mode 100644
index 0000000..80f2304
--- /dev/null
+++ b/example/input/documents/Touhou_Chireiden.md
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
+    『求聞口授』によれば、豪快かつ竹を割ったような性格で、「力強い者」「勇気ある者」を好み、「軟弱な者」「卑怯な者」を嫌う。幻想郷最強の種族とされる鬼の中でも屈指の怪力の持ち主で、友人である萃香は「肉体を使った力は自分より強いかも」と述べている。また、「語られる怪力乱神」と呼ばれることがある。そのため、力による支配がルールとされている旧地獄には敵が存在せず、「地底世界は私達の楽園」と語っている[9]。手加減したとはいえ、人間でありながら自分に勝利した霊夢たちを気に入ったらしく、魔理沙を地底の宴会によく誘っている[10]。
+    星のマークが入った巨大な赤い盃を持ち歩いている。これは「星熊盃」と呼ばれる鬼の名品の一つであり、注がれた酒を一瞬にして最高ランクの純米大吟醸に変えることができる[9]。
+
+#### 古明地 さとり（こめいじ さとり）
+
+    [さとり](/wiki/%E8%A6%9A "覚")。旧灼熱獄跡の上に建てられた「地霊殿」の主であり、古明地こいしの姉。
+    「**心を読む程度の能力** 」を持ち、左胸部の「サード・アイ」で相手の心を読むことができる。他人の心を見透かす能力ゆえに、嫌われ者として地底に封じられた妖怪の中でも群を抜いて恐れられている存在であり、旧地獄において屈指の実力を持つ大物でもある。ただし、戦闘は余り得意ではないらしい[11]。妹のこいし曰く「お姉ちゃんの知り合いだと言えば、地底では誰も逆らわない」。また、言葉を持たない幽霊や怨霊からも苦手とされており、この能力を活かして閻魔から灼熱地獄跡の怨霊の管理を任されている。『求聞口授』では、神である八坂神奈子が霊烏路空に力を授ける際にも、彼女との接触を避けるべく注意を払っていたとされている[12]。
+    彼女自身も自分が忌み嫌われる存在であることを理解しているため、他者との接触やコミュニケーションを拒絶し、住居である地霊殿に引き籠もっている。その代わり、言葉を話せない動物からは好かれているらしく、地霊殿には彼女を慕うペットたちが数多く住んでいる。その中には怨霊や[魑魅魍魎](/wiki/%E9%AD%91%E9%AD%85%E9%AD%8D%E9%AD%8E "魑魅魍魎")を喰らうことで力をつけ、妖怪化した者たちもいる。そのため、普段は屋敷や旧地獄の管理、妹や他のペットの世話などを彼女らに任せ、自分は読書をしたり小説を書いたりして暮らしている[11]。
+    『地霊殿』では、地霊殿を訪れた博麗霊夢や霧雨魔理沙の心を読んで地底を訪れた目的を探ろうとするが、異変の解決に消極的だった2人からは目的を上手く探ることができなかった。言動と考えの一致しない2人を不審に思い、対戦する。その後はペットのいる灼熱地獄跡へ案内する。対戦時は、自身の能力で霊夢や魔理沙の記憶の中にある「[トラウマ](/wiki/%E3%83%88%E3%83%A9%E3%82%A6%E3%83%9E "トラウマ")」を読み取り、それを再現した攻撃を行う。具体的な作中描写としては、パートナーとして選択した妖怪が過去の作品で使用したスペルカードを真似たものを、さとり自身のスペルカードとして使用する。
+
+#### 火焔猫 燐（かえんびょう りん）
+
+    [火車](/wiki/%E7%81%AB%E8%BB%8A_\(%E5%A6%96%E6%80%AA\) "火車 \(妖怪\)")。古明地さとりのペットの1人であり、灼熱地獄跡で怨霊の管理や死体運びを任されている。灼熱地獄跡が本当の地獄だった頃から生きており、努力の末に死体や怨霊を操る能力を会得し[13]、彼らと会話・意思疎通ができる。さとりのペットとなった時期は地底界が地獄から切り離された頃で、同じくペットの霊烏路空とはその頃からの古い友人。
+    力を手に入れて調子に乗る空に呆れながらも、暴走が主人のさとりや旧地獄の住人に知られて彼女が処罰されることを恐れ、地上に怨霊を送り込むことで地上の妖怪に異変を知らせ、空を止めさせようと試みた。しかし、意に反して現れたのは人間だったため、その実力を試すために対戦する。
+    作中では猫の鳴き声のような効果音と共に黒猫の姿で何度も登場し、中ボスとして対戦する。5面ボス戦前の会話イベントで「猫の姿では会話ができない」として人型に変身する。変身後の姿では猫耳を持つが、側頭部に人の耳も付いている。
+    死体を好む妖怪である火車であり、『地霊殿』では霊夢や魔理沙の死体を得たいと当人に話している。『地霊殿』や『求聞口授』では、地上でときどき発生する人間の死体が盗まれる事件の犯人がお燐であることが示唆されている[14]。萃香の言によれば、彼女に死体を奪われた死者はそのまま怨霊と化し、あの世に行くこともできなくなってしまうという。死体は最終的には「燃料」として灼熱地獄の炎の中へ放り込んでしまう[_[要出典](/wiki/Wikipedia:%E3%80%8C%E8%A6%81%E5%87%BA%E5%85%B8%E3%80%8D%E3%82%92%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E3%81%95%E3%82%8C%E3%81%9F%E6%96%B9%E3%81%B8 "Wikipedia:「要出典」をクリックされた方へ")_]。
+    自分の本名が長いことを嫌っており、皆に「お燐」と呼ばせている。会話イベントでも通称である「お燐」という名前が表示され、作中では本名が表示されない。本名は『地霊殿』付属の「キャラ設定.txt」に記載されている。『ダブルスポイラー』でも「お燐」名義で登場する。
+
+#### 霊烏路 空（れいうじ うつほ）
+
+    地獄の妖怪[固有種](/wiki/%E5%9B%BA%E6%9C%89%E7%A8%AE "固有種")である「地獄烏」[15]。古明地さとりのペットで、お燐と共に灼熱地獄跡の管理を任されており、空は火力調節を担当する。
+    ある日、幻想郷の産業革命計画を計った八坂神奈子と洩矢諏訪子の2柱によって太陽の化身である神霊「[八咫烏](/wiki/%E5%85%AB%E5%92%AB%E7%83%8F "八咫烏")」の力を与えられ、「**核融合を操る程度の能力** 」を手に入れた。しかし、彼女はその強大な力に溺れて能力を濫用し、遂には間欠泉を噴出させる異変を引き起こす。その後、異変解決のために灼熱地獄跡を訪れた霊夢や魔理沙に対して「地上へ進出して世界を灼熱地獄に変える」という野望を明かし勝負を挑むが、撃退され改心する。後にお燐と共に博麗神社を訪れ、「二人組の神様」から能力をもらったことを霊夢と魔理沙に告げる。お燐から「[鳥頭](/wiki/%E9%B3%A5%E9%A0%AD "鳥頭")」と揶揄されるほど記憶力に欠け、神から力を与えられた理由などは完全に記憶から抜け落ちていたため、さとりの能力を使用しても読み取ることができなかった。
+    その後は、神奈子の指示で地底に建造された核融合研究施設である「間欠泉地下センター」で、何らかの仕事をしている。『非想天則』では、センターに入り込んだ東風谷早苗やチルノを「異物」として排除するために現れた。
+    八咫烏の力を取り込んだ彼女は、その影響により元の姿から大きく変化したとされる。左足は電子のようなものが周囲を漂う「分解の足」、右足は金属の塊のような「融合の足」、右手は多角柱の制御棒である「第三の足」となり、これらの「三本の足」で核融合反応を操作する。また、胸には巨大な鳥の目のような「赤の目」が存在する[15]。対戦時には核の力を使ったスペルカードを使用し、スペルカード発動時にはメルトダウンのようなアラートと共に「[☢](/wiki/%E6%94%BE%E5%B0%84%E7%B7%9A#概要 "放射線") CAUTION!!」の文字が表示される。
+    皆から「おくう」と呼ばれているとされ[16]、実際にお燐や古明地こいしは作中で「おくう」と呼んでいるが、お燐とは異なり、会話イベントでは本名が表示される。『ダブルスポイラー』では射命丸文から「お空さん」と呼ばれている。
+
+#### 古明地こいし（こめいじ こいし）
+
+    古明地さとりの妹。姉と同じく種族は「さとり」で、元々はこいしも心を読む能力を持っていたが、能力のせいで皆に嫌われることを知ったため、サード・アイを閉じて能力を封印し、心を閉ざしてしまう。その結果、本来の心を読む能力に代わり、新たに「**無意識を操る程度の能力** 」を手に入れた。これによって誰からも気づかれずにフラフラと出かけては帰ってくるという妖怪となっている。さらに、姉のさとりも、閉ざされたこいしの心だけは読むことができなくなった。こいしを不憫に思ったさとりから、こいしと遊ぶための専属のペットを与えられている。そのおかげか、少しずつではあるがこいしも以前とは変わってきたようである。
+    博麗霊夢や霧雨魔理沙が地底にやって来てさとりやお燐、霊烏路空と戦いを繰り広げたことを聞き、中でも八咫烏を取り込んだ空の驚異的な能力アップに興味を示す。自分のペットも空のように強化してもらおうと思ったこいしは、妖怪の山の守矢神社を目指すことにする。『地霊殿』Extraステージでは、天狗が警備する妖怪の山を誰にも気付かれることなく侵入し、その先で博麗霊夢や霧雨魔理沙と遭遇している。作中では射命丸文やパチュリー・ノーレッジからは、全く気配を感じない存在だと言われている。
+
+### 既存の登場人物
+
+
+ここでは、『地霊殿』が初出ではない登場人物を解説する。 
+
+#### [博麗霊夢](/wiki/%E5%8D%9A%E9%BA%97%E9%9C%8A%E5%A4%A2 "博麗霊夢")
+
+    博麗神社の巫女。温泉を止める気はない。
+
+#### [霧雨魔理沙](/wiki/%E9%9C%A7%E9%9B%A8%E9%AD%94%E7%90%86%E6%B2%99 "霧雨魔理沙")
+
+    魔法使いの少女。間欠泉に興味津々。
+
+#### 八雲紫
+
+    古い妖怪。地上の妖怪と地底の妖怪が干渉することに難色を示し、人間である霊夢を地底に送る。霊夢の陰陽玉に通信機能を付けた。
+
+#### 伊吹萃香
+
+    地底に住んでいた鬼。自分で地底に行っても問題はないのだが、紫の作戦が面白そうだったので霊夢のサポートに回る。
+
+#### 射命丸文
+
+    山に住む鴉天狗で、新聞記者。山の神々と河童の不穏な動きを調査していたところ地底が怪しいことをつかんだため、霊夢を利用して調査させる。
+
+#### [アリス・マーガトロイド](/wiki/%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%BB%E3%83%9E%E3%83%BC%E3%82%AC%E3%83%88%E3%83%AD%E3%82%A4%E3%83%89 "アリス・マーガトロイド")
+
+    人形を操る妖怪。紫に作ってもらった遠隔操作できる人形で、魔理沙をサポートする。
+
+#### [パチュリー・ノーレッジ](/wiki/%E3%83%91%E3%83%81%E3%83%A5%E3%83%AA%E3%83%BC%E3%83%BB%E3%83%8E%E3%83%BC%E3%83%AC%E3%83%83%E3%82%B8 "パチュリー・ノーレッジ")
+
+    [紅魔館](/wiki/%E5%B9%BB%E6%83%B3%E9%83%B7#紅魔館 "幻想郷")の魔法使い。間欠泉から湧いた霊の正体が有害な「怨霊」であることに気付き、紫に相談する。
+
+#### 河城にとり
+
+    山に住む河童。山の神々が地底に核融合炉を作ったという情報に興味を示す。霊夢が妖怪に促されて地底に潜るという話を聞いたため、先を越されることをおそれて魔理沙をけしかけて地底に送る。
+
+#### [東風谷早苗](/wiki/%E6%9D%B1%E9%A2%A8%E8%B0%B7%E6%97%A9%E8%8B%97 "東風谷早苗")
+
+    守矢神社の風祝。神社へやってきた霊夢たちに、挨拶と称して勝負を挑んでくる。
+
+#### 八坂神奈子、洩矢諏訪子
+
+    守矢神社の神々。霊烏路空に核融合の力を与え、『地霊殿』での一連の騒動の原因を作った張本人。
+
+## ステージ
+
+
+ステージ | ステージタイトル | 場所 | 中ボス | ボス   
+---|---|---|---|---  
+Stage 1  | 忘恩の地から吹く風 | 幻想風穴 | キスメ | 黒谷ヤマメ   
+Stage 2  | 地上と過去を結ぶ深道 | 地獄の深道 | 水橋パルスィ | 水橋パルスィ   
+Stage 3  | 忘れられた雪の旧都 | 旧地獄街道 | 星熊勇儀 | 星熊勇儀   
+Stage 4  | 誰からも好かれない恐怖の目 | 地霊殿 | 火焔猫燐（猫の姿） | 古明地さとり   
+Stage 5  | 昔時の業火 | 灼熱地獄跡 | 火焔猫燐（猫の姿） | 火焔猫燐   
+Stage 6  | 荒々しき二つ目の太陽 | 地底都市最深部 | 火焔猫燐 | 霊烏路空   
+Extra Stage  | 地獄のラブリービジター | 守矢神社 | 東風谷早苗 | 古明地こいし   
+  
+## 曲目リスト
+
+
+  1. 地霊達の起床 - タイトル
+  2. 暗闇の風穴 - 1面のテーマ
+  3. 封じられた妖怪 〜 Lost Place - 黒谷ヤマメのテーマ
+  4. 渡る者の途絶えた橋 - 2面のテーマ
+  5. 緑眼のジェラシー - 水橋パルスィのテーマ
+  6. 旧地獄街道を行く - 3面のテーマ
+  7. 華のさかづき大江山 - 星熊勇儀のテーマ
+  8. ハートフェルトファンシー - 4面のテーマ
+  9. 少女さとり 〜 3rd eye - 古明地さとりのテーマ
+  10. 廃獄ララバイ - 5面のテーマ
+  11. 死体旅行 〜 Be of good cheer! - 火焔猫燐のテーマ
+  12. 業火マントル - 6面のテーマ
+  13. 霊知の太陽信仰 〜 Nuclear Fusion - 霊烏路空のテーマ
+  14. ラストリモート - Extraのテーマ
+  15. ハルトマンの妖怪少女 - 古明地こいしのテーマ
+  16. 地霊達の帰宅 - エンディング
+  17. エネルギー黎明 〜 Future Dream... - スタッフロール
\ No newline at end of file
diff --git a/example/input/documents/sample_document.txt b/example/input/documents/sample_document.txt
new file mode 100644
index 0000000..657ab96
--- /dev/null
+++ b/example/input/documents/sample_document.txt
@@ -0,0 +1,14 @@
+Pythonは1991年にGuido van Rossumによって開発されたプログラミング言語です。Pythonの設計哲学は「読みやすさ」を重視しており、シンプルで理解しやすい構文が特徴です。
+
+Pythonはインタープリター型言語であり、コンパイルの必要がないため、開発とテストのサイクルが高速です。また、動的型付けを採用しているため、変数の型を事前に宣言する必要がありません。
+
+Pythonの主な特徴として以下が挙げられます：
+- 豊富な標準ライブラリ
+- クロスプラットフォーム対応
+- オブジェクト指向プログラミングのサポート
+- 関数型プログラミングの要素
+- 大規模なコミュニティとエコシステム
+
+Pythonは様々な分野で活用されています。Web開発ではDjangoやFlaskなどのフレームワークが人気です。データサイエンス分野では、NumPy、Pandas、Matplotlibなどのライブラリが広く使用されています。機械学習では、TensorFlowやPyTorchなどの強力なライブラリが利用可能です。
+
+Pythonの学習は比較的容易で、初心者にも優しい言語として知られています。しかし、その一方で高度な機能も提供しており、専門的な開発にも十分対応できる言語です。
\ No newline at end of file
diff --git a/example/input/documents/sample_ga_definition.md b/example/input/documents/sample_ga_definition.md
new file mode 100644
index 0000000..8e20c5d
--- /dev/null
+++ b/example/input/documents/sample_ga_definition.md
@@ -0,0 +1,21 @@
+# Genre: 学術論文
+学術的で厳密な表現を用い、専門用語を正確に使用し、論理的で客観的な回答を提供します。
+
+# Audience: 大学生
+大学レベルの知識を持つ学習者向けに、基礎概念から応用まで段階的に説明します。
+
+---
+
+# Genre: 技術ブログ
+実践的で親しみやすい表現を用い、具体例やコード例を交えて説明します。
+
+# Audience: エンジニア
+実務経験のある開発者向けに、実装の詳細や最適化のポイントを重視した内容を提供します。
+
+---
+
+# Genre: 教科書
+体系的で網羅的な説明を行い、学習の順序を考慮した構成で知識を整理します。
+
+# Audience: 初心者
+プログラミングや技術分野の初学者向けに、基本概念から丁寧に解説します。
\ No newline at end of file
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
