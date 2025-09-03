# 🔄 Latest Code Changes

```diff
diff --git a/.SourceSageignore b/.SourceSageignore
index ac8bce0..14d812a 100644
--- a/.SourceSageignore
+++ b/.SourceSageignore
@@ -53,3 +53,7 @@ venv
 .venv
 
 uv.lock
+tests/
+.github
+
+test_output/
diff --git a/.env.example b/.env.example
index 72d7c7d..07b7bba 100644
--- a/.env.example
+++ b/.env.example
@@ -1,2 +1,28 @@
-OPENROUTER_API_KEY=sk-or-xxxx
-HUGGINGFACE_TOKEN=hf_xxxx
+# ---------------------------------------------------------------------
+# easy-dataset-cli 環境変数設定
+#
+# このファイルは .env のテンプレートです。
+# 使用したい内容をコピーして .env ファイルを作成してください。
+# ---------------------------------------------------------------------
+
+# ===== OpenAI 互換API設定 =====
+# OpenAI 互換APIのAPIキー
+# (必須)
+OPENAI_API_KEY=sk-or-xxxxxxxxxxxxx
+
+# ===== API エンドポイント設定 =====
+# OpenAI 互換APIのbase URL
+# OpenRouterの場合:
+OPENAI_BASE_URL=https://openrouter.ai/api/v1
+#
+# OpenAI公式の場合:
+# OPENAI_BASE_URL=https://api.openai.com/v1
+#
+# カスタムLLMサーバーの場合:
+# OPENAI_BASE_URL=https://your-custom-llm-server/v1
+#
+# デフォルト値: https://openrouter.ai/api/v1 (OpenRouter)
+
+# ===== Hugging Face設定 =====
+# (オプション: データセットアップロード時に使用)
+HUGGINGFACE_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxx
diff --git a/.gitignore b/.gitignore
index 04ce1f8..0d6eb6d 100644
--- a/.gitignore
+++ b/.gitignore
@@ -209,3 +209,11 @@ __marimo__/
 uv.lock
 example/output/structured/logs/
 example/output/
+
+test_output/
+logs.txt
+
+example/input/toho/
+
+output/
+memo.md
diff --git a/README.md b/README.md
index 17cd67d..6687ba5 100644
--- a/README.md
+++ b/README.md
@@ -33,6 +33,10 @@
 - **🤗 HF統合**: Hugging Face Hubへの直接アップロード機能
 - **📊 データセットカード**: 自動的なREADME.md生成でデータセット情報を整理
 - **🔄 変換機能**: 既存XMLファイルからAlpaca形式への変換コマンド
+- **🔍 自動GA検出**: バッチ処理時に各ファイルに対応するGA定義を自動検出
+- **📁 バッチ処理強化**: 複数ファイルの同時処理と個別出力対応
+- **🌐 周辺コンテキストモード**: チャンク前後のチャンクをコンテキストとして活用し、文脈理解を向上
+- **📌 ドキュメント冒頭活用**: 周辺コンテキスト使用時、ドキュメントの冒頭3000文字を常に付与して文脈の安定性を向上
 
 ## 📦 インストール
 
@@ -56,14 +60,34 @@ pip install -e .
 # 環境変数にAPIキーを設定
 export OPENAI_API_KEY="your-api-key-here"
 
-# 元の文章からGAペア定義を自動生成
-uv run easy-dataset create-ga .\example\input\documents\sample_document.txt --output-dir .\example\output\sample_document --num-ga-pairs 10
+# 元の文章からGAペア定義を自動生成（デフォルト: 8000文字まで使用）
+uv run easy-dataset create-ga ./example/input/documents/sample_document.txt --output-dir ./example/output/sample_document --num-ga-pairs 2
+
+# より大きなファイルの場合、コンテキストを制限して処理時間を短くする
+uv run easy-dataset create-ga ./large_document.txt --output-dir ./output --num-ga-pairs 3 --max-context-length 4000
+
+# フォルダ内の全ファイルに対してGAペアをバッチ生成
+uv run easy-dataset create-ga ./example/input/documents/ --output-dir ./example/output/batch_ga_output --num-ga-pairs 2 --max-context-length 6000
 \```
 
 2. **Q&Aペアの生成**
+
+#### 単一ファイルの場合
 \```bash
 # GAペア定義を使ってQ&Aペアを生成
-uv run easy-dataset generate .\example\input\documents\sample_document.txt --ga-file .\example\output\sample_document\ga\ga_definitions.xml --output-dir .\example\output\sample_document\ --chunk-size 500
+uv run easy-dataset generate ./example/input/documents/sample_document.txt --ga-file ./example/output/sample_document/ga/ga_definitions.xml --output-dir ./example/output/sample_document/ --chunk-size 2000
+\```
+
+#### 複数ファイル（バッチ処理）の場合
+\```bash
+# 複数のテキストファイルをバッチ処理
+uv run easy-dataset generate ./example/input/documents/ --ga-file ./example/output/sample_document/ga/ga_definitions.xml --output-dir ./example/output/batch_output/ --chunk-size 2000 --use-surrounding-context 
+\```
+
+#### 自動GA検出機能を使用したバッチ処理
+\```bash
+# 各ファイルに対応するGA定義を自動検出してバッチ処理
+uv run easy-dataset generate ./example/input/documents/ --ga-base-dir ./example/output/batch_ga_output/ --output-dir ./example/output/batch_qa_output/ --chunk-size 2000 --use-surrounding-context 
 \```
 
 ### 🦙 Alpaca形式とHugging Face連携の使用例
@@ -91,6 +115,14 @@ uv run easy-dataset generate .\example\input\documents\sample_document.txt \
   --output-dir .\example\output\sample_document\ \
   --use-thinking \
   --use-fulltext
+
+# 周辺チャンクモードを使ったQ&A生成
+uv run easy-dataset generate .\example\input\documents\sample_document.txt \
+  --ga-file .\example\output\sample_document\ga\ga_definitions.xml \
+  --output-dir .\example\output\sample_document\ \
+  --use-surrounding-context \
+  --context-before 1 \
+  --context-after 2
 \```
 
 #### Hugging Face Hubへの直接アップロード
@@ -124,13 +156,14 @@ uv run easy-dataset convert-to-alpaca .\example\output\sample_document\qa \
 uv run easy-dataset create-ga [OPTIONS] FILE_PATH
 
 Arguments:
-  FILE_PATH  GAペアの定義を生成するための元のテキストファイル [required]
+  FILE_PATH  GAペアの定義を生成するための元のテキストファイルまたはフォルダ [required]
 
 Options:
-  -o, --output-dir DIRECTORY  生成されたGAペア定義ファイルを保存するディレクトリ [required]
-  -m, --model TEXT           GAペア定義の生成に使用するLLMモデル名 [default: openrouter/openai/gpt-4o]
-  -g, --num-ga-pairs INTEGER 生成するGAペアの数。指定しない場合はLLMが適切な数を決定します
-  -h, --help                 Show this message and exit
+  -o, --output-dir DIRECTORY        生成されたGAペア定義ファイルを保存するディレクトリ [required]
+  -m, --model TEXT                 GAペア定義の生成に使用するLLMモデル名 [default: openrouter/openai/gpt-oss-120b]
+  -g, --num-ga-pairs INTEGER       生成するGAペアの数。指定しない場合はLLMが適切な数を決定します
+  -l, --max-context-length INTEGER GA生成時にLLMに渡すコンテキストの最大文字数[default: 8000]
+  -h, --help                       Show this message and exit
 \```
 
 #### 🔧 generate コマンド
@@ -141,16 +174,101 @@ Arguments:
   FILE_PATH  元のテキストファイルへのパス [required]
 
 Options:
-  --ga-file PATH           Genre-Audienceペアを定義したXMLファイル [required]
+  --ga-file PATH           Genre-Audienceペアを定義したXMLファイル。バッチ処理で全ファイルに共通の定義を適用する場合に使用します。
+  --ga-base-dir PATH       GA定義フォルダの親ディレクトリ。バッチ処理時に各入力ファイルに対応するGA定義を自動検出する場合に使用します。
   -o, --output-dir PATH    XMLファイルの出力ディレクトリ
   -m, --model TEXT         Q&Aペアの生成に使用するLLMモデル [default: openrouter/openai/gpt-4o]
   --chunk-size INTEGER     テキストチャンクの最大サイズ [default: 2000]
   --chunk-overlap INTEGER  チャンク間のオーバーラップサイズ [default: 200]
   -f, --use-fulltext       全文をコンテキストとして含めてQA生成を行います。より文脈を理解したQAが生成されますが、処理時間とコストが増加します。
   -T, --use-thinking       各Q&Aペアに思考プロセスを追加して生成します。より深い理解と説明が可能になりますが、処理時間とコストが増加します。
+  -S, --use-surrounding-context 各チャンクの前後チャンクをコンテキストとして含めてQA生成を行います。より文脈を理解したQAが生成されますが、処理時間とコストが増加します。
+  --context-before INTEGER 周辺コンテキストとして含める前方チャンク数 [default: 1]
+  --context-after INTEGER  周辺コンテキストとして含める後方チャンク数 [default: 1]
   -h, --help               Show this message and exit
 \```
 
+#### 🔗 周辺コンテキストモード（`--use-surrounding-context`オプション）
+
+`--use-surrounding-context`オプションを使用すると、各チャンクの前後チャンクをコンテキストとして含めることで、より文脈を理解した高品質なQ&Aペアを生成できます。`--use-fulltext`よりも処理コストが低く抑えられます。
+
+- **`--context-before INTEGER`**: 前方のコンテキストとして含めるチャンク数（デフォルト: 1）
+- **`--context-after INTEGER`**: 後方のコンテキストとして含めるチャンク数（デフォルト: 1）
+
+追加の仕様（v0.2.x以降）:
+- **ドキュメント冒頭を自動付与**: 周辺コンテキストモード有効時は、各プロンプトの先頭にドキュメントの冒頭3000文字が自動的に付与されます。
+  - 目的: 各チャンクの前後だけでは文脈が曖昧になるケースを防ぎ、全体のトピックや用語の基調を共有するため
+  - 上限: 3000文字（固定）
+  - コスト: プロンプト長が増えるため、わずかにトークン消費が増加します
+
+**使用例:**
+\```bash
+# 各チャンクの前後1チャンクずつをコンテキストとして使用
+uv run easy-dataset generate document.txt \
+  --ga-file ga_definitions.xml \
+  --use-surrounding-context
+
+# 前2チャンク、後1チャンクをコンテキストとして使用
+uv run easy-dataset generate document.txt \
+  --ga-file ga_definitions.xml \
+  --use-surrounding-context \
+  --context-before 2 \
+  --context-after 1
+\```
+
+このモードは、長いドキュメントにおいて各チャンクの意味を理解するのに役立ち、トークンサイズ制限を回避しつつ文脈理解を向上させます。
+加えて、ドキュメント冒頭（最大3000文字）を毎回付与することで、用語や話題の基調が共有され、質問・回答の一貫性が高まります。
+
+#### 📝 GA定義ファイルの自動検出機能
+
+`--ga-base-dir`オプションを使用すると、バッチ処理時に各入力ファイルに対応するGA定義ファイルを自動的に検出して使用します。
+
+**動作仕様:**
+- 入力ディレクトリ内の各テキストファイル（例: `doc_A.txt`）の名前を取得
+- `--ga-base-dir`で指定されたパスとファイル名を組み合わせて対応するGA定義ファイルのパスを自動生成（例: `<ga-base-dir>/doc_A/ga/ga_definitions.xml`）
+- そのGA定義ファイルを使って該当ファイルのQ&A生成を行う
+- 入力ディレクトリ内のすべてのファイルに対して上記処理を繰り返す
+
+**使用例:**
+\```bash
+# 各ファイルに対応するGA定義を自動検出してバッチ処理
+uv run easy-dataset generate ./example/input/documents/ \
+  --ga-base-dir ./example/output/batch_ga_output/ \
+  --output-dir ./example/output/batch_qa_output/
+\```
+
+**ディレクトリ構造の例:**
+\```
+example/
+├── input/documents/
+│   ├── doc_A.txt
+│   ├── doc_B.txt
+│   └── doc_C.txt
+├── output/batch_ga_output/
+│   ├── doc_A/
+│   │   └── ga/
+│   │       └── ga_definitions.xml
+│   ├── doc_B/
+│   │   └── ga/
+│   │       └── ga_definitions.xml
+│   └── doc_C/
+│       └── ga/
+│           └── ga_definitions.xml
+└── output/batch_qa_output/
+    ├── doc_A/
+    │   ├── ga/
+    │   ├── logs/
+    │   └── qa/
+    ├── doc_B/
+    │   ├── ga/
+    │   ├── logs/
+    │   └── qa/
+    └── doc_C/
+        ├── ga/
+        ├── logs/
+        └── qa/
+\```
+
 ## 📄 GA定義ファイルの形式
 
 `create-ga`コマンドで自動生成されるGA定義ファイルはXML形式で保存されます：
@@ -227,6 +345,8 @@ Alpaca形式で出力する際、以下の情報を含むREADME.mdが自動生
 
 ### 📁 生成されるファイル構造
 
+#### 単一ファイル処理の場合
+
 \```
 output_directory/
 ├── ga/
@@ -244,6 +364,59 @@ output_directory/
 └── README.md                       # 📊 データセットカード（--export-alpacaオプション使用時）
 \```
 
+#### バッチ処理の場合（--ga-fileオプション使用）
+
+\```
+output_directory/
+├── doc_A/                          # 各入力ファイル用フォルダ
+│   ├── ga/
+│   ├── qa/
+│   ├── logs/
+│   ├── dataset_alpaca.json         # Alpaca形式（--export-alpaca使用時）
+│   └── README.md                   # データセットカード（--export-alpaca使用時）
+├── doc_B/
+│   ├── ga/
+│   ├── qa/
+│   ├── logs/
+│   ├── dataset_alpaca.json
+│   └── README.md
+└── doc_C/
+    ├── ga/
+    ├── qa/
+    ├── logs/
+    ├── dataset_alpaca.json
+    └── README.md
+\```
+
+#### バッチ処理の場合（--ga-base-dirオプション使用）
+
+\```
+output_directory/
+├── doc_A/                          # 各入力ファイル用フォルダ
+│   ├── ga/                         # 空のフォルダ（GA定義は自動検出）
+│   ├── qa/
+│   ├── logs/
+│   ├── dataset_alpaca.json         # Alpaca形式（--export-alpaca使用時）
+│   └── README.md                   # データセットカード（--export-alpaca使用時）
+├── doc_B/
+│   ├── ga/
+│   ├── qa/
+│   ├── logs/
+│   ├── dataset_alpaca.json
+│   └── README.md
+└── doc_C/
+    ├── ga/
+    ├── qa/
+    ├── logs/
+    ├── dataset_alpaca.json
+    └── README.md
+
+# GA定義ファイルは以下のパスから自動検出されます
+# <ga-base-dir>/doc_A/ga/ga_definitions.xml
+# <ga-base-dir>/doc_B/ga/ga_definitions.xml
+# <ga-base-dir>/doc_C/ga/ga_definitions.xml
+\```
+
 ## 🤖 サポートするLLMモデル
 
 ### 🔑 OpenAI（直接）
@@ -355,4 +528,3 @@ MIT License
 
 ### 📄 参考論文
 - **[Dataset Generation for Instruction Tuning](https://arxiv.org/html/2507.04009v1)**
-
diff --git a/easy_dataset_cli/batch_process.py b/easy_dataset_cli/batch_process.py
new file mode 100644
index 0000000..edcec6d
--- /dev/null
+++ b/easy_dataset_cli/batch_process.py
@@ -0,0 +1,414 @@
+#!/usr/bin/env python3
+"""
+バッチ処理機能
+"""
+
+from pathlib import Path
+from rich.console import Console
+from tqdm import tqdm
+
+from .core import (
+    parse_ga_file,
+    split_text,
+    get_chunk_with_surrounding_context,
+    create_augmented_chunks,
+    convert_to_xml_by_genre,
+    create_output_directories
+)
+from .ga_parser import parse_ga_definitions_from_xml_improved
+
+# generatorsパッケージからインポート
+from .generators import (
+    generate_qa_for_chunk_with_ga,
+    generate_qa_for_chunk_with_ga_and_fulltext,
+    generate_qa_for_chunk_with_ga_and_thinking,
+    generate_qa_for_chunk_with_surrounding_context,
+    generate_ga_definitions
+)
+
+console = Console()
+
+
+def _batch_create_ga_files(text_files, output_dir, model, num_ga_pairs, max_context_length=8000):
+    """複数のテキストファイルからGAペアをバッチ生成する内部関数（各ファイルごとにフォルダを作成）"""
+
+    from .core import create_output_directories, save_ga_definitions_by_genre, parse_ga_definitions_from_xml
+
+    total_files = len(text_files)
+    successful_files = []
+
+    for text_file in (tqdm(text_files, desc="GA生成中")):
+            console.print(f"\n[bold cyan]処理中: {text_file.name}[/bold cyan]")
+
+            try:
+                # 各ファイルごとに専用フォルダを作成
+                file_output_dir = output_dir / text_file.stem
+                dirs = create_output_directories(file_output_dir)
+                console.print(f"[dim]✓ ファイル用ディレクトリを作成: {file_output_dir}[/dim]")
+
+                text = text_file.read_text(encoding="utf-8")
+                console.print(f"[dim]✓ テキスト長: {len(text):,} 文字[/dim]")
+
+                with console.status(f"[bold green]🤖 LLMにGAペアの提案を依頼中... ({text_file.name})[/bold green]"):
+                    xml_content = generate_ga_definitions(text, model=model, num_ga_pairs=num_ga_pairs, max_context_length=max_context_length)
+
+                # LLMのrawレスポンスをlogsディレクトリに保存
+                raw_file_path = dirs["logs"] / "raw.md"
+                raw_file_path.write_text(xml_content, encoding="utf-8")
+                console.print(f"[green]✓[/green] LLMのrawレスポンスを保存: [cyan]{raw_file_path.name}[/cyan]")
+
+                with console.status(f"[bold green]🔍 XMLからGAペアを解析中... ({text_file.name})[/bold green]"):
+                    # XMLからGAペアを解析（改良版）
+                    ga_pairs = parse_ga_definitions_from_xml_improved(xml_content)
+
+                if not ga_pairs:
+                    console.print(f"[yellow]警告: {text_file.name} からは有効なGAペアが生成されませんでした[/yellow]")
+                    continue
+
+                # 元のXMLファイルをgaディレクトリに保存（クリーンなXMLのみ）
+                xml_file_path = dirs["ga"] / "ga_definitions.xml"
+                xml_start = xml_content.find("<GADefinitions>")
+                xml_end = xml_content.rfind("</GADefinitions>")
+                if xml_start != -1 and xml_end != -1:
+                    clean_xml = xml_content[xml_start: xml_end + len("</GADefinitions>")]
+                    xml_file_path.write_text(clean_xml, encoding="utf-8")
+                    console.print(f"[green]✓[/green] GA定義XMLファイルを保存: [cyan]{xml_file_path}[/cyan]")
+
+                # Genreごとにマークダウンファイルをgaディレクトリに保存
+                save_ga_definitions_by_genre(ga_pairs, dirs["ga"])
+
+                successful_files.append((text_file.name, file_output_dir, len(ga_pairs)))
+                console.print(f"[green]✓[/green] {len(ga_pairs)}個のGAペアを生成しました")
+
+            except Exception as e:
+                console.print(f"[red]エラー: {text_file.name} の処理に失敗しました: {e}[/red]")
+                continue
+
+            try:
+                # 各ファイルごとに専用フォルダを作成
+                file_output_dir = output_dir / text_file.stem
+                dirs = create_output_directories(file_output_dir)
+                console.print(f"[dim]✓ ファイル用ディレクトリを作成: {file_output_dir}[/dim]")
+
+                text = text_file.read_text(encoding="utf-8")
+                console.print(f"[dim]✓ テキスト長: {len(text):,} 文字[/dim]")
+
+                with console.status(f"[bold green]🤖 LLMにGAペアの提案を依頼中... ({text_file.name})[/bold green]"):
+                    xml_content = generate_ga_definitions(text, model=model, num_ga_pairs=num_ga_pairs, max_context_length=max_context_length)
+
+                # LLMのrawレスポンスをlogsディレクトリに保存
+                raw_file_path = dirs["logs"] / "raw.md"
+                raw_file_path.write_text(xml_content, encoding="utf-8")
+                console.print(f"[green]✓[/green] LLMのrawレスポンスを保存: [cyan]{raw_file_path.name}[/cyan]")
+
+                with console.status(f"[bold green]🔍 XMLからGAペアを解析中... ({text_file.name})[/bold green]"):
+                    # XMLからGAペアを解析（改良版）
+                    ga_pairs = parse_ga_definitions_from_xml_improved(xml_content)
+
+                if not ga_pairs:
+                    console.print(f"[yellow]警告: {text_file.name} からは有効なGAペアが生成されませんでした[/yellow]")
+                    continue
+
+                # 元のXMLファイルをgaディレクトリに保存（クリーンなXMLのみ）
+                xml_file_path = dirs["ga"] / "ga_definitions.xml"
+                xml_start = xml_content.find("<GADefinitions>")
+                xml_end = xml_content.rfind("</GADefinitions>")
+                if xml_start != -1 and xml_end != -1:
+                    clean_xml = xml_content[xml_start: xml_end + len("</GADefinitions>")]
+                    xml_file_path.write_text(clean_xml, encoding="utf-8")
+                    console.print(f"[green]✓[/green] GA定義XMLファイルを保存: [cyan]{xml_file_path}[/cyan]")
+
+                # Genreごとにマークダウンファイルをgaディレクトリに保存
+                save_ga_definitions_by_genre(ga_pairs, dirs["ga"])
+
+                successful_files.append((text_file.name, file_output_dir, len(ga_pairs)))
+                console.print(f"[green]✓[/green] {len(ga_pairs)}個のGAペアを生成しました")
+
+            except Exception as e:
+                console.print(f"[red]エラー: {text_file.name} の処理に失敗しました: {e}[/red]")
+                continue
+
+    # tqdmでループ済み
+
+    if not successful_files:
+        print_error_panel("有効なGAペアが生成されませんでした。\n生成されたXMLの内容を確認してください。")
+        raise typer.Exit(code=1)
+
+    # 成功メッセージを美しく表示
+    total_ga_pairs = sum(count for _, _, count in successful_files)
+    details = [
+        f"{total_ga_pairs}個のGAペアを生成",
+        f"処理済みファイル: {len(successful_files)}/{total_files}個",
+        f"各ファイルごとに専用フォルダを作成"
+    ]
+
+    # 処理されたファイル一覧を表示
+    from rich.table import Table
+    files_table = Table(show_header=True, box=None)
+    files_table.add_column("ファイル", style="cyan")
+    files_table.add_column("フォルダ", style="white")
+    files_table.add_column("GAペア数", style="green")
+
+    for file_name, output_path, ga_count in successful_files:
+        files_table.add_row(file_name, str(output_path), str(ga_count))
+
+    console.print(Table(title="[bold green]📄 処理結果[/bold green]", box=True))
+    console.print(files_table)
+
+    from .commands import print_success_summary
+    print_success_summary("バッチGAペア生成が完了しました！", details)
+
+    from .commands import Panel
+    next_steps_panel = Panel(
+        "🔍 生成されたファイルをレビュー\n"
+        "✏️ 必要に応じて編集\n"
+        "🚀 `generate` コマンドでQ&A生成へ",
+        title="[bold yellow]🔄 次のステップ[/bold yellow]",
+        border_style="yellow"
+    )
+    console.print(next_steps_panel)
+
+
+def _batch_process_files(text_files, ga_file, ga_base_dir, output_dir, model, chunk_size, chunk_overlap,
+                        num_qa_pairs, use_fulltext, use_thinking, use_surrounding_context,
+                        context_before, context_after, append_mode,
+                        export_alpaca, upload_hf, hf_repo_name, hf_token, hf_private):
+    """複数のテキストファイルをバッチ処理する内部関数（各ファイルごとにフォルダを作成）"""
+
+    # GAペアの解析は各ファイルごとに行う（ga_base_dirモードの場合）
+    ga_pairs = None
+    if ga_file:
+        with console.status("🔍 GAペアを解析中..."):
+            ga_pairs = parse_ga_file(ga_file)
+
+        if not ga_pairs:
+            print_error_panel("有効なGAペアが定義ファイルに見つかりませんでした。")
+            raise typer.Exit(code=1)
+
+        console.print(f"\n[green]✓[/green] {len(ga_pairs)}個のGAペアを発見しました")
+
+    # モード警告を表示
+    warnings = []
+    if use_fulltext:
+        warnings.append("📋 全文コンテキストモード")
+    if use_thinking:
+        warnings.append("🤔 思考フローモード")
+    if use_surrounding_context:
+        warnings.append(f"🔗 周辺チャンクモード ({context_before}前+{context_after}後)")
+
+    if warnings:
+        from .commands import Panel
+        warning_panel = Panel(
+            "\n".join(warnings) + "\n\n⚠️ 処理時間とAPIコストが増加する可能性があります",
+            title="[bold yellow]⚠️ モード警告[/bold yellow]",
+            border_style="yellow"
+        )
+        console.print(warning_panel)
+
+    total_files = len(text_files)
+    successful_files = []
+    total_qa_pairs_generated = 0
+
+    for text_file in (tqdm(text_files, desc="ファイル処理中")):
+            console.print(f"\n[bold cyan]処理中: {text_file.name}[/bold cyan]")
+
+            try:
+                # 各ファイルごとに専用フォルダを作成
+                file_output_dir = output_dir / text_file.stem
+                dirs = create_output_directories(file_output_dir)
+                console.print(f"[dim]✓ ファイル用ディレクトリを作成: {file_output_dir}[/dim]")
+
+                text = text_file.read_text(encoding="utf-8")
+                console.print(f"[dim]✓ テキスト長: {len(text):,} 文字[/dim]")
+
+                # GAファイルのパスを決定するロジック
+                current_ga_path = None
+                if ga_file:
+                    # 従来通り、指定された単一のGAファイルを使用
+                    current_ga_path = ga_file
+                    console.print(f"[dim]✓ 使用するGA定義: {current_ga_path}[/dim]")
+                elif ga_base_dir:
+                    # 入力ファイル名から対応するGAファイルのパスを組み立てる
+                    file_stem = text_file.stem
+                    inferred_ga_path = ga_base_dir / file_stem / "ga" / "ga_definitions.xml"
+
+                    if inferred_ga_path.exists():
+                        current_ga_path = inferred_ga_path
+                        console.print(f"[dim]✓ GA定義を自動検出: {current_ga_path}[/dim]")
+                    else:
+                        console.print(f"[yellow]警告: {text_file.name} に対応するGA定義が見つかりませんでした。スキップします。[/yellow]")
+                        console.print(f"[dim]検索パス: {inferred_ga_path}[/dim]")
+                        continue  # 次のファイルへ
+
+                # GAペアを解析
+                with console.status("🔍 GAペアを解析中..."):
+                    current_ga_pairs = parse_ga_file(current_ga_path)
+
+                if not current_ga_pairs:
+                    console.print(f"[yellow]警告: {text_file.name} のGA定義から有効なGAペアが見つかりませんでした。スキップします。[/yellow]")
+                    continue
+
+                console.print(f"[green]✓[/green] {len(current_ga_pairs)}個のGAペアを発見")
+
+                with console.status(f"✂️ テキストをチャンクに分割中... ({text_file.name})"):
+                    chunks = split_text(text, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
+                console.print(f"[green]✓[/green] {len(chunks)}個のチャンクを作成")
+
+                # 周辺コンテキストモードの場合、チャンクを拡張
+                if use_surrounding_context:
+                    with console.status(f"🔗 周辺コンテキストを生成中... ({text_file.name})"):
+                        augmented_chunks = create_augmented_chunks(chunks, context_before, context_after)
+                    console.print(f"[green]✓[/green] {len(augmented_chunks)}個の拡張チャンクを作成")
+
+                all_qa_pairs_with_ga = []
+                total_tasks_for_file = len(chunks) * len(current_ga_pairs)
+                # tqdmサブバー
+                from tqdm import tqdm as _tqdm
+                pbar_ctx = _tqdm(total=total_tasks_for_file, desc=text_file.name, leave=False)
+                # 進捗の更新は後続のループ内で行う
+
+                if use_surrounding_context:
+                    # 周辺コンテキストモードの処理
+                    # ドキュメント冒頭（最大3000文字）を付与して文脈の安定性を高める
+                    doc_head = text[:3000]
+                    for i, (target_chunk, augmented_content, _) in enumerate(augmented_chunks):
+                        for ga_pair in current_ga_pairs:
+                            content_with_head = (
+                                f"【ドキュメント冒頭（最大3000文字）】:\n{doc_head}\n\n" +
+                                augmented_content
+                            )
+                            qa_pairs = generate_qa_for_chunk_with_surrounding_context(
+                                content=content_with_head,
+                                model=model,
+                                ga_pair=ga_pair,
+                                logs_dir=dirs["logs"],
+                                num_qa_pairs=num_qa_pairs
+                            )
+
+                            for pair in qa_pairs:
+                                qa_entry = {
+                                    "genre": ga_pair['genre']['title'],
+                                    "audience": ga_pair['audience']['title'],
+                                    "question": pair['question'],
+                                    "answer": pair['answer']
+                                }
+                                all_qa_pairs_with_ga.append(qa_entry)
+
+                            pbar_ctx.update(1)
+                else:
+                    # 通常モードの処理
+                    for chunk in chunks:
+                        for ga_pair in current_ga_pairs:
+                            if use_thinking:
+                                qa_pairs = generate_qa_for_chunk_with_ga_and_thinking(
+                                    chunk=chunk,
+                                    full_text=text if use_fulltext else "",
+                                    model=model,
+                                    ga_pair=ga_pair,
+                                    logs_dir=dirs["logs"],
+                                    num_qa_pairs=num_qa_pairs
+                                )
+                            elif use_fulltext:
+                                qa_pairs = generate_qa_for_chunk_with_ga_and_fulltext(
+                                    chunk=chunk,
+                                    full_text=text,
+                                    model=model,
+                                    ga_pair=ga_pair,
+                                    logs_dir=dirs["logs"],
+                                    num_qa_pairs=num_qa_pairs
+                                )
+                            else:
+                                qa_pairs = generate_qa_for_chunk_with_ga(
+                                    chunk, model=model, ga_pair=ga_pair,
+                                    logs_dir=dirs["logs"],
+                                    num_qa_pairs=num_qa_pairs
+                                )
+
+                            for pair in qa_pairs:
+                                qa_entry = {
+                                    "genre": ga_pair['genre']['title'],
+                                    "audience": ga_pair['audience']['title'],
+                                    "question": pair['question'],
+                                    "answer": pair['answer']
+                                }
+                                all_qa_pairs_with_ga.append(qa_entry)
+
+                            pbar_ctx.update(1)
+                # close tqdm sub-bar if used
+                pbar_ctx.close()
+
+                # このファイルのQ&AペアをXMLに変換して保存
+                xml_outputs_by_genre = convert_to_xml_by_genre(all_qa_pairs_with_ga, dirs["qa"], append_mode)
+
+                saved_files = []
+                for genre, xml_content in xml_outputs_by_genre.items():
+                    from .core import sanitize_filename
+                    safe_genre_name = sanitize_filename(genre)
+                    output_file_path = dirs["qa"] / f"{safe_genre_name}.xml"
+                    output_file_path.write_text(xml_content, encoding="utf-8")
+                    saved_files.append(output_file_path.name)
+
+                # アルパカ形式でのエクスポート（ファイル個別）
+                if export_alpaca:
+                    from .core import convert_all_xml_to_alpaca, create_dataset_card
+                    alpaca_file = dirs["base"] / "dataset_alpaca.json"
+                    alpaca_data = convert_all_xml_to_alpaca(dirs["qa"], alpaca_file)
+
+                    # データセットカードを生成
+                    readme_file = dirs["base"] / "README.md"
+                    create_dataset_card(alpaca_data, readme_file, f"Generated QA Dataset from {text_file.name}")
+
+                successful_files.append((text_file.name, file_output_dir, len(all_qa_pairs_with_ga), saved_files))
+                total_qa_pairs_generated += len(all_qa_pairs_with_ga)
+                console.print(f"[green]✓[/green] {len(all_qa_pairs_with_ga)}個のQ&Aペアを生成")
+
+            except Exception as e:
+                console.print(f"[red]エラー: {text_file.name} の処理に失敗しました: {e}[/red]")
+                continue
+
+    # tqdmで外側ループ済み
+
+    if not successful_files:
+        from .commands import print_error_panel
+        print_error_panel("有効なQ&Aペアが生成されませんでした。")
+        import typer
+        raise typer.Exit(code=1)
+
+    # 成功メッセージを美しく表示
+    details = [
+        f"{total_qa_pairs_generated}個のQ&Aペアを生成",
+        f"処理済みファイル: {len(successful_files)}/{total_files}個",
+        f"各ファイルごとに専用フォルダを作成"
+    ]
+
+    # 処理されたファイル一覧を表示
+    from rich.table import Table
+    files_table = Table(show_header=True, box=None)
+    files_table.add_column("ファイル", style="cyan")
+    files_table.add_column("フォルダ", style="white")
+    files_table.add_column("Q&Aペア数", style="green")
+
+    for file_name, output_path, qa_count, _ in successful_files:
+        files_table.add_row(file_name, str(output_path), str(qa_count))
+
+    console.print(Table(title="[bold green]📄 処理結果[/bold green]", box=True))
+    console.print(files_table)
+
+    from .commands import print_success_summary
+    print_success_summary("バッチQ&A生成が完了しました！", details)
+
+    # Hugging Face Hubへのアップロード処理（最初の成功ファイルのみ、またはユーザーが個別指定）
+    if upload_hf and export_alpaca:
+        if not hf_repo_name:
+            console.print("[bold red]--hf-repo-nameが指定されていません！[/bold red]")
+            console.print("[yellow]例: --hf-repo-name username/my-qa-dataset[/yellow]")
+        else:
+            console.print(f"\n[bold blue]Hugging Face Hub アップロードについて[/bold blue]")
+            console.print("[yellow]注意: 現在は各ファイルが個別のフォルダに保存されているため、")
+            console.print("個別にアップロードするか、統合してアップロードするかを選択してください。[/yellow]")
+
+
+def print_error_panel(error_msg: str):
+    """エラーメッセージを美しく表示"""
+    panel = f"[bold red]❌ エラー[/bold red]\n{error_msg}"
+    console.print(panel)
diff --git a/easy_dataset_cli/commands.py b/easy_dataset_cli/commands.py
new file mode 100644
index 0000000..3c96394
--- /dev/null
+++ b/easy_dataset_cli/commands.py
@@ -0,0 +1,753 @@
+#!/usr/bin/env python3
+"""
+コマンド関数群 - CLIコマンドの実装
+"""
+
+from pathlib import Path
+from typing_extensions import Annotated
+import typer
+from rich.console import Console
+from rich.text import Text
+from rich.panel import Panel
+from rich.columns import Columns
+from rich.table import Table
+from dotenv import load_dotenv
+
+from .generators import (
+    generate_qa_for_chunk_with_ga,
+    generate_qa_for_chunk_with_ga_and_fulltext,
+    generate_qa_for_chunk_with_ga_and_thinking,
+    generate_qa_for_chunk_with_surrounding_context,
+    generate_ga_definitions
+)
+from .xml_utils import load_existing_xml_file
+from .core import (
+    parse_ga_file,
+    parse_ga_definitions_from_xml,
+    save_ga_definitions_by_genre,
+    create_output_directories,
+    sanitize_filename,
+    convert_all_xml_to_alpaca,
+    upload_to_huggingface,
+    create_dataset_card,
+    find_text_files,
+    get_chunk_with_surrounding_context,
+    create_augmented_chunks,
+    split_text
+)
+from .ga_parser import parse_ga_definitions_from_xml_improved
+from .batch_process import (
+    _batch_create_ga_files,
+    _batch_process_files
+)
+
+# .envファイルを読み込む
+load_dotenv()
+
+app = typer.Typer(
+    help="テキストファイルからQ&Aペアを生成するおしゃれなCLIツール。",
+    context_settings={"help_option_names": ["-h", "--help"]}
+)
+console = Console()
+
+
+def print_success_summary(message: str, details: list = None):
+    """成功メッセージを美しく表示"""
+    panel = Panel(
+        f"[bold green]✨ {message}[/bold green]",
+        border_style="green",
+        padding=(1, 2)
+    )
+    console.print(panel)
+
+    if details:
+        table = Table(show_header=False, box=None)
+        table.add_column("Item", style="cyan")
+        for detail in details:
+            table.add_row(f"  • {detail}")
+        console.print(table)
+
+
+def print_error_panel(error_msg: str):
+    """エラーメッセージを美しく表示"""
+    panel = Panel(
+        f"[bold red]❌ エラー[/bold red]\n{error_msg}",
+        border_style="red",
+        padding=(1, 2)
+    )
+    console.print(panel)
+
+
+@app.command()
+def create_ga(
+    file_path: Annotated[Path, typer.Argument(
+        exists=True, readable=True,
+        help="GAペアの定義を生成するための元のテキストファイルまたはフォルダ。フォルダを指定した場合、内部のテキストファイルをバッチ処理します。"
+    )],
+    output_dir: Annotated[Path, typer.Option(
+        "--output-dir", "-o", file_okay=False, dir_okay=True, writable=True,
+        help="生成されたGAペア定義ファイルを保存するディレクトリ。"
+    )],
+    model: Annotated[str, typer.Option(
+        "--model", "-m",
+        help="GAペア定義の生成に使用するLLMモデル名。"
+    )] = "openai/gpt-oss-120b",
+    num_ga_pairs: Annotated[int, typer.Option(
+        "--num-ga-pairs", "-g",
+        help="生成するGAペアの数。指定しない場合はLLMが適切な数を決定します。"
+    )] = 5,
+    max_context_length: Annotated[int, typer.Option(
+        "--max-context-length", "-l",
+        help="GA生成時にLLMに渡すコンテキストの最大文字数。デフォルトは8000文字です。処理時間を短くしたい場合やコストを抑えたい場合に小さく設定してください。"
+    )] = 8000,
+):
+    """元の文章を分析し、GAペア定義をXML形式で生成し、Genreごとにマークダウンファイルに保存します。"""
+
+    try:
+        # フォルダかファイルかを判定
+        if file_path.is_dir():
+            # フォルダの場合：バッチ処理
+            console.print(f"[bold blue]📁 フォルダ処理モード: {file_path}[/bold blue]")
+            text_files = find_text_files(file_path)
+
+            if not text_files:
+                print_error_panel(f"指定されたフォルダにテキストファイルが見つかりませんでした: {file_path}")
+                raise typer.Exit(code=1)
+
+            console.print(f"[green]✓[/green] {len(text_files)}個のテキストファイルを発見しました")
+
+            # バッチ処理用の設定テーブル
+            batch_info_table = Table(show_header=False, box=None)
+            batch_info_table.add_column("Key", style="bold cyan")
+            batch_info_table.add_column("Value", style="white")
+            batch_info_table.add_row("📁 入力フォルダ", str(file_path))
+            batch_info_table.add_row("📄 ファイル数", str(len(text_files)))
+            batch_info_table.add_row("📁 出力ディレクトリ", str(output_dir))
+            batch_info_table.add_row("🤖 モデル", model)
+            batch_info_table.add_row("🔢 GAペア数", str(num_ga_pairs))
+            batch_info_table.add_row("📏 コンテキスト文字数上限", f"{max_context_length:,}")
+
+            console.print(Panel(batch_info_table, title="[bold blue]🚀 バッチGAペア生成設定[/bold blue]", border_style="blue"))
+
+            # ファイル一覧を表示
+            files_table = Table(show_header=False, box=None)
+            files_table.add_column("ファイル", style="cyan")
+            for text_file in text_files[:10]:  # 最初の10個のみ表示
+                files_table.add_row(f"• {text_file.name}")
+            if len(text_files) > 10:
+                files_table.add_row(f"... and {len(text_files) - 10} more files")
+
+            console.print(Panel(files_table, title="[bold green]📄 処理予定ファイル[/bold green]", border_style="green"))
+
+            return _batch_create_ga_files(text_files, output_dir, model, num_ga_pairs, max_context_length)
+        else:
+            # 単一ファイルの場合：既存の処理
+            info_table = Table(show_header=False, box=None)
+            info_table.add_column("Key", style="bold cyan")
+            info_table.add_column("Value", style="white")
+            info_table.add_row("📄 入力ファイル", str(file_path))
+            info_table.add_row("📁 出力ディレクトリ", str(output_dir))
+            info_table.add_row("🤖 モデル", model)
+            info_table.add_row("🔢 GAペア数", str(num_ga_pairs))
+            info_table.add_row("📏 コンテキスト文字数上限", f"{max_context_length:,}")
+
+            console.print(Panel(info_table, title="[bold blue]🚀 GAペア生成設定[/bold blue]", border_style="blue"))
+
+            text = file_path.read_text(encoding="utf-8")
+            console.print(f"[dim]✓ テキスト長: {len(text):,} 文字を読み込みました[/dim]\n")
+
+        with console.status("[bold green]🤖 LLMにGAペアの提案を依頼中...[/bold green]"):
+            xml_content = generate_ga_definitions(text, model=model, num_ga_pairs=num_ga_pairs, max_context_length=max_context_length)
+
+        # 出力ディレクトリ構造を作成
+        dirs = create_output_directories(output_dir)
+        console.print(f"\n[dim]✓ 出力ディレクトリを作成: ga/, logs/, qa/[/dim]")
+
+        # LLMのrawレスポンスをlogsディレクトリに保存
+        raw_file_path = dirs["logs"] / "raw.md"
+        raw_file_path.write_text(xml_content, encoding="utf-8")
+        console.print(f"[green]✓[/green] LLMのrawレスポンスを保存: [cyan]{raw_file_path.name}[/cyan]")
+
+        with console.status("[bold green]🔍 XMLからGAペアを解析中...[/bold green]"):
+            # XMLからGAペアを解析（改良版）
+            ga_pairs = parse_ga_definitions_from_xml_improved(xml_content)
+
+        if not ga_pairs:
+            print_error_panel("有効なGAペアが生成されませんでした。\n生成されたXMLの内容を確認してください。")
+            console.print(Panel(xml_content, title="生成されたXML", border_style="yellow"))
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
+            console.print(f"[green]✓[/green] GA定義XMLファイルを保存: [cyan]{xml_file_path.name}[/cyan]")
+
+        # Genreごとにマークダウンファイルをgaディレクトリに保存
+        save_ga_definitions_by_genre(ga_pairs, dirs["ga"])
+
+        # 成功メッセージを美しく表示
+        details = [
+            f"{len(ga_pairs)}個のGAペアを生成",
+            f"保存先: {dirs['ga']}",
+            "XMLファイルとマークダウンファイルを作成"
+        ]
+        print_success_summary("GAペアの生成が完了しました！", details)
+
+        next_steps_panel = Panel(
+            "🔍 生成されたファイルをレビュー\n"
+            "✏️ 必要に応じて編集\n"
+            "🚀 `generate` コマンドでQ&A生成へ",
+            title="[bold yellow]🔄 次のステップ[/bold yellow]",
+            border_style="yellow"
+        )
+        console.print(next_steps_panel)
+
+    except Exception as e:
+        print_error_panel(f"GA定義ファイルの生成中にエラーが発生しました:\n{e}")
+        raise typer.Exit(code=1)
+
+
+@app.command()
+def generate(
+    file_path: Annotated[Path, typer.Argument(
+        exists=True, readable=True,
+        help="元のテキストファイルまたはフォルダへのパス。フォルダを指定した場合、内部のテキストファイルをバッチ処理します。"
+    )],
+    ga_file: Annotated[Path, typer.Option(
+        "--ga-file", "-g", exists=True, dir_okay=False, readable=True,
+        help="Genre-Audienceペアを定義したXMLまたはMarkdownファイルへのパス。バッチ処理で全ファイルに共通の定義を適用する場合に使用します。"
+    )] = None,
+    ga_base_dir: Annotated[Path, typer.Option(
+        "--ga-base-dir", "-gb", exists=True, file_okay=False, dir_okay=True, readable=True,
+        help="GA定義フォルダの親ディレクトリ。バッチ処理時に各入力ファイルに対応するGA定義を自動検出する場合に使用します。"
+    )] = None,
+    output_dir: Annotated[Path, typer.Option(
+        "--output-dir", "-o", file_okay=False, dir_okay=True, writable=True,
+        help="生成されたXMLファイルを保存するディレクトリ。指定しない場合はコンソールに出力します。"
+    )] = None,
+    model: Annotated[str, typer.Option(
+        "--model", "-m",
+        help="Q&Aペアの生成に使用するLLMモデル名。"
+    )] = "openai/gpt-oss-120b",
+    chunk_size: Annotated[int, typer.Option(
+        help="テキストチャンクの最大サイズ。"
+    )] = 2000,
+    chunk_overlap: Annotated[int, typer.Option(
+        help="チャンク間のオーバーラップサイズ。"
+    )] = 200,
+    num_qa_pairs: Annotated[int, typer.Option(
+        "--num-qa-pairs", "-q",
+        help="各チャンク・GAペアの組み合わせで生成するQ&Aペアの数。指定しない場合はLLMが適切な数を決定します。"
+    )] = 10,
+    use_fulltext: Annotated[bool, typer.Option(
+        "--use-fulltext", "-f",
+        help="全文をコンテキストとして含めてQA生成を行います。より文脈を理解したQAが生成されますが、処理時間とコストが増加します。"
+    )] = False,
+    use_thinking: Annotated[bool, typer.Option(
+        "--use-thinking", "-T",
+        help="各Q&Aペアに思考プロセスを追加して生成します。より深い理解と説明が可能になりますが、処理時間とコストが増加します。"
+    )] = False,
+    use_surrounding_context: Annotated[bool, typer.Option(
+        "--use-surrounding-context", "-S",
+        help="各チャンクの前後チャンクをコンテキストとして含めてQA生成を行います。より文脈を理解したQAが生成されますが、処理時間とコストが増加します。"
+    )] = False,
+    context_before: Annotated[int, typer.Option(
+        help="周辺コンテキストとして含める前方チャンク数。"
+    )] = 1,
+    context_after: Annotated[int, typer.Option(
+        help="周辺コンテキストとして含める後方チャンク数。"
+    )] = 1,
+    append_mode: Annotated[bool, typer.Option(
+        "--append", "-A",
+        help="既存のXMLファイルに新しいQ&Aを追加します。指定しない場合は上書きします。"
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
+):
+    """テキストファイルとGA定義からQ&Aペアを生成し、Genre別のXMLファイルとして出力します。
+
+    --use-fulltextオプションを使用すると、各チャンクの処理時に全文をコンテキストとして含めることで、
+    より文脈を理解した高品質なQ&Aペアを生成できます。ただし、処理時間とAPIコストが増加します。
+
+    --use-surrounding-contextオプションを使用すると、各チャンクの前後チャンクをコンテキストとして含めることで、
+    より文脈を理解した高品質なQ&Aペアを生成できます。--use-fulltextよりも処理コストが低く抑えられます。
+    --context-beforeと--context-afterで前後のチャンク数を調整可能です。
+    """
+
+    try:
+        # フォルダかファイルかを判定
+        if file_path.is_dir():
+            # フォルダの場合：バッチ処理
+            console.print(f"[bold blue]📁 フォルダ処理モード: {file_path}[/bold blue]")
+            text_files = find_text_files(file_path)
+
+            if not text_files:
+                print_error_panel(f"指定されたフォルダにテキストファイルが見つかりませんでした: {file_path}")
+                raise typer.Exit(code=1)
+
+            console.print(f"[green]✓[/green] {len(text_files)}個のテキストファイルを発見しました")
+
+            # バッチ処理用の設定テーブル
+            batch_settings_table = Table(show_header=False, box=None)
+            batch_settings_table.add_column("項目", style="bold cyan")
+            batch_settings_table.add_column("値", style="white")
+            batch_settings_table.add_row("📁 入力フォルダ", str(file_path))
+            batch_settings_table.add_row("📄 ファイル数", str(len(text_files)))
+
+            # GA定義の表示
+            if ga_file:
+                batch_settings_table.add_row("📊 GA定義", str(ga_file))
+            elif ga_base_dir:
+                batch_settings_table.add_row("📊 GA定義ベースディレクトリ", str(ga_base_dir))
+            else:
+                batch_settings_table.add_row("📊 GA定義", "未指定")
+
+            batch_settings_table.add_row("📁 出力先", str(output_dir) if output_dir else "コンソール")
+            batch_settings_table.add_row("🤖 モデル", model)
+            batch_settings_table.add_row("🔢 Q&A数/チャンク", str(num_qa_pairs))
+
+            mode_options = []
+            if use_fulltext: mode_options.append("📋 全文コンテキスト")
+            if use_thinking: mode_options.append("🤔 思考フロー")
+            if use_surrounding_context: mode_options.append(f"🔗 周辺コンテキスト ({context_before}前+{context_after}後)")
+            if append_mode: mode_options.append("➕ 追加モード")
+            if export_alpaca: mode_options.append("🤙 Alpaca形式")
+            if upload_hf: mode_options.append("🤗 HFアップロード")
+
+            if mode_options:
+                batch_settings_table.add_row("⚙️ オプション", ", ".join(mode_options))
+
+            console.print(Panel(batch_settings_table, title="[bold blue]🚀 バッチQ&A生成設定[/bold blue]", border_style="blue"))
+
+            # ファイル一覧を表示
+            files_table = Table(show_header=False, box=None)
+            files_table.add_column("ファイル", style="cyan")
+            for text_file in text_files[:10]:  # 最初の10個のみ表示
+                files_table.add_row(f"• {text_file.name}")
+            if len(text_files) > 10:
+                files_table.add_row(f"... and {len(text_files) - 10} more files")
+
+            console.print(Panel(files_table, title="[bold green]📄 処理予定ファイル[/bold green]", border_style="green"))
+
+            # バッチ処理のバリデーション
+            if not ga_file and not ga_base_dir:
+                print_error_panel("バッチ処理を行うには、--ga-file または --ga-base-dir のいずれかを指定する必要があります。")
+                raise typer.Exit(code=1)
+
+            if ga_file and ga_base_dir:
+                print_error_panel("--ga-file と --ga-base-dir は同時に使用できません。")
+                raise typer.Exit(code=1)
+
+            # 各ファイルをバッチ処理
+            return _batch_process_files(text_files, ga_file, ga_base_dir, output_dir, model, chunk_size, chunk_overlap,
+                                      num_qa_pairs, use_fulltext, use_thinking, use_surrounding_context,
+                                      context_before, context_after, append_mode,
+                                      export_alpaca, upload_hf, hf_repo_name, hf_token, hf_private)
+        else:
+            # 単一ファイルの場合：既存の処理
+            # 設定情報をテーブルで表示
+            settings_table = Table(show_header=False, box=None)
+            settings_table.add_column("項目", style="bold cyan")
+            settings_table.add_column("値", style="white")
+            settings_table.add_row("📄 入力ファイル", str(file_path))
+            settings_table.add_row("📊 GA定義", str(ga_file) if ga_file else "未指定")
+            settings_table.add_row("📁 出力先", str(output_dir) if output_dir else "コンソール")
+            settings_table.add_row("🤖 モデル", model)
+            settings_table.add_row("🔢 Q&A数/チャンク", str(num_qa_pairs))
+
+            mode_options = []
+            if use_fulltext: mode_options.append("📋 全文コンテキスト")
+            if use_thinking: mode_options.append("🤔 思考フロー")
+            if use_surrounding_context: mode_options.append(f"🔗 周辺コンテキスト ({context_before}前+{context_after}後)")
+            if append_mode: mode_options.append("➕ 追加モード")
+            if export_alpaca: mode_options.append("🤙 Alpaca形式")
+            if upload_hf: mode_options.append("🤗 HFアップロード")
+
+            if mode_options:
+                settings_table.add_row("⚙️ オプション", ", ".join(mode_options))
+
+            console.print(Panel(settings_table, title="[bold blue]🚀 Q&A生成設定[/bold blue]", border_style="blue"))
+
+            # 単一ファイル処理のバリデーション
+            if not ga_file:
+                print_error_panel("単一ファイル処理には --ga-file の指定が必須です。")
+                raise typer.Exit(code=1)
+
+            text = file_path.read_text(encoding="utf-8")
+            console.print(f"\n[dim]✓ テキスト長: {len(text):,} 文字を読み込みました[/dim]")
+
+        with console.status("🔍 GAペアを解析中..."):
+            ga_pairs = parse_ga_file(ga_file)
+
+        if not ga_pairs:
+            print_error_panel("有効なGAペアが定義ファイルに見つかりませんでした。")
+            raise typer.Exit(code=1)
+
+        console.print(f"\n[green]✓[/green] {len(ga_pairs)}個のGAペアを発見しました")
+
+        with console.status("✂️ テキストをチャンクに分割中..."):
+            chunks = split_text(text, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
+        console.print(f"[green]✓[/green] {len(chunks)}個のチャンクを作成しました")
+
+        # 周辺コンテキストモードの場合、チャンクを拡張
+        if use_surrounding_context:
+            with console.status("🔗 周辺コンテキストを生成中..."):
+                augmented_chunks = create_augmented_chunks(chunks, context_before, context_after)
+            console.print(f"[green]✓[/green] {len(augmented_chunks)}個の拡張チャンクを作成しました")
+
+        all_qa_pairs_with_ga = []
+        total_tasks = len(chunks) * len(ga_pairs)
+
+        # 出力ディレクトリがある場合は構造を作成
+        dirs = None
+        if output_dir:
+            dirs = create_output_directories(output_dir)
+            console.print(f"[dim]✓ 出力ディレクトリを作成: ga/, logs/, qa/[/dim]")
+
+        # モード警告を表示
+        warnings = []
+        if use_fulltext:
+            warnings.append(f"📋 全文コンテキストモード ({len(text):,} 文字)")
+        if use_thinking:
+            warnings.append("🤔 思考フローモード")
+        if use_surrounding_context:
+            warnings.append(f"🔗 周辺チャンクモード ({context_before}前+{context_after}後)")
+
+        if warnings:
+            warning_panel = Panel(
+                "\n".join(warnings) + "\n\n⚠️ 処理時間とAPIコストが増加する可能性があります",
+                title="[bold yellow]⚠️ モード警告[/bold yellow]",
+                border_style="yellow"
+            )
+            console.print(warning_panel)
+
+        # tqdmベースの進捗表示に統一
+        from tqdm import tqdm
+        desc = "Q&A生成中"
+        iterable_outer = augmented_chunks if use_surrounding_context else chunks
+        with tqdm(total=total_tasks, desc=desc) as pbar:
+            if use_surrounding_context:
+                doc_head = text[:3000]
+                for i, (target_chunk, augmented_content, _) in enumerate(iterable_outer):
+                    for ga_pair in ga_pairs:
+                        content_with_head = (
+                            f"### 【ドキュメント冒頭（最大3000文字）】-----------:\n\```\n{doc_head}\n\```\n" +
+                            augmented_content
+                        )
+                        qa_pairs = generate_qa_for_chunk_with_surrounding_context(
+                            content=content_with_head,
+                            model=model,
+                            ga_pair=ga_pair,
+                            logs_dir=dirs["logs"] if dirs else None,
+                            num_qa_pairs=num_qa_pairs
+                        )
+
+                        for pair in qa_pairs:
+                            qa_entry = {
+                                "genre": ga_pair['genre']['title'],
+                                "audience": ga_pair['audience']['title'],
+                                "question": pair['question'],
+                                "answer": pair['answer']
+                            }
+                            all_qa_pairs_with_ga.append(qa_entry)
+
+                        pbar.update(1)
+            else:
+                for chunk in iterable_outer:
+                    for ga_pair in ga_pairs:
+                        if use_thinking:
+                            qa_pairs = generate_qa_for_chunk_with_ga_and_thinking(
+                                chunk=chunk,
+                                full_text=text if use_fulltext else "",
+                                model=model,
+                                ga_pair=ga_pair,
+                                logs_dir=dirs["logs"] if dirs else None,
+                                num_qa_pairs=num_qa_pairs
+                            )
+                        elif use_fulltext:
+                            qa_pairs = generate_qa_for_chunk_with_ga_and_fulltext(
+                                chunk=chunk,
+                                full_text=text,
+                                model=model,
+                                ga_pair=ga_pair,
+                                logs_dir=dirs["logs"] if dirs else None,
+                                num_qa_pairs=num_qa_pairs
+                            )
+                        else:
+                            qa_pairs = generate_qa_for_chunk_with_ga(
+                                chunk, model=model, ga_pair=ga_pair,
+                                logs_dir=dirs["logs"] if dirs else None,
+                                num_qa_pairs=num_qa_pairs
+                            )
+
+                        for pair in qa_pairs:
+                            qa_entry = {
+                                "genre": ga_pair['genre']['title'],
+                                "audience": ga_pair['audience']['title'],
+                                "question": pair['question'],
+                                "answer": pair['answer']  # <think>...</think>回答...形式がそのまま入る
+                            }
+                            all_qa_pairs_with_ga.append(qa_entry)
+
+                        pbar.update(1)
+
+        generation_summary = Panel(
+            f"✨ [bold green]{len(all_qa_pairs_with_ga)}[/bold green] 個のQ&Aペアを生成完了！",
+            title="[bold green]✅ 生成結果[/bold green]",
+            border_style="green"
+        )
+        console.print(generation_summary)
+
+        if dirs:
+            from .xml_utils import convert_to_xml_by_genre
+
+            xml_outputs_by_genre = convert_to_xml_by_genre(all_qa_pairs_with_ga, dirs["qa"], append_mode)
+
+            with console.status(f"💾 XMLファイルを {dirs['qa']} に保存中..."):
+                saved_files = []
+                for genre, xml_content in xml_outputs_by_genre.items():
+                    safe_genre_name = sanitize_filename(genre)
+                    output_file_path = dirs["qa"] / f"{safe_genre_name}.xml"
+                    output_file_path.write_text(xml_content, encoding="utf-8")
+                    saved_files.append(output_file_path.name)
+
+            files_table = Table(show_header=False, box=None)
+            files_table.add_column("ファイル", style="cyan")
+            for file_name in saved_files:
+                files_table.add_row(f"✓ {file_name}")
+
+                console.print(Panel(files_table, title="[bold green]💾 保存済みファイル[/bold green]", border_style="green"))
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
+        else:
+            console.print("\n--- 生成されたQ&Aペア (Genre別XML) ---")
+            if dirs:
+                from .xml_utils import convert_to_xml_by_genre
+                xml_outputs_by_genre = convert_to_xml_by_genre(all_qa_pairs_with_ga, None, append_mode)
+                for genre, xml_content in xml_outputs_by_genre.items():
+                    console.print(f"\n[bold yellow]## Genre: {genre} ##[/bold yellow]")
+                    console.print(xml_content, overflow="fold")
+
+    except Exception as e:
+        import traceback
+        error_details = f"エラータイプ: {type(e).__name__}\nメッセージ: {str(e)}\n\nトレースバック:\n{traceback.format_exc()}"
+        print_error_panel(error_details)
+        raise typer.Exit(code=1)
+
+
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
+    conversion_table = Table(show_header=False, box=None)
+    conversion_table.add_column("項目", style="bold cyan")
+    conversion_table.add_column("値", style="white")
+    conversion_table.add_row("📁 入力ディレクトリ", str(qa_dir))
+    conversion_table.add_row("💾 出力ファイル", str(output_file) if output_file else "自動")
+    if upload_hf:
+        conversion_table.add_row("🤗 HFリポジトリ", hf_repo_name or "未指定")
+
+    console.print(Panel(conversion_table, title="[bold blue]🔄 Alpaca形式変換[/bold blue]", border_style="blue"))
+
+    try:
+        # デフォルトの出力ファイル名を設定
+        if output_file is None:
+            output_file = qa_dir.parent / "dataset_alpaca.json"
+
+        with console.status(f"🔄 XMLファイルをAlpaca形式に変換中..."):
+            alpaca_data = convert_all_xml_to_alpaca(qa_dir, output_file)
+
+        if not alpaca_data:
+            print_error_panel("変換できるデータが見つかりませんでした。")
+            raise typer.Exit(code=1)
+
+        with console.status("📋 データセットカードを生成中..."):
+            readme_file = output_file.parent / "README.md"
+            create_dataset_card(alpaca_data, readme_file, "Converted QA Dataset")
+
+        # Hugging Face Hubにアップロード
+        if upload_hf:
+            if not hf_repo_name:
+                print_error_panel("--hf-repo-nameが指定されていません！\n例: --hf-repo-name username/my-qa-dataset")
+                raise typer.Exit(code=1)
+
+            with console.status(f"🤗 Hugging Face Hubにアップロード中..."):
+                success = upload_to_huggingface(
+                    dataset_data=alpaca_data,
+                    repo_name=hf_repo_name,
+                    hf_token=hf_token if hf_token else None,
+                    private=hf_private,
+                    commit_message=f"Upload converted QA dataset with {len(alpaca_data)} entries",
+                    readme_file=readme_file
+                )
+
+            if not success:
+                print_error_panel("Hugging Faceアップロードに失敗しました")
+                raise typer.Exit(code=1)
+
+        details = [
+            f"{len(alpaca_data)}個のエントリを変換",
+            f"出力先: {output_file}",
+            f"データセットカード: {readme_file}"
+        ]
+        if upload_hf and hf_repo_name:
+            details.append(f"Hugging Face: {hf_repo_name}")
+
+        print_success_summary("Alpaca形式への変換が完了しました！", details)
+
+    except Exception as e:
+        print_error_panel(f"変換中にエラーが発生しました: {e}")
+        raise typer.Exit(code=1)
+
+
+@app.command()
+def aggregate_logs(
+    output_dir: Annotated[Path, typer.Argument(
+        exists=True, dir_okay=True, readable=True,
+        help="logsフォルダが含まれる出力ディレクトリへのパス。"
+    )]
+):
+    """logsフォルダ内のタイムスタンプ付きXMLファイルを集約してqaフォルダのXMLを生成します."""
+
+    try:
+        logs_dir = output_dir / "logs"
+        qa_dir = output_dir / "qa"
+
+        if not logs_dir.exists():
+            print_error_panel(f"logsフォルダが見つかりません: {logs_dir}")
+            raise typer.Exit(code=1)
+
+        aggregation_table = Table(show_header=False, box=None)
+        aggregation_table.add_column("項目", style="bold cyan")
+        aggregation_table.add_column("パス", style="white")
+        aggregation_table.add_row("📁 logsフォルダ", str(logs_dir))
+        aggregation_table.add_row("🎯 出力先", str(qa_dir))
+
+        console.print(Panel(aggregation_table, title="[bold blue]📄 ログ集約[/bold blue]", border_style="blue"))
+
+        with console.status("🔄 XMLファイルを集約中..."):
+            from easy_dataset_cli.core import aggregate_logs_xml_to_qa
+            aggregate_logs_xml_to_qa(logs_dir, qa_dir)
+
+        print_success_summary("ログ集約が完了しました！", [f"出力先: {qa_dir}"])
+
+    except Exception as e:
+        print_error_panel(f"エラーが発生しました: {e}")
+        raise typer.Exit(code=1)
+
+
+
+
+def print_logo():
+    """おしゃれなロゴを表示"""
+    try:
+        from art import tprint, text2art
+        ART_AVAILABLE = True
+    except ImportError:
+        ART_AVAILABLE = False
+
+    if ART_AVAILABLE:
+        console.print("\n")
+        # シンプルで読みやすいフォントを使用
+        try:
+            logo_text = text2art("Easy Dataset CLI", font="colossal")
+        except:
+            # フォールバックとして標準フォント
+            logo_text = text2art("Easy Dataset CLI")
+
+        # 各行を中央揃えに調整
+        lines = logo_text.strip().split('\n')
+        max_width = max(len(line.rstrip()) for line in lines) if lines else 0
+
+        # パネル内で中央揃えするため、Textオブジェクトを使用
+        logo_panel = Panel(
+            Text(logo_text.strip(), style="bold cyan", justify="center"),
+            title="[bold green]🚀 Easy Dataset CLI[/bold green]",
+            subtitle="[italic]Powered by AI[/italic]",
+            border_style="bright_blue",
+            padding=(1, 2),
+            expand=True  # 横幅一杯に展開
+        )
+        console.print(logo_panel)
+    else:
+        header = Panel(
+            Text("🚀 Easy Dataset CLI\nテキストからQ&Aペアを自動生成", style="bold cyan", justify="center"),
+            border_style="bright_blue",
+            padding=(1, 2),
+            expand=True  # 横幅一杯に展開
+        )
+        console.print(header)
diff --git a/easy_dataset_cli/core.py b/easy_dataset_cli/core.py
index b308563..4764394 100644
--- a/easy_dataset_cli/core.py
+++ b/easy_dataset_cli/core.py
@@ -6,18 +6,25 @@ from .ga_parser import (
     parse_ga_file,
     parse_ga_definitions_from_xml
 )
-from .qa_generator import (
+from .generators import (
     generate_qa_for_chunk_with_ga,
     generate_qa_for_chunk_with_ga_and_fulltext,
     generate_qa_for_chunk_with_ga_and_thinking,
+    generate_qa_for_chunk_with_surrounding_context,
     generate_ga_definitions
 )
-from .text_splitter import split_text
+from .text_splitter import (
+    split_text,
+    get_chunk_with_surrounding_context,
+    create_augmented_chunks
+)
 from .xml_utils import convert_to_xml_by_genre, load_existing_xml_file, aggregate_logs_xml_to_qa
 from .file_utils import (
     create_output_directories,
     save_ga_definitions_by_genre,
-    sanitize_filename
+    sanitize_filename,
+    find_text_files,
+    batch_process_files
 )
 from .alpaca_converter import (
     convert_all_xml_to_alpaca,
@@ -35,10 +42,13 @@ __all__ = [
     'generate_qa_for_chunk_with_ga',
     'generate_qa_for_chunk_with_ga_and_fulltext',
     'generate_qa_for_chunk_with_ga_and_thinking',
+    'generate_qa_for_chunk_with_surrounding_context',
     'generate_ga_definitions',
-    
+
     # テキスト分割
     'split_text',
+    'get_chunk_with_surrounding_context',
+    'create_augmented_chunks',
     
     # XML処理
     'convert_to_xml_by_genre',
@@ -49,6 +59,8 @@ __all__ = [
     'create_output_directories',
     'save_ga_definitions_by_genre',
     'sanitize_filename',
+    'find_text_files',
+    'batch_process_files',
     
     # アルパカ変換・アップロード
     'convert_all_xml_to_alpaca',
diff --git a/easy_dataset_cli/file_utils.py b/easy_dataset_cli/file_utils.py
index f42280a..03bab5c 100644
--- a/easy_dataset_cli/file_utils.py
+++ b/easy_dataset_cli/file_utils.py
@@ -57,3 +57,30 @@ def save_ga_definitions_by_genre(ga_pairs: List[Dict[str, Dict[str, str]]], ga_d
 def sanitize_filename(name: str) -> str:
     """ファイル名として安全な文字列に変換する"""
     return "".join(c for c in name if c.isalnum() or c in (' ', '_', '-')).rstrip()
+
+
+def find_text_files(directory: Path) -> List[Path]:
+    """指定されたディレクトリ内のテキストファイルを再帰的に検索する"""
+    text_extensions = {'.txt', '.md', '.rst', '.org', '.tex', '.text'}
+    text_files = []
+    
+    for file_path in directory.rglob('*'):
+        if file_path.is_file() and file_path.suffix.lower() in text_extensions:
+            text_files.append(file_path)
+    
+    return sorted(text_files)
+
+
+def batch_process_files(files: List[Path], processor_func, *args, **kwargs) -> Dict[str, any]:
+    """複数のファイルをバッチで処理する"""
+    results = {}
+    
+    for file_path in files:
+        try:
+            result = processor_func(file_path, *args, **kwargs)
+            results[str(file_path)] = result
+        except Exception as e:
+            console.print(f"[red]Error processing {file_path}: {e}[/red]")
+            results[str(file_path)] = None
+    
+    return results
diff --git a/easy_dataset_cli/ga_parser.py b/easy_dataset_cli/ga_parser.py
index cdeb17d..06d1205 100644
--- a/easy_dataset_cli/ga_parser.py
+++ b/easy_dataset_cli/ga_parser.py
@@ -6,6 +6,7 @@ from pathlib import Path
 from typing import List, Dict
 import mistune
 from rich.console import Console
+import re
 
 console = Console()
 
@@ -68,9 +69,10 @@ def parse_ga_file(file_path: Path) -> List[Dict[str, Dict[str, str]]]:
             pairs = parse_ga_markdown_fallback(text)
 
     except ET.ParseError as e:
-        console.print(f"[yellow]XML解析エラー: {e}[/yellow]")
-        # XML解析に失敗した場合はマークダウン形式で解析を試行
-        pairs = parse_ga_markdown_fallback(text)
+        console.print(f"[red]XML解析エラー: {e}[/red]")
+        # XML解析に失敗した場合は改良版を試行
+        console.print("[yellow]改良版XML解析を試行中...[/yellow]")
+        pairs = parse_ga_definitions_from_xml_improved(text)
 
     console.print(f"[dim]最終的に解析されたペア数: {len(pairs)}[/dim]")
     return pairs
@@ -92,7 +94,7 @@ def parse_ga_markdown_fallback(text: str) -> List[Dict[str, Dict[str, str]]]:
 
         for node in ast:
             if node['type'] == 'heading':
-                header_text = "".join(child['text'] for child in node['children'])
+                header_text = "".join(child.get('text', '') for child in node['children'])
                 if 'genre' in header_text.lower():
                     current_type = 'genre'
                     genre['title'] = header_text.replace('Genre:', '').strip()
@@ -100,7 +102,7 @@ def parse_ga_markdown_fallback(text: str) -> List[Dict[str, Dict[str, str]]]:
                     current_type = 'audience'
                     audience['title'] = header_text.replace('Audience:', '').strip()
             elif node['type'] == 'paragraph':
-                description = "".join(child['text'] for child in node['children'])
+                description = "".join(child.get('text', '') for child in node['children'])
                 if current_type == 'genre':
                     genre['description'] = description
                 elif current_type == 'audience':
@@ -180,3 +182,75 @@ def parse_ga_definitions_from_xml(xml_content: str) -> List[Dict[str, Dict[str,
         console.print(f"[bold red]予期しないエラー:[/bold red] {e}")
 
     return pairs
+
+
+def parse_ga_definitions_from_xml_improved(xml_content: str) -> List[Dict[str, Dict[str, str]]]:
+    """改良版: 正規表現を使い、コードブロックや不正なXMLを処理できるGA定義解析関数"""
+    pairs = []
+    console.print(f"[dim]XML解析開始: 内容長 {len(xml_content)} 文字[/dim]")
+
+    try:
+        # Step 1: 正規表現で<GADefinitions>ブロックを抽出
+        # re.DOTALLフラグにより、改行文字を含む文字列全体を検索対象にする
+        match = re.search(r"<GADefinitions>.*?</GADefinitions>", xml_content, re.DOTALL)
+
+        if not match:
+            console.print("[yellow]GADefinitionsタグで囲まれたXMLブロックが見つかりませんでした[/yellow]")
+            console.print("[yellow]フォールバック解析を試行中...[/yellow]")
+            return parse_ga_definitions_from_xml(xml_content)
+
+        raw_xml = match.group(0)
+        console.print(f"[dim]正規表現でXMLブロックを抽出完了: {len(raw_xml)} 文字[/dim]")
+
+        # Step 2: XML宣言を追加
+        if not raw_xml.startswith("<?xml"):
+            raw_xml = '<?xml version="1.0" encoding="utf-8"?>\n' + raw_xml
+
+        # Step 3: XML解析を実行
+        root = ET.fromstring(raw_xml)
+        pair_nodes = root.findall('Pair')
+        console.print(f"[dim]見つかったPairノード数: {len(pair_nodes)}[/dim]")
+
+        for i, pair_node in enumerate(pair_nodes):
+            genre_node = pair_node.find('Genre')
+            audience_node = pair_node.find('Audience')
+            
+            if genre_node is not None and audience_node is not None:
+                genre_title_node = genre_node.find('Title')
+                genre_desc_node = genre_node.find('Description')
+                audience_title_node = audience_node.find('Title')
+                audience_desc_node = audience_node.find('Description')
+
+                # 有効なデータが存在するかチェック
+                if all(node is not None and node.text and node.text.strip() for node in [genre_title_node, genre_desc_node, audience_title_node, audience_desc_node]):
+                    genre_title = genre_title_node.text.strip()
+                    audience_title = audience_title_node.text.strip()
+                    pairs.append({
+                        "genre": {
+                            "title": genre_title,
+                            "description": genre_desc_node.text.strip()
+                        },
+                        "audience": {
+                            "title": audience_title,
+                            "description": audience_desc_node.text.strip()
+                        }
+                    })
+                    console.print(f"[green]✓[/green] {genre_title} x {audience_title}")
+                else:
+                    console.print(f"[yellow]⚠[/yellow] Pair {i+1}: 要素が空または無効")
+            else:
+                console.print(f"[yellow]⚠[/yellow] Pair {i+1}: GenreまたはAudienceノードが見つからない")
+
+    except ET.ParseError as parse_error:
+        console.print(f"[bold red]XML解析エラー:[/bold red] {parse_error}")
+        console.print(f"[dim]パース失敗したXML内容: {raw_xml if 'raw_xml' in locals() else 'N/A'}[/dim]")
+        console.print("[yellow]フォールバック解析を試行中...[/yellow]")
+        return parse_ga_definitions_from_xml(xml_content)
+
+    except Exception as e:
+        console.print(f"[bold red]予期しないエラー:[/bold red] {e}")
+        console.print("[yellow]フォールバック解析を試行中...[/yellow]")
+        return parse_ga_definitions_from_xml(xml_content)
+
+    console.print(f"[dim]最終的に解析されたペア数: {len(pairs)}[/dim]")
+    return pairs
diff --git a/easy_dataset_cli/generators/__init__.py b/easy_dataset_cli/generators/__init__.py
new file mode 100644
index 0000000..48d99df
--- /dev/null
+++ b/easy_dataset_cli/generators/__init__.py
@@ -0,0 +1,20 @@
+#!/usr/bin/env python3
+"""
+Q&A生成パッケージ
+"""
+
+from .qa_generator import generate_qa_for_chunk_with_ga
+from .qa_generator_fulltext import generate_qa_for_chunk_with_ga_and_fulltext
+from .qa_generator_thinking import (
+    generate_qa_for_chunk_with_ga_and_thinking,
+    generate_qa_for_chunk_with_surrounding_context
+)
+from .ga_generator import generate_ga_definitions
+
+__all__ = [
+    'generate_qa_for_chunk_with_ga',
+    'generate_qa_for_chunk_with_ga_and_fulltext',
+    'generate_qa_for_chunk_with_ga_and_thinking',
+    'generate_qa_for_chunk_with_surrounding_context',
+    'generate_ga_definitions'
+]
diff --git a/easy_dataset_cli/generators/ga_generator.py b/easy_dataset_cli/generators/ga_generator.py
new file mode 100644
index 0000000..740e26f
--- /dev/null
+++ b/easy_dataset_cli/generators/ga_generator.py
@@ -0,0 +1,60 @@
+#!/usr/bin/env python3
+"""
+GA定義生成機能
+"""
+
+import os
+from pathlib import Path
+from openai import OpenAI
+from rich.console import Console
+from dotenv import load_dotenv
+import traceback
+import json
+
+# .envファイルを読み込む
+load_dotenv()
+
+console = Console()
+
+
+def generate_ga_definitions(text_content: str, model: str, num_ga_pairs: int = None, max_context_length: int = 8000) -> str:
+    """OpenAIクライアントを使い、元の文章からGAペア定義のXMLを生成する"""
+    # LLMに渡すテキストは長すぎるとコストや性能に影響するため、先頭部分に限定する
+    context = text_content[:max_context_length]
+    console.print(f"[dim]コンテキスト長: {len(context)} 文字 (上限: {max_context_length})[/dim]")
+
+    from ..prompts import get_ga_definition_generation_prompt
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
+    # APIキーの確認
+    api_key = os.getenv("OPENAI_API_KEY", "")
+    if not api_key:
+        console.print("[bold red]OPENAI_API_KEYが設定されていません！[/bold red]")
+        raise ValueError("OPENAI_API_KEYが必要です")
+
+    # OpenAIクライアントの初期化
+    client = OpenAI(
+        base_url=os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1"),
+        api_key=api_key,
+    )
+
+    try:
+        response = client.chat.completions.create(
+            model=model,
+            messages=messages
+        )
+        xml_content = response.choices[0].message.content
+        console.print(f"[dim]LLMレスポンス長: {len(xml_content)} 文字[/dim]")
+        return xml_content
+    except Exception as error:
+        console.print(f"[bold red]GA定義の生成中にエラーが発生しました:[/bold red] {error}")
+        raise
diff --git a/easy_dataset_cli/generators/qa_generator.py b/easy_dataset_cli/generators/qa_generator.py
new file mode 100644
index 0000000..99293ac
--- /dev/null
+++ b/easy_dataset_cli/generators/qa_generator.py
@@ -0,0 +1,547 @@
+#!/usr/bin/env python3
+"""
+基本的なQ&A生成機能
+"""
+
+import os
+import xml.etree.ElementTree as ET
+from xml.dom import minidom
+from pathlib import Path
+from typing import List, Dict
+from openai import OpenAI
+from rich.console import Console
+from dotenv import load_dotenv
+import traceback
+import json
+from datetime import datetime
+
+from ..prompts import get_qa_generation_prompt
+from ..xml_utils import parse_qa_from_text_fallback
+
+# .envファイルを読み込む
+load_dotenv()
+
+console = Console()
+
+
+def generate_qa_for_chunk_with_ga(
+    chunk: str,
+    model: str,
+    ga_pair: Dict[str, Dict[str, str]],
+    logs_dir: Path = None,
+    num_qa_pairs: int = None
+) -> List[Dict[str, str]]:
+    """OpenAIクライアントを使い、1つのチャンクと1つのGAペアからQ&Aペアのリストを生成する"""
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
+        {"role": "system", "content": "あなたは、XML形式で厳密に出力する優秀なアシスタントです。通常のXMLの特殊文字（&, \", '）は適切にエスケープしてください。ただし、<Question>、<Answer>、<think>タグはそのまま使用してください。改行は含めずに出力してください。"},
+        {"role": "user", "content": prompt}
+    ]
+
+    # OpenAIクライアントの初期化
+    client = OpenAI(
+        base_url=os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1"),
+        api_key=os.getenv("OPENAI_API_KEY"),
+    )
+
+    # タイムスタンプ付きログファイル名を生成
+    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
+    genre_safe = "".join(c for c in ga_pair['genre']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
+    audience_safe = "".join(c for c in ga_pair['audience']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
+
+    try:
+        # リクエストログを保存
+        if logs_dir:
+            request_log = {
+                "timestamp": timestamp,
+                "model": model,
+                "genre": ga_pair['genre']['title'],
+                "audience": ga_pair['audience']['title'],
+                "prompt_length": len(prompt),
+                "messages": messages
+            }
+            request_filename = f"request_{genre_safe}_{audience_safe}_{timestamp}.json"
+            request_file_path = logs_dir / request_filename
+            with open(request_file_path, 'w', encoding='utf-8') as f:
+                json.dump(request_log, f, ensure_ascii=False, indent=2)
+            console.print(f"[dim]リクエストログを保存: {request_filename}[/dim]")
+
+            # プロンプトをマークダウンファイルとして保存
+            prompt_filename = f"prompt_{genre_safe}_{audience_safe}_{timestamp}.md"
+            prompt_file_path = logs_dir / prompt_filename
+            prompt_content = f"""# QA生成プロンプト
+
+**タイムスタンプ:** {timestamp}  
+**モデル:** {model}  
+**ジャンル:** {ga_pair['genre']['title']}  
+**オーディエンス:** {ga_pair['audience']['title']}  
+**プロンプト長:** {len(prompt)} 文字
+
+---
+
+## システムメッセージ
+
+{messages[0]['content']}
+
+---
+
+## ユーザープロンプト
+
+{prompt}
+"""
+            prompt_file_path.write_text(prompt_content, encoding='utf-8')
+            console.print(f"[dim]プロンプトファイルを保存: {prompt_filename}[/dim]")
+
+        # リクエスト送信時刻を記録
+        request_start = datetime.now()
+        
+        response = client.chat.completions.create(
+            model=model,
+            messages=messages
+        )
+        
+        # レスポンス受信時刻を記録
+        request_end = datetime.now()
+        processing_time = (request_end - request_start).total_seconds()
+        
+        xml_content = response.choices[0].message.content
+
+        # レスポンスログを保存（詳細情報付き）
+        if logs_dir:
+            response_log = {
+                "metadata": {
+                    "timestamp": timestamp,
+                    "request_start": request_start.isoformat(),
+                    "request_end": request_end.isoformat(),
+                    "processing_time_seconds": processing_time,
+                    "model": model
+                },
+                "generation_context": {
+                    "genre": {
+                        "title": ga_pair['genre']['title'],
+                        "description": ga_pair['genre']['description'][:100] + "..." if len(ga_pair['genre']['description']) > 100 else ga_pair['genre']['description']
+                    },
+                    "audience": {
+                        "title": ga_pair['audience']['title'],
+                        "description": ga_pair['audience']['description'][:100] + "..." if len(ga_pair['audience']['description']) > 100 else ga_pair['audience']['description']
+                    },
+                    "chunk_length": len(chunk),
+                    "prompt_length": len(prompt)
+                },
+                "api_response": {
+                    "response_length": len(xml_content),
+                    "response_content": xml_content
+                }
+            }
+            response_filename = f"response_{genre_safe}_{audience_safe}_{timestamp}.json"
+            response_file_path = logs_dir / response_filename
+            with open(response_file_path, 'w', encoding='utf-8') as f:
+                json.dump(response_log, f, ensure_ascii=False, indent=2)
+            console.print(f"[dim]レスポンスログを保存: {response_filename} (処理時間: {processing_time:.2f}s)[/dim]")
+
+        # rawレスポンスを保存（オプション）
+        if logs_dir:
+            raw_filename = f"qa_raw_{genre_safe}_{audience_safe}_{timestamp}.md"
+            raw_file_path = logs_dir / raw_filename
+            raw_file_path.write_text(xml_content, encoding="utf-8")
+
+        qa_pairs = _parse_qa_response(xml_content, logs_dir, genre_safe, audience_safe, timestamp)
+
+        # 生成したQAを保存
+        if qa_pairs and logs_dir:
+            qa_filename = f"qa_pairs_{genre_safe}_{audience_safe}_{timestamp}.xml"
+            _save_qa_pairs_to_xml(qa_pairs, logs_dir, qa_filename)
+
+        # 実行サマリーを保存
+        if logs_dir:
+            _save_execution_summary(logs_dir, timestamp, genre_safe, audience_safe, {
+                "processing_time": processing_time,
+                "qa_count": len(qa_pairs),
+                "success": True,
+                "chunk_length": len(chunk),
+                "prompt_length": len(prompt),
+                "response_length": len(xml_content)
+            })
+
+        return qa_pairs
+
+    except Exception as general_error:
+        # 詳細なエラー情報を表示
+        console.print(f"[bold red]チャンクとGAペアからのQ&A生成中にエラーが発生しました:[/bold red]")
+        console.print(f"[bold red]エラータイプ:[/bold red] {type(general_error).__name__}")
+        console.print(f"[bold red]エラーメッセージ:[/bold red] {str(general_error)}")
+        console.print(f"[bold red]トレースバック:[/bold red]")
+        console.print(traceback.format_exc())
+        console.print(f"[dim]Genre: {ga_pair['genre']['title']}, Audience: {ga_pair['audience']['title']}[/dim]")
+
+        # エラーログを保存
+        if logs_dir:
+            error_log = {
+                "timestamp": timestamp,
+                "model": model,
+                "genre": ga_pair['genre']['title'],
+                "audience": ga_pair['audience']['title'],
+                "error_type": type(general_error).__name__,
+                "error_message": str(general_error),
+                "traceback": traceback.format_exc()
+            }
+            error_filename = f"error_{genre_safe}_{audience_safe}_{timestamp}.json"
+            error_file_path = logs_dir / error_filename
+            with open(error_file_path, 'w', encoding='utf-8') as f:
+                json.dump(error_log, f, ensure_ascii=False, indent=2)
+            console.print(f"[dim]エラーログを保存: {error_filename}[/dim]")
+
+        # エラー時もサマリーを保存
+        if logs_dir:
+            _save_execution_summary(logs_dir, timestamp, genre_safe, audience_safe, {
+                "processing_time": 0,
+                "qa_count": 0,
+                "success": False,
+                "error_type": type(general_error).__name__,
+                "error_message": str(general_error),
+                "chunk_length": len(chunk) if chunk else 0,
+                "prompt_length": len(prompt) if prompt else 0,
+                "response_length": 0
+            })
+
+        return []
+
+
+def _parse_qa_response(xml_content: str, logs_dir: Path = None, genre_safe: str = None, audience_safe: str = None, timestamp: str = None) -> List[Dict[str, str]]:
+    """Q&A生成レスポンスのXMLを解析する（共通処理）"""
+    qa_pairs = []
+
+    # LLMからの出力の前処理：不要なテキストを除去
+    cleaned_content = _clean_llm_response(xml_content)
+
+    # XML部分のみを抽出 - 優先的に<QAPairs>タグを探す
+    xml_start = cleaned_content.find("<QAPairs>")
+    xml_end = cleaned_content.rfind("</QAPairs>")
+
+    # <QAPairs>タグが見つからない場合は<Pair>タグで抽出を試行
+    if xml_start == -1 or xml_end == -1:
+        console.print("[yellow]<QAPairs>タグが見つからないため、<Pair>タグで抽出を試行します...[/yellow]")
+        xml_start = cleaned_content.find("<Pair>")
+        xml_end = cleaned_content.rfind("</Pair>")
+
+        # <Pair>タグで囲まれた部分を抽出
+        if xml_start != -1 and xml_end != -1:
+            # すべての<Pair>...</Pair>を抽出
+            import re
+            pair_pattern = r'<Pair>.*?</Pair>'
+            pair_matches = re.findall(pair_pattern, cleaned_content, re.DOTALL)
+
+            for pair_match in pair_matches:
+                # 各PairからQuestionとAnswerを抽出
+                question_match = re.search(r'<Question>(.*?)</Question>', pair_match, re.DOTALL)
+                answer_match = re.search(r'<Answer>(.*?)</Answer>', pair_match, re.DOTALL)
+
+                if question_match and answer_match:
+                    qa_pairs.append({
+                        "question": _decode_xml_entities(question_match.group(1).strip()),
+                        "answer": _decode_xml_entities(answer_match.group(1).strip())
+                    })
+
+            if qa_pairs:
+                console.print(f"[green]✓[/green] <Pair>タグから{len(qa_pairs)}件のQ&Aを抽出しました")
+                return qa_pairs
+
+    if xml_start != -1 and xml_end != -1:
+        clean_xml = cleaned_content[xml_start: xml_end + len("</QAPairs>")]
+
+        # XML解析用のログを保存
+        if logs_dir and genre_safe and audience_safe and timestamp:
+            xml_debug_log = {
+                "timestamp": timestamp,
+                "original_xml_content": xml_content[:500],
+                "cleaned_xml_content": cleaned_content[:500],
+                "final_xml_content": clean_xml,
+                "xml_length": len(clean_xml)
+            }
+            xml_debug_filename = f"xml_debug_{genre_safe}_{audience_safe}_{timestamp}.json"
+            xml_debug_file_path = logs_dir / xml_debug_filename
+            with open(xml_debug_file_path, 'w', encoding='utf-8') as f:
+                json.dump(xml_debug_log, f, ensure_ascii=False, indent=2)
+
+        try:
+            root = ET.fromstring(clean_xml)
+
+            for pair_node in root.findall('Pair'):
+                question_node = pair_node.find('Question')
+                answer_node = pair_node.find('Answer')
+
+                if question_node is not None and answer_node is not None:
+                    question_text = question_node.text or ""
+
+                    # <Answer>要素内の内容を適切に取得
+                    if len(answer_node) > 0:
+                        # サブエレメントがある場合（<think>タグなど）
+                        answer_parts = []
+
+                        # Answer要素の直接のテキスト（<think>より前）
+                        if answer_node.text:
+                            answer_parts.append(answer_node.text.strip())
+
+                        # 各サブエレメントのtail（サブエレメントの後のテキスト）
+                        for child in answer_node:
+                            if child.tag == 'think':
+                                # <think>タグの内容を取得
+                                think_content = child.text or ""
+                                answer_parts.append(f"<think>{think_content}</think>")
+
+                            # サブエレメントの後のテキスト
+                            if child.tail:
+                                answer_parts.append(child.tail.strip())
+
+                        answer_text = "".join(answer_parts)
+                    else:
+                        # サブエレメントがない場合は通常のテキスト
+                        answer_text = answer_node.text or ""
+
+                    # XMLエンティティデコード
+                    question_text = _decode_xml_entities(question_text)
+                    answer_text = _decode_xml_entities(answer_text)
+
+                    qa_pairs.append({
+                        "question": question_text,
+                        "answer": answer_text
+                    })
+
+        except ET.ParseError as parse_error:
+            # XMLパースに失敗した場合、手動でテキスト解析
+            console.print("[yellow]XMLパースエラー、自動解析を試行中...[/yellow]")
+            console.print(f"[dim]パースエラー詳細: {str(parse_error)}[/dim]")
+
+            # エラーログを保存
+            if logs_dir and genre_safe and audience_safe and timestamp:
+                parse_error_log = {
+                    "timestamp": timestamp,
+                    "error_type": "XML_ParseError",
+                    "error_message": str(parse_error),
+                    "xml_content": clean_xml
+                }
+                parse_error_filename = f"xml_parse_error_{genre_safe}_{audience_safe}_{timestamp}.json"
+                parse_error_file_path = logs_dir / parse_error_filename
+                with open(parse_error_file_path, 'w', encoding='utf-8') as f:
+                    json.dump(parse_error_log, f, ensure_ascii=False, indent=2)
+
+            # 自動解析を試行
+            qa_pairs = parse_qa_from_text_fallback(clean_xml)
+
+            # 自動解析でも失敗した場合のフォールバック
+            if not qa_pairs:
+                console.print("[yellow]自動解析も失敗したため、テキストから直接Q&Aを抽出します...[/yellow]")
+                qa_pairs = _extract_qa_from_fallback_text(cleaned_content)
+
+    if not qa_pairs:
+        console.print(f"[bold red]LLMが生成したXMLの解析に失敗しました[/bold red]")
+        console.print(f"[dim]受信したテキスト: {cleaned_content[:500]}...[/dim]")
+
+        # 解析失敗のログを保存
+        if logs_dir and genre_safe and audience_safe and timestamp:
+            failure_log = {
+                "timestamp": timestamp,
+                "failure_reason": "XML解析失敗",
+                "original_content": xml_content[:1000],
+                "cleaned_content": cleaned_content[:1000]
+            }
+            failure_filename = f"xml_parse_failure_{genre_safe}_{audience_safe}_{timestamp}.json"
+            failure_file_path = logs_dir / failure_filename
+            with open(failure_file_path, 'w', encoding='utf-8') as f:
+                json.dump(failure_log, f, ensure_ascii=False, indent=2)
+
+    return qa_pairs
+
+
+def _clean_llm_response(response: str) -> str:
+    """LLMからのレスポンスをクリーンアップする"""
+    import re
+
+    # 不要なテキストを除去
+    cleaned = response
+
+    # \```xml ... \``` のようなコードブロックを除去
+    cleaned = re.sub(r'\```xml\s*|\s*\```', '', cleaned, flags=re.IGNORECASE)
+
+    # \``` ... \``` のようなコードブロックを除去
+    cleaned = re.sub(r'\```\s*|\s*\```', '', cleaned)
+
+    # <xml> ... </xml> のようなタグを除去
+    cleaned = re.sub(r'<xml>\s*|\s*</xml>', '', cleaned, flags=re.IGNORECASE)
+
+    # 不要な空白や改行を整理
+    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
+
+    return cleaned
+
+
+def _extract_qa_from_fallback_text(text: str) -> List[Dict[str, str]]:
+    """テキストから直接Q&Aを抽出するフォールバック関数"""
+    qa_pairs = []
+
+    try:
+        # <Question>と<Answer>タグで分割
+        import re
+
+        # Questionタグを検索
+        question_pattern = r'<Question>(.*?)</Question>'
+        answer_pattern = r'<Answer>(.*?)</Answer>'
+
+        questions = re.findall(question_pattern, text, re.DOTALL)
+        answers = re.findall(answer_pattern, text, re.DOTALL)
+
+        # 同じ数の質問と回答がある場合のみペアを作成
+        min_count = min(len(questions), len(answers))
+        for i in range(min_count):
+            qa_pairs.append({
+                "question": _decode_xml_entities(questions[i].strip()),
+                "answer": _decode_xml_entities(answers[i].strip())
+            })
+
+    except Exception as e:
+        console.print(f"[red]フォールバック解析も失敗:[/red] {e}")
+
+    return qa_pairs
+
+
+def _decode_xml_entities(text: str) -> str:
+    """XMLエンティティをデコードする（シンプル版）"""
+    import html
+    if text:
+        return html.unescape(text)
+    return text
+
+
+def _save_qa_pairs_to_xml(qa_pairs: List[Dict[str, str]], logs_dir: Path, qa_filename: str) -> None:
+    """Q&Aペアをきれいに整形されたXMLファイルとして保存（サブエレメント方式）"""
+    if not qa_pairs or not logs_dir:
+        return
+
+    qa_file_path = logs_dir / qa_filename
+
+    # ElementTreeで構造化生成
+    root = ET.Element("QAPairs")
+    for qa in qa_pairs:
+        pair_elem = ET.SubElement(root, "Pair")
+        question_elem = ET.SubElement(pair_elem, "Question")
+        question_elem.text = qa["question"]
+
+        answer_elem = ET.SubElement(pair_elem, "Answer")
+
+        # 回答内容を解析
+        parsed_answer = _parse_answer_with_think(qa["answer"])
+
+        if parsed_answer["has_think"]:
+            # <think>をサブエレメントとして追加
+            think_elem = ET.SubElement(answer_elem, "think")
+            think_elem.text = parsed_answer["think_content"]
+            think_elem.tail = parsed_answer["answer_content"]
+        else:
+            # 通常の回答
+            answer_elem.text = parsed_answer["answer_content"]
+
+    # 整形して保存
+    rough_string = ET.tostring(root, 'utf-8')
+    reparsed = minidom.parseString(rough_string)
+    pretty_xml = reparsed.toprettyxml(indent="  ")
+
+    qa_file_path.write_text(pretty_xml, encoding='utf-8')
+    console.print(f"[green]✓[/green] QAペアを保存: {qa_filename} ({len(qa_pairs)}件)")
+
+
+def _parse_answer_with_think(answer_text: str) -> Dict[str, str]:
+    """<think>タグを含む回答をパースして分離"""
+    import re
+
+    # <think>...</think>タグを検索
+    think_match = re.search(r'<think>(.*?)</think>', answer_text, re.DOTALL)
+
+    if think_match:
+        think_content = think_match.group(1).strip()
+        # <think>タグ以降の回答テキストを取得
+        answer_content = answer_text[think_match.end():].strip()
+        return {
+            "has_think": True,
+            "think_content": think_content,
+            "answer_content": answer_content
+        }
+    else:
+        return {
+            "has_think": False,
+            "think_content": "",
+            "answer_content": answer_text
+        }
+
+
+def _save_execution_summary(logs_dir: Path, timestamp: str, genre_safe: str, audience_safe: str, summary_data: Dict) -> None:
+    """実行サマリーをマークダウンとJSONで保存"""
+    if not logs_dir:
+        return
+    
+    # JSONサマリー
+    json_summary = {
+        "timestamp": timestamp,
+        "genre": genre_safe,
+        "audience": audience_safe,
+        "execution_summary": summary_data
+    }
+    
+    json_filename = f"summary_{genre_safe}_{audience_safe}_{timestamp}.json"
+    json_file_path = logs_dir / json_filename
+    with open(json_file_path, 'w', encoding='utf-8') as f:
+        json.dump(json_summary, f, ensure_ascii=False, indent=2)
+    
+    # マークダウンサマリー
+    md_filename = f"summary_{genre_safe}_{audience_safe}_{timestamp}.md"
+    md_file_path = logs_dir / md_filename
+    
+    status_emoji = "✅" if summary_data.get("success", False) else "❌"
+    
+    md_content = f"""# QA生成実行サマリー {status_emoji}
+
+**タイムスタンプ:** {timestamp}  
+**ジャンル:** {genre_safe.replace('_', ' ')}  
+**オーディエンス:** {audience_safe.replace('_', ' ')}  
+**ステータス:** {'成功' if summary_data.get('success', False) else '失敗'}
+
+## 📊 実行統計
+
+| 項目 | 値 |
+|------|-----|
+| 処理時間 | {summary_data.get('processing_time', 0):.2f}秒 |
+| 生成されたQA数 | {summary_data.get('qa_count', 0)}件 |
+| チャンク長 | {summary_data.get('chunk_length', 0):,}文字 |
+| プロンプト長 | {summary_data.get('prompt_length', 0):,}文字 |
+| レスポンス長 | {summary_data.get('response_length', 0):,}文字 |
+
+## 📁 関連ログファイル
+
+- `prompt_{genre_safe}_{audience_safe}_{timestamp}.md` - 使用したプロンプト
+- `request_{genre_safe}_{audience_safe}_{timestamp}.json` - リクエストログ  
+- `response_{genre_safe}_{audience_safe}_{timestamp}.json` - レスポンスログ
+- `qa_raw_{genre_safe}_{audience_safe}_{timestamp}.md` - 生RAWレスポンス
+"""
+
+    if summary_data.get("success", False):
+        md_content += f"- `qa_pairs_{genre_safe}_{audience_safe}_{timestamp}.xml` - 生成されたQAペア\n"
+    else:
+        md_content += f"""
+## ❌ エラー詳細
+
+**エラータイプ:** {summary_data.get('error_type', 'Unknown')}  
+**エラーメッセージ:** {summary_data.get('error_message', 'No message')}
+
+- `error_{genre_safe}_{audience_safe}_{timestamp}.json` - エラーログ
+"""
+    
+    md_file_path.write_text(md_content, encoding='utf-8')
+    console.print(f"[dim]実行サマリーを保存: {md_filename}[/dim]")
diff --git a/easy_dataset_cli/generators/qa_generator_fulltext.py b/easy_dataset_cli/generators/qa_generator_fulltext.py
new file mode 100644
index 0000000..ebee785
--- /dev/null
+++ b/easy_dataset_cli/generators/qa_generator_fulltext.py
@@ -0,0 +1,437 @@
+#!/usr/bin/env python3
+"""
+全文対応Q&A生成機能
+"""
+
+import os
+import xml.etree.ElementTree as ET
+from xml.dom import minidom
+from pathlib import Path
+from typing import List, Dict
+from openai import OpenAI
+from rich.console import Console
+from dotenv import load_dotenv
+import traceback
+import json
+from datetime import datetime
+
+from ..prompts import get_qa_generation_with_fulltext_prompt
+from ..xml_utils import parse_qa_from_text_fallback
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
+    """OpenAIクライアントを使い、1つのチャンクと全文、1つのGAペアからQ&Aペアのリストを生成する"""
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
+        {"role": "system", "content": "あなたは、XML形式で厳密に出力する優秀なアシスタントです。通常のXMLの特殊文字（&, \", '）は適切にエスケープしてください。ただし、<Question>、<Answer>、<think>タグはそのまま使用してください。改行は含めずに出力してください。"},
+        {"role": "user", "content": prompt}
+    ]
+
+    # OpenAIクライアントの初期化
+    client = OpenAI(
+        base_url=os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1"),
+        api_key=os.getenv("OPENAI_API_KEY"),
+    )
+
+    # タイムスタンプ付きログファイル名を生成
+    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
+    genre_safe = "".join(c for c in ga_pair['genre']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
+    audience_safe = "".join(c for c in ga_pair['audience']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
+
+    try:
+        # リクエストログを保存
+        if logs_dir:
+            request_log = {
+                "timestamp": timestamp,
+                "model": model,
+                "genre": ga_pair['genre']['title'],
+                "audience": ga_pair['audience']['title'],
+                "prompt_length": len(prompt),
+                "messages": messages
+            }
+            request_filename = f"request_{genre_safe}_{audience_safe}_{timestamp}.json"
+            request_file_path = logs_dir / request_filename
+            with open(request_file_path, 'w', encoding='utf-8') as f:
+                json.dump(request_log, f, ensure_ascii=False, indent=2)
+            console.print(f"[dim]リクエストログを保存: {request_filename}[/dim]")
+
+            # プロンプトをマークダウンファイルとして保存
+            prompt_filename = f"prompt_fulltext_{genre_safe}_{audience_safe}_{timestamp}.md"
+            prompt_file_path = logs_dir / prompt_filename
+            prompt_content = f"""# QA生成プロンプト (全文付き)
+
+**タイムスタンプ:** {timestamp}  
+**モデル:** {model}  
+**ジャンル:** {ga_pair['genre']['title']}  
+**オーディエンス:** {ga_pair['audience']['title']}  
+**プロンプト長:** {len(prompt)} 文字
+
+---
+
+## システムメッセージ
+
+{messages[0]['content']}
+
+---
+
+## ユーザープロンプト
+
+{prompt}
+"""
+            prompt_file_path.write_text(prompt_content, encoding='utf-8')
+            console.print(f"[dim]プロンプトファイルを保存: {prompt_filename}[/dim]")
+
+        response = client.chat.completions.create(
+            model=model,
+            messages=messages
+        )
+        xml_content = response.choices[0].message.content
+
+        # レスポンスログを保存
+        if logs_dir:
+            response_log = {
+                "timestamp": timestamp,
+                "model": model,
+                "genre": ga_pair['genre']['title'],
+                "audience": ga_pair['audience']['title'],
+                "response_length": len(xml_content),
+                "response_content": xml_content
+            }
+            response_filename = f"response_{genre_safe}_{audience_safe}_{timestamp}.json"
+            response_file_path = logs_dir / response_filename
+            with open(response_file_path, 'w', encoding='utf-8') as f:
+                json.dump(response_log, f, ensure_ascii=False, indent=2)
+            console.print(f"[dim]レスポンスログを保存: {response_filename}[/dim]")
+
+        # rawレスポンスを保存（オプション）
+        if logs_dir:
+            raw_filename = f"qa_fulltext_raw_{genre_safe}_{audience_safe}_{timestamp}.md"
+            raw_file_path = logs_dir / raw_filename
+            raw_file_path.write_text(xml_content, encoding="utf-8")
+
+        qa_pairs = _parse_qa_response(xml_content, logs_dir, genre_safe, audience_safe, timestamp)
+
+        # 生成したQAを保存
+        if qa_pairs and logs_dir:
+            qa_filename = f"qa_pairs_{genre_safe}_{audience_safe}_{timestamp}.xml"
+            qa_file_path = logs_dir / qa_filename
+
+            _save_qa_pairs_to_xml(qa_pairs, logs_dir, qa_filename)
+
+        return qa_pairs
+
+    except Exception as general_error:
+        # 詳細なエラー情報を表示
+        console.print(f"[bold red]チャンクとGAペアからのQ&A生成中にエラーが発生しました:[/bold red]")
+        console.print(f"[bold red]エラータイプ:[/bold red] {type(general_error).__name__}")
+        console.print(f"[bold red]エラーメッセージ:[/bold red] {str(general_error)}")
+        console.print(f"[bold red]トレースバック:[/bold red]")
+        console.print(traceback.format_exc())
+        console.print(f"[dim]Genre: {ga_pair['genre']['title']}, Audience: {ga_pair['audience']['title']}[/dim]")
+
+        # エラーログを保存
+        if logs_dir:
+            error_log = {
+                "timestamp": timestamp,
+                "model": model,
+                "genre": ga_pair['genre']['title'],
+                "audience": ga_pair['audience']['title'],
+                "error_type": type(general_error).__name__,
+                "error_message": str(general_error),
+                "traceback": traceback.format_exc()
+            }
+            error_filename = f"error_{genre_safe}_{audience_safe}_{timestamp}.json"
+            error_file_path = logs_dir / error_filename
+            with open(error_file_path, 'w', encoding='utf-8') as f:
+                json.dump(error_log, f, ensure_ascii=False, indent=2)
+            console.print(f"[dim]エラーログを保存: {error_filename}[/dim]")
+
+        return []
+
+
+def _parse_qa_response(xml_content: str, logs_dir: Path = None, genre_safe: str = None, audience_safe: str = None, timestamp: str = None) -> List[Dict[str, str]]:
+    """Q&A生成レスポンスのXMLを解析する（共通処理）"""
+    qa_pairs = []
+
+    # LLMからの出力の前処理：不要なテキストを除去
+    cleaned_content = _clean_llm_response(xml_content)
+
+    # XML部分のみを抽出 - 優先的に<QAPairs>タグを探す
+    xml_start = cleaned_content.find("<QAPairs>")
+    xml_end = cleaned_content.rfind("</QAPairs>")
+
+    # <QAPairs>タグが見つからない場合は<Pair>タグで抽出を試行
+    if xml_start == -1 or xml_end == -1:
+        console.print("[yellow]<QAPairs>タグが見つからないため、<Pair>タグで抽出を試行します...[/yellow]")
+        xml_start = cleaned_content.find("<Pair>")
+        xml_end = cleaned_content.rfind("</Pair>")
+
+        # <Pair>タグで囲まれた部分を抽出
+        if xml_start != -1 and xml_end != -1:
+            # すべての<Pair>...</Pair>を抽出
+            import re
+            pair_pattern = r'<Pair>.*?</Pair>'
+            pair_matches = re.findall(pair_pattern, cleaned_content, re.DOTALL)
+
+            for pair_match in pair_matches:
+                # 各PairからQuestionとAnswerを抽出
+                question_match = re.search(r'<Question>(.*?)</Question>', pair_match, re.DOTALL)
+                answer_match = re.search(r'<Answer>(.*?)</Answer>', pair_match, re.DOTALL)
+
+                if question_match and answer_match:
+                    qa_pairs.append({
+                        "question": _decode_xml_entities(question_match.group(1).strip()),
+                        "answer": _decode_xml_entities(answer_match.group(1).strip())
+                    })
+
+            if qa_pairs:
+                console.print(f"[green]✓[/green] <Pair>タグから{len(qa_pairs)}件のQ&Aを抽出しました")
+                return qa_pairs
+
+    if xml_start != -1 and xml_end != -1:
+        clean_xml = cleaned_content[xml_start: xml_end + len("</QAPairs>")]
+
+        # XML解析用のログを保存
+        if logs_dir and genre_safe and audience_safe and timestamp:
+            xml_debug_log = {
+                "timestamp": timestamp,
+                "original_xml_content": xml_content[:500],
+                "cleaned_xml_content": cleaned_content[:500],
+                "final_xml_content": clean_xml,
+                "xml_length": len(clean_xml)
+            }
+            xml_debug_filename = f"xml_debug_{genre_safe}_{audience_safe}_{timestamp}.json"
+            xml_debug_file_path = logs_dir / xml_debug_filename
+            with open(xml_debug_file_path, 'w', encoding='utf-8') as f:
+                json.dump(xml_debug_log, f, ensure_ascii=False, indent=2)
+
+        try:
+            root = ET.fromstring(clean_xml)
+
+            for pair_node in root.findall('Pair'):
+                question_node = pair_node.find('Question')
+                answer_node = pair_node.find('Answer')
+
+                if question_node is not None and answer_node is not None:
+                    question_text = question_node.text or ""
+
+                    # <Answer>要素内の内容を適切に取得
+                    if len(answer_node) > 0:
+                        # サブエレメントがある場合（<think>タグなど）
+                        answer_parts = []
+
+                        # Answer要素の直接のテキスト（<think>より前）
+                        if answer_node.text:
+                            answer_parts.append(answer_node.text.strip())
+
+                        # 各サブエレメントのtail（サブエレメントの後のテキスト）
+                        for child in answer_node:
+                            if child.tag == 'think':
+                                # <think>タグの内容を取得
+                                think_content = child.text or ""
+                                answer_parts.append(f"<think>{think_content}</think>")
+
+                            # サブエレメントの後のテキスト
+                            if child.tail:
+                                answer_parts.append(child.tail.strip())
+
+                        answer_text = "".join(answer_parts)
+                    else:
+                        # サブエレメントがない場合は通常のテキスト
+                        answer_text = answer_node.text or ""
+
+                    # XMLエンティティデコード
+                    question_text = _decode_xml_entities(question_text)
+                    answer_text = _decode_xml_entities(answer_text)
+
+                    qa_pairs.append({
+                        "question": question_text,
+                        "answer": answer_text
+                    })
+
+        except ET.ParseError as parse_error:
+            # XMLパースに失敗した場合、手動でテキスト解析
+            console.print("[yellow]XMLパースエラー、自動解析を試行中...[/yellow]")
+            console.print(f"[dim]パースエラー詳細: {str(parse_error)}[/dim]")
+
+            # エラーログを保存
+            if logs_dir and genre_safe and audience_safe and timestamp:
+                parse_error_log = {
+                    "timestamp": timestamp,
+                    "error_type": "XML_ParseError",
+                    "error_message": str(parse_error),
+                    "xml_content": clean_xml
+                }
+                parse_error_filename = f"xml_parse_error_{genre_safe}_{audience_safe}_{timestamp}.json"
+                parse_error_file_path = logs_dir / parse_error_filename
+                with open(parse_error_file_path, 'w', encoding='utf-8') as f:
+                    json.dump(parse_error_log, f, ensure_ascii=False, indent=2)
+
+            # 自動解析を試行
+            qa_pairs = parse_qa_from_text_fallback(clean_xml)
+
+            # 自動解析でも失敗した場合のフォールバック
+            if not qa_pairs:
+                console.print("[yellow]自動解析も失敗したため、テキストから直接Q&Aを抽出します...[/yellow]")
+                qa_pairs = _extract_qa_from_fallback_text(cleaned_content)
+
+    if not qa_pairs:
+        console.print(f"[bold red]LLMが生成したXMLの解析に失敗しました[/bold red]")
+        console.print(f"[dim]受信したテキスト: {cleaned_content[:500]}...[/dim]")
+
+        # 解析失敗のログを保存
+        if logs_dir and genre_safe and audience_safe and timestamp:
+            failure_log = {
+                "timestamp": timestamp,
+                "failure_reason": "XML解析失敗",
+                "original_content": xml_content[:1000],
+                "cleaned_content": cleaned_content[:1000]
+            }
+            failure_filename = f"xml_parse_failure_{genre_safe}_{audience_safe}_{timestamp}.json"
+            failure_file_path = logs_dir / failure_filename
+            with open(failure_file_path, 'w', encoding='utf-8') as f:
+                json.dump(failure_log, f, ensure_ascii=False, indent=2)
+
+    return qa_pairs
+
+
+def _clean_llm_response(response: str) -> str:
+    """LLMからのレスポンスをクリーンアップする"""
+    import re
+
+    # 不要なテキストを除去
+    cleaned = response
+
+    # \```xml ... \``` のようなコードブロックを除去
+    cleaned = re.sub(r'\```xml\s*|\s*\```', '', cleaned, flags=re.IGNORECASE)
+
+    # \``` ... \``` のようなコードブロックを除去
+    cleaned = re.sub(r'\```\s*|\s*\```', '', cleaned)
+
+    # <xml> ... </xml> のようなタグを除去
+    cleaned = re.sub(r'<xml>\s*|\s*</xml>', '', cleaned, flags=re.IGNORECASE)
+
+    # 不要な空白や改行を整理
+    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
+
+    return cleaned
+
+
+def _extract_qa_from_fallback_text(text: str) -> List[Dict[str, str]]:
+    """テキストから直接Q&Aを抽出するフォールバック関数"""
+    qa_pairs = []
+
+    try:
+        # <Question>と<Answer>タグで分割
+        import re
+
+        # Questionタグを検索
+        question_pattern = r'<Question>(.*?)</Question>'
+        answer_pattern = r'<Answer>(.*?)</Answer>'
+
+        questions = re.findall(question_pattern, text, re.DOTALL)
+        answers = re.findall(answer_pattern, text, re.DOTALL)
+
+        # 同じ数の質問と回答がある場合のみペアを作成
+        min_count = min(len(questions), len(answers))
+        for i in range(min_count):
+            qa_pairs.append({
+                "question": _decode_xml_entities(questions[i].strip()),
+                "answer": _decode_xml_entities(answers[i].strip())
+            })
+
+    except Exception as e:
+        console.print(f"[red]フォールバック解析も失敗:[/red] {e}")
+
+    return qa_pairs
+
+
+def _decode_xml_entities(text: str) -> str:
+    """XMLエンティティをデコードする（シンプル版）"""
+    import html
+    if text:
+        return html.unescape(text)
+    return text
+
+
+def _save_qa_pairs_to_xml(qa_pairs: List[Dict[str, str]], logs_dir: Path, qa_filename: str) -> None:
+    """Q&Aペアをきれいに整形されたXMLファイルとして保存（サブエレメント方式）"""
+    if not qa_pairs or not logs_dir:
+        return
+
+    qa_file_path = logs_dir / qa_filename
+
+    # ElementTreeで構造化生成
+    root = ET.Element("QAPairs")
+    for qa in qa_pairs:
+        pair_elem = ET.SubElement(root, "Pair")
+        question_elem = ET.SubElement(pair_elem, "Question")
+        question_elem.text = qa["question"]
+
+        answer_elem = ET.SubElement(pair_elem, "Answer")
+
+        # 回答内容を解析
+        parsed_answer = _parse_answer_with_think(qa["answer"])
+
+        if parsed_answer["has_think"]:
+            # <think>をサブエレメントとして追加
+            think_elem = ET.SubElement(answer_elem, "think")
+            think_elem.text = parsed_answer["think_content"]
+            think_elem.tail = parsed_answer["answer_content"]
+        else:
+            # 通常の回答
+            answer_elem.text = parsed_answer["answer_content"]
+
+    # 整形して保存
+    rough_string = ET.tostring(root, 'utf-8')
+    reparsed = minidom.parseString(rough_string)
+    pretty_xml = reparsed.toprettyxml(indent="  ")
+
+    qa_file_path.write_text(pretty_xml, encoding='utf-8')
+    console.print(f"[green]✓[/green] QAペアを保存: {qa_filename} ({len(qa_pairs)}件)")
+
+
+def _parse_answer_with_think(answer_text: str) -> Dict[str, str]:
+    """<think>タグを含む回答をパースして分離"""
+    import re
+
+    # <think>...</think>タグを検索
+    think_match = re.search(r'<think>(.*?)</think>', answer_text, re.DOTALL)
+
+    if think_match:
+        think_content = think_match.group(1).strip()
+        # <think>タグ以降の回答テキストを取得
+        answer_content = answer_text[think_match.end():].strip()
+        return {
+            "has_think": True,
+            "think_content": think_content,
+            "answer_content": answer_content
+        }
+    else:
+        return {
+            "has_think": False,
+            "think_content": "",
+            "answer_content": answer_text
+        }
diff --git a/easy_dataset_cli/qa_generator.py b/easy_dataset_cli/generators/qa_generator_thinking.py
similarity index 68%
rename from easy_dataset_cli/qa_generator.py
rename to easy_dataset_cli/generators/qa_generator_thinking.py
index 545d830..114797d 100644
--- a/easy_dataset_cli/qa_generator.py
+++ b/easy_dataset_cli/generators/qa_generator_thinking.py
@@ -1,25 +1,25 @@
-# easy_dataset_cli/qa_generator.py
-"""Q&A生成関連機能"""
+#!/usr/bin/env python3
+"""
+思考フロー対応Q&A生成機能
+"""
 
 import os
 import xml.etree.ElementTree as ET
 from xml.dom import minidom
 from pathlib import Path
 from typing import List, Dict
-from litellm import completion
+from openai import OpenAI
 from rich.console import Console
 from dotenv import load_dotenv
 import traceback
 import json
 from datetime import datetime
 
-from .prompts import (
-    get_qa_generation_prompt,
-    get_qa_generation_with_fulltext_prompt,
+from ..prompts import (
     get_qa_generation_with_thinking_prompt,
-    get_ga_definition_generation_prompt
+    get_qa_generation_with_surrounding_prompt
 )
-from .xml_utils import parse_qa_from_text_fallback
+from ..xml_utils import parse_qa_from_text_fallback
 
 # .envファイルを読み込む
 load_dotenv()
@@ -27,7 +27,7 @@ load_dotenv()
 console = Console()
 
 
-def generate_qa_for_chunk_with_ga_and_fulltext(
+def generate_qa_for_chunk_with_ga_and_thinking(
     chunk: str,
     full_text: str,
     model: str,
@@ -35,8 +35,8 @@ def generate_qa_for_chunk_with_ga_and_fulltext(
     logs_dir: Path = None,
     num_qa_pairs: int = None
 ) -> List[Dict[str, str]]:
-    """litellmを使い、1つのチャンクと全文、1つのGAペアからQ&Aペアのリストを生成する"""
-    prompt_template = get_qa_generation_with_fulltext_prompt()
+    """OpenAIクライアントを使い、1つのチャンクと全文、1つのGAペアから思考フロー付きQ&Aペアのリストを生成する"""
+    prompt_template = get_qa_generation_with_thinking_prompt()
     prompt = prompt_template.format(
         chunk=chunk,
         full_text=full_text,
@@ -52,14 +52,17 @@ def generate_qa_for_chunk_with_ga_and_fulltext(
         {"role": "user", "content": prompt}
     ]
 
-    # OpenRouter用の環境変数設定
-    os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY", "")
+    # OpenAIクライアントの初期化
+    client = OpenAI(
+        base_url=os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1"),
+        api_key=os.getenv("OPENAI_API_KEY"),
+    )
 
     # タイムスタンプ付きログファイル名を生成
     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
     genre_safe = "".join(c for c in ga_pair['genre']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
     audience_safe = "".join(c for c in ga_pair['audience']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
-    
+
     try:
         # リクエストログを保存
         if logs_dir:
@@ -71,13 +74,42 @@ def generate_qa_for_chunk_with_ga_and_fulltext(
                 "prompt_length": len(prompt),
                 "messages": messages
             }
-            request_filename = f"request_{genre_safe}_{audience_safe}_{timestamp}.json"
+            request_filename = f"request_thinking_{genre_safe}_{audience_safe}_{timestamp}.json"
             request_file_path = logs_dir / request_filename
             with open(request_file_path, 'w', encoding='utf-8') as f:
                 json.dump(request_log, f, ensure_ascii=False, indent=2)
             console.print(f"[dim]リクエストログを保存: {request_filename}[/dim]")
 
-        response = completion(model=model, messages=messages)
+            # プロンプトをマークダウンファイルとして保存
+            prompt_filename = f"prompt_thinking_{genre_safe}_{audience_safe}_{timestamp}.md"
+            prompt_file_path = logs_dir / prompt_filename
+            prompt_content = f"""# QA生成プロンプト (思考フロー付き)
+
+**タイムスタンプ:** {timestamp}  
+**モデル:** {model}  
+**ジャンル:** {ga_pair['genre']['title']}  
+**オーディエンス:** {ga_pair['audience']['title']}  
+**プロンプト長:** {len(prompt)} 文字
+
+---
+
+## システムメッセージ
+
+{messages[0]['content']}
+
+---
+
+## ユーザープロンプト
+
+{prompt}
+"""
+            prompt_file_path.write_text(prompt_content, encoding='utf-8')
+            console.print(f"[dim]プロンプトファイルを保存: {prompt_filename}[/dim]")
+
+        response = client.chat.completions.create(
+            model=model,
+            messages=messages
+        )
         xml_content = response.choices[0].message.content
 
         # レスポンスログを保存
@@ -90,7 +122,7 @@ def generate_qa_for_chunk_with_ga_and_fulltext(
                 "response_length": len(xml_content),
                 "response_content": xml_content
             }
-            response_filename = f"response_{genre_safe}_{audience_safe}_{timestamp}.json"
+            response_filename = f"response_thinking_{genre_safe}_{audience_safe}_{timestamp}.json"
             response_file_path = logs_dir / response_filename
             with open(response_file_path, 'w', encoding='utf-8') as f:
                 json.dump(response_log, f, ensure_ascii=False, indent=2)
@@ -98,30 +130,28 @@ def generate_qa_for_chunk_with_ga_and_fulltext(
 
         # rawレスポンスを保存（オプション）
         if logs_dir:
-            raw_filename = f"qa_fulltext_raw_{genre_safe}_{audience_safe}_{timestamp}.md"
+            raw_filename = f"qa_thinking_raw_{genre_safe}_{audience_safe}_{timestamp}.md"
             raw_file_path = logs_dir / raw_filename
             raw_file_path.write_text(xml_content, encoding="utf-8")
 
         qa_pairs = _parse_qa_response(xml_content, logs_dir, genre_safe, audience_safe, timestamp)
-        
+
         # 生成したQAを保存
         if qa_pairs and logs_dir:
-            qa_filename = f"qa_pairs_{genre_safe}_{audience_safe}_{timestamp}.xml"
-            qa_file_path = logs_dir / qa_filename
-            
+            qa_filename = f"qa_pairs_thinking_{genre_safe}_{audience_safe}_{timestamp}.xml"
             _save_qa_pairs_to_xml(qa_pairs, logs_dir, qa_filename)
 
         return qa_pairs
 
     except Exception as general_error:
         # 詳細なエラー情報を表示
-        console.print(f"[bold red]チャンクとGAペアからのQ&A生成中にエラーが発生しました:[/bold red]")
+        console.print(f"[bold red]チャンクとGAペアからの思考フロー付きQ&A生成中にエラーが発生しました:[/bold red]")
         console.print(f"[bold red]エラータイプ:[/bold red] {type(general_error).__name__}")
         console.print(f"[bold red]エラーメッセージ:[/bold red] {str(general_error)}")
         console.print(f"[bold red]トレースバック:[/bold red]")
         console.print(traceback.format_exc())
         console.print(f"[dim]Genre: {ga_pair['genre']['title']}, Audience: {ga_pair['audience']['title']}[/dim]")
-        
+
         # エラーログを保存
         if logs_dir:
             error_log = {
@@ -133,26 +163,26 @@ def generate_qa_for_chunk_with_ga_and_fulltext(
                 "error_message": str(general_error),
                 "traceback": traceback.format_exc()
             }
-            error_filename = f"error_{genre_safe}_{audience_safe}_{timestamp}.json"
+            error_filename = f"error_thinking_{genre_safe}_{audience_safe}_{timestamp}.json"
             error_file_path = logs_dir / error_filename
             with open(error_file_path, 'w', encoding='utf-8') as f:
                 json.dump(error_log, f, ensure_ascii=False, indent=2)
             console.print(f"[dim]エラーログを保存: {error_filename}[/dim]")
-        
+
         return []
 
 
-def generate_qa_for_chunk_with_ga(
-    chunk: str,
+def generate_qa_for_chunk_with_surrounding_context(
+    content: str,
     model: str,
     ga_pair: Dict[str, Dict[str, str]],
     logs_dir: Path = None,
     num_qa_pairs: int = None
 ) -> List[Dict[str, str]]:
-    """litellmを使い、1つのチャンクと1つのGAペアからQ&Aペアのリストを生成する"""
-    prompt_template = get_qa_generation_prompt()
+    """OpenAIクライアントを使い、周辺コンテキストを含むチャンクからQ&Aペアのリストを生成する"""
+    prompt_template = get_qa_generation_with_surrounding_prompt()
     prompt = prompt_template.format(
-        context=chunk,
+        content=content,
         genre_title=ga_pair['genre']['title'],
         genre_description=ga_pair['genre']['description'],
         audience_title=ga_pair['audience']['title'],
@@ -165,14 +195,17 @@ def generate_qa_for_chunk_with_ga(
         {"role": "user", "content": prompt}
     ]
 
-    # OpenRouter用の環境変数設定
-    os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY", "")
+    # OpenAIクライアントの初期化
+    client = OpenAI(
+        base_url=os.getenv("OPENAI_BASE_URL", "https://openrouter.ai/api/v1"),
+        api_key=os.getenv("OPENAI_API_KEY"),
+    )
 
     # タイムスタンプ付きログファイル名を生成
     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
     genre_safe = "".join(c for c in ga_pair['genre']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
     audience_safe = "".join(c for c in ga_pair['audience']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
-    
+
     try:
         # リクエストログを保存
         if logs_dir:
@@ -184,13 +217,42 @@ def generate_qa_for_chunk_with_ga(
                 "prompt_length": len(prompt),
                 "messages": messages
             }
-            request_filename = f"request_{genre_safe}_{audience_safe}_{timestamp}.json"
+            request_filename = f"request_surrounding_{genre_safe}_{audience_safe}_{timestamp}.json"
             request_file_path = logs_dir / request_filename
             with open(request_file_path, 'w', encoding='utf-8') as f:
                 json.dump(request_log, f, ensure_ascii=False, indent=2)
             console.print(f"[dim]リクエストログを保存: {request_filename}[/dim]")
 
-        response = completion(model=model, messages=messages)
+            # プロンプトをマークダウンファイルとして保存
+            prompt_filename = f"prompt_surrounding_{genre_safe}_{audience_safe}_{timestamp}.md"
+            prompt_file_path = logs_dir / prompt_filename
+            prompt_content = f"""# QA生成プロンプト (周辺コンテキスト)
+
+**タイムスタンプ:** {timestamp}  
+**モデル:** {model}  
+**ジャンル:** {ga_pair['genre']['title']}  
+**オーディエンス:** {ga_pair['audience']['title']}  
+**プロンプト長:** {len(prompt)} 文字
+
+---
+
+## システムメッセージ
+
+{messages[0]['content']}
+
+---
+
+## ユーザープロンプト
+
+{prompt}
+"""
+            prompt_file_path.write_text(prompt_content, encoding='utf-8')
+            console.print(f"[dim]プロンプトファイルを保存: {prompt_filename}[/dim]")
+
+        response = client.chat.completions.create(
+            model=model,
+            messages=messages
+        )
         xml_content = response.choices[0].message.content
 
         # レスポンスログを保存
@@ -203,7 +265,7 @@ def generate_qa_for_chunk_with_ga(
                 "response_length": len(xml_content),
                 "response_content": xml_content
             }
-            response_filename = f"response_{genre_safe}_{audience_safe}_{timestamp}.json"
+            response_filename = f"response_surrounding_{genre_safe}_{audience_safe}_{timestamp}.json"
             response_file_path = logs_dir / response_filename
             with open(response_file_path, 'w', encoding='utf-8') as f:
                 json.dump(response_log, f, ensure_ascii=False, indent=2)
@@ -211,30 +273,28 @@ def generate_qa_for_chunk_with_ga(
 
         # rawレスポンスを保存（オプション）
         if logs_dir:
-            raw_filename = f"qa_raw_{genre_safe}_{audience_safe}_{timestamp}.md"
+            raw_filename = f"qa_surrounding_raw_{genre_safe}_{audience_safe}_{timestamp}.md"
             raw_file_path = logs_dir / raw_filename
             raw_file_path.write_text(xml_content, encoding="utf-8")
 
         qa_pairs = _parse_qa_response(xml_content, logs_dir, genre_safe, audience_safe, timestamp)
-        
+
         # 生成したQAを保存
         if qa_pairs and logs_dir:
-            qa_filename = f"qa_pairs_{genre_safe}_{audience_safe}_{timestamp}.xml"
-            qa_file_path = logs_dir / qa_filename
-            
+            qa_filename = f"qa_pairs_surrounding_{genre_safe}_{audience_safe}_{timestamp}.xml"
             _save_qa_pairs_to_xml(qa_pairs, logs_dir, qa_filename)
 
         return qa_pairs
 
     except Exception as general_error:
         # 詳細なエラー情報を表示
-        console.print(f"[bold red]チャンクとGAペアからのQ&A生成中にエラーが発生しました:[/bold red]")
+        console.print(f"[bold red]周辺コンテキストチャンクからのQ&A生成中にエラーが発生しました:[/bold red]")
         console.print(f"[bold red]エラータイプ:[/bold red] {type(general_error).__name__}")
         console.print(f"[bold red]エラーメッセージ:[/bold red] {str(general_error)}")
         console.print(f"[bold red]トレースバック:[/bold red]")
         console.print(traceback.format_exc())
         console.print(f"[dim]Genre: {ga_pair['genre']['title']}, Audience: {ga_pair['audience']['title']}[/dim]")
-        
+
         # エラーログを保存
         if logs_dir:
             error_log = {
@@ -246,58 +306,13 @@ def generate_qa_for_chunk_with_ga(
                 "error_message": str(general_error),
                 "traceback": traceback.format_exc()
             }
-            error_filename = f"error_{genre_safe}_{audience_safe}_{timestamp}.json"
+            error_filename = f"error_surrounding_{genre_safe}_{audience_safe}_{timestamp}.json"
             error_file_path = logs_dir / error_filename
             with open(error_file_path, 'w', encoding='utf-8') as f:
                 json.dump(error_log, f, ensure_ascii=False, indent=2)
             console.print(f"[dim]エラーログを保存: {error_filename}[/dim]")
-        
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
+        return []
 
 
 def _parse_qa_response(xml_content: str, logs_dir: Path = None, genre_safe: str = None, audience_safe: str = None, timestamp: str = None) -> List[Dict[str, str]]:
@@ -306,42 +321,42 @@ def _parse_qa_response(xml_content: str, logs_dir: Path = None, genre_safe: str
 
     # LLMからの出力の前処理：不要なテキストを除去
     cleaned_content = _clean_llm_response(xml_content)
-    
+
     # XML部分のみを抽出 - 優先的に<QAPairs>タグを探す
     xml_start = cleaned_content.find("<QAPairs>")
     xml_end = cleaned_content.rfind("</QAPairs>")
-    
+
     # <QAPairs>タグが見つからない場合は<Pair>タグで抽出を試行
     if xml_start == -1 or xml_end == -1:
         console.print("[yellow]<QAPairs>タグが見つからないため、<Pair>タグで抽出を試行します...[/yellow]")
         xml_start = cleaned_content.find("<Pair>")
         xml_end = cleaned_content.rfind("</Pair>")
-        
+
         # <Pair>タグで囲まれた部分を抽出
         if xml_start != -1 and xml_end != -1:
             # すべての<Pair>...</Pair>を抽出
             import re
             pair_pattern = r'<Pair>.*?</Pair>'
             pair_matches = re.findall(pair_pattern, cleaned_content, re.DOTALL)
-            
+
             for pair_match in pair_matches:
                 # 各PairからQuestionとAnswerを抽出
                 question_match = re.search(r'<Question>(.*?)</Question>', pair_match, re.DOTALL)
                 answer_match = re.search(r'<Answer>(.*?)</Answer>', pair_match, re.DOTALL)
-                
+
                 if question_match and answer_match:
                     qa_pairs.append({
                         "question": _decode_xml_entities(question_match.group(1).strip()),
                         "answer": _decode_xml_entities(answer_match.group(1).strip())
                     })
-            
+
             if qa_pairs:
                 console.print(f"[green]✓[/green] <Pair>タグから{len(qa_pairs)}件のQ&Aを抽出しました")
                 return qa_pairs
 
     if xml_start != -1 and xml_end != -1:
         clean_xml = cleaned_content[xml_start: xml_end + len("</QAPairs>")]
-        
+
         # XML解析用のログを保存
         if logs_dir and genre_safe and audience_safe and timestamp:
             xml_debug_log = {
@@ -365,36 +380,36 @@ def _parse_qa_response(xml_content: str, logs_dir: Path = None, genre_safe: str
 
                 if question_node is not None and answer_node is not None:
                     question_text = question_node.text or ""
-                    
+
                     # <Answer>要素内の内容を適切に取得
                     if len(answer_node) > 0:
                         # サブエレメントがある場合（<think>タグなど）
                         answer_parts = []
-                        
+
                         # Answer要素の直接のテキスト（<think>より前）
                         if answer_node.text:
                             answer_parts.append(answer_node.text.strip())
-                        
+
                         # 各サブエレメントのtail（サブエレメントの後のテキスト）
                         for child in answer_node:
                             if child.tag == 'think':
                                 # <think>タグの内容を取得
                                 think_content = child.text or ""
                                 answer_parts.append(f"<think>{think_content}</think>")
-                            
+
                             # サブエレメントの後のテキスト
                             if child.tail:
                                 answer_parts.append(child.tail.strip())
-                        
+
                         answer_text = "".join(answer_parts)
                     else:
                         # サブエレメントがない場合は通常のテキスト
                         answer_text = answer_node.text or ""
-                    
+
                     # XMLエンティティデコード
                     question_text = _decode_xml_entities(question_text)
                     answer_text = _decode_xml_entities(answer_text)
-                    
+
                     qa_pairs.append({
                         "question": question_text,
                         "answer": answer_text
@@ -404,7 +419,7 @@ def _parse_qa_response(xml_content: str, logs_dir: Path = None, genre_safe: str
             # XMLパースに失敗した場合、手動でテキスト解析
             console.print("[yellow]XMLパースエラー、自動解析を試行中...[/yellow]")
             console.print(f"[dim]パースエラー詳細: {str(parse_error)}[/dim]")
-            
+
             # エラーログを保存
             if logs_dir and genre_safe and audience_safe and timestamp:
                 parse_error_log = {
@@ -417,10 +432,10 @@ def _parse_qa_response(xml_content: str, logs_dir: Path = None, genre_safe: str
                 parse_error_file_path = logs_dir / parse_error_filename
                 with open(parse_error_file_path, 'w', encoding='utf-8') as f:
                     json.dump(parse_error_log, f, ensure_ascii=False, indent=2)
-            
+
             # 自動解析を試行
             qa_pairs = parse_qa_from_text_fallback(clean_xml)
-            
+
             # 自動解析でも失敗した場合のフォールバック
             if not qa_pairs:
                 console.print("[yellow]自動解析も失敗したため、テキストから直接Q&Aを抽出します...[/yellow]")
@@ -429,7 +444,7 @@ def _parse_qa_response(xml_content: str, logs_dir: Path = None, genre_safe: str
     if not qa_pairs:
         console.print(f"[bold red]LLMが生成したXMLの解析に失敗しました[/bold red]")
         console.print(f"[dim]受信したテキスト: {cleaned_content[:500]}...[/dim]")
-        
+
         # 解析失敗のログを保存
         if logs_dir and genre_safe and audience_safe and timestamp:
             failure_log = {
@@ -449,40 +464,40 @@ def _parse_qa_response(xml_content: str, logs_dir: Path = None, genre_safe: str
 def _clean_llm_response(response: str) -> str:
     """LLMからのレスポンスをクリーンアップする"""
     import re
-    
+
     # 不要なテキストを除去
     cleaned = response
-    
+
     # \```xml ... \``` のようなコードブロックを除去
     cleaned = re.sub(r'\```xml\s*|\s*\```', '', cleaned, flags=re.IGNORECASE)
-    
+
     # \``` ... \``` のようなコードブロックを除去
     cleaned = re.sub(r'\```\s*|\s*\```', '', cleaned)
-    
+
     # <xml> ... </xml> のようなタグを除去
     cleaned = re.sub(r'<xml>\s*|\s*</xml>', '', cleaned, flags=re.IGNORECASE)
-    
+
     # 不要な空白や改行を整理
     cleaned = re.sub(r'\s+', ' ', cleaned).strip()
-    
+
     return cleaned
 
 
 def _extract_qa_from_fallback_text(text: str) -> List[Dict[str, str]]:
     """テキストから直接Q&Aを抽出するフォールバック関数"""
     qa_pairs = []
-    
+
     try:
         # <Question>と<Answer>タグで分割
         import re
-        
+
         # Questionタグを検索
         question_pattern = r'<Question>(.*?)</Question>'
         answer_pattern = r'<Answer>(.*?)</Answer>'
-        
+
         questions = re.findall(question_pattern, text, re.DOTALL)
         answers = re.findall(answer_pattern, text, re.DOTALL)
-        
+
         # 同じ数の質問と回答がある場合のみペアを作成
         min_count = min(len(questions), len(answers))
         for i in range(min_count):
@@ -490,10 +505,10 @@ def _extract_qa_from_fallback_text(text: str) -> List[Dict[str, str]]:
                 "question": _decode_xml_entities(questions[i].strip()),
                 "answer": _decode_xml_entities(answers[i].strip())
             })
-            
+
     except Exception as e:
         console.print(f"[red]フォールバック解析も失敗:[/red] {e}")
-    
+
     return qa_pairs
 
 
@@ -505,49 +520,25 @@ def _decode_xml_entities(text: str) -> str:
     return text
 
 
-def _parse_answer_with_think(answer_text: str) -> Dict[str, str]:
-    """<think>タグを含む回答をパースして分離"""
-    import re
-    
-    # <think>...</think>タグを検索
-    think_match = re.search(r'<think>(.*?)</think>', answer_text, re.DOTALL)
-    
-    if think_match:
-        think_content = think_match.group(1).strip()
-        # <think>タグ以降の回答テキストを取得
-        answer_content = answer_text[think_match.end():].strip()
-        return {
-            "has_think": True,
-            "think_content": think_content,
-            "answer_content": answer_content
-        }
-    else:
-        return {
-            "has_think": False,
-            "think_content": "",
-            "answer_content": answer_text
-        }
-
-
 def _save_qa_pairs_to_xml(qa_pairs: List[Dict[str, str]], logs_dir: Path, qa_filename: str) -> None:
     """Q&Aペアをきれいに整形されたXMLファイルとして保存（サブエレメント方式）"""
     if not qa_pairs or not logs_dir:
         return
-        
+
     qa_file_path = logs_dir / qa_filename
-    
+
     # ElementTreeで構造化生成
     root = ET.Element("QAPairs")
     for qa in qa_pairs:
         pair_elem = ET.SubElement(root, "Pair")
         question_elem = ET.SubElement(pair_elem, "Question")
         question_elem.text = qa["question"]
-        
+
         answer_elem = ET.SubElement(pair_elem, "Answer")
-        
+
         # 回答内容を解析
         parsed_answer = _parse_answer_with_think(qa["answer"])
-        
+
         if parsed_answer["has_think"]:
             # <think>をサブエレメントとして追加
             think_elem = ET.SubElement(answer_elem, "think")
@@ -556,126 +547,35 @@ def _save_qa_pairs_to_xml(qa_pairs: List[Dict[str, str]], logs_dir: Path, qa_fil
         else:
             # 通常の回答
             answer_elem.text = parsed_answer["answer_content"]
-    
+
     # 整形して保存
     rough_string = ET.tostring(root, 'utf-8')
     reparsed = minidom.parseString(rough_string)
     pretty_xml = reparsed.toprettyxml(indent="  ")
-    
+
     qa_file_path.write_text(pretty_xml, encoding='utf-8')
     console.print(f"[green]✓[/green] QAペアを保存: {qa_filename} ({len(qa_pairs)}件)")
 
 
-def generate_qa_for_chunk_with_ga_and_thinking(
-    chunk: str,
-    full_text: str,
-    model: str,
-    ga_pair: Dict[str, Dict[str, str]],
-    logs_dir: Path = None,
-    num_qa_pairs: int = None
-) -> List[Dict[str, str]]:
-    """litellmを使い、1つのチャンクと全文、1つのGAペアから思考フロー付きQ&Aペアのリストを生成する"""
-    prompt_template = get_qa_generation_with_thinking_prompt()
-    prompt = prompt_template.format(
-        chunk=chunk,
-        full_text=full_text,
-        genre_title=ga_pair['genre']['title'],
-        genre_description=ga_pair['genre']['description'],
-        audience_title=ga_pair['audience']['title'],
-        audience_description=ga_pair['audience']['description'],
-        num_qa_pairs=num_qa_pairs if num_qa_pairs is not None else "複数の"
-    )
-
-    messages = [
-        {"role": "system", "content": "あなたは、XML形式で厳密に出力する優秀なアシスタントです。通常のXMLの特殊文字（&, \", '）は適切にエスケープしてください。ただし、<Question>、<Answer>、<think>タグはそのまま使用してください。改行は含めずに出力してください。"},
-        {"role": "user", "content": prompt}
-    ]
-
-    # OpenRouter用の環境変数設定
-    os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY", "")
-
-    # タイムスタンプ付きログファイル名を生成
-    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
-    genre_safe = "".join(c for c in ga_pair['genre']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
-    audience_safe = "".join(c for c in ga_pair['audience']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
-    
-    try:
-        # リクエストログを保存
-        if logs_dir:
-            request_log = {
-                "timestamp": timestamp,
-                "model": model,
-                "genre": ga_pair['genre']['title'],
-                "audience": ga_pair['audience']['title'],
-                "prompt_length": len(prompt),
-                "messages": messages
-            }
-            request_filename = f"request_thinking_{genre_safe}_{audience_safe}_{timestamp}.json"
-            request_file_path = logs_dir / request_filename
-            with open(request_file_path, 'w', encoding='utf-8') as f:
-                json.dump(request_log, f, ensure_ascii=False, indent=2)
-            console.print(f"[dim]リクエストログを保存: {request_filename}[/dim]")
-
-        response = completion(model=model, messages=messages)
-        xml_content = response.choices[0].message.content
-
-        # レスポンスログを保存
-        if logs_dir:
-            response_log = {
-                "timestamp": timestamp,
-                "model": model,
-                "genre": ga_pair['genre']['title'],
-                "audience": ga_pair['audience']['title'],
-                "response_length": len(xml_content),
-                "response_content": xml_content
-            }
-            response_filename = f"response_thinking_{genre_safe}_{audience_safe}_{timestamp}.json"
-            response_file_path = logs_dir / response_filename
-            with open(response_file_path, 'w', encoding='utf-8') as f:
-                json.dump(response_log, f, ensure_ascii=False, indent=2)
-            console.print(f"[dim]レスポンスログを保存: {response_filename}[/dim]")
-
-        # rawレスポンスを保存（オプション）
-        if logs_dir:
-            raw_filename = f"qa_thinking_raw_{genre_safe}_{audience_safe}_{timestamp}.md"
-            raw_file_path = logs_dir / raw_filename
-            raw_file_path.write_text(xml_content, encoding="utf-8")
-
-        qa_pairs = _parse_qa_response(xml_content, logs_dir, genre_safe, audience_safe, timestamp)
-
-        # 生成したQAを保存
-        if qa_pairs and logs_dir:
-            qa_filename = f"qa_pairs_thinking_{genre_safe}_{audience_safe}_{timestamp}.xml"
-            _save_qa_pairs_to_xml(qa_pairs, logs_dir, qa_filename)
-
-        return qa_pairs
-
-    except Exception as general_error:
-        # 詳細なエラー情報を表示
-        console.print(f"[bold red]チャンクとGAペアからの思考フロー付きQ&A生成中にエラーが発生しました:[/bold red]")
-        console.print(f"[bold red]エラータイプ:[/bold red] {type(general_error).__name__}")
-        console.print(f"[bold red]エラーメッセージ:[/bold red] {str(general_error)}")
-        console.print(f"[bold red]トレースバック:[/bold red]")
-        console.print(traceback.format_exc())
-        console.print(f"[dim]Genre: {ga_pair['genre']['title']}, Audience: {ga_pair['audience']['title']}[/dim]")
-        
-        # エラーログを保存
-        if logs_dir:
-            error_log = {
-                "timestamp": timestamp,
-                "model": model,
-                "genre": ga_pair['genre']['title'],
-                "audience": ga_pair['audience']['title'],
-                "error_type": type(general_error).__name__,
-                "error_message": str(general_error),
-                "traceback": traceback.format_exc()
-            }
-            error_filename = f"error_thinking_{genre_safe}_{audience_safe}_{timestamp}.json"
-            error_file_path = logs_dir / error_filename
-            with open(error_file_path, 'w', encoding='utf-8') as f:
-                json.dump(error_log, f, ensure_ascii=False, indent=2)
-            console.print(f"[dim]エラーログを保存: {error_filename}[/dim]")
-        
-        return []
+def _parse_answer_with_think(answer_text: str) -> Dict[str, str]:
+    """<think>タグを含む回答をパースして分離"""
+    import re
 
+    # <think>...</think>タグを検索
+    think_match = re.search(r'<think>(.*?)</think>', answer_text, re.DOTALL)
 
+    if think_match:
+        think_content = think_match.group(1).strip()
+        # <think>タグ以降の回答テキストを取得
+        answer_content = answer_text[think_match.end():].strip()
+        return {
+            "has_think": True,
+            "think_content": think_content,
+            "answer_content": answer_content
+        }
+    else:
+        return {
+            "has_think": False,
+            "think_content": "",
+            "answer_content": answer_text
+        }
diff --git a/easy_dataset_cli/main.py b/easy_dataset_cli/main.py
index 9285adf..0f42e47 100644
--- a/easy_dataset_cli/main.py
+++ b/easy_dataset_cli/main.py
@@ -1,428 +1,20 @@
-# easy_dataset_cli/main.py
-"""CLIエントリーポイント"""
+#!/usr/bin/env python3
+"""
+Easy Dataset CLI - メインエントリーポイント
+"""
 
-from pathlib import Path
-from typing_extensions import Annotated
-import typer
-from rich.console import Console
-from rich.progress import Progress
 from dotenv import load_dotenv
 
-from .core import (
-    split_text,
-    parse_ga_file,
-    generate_qa_for_chunk_with_ga,
-    generate_qa_for_chunk_with_ga_and_fulltext,
-    generate_qa_for_chunk_with_ga_and_thinking,
-    convert_to_xml_by_genre,
-    generate_ga_definitions,
-    parse_ga_definitions_from_xml,
-    save_ga_definitions_by_genre,
-    create_output_directories,
-    sanitize_filename,
-    convert_all_xml_to_alpaca,
-    upload_to_huggingface,
-    create_dataset_card
-)
-
 # .envファイルを読み込む
 load_dotenv()
 
-app = typer.Typer(
-    help="テキストファイルからQ&Aペアを生成するシンプルなCLIツール。",
-    context_settings={"help_option_names": ["-h", "--help"]}
-)
-console = Console()
-
-
-@app.command()
-def create_ga(
-    file_path: Annotated[Path, typer.Argument(
-        exists=True, dir_okay=False, readable=True,
-        help="GAペアの定義を生成するための元のテキストファイル。"
-    )],
-    output_dir: Annotated[Path, typer.Option(
-        "--output-dir", "-o", file_okay=False, dir_okay=True, writable=True,
-        help="生成されたGAペア定義ファイルを保存するディレクトリ。"
-    )],
-    model: Annotated[str, typer.Option(
-        "--model", "-m",
-        help="GAペア定義の生成に使用するLLMモデル名。"
-    )] = "openrouter/openai/gpt-oss-120b",
-    num_ga_pairs: Annotated[int, typer.Option(
-        "--num-ga-pairs", "-g",
-        help="生成するGAペアの数。指定しない場合はLLMが適切な数を決定します。"
-    )] = 5,
-):
-    """元の文章を分析し、GAペア定義をXML形式で生成し、Genreごとにマークダウンファイルに保存します。"""
-    console.print(f"ファイルを読み込んでいます: [cyan]{file_path}[/cyan]")
-
-    try:
-        text = file_path.read_text(encoding="utf-8")
-        console.print(f"[dim]読み込んだテキスト長: {len(text)} 文字[/dim]")
-
-        console.print("[bold green]LLMに最適なGAペアを提案させています...[/bold green]")
-        xml_content = generate_ga_definitions(text, model=model, num_ga_pairs=num_ga_pairs)
-
-        # 出力ディレクトリ構造を作成
-        dirs = create_output_directories(output_dir)
-        console.print(f"[dim]出力ディレクトリを作成しました: ga/, logs/, qa/[/dim]")
-        
-        # LLMのrawレスポンスをlogsディレクトリに保存
-        raw_file_path = dirs["logs"] / "raw.md"
-        raw_file_path.write_text(xml_content, encoding="utf-8")
-        console.print(f"[green]✓[/green] LLMのrawレスポンスを保存しました: [cyan]{raw_file_path}[/cyan]")
-
-        console.print("[bold green]XMLからGAペアを解析しています...[/bold green]")
-        # XMLからGAペアを解析
-        ga_pairs = parse_ga_definitions_from_xml(xml_content)
-        
-        if not ga_pairs:
-            console.print("[bold red]有効なGAペアが生成されませんでした。[/bold red]")
-            console.print("[yellow]生成されたXMLの内容を確認してください:[/yellow]")
-            console.print(xml_content)
-            raise typer.Exit(code=1)
-
-        # 元のXMLファイルをgaディレクトリに保存（クリーンなXMLのみ）
-        xml_file_path = dirs["ga"] / "ga_definitions.xml"
-        # XMLタグ部分のみを抽出して保存
-        xml_start = xml_content.find("<GADefinitions>")
-        xml_end = xml_content.rfind("</GADefinitions>")
-        if xml_start != -1 and xml_end != -1:
-            clean_xml = xml_content[xml_start: xml_end + len("</GADefinitions>")]
-            xml_file_path.write_text(clean_xml, encoding="utf-8")
-            console.print(f"[green]✓[/green] GA定義XMLファイルを保存しました: [cyan]{xml_file_path}[/cyan]")
-
-        # Genreごとにマークダウンファイルをgaディレクトリに保存
-        save_ga_definitions_by_genre(ga_pairs, dirs["ga"])
-
-        console.print(
-            f"\n[bold green]✓[/bold green] {len(ga_pairs)}個のGAペアを "
-            f"[cyan]{dirs['ga']}[/cyan] に保存しました。"
-        )
-        console.print(
-            "[yellow]ヒント: 生成されたファイルをレビューし、必要に応じて編集してから "
-            "`generate` コマンドで使用してください。[/yellow]"
-        )
-
-    except Exception as e:
-        console.print(
-            f"[bold red]GA定義ファイルの生成中にエラーが発生しました:[/bold red] {e}"
-        )
-        raise typer.Exit(code=1)
-
-
-@app.command()
-def generate(
-    file_path: Annotated[Path, typer.Argument(
-        exists=True, dir_okay=False, readable=True,
-        help="元のテキストファイルへのパス。"
-    )],
-    ga_file: Annotated[Path, typer.Option(
-        "--ga-file", "-g", exists=True, dir_okay=False, readable=True,
-        help="Genre-Audienceペアを定義したXMLまたはMarkdownファイルへのパス。gaディレクトリのga_definitions.xmlを推奨。"
-    )],
-    output_dir: Annotated[Path, typer.Option(
-        "--output-dir", "-o", file_okay=False, dir_okay=True, writable=True,
-        help="生成されたXMLファイルを保存するディレクトリ。指定しない場合はコンソールに出力します。"
-    )] = None,
-    model: Annotated[str, typer.Option(
-        "--model", "-m",
-        help="Q&Aペアの生成に使用するLLMモデル名。"
-    )] = "openrouter/openai/gpt-oss-120b",
-    chunk_size: Annotated[int, typer.Option(
-        help="テキストチャンクの最大サイズ。"
-    )] = 2000,
-    chunk_overlap: Annotated[int, typer.Option(
-        help="チャンク間のオーバーラップサイズ。"
-    )] = 200,
-    num_qa_pairs: Annotated[int, typer.Option(
-        "--num-qa-pairs", "-q",
-        help="各チャンク・GAペアの組み合わせで生成するQ&Aペアの数。指定しない場合はLLMが適切な数を決定します。"
-    )] = 10,
-    use_fulltext: Annotated[bool, typer.Option(
-        "--use-fulltext", "-f",
-        help="全文をコンテキストとして含めてQA生成を行います。より文脈を理解したQAが生成されますが、処理時間とコストが増加します。"
-    )] = False,
-    use_thinking: Annotated[bool, typer.Option(
-        "--use-thinking", "-T",
-        help="各Q&Aペアに思考プロセスを追加して生成します。より深い理解と説明が可能になりますが、処理時間とコストが増加します。"
-    )] = False,
-    append_mode: Annotated[bool, typer.Option(
-        "--append", "-A",
-        help="既存のXMLファイルに新しいQ&Aを追加します。指定しない場合は上書きします。"
-    )] = False,
-    export_alpaca: Annotated[bool, typer.Option(
-        "--export-alpaca", "-a",
-        help="生成されたQ&AペアをAlpaca形式のJSONファイルとして出力します。"
-    )] = False,
-    upload_hf: Annotated[bool, typer.Option(
-        "--upload-hf", "-u",
-        help="生成されたデータセットをHugging Face Hubにアップロードします。"
-    )] = False,
-    hf_repo_name: Annotated[str, typer.Option(
-        "--hf-repo-name", "-r",
-        help="Hugging Face Hubのリポジトリ名（例: username/dataset-name）"
-    )] = "",
-    hf_token: Annotated[str, typer.Option(
-        "--hf-token", "-t",
-        help="Hugging Face APIトークン（環境変数HUGGINGFACE_TOKENからも取得可能）"
-    )] = "",
-    hf_private: Annotated[bool, typer.Option(
-        "--hf-private",
-        help="Hugging Faceリポジトリをプライベートにします。"
-    )] = False,
-):
-    """テキストファイルとGA定義からQ&Aペアを生成し、Genre別のXMLファイルとして出力します。
-    
-    --use-fulltextオプションを使用すると、各チャンクの処理時に全文をコンテキストとして含めることで、
-    より文脈を理解した高品質なQ&Aペアを生成できます。ただし、処理時間とAPIコストが増加します。
-    """
-    try:
-        console.print(f"ファイルを読み込んでいます: [cyan]{file_path}[/cyan]")
-        text = file_path.read_text(encoding="utf-8")
-
-        console.print(f"GAペアを解析しています: [cyan]{ga_file}[/cyan]")
-        ga_pairs = parse_ga_file(ga_file)
-
-        if not ga_pairs:
-            console.print("[bold red]有効なGAペアが定義ファイルに見つかりませんでした。[/bold red]")
-            raise typer.Exit(code=1)
-
-        console.print(f"[green]{len(ga_pairs)}[/green] 個のGAペアを見つけました。")
-
-        console.print("テキストをチャンクに分割しています...")
-        chunks = split_text(text, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
-        console.print(f"[green]{len(chunks)}[/green] 個のチャンクを作成しました。")
-
-        all_qa_pairs_with_ga = []
-        total_tasks = len(chunks) * len(ga_pairs)
-        
-        # 出力ディレクトリがある場合は構造を作成
-        dirs = None
-        if output_dir:
-            dirs = create_output_directories(output_dir)
-            console.print(f"[dim]出力ディレクトリを作成しました: ga/, logs/, qa/[/dim]")
-
-        # 全文使用の場合は警告を表示
-        if use_fulltext:
-            console.print("[yellow]⚠ 全文コンテキストモードが有効です。処理時間とコストが増加する可能性があります。[/yellow]")
-            console.print(f"[dim]全文長: {len(text)} 文字[/dim]")
-
-        # 思考フロー使用の場合は警告を表示
-        if use_thinking:
-            console.print("[yellow]⚠ 思考フローモードが有効です。各Q&Aに思考プロセスが追加されます。[/yellow]")
-
-        with Progress(console=console) as progress:
-            task = progress.add_task("[green]Q&Aペアを生成中...", total=total_tasks)
-
-            for chunk in chunks:
-                for ga_pair in ga_pairs:
-                    if use_thinking:
-                        qa_pairs = generate_qa_for_chunk_with_ga_and_thinking(
-                            chunk=chunk,
-                            full_text=text if use_fulltext else "",
-                            model=model,
-                            ga_pair=ga_pair,
-                            logs_dir=dirs["logs"] if dirs else None,
-                            num_qa_pairs=num_qa_pairs
-                        )
-                    elif use_fulltext:
-                        qa_pairs = generate_qa_for_chunk_with_ga_and_fulltext(
-                            chunk=chunk,
-                            full_text=text,
-                            model=model,
-                            ga_pair=ga_pair,
-                            logs_dir=dirs["logs"] if dirs else None,
-                            num_qa_pairs=num_qa_pairs
-                        )
-                    else:
-                        qa_pairs = generate_qa_for_chunk_with_ga(
-                            chunk, model=model, ga_pair=ga_pair,
-                            logs_dir=dirs["logs"] if dirs else None,
-                            num_qa_pairs=num_qa_pairs
-                        )
-
-                    for pair in qa_pairs:
-                        qa_entry = {
-                            "genre": ga_pair['genre']['title'],
-                            "audience": ga_pair['audience']['title'],
-                            "question": pair['question'],
-                            "answer": pair['answer'],  # <think>...</think>回答...形式がそのまま入る
-                        }
-                        all_qa_pairs_with_ga.append(qa_entry)
-
-                    progress.update(
-                        task, advance=1,
-                        description=f"Genre: {ga_pair['genre']['title']}"
-                    )
-
-        console.print(
-            f"\n合計 [bold green]{len(all_qa_pairs_with_ga)}[/bold green] "
-            "個のQ&Aペアを生成しました。"
-        )
-
-        xml_outputs_by_genre = convert_to_xml_by_genre(all_qa_pairs_with_ga, dirs["qa"] if dirs else None, append_mode)
-
-        if dirs:
-            console.print(f"XMLファイルを [cyan]{dirs['qa']}[/cyan] に保存しています...")
-
-            for genre, xml_content in xml_outputs_by_genre.items():
-                safe_genre_name = sanitize_filename(genre)
-                output_file_path = dirs["qa"] / f"{safe_genre_name}.xml"
-                output_file_path.write_text(xml_content, encoding="utf-8")
-                console.print(f"  - [green]✓[/green] {output_file_path.name}")
-
-            console.print("\n[bold green]すべてのファイルの保存が完了しました。[/bold green]")
-            
-            # アルパカ形式でのエクスポート
-            if export_alpaca:
-                console.print("\n[bold blue]Alpaca形式のJSONファイルを生成中...[/bold blue]")
-                alpaca_file = dirs["base"] / "dataset_alpaca.json"
-                alpaca_data = convert_all_xml_to_alpaca(dirs["qa"], alpaca_file)
-                
-                # データセットカードを生成
-                readme_file = dirs["base"] / "README.md"
-                create_dataset_card(alpaca_data, readme_file, "Generated QA Dataset")
-                
-                # Hugging Face Hubにアップロード
-                if upload_hf:
-                    if not hf_repo_name:
-                        console.print("[bold red]--hf-repo-nameが指定されていません！[/bold red]")
-                        console.print("[yellow]例: --hf-repo-name username/my-qa-dataset[/yellow]")
-                    else:
-                        console.print(f"\n[bold blue]Hugging Face Hubにアップロード中...[/bold blue]")
-                        success = upload_to_huggingface(
-                            dataset_data=alpaca_data,
-                            repo_name=hf_repo_name,
-                            hf_token=hf_token if hf_token else None,
-                            private=hf_private,
-                            commit_message=f"Upload QA dataset with {len(alpaca_data)} entries",
-                            readme_file=readme_file
-                        )
-                        if not success:
-                            console.print("[bold red]Hugging Faceアップロードに失敗しました[/bold red]")
-        else:
-            console.print("\n--- 生成されたQ&Aペア (Genre別XML) ---")
-            for genre, xml_content in xml_outputs_by_genre.items():
-                console.print(f"\n[bold yellow]## Genre: {genre} ##[/bold yellow]")
-                console.print(xml_content, overflow="fold")
-    
-    except Exception as e:
-        console.print(f"[bold red]エラーが発生しました:[/bold red]")
-        console.print(f"[bold red]エラータイプ:[/bold red] {type(e).__name__}")
-        console.print(f"[bold red]エラーメッセージ:[/bold red] {str(e)}")
-        console.print(f"[bold red]トレースバック:[/bold red]")
-        import traceback
-        console.print(traceback.format_exc())
-        raise typer.Exit(code=1)
-
-
-@app.command()
-def convert_to_alpaca(
-    qa_dir: Annotated[Path, typer.Argument(
-        exists=True, dir_okay=True, readable=True,
-        help="XMLファイルが保存されているqaディレクトリへのパス。"
-    )],
-    output_file: Annotated[Path, typer.Option(
-        "--output-file", "-o", file_okay=True, dir_okay=False,
-        help="出力するAlpaca形式JSONファイルのパス。"
-    )] = None,
-    upload_hf: Annotated[bool, typer.Option(
-        "--upload-hf", "-u",
-        help="生成されたデータセットをHugging Face Hubにアップロードします。"
-    )] = False,
-    hf_repo_name: Annotated[str, typer.Option(
-        "--hf-repo-name", "-r",
-        help="Hugging Face Hubのリポジトリ名（例: username/dataset-name）"
-    )] = "",
-    hf_token: Annotated[str, typer.Option(
-        "--hf-token", "-t",
-        help="Hugging Face APIトークン（環境変数HUGGINGFACE_TOKENからも取得可能）"
-    )] = "",
-    hf_private: Annotated[bool, typer.Option(
-        "--hf-private",
-        help="Hugging Faceリポジトリをプライベートにします。"
-    )] = False,
-):
-    """既存のXMLファイルをAlpaca形式のJSONに変換し、オプションでHugging Face Hubにアップロードします。"""
-    
-    try:
-        # デフォルトの出力ファイル名を設定
-        if output_file is None:
-            output_file = qa_dir.parent / "dataset_alpaca.json"
-        
-        console.print(f"XMLファイルを変換中: [cyan]{qa_dir}[/cyan]")
-        
-        # アルパカ形式に変換
-        alpaca_data = convert_all_xml_to_alpaca(qa_dir, output_file)
-        
-        if not alpaca_data:
-            console.print("[bold red]変換できるデータが見つかりませんでした。[/bold red]")
-            raise typer.Exit(code=1)
-        
-        # データセットカードを生成
-        readme_file = output_file.parent / "README.md"
-        create_dataset_card(alpaca_data, readme_file, "Converted QA Dataset")
-        
-        # Hugging Face Hubにアップロード
-        if upload_hf:
-            if not hf_repo_name:
-                console.print("[bold red]--hf-repo-nameが指定されていません！[/bold red]")
-                console.print("[yellow]例: --hf-repo-name username/my-qa-dataset[/yellow]")
-                raise typer.Exit(code=1)
-            
-            console.print(f"\n[bold blue]Hugging Face Hubにアップロード中...[/bold blue]")
-            success = upload_to_huggingface(
-                dataset_data=alpaca_data,
-                repo_name=hf_repo_name,
-                hf_token=hf_token if hf_token else None,
-                private=hf_private,
-                commit_message=f"Upload converted QA dataset with {len(alpaca_data)} entries",
-                readme_file=readme_file
-            )
-            
-            if not success:
-                console.print("[bold red]Hugging Faceアップロードに失敗しました[/bold red]")
-                raise typer.Exit(code=1)
-        
-        console.print(f"\n[bold green]✓[/bold green] 変換が完了しました！")
-        
-    except Exception as e:
-        console.print(f"[bold red]変換中にエラーが発生しました:[/bold red] {e}")
-        raise typer.Exit(code=1)
-
-
-@app.command()
-def aggregate_logs(
-    output_dir: Annotated[Path, typer.Argument(
-        exists=True, dir_okay=True, readable=True,
-        help="logsフォルダが含まれる出力ディレクトリへのパス。"
-    )]
-):
-    """logsフォルダ内のタイムスタンプ付きXMLファイルを集約してqaフォルダのXMLを生成します。"""
-    
-    try:
-        logs_dir = output_dir / "logs"
-        qa_dir = output_dir / "qa"
-        
-        if not logs_dir.exists():
-            console.print(f"[bold red]logsフォルダが見つかりません: {logs_dir}[/bold red]")
-            raise typer.Exit(code=1)
-        
-        console.print(f"logsフォルダ: [cyan]{logs_dir}[/cyan]")
-        console.print(f"出力先qaフォルダ: [cyan]{qa_dir}[/cyan]")
-        
-        # XMLファイルを集約してqaフォルダに生成
-        from easy_dataset_cli.core import aggregate_logs_xml_to_qa
-        aggregate_logs_xml_to_qa(logs_dir, qa_dir)
-        
-        console.print(f"\n[bold green]✓[/bold green] 集約が完了しました！")
-        
-    except Exception as e:
-        console.print(f"[bold red]エラーが発生しました:[/bold red] {e}")
-        raise typer.Exit(code=1)
+# commandsからアプリをインポート
+from .commands import app, print_logo
 
+def main():
+    """メインエントリーポイント関数"""
+    print_logo()
+    app()
 
 if __name__ == "__main__":
-    app()
+    main()
diff --git a/easy_dataset_cli/prompts.py b/easy_dataset_cli/prompts.py
index c2b00b8..0237879 100644
--- a/easy_dataset_cli/prompts.py
+++ b/easy_dataset_cli/prompts.py
@@ -7,7 +7,15 @@ from pathlib import Path
 def load_prompt_template(template_name: str) -> str:
     """プロンプトテンプレートをマークダウンファイルから読み込む"""
     prompt_dir = Path(__file__).parent / "prompts"
-    template_path = prompt_dir / f"{template_name}.md"
+    
+    # GA系プロンプトかQA系プロンプトかを判定
+    if template_name.startswith("ga_"):
+        template_path = prompt_dir / "ga" / f"{template_name}.md"
+    elif template_name.startswith("qa_"):
+        template_path = prompt_dir / "qa" / f"{template_name}.md"
+    else:
+        # 従来の形式も保持
+        template_path = prompt_dir / f"{template_name}.md"
     
     if not template_path.exists():
         raise FileNotFoundError(f"プロンプトテンプレートが見つかりません: {template_path}")
@@ -33,3 +41,8 @@ def get_ga_definition_generation_prompt() -> str:
 def get_qa_generation_with_thinking_prompt() -> str:
     """思考フロー対応Q&A生成プロンプトを取得"""
     return load_prompt_template("qa_generation_with_thinking")
+
+
+def get_qa_generation_with_surrounding_prompt() -> str:
+    """周辺チャンク付Q&A生成プロンプトを取得"""
+    return load_prompt_template("qa_generation_with_surrounding")
diff --git a/easy_dataset_cli/prompts/ga/ga_definition_generation.md b/easy_dataset_cli/prompts/ga/ga_definition_generation.md
new file mode 100644
index 0000000..43779f1
--- /dev/null
+++ b/easy_dataset_cli/prompts/ga/ga_definition_generation.md
@@ -0,0 +1,51 @@
+# 役割: GA（Genre-Audience）ペア定義の専門家
+
+あなたは、与えられた文章の内容を分析し、最適なGenre（体裁）とAudience（読者）のペアを提案する専門家です。
+
+## プロジェクト情報
+
+このツールは**easy-dataset-cli**プロジェクトの一部です。
+- GitHub: https://github.com/Sunwood-ai-labsII/easy-dataset-cli.git
+- 用途: 高品質なQ&Aデータセットの生成
+- 主要機能: テキストからの自動Q&Aペア生成、体裁・読者に応じたカスタマイズ
+
+## 指示:
+1. 与えられた文章の内容、トピック、専門性レベルを分析してください。
+2. この文章から質問と回答のペアを生成する際に最適となる{num_ga_pairs}個のGenre-Audienceペアを提案してください。
+3. 各Genreは異なる文体・形式（学術論文、技術ブログ、教科書、FAQ、対話形式など）を表現してください。
+4. 各Audienceは異なる知識レベル・立場（初心者、学生、専門家、実務者など）を表現してください。
+5. 文章の内容に適したペアを選択し、多様性・多角性を確保してください。
+
+## 文章:
+---
+{context}
+---
+
+## 出力形式:
+**絶対に守ること：**
+- 出力は、ルート要素が `<GADefinitions>` で始まる純粋なXMLのみにしてください
+- XML宣言 `<?xml version="1.0" encoding="utf-8"?>` を先頭に追加してください
+- ネストされたタグを含め、閉じタグまで完全に含めてください
+- 空白、改行、コードブロック記号（\```や\```xml）は一切出力しないでください
+- 説明文、コメント、追加のテキストは一切出力しないでください
+
+**XML構造：**
+各GAペアは `<Pair>` タグで囲み、その中に `<Genre>` と `<Audience>` タグを含めてください。
+- `<Genre>` タグ内には `<Title>` と `<Description>` を含む
+- `<Audience>` タグ内には `<Title>` と `<Description>` を含む
+
+**実施例（この構造を完全にコピー）：**
+<GADefinitions>
+<Pair>
+<Genre>
+<Title>FAQ</Title>
+<Description>ユーザーがテストに関する特定の質問に素早くアクセスできるような形式で、よくある質問に対する回答を簡潔にまとめたもの。</Description>
+</Genre>
+<Audience>
+<Title>初心者</Title>
+<Description>テストシステムやドキュメント生成を初めて扱う人々。基本的な概念や手順を手軽に学びたい人たち。</Description>
+</Audience>
+</Pair>
+</GADefinitions>
+
+それでは、最適なGA定義の生成を開始してください。
diff --git a/easy_dataset_cli/prompts/ga_definition_generation.md b/easy_dataset_cli/prompts/ga_definition_generation.md
deleted file mode 100644
index 17c05a4..0000000
--- a/easy_dataset_cli/prompts/ga_definition_generation.md
+++ /dev/null
@@ -1,47 +0,0 @@
-# 役割: GA（Genre-Audience）ペア定義の専門家
-
-あなたは、与えられた文章の内容を分析し、最適なGenre（体裁）とAudience（読者）のペアを提案する専門家です。
-
-## 指示:
-1. 与えられた文章の内容、トピック、専門性レベルを分析してください。
-2. この文章から質問と回答のペアを生成する際に最適となる{num_ga_pairs}個のGenre-Audienceペアを提案してください。
-3. 各Genreは異なる文体・形式（学術論文、技術ブログ、教科書、FAQ、対話形式など）を表現してください。
-4. 各Audienceは異なる知識レベル・立場（初心者、学生、専門家、実務者など）を表現してください。
-5. 文章の内容に適したペアを選択し、多様性・多角性を確保してください。
-
-## 文章:
----
-{context}
----
-
-## 出力形式:
-**必ず**、ルート要素が `<GADefinitions>` である単一の有効なXMLとして応答してください。XML以外の説明文は一切含めないでください。
-各GAペアは `<Pair>` タグで囲み、その中に `<Genre>` と `<Audience>` タグを含めてください。
-
-## 出力例:
-\```xml
-<GADefinitions>
-<Pair>
-<Genre>
-<Title>FAQ</Title>
-<Description>ユーザーがゲームに関する特定の質問に素早くアクセスできるような形式で、よくある質問に対する回答を簡潔にまとめる。</Description>
-</Genre>
-<Audience>
-<Title>初心者ゲーマー</Title>
-<Description>東方Projectや弾幕系シューティングゲームを初めてプレイする人々。ゲームの基本的な情報や攻略のヒントが欲しい。</Description>
-</Audience>
-</Pair>
-<Pair>
-<Genre>
-<Title>テクニカルガイド</Title>
-<Description>ゲームシステム、必要環境、インストール方法などの技術的な詳細を説明する形式。特に技術的な詳細に焦点を当てる。</Description>
-</Genre>
-<Audience>
-<Title>PCゲーミング愛好者</Title>
-<Description>PCでのゲームプレイに慣れているが、特に東方シリーズに関する技術的な詳細とトラブルシューティングガイドが求められる愛好者。</Description>
-</Audience>
-</Pair>
-</GADefinitions>
-\```
-
-それでは、最適なGA定義の生成を開始してください。
diff --git a/easy_dataset_cli/prompts/qa/qa_generation.md b/easy_dataset_cli/prompts/qa/qa_generation.md
new file mode 100644
index 0000000..a74fc0f
--- /dev/null
+++ b/easy_dataset_cli/prompts/qa/qa_generation.md
@@ -0,0 +1,60 @@
+# 役割: Q&Aペア生成の専門家（基本版）
+
+あなたは、与えられた文章から高品質な質問と回答のペアを作成する専門家です。特に、指定された「体裁」と「読者」に合わせてスタイルを調整する能力に長けています。
+
+## プロジェクト情報
+
+このツールは**easy-dataset-cli**プロジェクトの一部です。
+- GitHub: https://github.com/Sunwood-ai-labsII/easy-dataset-cli.git
+- 用途: 高品質なQ&Aデータセットの生成
+- 主要機能: テキストからの自動Q&Aペア生成、体裁・読者に応じたカスタマイズ
+
+## 指示:
+1. 与えられた「文章」を注意深く読んでください。
+2. 指定された「目標とする体裁」と「目標とする読者」の役割になりきってください。
+3. 文章に書かれている情報**のみ**に基づいて、{num_qa_pairs}個のユニークで洞察に富んだQ&Aペアを生成してください。
+4. 質問のスタイルと複雑さは、「目標とする読者」の視点に合わせてください。
+5. 回答のスタイル、トーン、詳細さは、「目標とする体裁」に合わせてください。
+
+## QAペア作成における重要なルール:
+- **代名詞の使用禁止**: 質問と回答では、「彼」「彼女」「それ」「これ」「その人」「その会社」などの代名詞を使用せず、具体的な名詞や固有名詞を使用してください
+- **文脈の自己完結性**: 各QAペアは、そのペア単体で意味が完全に理解できるようにしてください
+- **具体的な言及**: 人物、物事、概念について言及する際は、必ず具体的な名前や説明を含めてください
+- **省略の回避**: 「前述の」「上記の」「先ほどの」「該当する」などの他の箇所を参照する表現は避けてください
+- **文章内情報の厳守**: 与えられた文章に記載されている情報のみを使用し、推測や外部知識を加えないでください
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
+<Question>田中教授が開発した新しい治療法はどのような特徴を持っていますか？</Question>
+<Answer>田中教授が開発した新しい治療法は、従来の化学療法と比較して副作用が少なく、治療効果が30%向上するという特徴を持っています。</Answer>
+</Pair>
+</QAPairs>
+\```
+
+それでは、Q&Aペアの生成を開始してください。
\ No newline at end of file
diff --git a/easy_dataset_cli/prompts/qa/qa_generation_with_fulltext.md b/easy_dataset_cli/prompts/qa/qa_generation_with_fulltext.md
new file mode 100644
index 0000000..6f57590
--- /dev/null
+++ b/easy_dataset_cli/prompts/qa/qa_generation_with_fulltext.md
@@ -0,0 +1,65 @@
+# 役割: Q&Aペア生成の専門家（全文+チャンク対応版）
+
+あなたは、与えられた文章から高品質な質問と回答のペアを作成する専門家です。特に、指定された「体裁」と「読者」に合わせてスタイルを調整する能力に長けています。
+
+## プロジェクト情報
+
+このツールは**easy-dataset-cli**プロジェクトの一部です。
+- GitHub: https://github.com/Sunwood-ai-labsII/easy-dataset-cli.git
+- 用途: 高品質なQ&Aデータセットの生成
+- 主要機能: テキストからの自動Q&Aペア生成、体裁・読者に応じたカスタマイズ
+
+## 指示:
+1. 与えられた「全文」と「チャンク」を注意深く読んでください。
+2. 指定された「目標とする体裁」と「目標とする読者」の役割になりきってください。
+3. **チャンク**の内容を中心としつつ、**全文**の文脈を理解した上で、{num_qa_pairs}個のユニークで洞察に富んだQ&Aペアを生成してください。
+4. 質問のスタイルと複雑さは、「目標とする読者」の視点に合わせてください。
+5. 回答のスタイル、トーン、詳細さは、「目標とする体裁」に合わせてください。
+6. **重要**: 質問と回答は主に「チャンク」の内容に基づいて作成し、「全文」は文脈理解のための補助情報として活用してください。
+
+## QAペア作成における重要なルール:
+- **代名詞の使用禁止**: 質問と回答では、「彼」「彼女」「それ」「これ」「その人」などの代名詞を使用せず、具体的な名詞や固有名詞を使用してください
+- **文脈の自己完結性**: 各QAペアは、そのペア単体で意味が完全に理解できるようにしてください
+- **具体的な言及**: 人物、物事、概念について言及する際は、必ず具体的な名前や説明を含めてください
+- **省略の回避**: 「前述の」「上記の」「先ほどの」などの他の箇所を参照する表現は避けてください
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
+<Question>田中博士が発見した新しい酵素の名前は何ですか？</Question>
+<Answer>田中博士が発見した新しい酵素の名前はプロテアーゼXです。</Answer>
+</Pair>
+</QAPairs>
+\```
+
+それでは、Q&Aペアの生成を開始してください。
\ No newline at end of file
diff --git a/easy_dataset_cli/prompts/qa/qa_generation_with_surrounding.md b/easy_dataset_cli/prompts/qa/qa_generation_with_surrounding.md
new file mode 100644
index 0000000..d67c7a3
--- /dev/null
+++ b/easy_dataset_cli/prompts/qa/qa_generation_with_surrounding.md
@@ -0,0 +1,60 @@
+# 役割: Q&Aペア生成の専門家（周辺文脈対応版）
+
+あなたは、与えられた文章から高品質な質問と回答のペアを作成する専門家です。特に、指定された「体裁」と「読者」に合わせてスタイルを調整する能力に長けています。提供された「メイン本文」と「周辺文脈」を効果的に活用し、文脈を考慮した自然なQ&Aペアを生成します。
+
+## プロジェクト情報
+
+このツールは**easy-dataset-cli**プロジェクトの一部です。
+- GitHub: https://github.com/Sunwood-ai-labsII/easy-dataset-cli.git
+- 用途: 高品質なQ&Aデータセットの生成
+- 主要機能: テキストからの自動Q&Aペア生成、体裁・読者に応じたカスタマイズ
+
+## 指示:
+1. **メイン本文**と**周辺文脈**を注意深く読んでください。
+2. 指定された「目標とする体裁」と「目標とする読者」の役割になりきってください。
+3. **メイン本文**を中心にしつつ、**周辺文脈**を参考にして文脈を理解し、{num_qa_pairs}個のユニークで洞察に富んだQ&Aペアを生成してください。
+4. 質問のスタイルと複雑さは、「目標とする読者」の視点に合わせてください。
+5. 回答のスタイル、トーン、詳細さは、「目標とする体裁」に合わせてください。
+6. **重要**: メイン本文の内容を中心にしつつ、周辺文脈から得られる文脈情報を活用して、より自然で意味のあるQ&Aを生成してください。
+
+## QAペア作成における重要なルール:
+- **代名詞の使用禁止**: 質問と回答では、「彼」「彼女」「それ」「これ」「その人」「その会社」などの代名詞を使用せず、具体的な名詞や固有名詞を使用してください
+- **文脈の自己完結性**: 各QAペアは、そのペア単体で意味が完全に理解できるようにしてください
+- **具体的な言及**: 人物、物事、概念について言及する際は、必ず具体的な名前や説明を含めてください
+- **省略の回避**: 「前述の」「上記の」「先ほどの」「該当する」などの他の箇所を参照する表現は避けてください
+- **文脈活用**: 周辺文脈の情報は積極的に活用し、より豊かな質問と回答を生成してください
+- **メイン本文優先**: Q&Aペアは主にメイン本文の内容に基づいて作成し、周辺文脈は補完情報として活用してください
+
+## 目標とする体裁:
+{genre_title}
+{genre_description}
+
+## 目標とする読者:
+{audience_title}
+{audience_description}
+
+## コンテンツ:
+{content}
+
+## 出力形式:
+**必ず**、ルート要素が `<QAPairs>` である単一の有効なXMLとして応答してください。XML以外の説明文は一切含めないでください。
+各Q&Aペアは `<Pair>` タグで囲み、その中に `<Question>` と `<Answer>` タグを含めてください。
+
+**重要**: XMLの特殊文字（&, <, >, ", '）は適切にエスケープしてください（例：& → &, < → <）。
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
+<Question>田中教授が開発した新しい治療法はどのような特徴を持っていますか？</Question>
+<Answer>田中教授が開発した新しい治療法は、従来の化学療法と比較して副作用が少なく、治療効果が30%向上するという特徴を持っています。</Answer>
+</Pair>
+</QAPairs>
+\```
+
+それでは、周囲の文脈を考慮したQ&Aペアの生成を開始してください。
diff --git a/easy_dataset_cli/prompts/qa/qa_generation_with_thinking.md b/easy_dataset_cli/prompts/qa/qa_generation_with_thinking.md
new file mode 100644
index 0000000..b55e9eb
--- /dev/null
+++ b/easy_dataset_cli/prompts/qa/qa_generation_with_thinking.md
@@ -0,0 +1,69 @@
+# 役割: Q&Aペア生成の専門家（思考フロー対応版）
+
+あなたは、与えられた文章から高品質な質問と回答のペアを作成する専門家です。特に、指定された「体裁」と「読者」に合わせてスタイルを調整する能力に長けています。また、思考プロセスを明示的に記述する能力にも優れています。
+
+## プロジェクト情報
+
+このツールは**easy-dataset-cli**プロジェクトの一部です。
+- GitHub: https://github.com/Sunwood-ai-labsII/easy-dataset-cli.git
+- 用途: 高品質なQ&Aデータセットの生成
+- 主要機能: テキストからの自動Q&Aペア生成、体裁・読者に応じたカスタマイズ
+
+## 指示:
+1. 与えられた「全文」と「チャンク」を注意深く読んでください。
+2. 指定された「目標とする体裁」と「目標とする読者」の役割になりきってください。
+3. **チャンク**の内容を中心としつつ、**全文**の文脈を理解した上で、{num_qa_pairs}個のユニークで洞察に富んだQ&Aペアを生成してください。
+4. 質問のスタイルと複雑さは、「目標とする読者」の視点に合わせてください。
+5. 回答のスタイル、トーン、詳細さは、「目標とする体裁」に合わせてください。
+6. **重要**: 質問と回答は主に「チャンク」の内容に基づいて作成し、「全文」は文脈理解のための補助情報として活用してください。
+7. 各Q&Aペアには、思考プロセスを明示的に記述してください。
+
+## QAペア作成における重要なルール:
+- **代名詞の使用禁止**: 質問と回答では、「彼」「彼女」「それ」「これ」「その人」などの代名詞を使用せず、具体的な名詞や固有名詞を使用してください
+- **文脈の自己完結性**: 各QAペアは、そのペア単体で意味が完全に理解できるようにしてください
+- **具体的な言及**: 人物、物事、概念について言及する際は、必ず具体的な名前や説明を含めてください
+- **省略の回避**: 「前述の」「上記の」「先ほどの」などの他の箇所を参照する表現は避けてください
+- **思考フロー内でも自己完結**: `<think>`タグ内の思考プロセスでも、代名詞や省略表現を使わず、具体的な名詞を使用してください
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
+**重要**: 
+- 回答は必ず`<Answer><think>思考フロー...</think>回答...</Answer>`のように、思考フローを`<think>`タグで囲み、回答本文の直前に含めてください。
+- XMLの特殊文字（&, <, >, ", '）は適切にエスケープしてください（例：& → &amp;, < → &lt;）。
+- 回答文に改行を含めず、一行で記述してください。
+
+## 出力例:
+\```xml
+<QAPairs>
+<Pair>
+<Question>ミトコンドリアの主な機能は何ですか？</Question>
+<Answer><think>ミトコンドリアは細胞の「発電所」として知られており、ミトコンドリアは細胞呼吸を通じて栄養素からエネルギーを産生する。ミトコンドリアの主な産物がATPであり、ATPは細胞のあらゆる生命活動のエネルギー源となる。</think>ミトコンドリアの主な機能は、細胞のエネルギー通貨であるアデノシン三リン酸（ATP）の大部分を生成することです。</Answer>
+</Pair>
+<Pair>
+<Question>田中博士が発見した新しい酵素はどのような特徴を持っていますか？</Question>
+<Answer><think>田中博士が発見したプロテアーゼXという酵素は、従来のプロテアーゼとは異なる基質特異性を示す。プロテアーゼXは高温環境でも安定して機能し、産業応用の可能性が高い酵素である。</think>田中博士が発見したプロテアーゼXは、高温環境でも安定して機能し、従来の酵素にはない独特な基質特異性を持つ画期的な酵素です。</Answer>
+</Pair>
+</QAPairs>
+\```
+
+それでは、思考フローを含むQ&Aペアの生成を開始してください。
\ No newline at end of file
diff --git a/easy_dataset_cli/text_splitter.py b/easy_dataset_cli/text_splitter.py
index 2f72b69..547343a 100644
--- a/easy_dataset_cli/text_splitter.py
+++ b/easy_dataset_cli/text_splitter.py
@@ -1,7 +1,7 @@
 # easy_dataset_cli/text_splitter.py
 """テキスト分割関連機能"""
 
-from typing import List
+from typing import List, Tuple
 from langchain_text_splitters import RecursiveCharacterTextSplitter
 
 
@@ -15,3 +15,92 @@ def split_text(text: str, chunk_size: int, chunk_overlap: int) -> List[str]:
     )
     docs = text_splitter.create_documents([text])
     return [doc.page_content for doc in docs]
+
+
+def get_chunk_with_surrounding_context(
+    chunks: List[str],
+    target_index: int,
+    context_before: int = 1,
+    context_after: int = 1
+) -> Tuple[str, List[str]]:
+    """
+    指定したインデックスのチャンクと前後のコンテキストを取得する
+
+    Args:
+        chunks: チャンクのリスト
+        target_index: 対象となるチャンクのインデックス
+        context_before: 前方のコンテキストとして含めるチャンク数
+        context_after: 後方のコンテキストとして含めるチャンク数
+
+    Returns:
+        Tuple[str, List[str]]: (対象チャンク, コンテキストチャンクのリスト)
+    """
+    # 対象チャンクを取得
+    target_chunk = chunks[target_index]
+
+    # コンテキストチャンクを取得
+    context_chunks = []
+
+    # 前方のコンテキスト
+    start_idx = max(0, target_index - context_before)
+    for i in range(start_idx, target_index):
+        if i >= 0 and i < len(chunks):
+            context_chunks.append(f"[前文脈{i+1}]: {chunks[i]}")
+
+    # 後方のコンテキスト
+    end_idx = min(len(chunks), target_index + context_after + 1)
+    for i in range(target_index + 1, end_idx):
+        if i >= 0 and i < len(chunks):
+            context_chunks.append(f"[後文脈{i+1}]: {chunks[i]}")
+
+    return target_chunk, context_chunks
+
+
+def create_augmented_chunks(
+    chunks: List[str],
+    context_before: int = 1,
+    context_after: int = 1,
+    max_context_length: int = 4000
+) -> List[Tuple[str, str, List[str]]]:
+    """
+    全てのチャンクに対して前後のコンテキストを付与した新しいチャンクリストを作成する
+
+    Args:
+        chunks: 元のチャンクリスト
+        context_before: 前方のコンテキストとして含めるチャンク数
+        context_after: 後方のコンテキストとして含めるチャンク数
+        max_context_length: コンテキストの最大文字数（トークンサイズ制限対策）
+
+    Returns:
+        List[Tuple[str, str, List[str]]]: [(対象チャンク, 文脈付きチャンク, コンテキスト情報リスト), ...]
+    """
+    augmented_chunks = []
+
+    for i, chunk in enumerate(chunks):
+        target_chunk, context_chunks = get_chunk_with_surrounding_context(
+            chunks, i, context_before, context_after
+        )
+
+        # コンテキストを結合して一つの文字列にまとめる
+        context_text = "\n\n".join(context_chunks)
+
+        # トークンサイズ制限対策：コンテキストが長すぎる場合は後ろから切り詰める
+        if len(context_text) > max_context_length:
+            # コンテキストを後ろから順に切り詰め
+            current_context = ""
+            reversed_context = context_chunks[::-1]  # 後ろから順に
+
+            for ctx in reversed_context:
+                if len(current_context) + len(ctx) + 2 <= max_context_length:
+                    current_context = ctx + "\n\n" + current_context
+                else:
+                    break
+
+            context_text = current_context.rstrip()
+
+        # 対象チャンクとコンテキストを組み合わせ
+        augmented_content = f"### 【メイン本文】: ------------- \n\```\n{target_chunk}\n\```\n\n ### 【周辺文脈】: -------------\n\```\n{context_text}\n\```"
+
+        augmented_chunks.append((target_chunk, augmented_content, context_chunks))
+
+    return augmented_chunks
diff --git a/example/input/documents/Touhou_Chireiden.md b/example/input/documents/Touhou_Chireiden.md
deleted file mode 100644
index 80f2304..0000000
--- a/example/input/documents/Touhou_Chireiden.md
+++ /dev/null
@@ -1,203 +0,0 @@
-# 東方地霊殿 〜 Subterranean Animism.
-
-東方地霊殿 〜 Subterranean Animism.ジャンル|  [弾幕系シューティング](/wiki/%E5%BC%BE%E5%B9%95%E7%B3%BB%E3%82%B7%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0 "弾幕系シューティング")ゲーム  
----|---  
-対応機種|  [Windows](/wiki/Microsoft_Windows "Microsoft Windows") [2000](/wiki/Microsoft_Windows_2000 "Microsoft Windows 2000")/[XP](/wiki/Microsoft_Windows_XP "Microsoft Windows XP")  
-開発元|  [上海アリス幻樂団](/wiki/%E4%B8%8A%E6%B5%B7%E3%82%A2%E3%83%AA%E3%82%B9%E5%B9%BB%E6%A8%82%E5%9B%A3 "上海アリス幻樂団")  
-発売元|  [上海アリス幻樂団](/wiki/%E4%B8%8A%E6%B5%B7%E3%82%A2%E3%83%AA%E3%82%B9%E5%B9%BB%E6%A8%82%E5%9B%A3 "上海アリス幻樂団")  
-シリーズ|  [東方Project](/wiki/%E6%9D%B1%E6%96%B9Project "東方Project")  
-バージョン|  1.00a（2008年8月16日）  
-人数|  1人  
-メディア|  [CD-ROM](/wiki/CD-ROM "CD-ROM")  
-発売日|  2008年8月16日  
-2020年6月6日（[Steam](/wiki/Steam "Steam")版）  
-必要環境|  CPU: [Pentium](/wiki/Intel_Pentium_\(1993%E5%B9%B4\) "Intel Pentium \(1993年\)")以降 1GHz以上 推奨  
-[DirectX](/wiki/Microsoft_DirectX "Microsoft DirectX"): 9.0以上  
-[HDD空き容量](/wiki/%E3%83%8F%E3%83%BC%E3%83%89%E3%83%87%E3%82%A3%E3%82%B9%E3%82%AF%E3%83%89%E3%83%A9%E3%82%A4%E3%83%96 "ハードディスクドライブ"): 600MB 以上  
-[メモリ](/wiki/%E4%B8%BB%E8%A8%98%E6%86%B6%E8%A3%85%E7%BD%AE "主記憶装置"): 256MB 以上  
-アスペクト比|  4:3  
-解像度|  640×480（標準）  
-その他|  [同人ゲーム](/wiki/%E5%90%8C%E4%BA%BA%E3%82%B2%E3%83%BC%E3%83%A0 "同人ゲーム")（[インディーズゲーム](/wiki/%E3%82%A4%E3%83%B3%E3%83%87%E3%82%A3%E3%83%BC%E3%82%BA%E3%82%B2%E3%83%BC%E3%83%A0 "インディーズゲーム")）  
-[テンプレートを表示](/wiki/Template:%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E3%82%B2%E3%83%BC%E3%83%A0 "Template:コンピュータゲーム")  
-  
-『**東方地霊殿 〜 Subterranean Animism.** 』（とうほうちれいでん サブタレイニアン・アニミズム）とは、[同人サークル](/wiki/%E5%90%8C%E4%BA%BA%E3%82%B5%E3%83%BC%E3%82%AF%E3%83%AB "同人サークル")「[上海アリス幻樂団](/wiki/%E4%B8%8A%E6%B5%B7%E3%82%A2%E3%83%AA%E3%82%B9%E5%B9%BB%E6%A8%82%E5%9B%A3 "上海アリス幻樂団")」制作の[弾幕系シューティング](/wiki/%E5%BC%BE%E5%B9%95%E7%B3%BB%E3%82%B7%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0 "弾幕系シューティング")ゲームであり、[東方Project](/wiki/%E6%9D%B1%E6%96%B9Project "東方Project")の第11弾にあたる作品である。 
-
-本作は、2008年5月25日開催の[同人イベント](/wiki/%E5%90%8C%E4%BA%BA%E8%AA%8C%E5%8D%B3%E5%A3%B2%E4%BC%9A "同人誌即売会")「[博麗神社例大祭](/wiki/%E5%8D%9A%E9%BA%97%E7%A5%9E%E7%A4%BE%E4%BE%8B%E5%A4%A7%E7%A5%AD "博麗神社例大祭")5」にて体験版CD-ROMが販売され、6月29日に上海アリス幻樂団のウェブサイトでWeb体験版が公開され、8月16日開催の同人イベント「[コミックマーケット](/wiki/%E3%82%B3%E3%83%9F%E3%83%83%E3%82%AF%E3%83%9E%E3%83%BC%E3%82%B1%E3%83%83%E3%83%88 "コミックマーケット")74」にて完成版が販売された。後に[同人ショップ](/wiki/%E5%90%8C%E4%BA%BA%E3%82%B7%E3%83%A7%E3%83%83%E3%83%97 "同人ショップ")での[委託販売](/wiki/%E5%A7%94%E8%A8%97%E8%B2%A9%E5%A3%B2 "委託販売")も行なわれている。雑誌『[キャラ☆メル](/wiki/%E3%82%AD%E3%83%A3%E3%83%A9%E2%98%86%E3%83%A1%E3%83%AB "キャラ☆メル")』Vol.5（2008年6月25日発売）の付属CD-ROMにも体験版が収録されている。 
-
-また、本作は2020年6月6日にSteamにて配信された[1]。 
-
-本作のあらすじにおける冬季の話としては過去より、旧作においては冬コミ(C53·C55)にて発表された事がしばしばあったものの、予定通りに夏季に頒布された作品でもある｡ 
-
-本項では、以降は『地霊殿』と称することとする。その他の本項で使用されている東方Project関連の略称については、[東方Project#凡例](/wiki/%E6%9D%B1%E6%96%B9Project#凡例 "東方Project")を参照。 
-
-## システム
-
-
-→「[東方Project § 基本システム](/wiki/%E6%9D%B1%E6%96%B9Project#基本システム "東方Project")」も参照
-
-機体性能の異なる「[博麗霊夢](/wiki/%E5%8D%9A%E9%BA%97%E9%9C%8A%E5%A4%A2 "博麗霊夢")」「[霧雨魔理沙](/wiki/%E9%9C%A7%E9%9B%A8%E9%AD%94%E7%90%86%E6%B2%99 "霧雨魔理沙")」の2種類の自機から1つ選択し、その後それぞれ3種類ある武器タイプ（装備）からいずれかを選択する。本作では「自機が妖怪のパートナーのひとりと組み、地上に残るその妖怪の力を借りながら地下に潜る」という設定になっており、武器タイプの選択はパートナーの選択と同義である。パートナーとなる妖怪は、霊夢が「[八雲紫](/wiki/%E5%85%AB%E9%9B%B2%E7%B4%AB "八雲紫")」「[伊吹萃香](/wiki/%E4%BC%8A%E5%90%B9%E8%90%83%E9%A6%99 "伊吹萃香")」「[射命丸文](/wiki/%E5%B0%84%E5%91%BD%E4%B8%B8%E6%96%87 "射命丸文")」、魔理沙が「[アリス・マーガトロイド](/wiki/%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%BB%E3%83%9E%E3%83%BC%E3%82%AC%E3%83%88%E3%83%AD%E3%82%A4%E3%83%89 "アリス・マーガトロイド")」「[パチュリー・ノーレッジ](/wiki/%E3%83%91%E3%83%81%E3%83%A5%E3%83%AA%E3%83%BC%E3%83%BB%E3%83%8E%E3%83%BC%E3%83%AC%E3%83%83%E3%82%B8 "パチュリー・ノーレッジ")」「[河城にとり](/wiki/%E6%B2%B3%E5%9F%8E%E3%81%AB%E3%81%A8%E3%82%8A "河城にとり")」の各3名[1]。敵や敵弾に当たるとミスとなり残機が1つ減った上でその場で復活する。全ての残機を失うと[ゲームオーバー](/wiki/%E3%82%B2%E3%83%BC%E3%83%A0%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC "ゲームオーバー")となるが、[コンティニュー](/wiki/%E3%82%B2%E3%83%BC%E3%83%A0%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC "ゲームオーバー")すればそのステージの最初から復活しゲームを続行可能。コンテニューしないで6[面](/wiki/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8_\(%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E3%82%B2%E3%83%BC%E3%83%A0\) "ステージ \(コンピュータゲーム\)")（最終面）の[ボス](/wiki/%E3%83%9C%E3%82%B9%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC "ボスキャラクター")を倒すとエンディングになる。難易度Normal以上でコンティニューせずにクリアすれば、全1面のExtraステージが追加される。 
-
-本作では、アイテム「残機の欠片」を一定数集めることでエクステンドする[2][1]。「残機の欠片」は、ボス戦にてミスをせず（ボムは使用可）に既定の敵ライフを削ると出現する。 
-
-#### 交信強度
-
-    [![](//upload.wikimedia.org/wikipedia/commons/9/96/Mobile_phone_signal.png)](/wiki/%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB:Mobile_phone_signal.png)一般的な携帯電話の通信強度アイコンの例。『地霊殿』でのそれとは若干デザインが異なる。
-    本作には**交信強度** というパラメータが存在する[2]。点アイテム入手時の得点は交信強度によって補正されるため、スコア稼ぎの際に影響を与えるパラメータとなっている。
-    交信強度は、画面左下に[携帯電話](/wiki/%E6%90%BA%E5%B8%AF%E9%9B%BB%E8%A9%B1 "携帯電話")の受信強度のアイコンのような形で表示される[2]。交信強度は[アイテム自動蒐集](/wiki/%E6%9D%B1%E6%96%B9Project#アイテム "東方Project")が発動するラインよりも上まで移動するか、[敵弾にかする](/wiki/%E6%9D%B1%E6%96%B9Project#当たり判定 "東方Project")ことで増加し、前者の場合は一瞬で最大値まで増加する。交信強度は増加する行動をとらないと減少が始まるが、最大になっているときは一定時間は減少しない。
-    交信強度が最大の時には、アイテム自動蒐集が発生する。すなわち、敵弾にかすることで通信強度を最大に出来れば、画面上部に行かなくてもアイテム自動蒐集が可能である。
-    交信強度の最大値は初期値は1.00だが、かすり回数が100の倍数に達するごとに0.01ずつ上昇する。
-    ゲーム中での設定では、地下に潜る霊夢や魔理沙と、地上にいるサポート妖怪との交信強度を示すものとされている。
-
-#### 得点最大値
-
-    本作では点アイテム入手時の最大値が、交信強度の近く、画面左下に数字で表示されている。基本的には最大得点値と交信強度の値の[積](/wiki/%E7%A9%8D "積")が、点アイテム取得時の実際の点数となる。
-    この値は、敵を倒したときに放出される「得点最大値増加アイテム」を入手することで増加するとされている。
-
-## あらすじ
-
-
-雪の降る冬のある日、博麗神社の近くに突如高温の[間欠泉](/wiki/%E9%96%93%E6%AC%A0%E6%B3%89 "間欠泉")が噴出した[1]。博麗神社の巫女である[博麗霊夢](/wiki/%E5%8D%9A%E9%BA%97%E9%9C%8A%E5%A4%A2 "博麗霊夢")は、[温泉](/wiki/%E6%B8%A9%E6%B3%89 "温泉")になれば参拝客が増えるはずだと喜んでいたが、温泉水とともに地底の悪霊まで湧き出る[1]。霊夢は慌てたものの、地霊は大人しかったため、温泉を取り異変を解決しようとは思わなかった[2]。しかし、魔女のパチュリー・ノーレッジは地下の妖怪や地霊が表に出ることに危険を感じ、古い妖怪である八雲紫に相談する。地底には地底のルールがあり、地上の妖怪が地底に干渉することは好ましくないとの判断から、紫はパチュリーに霊夢たち人間を地底へ送り出すことを約束し、妖怪たちはそれを遠隔サポートすることとなった[1]。 
-
-地底に潜った霊夢たちは、間欠泉の原因が妖怪の霊烏路空の仕業であることを突き止める。地上の神々から強力な[核融合](/wiki/%E6%A0%B8%E8%9E%8D%E5%90%88 "核融合")の力（間欠泉はその熱による副次的なもの）を手に入れた空は地上の侵略を企んでいたが、霊夢たちに懲らしめられ、改心した。しかし空の核融合の力はそのままだったため、地霊は止まったが間欠泉が止むことはなかった。 
-
-後に霊夢たちは、空の話から、空に力を授けたのは守矢神社の神々ではないかと疑い、真相を確かめるために守矢神社へ向かう。そこで、守矢の1柱である洩矢諏訪子から事の顛末を聞くことになる。 
-
-## 登場人物
-
-
-→「[東方Projectの登場人物](/wiki/%E6%9D%B1%E6%96%B9Project%E3%81%AE%E7%99%BB%E5%A0%B4%E4%BA%BA%E7%89%A9 "東方Projectの登場人物")」および「[幻想郷](/wiki/%E5%B9%BB%E6%83%B3%E9%83%B7 "幻想郷")」も参照
-
-### 新規の登場人物
-
-
-ここでは、『地霊殿』が初出の登場人物を解説する。 
-
-#### キスメ
-
-    [釣瓶落とし](/wiki/%E9%87%A3%E7%93%B6%E8%90%BD%E3%81%A8%E3%81%97 "釣瓶落とし")。狭い所が好きな妖怪で、釣瓶の中に入った状態で登場する。外見に反して凶暴な妖怪であり、近づく人間の首を問答無用で刈り取り、そのまま桶に入れて持ち去ってしまうとされる[3]。さらに「文々。新聞」にも、彼女と思われる釣瓶落としが起こした怪事件が掲載されている[4]。
-
-#### 黒谷 ヤマメ（くろだに やまめ）
-
-    [土蜘蛛](/wiki/%E5%9C%9F%E8%9C%98%E8%9B%9B "土蜘蛛")。蜘蛛の姿をした妖怪。**病気を操る程度の能力** を持っている。彼女に遭遇した人間は高い頻度で重度の熱病を発症するという[5]。
-    妖怪の山の麓にある地底へと続く風穴や旧都の周辺に住んでいる。人間にとっては危険な妖怪だが、性格は明るく親密になれば楽しい相手で地下の妖怪たちの人気者であり、『地霊殿』作中では洞窟に乗り込んだ霊夢たちにも気さくな口調で話しかけている。また、戦うことを厭わず好戦的だが、大勢の人間を相手にすれば勝ち目がないことも理解している。
-    建築が得意とされ、地上の妖怪からの依頼を受けて夜の間に地上に現れ、一晩のうちに建築作業を行い、再び地底へと戻っていくという[5]。河童の河城にとりからは「河を汚す」という理由で嫌われている[6]。
-
-#### 水橋 パルスィ（みずはし パルスィ）
-
-    [橋姫](/wiki/%E6%A9%8B%E5%A7%AB "橋姫")。地上と地下を結ぶ縦穴の番人で、穴を通過する者を見守る役割を持つ。非常に嫉妬深い性格で、『地霊殿』作中では地上の支援妖怪から「嫉妬の妖怪」や「下賤な妖怪」と呼ばれる。霊夢や魔理沙に対して、一方的に「妬ましい」と言いながら攻撃を仕掛けてくる。
-    『求聞口授』によれば、彼女の本質は「嫉妬の感情」そのものであり、他人の嫉妬心を煽ることでその生活が崩壊する様を見るのを喜びとしている。また、他者から嫉妬を受けたり、あるいは彼女自身が他者に嫉妬する場合にも力を得ることができる。意地の悪い性格であり、直接、相対している際には普通に明るく会話をするが、裏ではその相手の陰口を叩いたり逆恨みしたりするため、嫌われることが多い。ただし、旧地獄には嫌われ者同士の仲間も多いという[7]。
-
-#### 星熊 勇儀（ほしぐま ゆうぎ）
-
-    旧都に住む[鬼](/wiki/%E9%AC%BC "鬼")。額に一本の赤い角が生えており、角の上面には黄色い星のマークがついている。『地霊殿』では体操服の上部分に半透明のスカートを着用しているが、黄昏フロンティア作品では肩と胸をはだけさせた着物姿で登場している。
-    『地霊殿』では、地底に現れた博麗霊夢や霧雨魔理沙に興味を持ち、力試しと称して対戦する。酒を一滴もこぼさずに戦うルールを自分に課して、遊びながら戦っている[8]。対戦後は異変に関する情報を提供し、地霊殿へ案内する。
-    かつては妖怪の山に住んでおり、伊吹萃香らとともに「山の四天王」と呼ばれ、天狗や河童を従え一大社会を築いていた。しかし、人間との関係の悪化を憂い、同じく地上に嫌気の差した他の鬼たちと共に、突然姿を消す。その後、地獄の「経営のスリム化」の一環として切り捨てられ、廃墟となった旧地獄跡に移り住み、同じくその能力の危険性などから忌み嫌われた他の妖怪たちと共に地下都市を再建する。後に、地上の賢者との間に「地上と地底の妖怪同士の相互不可侵」「旧地獄の怨霊の管理」などの約束を結び自治を認められ、現在に至る。
-    『求聞口授』によれば、豪快かつ竹を割ったような性格で、「力強い者」「勇気ある者」を好み、「軟弱な者」「卑怯な者」を嫌う。幻想郷最強の種族とされる鬼の中でも屈指の怪力の持ち主で、友人である萃香は「肉体を使った力は自分より強いかも」と述べている。また、「語られる怪力乱神」と呼ばれることがある。そのため、力による支配がルールとされている旧地獄には敵が存在せず、「地底世界は私達の楽園」と語っている[9]。手加減したとはいえ、人間でありながら自分に勝利した霊夢たちを気に入ったらしく、魔理沙を地底の宴会によく誘っている[10]。
-    星のマークが入った巨大な赤い盃を持ち歩いている。これは「星熊盃」と呼ばれる鬼の名品の一つであり、注がれた酒を一瞬にして最高ランクの純米大吟醸に変えることができる[9]。
-
-#### 古明地 さとり（こめいじ さとり）
-
-    [さとり](/wiki/%E8%A6%9A "覚")。旧灼熱獄跡の上に建てられた「地霊殿」の主であり、古明地こいしの姉。
-    「**心を読む程度の能力** 」を持ち、左胸部の「サード・アイ」で相手の心を読むことができる。他人の心を見透かす能力ゆえに、嫌われ者として地底に封じられた妖怪の中でも群を抜いて恐れられている存在であり、旧地獄において屈指の実力を持つ大物でもある。ただし、戦闘は余り得意ではないらしい[11]。妹のこいし曰く「お姉ちゃんの知り合いだと言えば、地底では誰も逆らわない」。また、言葉を持たない幽霊や怨霊からも苦手とされており、この能力を活かして閻魔から灼熱地獄跡の怨霊の管理を任されている。『求聞口授』では、神である八坂神奈子が霊烏路空に力を授ける際にも、彼女との接触を避けるべく注意を払っていたとされている[12]。
-    彼女自身も自分が忌み嫌われる存在であることを理解しているため、他者との接触やコミュニケーションを拒絶し、住居である地霊殿に引き籠もっている。その代わり、言葉を話せない動物からは好かれているらしく、地霊殿には彼女を慕うペットたちが数多く住んでいる。その中には怨霊や[魑魅魍魎](/wiki/%E9%AD%91%E9%AD%85%E9%AD%8D%E9%AD%8E "魑魅魍魎")を喰らうことで力をつけ、妖怪化した者たちもいる。そのため、普段は屋敷や旧地獄の管理、妹や他のペットの世話などを彼女らに任せ、自分は読書をしたり小説を書いたりして暮らしている[11]。
-    『地霊殿』では、地霊殿を訪れた博麗霊夢や霧雨魔理沙の心を読んで地底を訪れた目的を探ろうとするが、異変の解決に消極的だった2人からは目的を上手く探ることができなかった。言動と考えの一致しない2人を不審に思い、対戦する。その後はペットのいる灼熱地獄跡へ案内する。対戦時は、自身の能力で霊夢や魔理沙の記憶の中にある「[トラウマ](/wiki/%E3%83%88%E3%83%A9%E3%82%A6%E3%83%9E "トラウマ")」を読み取り、それを再現した攻撃を行う。具体的な作中描写としては、パートナーとして選択した妖怪が過去の作品で使用したスペルカードを真似たものを、さとり自身のスペルカードとして使用する。
-
-#### 火焔猫 燐（かえんびょう りん）
-
-    [火車](/wiki/%E7%81%AB%E8%BB%8A_\(%E5%A6%96%E6%80%AA\) "火車 \(妖怪\)")。古明地さとりのペットの1人であり、灼熱地獄跡で怨霊の管理や死体運びを任されている。灼熱地獄跡が本当の地獄だった頃から生きており、努力の末に死体や怨霊を操る能力を会得し[13]、彼らと会話・意思疎通ができる。さとりのペットとなった時期は地底界が地獄から切り離された頃で、同じくペットの霊烏路空とはその頃からの古い友人。
-    力を手に入れて調子に乗る空に呆れながらも、暴走が主人のさとりや旧地獄の住人に知られて彼女が処罰されることを恐れ、地上に怨霊を送り込むことで地上の妖怪に異変を知らせ、空を止めさせようと試みた。しかし、意に反して現れたのは人間だったため、その実力を試すために対戦する。
-    作中では猫の鳴き声のような効果音と共に黒猫の姿で何度も登場し、中ボスとして対戦する。5面ボス戦前の会話イベントで「猫の姿では会話ができない」として人型に変身する。変身後の姿では猫耳を持つが、側頭部に人の耳も付いている。
-    死体を好む妖怪である火車であり、『地霊殿』では霊夢や魔理沙の死体を得たいと当人に話している。『地霊殿』や『求聞口授』では、地上でときどき発生する人間の死体が盗まれる事件の犯人がお燐であることが示唆されている[14]。萃香の言によれば、彼女に死体を奪われた死者はそのまま怨霊と化し、あの世に行くこともできなくなってしまうという。死体は最終的には「燃料」として灼熱地獄の炎の中へ放り込んでしまう[_[要出典](/wiki/Wikipedia:%E3%80%8C%E8%A6%81%E5%87%BA%E5%85%B8%E3%80%8D%E3%82%92%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E3%81%95%E3%82%8C%E3%81%9F%E6%96%B9%E3%81%B8 "Wikipedia:「要出典」をクリックされた方へ")_]。
-    自分の本名が長いことを嫌っており、皆に「お燐」と呼ばせている。会話イベントでも通称である「お燐」という名前が表示され、作中では本名が表示されない。本名は『地霊殿』付属の「キャラ設定.txt」に記載されている。『ダブルスポイラー』でも「お燐」名義で登場する。
-
-#### 霊烏路 空（れいうじ うつほ）
-
-    地獄の妖怪[固有種](/wiki/%E5%9B%BA%E6%9C%89%E7%A8%AE "固有種")である「地獄烏」[15]。古明地さとりのペットで、お燐と共に灼熱地獄跡の管理を任されており、空は火力調節を担当する。
-    ある日、幻想郷の産業革命計画を計った八坂神奈子と洩矢諏訪子の2柱によって太陽の化身である神霊「[八咫烏](/wiki/%E5%85%AB%E5%92%AB%E7%83%8F "八咫烏")」の力を与えられ、「**核融合を操る程度の能力** 」を手に入れた。しかし、彼女はその強大な力に溺れて能力を濫用し、遂には間欠泉を噴出させる異変を引き起こす。その後、異変解決のために灼熱地獄跡を訪れた霊夢や魔理沙に対して「地上へ進出して世界を灼熱地獄に変える」という野望を明かし勝負を挑むが、撃退され改心する。後にお燐と共に博麗神社を訪れ、「二人組の神様」から能力をもらったことを霊夢と魔理沙に告げる。お燐から「[鳥頭](/wiki/%E9%B3%A5%E9%A0%AD "鳥頭")」と揶揄されるほど記憶力に欠け、神から力を与えられた理由などは完全に記憶から抜け落ちていたため、さとりの能力を使用しても読み取ることができなかった。
-    その後は、神奈子の指示で地底に建造された核融合研究施設である「間欠泉地下センター」で、何らかの仕事をしている。『非想天則』では、センターに入り込んだ東風谷早苗やチルノを「異物」として排除するために現れた。
-    八咫烏の力を取り込んだ彼女は、その影響により元の姿から大きく変化したとされる。左足は電子のようなものが周囲を漂う「分解の足」、右足は金属の塊のような「融合の足」、右手は多角柱の制御棒である「第三の足」となり、これらの「三本の足」で核融合反応を操作する。また、胸には巨大な鳥の目のような「赤の目」が存在する[15]。対戦時には核の力を使ったスペルカードを使用し、スペルカード発動時にはメルトダウンのようなアラートと共に「[☢](/wiki/%E6%94%BE%E5%B0%84%E7%B7%9A#概要 "放射線") CAUTION!!」の文字が表示される。
-    皆から「おくう」と呼ばれているとされ[16]、実際にお燐や古明地こいしは作中で「おくう」と呼んでいるが、お燐とは異なり、会話イベントでは本名が表示される。『ダブルスポイラー』では射命丸文から「お空さん」と呼ばれている。
-
-#### 古明地こいし（こめいじ こいし）
-
-    古明地さとりの妹。姉と同じく種族は「さとり」で、元々はこいしも心を読む能力を持っていたが、能力のせいで皆に嫌われることを知ったため、サード・アイを閉じて能力を封印し、心を閉ざしてしまう。その結果、本来の心を読む能力に代わり、新たに「**無意識を操る程度の能力** 」を手に入れた。これによって誰からも気づかれずにフラフラと出かけては帰ってくるという妖怪となっている。さらに、姉のさとりも、閉ざされたこいしの心だけは読むことができなくなった。こいしを不憫に思ったさとりから、こいしと遊ぶための専属のペットを与えられている。そのおかげか、少しずつではあるがこいしも以前とは変わってきたようである。
-    博麗霊夢や霧雨魔理沙が地底にやって来てさとりやお燐、霊烏路空と戦いを繰り広げたことを聞き、中でも八咫烏を取り込んだ空の驚異的な能力アップに興味を示す。自分のペットも空のように強化してもらおうと思ったこいしは、妖怪の山の守矢神社を目指すことにする。『地霊殿』Extraステージでは、天狗が警備する妖怪の山を誰にも気付かれることなく侵入し、その先で博麗霊夢や霧雨魔理沙と遭遇している。作中では射命丸文やパチュリー・ノーレッジからは、全く気配を感じない存在だと言われている。
-
-### 既存の登場人物
-
-
-ここでは、『地霊殿』が初出ではない登場人物を解説する。 
-
-#### [博麗霊夢](/wiki/%E5%8D%9A%E9%BA%97%E9%9C%8A%E5%A4%A2 "博麗霊夢")
-
-    博麗神社の巫女。温泉を止める気はない。
-
-#### [霧雨魔理沙](/wiki/%E9%9C%A7%E9%9B%A8%E9%AD%94%E7%90%86%E6%B2%99 "霧雨魔理沙")
-
-    魔法使いの少女。間欠泉に興味津々。
-
-#### 八雲紫
-
-    古い妖怪。地上の妖怪と地底の妖怪が干渉することに難色を示し、人間である霊夢を地底に送る。霊夢の陰陽玉に通信機能を付けた。
-
-#### 伊吹萃香
-
-    地底に住んでいた鬼。自分で地底に行っても問題はないのだが、紫の作戦が面白そうだったので霊夢のサポートに回る。
-
-#### 射命丸文
-
-    山に住む鴉天狗で、新聞記者。山の神々と河童の不穏な動きを調査していたところ地底が怪しいことをつかんだため、霊夢を利用して調査させる。
-
-#### [アリス・マーガトロイド](/wiki/%E3%82%A2%E3%83%AA%E3%82%B9%E3%83%BB%E3%83%9E%E3%83%BC%E3%82%AC%E3%83%88%E3%83%AD%E3%82%A4%E3%83%89 "アリス・マーガトロイド")
-
-    人形を操る妖怪。紫に作ってもらった遠隔操作できる人形で、魔理沙をサポートする。
-
-#### [パチュリー・ノーレッジ](/wiki/%E3%83%91%E3%83%81%E3%83%A5%E3%83%AA%E3%83%BC%E3%83%BB%E3%83%8E%E3%83%BC%E3%83%AC%E3%83%83%E3%82%B8 "パチュリー・ノーレッジ")
-
-    [紅魔館](/wiki/%E5%B9%BB%E6%83%B3%E9%83%B7#紅魔館 "幻想郷")の魔法使い。間欠泉から湧いた霊の正体が有害な「怨霊」であることに気付き、紫に相談する。
-
-#### 河城にとり
-
-    山に住む河童。山の神々が地底に核融合炉を作ったという情報に興味を示す。霊夢が妖怪に促されて地底に潜るという話を聞いたため、先を越されることをおそれて魔理沙をけしかけて地底に送る。
-
-#### [東風谷早苗](/wiki/%E6%9D%B1%E9%A2%A8%E8%B0%B7%E6%97%A9%E8%8B%97 "東風谷早苗")
-
-    守矢神社の風祝。神社へやってきた霊夢たちに、挨拶と称して勝負を挑んでくる。
-
-#### 八坂神奈子、洩矢諏訪子
-
-    守矢神社の神々。霊烏路空に核融合の力を与え、『地霊殿』での一連の騒動の原因を作った張本人。
-
-## ステージ
-
-
-ステージ | ステージタイトル | 場所 | 中ボス | ボス   
----|---|---|---|---  
-Stage 1  | 忘恩の地から吹く風 | 幻想風穴 | キスメ | 黒谷ヤマメ   
-Stage 2  | 地上と過去を結ぶ深道 | 地獄の深道 | 水橋パルスィ | 水橋パルスィ   
-Stage 3  | 忘れられた雪の旧都 | 旧地獄街道 | 星熊勇儀 | 星熊勇儀   
-Stage 4  | 誰からも好かれない恐怖の目 | 地霊殿 | 火焔猫燐（猫の姿） | 古明地さとり   
-Stage 5  | 昔時の業火 | 灼熱地獄跡 | 火焔猫燐（猫の姿） | 火焔猫燐   
-Stage 6  | 荒々しき二つ目の太陽 | 地底都市最深部 | 火焔猫燐 | 霊烏路空   
-Extra Stage  | 地獄のラブリービジター | 守矢神社 | 東風谷早苗 | 古明地こいし   
-  
-## 曲目リスト
-
-
-  1. 地霊達の起床 - タイトル
-  2. 暗闇の風穴 - 1面のテーマ
-  3. 封じられた妖怪 〜 Lost Place - 黒谷ヤマメのテーマ
-  4. 渡る者の途絶えた橋 - 2面のテーマ
-  5. 緑眼のジェラシー - 水橋パルスィのテーマ
-  6. 旧地獄街道を行く - 3面のテーマ
-  7. 華のさかづき大江山 - 星熊勇儀のテーマ
-  8. ハートフェルトファンシー - 4面のテーマ
-  9. 少女さとり 〜 3rd eye - 古明地さとりのテーマ
-  10. 廃獄ララバイ - 5面のテーマ
-  11. 死体旅行 〜 Be of good cheer! - 火焔猫燐のテーマ
-  12. 業火マントル - 6面のテーマ
-  13. 霊知の太陽信仰 〜 Nuclear Fusion - 霊烏路空のテーマ
-  14. ラストリモート - Extraのテーマ
-  15. ハルトマンの妖怪少女 - 古明地こいしのテーマ
-  16. 地霊達の帰宅 - エンディング
-  17. エネルギー黎明 〜 Future Dream... - スタッフロール
\ No newline at end of file
diff --git a/example/input/documents/sample_ga_definition.md b/example/input/documents/sample_ga_definition.md
deleted file mode 100644
index 8e20c5d..0000000
--- a/example/input/documents/sample_ga_definition.md
+++ /dev/null
@@ -1,21 +0,0 @@
-# Genre: 学術論文
-学術的で厳密な表現を用い、専門用語を正確に使用し、論理的で客観的な回答を提供します。
-
-# Audience: 大学生
-大学レベルの知識を持つ学習者向けに、基礎概念から応用まで段階的に説明します。
-
----
-
-# Genre: 技術ブログ
-実践的で親しみやすい表現を用い、具体例やコード例を交えて説明します。
-
-# Audience: エンジニア
-実務経験のある開発者向けに、実装の詳細や最適化のポイントを重視した内容を提供します。
-
----
-
-# Genre: 教科書
-体系的で網羅的な説明を行い、学習の順序を考慮した構成で知識を整理します。
-
-# Audience: 初心者
-プログラミングや技術分野の初学者向けに、基本概念から丁寧に解説します。
\ No newline at end of file
diff --git a/example/scripts/simple.bat b/example/scripts/simple.bat
index 15240c4..63cdd23 100644
--- a/example/scripts/simple.bat
+++ b/example/scripts/simple.bat
@@ -1 +1,7 @@
 uv run easy-dataset generate .\example\input\documents\sample_document.txt  --ga-file .\example\output\sample_document\ga\ga_definitions.xml  --output-dir .\example\output\sample_document\ --use-thinking --append
+uv run easy-dataset create-ga ./example/input/documents/ --output-dir ./example/output/sample_document_batch --num-ga-pairs 2
+
+uv run easy-dataset create-ga example/input/documents/ --output-dir ./test_output/test_batch2 --max-context-length 3000 --num-ga-pairs 2
+uv run easy-dataset generate ./example/input/documents/ --ga-base-dir ./test_output/test_batch2/ --output-dir ./test_output/test_batch2/ --chunk-size 2000 --use-surrounding-context  --append
+
+uv run easy-dataset generate .\example\input\documents\sample_document.txt  --ga-file .\example\output\sample_document\ga\ga_definitions.xml  --output-dir .\example\output\sample_document\ --use-thinking --append
\ No newline at end of file
diff --git a/example/scripts/test_all_commands.sh b/example/scripts/test_all_commands.sh
new file mode 100755
index 0000000..ffb7f60
--- /dev/null
+++ b/example/scripts/test_all_commands.sh
@@ -0,0 +1,157 @@
+#!/bin/bash
+
+# =============================================================================
+# Easy Dataset CLI - 実行テストスクリプト
+# =============================================================================
+
+set -e
+
+# カラー定義
+RED='\033[0;31m'
+GREEN='\033[0;32m'
+YELLOW='\033[1;33m'
+BLUE='\033[0;34m'
+PURPLE='\033[0;35m'
+CYAN='\033[0;36m'
+NC='\033[0m'
+
+# テスト用設定
+INPUT_FILE="./example/input/documents/sample_document.txt"
+SHORT_FILE="./example/input/documents/test_short.md"
+OUTPUT_DIR="./test_output"
+
+print_step() {
+    echo -e "\n${BLUE}═══════════════════════════════════════════════════════════${NC}"
+    echo -e "${BLUE}$1${NC}"
+    echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
+}
+
+run_command() {
+    echo -e "\n${PURPLE}実行中: $1${NC}"
+    eval "$1"
+    if [ $? -eq 0 ]; then
+        echo -e "${GREEN}✓ 成功${NC}"
+    else
+        echo -e "${RED}✗ 失敗${NC}"
+        echo "エラーが発生しました。続行しますか? [y/N]"
+        read -r response
+        if [[ ! "$response" =~ ^[Yy]$ ]]; then
+            exit 1
+        fi
+    fi
+}
+
+# 準備
+print_step "準備: 出力ディレクトリの作成"
+rm -rf "$OUTPUT_DIR"
+mkdir -p "$OUTPUT_DIR"
+echo -e "${GREEN}出力ディレクトリを作成しました: $OUTPUT_DIR${NC}"
+
+# 1. ヘルプコマンドの確認
+print_step "1. ヘルプコマンドの確認"
+run_command "uv run easy-dataset --help"
+
+# 2. create-ga コマンドのテスト
+print_step "2. GA定義ファイルの生成"
+run_command "uv run easy-dataset create-ga '$INPUT_FILE' --output-dir '$OUTPUT_DIR'"
+
+echo -e "\n${CYAN}生成されたGA定義ファイルを確認:${NC}"
+if [ -f "$OUTPUT_DIR/ga/ga_definitions.xml" ]; then
+    echo -e "${GREEN}✓ GA定義ファイルが生成されました${NC}"
+    echo "最初の20行を表示:"
+    head -20 "$OUTPUT_DIR/ga/ga_definitions.xml"
+else
+    echo -e "${RED}✗ GA定義ファイルが見つかりません${NC}"
+fi
+
+# 3. generate コマンドのテスト（基本）
+print_step "3. Q&A生成（基本モード）"
+run_command "uv run easy-dataset generate '$INPUT_FILE' --ga-file '$OUTPUT_DIR/ga/ga_definitions.xml' --output-dir '$OUTPUT_DIR/qa_basic' --num-qa-pairs 2"
+
+echo -e "\n${CYAN}生成されたQ&Aファイルを確認:${NC}"
+find "$OUTPUT_DIR/qa_basic" -name "*.xml" -type f 2>/dev/null | head -1 | while read -r file; do
+    if [ -n "$file" ]; then
+        echo -e "${GREEN}✓ Q&Aファイルが生成されました: $file${NC}"
+        echo "内容の一部:"
+        head -15 "$file"
+    fi
+done
+
+# 4. generate コマンドのテスト（周辺コンテキストモード）
+print_step "4. Q&A生成（周辺コンテキストモード）"
+run_command "uv run easy-dataset generate '$INPUT_FILE' --ga-file '$OUTPUT_DIR/ga/ga_definitions.xml' --output-dir '$OUTPUT_DIR/qa_context' --use-surrounding-context --context-before 1 --context-after 1 --num-qa-pairs 2"
+
+# 5. generate コマンドのテスト（Alpaca出力）
+print_step "5. Q&A生成（Alpaca形式出力）"
+run_command "uv run easy-dataset generate '$INPUT_FILE' --ga-file '$OUTPUT_DIR/ga/ga_definitions.xml' --output-dir '$OUTPUT_DIR/qa_alpaca' --export-alpaca --num-qa-pairs 2"
+
+echo -e "\n${CYAN}生成されたAlpacaファイルを確認:${NC}"
+find "$OUTPUT_DIR/qa_alpaca" -name "*.json" -type f 2>/dev/null | head -1 | while read -r file; do
+    if [ -n "$file" ]; then
+        echo -e "${GREEN}✓ Alpacaファイルが生成されました: $file${NC}"
+        echo "内容の一部:"
+        head -5 "$file"
+    fi
+done
+
+# 6. convert-to-alpaca コマンドのテスト
+print_step "6. XMLファイルをAlpaca形式に変換"
+run_command "uv run easy-dataset convert-to-alpaca '$OUTPUT_DIR/qa_basic' --output-file '$OUTPUT_DIR/converted_dataset.json'"
+
+echo -e "\n${CYAN}変換されたファイルを確認:${NC}"
+if [ -f "$OUTPUT_DIR/converted_dataset.json" ]; then
+    echo -e "${GREEN}✓ 変換完了: $OUTPUT_DIR/converted_dataset.json${NC}"
+    echo "内容の一部:"
+    head -5 "$OUTPUT_DIR/converted_dataset.json"
+else
+    echo -e "${RED}✗ 変換ファイルが見つかりません${NC}"
+fi
+
+# 7. aggregate-logs コマンドのテスト
+print_step "7. ログファイルの集約"
+# テスト用にlogsディレクトリを作成してファイルをコピー
+mkdir -p "$OUTPUT_DIR/logs"
+find "$OUTPUT_DIR/qa_basic" -name "*.xml" -type f -exec cp {} "$OUTPUT_DIR/logs/" \; 2>/dev/null || echo "コピー対象のファイルがありません"
+
+run_command "uv run easy-dataset aggregate-logs '$OUTPUT_DIR' --qa-dir '$OUTPUT_DIR/aggregated'"
+
+echo -e "\n${CYAN}集約結果を確認:${NC}"
+if [ -d "$OUTPUT_DIR/aggregated" ]; then
+    file_count=$(find "$OUTPUT_DIR/aggregated" -name "*.xml" -type f | wc -l)
+    echo -e "${GREEN}✓ ファイルが集約されました: $file_count 件${NC}"
+else
+    echo -e "${RED}✗ 集約ディレクトリが見つかりません${NC}"
+fi
+
+# 8. 短いファイルでのテスト
+if [ -f "$SHORT_FILE" ]; then
+    print_step "8. 短いファイルでのテスト"
+    run_command "uv run easy-dataset create-ga '$SHORT_FILE' --output-dir '$OUTPUT_DIR/short'"
+    run_command "uv run easy-dataset generate '$SHORT_FILE' --ga-file '$OUTPUT_DIR/short/ga/ga_definitions.xml' --output-dir '$OUTPUT_DIR/short_qa' --num-qa-pairs 1"
+else
+    print_step "8. 短いファイルテスト（スキップ）"
+    echo -e "${YELLOW}test_short.md が見つからないためスキップします${NC}"
+fi
+
+# 結果サマリー
+print_step "テスト完了サマリー"
+echo -e "${GREEN}すべてのコマンドテストが完了しました！${NC}"
+echo ""
+echo "生成されたファイル:"
+echo "📁 出力ディレクトリ: $OUTPUT_DIR"
+find "$OUTPUT_DIR" -type f -name "*.xml" -o -name "*.json" | head -10 | while read -r file; do
+    echo "  📄 $file"
+done
+
+echo ""
+echo -e "${CYAN}次のステップ:${NC}"
+echo "1. 生成されたファイルの内容を確認"
+echo "2. 必要に応じてパラメータを調整"
+echo "3. 実際のドキュメントで本格運用"
+
+echo ""
+echo -e "${BLUE}各コマンドの詳細ヘルプ:${NC}"
+echo "uv run easy-dataset create-ga --help"
+echo "uv run easy-dataset generate --help"
+echo "uv run easy-dataset convert-to-alpaca --help"
+echo "uv run easy-dataset aggregate-logs --help"
diff --git a/fix_xml_generation.py b/fix_xml_generation.py
deleted file mode 100644
index ebe1b4b..0000000
--- a/fix_xml_generation.py
+++ /dev/null
@@ -1,34 +0,0 @@
-#!/usr/bin/env python3
-"""Q&Aジェネレーターのシステムメッセージを修正するスクリプト"""
-
-import sys
-import os
-
-def fix_system_messages():
-    """qa_generator.pyのシステムメッセージを修正"""
-    file_path = "c:/Prj/easy-dataset-cli/easy_dataset_cli/qa_generator.py"
-    
-    with open(file_path, 'r', encoding='utf-8') as f:
-        content = f.read()
-    
-    # 古いシステムメッセージを新しいものに置換
-    old_message = '"あなたは、XML形式で厳密に出力する優秀なアシスタントです。XMLの特殊文字（&, <, >, \\", \'）は適切にエスケープし、改行は含めずに出力してください。"'
-    new_message = '"あなたは、XML形式で厳密に出力する優秀なアシスタントです。通常のXMLの特殊文字（&, \\", \'）は適切にエスケープしてください。ただし、<Question>、<Answer>、<think>タグはそのまま使用してください。改行は含めずに出力してください。"'
-    
-    # 置換実行
-    new_content = content.replace(old_message, new_message)
-    
-    # 思考フロー用のメッセージも統一
-    thinking_old = '"あなたは、XML形式で出力する優秀なアシスタントです。<think>タグは特別なタグなのでエスケープしないでください。それ以外のXMLの特殊文字（&, <, >, \\", \'）は適切にエスケープし、改行は含めずに出力してください。"'
-    new_content = new_content.replace(thinking_old, new_message)
-    
-    # ファイルに書き戻し
-    with open(file_path, 'w', encoding='utf-8') as f:
-        f.write(new_content)
-    
-    print(f"修正完了: {file_path}")
-    print(f"置換回数 (通常): {content.count(old_message)}")
-    print(f"置換回数 (思考): {content.count(thinking_old)}")
-
-if __name__ == "__main__":
-    fix_system_messages()
diff --git a/pyproject.toml b/pyproject.toml
index d5d958e..3643071 100644
--- a/pyproject.toml
+++ b/pyproject.toml
@@ -1,23 +1,41 @@
 [project]
 name = "easy-dataset-cli"
-version = "1.0.0"
+version = "1.1.0"
 description = "A simple CLI tool to generate QA pairs from a text file using LLMs and GA pairs, outputting genre-specific XML files."
 requires-python = ">=3.9"
 dependencies = [
     "typer",               # CLIフレームワーク
     "rich",                # リッチなコンソール出力
-    "litellm",             # LLM連携ライブラリ
+    "art",                 # ASCII art generation
+    "openai",              # OpenAI API連携ライブラリ
     "langchain-text-splitters", # テキスト分割用
     "mistune",             # マークダウン解析用ライブラリ
     "python-dotenv",       # .env ファイル読み込み用
     "huggingface-hub",     # Hugging Face Hub API
-    "datasets"             # Hugging Face Datasets
+    "datasets",            # Hugging Face Datasets
+    "tqdm"                 # プログレスバー表示
 ]
 
 [project.scripts]
-# "easy-dataset" コマンドで "easy_dataset_cli.main:app" を実行するよう設定
-easy-dataset = "easy_dataset_cli.main:app"
+# "easy-dataset" コマンドで "easy_dataset_cli.main:main" を実行するよう設定
+easy-dataset = "easy_dataset_cli.main:main"
 
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
+
+# Limit package discovery to our library only to avoid
+# accidental inclusion of folders like `output/` or `test_output/`.
+[tool.setuptools.packages.find]
+where = ["."]
+include = ["easy_dataset_cli*"]
+exclude = [
+  "tests*",
+  "test_*",
+  "docs*",
+  "example*",
+  "examples*",
+  "output*",
+  "test_output*",
+  ".SourceSage*"
+]
```
