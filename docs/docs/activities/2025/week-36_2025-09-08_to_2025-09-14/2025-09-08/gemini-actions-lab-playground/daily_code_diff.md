# 💻 Daily Code Changes

## Full Diff

```diff
commit 775af94c2baacd6b27a389cd3cf9005337b3ead2
Author: Yukihiko.F@sunwood.ai.labs <yukihiko.fuyuki@gmail.com>
Date:   Tue Sep 9 00:13:39 2025 +0900

    Update gemini-cli.yml

diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 87bbd9f..16acaf6 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -209,6 +209,7 @@ jobs:
           gemini_api_key: ${{ secrets.GEMINI_API_KEY }} # Vertex を使わない場合は必須
           # gemini_model: 'gemini-2.5-flash'              # ← 明示的に指定（必要に応じて pro へ）
           # gemini_model: 'gemini-2.5-pro'              # ← 明示的に指定（必要に応じて pro へ）
+          gemini_model: 'gemini-1.5-pro-002'
           gemini_debug: true                            # 追加ログで原因特定しやすく
           # Vertex / GCA を使う構成なら以下を有効化
           gcp_workload_identity_provider: ${{ vars.GCP_WIF_PROVIDER }}
```
