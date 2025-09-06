# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
index a5b3b05..e1fcb26 100644
--- a/.github/workflows/imagen4.yml
+++ b/.github/workflows/imagen4.yml
@@ -39,7 +39,6 @@ jobs:
           gemini_model: gemini-2.5-flash
           gemini_cli_version: latest
           gemini_debug: true
-          # ここでは model だけを埋め込み、それ以外は prompt 内で渡す
           settings: |
             {
               "mcpServers": {
@@ -54,7 +53,6 @@ jobs:
                 }
               }
             }
-          # ユーザー入力は env で受け渡し、プロンプトに素直に埋め込む
           env: |
             PROMPT=${{ inputs.image_prompt }}
             NUM=${{ inputs.num }}
@@ -91,14 +89,15 @@ jobs:
           AR: ${{ inputs.aspect_ratio }}
           NUM: ${{ inputs.num }}
           SEED: ${{ inputs.seed }}
+          DATE_FORMAT: "%Y%m%d"
+          TIMESTAMP_FORMAT: "%Y-%m-%dT%H:%M:%SZ"
         run: |
           set -euo pipefail
-          DATE_UTC=$(date -u +%Y%m%d)
-          TS_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)
-          DEST="assets/imagen4/${DATE_UTC}-${GITHUB_RUN_ID}"
+          DATE_UTC=$(date -u +"$DATE_FORMAT")
+          TS_UTC=$(date -u +"$TIMESTAMP_FORMAT")
+          DEST="assets/imagen4/$DATE_UTC-$GITHUB_RUN_ID"
           mkdir -p "$DEST"
           cp -v generated-images/* "$DEST"/
-          # jq で JSON を安全に生成（Ubuntu イメージに jq は標準で入っています）
           jq -n \
             --arg repo "$GITHUB_REPOSITORY" \
             --arg run_id "$GITHUB_RUN_ID" \
@@ -112,18 +111,15 @@ jobs:
             --arg ts "$TS_UTC" \
             '{repo:$repo, run_id:$run_id, run_url:$run_url, workflow:$workflow, prompt:$prompt, model:$model, aspect_ratio:$aspect_ratio, num:$num, seed:$seed, timestamp_utc:$ts}' \
             > "$DEST/index.json"
-          git config user.name  "$GH_USER_NAME"
+          git config user.name "$GH_USER_NAME"
           git config user.email "$GH_USER_EMAIL"
           git add "$DEST"
           if git diff --cached --quiet; then
             echo "No changes to commit."
             exit 0
           fi
-          git commit -m "chore(images): add Imagen outputs for run ${GITHUB_RUN_ID}"
-          git push origin "HEAD:${GITHUB_REF_NAME}"
+          git commit -m "chore(images): add Imagen outputs for run $GITHUB_RUN_ID"
+          git push origin "HEAD:$GITHUB_REF_NAME"
 
       - name: Show saved path
-        shell: bash
-        env:
-          DATE_FORMAT: "%Y%m%d"
-        run: echo "Saved to: assets/imagen4/$(date -u +"$DATE_FORMAT")-$GITHUB_RUN_ID"
+        run: echo "Saved to assets/imagen4/$(date -u +%Y%m%d)-$GITHUB_RUN_ID"
```
