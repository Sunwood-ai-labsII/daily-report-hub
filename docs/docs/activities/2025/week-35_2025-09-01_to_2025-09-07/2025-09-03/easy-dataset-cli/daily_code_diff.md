# 💻 Daily Code Changes

## Full Diff

```diff
diff --git a/easy_dataset_cli/batch_process.py b/easy_dataset_cli/batch_process.py
index 8c01d5e..edcec6d 100644
--- a/easy_dataset_cli/batch_process.py
+++ b/easy_dataset_cli/batch_process.py
@@ -5,7 +5,7 @@
 
 from pathlib import Path
 from rich.console import Console
-from rich.progress import Progress
+from tqdm import tqdm
 
 from .core import (
     parse_ga_file,
@@ -37,10 +37,7 @@ def _batch_create_ga_files(text_files, output_dir, model, num_ga_pairs, max_cont
     total_files = len(text_files)
     successful_files = []
 
-    with Progress(console=console) as progress:
-        main_task = progress.add_task("[green]GAペアを生成中...", total=total_files)
-
-        for file_idx, text_file in enumerate(text_files):
+    for text_file in (tqdm(text_files, desc="GA生成中")):
             console.print(f"\n[bold cyan]処理中: {text_file.name}[/bold cyan]")
 
             try:
@@ -87,10 +84,51 @@ def _batch_create_ga_files(text_files, output_dir, model, num_ga_pairs, max_cont
                 console.print(f"[red]エラー: {text_file.name} の処理に失敗しました: {e}[/red]")
                 continue
 
-            progress.update(
-                main_task, advance=1,
-                description=f"完了: {text_file.name}"
-            )
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
 
     if not successful_files:
         print_error_panel("有効なGAペアが生成されませんでした。\n生成されたXMLの内容を確認してください。")
@@ -171,10 +209,7 @@ def _batch_process_files(text_files, ga_file, ga_base_dir, output_dir, model, ch
     successful_files = []
     total_qa_pairs_generated = 0
 
-    with Progress(console=console) as progress:
-        main_task = progress.add_task("[green]ファイルを処理中...", total=total_files)
-
-        for file_idx, text_file in enumerate(text_files):
+    for text_file in (tqdm(text_files, desc="ファイル処理中")):
             console.print(f"\n[bold cyan]処理中: {text_file.name}[/bold cyan]")
 
             try:
@@ -227,7 +262,10 @@ def _batch_process_files(text_files, ga_file, ga_base_dir, output_dir, model, ch
 
                 all_qa_pairs_with_ga = []
                 total_tasks_for_file = len(chunks) * len(current_ga_pairs)
-                file_task = progress.add_task(f"[blue]{text_file.name}", total=total_tasks_for_file)
+                # tqdmサブバー
+                from tqdm import tqdm as _tqdm
+                pbar_ctx = _tqdm(total=total_tasks_for_file, desc=text_file.name, leave=False)
+                # 進捗の更新は後続のループ内で行う
 
                 if use_surrounding_context:
                     # 周辺コンテキストモードの処理
@@ -256,10 +294,7 @@ def _batch_process_files(text_files, ga_file, ga_base_dir, output_dir, model, ch
                                 }
                                 all_qa_pairs_with_ga.append(qa_entry)
 
-                            progress.update(
-                                file_task, advance=1,
-                                description=f"Genre: {ga_pair['genre']['title']}"
-                            )
+                            pbar_ctx.update(1)
                 else:
                     # 通常モードの処理
                     for chunk in chunks:
@@ -298,12 +333,9 @@ def _batch_process_files(text_files, ga_file, ga_base_dir, output_dir, model, ch
                                 }
                                 all_qa_pairs_with_ga.append(qa_entry)
 
-                            progress.update(
-                                file_task, advance=1,
-                                description=f"Genre: {ga_pair['genre']['title']}"
-                            )
-
-                progress.remove_task(file_task)
+                            pbar_ctx.update(1)
+                # close tqdm sub-bar if used
+                pbar_ctx.close()
 
                 # このファイルのQ&AペアをXMLに変換して保存
                 xml_outputs_by_genre = convert_to_xml_by_genre(all_qa_pairs_with_ga, dirs["qa"], append_mode)
@@ -334,10 +366,7 @@ def _batch_process_files(text_files, ga_file, ga_base_dir, output_dir, model, ch
                 console.print(f"[red]エラー: {text_file.name} の処理に失敗しました: {e}[/red]")
                 continue
 
-            progress.update(
-                main_task, advance=1,
-                description=f"完了: {text_file.name}"
-            )
+    # tqdmで外側ループ済み
 
     if not successful_files:
         from .commands import print_error_panel
diff --git a/easy_dataset_cli/commands.py b/easy_dataset_cli/commands.py
index 89a7e3d..3c96394 100644
--- a/easy_dataset_cli/commands.py
+++ b/easy_dataset_cli/commands.py
@@ -7,7 +7,6 @@ from pathlib import Path
 from typing_extensions import Annotated
 import typer
 from rich.console import Console
-from rich.progress import Progress
 from rich.text import Text
 from rich.panel import Panel
 from rich.columns import Columns
@@ -445,16 +444,15 @@ def generate(
             )
             console.print(warning_panel)
 
-        with Progress(console=console) as progress:
-            task = progress.add_task("[green]Q&Aペアを生成中...", total=total_tasks)
-
+        # tqdmベースの進捗表示に統一
+        from tqdm import tqdm
+        desc = "Q&A生成中"
+        iterable_outer = augmented_chunks if use_surrounding_context else chunks
+        with tqdm(total=total_tasks, desc=desc) as pbar:
             if use_surrounding_context:
-                # 周辺コンテキストモードの処理
-                # ドキュメント冒頭（最大3000文字）を付与して文脈の安定性を高める
                 doc_head = text[:3000]
-                for i, (target_chunk, augmented_content, _) in enumerate(augmented_chunks):
+                for i, (target_chunk, augmented_content, _) in enumerate(iterable_outer):
                     for ga_pair in ga_pairs:
-                        # 冒頭 + 既存の周辺文脈を結合
                         content_with_head = (
                             f"### 【ドキュメント冒頭（最大3000文字）】-----------:\n\```\n{doc_head}\n\```\n" +
                             augmented_content
@@ -476,13 +474,9 @@ def generate(
                             }
                             all_qa_pairs_with_ga.append(qa_entry)
 
-                        progress.update(
-                            task, advance=1,
-                            description=f"Genre: {ga_pair['genre']['title']}"
-                        )
+                        pbar.update(1)
             else:
-                # 通常モードの処理
-                for chunk in chunks:
+                for chunk in iterable_outer:
                     for ga_pair in ga_pairs:
                         if use_thinking:
                             qa_pairs = generate_qa_for_chunk_with_ga_and_thinking(
@@ -518,10 +512,7 @@ def generate(
                             }
                             all_qa_pairs_with_ga.append(qa_entry)
 
-                        progress.update(
-                            task, advance=1,
-                            description=f"Genre: {ga_pair['genre']['title']}"
-                        )
+                        pbar.update(1)
 
         generation_summary = Panel(
             f"✨ [bold green]{len(all_qa_pairs_with_ga)}[/bold green] 個のQ&Aペアを生成完了！",
diff --git a/pyproject.toml b/pyproject.toml
index 60a7946..3643071 100644
--- a/pyproject.toml
+++ b/pyproject.toml
@@ -1,6 +1,6 @@
 [project]
 name = "easy-dataset-cli"
-version = "1.0.0"
+version = "1.1.0"
 description = "A simple CLI tool to generate QA pairs from a text file using LLMs and GA pairs, outputting genre-specific XML files."
 requires-python = ">=3.9"
 dependencies = [
@@ -12,7 +12,8 @@ dependencies = [
     "mistune",             # マークダウン解析用ライブラリ
     "python-dotenv",       # .env ファイル読み込み用
     "huggingface-hub",     # Hugging Face Hub API
-    "datasets"             # Hugging Face Datasets
+    "datasets",            # Hugging Face Datasets
+    "tqdm"                 # プログレスバー表示
 ]
 
 [project.scripts]
@@ -22,3 +23,19 @@ easy-dataset = "easy_dataset_cli.main:main"
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
