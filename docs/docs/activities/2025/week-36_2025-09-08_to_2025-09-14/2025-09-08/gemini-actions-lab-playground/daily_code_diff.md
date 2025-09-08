# 💻 Daily Code Changes

## Full Diff

```diff
commit 27e57b36a0098df53cdaffd7b943f322e173e7a1
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Mon Sep 8 23:52:09 2025 +0900

    Update gemini-cli.yml

diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 0efb331..c965339 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -207,7 +207,7 @@ jobs:
           gemini_cli_version: 'latest'                  # ← 直近で動いた版に固定（例）
           # ---- 認証/モデルは“入力”として明示（env 依存しない）----
           gemini_api_key: ${{ secrets.GEMINI_API_KEY }} # Vertex を使わない場合は必須
-          gemini_model: 'gemini-2.5-flash'              # ← 明示的に指定（必要に応じて pro へ）
+          # gemini_model: 'gemini-2.5-flash'              # ← 明示的に指定（必要に応じて pro へ）
           gemini_debug: true                            # 追加ログで原因特定しやすく
           # Vertex / GCA を使う構成なら以下を有効化
           gcp_workload_identity_provider: ${{ vars.GCP_WIF_PROVIDER }}
```
