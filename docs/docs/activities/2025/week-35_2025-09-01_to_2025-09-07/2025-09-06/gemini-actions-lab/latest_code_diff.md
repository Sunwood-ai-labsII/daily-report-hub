# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
index f5a1c9f..2bbb708 100644
--- a/.github/workflows/imagen4.yml
+++ b/.github/workflows/imagen4.yml
@@ -93,14 +93,11 @@ jobs:
           SEED: ${{ inputs.seed }}
         run: |
           set -euo pipefail
-
           DATE_UTC=$(date -u +%Y%m%d)
           TS_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)
           DEST="assets/imagen4/${DATE_UTC}-${GITHUB_RUN_ID}"
           mkdir -p "$DEST"
-
           cp -v generated-images/* "$DEST"/
-
           # jq で JSON を安全に生成（Ubuntu イメージに jq は標準で入っています）
           jq -n \
             --arg repo "$GITHUB_REPOSITORY" \
@@ -115,16 +112,13 @@ jobs:
             --arg ts "$TS_UTC" \
             '{repo:$repo, run_id:$run_id, run_url:$run_url, workflow:$workflow, prompt:$prompt, model:$model, aspect_ratio:$aspect_ratio, num:$num, seed:$seed, timestamp_utc:$ts}' \
             > "$DEST/index.json"
-
           git config user.name  "$GH_USER_NAME"
           git config user.email "$GH_USER_EMAIL"
           git add "$DEST"
-
           if git diff --cached --quiet; then
             echo "No changes to commit."
             exit 0
           fi
-
           git commit -m "chore(images): add Imagen outputs for run ${GITHUB_RUN_ID}"
           git push origin "HEAD:${GITHUB_REF_NAME}"
 
```
