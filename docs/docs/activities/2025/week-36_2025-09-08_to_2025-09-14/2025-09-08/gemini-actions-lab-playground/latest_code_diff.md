# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 7c78682..0efb331 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -207,7 +207,7 @@ jobs:
           gemini_cli_version: 'latest'                  # ← 直近で動いた版に固定（例）
           # ---- 認証/モデルは“入力”として明示（env 依存しない）----
           gemini_api_key: ${{ secrets.GEMINI_API_KEY }} # Vertex を使わない場合は必須
-          gemini_model: 'gemini-2.5-pro'              # ← 明示的に指定（必要に応じて pro へ）
+          gemini_model: 'gemini-2.5-flash'              # ← 明示的に指定（必要に応じて pro へ）
           gemini_debug: true                            # 追加ログで原因特定しやすく
           # Vertex / GCA を使う構成なら以下を有効化
           gcp_workload_identity_provider: ${{ vars.GCP_WIF_PROVIDER }}
```
