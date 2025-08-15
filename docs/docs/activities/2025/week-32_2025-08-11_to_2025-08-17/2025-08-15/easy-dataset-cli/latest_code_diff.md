# 🔄 Latest Code Changes

```diff
diff --git a/.SourceSageignore b/.SourceSageignore
index a029c83..ac8bce0 100644
--- a/.SourceSageignore
+++ b/.SourceSageignore
@@ -52,3 +52,4 @@ repository_summary.md
 venv
 .venv
 
+uv.lock
diff --git a/.env.example b/.env.example
new file mode 100644
index 0000000..72d7c7d
--- /dev/null
+++ b/.env.example
@@ -0,0 +1,2 @@
+OPENROUTER_API_KEY=sk-or-xxxx
+HUGGINGFACE_TOKEN=hf_xxxx
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
index 27bea1e..49e8d17 100644
--- a/README.md
+++ b/README.md
@@ -1,15 +1,38 @@
-# Easy Dataset CLI
+<div align="center">
 
-テキストファイルからQ&Aペアを生成するシンプルなCLIツールです。LLMを使用してGenre-Audienceペアに基づいた多様なQ&Aデータセットを作成し、Genre別のXMLファイルとして出力します。
+![](https://github.com/user-attachments/assets/865632a4-911f-4de4-867d-c65cef365d79)
 
-## 特徴
+# 🚀 Easy Dataset CLI
 
-- **シンプル**: データベース不要、マークダウンでGA定義
-- **柔軟**: 複数のGenre-Audienceペアに対応
-- **安定**: LLMからの直接XML出力で信頼性向上
-- **効率的**: テキスト分割とバッチ処理で大きなファイルにも対応
+<p align="center">
+  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python Version">
+  <img src="https://img.shields.io/badge/CLI-Typer-green.svg" alt="CLI Framework">
+  <img src="https://img.shields.io/badge/LLM-OpenAI%20%7C%20OpenRouter-orange.svg" alt="LLM Support">
+  <img src="https://img.shields.io/badge/Format-Alpaca%20%7C%20XML-purple.svg" alt="Output Format">
+  <img src="https://img.shields.io/badge/🤗-Hugging%20Face-yellow.svg" alt="Hugging Face">
+  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
+</p>
 
-## インストール
+<p align="center">
+  テキストファイルからQ&Aペアを生成するシンプルなCLIツール<br>
+  LLMを使用してGenre-Audienceペアに基づいた多様なQ&Aデータセットを作成し、<br>
+  <strong>Alpaca形式JSON</strong>やGenre別XMLファイルとして出力、<strong>Hugging Face Hub</strong>への直接アップロードも対応
+</p>
+
+</div>
+
+## ✨ 特徴
+
+- **🎯 シンプル**: データベース不要、マークダウンでGA定義
+- **🔄 柔軟**: 複数のGenre-Audienceペアに対応
+- **🛡️ 安定**: LLMからの直接XML出力で信頼性向上
+- **⚡ 効率的**: テキスト分割とバッチ処理で大きなファイルにも対応
+- **🦙 Alpaca対応**: 生成されたQ&AペアをAlpaca形式のJSONで出力
+- **🤗 HF統合**: Hugging Face Hubへの直接アップロード機能
+- **📊 データセットカード**: 自動的なREADME.md生成でデータセット情報を整理
+- **🔄 変換機能**: 既存XMLファイルからAlpaca形式への変換コマンド
+
+## 📦 インストール
 
 \```bash
 # 仮想環境の作成（推奨）
@@ -22,9 +45,9 @@ venv\Scripts\activate     # Windows
 pip install -e .
 \```
 
-## 使用方法
+## 🚀 使用方法
 
-### 新しいワークフロー（推奨）
+### 📋 基本的なワークフロー
 
 1. **GAペア定義ファイルの自動生成**
 \```bash
@@ -32,121 +55,284 @@ pip install -e .
 export OPENAI_API_KEY="your-api-key-here"
 
 # 元の文章からGAペア定義を自動生成
-easy-dataset create-ga sample_document.txt --output ga-definitions.md
+uv run easy-dataset create-ga .\example\input\documents\sample_document.txt --output-dir .\example\output\sample_document --num-ga-pairs 10
 \```
 
-2. **（任意）生成されたGA定義のレビュー・編集**
+2. **Q&Aペアの生成**
 \```bash
-# テキストエディタで内容を確認・修正
-notepad ga-definitions.md  # Windows
-# または
-nano ga-definitions.md     # Linux/macOS
+# GAペア定義を使ってQ&Aペアを生成
+uv run easy-dataset generate .\example\input\documents\sample_document.txt --ga-file .\example\output\sample_document\ga\ga_definitions.xml --output-dir .\example\output\sample_document\ --chunk-size 500
 \```
 
-3. **Q&Aペアの生成**
+### 🦙 Alpaca形式とHugging Face連携の使用例
+
+#### Alpaca形式での出力
 \```bash
-# GAペア定義を使ってQ&Aペアを生成
-easy-dataset generate sample_document.txt --ga-file ga-definitions.md --output-dir ./results
+# Q&A生成と同時にAlpaca形式のJSONファイルを出力
+uv run easy-dataset generate .\example\input\documents\sample_document.txt \
+  --ga-file .\example\output\sample_document\ga\ga_definitions.xml \
+  --output-dir .\example\output\sample_document\ \
+  --export-alpaca
 \```
 
-### 従来の方法（手動でGA定義を作成）
+#### Hugging Face Hubへの直接アップロード
+\```bash
+# 環境変数でトークンを設定
+set HUGGINGFACE_TOKEN=hf_your_token_here
+
+# データセット生成とHugging Face Hubアップロードを一度に実行
+uv run easy-dataset generate .\example\input\documents\sample_document.txt \
+  --ga-file .\example\output\sample_document\ga\ga_definitions.xml \
+  --output-dir .\example\output\sample_document\ \
+  --export-alpaca \
+  --upload-hf \
+  --hf-repo-name username/my-qa-dataset
+\```
 
+#### 既存XMLファイルの変換とアップロード
 \```bash
-# 手動で作成したGA定義ファイルを使用
-easy-dataset generate sample_document.txt --ga-file sample_ga_definition.md --output-dir ./results
+# 既存のXMLファイルをAlpaca形式に変換してHugging Face Hubにアップロード
+uv run easy-dataset convert-to-alpaca .\example\output\sample_document\qa \
+  --output-file dataset.json \
+  --upload-hf \
+  --hf-repo-name username/my-qa-dataset \
+  --hf-private
 \```
 
-### コマンドオプション
+### ⚙️ コマンドオプション
 
-#### create-ga コマンド
+#### 🔧 create-ga コマンド
 \```bash
-easy-dataset create-ga [OPTIONS] FILE_PATH
+uv run easy-dataset create-ga [OPTIONS] FILE_PATH
 
 Arguments:
-  FILE_PATH  GAペアの定義を生成するための元のテキストファイル
+  FILE_PATH  GAペアの定義を生成するための元のテキストファイル [required]
 
 Options:
-  -o, --output PATH    生成されたGAペア定義を保存するファイルパス [required]
-  -m, --model TEXT     GAペア定義の生成に使用するLLMモデル [default: gpt-4o]
-  -h, --help           ヘルプを表示
+  -o, --output-dir DIRECTORY  生成されたGAペア定義ファイルを保存するディレクトリ [required]
+  -m, --model TEXT           GAペア定義の生成に使用するLLMモデル名 [default: openrouter/openai/gpt-4o]
+  -g, --num-ga-pairs INTEGER 生成するGAペアの数。指定しない場合はLLMが適切な数を決定します
+  -h, --help                 Show this message and exit
 \```
 
-#### generate コマンド
+#### 🔧 generate コマンド
 \```bash
-easy-dataset generate [OPTIONS] FILE_PATH
+uv run easy-dataset generate [OPTIONS] FILE_PATH
 
 Arguments:
-  FILE_PATH  元のテキストファイルへのパス
+  FILE_PATH  元のテキストファイルへのパス [required]
 
 Options:
-  -g, --ga-file PATH        Genre-Audienceペアを定義したMarkdownファイル [required]
-  -o, --output-dir PATH     XMLファイルの出力ディレクトリ（省略時はコンソール出力）
-  -m, --model TEXT          Q&Aペアの生成に使用するLLMモデル [default: gpt-4o]
-  --chunk-size INTEGER      テキストチャンクの最大サイズ [default: 2000]
-  --chunk-overlap INTEGER   チャンク間のオーバーラップサイズ [default: 200]
-  -h, --help                ヘルプを表示
+  --ga-file PATH           Genre-Audienceペアを定義したXMLファイル [required]
+  -o, --output-dir PATH    XMLファイルの出力ディレクトリ
+  -m, --model TEXT         Q&Aペアの生成に使用するLLMモデル [default: openrouter/openai/gpt-4o]
+  --chunk-size INTEGER     テキストチャンクの最大サイズ [default: 2000]
+  --chunk-overlap INTEGER  チャンク間のオーバーラップサイズ [default: 200]
+  -h, --help               Show this message and exit
 \```
 
-## GA定義ファイルの形式
-
-Genre-Audienceペアをマークダウン形式で定義します：
-
-\```markdown
-# Genre: 学術論文
-学術的で厳密な表現を用い、専門用語を正確に使用し、論理的で客観的な回答を提供します。
+## 📄 GA定義ファイルの形式
 
-# Audience: 大学生
-大学レベルの知識を持つ学習者向けに、基礎概念から応用まで段階的に説明します。
+`create-ga`コマンドで自動生成されるGA定義ファイルはXML形式で保存されます：
 
----
+\```xml
+<?xml version="1.0" encoding="utf-8"?>
+<GADefinitions>
+  <Pair>
+    <Genre>学術論文</Genre>
+    <GenreDescription>学術的で厳密な表現を用い、専門用語を正確に使用し、論理的で客観的な回答を提供します。</GenreDescription>
+    <Audience>コンピュータサイエンス研究者</Audience>
+    <AudienceDescription>コンピュータサイエンス分野の研究者向けに、最新の研究動向や理論的背景を含む専門的な内容を提供します。</AudienceDescription>
+  </Pair>
+  <Pair>
+    <Genre>技術ブログ</Genre>
+    <GenreDescription>実践的で親しみやすい表現を用い、具体例やコード例を交えて説明します。</GenreDescription>
+    <Audience>プログラミング初心者</Audience>
+    <AudienceDescription>プログラミングを学び始めた初心者向けに、基礎的な概念を分かりやすく説明します。</AudienceDescription>
+  </Pair>
+</GADefinitions>
+\```
 
-# Genre: 技術ブログ
-実践的で親しみやすい表現を用い、具体例やコード例を交えて説明します。
+また、各Genre別にマークダウンファイルも生成され、必要に応じて手動で編集できます。
 
-# Audience: エンジニア
-実務経験のある開発者向けに、実装の詳細や最適化のポイントを重視した内容を提供します。
-\```
+## 📁 出力形式
 
-## 出力形式
+### 📄 XML形式（デフォルト）
 
-各GenreごとにXMLファイルが生成されます：
+`generate`コマンドの実行により、各GenreごとにXMLファイルが生成されます：
 
 \```xml
 <?xml version="1.0" ?>
 <QAPairs genre="学術論文">
   <Pair>
-    <Audience>大学生</Audience>
+    <Audience>コンピュータサイエンス研究者</Audience>
     <Question>Pythonの設計哲学における主要な特徴は何ですか？</Question>
     <Answer>Pythonの設計哲学は「読みやすさ」を重視しており、シンプルで理解しやすい構文が特徴です。</Answer>
   </Pair>
 </QAPairs>
 \```
 
-## サポートするLLMモデル
+### 🦙 Alpaca形式（`--export-alpaca`オプション）
+
+`--export-alpaca`オプションを使用すると、機械学習で広く使用されるAlpaca形式のJSONファイルが生成されます：
+
+\```json
+[
+  {
+    "instruction": "Pythonの設計哲学における主要な特徴は何ですか？",
+    "input": "",
+    "output": "Pythonの設計哲学は「読みやすさ」を重視しており、シンプルで理解しやすい構文が特徴です。",
+    "genre": "学術論文",
+    "audience": "コンピュータサイエンス研究者"
+  },
+  {
+    "instruction": "Pythonのインタープリター型言語としての利点は何ですか？",
+    "input": "",
+    "output": "インタープリター型のため、コンパイル不要で即座にコードを実行でき、開発サイクルが高速化されます。",
+    "genre": "技術ブログ",
+    "audience": "プログラミング初心者"
+  }
+]
+\```
+
+### 📊 自動生成されるデータセットカード
+
+Alpaca形式で出力する際、以下の情報を含むREADME.mdが自動生成されます：
+
+- **データセット概要**: エントリ数、形式、言語、ライセンス
+- **ジャンル分布**: 含まれるすべてのジャンルのリスト
+- **対象読者分布**: 含まれるすべての対象読者のリスト
+- **使用方法**: Hugging Face Datasetsでの読み込み例
+- **メタデータ**: Hugging Face Hub用のYAMLフロントマター
+
+### 📁 生成されるファイル構造
+
+\```
+output_directory/
+├── ga/
+│   ├── ga_definitions.xml          # メインのGA定義ファイル
+│   ├── ga_definitions_学術論文.md   # Genre別マークダウンファイル
+│   ├── ga_definitions_技術ブログ.md
+│   └── ...
+├── qa/
+│   ├── 学術論文.xml                # Genre別Q&AファイルXML形式）
+│   ├── 技術ブログ.xml
+│   └── ...
+├── logs/
+│   └── raw.md                      # LLMの生レスポンス
+├── dataset_alpaca.json             # 🦙 Alpaca形式のデータセット（--export-alpacaオプション使用時）
+└── README.md                       # 📊 データセットカード（--export-alpacaオプション使用時）
+\```
+
+## 🤖 サポートするLLMモデル
 
-### OpenAI（直接）
+### 🔑 OpenAI（直接）
 \```bash
 export OPENAI_API_KEY="sk-..."
 easy-dataset generate document.txt -g ga.md -m gpt-4o
 \```
 
-### OpenRouter経由
+### 🌐 OpenRouter経由
 \```bash
 export OPENROUTER_API_KEY="sk-or-v1-..."
 easy-dataset generate document.txt -g ga.md -m gpt-4o  # 自動でopenai/gpt-4oに変換
 easy-dataset generate document.txt -g ga.md -m claude-3-sonnet  # 自動でanthropic/claude-3-sonnetに変換
 \```
 
-### その他のプロバイダー
-- Anthropic: `claude-3-opus`, `claude-3-sonnet`, `claude-3-haiku`
-- Ollama: `ollama/llama3`, `ollama/mistral`
-- その他litellmがサポートするすべてのモデル
+## 🤗 Hugging Face Hub統合
+
+### 🔑 環境変数の設定
+
+\```bash
+# Windows (cmd)
+set HUGGINGFACE_TOKEN=hf_your_token_here
+
+# Windows (PowerShell)
+$env:HUGGINGFACE_TOKEN="hf_your_token_here"
+
+# Linux/macOS
+export HUGGINGFACE_TOKEN="hf_your_token_here"
+\```
+
+### 📤 データセットのアップロード
+
+\```bash
+# 生成と同時にHugging Face Hubにアップロード
+uv run easy-dataset generate document.txt \
+  --ga-file ga.xml \
+  --export-alpaca \
+  --upload-hf \
+  --hf-repo-name username/my-dataset
+
+# 既存XMLファイルを変換してアップロード
+uv run easy-dataset convert-to-alpaca ./qa_directory \
+  --upload-hf \
+  --hf-repo-name username/my-dataset \
+  --hf-private  # プライベートリポジトリとして作成
+\```
+
+### 📥 アップロード後の使用方法
+
+\```python
+from datasets import load_dataset
+
+# Hugging Face Hubからデータセットを読み込み
+dataset = load_dataset("username/my-dataset")
+
+# データセットの内容を確認
+print(dataset['train'][0])
+# {
+#   'instruction': 'Pythonの設計哲学における主要な特徴は何ですか？',
+#   'input': '',
+#   'output': 'Pythonの設計哲学は「読みやすさ」を重視しており...',
+#   'genre': '学術論文',
+#   'audience': 'コンピュータサイエンス研究者'
+# }
+
+# ファインチューニング用のデータ準備
+def format_instruction(example):
+    return f"### 指示:\n{example['instruction']}\n\n### 回答:\n{example['output']}"
+
+formatted_dataset = dataset.map(lambda x: {"text": format_instruction(x)})
+\```
+
+### 📊 自動生成されるデータセットカードの例
+
+アップロード時に自動生成されるREADME.mdには以下の情報が含まれます：
+
+\```yaml
+---
+license: mit
+task_categories:
+- question-answering
+- text-generation
+language:
+- ja
+tags:
+- alpaca
+- qa
+- japanese
+size_categories:
+- n<1K  # データ量に応じて自動設定
+---
+\```
+
+- **データセット概要**: エントリ数、形式、言語、ライセンス
+- **ジャンル・対象読者分布**: 含まれるすべてのカテゴリ
+- **使用方法**: Hugging Face Datasetsでの読み込み例
+- **生成ツール情報**: easy-dataset-cliへのリンク
+
+## 📜 ライセンス
+
+MIT License
+
+## 🔗 参考情報
+
+本プロジェクトは以下のOSSと論文を参考に開発されています：
 
-### 推奨モデル
-- **高品質**: `gpt-4o`, `claude-3-opus`
-- **バランス**: `gpt-4`, `claude-3-sonnet`
-- **高速**: `gpt-3.5-turbo`, `claude-3-haiku`
+### 📦 参考OSS
+- **[Easy Dataset](https://github.com/ConardLi/easy-dataset)**
 
-## ライセンス
+### 📄 参考論文
+- **[Dataset Generation for Instruction Tuning](https://arxiv.org/html/2507.04009v1)**
 
-MIT License
\ No newline at end of file
diff --git a/easy_dataset_cli/alpaca_converter.py b/easy_dataset_cli/alpaca_converter.py
new file mode 100644
index 0000000..0a148ea
--- /dev/null
+++ b/easy_dataset_cli/alpaca_converter.py
@@ -0,0 +1,238 @@
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
+    commit_message: str = "Upload alpaca dataset",
+    readme_file: Optional[Path] = None
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
+    try:
+        # HfApiインスタンスを作成
+        api = HfApi(token=hf_token)
+        
+        # リポジトリを作成（既に存在する場合はスキップ）
+        try:
+            create_repo(
+                repo_id=repo_name,
+                token=hf_token,
+                repo_type="dataset",
+                private=private,
+                exist_ok=True
+            )
+            console.print(f"[green]✓[/green] リポジトリを作成/確認しました: [cyan]{repo_name}[/cyan]")
+        except Exception as e:
+            console.print(f"[yellow]リポジトリ作成時の警告: {e}[/yellow]")
+        
+        # データセットを作成
+        dataset = Dataset.from_list(dataset_data)
+        
+        # Hugging Face Hubにプッシュ
+        dataset.push_to_hub(
+            repo_id=repo_name,
+            token=hf_token,
+            commit_message=commit_message,
+            private=private
+        )
+        
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
+        console.print(f"[bold green]✓[/bold green] データセットをアップロードしました!")
+        console.print(f"[cyan]https://huggingface.co/datasets/{repo_name}[/cyan]")
+        
+        return True
+        
+    except Exception as e:
+        console.print(f"[bold red]Hugging Faceアップロードエラー:[/bold red] {e}")
+        return False
+
+def create_dataset_card(
+    dataset_data: List[Dict[str, str]], 
+    output_file: Path,
+    dataset_name: str = "Generated QA Dataset"
+) -> None:
+    """データセットカード（README.md）を生成"""
+    
+    # 統計情報を計算
+    total_entries = len(dataset_data)
+    genres = set(entry.get('genre', 'Unknown') for entry in dataset_data)
+    audiences = set(entry.get('audience', 'Unknown') for entry in dataset_data)
+    
+    # データセットカードの内容
+    card_content = f"""---
+license: mit
+task_categories:
+- question-answering
+- text-generation
+language:
+- ja
+tags:
+- alpaca
+- qa
+- japanese
+size_categories:
+- {get_size_category(total_entries)}
+---
+
+# {dataset_name}
+
+このデータセットは、easy-dataset-cliを使用して生成されたアルパカ形式の日本語Q&Aデータセットです。
+
+## データセット概要
+
+- **総エントリ数**: {total_entries:,}
+- **形式**: Alpaca形式
+- **言語**: 日本語
+- **ライセンス**: MIT
+
+## データ構造
+
+各エントリは以下の形式です：
+
+\```json
+{{
+  "instruction": "質問文",
+  "input": "",
+  "output": "回答文",
+  "genre": "ジャンル",
+  "audience": "対象読者"
+}}
+\```
+
+## ジャンル分布
+
+含まれるジャンル:
+{chr(10).join(f"- {genre}" for genre in sorted(genres))}
+
+## 対象読者分布
+
+含まれる対象読者:
+{chr(10).join(f"- {audience}" for audience in sorted(audiences))}
+
+## 使用方法
+
+\```python
+from datasets import load_dataset
+
+dataset = load_dataset("{dataset_name}")
+\```
+
+## 生成ツール
+
+このデータセットは[easy-dataset-cli](https://github.com/Sunwood-ai-labsII/easy-dataset-cli)を使用して生成されました。
+"""
+    
+    output_file.write_text(card_content, encoding='utf-8')
+    console.print(f"[green]✓[/green] データセットカードを生成しました: [cyan]{output_file}[/cyan]")
+
+def get_size_category(count: int) -> str:
+    """エントリ数に基づいてサイズカテゴリを返す"""
+    if count < 1000:
+        return "n<1K"
+    elif count < 10000:
+        return "1K<n<10K"
+    elif count < 100000:
+        return "10K<n<100K"
+    elif count < 1000000:
+        return "100K<n<1M"
+    else:
+        return "n>1M"
diff --git a/easy_dataset_cli/core.py b/easy_dataset_cli/core.py
index c9db332..056452b 100644
--- a/easy_dataset_cli/core.py
+++ b/easy_dataset_cli/core.py
@@ -1,519 +1,53 @@
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
-        if not section.strip():
-            continue
-
-        ast = mistune.create_markdown(renderer=None)(section)
-        genre = {"title": "", "description": ""}
-        audience = {"title": "", "description": ""}
-        current_type = None
-
-        for node in ast:
-            if node['type'] == 'heading':
-                header_text = "".join(child['text'] for child in node['children'])
-                if 'genre' in header_text.lower():
-                    current_type = 'genre'
-                    genre['title'] = header_text.replace('Genre:', '').strip()
-                elif 'audience' in header_text.lower():
-                    current_type = 'audience'
-                    audience['title'] = header_text.replace('Audience:', '').strip()
-            elif node['type'] == 'paragraph':
-                description = "".join(child['text'] for child in node['children'])
-                if current_type == 'genre':
-                    genre['description'] = description
-                elif current_type == 'audience':
-                    audience['description'] = description
-
-        if genre['title'] and audience['title']:
-            pairs.append({"genre": genre, "audience": audience})
-    
-    return pairs
-
-
-def split_text(text: str, chunk_size: int, chunk_overlap: int) -> List[str]:
-    """LangChainのTextSplitterを使ってテキストをチャンクに分割する"""
-    text_splitter = RecursiveCharacterTextSplitter(
-        chunk_size=chunk_size,
-        chunk_overlap=chunk_overlap,
-        length_function=len,
-        is_separator_regex=False,
-    )
-    docs = text_splitter.create_documents([text])
-    return [doc.page_content for doc in docs]
-
-
-def generate_qa_for_chunk_with_ga(
-    chunk: str, model: str, ga_pair: Dict[str, Dict[str, str]], logs_dir: Path = None, num_qa_pairs: int = None
-) -> List[Dict[str, str]]:
-    """litellmを使い、1つのチャンクと1つのGAペアからQ&Aペアのリストを生成する"""
-    prompt_template = get_qa_generation_prompt()
-    prompt = prompt_template.format(
-        context=chunk,
-        genre_title=ga_pair['genre']['title'],
-        genre_description=ga_pair['genre']['description'],
-        audience_title=ga_pair['audience']['title'],
-        audience_description=ga_pair['audience']['description'],
-        num_qa_pairs=num_qa_pairs if num_qa_pairs is not None else "複数の"
-    )
-
-    messages = [
-        {"role": "system", "content": "あなたは、XML形式で厳密に出力する優秀なアシスタントです。XMLの特殊文字（&, <, >, \", '）は適切にエスケープし、改行は含めずに出力してください。"},
-        {"role": "user", "content": prompt}
-    ]
-
-    # OpenRouter用の環境変数設定
-    os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY", "")
-    
-    try:
-        response = completion(model=model, messages=messages)
-        xml_content = response.choices[0].message.content
-        
-        # rawレスポンスを保存（オプション）
-        if logs_dir:
-            genre_safe = "".join(c for c in ga_pair['genre']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
-            audience_safe = "".join(c for c in ga_pair['audience']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
-            raw_filename = f"qa_raw_{genre_safe}_{audience_safe}.md"
-            raw_file_path = logs_dir / raw_filename
-            raw_file_path.write_text(xml_content, encoding="utf-8")
-        
-        qa_pairs = []
-
-        # LLMからの出力には余分なテキストが含まれることがあるため、XML部分のみを抽出
-        xml_start = xml_content.find("<QAPairs>")
-        xml_end = xml_content.rfind("</QAPairs>")
-
-        if xml_start != -1 and xml_end != -1:
-            clean_xml = xml_content[xml_start: xml_end + len("</QAPairs>")]
-            
-            try:
-                root = ET.fromstring(clean_xml)
-
-                for pair_node in root.findall('Pair'):
-                    question_node = pair_node.find('Question')
-                    answer_node = pair_node.find('Answer')
-
-                    if question_node is not None and answer_node is not None:
-                        qa_pairs.append({
-                            "question": question_node.text or "",
-                            "answer": answer_node.text or ""
-                        })
-            
-            except ET.ParseError:
-                # XMLパースに失敗した場合、手動でテキスト解析
-                console.print(f"[yellow]XMLパースエラー、手動解析を試行中...[/yellow]")
-                qa_pairs = parse_qa_from_text_fallback(clean_xml)
-
-        return qa_pairs
-
-    except ET.ParseError as parse_error:
-        console.print(
-            f"[bold red]LLMが生成したXMLの解析に失敗しました:[/bold red] {parse_error}"
-        )
-        console.print(f"[dim]受信したテキスト: {xml_content[:200]}...[/dim]")
-        return []
-    except Exception as general_error:
-        console.print(
-            f"[bold red]チャンクとGAペアからのQ&A生成中にエラーが発生しました:[/bold red] "
-            f"{general_error}"
-        )
-        console.print(
-            f"[dim]Genre: {ga_pair['genre']['title']}, "
-            f"Audience: {ga_pair['audience']['title']}[/dim]"
-        )
-        return []
-
-
-def generate_ga_definitions(text_content: str, model: str, num_ga_pairs: int = None) -> str:
-    """litellmを使い、元の文章からGAペア定義のXMLを生成する"""
-    # LLMに渡すテキストは長すぎるとコストや性能に影響するため、先頭部分に限定する
-    context = text_content[:8000]
-    console.print(f"[dim]コンテキスト長: {len(context)} 文字[/dim]")
-
-    prompt_template = get_ga_definition_generation_prompt()
-    prompt = prompt_template.format(
-        context=context,
-        num_ga_pairs=num_ga_pairs if num_ga_pairs is not None else "3-5個の"
-    )
-
-    messages = [
-        {"role": "system", "content": "あなたは、XML形式で厳密に出力する優秀なアシスタントです。"},
-        {"role": "user", "content": prompt}
-    ]
-
-    # OpenRouter用の環境変数設定
-    api_key = os.getenv("OPENROUTER_API_KEY", "")
-    if not api_key:
-        console.print("[bold red]OPENROUTER_API_KEYが設定されていません！[/bold red]")
-        raise ValueError("OPENROUTER_API_KEYが必要です")
-    
-    os.environ["OPENROUTER_API_KEY"] = api_key
-    
-    # OpenRouterのモデル名に変換（必要に応じて）
-    if "openrouter" not in model and not model.startswith("openrouter/"):
-        if model.startswith("gpt-"):
-            model = f"openrouter/openai/{model}"
-        elif model.startswith("claude-"):
-            model = f"openrouter/anthropic/{model}"
-        else:
-            # デフォルトでopenrouterプレフィックスを追加
-            model = f"openrouter/{model}"
-
-    try:
-        response = completion(model=model, messages=messages)
-        xml_content = response.choices[0].message.content
-        console.print(f"[dim]LLMレスポンス長: {len(xml_content)} 文字[/dim]")
-        return xml_content
-    except Exception as error:
-        console.print(f"[bold red]GA定義の生成中にエラーが発生しました:[/bold red] {error}")
-        raise
-
-
-def parse_ga_definitions_from_xml(xml_content: str) -> List[Dict[str, Dict[str, str]]]:
-    """XML形式のGA定義からGAペアのリストを解析する"""
-    pairs = []
-    
-    try:
-        # XMLタグから<GADefinitions>部分を抽出（マークダウンコードブロックを無視）
-        xml_start = xml_content.find("<GADefinitions>")
-        xml_end = xml_content.rfind("</GADefinitions>")
-        
-        if xml_start != -1 and xml_end != -1:
-            clean_xml = xml_content[xml_start: xml_end + len("</GADefinitions>")]
-            
-            # XMLの特殊文字をエスケープ
-            import html
-            clean_xml = html.unescape(clean_xml)
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
-                    # より詳細なチェック
-                    has_genre_title = genre_title_node is not None and genre_title_node.text and genre_title_node.text.strip()
-                    has_genre_desc = genre_desc_node is not None and genre_desc_node.text and genre_desc_node.text.strip()
-                    has_audience_title = audience_title_node is not None and audience_title_node.text and audience_title_node.text.strip()
-                    has_audience_desc = audience_desc_node is not None and audience_desc_node.text and audience_desc_node.text.strip()
-                    
-                    if all([has_genre_title, has_genre_desc, has_audience_title, has_audience_desc]):
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
-                        console.print(f"[green]✓[/green] {genre_title_node.text.strip()} x {audience_title_node.text.strip()}")
-                    else:
-                        console.print(f"[yellow]⚠[/yellow] Pair {i+1}: 必要な要素が不足")
-                else:
-                    console.print(f"[yellow]⚠[/yellow] Pair {i+1}: GenreまたはAudienceノードが見つからない")
-        else:
-            console.print("[yellow]GADefinitionsタグが見つかりませんでした[/yellow]")
-                        
-    except ET.ParseError as parse_error:
-        console.print(f"[bold red]GA定義XMLの解析に失敗しました:[/bold red] {parse_error}")
-        console.print(f"[dim]問題のあるXML: {xml_content[xml_start:xml_start+200] if xml_start != -1 else xml_content[:200]}...[/dim]")
-        
-        # XMLエラーの場合、手動でテキスト解析を試行
-        console.print("[yellow]手動解析を試行中...[/yellow]")
-        pairs = parse_ga_from_text_fallback(xml_content)
-        
-    except Exception as e:
-        console.print(f"[bold red]予期しないエラー:[/bold red] {e}")
-    
-    return pairs
-
-
-def parse_ga_from_text_fallback(content: str) -> List[Dict[str, Dict[str, str]]]:
-    """XMLパースに失敗した場合のフォールバック：テキストから直接解析"""
-    pairs = []
-    
-    try:
-        # <Pair>タグで分割
-        pair_sections = content.split('<Pair>')
-        
-        for section in pair_sections[1:]:  # 最初の要素は空なのでスキップ
-            if '</Pair>' not in section:
-                continue
-                
-            pair_content = section.split('</Pair>')[0]
-            
-            # Title要素を抽出
-            genre_title = extract_text_between_tags(pair_content, 'Genre', 'Title')
-            genre_desc = extract_text_between_tags(pair_content, 'Genre', 'Description')
-            audience_title = extract_text_between_tags(pair_content, 'Audience', 'Title')
-            audience_desc = extract_text_between_tags(pair_content, 'Audience', 'Description')
-            
-            if all([genre_title, genre_desc, audience_title, audience_desc]):
-                pairs.append({
-                    "genre": {
-                        "title": genre_title.strip(),
-                        "description": genre_desc.strip()
-                    },
-                    "audience": {
-                        "title": audience_title.strip(),
-                        "description": audience_desc.strip()
-                    }
-                })
-                console.print(f"[green]✓[/green] (手動解析) {genre_title} x {audience_title}")
-    
-    except Exception as e:
-        console.print(f"[red]手動解析も失敗:[/red] {e}")
-    
-    return pairs
-
-
-def extract_text_between_tags(content: str, parent_tag: str, child_tag: str) -> str:
-    """指定されたタグ間のテキストを抽出"""
-    try:
-        # 親タグ内を探す
-        parent_start = content.find(f'<{parent_tag}>')
-        parent_end = content.find(f'</{parent_tag}>')
-        
-        if parent_start == -1 or parent_end == -1:
-            return ""
-            
-        parent_content = content[parent_start:parent_end]
-        
-        # 子タグ内のテキストを抽出
-        child_start = parent_content.find(f'<{child_tag}>')
-        child_end = parent_content.find(f'</{child_tag}>')
-        
-        if child_start == -1 or child_end == -1:
-            return ""
-            
-        return parent_content[child_start + len(f'<{child_tag}>'):child_end]
-    
-    except Exception:
-        return ""
-
-
-def parse_qa_from_text_fallback(content: str) -> List[Dict[str, str]]:
-    """Q&A XMLパースに失敗した場合のフォールバック：テキストから直接解析"""
-    qa_pairs = []
-    
-    try:
-        # <Pair>タグで分割
-        pair_sections = content.split('<Pair>')
-        
-        for section in pair_sections[1:]:  # 最初の要素は空なのでスキップ
-            if '</Pair>' not in section:
-                continue
-                
-            pair_content = section.split('</Pair>')[0]
-            
-            # Question と Answer を抽出
-            question = extract_simple_tag_content(pair_content, 'Question')
-            answer = extract_simple_tag_content(pair_content, 'Answer')
-            
-            if question and answer:
-                qa_pairs.append({
-                    "question": question.strip(),
-                    "answer": answer.strip()
-                })
-                console.print(f"[green]✓[/green] (手動解析) Q&A追加")
-    
-    except Exception as e:
-        console.print(f"[red]Q&A手動解析も失敗:[/red] {e}")
-    
-    return qa_pairs
-
-
-def extract_simple_tag_content(content: str, tag: str) -> str:
-    """シンプルなタグ内のテキストを抽出"""
-    try:
-        start_tag = f'<{tag}>'
-        end_tag = f'</{tag}>'
-        
-        start_pos = content.find(start_tag)
-        end_pos = content.find(end_tag)
-        
-        if start_pos == -1 or end_pos == -1:
-            return ""
-            
-        return content[start_pos + len(start_tag):end_pos]
-    
-    except Exception:
-        return ""
-
-
-def create_output_directories(base_dir: Path) -> Dict[str, Path]:
-    """出力用のディレクトリ構造を作成する"""
-    directories = {
-        "base": base_dir,
-        "ga": base_dir / "ga",
-        "logs": base_dir / "logs", 
-        "qa": base_dir / "qa"
-    }
-    
-    for dir_path in directories.values():
-        dir_path.mkdir(parents=True, exist_ok=True)
-    
-    return directories
-
-
-def save_ga_definitions_by_genre(ga_pairs: List[Dict[str, Dict[str, str]]], ga_dir: Path) -> None:
-    """GAペアをGenreごとにマークダウンファイルに保存する"""
-    genre_groups = defaultdict(list)
-    
-    # Genreごとにグループ化
-    for pair in ga_pairs:
-        genre_title = pair['genre']['title']
-        genre_groups[genre_title].append(pair)
-    
-    # 各Genreごとにファイルを作成
-    for genre_title, pairs in genre_groups.items():
-        # ファイル名に使用できない文字を置換
-        safe_filename = "".join(c for c in genre_title if c.isalnum() or c in (' ', '-', '_')).rstrip()
-        safe_filename = safe_filename.replace(' ', '_').lower()
-        
-        file_path = ga_dir / f"ga_definitions_{safe_filename}.md"
-        
-        content = f"# {genre_title}\n\n"
-        
-        for pair in pairs:
-            content += f"## Genre: {pair['genre']['title']}\n"
-            content += f"{pair['genre']['description']}\n\n"
-            content += f"## Audience: {pair['audience']['title']}\n"
-            content += f"{pair['audience']['description']}\n\n"
-            content += "---\n\n"
-        
-        file_path.write_text(content, encoding="utf-8")
-        console.print(f"[green]GA定義を保存しました:[/green] {file_path}")
-
-
-def convert_to_xml_by_genre(all_qa_pairs: List[Dict[str, str]]) -> Dict[str, str]:
-    """Q&AペアのリストをGenreごとにグループ化し、整形されたXML文字列の辞書に変換する"""
-    grouped_by_genre = defaultdict(list)
-
-    for item in all_qa_pairs:
-        grouped_by_genre[item["genre"]].append(item)
-
-    xml_outputs = {}
-    for genre, pairs in grouped_by_genre.items():
-        root = ET.Element("QAPairs")
-        root.set("genre", genre)
-
-        for item in pairs:
-            pair_elem = ET.SubElement(root, "Pair")
-
-            audience_elem = ET.SubElement(pair_elem, "Audience")
-            audience_elem.text = item["audience"]
-
-            question_elem = ET.SubElement(pair_elem, "Question")
-            question_elem.text = item["question"]
-
-            answer_elem = ET.SubElement(pair_elem, "Answer")
-            answer_elem.text = item["answer"]
-
-        rough_string = ET.tostring(root, 'utf-8')
-        reparsed = minidom.parseString(rough_string)
-        xml_outputs[genre] = reparsed.toprettyxml(indent="  ")
-
-    return xml_outputs
+"""統合インターフェース - 各モジュールの機能を統合"""
+
+# 各モジュールから必要な関数をインポート
+from .ga_parser import (
+    parse_ga_file,
+    parse_ga_definitions_from_xml
+)
+from .qa_generator import (
+    generate_qa_for_chunk_with_ga,
+    generate_qa_for_chunk_with_ga_and_fulltext,
+    generate_ga_definitions
+)
+from .text_splitter import split_text
+from .xml_utils import convert_to_xml_by_genre
+from .file_utils import (
+    create_output_directories,
+    save_ga_definitions_by_genre,
+    sanitize_filename
+)
+from .alpaca_converter import (
+    convert_all_xml_to_alpaca,
+    upload_to_huggingface,
+    create_dataset_card
+)
+
+# 後方互換性のため、すべての関数を再エクスポート
+__all__ = [
+    # GA解析関連
+    'parse_ga_file',
+    'parse_ga_definitions_from_xml',
+    
+    # Q&A生成関連
+    'generate_qa_for_chunk_with_ga',
+    'generate_qa_for_chunk_with_ga_and_fulltext',
+    'generate_ga_definitions',
+    
+    # テキスト分割
+    'split_text',
+    
+    # XML処理
+    'convert_to_xml_by_genre',
+    
+    # ファイル操作
+    'create_output_directories',
+    'save_ga_definitions_by_genre',
+    'sanitize_filename',
+    
+    # アルパカ変換・アップロード
+    'convert_all_xml_to_alpaca',
+    'upload_to_huggingface',
+    'create_dataset_card'
+]
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
+        from .xml_utils import parse_ga_from_text_fallback
+        pairs = parse_ga_from_text_fallback(xml_content)
+
+    except Exception as e:
+        console.print(f"[bold red]予期しないエラー:[/bold red] {e}")
+
+    return pairs
diff --git a/easy_dataset_cli/main.py b/easy_dataset_cli/main.py
index 28adbaf..6f62532 100644
--- a/easy_dataset_cli/main.py
+++ b/easy_dataset_cli/main.py
@@ -12,11 +12,16 @@ from .core import (
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
+    sanitize_filename,
+    convert_all_xml_to_alpaca,
+    upload_to_huggingface,
+    create_dataset_card
 )
 
 # .envファイルを読み込む
@@ -29,11 +34,6 @@ app = typer.Typer(
 console = Console()
 
 
-def sanitize_filename(name: str) -> str:
-    """ファイル名として安全な文字列に変換する"""
-    return "".join(c for c in name if c.isalnum() or c in (' ', '_', '-')).rstrip()
-
-
 @app.command()
 def create_ga(
     file_path: Annotated[Path, typer.Argument(
@@ -47,11 +47,11 @@ def create_ga(
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
@@ -138,9 +138,37 @@ def generate(
     num_qa_pairs: Annotated[int, typer.Option(
         "--num-qa-pairs", "-q",
         help="各チャンク・GAペアの組み合わせで生成するQ&Aペアの数。指定しない場合はLLMが適切な数を決定します。"
-    )] = None,
+    )] = 10,
+    use_fulltext: Annotated[bool, typer.Option(
+        "--use-fulltext", "-f",
+        help="全文をコンテキストとして含めてQA生成を行います。より文脈を理解したQAが生成されますが、処理時間とコストが増加します。"
+    )] = False,
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
-    """テキストファイルとGA定義からQ&Aペアを生成し、Genre別のXMLファイルとして出力します。"""
+    """テキストファイルとGA定義からQ&Aペアを生成し、Genre別のXMLファイルとして出力します。
+    
+    --use-fulltextオプションを使用すると、各チャンクの処理時に全文をコンテキストとして含めることで、
+    より文脈を理解した高品質なQ&Aペアを生成できます。ただし、処理時間とAPIコストが増加します。
+    """
     try:
         console.print(f"ファイルを読み込んでいます: [cyan]{file_path}[/cyan]")
         text = file_path.read_text(encoding="utf-8")
@@ -167,16 +195,31 @@ def generate(
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
 
                     for pair in qa_pairs:
                         all_qa_pairs_with_ga.append({
@@ -208,6 +251,34 @@ def generate(
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
+                            commit_message=f"Upload QA dataset with {len(alpaca_data)} entries",
+                            readme_file=readme_file
+                        )
+                        if not success:
+                            console.print("[bold red]Hugging Faceアップロードに失敗しました[/bold red]")
         else:
             console.print("\n--- 生成されたQ&Aペア (Genre別XML) ---")
             for genre, xml_content in xml_outputs_by_genre.items():
@@ -219,5 +290,80 @@ def generate(
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
+        "--hf-token", "-t",
+        help="Hugging Face APIトークン（環境変数HUGGINGFACE_TOKENからも取得可能）"
+    )] = "",
+    hf_private: Annotated[bool, typer.Option(
+        "--hf-private",
+        help="Hugging Faceリポジトリをプライベートにします。"
+    )] = False,
+):
+    """既存のXMLファイルをAlpaca形式のJSONに変換し、オプションでHugging Face Hubにアップロードします。"""
+    
+    try:
+        # デフォルトの出力ファイル名を設定
+        if output_file is None:
+            output_file = qa_dir.parent / "dataset_alpaca.json"
+        
+        console.print(f"XMLファイルを変換中: [cyan]{qa_dir}[/cyan]")
+        
+        # アルパカ形式に変換
+        alpaca_data = convert_all_xml_to_alpaca(qa_dir, output_file)
+        
+        if not alpaca_data:
+            console.print("[bold red]変換できるデータが見つかりませんでした。[/bold red]")
+            raise typer.Exit(code=1)
+        
+        # データセットカードを生成
+        readme_file = output_file.parent / "README.md"
+        create_dataset_card(alpaca_data, readme_file, "Converted QA Dataset")
+        
+        # Hugging Face Hubにアップロード
+        if upload_hf:
+            if not hf_repo_name:
+                console.print("[bold red]--hf-repo-nameが指定されていません！[/bold red]")
+                console.print("[yellow]例: --hf-repo-name username/my-qa-dataset[/yellow]")
+                raise typer.Exit(code=1)
+            
+            console.print(f"\n[bold blue]Hugging Face Hubにアップロード中...[/bold blue]")
+            success = upload_to_huggingface(
+                dataset_data=alpaca_data,
+                repo_name=hf_repo_name,
+                hf_token=hf_token if hf_token else None,
+                private=hf_private,
+                commit_message=f"Upload converted QA dataset with {len(alpaca_data)} entries",
+                readme_file=readme_file
+            )
+            
+            if not success:
+                console.print("[bold red]Hugging Faceアップロードに失敗しました[/bold red]")
+                raise typer.Exit(code=1)
+        
+        console.print(f"\n[bold green]✓[/bold green] 変換が完了しました！")
+        
+    except Exception as e:
+        console.print(f"[bold red]変換中にエラーが発生しました:[/bold red] {e}")
+        raise typer.Exit(code=1)
+
+
 if __name__ == "__main__":
     app()
diff --git a/easy_dataset_cli/prompts.py b/easy_dataset_cli/prompts.py
index 5b2c825..24ba9f9 100644
--- a/easy_dataset_cli/prompts.py
+++ b/easy_dataset_cli/prompts.py
@@ -20,6 +20,11 @@ def get_qa_generation_prompt() -> str:
     return load_prompt_template("qa_generation")
 
 
+def get_qa_generation_with_fulltext_prompt() -> str:
+    """全文+チャンク対応Q&A生成プロンプトを取得"""
+    return load_prompt_template("qa_generation_with_fulltext")
+
+
 def get_ga_definition_generation_prompt() -> str:
     """GA定義生成プロンプトを取得"""
     return load_prompt_template("ga_definition_generation")
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
diff --git a/easy_dataset_cli/qa_generator.py b/easy_dataset_cli/qa_generator.py
new file mode 100644
index 0000000..0817065
--- /dev/null
+++ b/easy_dataset_cli/qa_generator.py
@@ -0,0 +1,209 @@
+# easy_dataset_cli/qa_generator.py
+"""Q&A生成関連機能"""
+
+import os
+import xml.etree.ElementTree as ET
+from pathlib import Path
+from typing import List, Dict
+from litellm import completion
+from rich.console import Console
+from dotenv import load_dotenv
+
+from .prompts import (
+    get_qa_generation_prompt,
+    get_qa_generation_with_fulltext_prompt,
+    get_ga_definition_generation_prompt
+)
+from .xml_utils import parse_qa_from_text_fallback
+
+# .envファイルを読み込む
+load_dotenv()
+
+console = Console()
+
+
+def generate_qa_for_chunk_with_ga_and_fulltext(
+    chunk: str,
+    full_text: str,
+    model: str,
+    ga_pair: Dict[str, Dict[str, str]],
+    logs_dir: Path = None,
+    num_qa_pairs: int = None
+) -> List[Dict[str, str]]:
+    """litellmを使い、1つのチャンクと全文、1つのGAペアからQ&Aペアのリストを生成する"""
+    prompt_template = get_qa_generation_with_fulltext_prompt()
+    prompt = prompt_template.format(
+        chunk=chunk,
+        full_text=full_text,
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
+            raw_filename = f"qa_fulltext_raw_{genre_safe}_{audience_safe}.md"
+            raw_file_path = logs_dir / raw_filename
+            raw_file_path.write_text(xml_content, encoding="utf-8")
+
+        return _parse_qa_response(xml_content)
+
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
+def generate_qa_for_chunk_with_ga(
+    chunk: str,
+    model: str,
+    ga_pair: Dict[str, Dict[str, str]],
+    logs_dir: Path = None,
+    num_qa_pairs: int = None
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
+        return _parse_qa_response(xml_content)
+
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
+def _parse_qa_response(xml_content: str) -> List[Dict[str, str]]:
+    """Q&A生成レスポンスのXMLを解析する（共通処理）"""
+    qa_pairs = []
+
+    # LLMからの出力には余分なテキストが含まれることがあるため、XML部分のみを抽出
+    xml_start = xml_content.find("<QAPairs>")
+    xml_end = xml_content.rfind("</QAPairs>")
+
+    if xml_start != -1 and xml_end != -1:
+        clean_xml = xml_content[xml_start: xml_end + len("</QAPairs>")]
+
+        try:
+            root = ET.fromstring(clean_xml)
+
+            for pair_node in root.findall('Pair'):
+                question_node = pair_node.find('Question')
+                answer_node = pair_node.find('Answer')
+
+                if question_node is not None and answer_node is not None:
+                    qa_pairs.append({
+                        "question": question_node.text or "",
+                        "answer": answer_node.text or ""
+                    })
+
+        except ET.ParseError:
+            # XMLパースに失敗した場合、手動でテキスト解析
+            console.print("[yellow]XMLパースエラー、手動解析を試行中...[/yellow]")
+            qa_pairs = parse_qa_from_text_fallback(clean_xml)
+
+    if not qa_pairs:
+        console.print(f"[bold red]LLMが生成したXMLの解析に失敗しました[/bold red]")
+        console.print(f"[dim]受信したテキスト: {xml_content[:200]}...[/dim]")
+
+    return qa_pairs
diff --git a/easy_dataset_cli/text_splitter.py b/easy_dataset_cli/text_splitter.py
new file mode 100644
index 0000000..2f72b69
--- /dev/null
+++ b/easy_dataset_cli/text_splitter.py
@@ -0,0 +1,17 @@
+# easy_dataset_cli/text_splitter.py
+"""テキスト分割関連機能"""
+
+from typing import List
+from langchain_text_splitters import RecursiveCharacterTextSplitter
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
diff --git a/easy_dataset_cli/xml_utils.py b/easy_dataset_cli/xml_utils.py
new file mode 100644
index 0000000..ec5a370
--- /dev/null
+++ b/easy_dataset_cli/xml_utils.py
@@ -0,0 +1,154 @@
+# easy_dataset_cli/xml_utils.py
+"""XML処理関連のユーティリティ"""
+
+import xml.etree.ElementTree as ET
+from xml.dom import minidom
+from collections import defaultdict
+from typing import List, Dict
+from rich.console import Console
+
+console = Console()
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
+                console.print("[green]✓[/green] (手動解析) Q&A追加")
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
