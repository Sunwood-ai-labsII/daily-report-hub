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

