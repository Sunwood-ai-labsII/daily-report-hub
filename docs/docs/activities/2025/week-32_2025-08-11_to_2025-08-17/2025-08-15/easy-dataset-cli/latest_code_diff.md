# 🔄 Latest Code Changes

```diff
diff --git a/README.md b/README.md
index 0946c9a..17cd67d 100644
--- a/README.md
+++ b/README.md
@@ -77,6 +77,22 @@ uv run easy-dataset generate .\example\input\documents\sample_document.txt \
   --export-alpaca
 \```
 
+#### 思考フロー付きQ&Aの生成
+\```bash
+# 思考フローを含むQ&Aペアを生成
+uv run easy-dataset generate .\example\input\documents\sample_document.txt \
+  --ga-file .\example\output\sample_document\ga\ga_definitions.xml \
+  --output-dir .\example\output\sample_document\ \
+  --use-thinking
+
+# 思考フローと全文コンテキストを併用して生成
+uv run easy-dataset generate .\example\input\documents\sample_document.txt \
+  --ga-file .\example\output\sample_document\ga\ga_definitions.xml \
+  --output-dir .\example\output\sample_document\ \
+  --use-thinking \
+  --use-fulltext
+\```
+
 #### Hugging Face Hubへの直接アップロード
 \```bash
 # 環境変数でトークンを設定
@@ -130,6 +146,8 @@ Options:
   -m, --model TEXT         Q&Aペアの生成に使用するLLMモデル [default: openrouter/openai/gpt-4o]
   --chunk-size INTEGER     テキストチャンクの最大サイズ [default: 2000]
   --chunk-overlap INTEGER  チャンク間のオーバーラップサイズ [default: 200]
+  -f, --use-fulltext       全文をコンテキストとして含めてQA生成を行います。より文脈を理解したQAが生成されますが、処理時間とコストが増加します。
+  -T, --use-thinking       各Q&Aペアに思考プロセスを追加して生成します。より深い理解と説明が可能になりますが、処理時間とコストが増加します。
   -h, --help               Show this message and exit
 \```
 
diff --git a/easy_dataset_cli/alpaca_converter.py b/easy_dataset_cli/alpaca_converter.py
index 0a148ea..3e31713 100644
--- a/easy_dataset_cli/alpaca_converter.py
+++ b/easy_dataset_cli/alpaca_converter.py
@@ -31,8 +31,7 @@ def xml_to_alpaca_format(xml_file_path: Path) -> List[Dict[str, str]]:
                 audience = audience_elem.text or ""
                 question = question_elem.text or ""
                 answer = answer_elem.text or ""
-                
-                # アルパカ形式に変換
+                # Answerタグの内容をそのままoutputに入れる（<think>...</think>含む）
                 alpaca_entry = {
                     "instruction": question,
                     "input": "",  # アルパカ形式では通常空文字
diff --git a/easy_dataset_cli/core.py b/easy_dataset_cli/core.py
index 056452b..b308563 100644
--- a/easy_dataset_cli/core.py
+++ b/easy_dataset_cli/core.py
@@ -9,10 +9,11 @@ from .ga_parser import (
 from .qa_generator import (
     generate_qa_for_chunk_with_ga,
     generate_qa_for_chunk_with_ga_and_fulltext,
+    generate_qa_for_chunk_with_ga_and_thinking,
     generate_ga_definitions
 )
 from .text_splitter import split_text
-from .xml_utils import convert_to_xml_by_genre
+from .xml_utils import convert_to_xml_by_genre, load_existing_xml_file, aggregate_logs_xml_to_qa
 from .file_utils import (
     create_output_directories,
     save_ga_definitions_by_genre,
@@ -33,6 +34,7 @@ __all__ = [
     # Q&A生成関連
     'generate_qa_for_chunk_with_ga',
     'generate_qa_for_chunk_with_ga_and_fulltext',
+    'generate_qa_for_chunk_with_ga_and_thinking',
     'generate_ga_definitions',
     
     # テキスト分割
@@ -40,6 +42,8 @@ __all__ = [
     
     # XML処理
     'convert_to_xml_by_genre',
+    'load_existing_xml_file',
+    'aggregate_logs_xml_to_qa',
     
     # ファイル操作
     'create_output_directories',
diff --git a/easy_dataset_cli/ga_parser.py b/easy_dataset_cli/ga_parser.py
index fb9aa16..cdeb17d 100644
--- a/easy_dataset_cli/ga_parser.py
+++ b/easy_dataset_cli/ga_parser.py
@@ -172,7 +172,7 @@ def parse_ga_definitions_from_xml(xml_content: str) -> List[Dict[str, Dict[str,
         console.print(f"[dim]問題のあるXML: {xml_content[xml_start:xml_start+200] if xml_start != -1 else xml_content[:200]}...[/dim]")
 
         # XMLエラーの場合、手動でテキスト解析を試行
-        console.print("[yellow]手動解析を試行中...[/yellow]")
+        console.print("[yellow]自動解析を試行中...[/yellow]")
         from .xml_utils import parse_ga_from_text_fallback
         pairs = parse_ga_from_text_fallback(xml_content)
 
diff --git a/easy_dataset_cli/main.py b/easy_dataset_cli/main.py
index 6f62532..9285adf 100644
--- a/easy_dataset_cli/main.py
+++ b/easy_dataset_cli/main.py
@@ -13,6 +13,7 @@ from .core import (
     parse_ga_file,
     generate_qa_for_chunk_with_ga,
     generate_qa_for_chunk_with_ga_and_fulltext,
+    generate_qa_for_chunk_with_ga_and_thinking,
     convert_to_xml_by_genre,
     generate_ga_definitions,
     parse_ga_definitions_from_xml,
@@ -143,6 +144,14 @@ def generate(
         "--use-fulltext", "-f",
         help="全文をコンテキストとして含めてQA生成を行います。より文脈を理解したQAが生成されますが、処理時間とコストが増加します。"
     )] = False,
+    use_thinking: Annotated[bool, typer.Option(
+        "--use-thinking", "-T",
+        help="各Q&Aペアに思考プロセスを追加して生成します。より深い理解と説明が可能になりますが、処理時間とコストが増加します。"
+    )] = False,
+    append_mode: Annotated[bool, typer.Option(
+        "--append", "-A",
+        help="既存のXMLファイルに新しいQ&Aを追加します。指定しない場合は上書きします。"
+    )] = False,
     export_alpaca: Annotated[bool, typer.Option(
         "--export-alpaca", "-a",
         help="生成されたQ&AペアをAlpaca形式のJSONファイルとして出力します。"
@@ -200,12 +209,25 @@ def generate(
             console.print("[yellow]⚠ 全文コンテキストモードが有効です。処理時間とコストが増加する可能性があります。[/yellow]")
             console.print(f"[dim]全文長: {len(text)} 文字[/dim]")
 
+        # 思考フロー使用の場合は警告を表示
+        if use_thinking:
+            console.print("[yellow]⚠ 思考フローモードが有効です。各Q&Aに思考プロセスが追加されます。[/yellow]")
+
         with Progress(console=console) as progress:
             task = progress.add_task("[green]Q&Aペアを生成中...", total=total_tasks)
 
             for chunk in chunks:
                 for ga_pair in ga_pairs:
-                    if use_fulltext:
+                    if use_thinking:
+                        qa_pairs = generate_qa_for_chunk_with_ga_and_thinking(
+                            chunk=chunk,
+                            full_text=text if use_fulltext else "",
+                            model=model,
+                            ga_pair=ga_pair,
+                            logs_dir=dirs["logs"] if dirs else None,
+                            num_qa_pairs=num_qa_pairs
+                        )
+                    elif use_fulltext:
                         qa_pairs = generate_qa_for_chunk_with_ga_and_fulltext(
                             chunk=chunk,
                             full_text=text,
@@ -222,12 +244,13 @@ def generate(
                         )
 
                     for pair in qa_pairs:
-                        all_qa_pairs_with_ga.append({
+                        qa_entry = {
                             "genre": ga_pair['genre']['title'],
                             "audience": ga_pair['audience']['title'],
                             "question": pair['question'],
-                            "answer": pair['answer'],
-                        })
+                            "answer": pair['answer'],  # <think>...</think>回答...形式がそのまま入る
+                        }
+                        all_qa_pairs_with_ga.append(qa_entry)
 
                     progress.update(
                         task, advance=1,
@@ -239,7 +262,7 @@ def generate(
             "個のQ&Aペアを生成しました。"
         )
 
-        xml_outputs_by_genre = convert_to_xml_by_genre(all_qa_pairs_with_ga)
+        xml_outputs_by_genre = convert_to_xml_by_genre(all_qa_pairs_with_ga, dirs["qa"] if dirs else None, append_mode)
 
         if dirs:
             console.print(f"XMLファイルを [cyan]{dirs['qa']}[/cyan] に保存しています...")
@@ -286,7 +309,12 @@ def generate(
                 console.print(xml_content, overflow="fold")
     
     except Exception as e:
-        console.print(f"[bold red]エラーが発生しました:[/bold red] {e}")
+        console.print(f"[bold red]エラーが発生しました:[/bold red]")
+        console.print(f"[bold red]エラータイプ:[/bold red] {type(e).__name__}")
+        console.print(f"[bold red]エラーメッセージ:[/bold red] {str(e)}")
+        console.print(f"[bold red]トレースバック:[/bold red]")
+        import traceback
+        console.print(traceback.format_exc())
         raise typer.Exit(code=1)
 
 
@@ -365,5 +393,36 @@ def convert_to_alpaca(
         raise typer.Exit(code=1)
 
 
+@app.command()
+def aggregate_logs(
+    output_dir: Annotated[Path, typer.Argument(
+        exists=True, dir_okay=True, readable=True,
+        help="logsフォルダが含まれる出力ディレクトリへのパス。"
+    )]
+):
+    """logsフォルダ内のタイムスタンプ付きXMLファイルを集約してqaフォルダのXMLを生成します。"""
+    
+    try:
+        logs_dir = output_dir / "logs"
+        qa_dir = output_dir / "qa"
+        
+        if not logs_dir.exists():
+            console.print(f"[bold red]logsフォルダが見つかりません: {logs_dir}[/bold red]")
+            raise typer.Exit(code=1)
+        
+        console.print(f"logsフォルダ: [cyan]{logs_dir}[/cyan]")
+        console.print(f"出力先qaフォルダ: [cyan]{qa_dir}[/cyan]")
+        
+        # XMLファイルを集約してqaフォルダに生成
+        from easy_dataset_cli.core import aggregate_logs_xml_to_qa
+        aggregate_logs_xml_to_qa(logs_dir, qa_dir)
+        
+        console.print(f"\n[bold green]✓[/bold green] 集約が完了しました！")
+        
+    except Exception as e:
+        console.print(f"[bold red]エラーが発生しました:[/bold red] {e}")
+        raise typer.Exit(code=1)
+
+
 if __name__ == "__main__":
     app()
diff --git a/easy_dataset_cli/prompts.py b/easy_dataset_cli/prompts.py
index 24ba9f9..c2b00b8 100644
--- a/easy_dataset_cli/prompts.py
+++ b/easy_dataset_cli/prompts.py
@@ -28,3 +28,8 @@ def get_qa_generation_with_fulltext_prompt() -> str:
 def get_ga_definition_generation_prompt() -> str:
     """GA定義生成プロンプトを取得"""
     return load_prompt_template("ga_definition_generation")
+
+
+def get_qa_generation_with_thinking_prompt() -> str:
+    """思考フロー対応Q&A生成プロンプトを取得"""
+    return load_prompt_template("qa_generation_with_thinking")
diff --git a/easy_dataset_cli/prompts/ga_definition_generation.md b/easy_dataset_cli/prompts/ga_definition_generation.md
index 757afcd..17c05a4 100644
--- a/easy_dataset_cli/prompts/ga_definition_generation.md
+++ b/easy_dataset_cli/prompts/ga_definition_generation.md
@@ -7,7 +7,7 @@
 2. この文章から質問と回答のペアを生成する際に最適となる{num_ga_pairs}個のGenre-Audienceペアを提案してください。
 3. 各Genreは異なる文体・形式（学術論文、技術ブログ、教科書、FAQ、対話形式など）を表現してください。
 4. 各Audienceは異なる知識レベル・立場（初心者、学生、専門家、実務者など）を表現してください。
-5. 文章の内容に適したペアを選択し、多様性を確保してください。
+5. 文章の内容に適したペアを選択し、多様性・多角性を確保してください。
 
 ## 文章:
 ---
diff --git a/easy_dataset_cli/prompts/qa_generation_with_thinking.md b/easy_dataset_cli/prompts/qa_generation_with_thinking.md
new file mode 100644
index 0000000..2bb04fe
--- /dev/null
+++ b/easy_dataset_cli/prompts/qa_generation_with_thinking.md
@@ -0,0 +1,53 @@
+# 役割: Q&Aペア生成の専門家（思考フロー対応版）
+
+あなたは、与えられた文章から高品質な質問と回答のペアを作成する専門家です。特に、指定された「体裁」と「読者」に合わせてスタイルを調整する能力に長けています。また、思考プロセスを明示的に記述する能力にも優れています。
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
+**重要**: 回答は必ず`<Answer><think>思考フロー...</think>回答...</Answer>`のように、思考フローを`<think>`タグで囲み、回答本文の直前に含めてください。
+回答文に改行を含めず、一行で記述してください。
+
+## 出力例:
+\```xml
+<QAPairs>
+<Pair>
+<Question>ミトコンドリアの主な機能は何ですか？</Question>
+<Answer><think>ミトコンドリアは細胞の「発電所」として知られており、細胞呼吸を通じて栄養素からエネルギーを産生する。その主な産物がATPであり、細胞のあらゆる生命活動のエネルギー源となる。</think>ミトコンドリアの主な機能は、細胞のエネルギー通貨であるアデノシン三リン酸（ATP）の大部分を生成することです。</Answer>
+</Pair>
+<Pair>
+<Question>ATPは細胞内でどのように利用されますか？</Question>
+<Answer><think>ATPはアデノシン三リン酸であり、リン酸結合の加水分解によってエネルギーを放出する。このエネルギーはタンパク質の合成、物質の輸送、細胞分裂など、細胞内のあらゆるエネルギー需要に供給される。</think>ATPは細胞内の様々な化学反応のエネルギー源として利用されます。</Answer>
+</Pair>
+</QAPairs>
+\```
+
+それでは、思考フローを含むQ&Aペアの生成を開始してください。
diff --git a/easy_dataset_cli/qa_generator.py b/easy_dataset_cli/qa_generator.py
index 0817065..545d830 100644
--- a/easy_dataset_cli/qa_generator.py
+++ b/easy_dataset_cli/qa_generator.py
@@ -3,15 +3,20 @@
 
 import os
 import xml.etree.ElementTree as ET
+from xml.dom import minidom
 from pathlib import Path
 from typing import List, Dict
 from litellm import completion
 from rich.console import Console
 from dotenv import load_dotenv
+import traceback
+import json
+from datetime import datetime
 
 from .prompts import (
     get_qa_generation_prompt,
     get_qa_generation_with_fulltext_prompt,
+    get_qa_generation_with_thinking_prompt,
     get_ga_definition_generation_prompt
 )
 from .xml_utils import parse_qa_from_text_fallback
@@ -43,36 +48,97 @@ def generate_qa_for_chunk_with_ga_and_fulltext(
     )
 
     messages = [
-        {"role": "system", "content": "あなたは、XML形式で厳密に出力する優秀なアシスタントです。XMLの特殊文字（&, <, >, \", '）は適切にエスケープし、改行は含めずに出力してください。"},
+        {"role": "system", "content": "あなたは、XML形式で厳密に出力する優秀なアシスタントです。通常のXMLの特殊文字（&, \", '）は適切にエスケープしてください。ただし、<Question>、<Answer>、<think>タグはそのまま使用してください。改行は含めずに出力してください。"},
         {"role": "user", "content": prompt}
     ]
 
     # OpenRouter用の環境変数設定
     os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY", "")
 
+    # タイムスタンプ付きログファイル名を生成
+    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
+    genre_safe = "".join(c for c in ga_pair['genre']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
+    audience_safe = "".join(c for c in ga_pair['audience']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
+    
     try:
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
         response = completion(model=model, messages=messages)
         xml_content = response.choices[0].message.content
 
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
         # rawレスポンスを保存（オプション）
         if logs_dir:
-            genre_safe = "".join(c for c in ga_pair['genre']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
-            audience_safe = "".join(c for c in ga_pair['audience']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
-            raw_filename = f"qa_fulltext_raw_{genre_safe}_{audience_safe}.md"
+            raw_filename = f"qa_fulltext_raw_{genre_safe}_{audience_safe}_{timestamp}.md"
             raw_file_path = logs_dir / raw_filename
             raw_file_path.write_text(xml_content, encoding="utf-8")
 
-        return _parse_qa_response(xml_content)
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
 
     except Exception as general_error:
-        console.print(
-            f"[bold red]チャンクとGAペアからのQ&A生成中にエラーが発生しました:[/bold red] "
-            f"{general_error}"
-        )
-        console.print(
-            f"[dim]Genre: {ga_pair['genre']['title']}, "
-            f"Audience: {ga_pair['audience']['title']}[/dim]"
-        )
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
         return []
 
 
@@ -95,36 +161,97 @@ def generate_qa_for_chunk_with_ga(
     )
 
     messages = [
-        {"role": "system", "content": "あなたは、XML形式で厳密に出力する優秀なアシスタントです。XMLの特殊文字（&, <, >, \", '）は適切にエスケープし、改行は含めずに出力してください。"},
+        {"role": "system", "content": "あなたは、XML形式で厳密に出力する優秀なアシスタントです。通常のXMLの特殊文字（&, \", '）は適切にエスケープしてください。ただし、<Question>、<Answer>、<think>タグはそのまま使用してください。改行は含めずに出力してください。"},
         {"role": "user", "content": prompt}
     ]
 
     # OpenRouter用の環境変数設定
     os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY", "")
 
+    # タイムスタンプ付きログファイル名を生成
+    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
+    genre_safe = "".join(c for c in ga_pair['genre']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
+    audience_safe = "".join(c for c in ga_pair['audience']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
+    
     try:
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
         response = completion(model=model, messages=messages)
         xml_content = response.choices[0].message.content
 
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
         # rawレスポンスを保存（オプション）
         if logs_dir:
-            genre_safe = "".join(c for c in ga_pair['genre']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
-            audience_safe = "".join(c for c in ga_pair['audience']['title'] if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')
-            raw_filename = f"qa_raw_{genre_safe}_{audience_safe}.md"
+            raw_filename = f"qa_raw_{genre_safe}_{audience_safe}_{timestamp}.md"
             raw_file_path = logs_dir / raw_filename
             raw_file_path.write_text(xml_content, encoding="utf-8")
 
-        return _parse_qa_response(xml_content)
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
 
     except Exception as general_error:
-        console.print(
-            f"[bold red]チャンクとGAペアからのQ&A生成中にエラーが発生しました:[/bold red] "
-            f"{general_error}"
-        )
-        console.print(
-            f"[dim]Genre: {ga_pair['genre']['title']}, "
-            f"Audience: {ga_pair['audience']['title']}[/dim]"
-        )
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
         return []
 
 
@@ -173,16 +300,61 @@ def generate_ga_definitions(text_content: str, model: str, num_ga_pairs: int = N
         raise
 
 
-def _parse_qa_response(xml_content: str) -> List[Dict[str, str]]:
+def _parse_qa_response(xml_content: str, logs_dir: Path = None, genre_safe: str = None, audience_safe: str = None, timestamp: str = None) -> List[Dict[str, str]]:
     """Q&A生成レスポンスのXMLを解析する（共通処理）"""
     qa_pairs = []
 
-    # LLMからの出力には余分なテキストが含まれることがあるため、XML部分のみを抽出
-    xml_start = xml_content.find("<QAPairs>")
-    xml_end = xml_content.rfind("</QAPairs>")
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
 
     if xml_start != -1 and xml_end != -1:
-        clean_xml = xml_content[xml_start: xml_end + len("</QAPairs>")]
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
 
         try:
             root = ET.fromstring(clean_xml)
@@ -192,18 +364,318 @@ def _parse_qa_response(xml_content: str) -> List[Dict[str, str]]:
                 answer_node = pair_node.find('Answer')
 
                 if question_node is not None and answer_node is not None:
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
                     qa_pairs.append({
-                        "question": question_node.text or "",
-                        "answer": answer_node.text or ""
+                        "question": question_text,
+                        "answer": answer_text
                     })
 
-        except ET.ParseError:
+        except ET.ParseError as parse_error:
             # XMLパースに失敗した場合、手動でテキスト解析
-            console.print("[yellow]XMLパースエラー、手動解析を試行中...[/yellow]")
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
             qa_pairs = parse_qa_from_text_fallback(clean_xml)
+            
+            # 自動解析でも失敗した場合のフォールバック
+            if not qa_pairs:
+                console.print("[yellow]自動解析も失敗したため、テキストから直接Q&Aを抽出します...[/yellow]")
+                qa_pairs = _extract_qa_from_fallback_text(cleaned_content)
 
     if not qa_pairs:
         console.print(f"[bold red]LLMが生成したXMLの解析に失敗しました[/bold red]")
-        console.print(f"[dim]受信したテキスト: {xml_content[:200]}...[/dim]")
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
     return qa_pairs
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
+def generate_qa_for_chunk_with_ga_and_thinking(
+    chunk: str,
+    full_text: str,
+    model: str,
+    ga_pair: Dict[str, Dict[str, str]],
+    logs_dir: Path = None,
+    num_qa_pairs: int = None
+) -> List[Dict[str, str]]:
+    """litellmを使い、1つのチャンクと全文、1つのGAペアから思考フロー付きQ&Aペアのリストを生成する"""
+    prompt_template = get_qa_generation_with_thinking_prompt()
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
+    # OpenRouter用の環境変数設定
+    os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY", "")
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
+            request_filename = f"request_thinking_{genre_safe}_{audience_safe}_{timestamp}.json"
+            request_file_path = logs_dir / request_filename
+            with open(request_file_path, 'w', encoding='utf-8') as f:
+                json.dump(request_log, f, ensure_ascii=False, indent=2)
+            console.print(f"[dim]リクエストログを保存: {request_filename}[/dim]")
+
+        response = completion(model=model, messages=messages)
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
+            response_filename = f"response_thinking_{genre_safe}_{audience_safe}_{timestamp}.json"
+            response_file_path = logs_dir / response_filename
+            with open(response_file_path, 'w', encoding='utf-8') as f:
+                json.dump(response_log, f, ensure_ascii=False, indent=2)
+            console.print(f"[dim]レスポンスログを保存: {response_filename}[/dim]")
+
+        # rawレスポンスを保存（オプション）
+        if logs_dir:
+            raw_filename = f"qa_thinking_raw_{genre_safe}_{audience_safe}_{timestamp}.md"
+            raw_file_path = logs_dir / raw_filename
+            raw_file_path.write_text(xml_content, encoding="utf-8")
+
+        qa_pairs = _parse_qa_response(xml_content, logs_dir, genre_safe, audience_safe, timestamp)
+
+        # 生成したQAを保存
+        if qa_pairs and logs_dir:
+            qa_filename = f"qa_pairs_thinking_{genre_safe}_{audience_safe}_{timestamp}.xml"
+            _save_qa_pairs_to_xml(qa_pairs, logs_dir, qa_filename)
+
+        return qa_pairs
+
+    except Exception as general_error:
+        # 詳細なエラー情報を表示
+        console.print(f"[bold red]チャンクとGAペアからの思考フロー付きQ&A生成中にエラーが発生しました:[/bold red]")
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
+            error_filename = f"error_thinking_{genre_safe}_{audience_safe}_{timestamp}.json"
+            error_file_path = logs_dir / error_filename
+            with open(error_file_path, 'w', encoding='utf-8') as f:
+                json.dump(error_log, f, ensure_ascii=False, indent=2)
+            console.print(f"[dim]エラーログを保存: {error_filename}[/dim]")
+        
+        return []
+
+
diff --git a/easy_dataset_cli/xml_utils.py b/easy_dataset_cli/xml_utils.py
index ec5a370..4337616 100644
--- a/easy_dataset_cli/xml_utils.py
+++ b/easy_dataset_cli/xml_utils.py
@@ -5,6 +5,7 @@ import xml.etree.ElementTree as ET
 from xml.dom import minidom
 from collections import defaultdict
 from typing import List, Dict
+from pathlib import Path
 from rich.console import Console
 
 console = Console()
@@ -41,10 +42,10 @@ def parse_ga_from_text_fallback(content: str) -> List[Dict[str, Dict[str, str]]]
                         "description": audience_desc.strip()
                     }
                 })
-                console.print(f"[green]✓[/green] (手動解析) {genre_title} x {audience_title}")
+                console.print(f"[green]✓[/green] (自動解析) {genre_title} x {audience_title}")
 
     except Exception as e:
-        console.print(f"[red]手動解析も失敗:[/red] {e}")
+        console.print(f"[red]自動解析も失敗:[/red] {e}")
 
     return pairs
 
@@ -97,10 +98,10 @@ def parse_qa_from_text_fallback(content: str) -> List[Dict[str, str]]:
                     "question": question.strip(),
                     "answer": answer.strip()
                 })
-                console.print("[green]✓[/green] (手動解析) Q&A追加")
+                console.print("[green]✓[/green] (自動解析) Q&A追加")
 
     except Exception as e:
-        console.print(f"[red]Q&A手動解析も失敗:[/red] {e}")
+        console.print(f"[red]Q&A自動解析も失敗:[/red] {e}")
 
     return qa_pairs
 
@@ -123,15 +124,248 @@ def extract_simple_tag_content(content: str, tag: str) -> str:
         return ""
 
 
-def convert_to_xml_by_genre(all_qa_pairs: List[Dict[str, str]]) -> Dict[str, str]:
-    """Q&AペアのリストをGenreごとにグループ化し、整形されたXML文字列の辞書に変換する"""
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
+def load_existing_xml_file(xml_file_path: Path) -> List[Dict[str, str]]:
+    """既存のXMLファイルからQ&Aペアを読み込む"""
+    qa_pairs = []
+    
+    try:
+        if not xml_file_path.exists():
+            return qa_pairs
+            
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
+                qa_pairs.append({
+                    "genre": genre,
+                    "audience": audience_elem.text or "",
+                    "question": question_elem.text or "",
+                    "answer": answer_elem.text or ""
+                })
+                
+    except Exception as e:
+        console.print(f"[yellow]既存XMLファイルの読み込みに失敗: {e}[/yellow]")
+    
+    return qa_pairs
+
+
+def load_existing_xml_file_with_fallback(xml_file_path: Path, genre_from_filename: str = None) -> List[Dict[str, str]]:
+    """既存のXMLファイルからQ&Aペアを読み込み、ファイル名からジャンル情報を取得するフォールバック関数"""
+    qa_pairs = []
+    
+    try:
+        if not xml_file_path.exists():
+            return qa_pairs
+            
+        tree = ET.parse(xml_file_path)
+        root = tree.getroot()
+        
+        # XML内のgenre属性を優先し、なければファイル名から取得した情報を使用
+        genre = root.get('genre', genre_from_filename or 'Unknown')
+        
+        for pair in root.findall('Pair'):
+            audience_elem = pair.find('Audience')
+            question_elem = pair.find('Question')
+            answer_elem = pair.find('Answer')
+            
+            # Audience要素がない場合は、ファイル名から取得したAudience情報を使用
+            if audience_elem is None:
+                # ファイル名からAudience情報を取得（この関数の呼び出し元で設定済み）
+                audience = genre_from_filename.split('_')[-1] if genre_from_filename and '_' in genre_from_filename else ""
+            else:
+                audience = audience_elem.text or ""
+            
+            if question_elem is not None and answer_elem is not None:
+                qa_pairs.append({
+                    "genre": genre,
+                    "audience": audience,
+                    "question": question_elem.text or "",
+                    "answer": answer_elem.text or ""
+                })
+                
+    except Exception as e:
+        console.print(f"[yellow]既存XMLファイルの読み込みに失敗: {e}[/yellow]")
+    
+    return qa_pairs
+
+
+def aggregate_logs_xml_to_qa(logs_dir: Path, qa_dir: Path) -> None:
+    """logsフォルダ内のXMLファイルを集約してqaフォルダの既存XMLファイルを更新・追加する"""
+    from rich.console import Console
+    
+    console = Console()
+    
+    console.print(f"[bold blue]logsフォルダからXMLファイルを集約して既存ファイルを更新しています...[/bold blue]")
+    
+    # qaディレクトリが存在しない場合は作成
+    qa_dir.mkdir(parents=True, exist_ok=True)
+    
+    # logsディレクトリ内のXMLファイルを検索
+    xml_files = list(logs_dir.glob("*.xml"))
+    
+    if not xml_files:
+        console.print(f"[yellow]logsフォルダにXMLファイルが見つかりません: {logs_dir}[/yellow]")
+        return
+    
+    console.print(f"[dim]{len(xml_files)}個のXMLファイルを検出[/dim]")
+    
+    # GenreごとにQ&Aペアを集約
+    genre_qa_pairs = defaultdict(list)
+    
+    for xml_file in xml_files:
+        try:
+            console.print(f"[dim]処理中: {xml_file.name}[/dim]")
+            
+            # ファイル名からGenre情報を抽出（例: qa_pairs_FAQ_初心者ゲーマー_20250815_171008.xml）
+            filename = xml_file.stem
+            if filename.startswith("qa_pairs_"):
+                # GenreとAudience情報を抽出
+                parts = filename.replace("qa_pairs_", "").split("_")
+                if len(parts) >= 3:  # genre + audience + timestamp + timestamp
+                    genre = parts[0]
+                    # 残りの部分はAudience（_で区切られている可能性がある）
+                    # 最後の2要素はタイムスタンプなので除外
+                    audience = "_".join(parts[1:-2])
+                    
+                    console.print(f"[dim]ファイル名解析: genre={genre}, audience={audience}[/dim]")
+                    
+                    # XMLファイルからQ&Aペアを読み込む（ファイル名からジャンル情報を渡す）
+                    qa_pairs = load_existing_xml_file_with_fallback(xml_file, genre)
+                    
+                    console.print(f"[dim]読み込んだQ&Aペア数: {len(qa_pairs)}[/dim]")
+                    
+                    # Genre情報を付与して保存
+                    for qa_pair in qa_pairs:
+                        qa_pair["genre"] = genre
+                        qa_pair["audience"] = audience
+                        genre_qa_pairs[genre].append(qa_pair)
+                else:
+                    console.print(f"[yellow]ファイル名の解析に失敗: {filename}[/yellow]")
+                        
+        except Exception as e:
+            console.print(f"[yellow]ファイルの処理中にエラー: {xml_file.name} - {e}[/yellow]")
+            continue
+    
+    # Genreごとに既存XMLファイルを更新
+    console.print(f"\n[bold green]集約結果:[/bold green]")
+    total_updated = 0
+    
+    for genre, qa_pairs in genre_qa_pairs.items():
+        console.print(f"  - [cyan]{genre}[/cyan]: {len(qa_pairs)}件のQ&Aを追加")
+        
+        # 既存のXMLファイルを検索
+        safe_genre_name = "".join(c for c in genre if c.isalnum() or c in (' ', '_', '-')).strip().replace(' ', '_')
+        existing_file = qa_dir / f"{safe_genre_name}.xml"
+        
+        # 既存のQ&Aペアを読み込む（ファイルが存在する場合）
+        existing_pairs = []
+        if existing_file.exists():
+            existing_pairs = load_existing_xml_file(existing_file)
+            console.print(f"    [dim]既存の{len(existing_pairs)}件のQ&Aを読み込み[/dim]")
+        
+        # 新しいQ&Aを追加（重複を避ける）
+        existing_questions = {pair["question"] for pair in existing_pairs}
+        new_pairs = []
+        for pair in qa_pairs:
+            if pair["question"] not in existing_questions:
+                new_pairs.append(pair)
+            else:
+                console.print(f"    [yellow]重複するQ&Aをスキップ: {pair['question'][:50]}...[/yellow]")
+        
+        console.print(f"    [green]追加する新しいQ&A: {len(new_pairs)}件[/green]")
+        
+        # 既存のペアに新しいペアを追加
+        updated_pairs = existing_pairs + new_pairs
+        
+        if updated_pairs:
+            # XMLに変換
+            root = ET.Element("QAPairs")
+            root.set("genre", genre)
+
+            for item in updated_pairs:
+                pair_elem = ET.SubElement(root, "Pair")
+
+                audience_elem = ET.SubElement(pair_elem, "Audience")
+                audience_elem.text = item["audience"]
+
+                question_elem = ET.SubElement(pair_elem, "Question")
+                question_elem.text = item["question"]
+
+                answer_elem = ET.SubElement(pair_elem, "Answer")
+                answer_elem.text = item["answer"]
+
+            # 整形して保存
+            rough_string = ET.tostring(root, 'utf-8')
+            reparsed = minidom.parseString(rough_string)
+            xml_content = reparsed.toprettyxml(indent="  ")
+            
+            existing_file.write_text(xml_content, encoding='utf-8')
+            console.print(f"    [green]✓[/green] {existing_file.name} を更新 ({len(updated_pairs)}件)")
+            total_updated += 1
+        else:
+            console.print(f"    [yellow]更新するQ&Aがありません[/yellow]")
+    
+    console.print(f"\n[bold green]✓[/bold green] 合計{total_updated}個のジャンルのXMLファイルを更新しました")
+
+
+def convert_to_xml_by_genre(all_qa_pairs: List[Dict[str, str]], qa_dir: Path = None, append_mode: bool = False) -> Dict[str, str]:
+    """Q&AペアのリストをGenreごとにグループ化し、整形されたXML文字列の辞書に変換する
+    
+    Args:
+        all_qa_pairs: 変換するQ&Aペアのリスト
+        qa_dir: QAファイルが保存されているディレクトリ（追加モードの場合に必要）
+        append_mode: 既存ファイルに追加するかどうか
+    """
     grouped_by_genre = defaultdict(list)
 
     for item in all_qa_pairs:
         grouped_by_genre[item["genre"]].append(item)
 
     xml_outputs = {}
+    
     for genre, pairs in grouped_by_genre.items():
+        # 追加モードの場合は既存のXMLファイルを読み込む
+        if append_mode and qa_dir:
+            safe_genre_name = "".join(c for c in genre if c.isalnum() or c in (' ', '_', '-')).strip().replace(' ', '_')
+            existing_file = qa_dir / f"{safe_genre_name}.xml"
+            
+            if existing_file.exists():
+                existing_pairs = load_existing_xml_file(existing_file)
+                console.print(f"[dim]Genre '{genre}': 既存の{len(existing_pairs)}件のQ&Aを読み込みました[/dim]")
+                # 既存のペアを先頭に追加
+                pairs = existing_pairs + pairs
+        
         root = ET.Element("QAPairs")
         root.set("genre", genre)
 
@@ -145,10 +379,23 @@ def convert_to_xml_by_genre(all_qa_pairs: List[Dict[str, str]]) -> Dict[str, str
             question_elem.text = item["question"]
 
             answer_elem = ET.SubElement(pair_elem, "Answer")
-            answer_elem.text = item["answer"]
+            
+            # 回答内容を解析
+            parsed_answer = _parse_answer_with_think(item["answer"])
+            
+            if parsed_answer["has_think"]:
+                # <think>をサブエレメントとして追加
+                think_elem = ET.SubElement(answer_elem, "think")
+                think_elem.text = parsed_answer["think_content"]
+                think_elem.tail = parsed_answer["answer_content"]
+            else:
+                # 通常の回答
+                answer_elem.text = parsed_answer["answer_content"]
 
         rough_string = ET.tostring(root, 'utf-8')
         reparsed = minidom.parseString(rough_string)
-        xml_outputs[genre] = reparsed.toprettyxml(indent="  ")
+        xml_output = reparsed.toprettyxml(indent="  ")
+        
+        xml_outputs[genre] = xml_output
 
     return xml_outputs
diff --git a/example/scripts/orin.bat b/example/scripts/orin.bat
new file mode 100644
index 0000000..cb3391b
--- /dev/null
+++ b/example/scripts/orin.bat
@@ -0,0 +1,5 @@
+uv run easy-dataset create-ga .\example\input\documents\Touhou_Chireiden.md --output-dir .\example\output\Touhou_Chireiden --num-ga-pairs 10
+
+uv run easy-dataset generate .\example\input\documents\Touhou_Chireiden.md  --ga-file .\example\output\Touhou_Chireiden\ga\ga_definitions.xml --output-dir .\example\output\Touhou_Chireiden\ --chunk-size 3000 --use-fulltext --append
+
+uv run easy-dataset convert-to-alpaca .\example\output\Touhou_Chireiden\qa --output-file example\output\Touhou_Chireiden\dataset.json --upload-hf --hf-repo-name MakiAi/Orin-Instruct-Alpaca-JP-v7
diff --git a/example/scripts/simple.bat b/example/scripts/simple.bat
new file mode 100644
index 0000000..15240c4
--- /dev/null
+++ b/example/scripts/simple.bat
@@ -0,0 +1 @@
+uv run easy-dataset generate .\example\input\documents\sample_document.txt  --ga-file .\example\output\sample_document\ga\ga_definitions.xml  --output-dir .\example\output\sample_document\ --use-thinking --append
diff --git a/fix_xml_generation.py b/fix_xml_generation.py
new file mode 100644
index 0000000..ebe1b4b
--- /dev/null
+++ b/fix_xml_generation.py
@@ -0,0 +1,34 @@
+#!/usr/bin/env python3
+"""Q&Aジェネレーターのシステムメッセージを修正するスクリプト"""
+
+import sys
+import os
+
+def fix_system_messages():
+    """qa_generator.pyのシステムメッセージを修正"""
+    file_path = "c:/Prj/easy-dataset-cli/easy_dataset_cli/qa_generator.py"
+    
+    with open(file_path, 'r', encoding='utf-8') as f:
+        content = f.read()
+    
+    # 古いシステムメッセージを新しいものに置換
+    old_message = '"あなたは、XML形式で厳密に出力する優秀なアシスタントです。XMLの特殊文字（&, <, >, \\", \'）は適切にエスケープし、改行は含めずに出力してください。"'
+    new_message = '"あなたは、XML形式で厳密に出力する優秀なアシスタントです。通常のXMLの特殊文字（&, \\", \'）は適切にエスケープしてください。ただし、<Question>、<Answer>、<think>タグはそのまま使用してください。改行は含めずに出力してください。"'
+    
+    # 置換実行
+    new_content = content.replace(old_message, new_message)
+    
+    # 思考フロー用のメッセージも統一
+    thinking_old = '"あなたは、XML形式で出力する優秀なアシスタントです。<think>タグは特別なタグなのでエスケープしないでください。それ以外のXMLの特殊文字（&, <, >, \\", \'）は適切にエスケープし、改行は含めずに出力してください。"'
+    new_content = new_content.replace(thinking_old, new_message)
+    
+    # ファイルに書き戻し
+    with open(file_path, 'w', encoding='utf-8') as f:
+        f.write(new_content)
+    
+    print(f"修正完了: {file_path}")
+    print(f"置換回数 (通常): {content.count(old_message)}")
+    print(f"置換回数 (思考): {content.count(thinking_old)}")
+
+if __name__ == "__main__":
+    fix_system_messages()
diff --git a/tests/test_aggregate_logs.py b/tests/test_aggregate_logs.py
new file mode 100644
index 0000000..6f1c10f
--- /dev/null
+++ b/tests/test_aggregate_logs.py
@@ -0,0 +1,145 @@
+#!/usr/bin/env python3
+"""logsフォルダのXML集約機能のテストスクリプト"""
+
+import sys
+import os
+import tempfile
+import shutil
+from pathlib import Path
+sys.path.append(os.path.join(os.path.dirname(__file__), 'easy_dataset_cli'))
+
+from easy_dataset_cli.xml_utils import aggregate_logs_xml_to_qa, load_existing_xml_file
+from easy_dataset_cli.core import aggregate_logs_xml_to_qa as core_aggregate_logs_xml_to_qa
+from rich.console import Console
+
+console = Console()
+
+def create_test_xml_files(logs_dir: Path):
+    """テスト用のXMLファイルを作成"""
+    
+    # logsディレクトリを作成
+    logs_dir.mkdir(parents=True, exist_ok=True)
+    
+    # テスト用XMLファイル1: FAQ_初心者ゲーマー
+    faq_xml_content = '''<?xml version="1.0" ?>
+<QAPairs genre="FAQ">
+  <Pair>
+    <Audience>初心者ゲーマー</Audience>
+    <Question>東方Projectとは何ですか？</Question>
+    <Answer>東方Projectは、上海アリス幻樂団によって制作された弾幕系シューティングゲームシリーズです。</Answer>
+  </Pair>
+  <Pair>
+    <Audience>初心者ゲーマー</Audience>
+    <Question>最初にどのゲームをプレイすればいいですか？</Question>
+    <Answer>初心者には「東方紅魔郷」や「東方妖々夢」がおすすめです。</Answer>
+  </Pair>
+</QAPairs>'''
+    
+    faq_file = logs_dir / "qa_pairs_FAQ_初心者ゲーマー_20250815_171008.xml"
+    faq_file.write_text(faq_xml_content, encoding='utf-8')
+    
+    # テスト用XMLファイル2: テクニカルガイド_PCゲーミング愛好者
+    tech_xml_content = '''<?xml version="1.0" ?>
+<QAPairs genre="テクニカルガイド">
+  <Pair>
+    <Audience>PCゲーミング愛好者</Audience>
+    <Question>東方Projectのシステム要件は？</Question>
+    <Answer>東方Projectのゲームは比較的古いPCでも動作するように設計されています。</Answer>
+  </Pair>
+  <Pair>
+    <Audience>PCゲーミング愛好者</Audience>
+    <Question>Steam版とダウンロード版の違いは？</Question>
+    <Answer>Steam版は自動アップデート機能があり、クラウドセーブに対応しています。</Answer>
+  </Pair>
+</QAPairs>'''
+    
+    tech_file = logs_dir / "qa_pairs_テクニカルガイド_PCゲーミング愛好者_20250815_171009.xml"
+    tech_file.write_text(tech_xml_content, encoding='utf-8')
+    
+    # テスト用XMLファイル3: FAQ_上級者
+    faq_advanced_xml_content = '''<?xml version="1.0" ?>
+<QAPairs genre="FAQ">
+  <Pair>
+    <Audience>上級者</Audience>
+    <Question>東方Projectのキャラクター設定はどこで確認できますか？</Question>
+    <Answer>公式サイトや各ゲームのマニュアル、二次創作情報サイトで詳細な設定を確認できます。</Answer>
+  </Pair>
+  <Pair>
+    <Audience>上級者</Audience>
+    <Question>弾幕の難易度設定について教えてください。</Question>
+    <Answer>各ゲームには複数の難易度設定があり、特に「Extra」や'Phantasm'は非常に高い難易度です。</Answer>
+  </Pair>
+</QAPairs>'''
+    
+    faq_advanced_file = logs_dir / "qa_pairs_FAQ_上級者_20250815_171010.xml"
+    faq_advanced_file.write_text(faq_advanced_xml_content, encoding='utf-8')
+
+def test_aggregate_logs():
+    """logsフォルダのXML集約機能のテスト"""
+    
+    print("=== logsフォルダのXML集約機能テスト ===\n")
+    
+    # 一時ディレクトリを作成
+    with tempfile.TemporaryDirectory() as temp_dir:
+        temp_path = Path(temp_dir)
+        logs_dir = temp_path / "logs"
+        qa_dir = temp_path / "qa"
+        
+        # テスト用XMLファイルを作成
+        create_test_xml_files(logs_dir)
+        
+        console.print(f"テスト用logsディレクトリ: {logs_dir}")
+        console.print(f"テスト用qaディレクトリ: {qa_dir}")
+        
+        # XMLファイルを集約
+        console.print("\n[bold blue]XMLファイルを集約中...[/bold blue]")
+        aggregate_logs_xml_to_qa(logs_dir, qa_dir)
+        
+        # 結果を確認
+        console.print("\n[bold green]=== 集約結果 ===[/bold green]")
+        
+        # qaディレクトリ内のファイルを確認
+        xml_files = list(qa_dir.glob("*.xml"))
+        console.print(f"生成されたXMLファイル数: {len(xml_files)}")
+        
+        for xml_file in xml_files:
+            console.print(f"\n[cyan]{xml_file.name}[/cyan]:")
+            
+            # XMLファイルの内容を確認
+            qa_pairs = load_existing_xml_file(xml_file)
+            console.print(f"  Q&Aペア数: {len(qa_pairs)}")
+            
+            for i, qa in enumerate(qa_pairs, 1):
+                console.print(f"  {i}. [yellow]質問:[/yellow] {qa['question']}")
+                console.print(f"     [yellow]回答:[/yellow] {qa['answer']}")
+                console.print(f"     [dim]ジャンル:[/dim] {qa['genre']}")
+                console.print(f"     [dim]対象読者:[/dim] {qa['audience']}")
+        
+        # 期待される結果を確認
+        expected_files = ["FAQ.xml", "テクニカルガイド.xml"]
+        console.print(f"\n[bold blue]=== 期待されるファイル ===[/bold blue]")
+        for expected_file in expected_files:
+            expected_path = qa_dir / expected_file
+            if expected_path.exists():
+                console.print(f"[green]✓[/green] {expected_file} が生成されました")
+            else:
+                console.print(f"[red]✗[/red] {expected_file} が生成されていません")
+        
+        # FAQ.xmlの内容を詳細に確認
+        faq_file = qa_dir / "FAQ.xml"
+        if faq_file.exists():
+            console.print(f"\n[bold blue]=== FAQ.xmlの詳細確認 ===[/bold blue]")
+            faq_content = faq_file.read_text(encoding='utf-8')
+            console.print(faq_content)
+        
+        # テスト結果を返す
+        success = len(xml_files) == 2 and all((qa_dir / f).exists() for f in expected_files)
+        return success
+
+if __name__ == "__main__":
+    success = test_aggregate_logs()
+    if success:
+        console.print("\n✅ すべてのテストが成功しました！")
+    else:
+        console.print("\n❌ テストに失敗しました。")
+    sys.exit(0 if success else 1)
diff --git a/tests/test_answer_extraction.py b/tests/test_answer_extraction.py
new file mode 100644
index 0000000..8d96d67
--- /dev/null
+++ b/tests/test_answer_extraction.py
@@ -0,0 +1,56 @@
+#!/usr/bin/env python3
+"""Answer要素の内容取得テスト"""
+
+import xml.etree.ElementTree as ET
+
+def test_answer_content_extraction():
+    """Answer要素の内容取得をテスト"""
+    
+    # テストXML
+    xml_content = """<QAPairs>
+    <Pair>
+        <Question>テスト質問1</Question>
+        <Answer><think>思考プロセス</think>回答内容</Answer>
+    </Pair>
+    <Pair>
+        <Question>テスト質問2</Question>
+        <Answer>普通の回答</Answer>
+    </Pair>
+</QAPairs>"""
+    
+    root = ET.fromstring(xml_content)
+    
+    for pair_node in root.findall('Pair'):
+        question_node = pair_node.find('Question')
+        answer_node = pair_node.find('Answer')
+        
+        if question_node is not None and answer_node is not None:
+            question_text = question_node.text or ""
+            
+            print(f"質問: {question_text}")
+            print(f"Answer要素の子要素数: {len(answer_node)}")
+            print(f"Answer.text: '{answer_node.text}'")
+            print(f"Answer.tail: '{answer_node.tail}'")
+            
+            # サブエレメントがある場合の詳細確認
+            if len(answer_node) > 0:
+                for i, child in enumerate(answer_node):
+                    print(f"  子要素{i}: tag='{child.tag}', text='{child.text}', tail='{child.tail}'")
+            
+            # <Answer>要素内の全ての内容を取得（サブエレメント含む）
+            if len(answer_node) > 0:
+                # サブエレメントがある場合、XML文字列として再構築
+                answer_content = ET.tostring(answer_node, encoding='unicode', method='xml')
+                print(f"Answer XML: {answer_content}")
+                # <Answer>タグを除去して内容のみ取得
+                answer_text = answer_content[answer_content.find('>')+1:answer_content.rfind('<')]
+                print(f"抽出された内容: '{answer_text}'")
+            else:
+                # サブエレメントがない場合は通常のテキスト
+                answer_text = answer_node.text or ""
+                print(f"通常テキスト: '{answer_text}'")
+            
+            print("---")
+
+if __name__ == "__main__":
+    test_answer_content_extraction()
diff --git a/tests/test_fixed_parsing.py b/tests/test_fixed_parsing.py
new file mode 100644
index 0000000..f0104f2
--- /dev/null
+++ b/tests/test_fixed_parsing.py
@@ -0,0 +1,68 @@
+#!/usr/bin/env python3
+"""修正されたAnswer解析のテスト"""
+
+import xml.etree.ElementTree as ET
+
+def test_fixed_answer_parsing():
+    """修正されたAnswer解析をテスト"""
+    
+    # テストXML（実際のファイルと同じ構造）
+    xml_content = """<QAPairs>
+    <Pair>
+        <Question>テスト質問1</Question>
+        <Answer>
+            <think>これは思考プロセスです</think>
+            これは回答内容です。
+        </Answer>
+    </Pair>
+    <Pair>
+        <Question>テスト質問2</Question>
+        <Answer>普通の回答です。</Answer>
+    </Pair>
+</QAPairs>"""
+    
+    root = ET.fromstring(xml_content)
+    
+    for i, pair_node in enumerate(root.findall('Pair'), 1):
+        question_node = pair_node.find('Question')
+        answer_node = pair_node.find('Answer')
+        
+        if question_node is not None and answer_node is not None:
+            question_text = question_node.text or ""
+            
+            print(f"=== Pair {i} ===")
+            print(f"質問: {question_text.strip()}")
+            print(f"Answer要素の子要素数: {len(answer_node)}")
+            
+            # <Answer>要素内の内容を適切に取得
+            if len(answer_node) > 0:
+                # サブエレメントがある場合（<think>タグなど）
+                answer_parts = []
+                
+                # Answer要素の直接のテキスト（<think>より前）
+                if answer_node.text:
+                    answer_parts.append(answer_node.text.strip())
+                    print(f"Answer.text: '{answer_node.text.strip()}'")
+                
+                # 各サブエレメントのtail（サブエレメントの後のテキスト）
+                for child in answer_node:
+                    print(f"子要素: tag='{child.tag}', text='{child.text}', tail='{child.tail}'")
+                    if child.tag == 'think':
+                        # <think>タグの内容を取得
+                        think_content = child.text or ""
+                        answer_parts.append(f"<think>{think_content}</think>")
+                    
+                    # サブエレメントの後のテキスト
+                    if child.tail:
+                        answer_parts.append(child.tail.strip())
+                
+                answer_text = "".join(answer_parts)
+            else:
+                # サブエレメントがない場合は通常のテキスト
+                answer_text = answer_node.text or ""
+            
+            print(f"最終的な回答: '{answer_text}'")
+            print()
+
+if __name__ == "__main__":
+    test_fixed_answer_parsing()
diff --git a/tests/test_simple_xml.py b/tests/test_simple_xml.py
new file mode 100644
index 0000000..ec2d59e
--- /dev/null
+++ b/tests/test_simple_xml.py
@@ -0,0 +1,68 @@
+#!/usr/bin/env python3
+"""ElementTreeでthinkタグを保持するテスト"""
+
+def test_elementtree_with_cdata():
+    """ElementTreeでCDATAセクションを使ってthinkタグを保持"""
+    
+    import xml.etree.ElementTree as ET
+    from xml.dom import minidom
+    
+    # サンプルデータ
+    qa_pairs = [
+        {
+            "question": "テスト質問1",
+            "answer": "<think>これは思考プロセスです</think>これはテスト回答1です。"
+        },
+        {
+            "question": "テスト質問2", 
+            "answer": "<think>別の思考プロセス</think>これはテスト回答2です。"
+        }
+    ]
+    
+    print("方法1: 単純な文字列置換")
+    # 方法1: ElementTreeで生成後、文字列置換
+    root = ET.Element("QAPairs")
+    for qa in qa_pairs:
+        pair_elem = ET.SubElement(root, "Pair")
+        question_elem = ET.SubElement(pair_elem, "Question")
+        question_elem.text = qa["question"]
+        answer_elem = ET.SubElement(pair_elem, "Answer")
+        answer_elem.text = qa["answer"]
+    
+    # 整形
+    rough_string = ET.tostring(root, 'utf-8')
+    reparsed = minidom.parseString(rough_string)
+    pretty_xml = reparsed.toprettyxml(indent="  ")
+    
+    # 単純な置換でthinkタグを復元
+    pretty_xml = pretty_xml.replace("&lt;think&gt;", "<think>")
+    pretty_xml = pretty_xml.replace("&lt;/think&gt;", "</think>")
+    
+    print(pretty_xml)
+    
+    print("\n方法2: ET.toustring後に置換")
+    # 方法2: ET.tostringの結果を直接操作
+    xml_string = ET.tostring(root, encoding='unicode')
+    xml_string = xml_string.replace("&lt;think&gt;", "<think>")
+    xml_string = xml_string.replace("&lt;/think&gt;", "</think>")
+    
+    # 手動で整形
+    import xml.dom.minidom
+    dom = xml.dom.minidom.parseString(xml_string)
+    pretty_xml2 = dom.toprettyxml(indent="  ")
+    
+    print(pretty_xml2)
+    
+    # <think>タグがエスケープされているかチェック
+    if "&lt;think&gt;" in pretty_xml:
+        print("❌ 方法1: <think>タグがエスケープされています!")
+    else:
+        print("✅ 方法1: <think>タグはエスケープされていません!")
+        
+    if "&lt;think&gt;" in pretty_xml2:
+        print("❌ 方法2: <think>タグがエスケープされています!")
+    else:
+        print("✅ 方法2: <think>タグはエスケープされていません!")
+
+if __name__ == "__main__":
+    test_elementtree_with_cdata()
diff --git a/tests/test_subelement.py b/tests/test_subelement.py
new file mode 100644
index 0000000..2c4bad0
--- /dev/null
+++ b/tests/test_subelement.py
@@ -0,0 +1,59 @@
+#!/usr/bin/env python3
+"""サブエレメントでthinkタグを扱うテスト"""
+
+import sys
+import os
+sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
+
+from easy_dataset_cli.qa_generator import _parse_answer_with_think, _save_qa_pairs_to_xml
+from pathlib import Path
+
+def test_parse_answer_with_think():
+    """_parse_answer_with_think関数のテスト"""
+    
+    # テストケース1: <think>タグあり
+    answer1 = "<think>これは思考プロセスです</think>これはテスト回答1です。"
+    result1 = _parse_answer_with_think(answer1)
+    print("テストケース1:", result1)
+    
+    # テストケース2: <think>タグなし
+    answer2 = "これは普通の回答です。"
+    result2 = _parse_answer_with_think(answer2)
+    print("テストケース2:", result2)
+    
+    # テストケース3: 実際のQ&Aペア保存テスト
+    qa_pairs = [
+        {
+            "question": "テスト質問1",
+            "answer": "<think>これは思考プロセスです</think>これはテスト回答1です。"
+        },
+        {
+            "question": "テスト質問2", 
+            "answer": "これは普通の回答です。"
+        }
+    ]
+    
+    test_dir = Path("test_output")
+    test_dir.mkdir(exist_ok=True)
+    
+    _save_qa_pairs_to_xml(qa_pairs, test_dir, "test_subelement.xml")
+    
+    # 生成されたファイルを読んで確認
+    generated_file = test_dir / "test_subelement.xml"
+    if generated_file.exists():
+        content = generated_file.read_text(encoding='utf-8')
+        print("\n生成されたXML:")
+        print(content)
+        
+        if "&lt;think&gt;" in content:
+            print("❌ <think>タグがエスケープされています!")
+        else:
+            print("✅ <think>タグはエスケープされていません!")
+    
+    # クリーンアップ
+    import shutil
+    if test_dir.exists():
+        shutil.rmtree(test_dir)
+
+if __name__ == "__main__":
+    test_parse_answer_with_think()
diff --git a/tests/test_think_tag_preservation.py b/tests/test_think_tag_preservation.py
new file mode 100644
index 0000000..7ada6b0
--- /dev/null
+++ b/tests/test_think_tag_preservation.py
@@ -0,0 +1,57 @@
+#!/usr/bin/env python3
+"""<think>タグのエスケープテスト"""
+
+import sys
+import os
+
+# プロジェクトのルートディレクトリをパスに追加
+sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
+
+from easy_dataset_cli.qa_generator import _decode_xml_entities
+
+def test_think_tag_preservation():
+    """<think>タグが適切に保持されることをテスト"""
+    
+    # テストケース1: <think>タグを含む回答
+    test_text1 = """<think>これはミトコンドリアの機能についての思考プロセスです。細胞のエネルギー工場として機能します。</think>ミトコンドリアは細胞のエネルギー通貨であるATPを生成する重要な細胞小器官です。"""
+    
+    result1 = _decode_xml_entities(test_text1)
+    print("テストケース1:")
+    print(f"入力: {test_text1}")
+    print(f"出力: {result1}")
+    print(f"<think>タグが保持されているか: {'<think>' in result1 and '</think>' in result1}")
+    print()
+    
+    # テストケース2: HTMLエンティティを含む文字列
+    test_text2 = """<think>ATPの生成について考えてみます。&lt;ATP&gt;は重要な分子です。</think>ATPはアデノシン三リン酸（adenosine triphosphate）で、細胞内でエネルギー貯蔵と転送の役割を果たします。"""
+    
+    result2 = _decode_xml_entities(test_text2)
+    print("テストケース2:")
+    print(f"入力: {test_text2}")
+    print(f"出力: {result2}")
+    print(f"<think>タグが保持されているか: {'<think>' in result2 and '</think>' in result2}")
+    print(f"HTMLエンティティがデコードされているか: {'<ATP>' in result2}")
+    print()
+    
+    # テストケース3: 複数の<think>タグ
+    test_text3 = """<think>最初の思考プロセス</think>最初の回答<think>二番目の思考プロセス</think>追加の説明"""
+    
+    result3 = _decode_xml_entities(test_text3)
+    print("テストケース3:")
+    print(f"入力: {test_text3}")
+    print(f"出力: {result3}")
+    print(f"複数の<think>タグが保持されているか: {result3.count('<think>') == 2 and result3.count('</think>') == 2}")
+    print()
+    
+    # テストケース4: <think>タグなし、HTMLエンティティのみ
+    test_text4 = """これは&amp;普通の&lt;回答&gt;です。"""
+    
+    result4 = _decode_xml_entities(test_text4)
+    print("テストケース4:")
+    print(f"入力: {test_text4}")
+    print(f"出力: {result4}")
+    print(f"HTMLエンティティがデコードされているか: {'&' in result4 and '<回答>' in result4}")
+    print()
+
+if __name__ == "__main__":
+    test_think_tag_preservation()
diff --git a/tests/test_xml_parsing.py b/tests/test_xml_parsing.py
new file mode 100644
index 0000000..7183a79
--- /dev/null
+++ b/tests/test_xml_parsing.py
@@ -0,0 +1,121 @@
+#!/usr/bin/env python3
+"""XMLパース改善のテストスクリプト"""
+
+import sys
+import os
+sys.path.append(os.path.join(os.path.dirname(__file__), 'easy_dataset_cli'))
+
+from easy_dataset_cli.qa_generator import _parse_qa_response, _clean_llm_response
+from pathlib import Path
+import json
+
+def test_xml_parsing():
+    """XMLパースのテスト"""
+    
+    # テストケース1: 正常なXML
+    test_xml_1 = '''<QAPairs>
+<Pair>
+<Question>テスト質問1</Question>
+<Answer>テスト回答1</Answer>
+</Pair>
+<Pair>
+<Question>テスト質問2</Question>
+<Answer>テスト回答2</Answer>
+</Pair>
+</QAPairs>'''
+    
+    # テストケース2: バッククォート付きのXML（エラーの原因）
+    test_xml_2 = '''\```xml
+<QAPairs>
+<Pair>
+<Question>東方地霊殿はどんなジャンルのゲームですか？</Question>
+<Answer>弾幕系シューティングゲームで、横スクロールの弾幕を回避しながら敵を倒すタイプです。</Answer>
+</Pair>
+<Pair>
+<Question>このゲームはどのOSでプレイできますか？</Question>
+<Answer>Windows 2000、XP、Vista以降のPCで動作し、2020年にはSteam版も配信されています。</Answer>
+</Pair>
+<Pair>
+<Question>最低動作環境は何ですか？</Question>
+<Answer>CPUは1GHz以上のPentium、DirectX 9.0以上、メモリ256 MB、HDD空き容量600 MBが必要です。</Answer>
+</Pair>
+<Pair>
+<Question>インストール手順は簡単ですか？</Question>
+<Answer>Steam版ならアカウントにログインして「購入」→「インストール」ボタンを押すだけで自動インストールされます。</Answer>
+</Pair>
+</QAPairs>
+\```'''
+    
+    # テストケース3: <Pair>タグのみのXML
+    test_xml_3 = '''<Pair>
+<Question>Pairタグのみの質問1</Question>
+<Answer>Pairタグのみの回答1</Answer>
+</Pair>
+<Pair>
+<Question>Pairタグのみの質問2</Question>
+<Answer>Pairタグのみの回答2</Answer>
+</Pair>'''
+    
+    # テストケース4: 不完全なXML
+    test_xml_4 = '''<QAPairs>
+<Pair>
+<Question>不完全なXMLの質問</Question>
+<Answer>不完全なXMLの回答</Answer>
+</Pair>
+<QAPairs>'''
+    
+    print("=== XMLパース改善テスト ===\n")
+    
+    # テストケース1
+    print("テストケース1: 正常なXML")
+    result1 = _parse_qa_response(test_xml_1, None, None, None, None)
+    print(f"結果: {len(result1)}件のQ&Aを抽出")
+    for i, qa in enumerate(result1, 1):
+        print(f"  {i}. Q: {qa['question']}")
+        print(f"     A: {qa['answer']}")
+    print()
+    
+    # テストケース2
+    print("テストケース2: バッククォート付きのXML（元のエラー）")
+    result2 = _parse_qa_response(test_xml_2, None, None, None, None)
+    print(f"結果: {len(result2)}件のQ&Aを抽出")
+    for i, qa in enumerate(result2, 1):
+        print(f"  {i}. Q: {qa['question']}")
+        print(f"     A: {qa['answer']}")
+    print()
+    
+    # テストケース3
+    print("テストケース3: <Pair>タグのみのXML")
+    result3 = _parse_qa_response(test_xml_3, None, None, None, None)
+    print(f"結果: {len(result3)}件のQ&Aを抽出")
+    for i, qa in enumerate(result3, 1):
+        print(f"  {i}. Q: {qa['question']}")
+        print(f"     A: {qa['answer']}")
+    print()
+    
+    # テストケース4
+    print("テストケース4: 不完全なXML")
+    result4 = _parse_qa_response(test_xml_4, None, None, None, None)
+    print(f"結果: {len(result4)}件のQ&Aを抽出")
+    for i, qa in enumerate(result4, 1):
+        print(f"  {i}. Q: {qa['question']}")
+        print(f"     A: {qa['answer']}")
+    print()
+    
+    # クリーニング機能のテスト
+    print("=== クリーニング機能テスト ===")
+    cleaned = _clean_llm_response(test_xml_2)
+    print("クリーニング前:")
+    print(test_xml_2[:200] + "...")
+    print("\nクリーニング後:")
+    print(cleaned[:200] + "...")
+    
+    return len(result1) > 0 and len(result2) > 0 and len(result3) > 0
+
+if __name__ == "__main__":
+    success = test_xml_parsing()
+    if success:
+        print("\n✅ すべてのテストが成功しました！")
+    else:
+        print("\n❌ テストに失敗しました。")
+    sys.exit(0 if success else 1)
```
