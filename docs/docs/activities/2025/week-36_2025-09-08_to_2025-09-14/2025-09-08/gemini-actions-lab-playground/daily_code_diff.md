# 💻 Daily Code Changes

## Full Diff

```diff
commit 444d52802d114e346b679b31422f5e1140f55342
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 23:37:43 2025 +0900

    Update gemini-cli.yml

diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 5881a57..87bda35 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -204,7 +204,7 @@ jobs:
         # ↑↑ 必要なら v0 固定でもOKだが、マイナーの既知安定版を明示推奨
         with:
           # ---- 重要：CLI バージョンを固定して回帰を遮断 ----
-          gemini_cli_version: '0.3.4'                  # ← 直近で動いた版に固定（例）
+          gemini_cli_version: '0.4.0-preview.2'                  # ← 直近で動いた版に固定（例）
           # ---- 認証/モデルは“入力”として明示（env 依存しない）----
           gemini_api_key: ${{ secrets.GEMINI_API_KEY }} # Vertex を使わない場合は必須
           gemini_model: 'gemini-2.5-pro'              # ← 明示的に指定（必要に応じて pro へ）
```
