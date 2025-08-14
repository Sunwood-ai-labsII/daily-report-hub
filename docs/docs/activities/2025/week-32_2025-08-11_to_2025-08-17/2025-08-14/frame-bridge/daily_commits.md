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

