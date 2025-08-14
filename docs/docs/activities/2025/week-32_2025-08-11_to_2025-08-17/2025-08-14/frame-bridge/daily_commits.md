# 📝 Daily Commits

## ⏰ 14:15:44 - `08d41d2`
**Initial commit**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Thu Aug 14 14:15:44 2025 +0900
A	.SourceSageignore
A	.dockerignore
A	.github/workflows/sync-to-hf.yml
A	.github/workflows/sync-to-report-gh.yml
A	.gitignore
A	Dockerfile
A	LICENSE
A	README.md
A	app.py
A	docker-compose.dev.yml
A	docker-compose.yml
A	requirements.txt
A	theme.py
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Thu Aug 14 14:15:44 2025 +0900

    Initial commit

 .SourceSageignore                       |  54 ++++
 .dockerignore                           |  56 +++++
 .github/workflows/sync-to-hf.yml        |  32 +++
 .github/workflows/sync-to-report-gh.yml |  52 ++++
 .gitignore                              | 208 +++++++++++++++
 Dockerfile                              |  28 +++
 LICENSE                                 |  21 ++
 README.md                               | 174 +++++++++++++
 app.py                                  | 431 ++++++++++++++++++++++++++++++++
 docker-compose.dev.yml                  |  25 ++
 docker-compose.yml                      |  27 ++
 requirements.txt                        |   4 +
 theme.py                                |  44 ++++
 13 files changed, 1156 insertions(+)
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
```

---

## ⏰ 14:16:50 - `967613d`
**Update sync-to-hf.yml**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Thu Aug 14 14:16:50 2025 +0900
M	.github/workflows/sync-to-hf.yml
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Thu Aug 14 14:16:50 2025 +0900

    Update sync-to-hf.yml

 .github/workflows/sync-to-hf.yml | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/sync-to-hf.yml b/.github/workflows/sync-to-hf.yml
index 5879e47..dca6955 100644
--- a/.github/workflows/sync-to-hf.yml
+++ b/.github/workflows/sync-to-hf.yml
@@ -26,7 +26,7 @@ jobs:
           git config --global user.name "GitHub Action"
           
           # Hugging Face Hubにリモートを追加
-          git remote add hf https://huggingface.co/spaces/MakiAi/wikipedia-to-markdown
+          git remote add hf https://huggingface.co/spaces/MakiAi/frame-bridge
           
           # 強制プッシュでHugging Faceに同期
-          git push --force https://user:$HF_TOKEN@huggingface.co/spaces/MakiAi/wikipedia-to-markdown HEAD:main
+          git push --force https://user:$HF_TOKEN@huggingface.co/spaces/MakiAi/frame-bridge HEAD:main
```

---

## ⏰ 14:25:24 - `b5598cb`
**Update README.md**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Thu Aug 14 14:25:24 2025 +0900
M	README.md
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Thu Aug 14 14:25:24 2025 +0900

    Update README.md

 README.md | 10 +++++-----
 1 file changed, 5 insertions(+), 5 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/README.md b/README.md
index a46db06..e3aa9ca 100644
--- a/README.md
+++ b/README.md
@@ -1,12 +1,12 @@
 ---
 license: mit
-title: wikipedia to markdown
+title: frame bridge
 sdk: gradio
-emoji: 📚
-colorFrom: yellow
-colorTo: gray
+emoji: 🏆
+colorFrom: red
+colorTo: indigo
 thumbnail: >-
-  https://cdn-uploads.huggingface.co/production/uploads/64e0ef4a4c78e1eba5178d7a/vJQZ24fctExV3dax_BGU-.jpeg
+  https://cdn-uploads.huggingface.co/production/uploads/64e0ef4a4c78e1eba5178d7a/BZfofcX1vEF7kwWQ0i-uB.png
 sdk_version: 5.42.0
 ---
 
```

---

## ⏰ 14:26:05 - `72358ac`
**Update README.md**
*by Maki*

### 📋 Changed Files
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Thu Aug 14 14:26:05 2025 +0900
M	README.md
```

### 📊 Statistics
```bash
Author: Maki <108736814+Sunwood-ai-labs@users.noreply.github.com>
Date:   Thu Aug 14 14:26:05 2025 +0900

    Update README.md

 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/README.md b/README.md
index e3aa9ca..9edb370 100644
--- a/README.md
+++ b/README.md
@@ -12,7 +12,7 @@ sdk_version: 5.42.0
 
 <div align="center">
 
-![Wikipedia to Markdown Converter](https://github.com/user-attachments/assets/201c0b39-6bf7-4599-a62a-dd3e6f61e5f8)
+![frame-bridge](https://github.com/user-attachments/assets/05977e5b-3e63-4ed2-a5f6-74ada8943994)
 
 # 📚 Wikipedia to Markdown Converter
 
```

---

## ⏰ 15:22:18 - `31b3477`
**🔧 プロジェクト設定とパッケージ依存関係の更新**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Thu Aug 14 15:22:18 2025 +0900
M	.gitignore
A	pyproject.toml
M	requirements.txt
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Thu Aug 14 15:22:18 2025 +0900

    🔧 プロジェクト設定とパッケージ依存関係の更新
    
    - pyproject.tomlを追加してプロジェクト構成を定義
    - requirements.txtを動画処理用ライブラリに変更（OpenCV、NumPy、Pillow、scikit-image）
    - .gitignoreに動画ファイルとバッチ処理結果を追加

 .gitignore       |   5 ++
 pyproject.toml   | 163 +++++++++++++++++++++++++++++++++++++++++++++++++++++++
 requirements.txt |   7 ++-
 3 files changed, 172 insertions(+), 3 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/.gitignore b/.gitignore
index 16c3c78..5580869 100644
--- a/.gitignore
+++ b/.gitignore
@@ -206,3 +206,8 @@ marimo/_static/
 marimo/_lsp/
 __marimo__/
 .SourceSageAssets/
+assets/*.mp4
+uv.lock
+assets/example/REI/input/*.mp4
+assets/example/REI/output/*.mp4
+assets/example/REI/output/batch_report.txt
diff --git a/pyproject.toml b/pyproject.toml
new file mode 100644
index 0000000..7ca8550
--- /dev/null
+++ b/pyproject.toml
@@ -0,0 +1,163 @@
+[build-system]
+requires = ["setuptools>=61.0", "wheel"]
+build-backend = "setuptools.build_meta"
+
+[project]
+name = "frame-bridge"
+version = "1.0.0"
+description = "AI-powered video frame bridging application using SSIM technology"
+readme = "README.md"
+license = {text = "MIT"}
+authors = [
+    {name = "Sunwood AI Labs", email = "info@sunwood-ai-labs.com"}
+]
+maintainers = [
+    {name = "Sunwood AI Labs", email = "info@sunwood-ai-labs.com"}
+]
+keywords = [
+    "video-processing",
+    "ai",
+    "computer-vision",
+    "gradio",
+    "opencv",
+    "ssim",
+    "frame-analysis",
+    "video-editing"
+]
+classifiers = [
+    "Development Status :: 4 - Beta",
+    "Intended Audience :: Developers",
+    "Intended Audience :: End Users/Desktop",
+    "License :: OSI Approved :: MIT License",
+    "Operating System :: OS Independent",
+    "Programming Language :: Python :: 3",
+
+    "Programming Language :: Python :: 3.10",
+    "Programming Language :: Python :: 3.11",
+    "Topic :: Multimedia :: Video",
+    "Topic :: Multimedia :: Video :: Display",
+    "Topic :: Scientific/Engineering :: Artificial Intelligence",
+    "Topic :: Scientific/Engineering :: Image Processing",
+]
+requires-python = ">=3.10"
+dependencies = [
+    "opencv-python>=4.8.0",
+    "numpy>=1.24.0",
+    "pillow>=10.0.0",
+    "gradio>=5.42.0",
+    "scikit-image>=0.21.0",
+]
+
+[project.optional-dependencies]
+dev = [
+    "pytest>=7.0.0",
+    "pytest-cov>=4.0.0",
+    "black>=23.0.0",
+    "flake8>=6.0.0",
+    "mypy>=1.0.0",
+    "pre-commit>=3.0.0",
+]
+docs = [
+    "sphinx>=6.0.0",
+    "sphinx-rtd-theme>=1.2.0",
+    "myst-parser>=1.0.0",
+]
+
+[project.urls]
+Homepage = "https://github.com/Sunwood-ai-labsII/frame-bridge"
+Repository = "https://github.com/Sunwood-ai-labsII/frame-bridge.git"
+Documentation = "https://github.com/Sunwood-ai-labsII/frame-bridge#readme"
+"Bug Tracker" = "https://github.com/Sunwood-ai-labsII/frame-bridge/issues"
+"Demo Site" = "https://huggingface.co/spaces/MakiAi/frame-bridge"
+
+[project.scripts]
+frame-bridge = "app:main"
+frame-bridge-test = "test_sample:main"
+frame-bridge-batch = "batch_test:main"
+
+[tool.setuptools.packages.find]
+where = ["."]
+include = ["*"]
+exclude = ["tests*", "docs*", ".github*"]
```

---

## ⏰ 15:22:30 - `60a1a3b`
**✨ 動画フレーム結合のコアモジュール実装**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Thu Aug 14 15:22:30 2025 +0900
A	src/frame_bridge/__init__.py
A	src/frame_bridge/batch_processor.py
A	src/frame_bridge/config.py
A	src/frame_bridge/video_processor.py
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Thu Aug 14 15:22:30 2025 +0900

    ✨ 動画フレーム結合のコアモジュール実装
    
    - VideoProcessorクラス: SSIM技術による高精度フレーム類似度計算
    - FrameBridgeクラス: 2つの動画の最適接続点検出と結合機能
    - BatchProcessorクラス: 複数動画の順次結合・ペア結合処理
    - 設定管理とパッケージ初期化ファイルを追加

 src/frame_bridge/__init__.py        |  20 ++
 src/frame_bridge/batch_processor.py | 311 ++++++++++++++++++++++++++++
 src/frame_bridge/config.py          |  46 +++++
 src/frame_bridge/video_processor.py | 399 ++++++++++++++++++++++++++++++++++++
 4 files changed, 776 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/src/frame_bridge/__init__.py b/src/frame_bridge/__init__.py
new file mode 100644
index 0000000..19144ea
--- /dev/null
+++ b/src/frame_bridge/__init__.py
@@ -0,0 +1,20 @@
+"""
+Frame Bridge - AI-powered video frame bridging application
+2つの動画を最適なフレームで自動結合するAIアプリケーション
+"""
+
+__version__ = "1.0.0"
+__author__ = "Sunwood AI Labs"
+__email__ = "info@sunwood-ai-labs.com"
+
+from .video_processor import VideoProcessor, FrameBridge
+from .batch_processor import BatchProcessor
+
+__all__ = [
+    "VideoProcessor",
+    "FrameBridge", 
+    "BatchProcessor",
+    "__version__",
+    "__author__",
+    "__email__"
+]
\ No newline at end of file
diff --git a/src/frame_bridge/batch_processor.py b/src/frame_bridge/batch_processor.py
new file mode 100644
index 0000000..d808640
--- /dev/null
+++ b/src/frame_bridge/batch_processor.py
@@ -0,0 +1,311 @@
+"""
+Frame Bridge - Batch Processing Module
+フォルダ内の動画ファイルを順次結合するバッチ処理モジュール
+"""
+
+import os
+import glob
+import logging
+from pathlib import Path
+from typing import List, Tuple, Optional
+from .video_processor import FrameBridge
+
+# ログ設定
+logging.basicConfig(level=logging.INFO)
+logger = logging.getLogger(__name__)
+
+
+class BatchProcessor:
+    """バッチ処理を行うクラス"""
+    
+    def __init__(self, output_dir: str = "output", exclude_edge_frames: bool = True):
+        """
+        初期化
+        
+        Args:
+            output_dir: 出力ディレクトリ
+            exclude_edge_frames: 最初と最後のフレームを除外するかどうか
+        """
+        self.frame_bridge = FrameBridge(exclude_edge_frames=exclude_edge_frames)
+        self.output_dir = Path(output_dir)
+        self.output_dir.mkdir(exist_ok=True)
+        self.exclude_edge_frames = exclude_edge_frames
+        
+        # サポートする動画形式
+        self.supported_formats = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm']
+    
+    def get_video_files(self, input_dir: str) -> List[str]:
+        """
+        指定ディレクトリから動画ファイルを取得し、名前順にソート
+        
+        Args:
+            input_dir: 入力ディレクトリ
+            
+        Returns:
+            ソートされた動画ファイルのリスト
+        """
+        input_path = Path(input_dir)
+        if not input_path.exists():
+            logger.error(f"入力ディレクトリが存在しません: {input_dir}")
+            return []
+        
+        video_files = []
+        for ext in self.supported_formats:
+            pattern = str(input_path / f"*{ext}")
+            video_files.extend(glob.glob(pattern))
+        
+        # ファイル名でソート（自然順序）
+        video_files.sort(key=lambda x: os.path.basename(x).lower())
+        
+        logger.info(f"検出された動画ファイル数: {len(video_files)}")
+        for i, file in enumerate(video_files):
+            logger.info(f"  {i+1}. {os.path.basename(file)}")
+        
+        return video_files
+    
+    def process_sequential_merge(self, input_dir: str, output_filename: str = "merged_sequence.mp4") -> Tuple[bool, str, List[dict]]:
+        """
```

---

## ⏰ 15:22:42 - `0afaece`
**🧪 テストファイルとバッチ処理テストの追加**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Thu Aug 14 15:22:42 2025 +0900
A	tests/batch_test.py
A	tests/test_sample.py
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Thu Aug 14 15:22:42 2025 +0900

    🧪 テストファイルとバッチ処理テストの追加
    
    - batch_test.py: バッチ処理機能の動作確認テスト
    - test_sample.py: サンプル動画を使用した基本機能テスト
    - 動画結合機能の品質保証とデバッグ支援

 tests/batch_test.py  | 96 ++++++++++++++++++++++++++++++++++++++++++++++++++++
 tests/test_sample.py | 72 +++++++++++++++++++++++++++++++++++++++
 2 files changed, 168 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/tests/batch_test.py b/tests/batch_test.py
new file mode 100644
index 0000000..b81b58b
--- /dev/null
+++ b/tests/batch_test.py
@@ -0,0 +1,96 @@
+"""
+Frame Bridge - バッチ処理テスト用スクリプト
+フォルダ内の動画ファイルを順次結合するテストスクリプト
+"""
+
+import os
+import sys
+import argparse
+from pathlib import Path
+import sys
+sys.path.append('..')
+from src.frame_bridge import BatchProcessor
+
+def main():
+    """メイン処理"""
+    parser = argparse.ArgumentParser(description="Frame Bridge - バッチ動画結合")
+    parser.add_argument("--input", "-i", default="examples/assets/example/REI/input", help="入力フォルダ (デフォルト: examples/assets/example/REI/input)")
+    parser.add_argument("--output", "-o", default="examples/assets/example/REI/output", help="出力フォルダ (デフォルト: examples/assets/example/REI/output)")
+    parser.add_argument("--exclude-edge", action="store_true", default=True, help="最初と最後のフレームを除外 (デフォルト: True)")
+    parser.add_argument("--include-edge", action="store_true", help="最初と最後のフレームを含める")
+    parser.add_argument("--mode", "-m", choices=["sequential", "pairwise"], default="sequential", 
+                       help="結合モード: sequential(順次結合) または pairwise(ペア結合)")
+    parser.add_argument("--filename", "-f", default="merged_sequence.mp4", help="出力ファイル名 (sequentialモードのみ)")
+    
+    args = parser.parse_args()
+    
+    print("🎬 Frame Bridge - バッチ処理テスト")
+    print("=" * 60)
+    print(f"📁 入力フォルダ: {args.input}")
+    print(f"📁 出力フォルダ: {args.output}")
+    print(f"🔄 処理モード: {args.mode}")
+    if args.mode == "sequential":
+        print(f"📄 出力ファイル名: {args.filename}")
+    print()
+    
+    # 入力フォルダの存在チェック
+    if not os.path.exists(args.input):
+        print(f"❌ 入力フォルダが見つかりません: {args.input}")
+        return
+    
+    # エッジフレーム除外設定
+    exclude_edge_frames = not args.include_edge if args.include_edge else args.exclude_edge
+    
+    print(f"🎯 エッジフレーム除外: {'有効' if exclude_edge_frames else '無効'}")
+    print()
+    
+    # バッチプロセッサを初期化
+    processor = BatchProcessor(output_dir=args.output, exclude_edge_frames=exclude_edge_frames)
+    
+    # 動画ファイルの確認
+    video_files = processor.get_video_files(args.input)
+    if len(video_files) < 2:
+        print("❌ 結合には最低2つの動画ファイルが必要です")
+        return
+    
+    print(f"✅ 検出された動画ファイル: {len(video_files)}個")
+    for i, file in enumerate(video_files):
+        print(f"  {i+1}. {os.path.basename(file)}")
+    print()
+    
+    # 処理モードに応じて実行
+    if args.mode == "sequential":
+        print("🔄 順次結合処理を開始...")
+        success, final_output, results = processor.process_sequential_merge(args.input, args.filename)
+        
+        if success:
+            print(f"✅ 順次結合完了!")
+            print(f"📁 最終出力: {final_output}")
+            print(f"📊 ファイルサイズ: {os.path.getsize(final_output) / (1024*1024):.1f} MB")
+        else:
+            print("❌ 順次結合に失敗しました")
+    
+    elif args.mode == "pairwise":
+        print("🔄 ペアワイズ結合処理を開始...")
+        success, output_files, results = processor.process_pairwise_merge(args.input)
+        
+        if success:
+            print(f"✅ ペアワイズ結合完了!")
+            print(f"📁 出力ファイル数: {len(output_files)}")
+            for i, file in enumerate(output_files):
+                size_mb = os.path.getsize(file) / (1024*1024)
+                print(f"  {i+1}. {os.path.basename(file)} ({size_mb:.1f} MB)")
+        else:
+            print("❌ ペアワイズ結合に失敗しました")
+    
+    # レポート生成
+    print("\n" + "=" * 60)
+    print("📋 処理レポート:")
+    report_path = Path(args.output) / "batch_report.txt"
+    report = processor.generate_report(results, str(report_path))
+    print(report)
+    
+    print("🎉 バッチ処理完了！")
+
```

---

## ⏰ 15:22:54 - `b9e21c9`
**🛠️ プロジェクト構造表示スクリプトの追加**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Thu Aug 14 15:22:54 2025 +0900
A	scripts/show_structure.py
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Thu Aug 14 15:22:54 2025 +0900

    🛠️ プロジェクト構造表示スクリプトの追加
    
    - show_structure.py: プロジェクトのディレクトリ構造を可視化
    - 開発時のファイル構成確認とドキュメント作成支援
    - プロジェクト管理の効率化

 scripts/show_structure.py | 58 +++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 58 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/scripts/show_structure.py b/scripts/show_structure.py
new file mode 100644
index 0000000..218c552
--- /dev/null
+++ b/scripts/show_structure.py
@@ -0,0 +1,58 @@
+"""
+Frame Bridge - Project Structure Display
+プロジェクト構造を表示するスクリプト
+"""
+
+import os
+from pathlib import Path
+
+def show_tree(directory, prefix="", max_depth=3, current_depth=0):
+    """ディレクトリツリーを表示"""
+    if current_depth > max_depth:
+        return
+    
+    directory = Path(directory)
+    if not directory.exists():
+        return
+    
+    items = sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
+    
+    for i, item in enumerate(items):
+        is_last = i == len(items) - 1
+        current_prefix = "└── " if is_last else "├── "
+        
+        if item.is_dir():
+            print(f"{prefix}{current_prefix}{item.name}/")
+            extension = "    " if is_last else "│   "
+            show_tree(item, prefix + extension, max_depth, current_depth + 1)
+        else:
+            print(f"{prefix}{current_prefix}{item.name}")
+
+def main():
+    """メイン処理"""
+    print("🎬 Frame Bridge - プロジェクト構造")
+    print("=" * 60)
+    
+    # プロジェクトルートから表示
+    project_root = Path(__file__).parent.parent
+    os.chdir(project_root)
+    
+    print("📁 プロジェクト構造:")
+    print("frame-bridge/")
+    show_tree(".", max_depth=3)
+    
+    print("\n" + "=" * 60)
+    print("📊 主要コンポーネント:")
+    print("• src/frame_bridge/     - メインライブラリ")
+    print("• scripts/              - 実行スクリプト")
+    print("• tests/                - テストファイル")
+    print("• examples/             - サンプルデータ")
+    print("• docs/                 - ドキュメント")
+    
+    print("\n🎯 新機能:")
+    print("• エッジフレーム除外オプション")
+    print("• 最適化されたフォルダ構造")
+    print("• 設定管理システム")
+
+if __name__ == "__main__":
+    main()
\ No newline at end of file
```

---

## ⏰ 15:23:05 - `8a75a03`
**🐳 Docker設定をOpenCV対応に更新**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Thu Aug 14 15:23:05 2025 +0900
M	Dockerfile
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Thu Aug 14 15:23:05 2025 +0900

    🐳 Docker設定をOpenCV対応に更新
    
    - OpenCV動作に必要なシステムライブラリを追加
    - libglib2.0、libsm6、libxext6、libxrender-dev等を導入
    - 動画処理とGUI表示のためのライブラリ環境を整備

 Dockerfile | 12 +++++++++++-
 1 file changed, 11 insertions(+), 1 deletion(-)
```

### 💻 Code Changes
```diff
diff --git a/Dockerfile b/Dockerfile
index 9021fbf..bd72ebe 100644
--- a/Dockerfile
+++ b/Dockerfile
@@ -4,8 +4,18 @@ FROM python:3.11-slim
 # 作業ディレクトリを設定
 WORKDIR /app
 
-# システムパッケージの更新とクリーンアップ
+# システムパッケージの更新とOpenCV用ライブラリをインストール
 RUN apt-get update && apt-get install -y \
+    libglib2.0-0 \
+    libsm6 \
+    libxext6 \
+    libxrender-dev \
+    libgomp1 \
+    libglib2.0-0 \
+    libgtk-3-0 \
+    libavcodec-dev \
+    libavformat-dev \
+    libswscale-dev \
     && rm -rf /var/lib/apt/lists/*
 
 # 依存関係ファイルをコピー
```

---

## ⏰ 15:23:18 - `9bf175f`
**🎬 メインアプリケーションを動画結合アプリに完全変更**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Thu Aug 14 15:23:18 2025 +0900
M	app.py
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Thu Aug 14 15:23:18 2025 +0900

    🎬 メインアプリケーションを動画結合アプリに完全変更
    
    - Wikipedia変換からFrame Bridge動画結合アプリに機能転換
    - 単体処理: 2つの動画の最適フレーム検出・結合機能
    - バッチ処理: 順次結合・ペア結合モードでの一括処理
    - リアルタイム動画情報表示と類似度スコア可視化

 app.py | 565 ++++++++++++++++++++++++-----------------------------------------
 1 file changed, 210 insertions(+), 355 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/app.py b/app.py
index cd88a94..deb494d 100644
--- a/app.py
+++ b/app.py
@@ -1,418 +1,273 @@
-import requests
-from bs4 import BeautifulSoup
-import html2text
-import re
 import gradio as gr
 from theme import create_zen_theme
-import tempfile
+from src.frame_bridge import FrameBridge, BatchProcessor
 import os
-import zipfile
-from urllib.parse import urlparse, unquote
 
-def scrape_wikipedia_to_markdown_final(url: str) -> str:
-    """
-    Wikipediaページをスクレイピングし、整形・不要部分削除を行い、
-    タイトルを付けてMarkdownに変換します。
+# Frame Bridge インスタンスを作成
+frame_bridge = FrameBridge(exclude_edge_frames=True)
+batch_processor = BatchProcessor(exclude_edge_frames=True)
 
-    処理フロー：
-    1. ページのタイトルをH1見出しとして取得します。
-    2. 「登場人物」などの<dt>タグを見出しに変換します。
-    3. 生成されたMarkdown文字列から「## 脚注」以降を完全に削除します。
-    4. [編集]リンクを削除します。
-    5. 最終的にタイトルと本文を結合して返します。
-
-    Args:
-        url (str): スクレイピング対象のWikipediaページのURL。
-
-    Returns:
-        str: 整形・変換された最終的なMarkdownコンテンツ。失敗した場合は空の文字列。
-    """
-    try:
-        # 1. HTMLの取得と解析
-        headers = {
-            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
-        }
-        response = requests.get(url, headers=headers)
-        response.raise_for_status()  # HTTPエラーがあれば例外を発生させる
-        response.encoding = response.apparent_encoding  # 文字コードを自動検出
-        soup = BeautifulSoup(response.text, 'html.parser')
-
-        # --- ページのタイトルを取得 ---
-        title_tag = soup.find('h1', id='firstHeading')
-        page_title = title_tag.get_text(strip=True) if title_tag else "Wikipedia ページ"
-
-        # 2. 主要コンテンツエリアの特定
-        content_div = soup.find('div', class_='mw-parser-output')
-        if not content_div:
-            return "エラー: コンテンツエリアが見つかりませんでした。"
-
-        # 3. HTMLの事前整形（登場人物などの見出し化）
-        for dt_tag in content_div.find_all('dt'):
-            h4_tag = soup.new_tag('h4')
-            h4_tag.extend(dt_tag.contents)
-            dt_tag.replace_with(h4_tag)
-
-        # 4. HTMLからMarkdownへの一次変換
-        h = html2text.HTML2Text()
-        h.body_width = 0  # テキストの折り返しを無効にする
-        full_markdown_text = h.handle(str(content_div))
-
-        # 5. 生成されたMarkdownから「## 脚注」以降を削除
-        footnote_marker = "\n## 脚注"
-        footnote_index = full_markdown_text.find(footnote_marker)
-        body_text = full_markdown_text[:footnote_index] if footnote_index != -1 else full_markdown_text
-
-        # 6. [編集]リンクを正規表現で一括削除
-        cleaned_body = re.sub(r'\[\[編集\]\(.+?\)]\n', '', body_text)
-
-        # 7. タイトルと整形後の本文を結合
-        final_markdown = f"# {page_title}\n\n{cleaned_body.strip()}"
-
-        return final_markdown
-
-    except requests.exceptions.RequestException as e:
-        return f"HTTPリクエストエラー: {e}"
-    except Exception as e:
-        return f"予期せぬエラーが発生しました: {e}"
-
-def get_filename_from_url(url):
-    """URLからファイル名を生成する関数"""
-    try:
-        # URLからページ名を抽出
-        parsed_url = urlparse(url)
-        page_name = parsed_url.path.split('/')[-1]
-        # URLデコード
-        page_name = unquote(page_name)
-        # ファイル名として使用できない文字を置換
-        safe_filename = re.sub(r'[<>:"/\\|?*]', '_', page_name)
-        return f"{safe_filename}.md"
-    except:
-        return "wikipedia_page.md"
+def process_sample_videos():
```

---

## ⏰ 15:23:30 - `20b74c6`
**📚 READMEをFrame Bridgeアプリ用に全面更新**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Thu Aug 14 15:23:30 2025 +0900
M	README.md
```

### 📊 Statistics
```bash
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Thu Aug 14 15:23:30 2025 +0900

    📚 READMEをFrame Bridgeアプリ用に全面更新
    
    - プロジェクト概要をAI動画結合アプリに変更
    - SSIM技術による高精度フレーム類似度計算の説明追加
    - 単体処理・バッチ処理の詳細な使用方法を記載
    - 技術的特徴と処理フローの詳細説明を追加

 README.md | 109 +++++++++++++++++++++++++++++++-------------------------------
 1 file changed, 55 insertions(+), 54 deletions(-)
```

### 💻 Code Changes
```diff
diff --git a/README.md b/README.md
index 9edb370..5793df9 100644
--- a/README.md
+++ b/README.md
@@ -2,9 +2,9 @@
 license: mit
 title: frame bridge
 sdk: gradio
-emoji: 🏆
-colorFrom: red
-colorTo: indigo
+emoji: 🎬
+colorFrom: purple
+colorTo: blue
 thumbnail: >-
   https://cdn-uploads.huggingface.co/production/uploads/64e0ef4a4c78e1eba5178d7a/BZfofcX1vEF7kwWQ0i-uB.png
 sdk_version: 5.42.0
@@ -14,14 +14,15 @@ sdk_version: 5.42.0
 
 ![frame-bridge](https://github.com/user-attachments/assets/05977e5b-3e63-4ed2-a5f6-74ada8943994)
 
-# 📚 Wikipedia to Markdown Converter
+# 🎬 Frame Bridge
 
-*WikipediaページをMarkdown形式に変換するWebアプリケーション*
+*2つの動画を最適なフレームで自動結合するAIアプリケーション*
 
 [![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
+[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)
 [![Gradio](https://img.shields.io/badge/Gradio-5.42+-FF6B6B?style=for-the-badge&logo=gradio&logoColor=white)](https://gradio.app)
 [![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
-[![Demo](https://img.shields.io/badge/🚀%20デモサイト-Live-orange?style=for-the-badge)](https://huggingface.co/spaces/MakiAi/wikipedia-to-markdown)
+[![Demo](https://img.shields.io/badge/🚀%20デモサイト-Live-orange?style=for-the-badge)](https://huggingface.co/spaces/MakiAi/frame-bridge)
 
 </div>
 
@@ -29,29 +30,29 @@ sdk_version: 5.42.0
 
 ## 🌟 概要
 
-**Wikipedia to Markdown Converter** は、Wikipediaの記事を整形されたMarkdownドキュメントに変換するWebアプリケーションです。単体処理と一括処理に対応し、複数のダウンロード形式を提供します。
+**Frame Bridge** は、2つの動画を視覚的に最適なフレームで自動結合するAIアプリケーションです。SSIM（構造的類似性指標）を使用して、動画1の終了部分と動画2の開始部分から最も類似したフレームを検出し、スムーズな動画結合を実現します。
 
 ### ✨ **主要機能**
 
-- 🔄 **単体・一括処理** - 1つまたは複数のWikipediaページを同時変換
-- 📊 **詳細分析** - 文字数、成功率、ファイル情報を表示
-- 🗜️ **複数形式** - 個別ファイル、結合文書、ZIPダウンロード
-- 🌐 **多言語対応** - 全てのWikipedia言語版に対応
-- � **要使いやすいUI** - 直感的で美しいインターフェース
+- 🤖 **AI自動分析** - SSIM技術による高精度フレーム類似度計算
+- 🎯 **最適接続点検出** - 動画間の最も自然な結合点を自動検出
+- 📊 **リアルタイム分析** - 動画情報の即座表示と詳細分析
+- 🎬 **スムーズ結合** - 視覚的に自然な動画結合を実現
+- 🖼️ **接続フレーム表示** - 結合に使用されるフレームの可視化
 
 ---
 
 ## 🚀 使い方
 
-### �  **オンラインで試す（推奨）**
-**[🚀 デモサイトはこちら](https://huggingface.co/spaces/MakiAi/wikipedia-to-markdown)**
+### 🌐 **オンラインで試す（推奨）**
+**[🚀 デモサイトはこちら](https://huggingface.co/spaces/MakiAi/frame-bridge)**
 
 ### 💻 **ローカルで実行**
 
 \```bash
 # リポジトリをクローン
-git clone https://github.com/your-username/wikipedia-to-markdown.git
-cd wikipedia-to-markdown
+git clone https://github.com/Sunwood-ai-labsII/frame-bridge.git
+cd frame-bridge
 
 # 依存関係をインストール
 pip install -r requirements.txt
@@ -73,40 +74,34 @@ docker-compose up -d
 
 ## 📋 操作方法
 
-### 🔗 **単体処理**
-1. WikipediaのURLを入力
-2. 「✨ 変換する」ボタンをクリック
-3. 生成されたMarkdownをコピーまたはダウンロード
+### 🎬 **動画結合の手順**
+1. **動画1（前半）** をアップロード
+2. **動画2（後半）** をアップロード  
+3. 「🌉 フレームブリッジ実行」ボタンをクリック
+4. AI分析結果と結合された動画をダウンロード
 
-### 📚 **一括処理**
-1. 複数のURLを1行に1つずつ入力
-2. 「🚀 一括変換する」ボタンをクリック
-3. 処理結果を確認し、必要な形式でダウンロード
-
-### 📊 **処理結果の表示例**
+### 📊 **分析結果の表示例**
 \```
-============================================================
-📊 処理結果サマリー
```

---

## ⏰ 15:23:56 - `11fe9ea`
**🔀 Merge: Frame Bridge動画結合アプリの完全実装**
*by Sunwood-ai-labs*

### 📋 Changed Files
```bash
Merge: 72358ac 20b74c6
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Thu Aug 14 15:23:56 2025 +0900
```

### 📊 Statistics
```bash
Merge: 72358ac 20b74c6
Author: Sunwood-ai-labs <sunwood.ai.labs@gmail.com>
Date:   Thu Aug 14 15:23:56 2025 +0900

    🔀 Merge: Frame Bridge動画結合アプリの完全実装
    
    - Wikipedia変換アプリからAI動画結合アプリへの完全転換
    - SSIM技術による高精度フレーム類似度計算機能
    - 単体処理・バッチ処理（順次結合・ペア結合）対応
    - OpenCV環境対応とテスト・ユーティリティ完備

 .gitignore                          |   5 +
 Dockerfile                          |  12 +-
 README.md                           | 109 +++----
 app.py                              | 565 ++++++++++++++----------------------
 pyproject.toml                      | 163 +++++++++++
 requirements.txt                    |   7 +-
 scripts/show_structure.py           |  58 ++++
 src/frame_bridge/__init__.py        |  20 ++
 src/frame_bridge/batch_processor.py | 311 ++++++++++++++++++++
 src/frame_bridge/config.py          |  46 +++
 src/frame_bridge/video_processor.py | 399 +++++++++++++++++++++++++
 tests/batch_test.py                 |  96 ++++++
 tests/test_sample.py                |  72 +++++
 13 files changed, 1450 insertions(+), 413 deletions(-)
```

### 💻 Code Changes
```diff
```

---

