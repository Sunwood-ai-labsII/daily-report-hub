# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
index f1da8e9..fd62fa1 100644
--- a/.github/workflows/imagen4.yml
+++ b/.github/workflows/imagen4.yml
@@ -25,6 +25,7 @@ permissions:
 jobs:
   generate_and_commit:
     runs-on: ubuntu-latest
+
     steps:
       - name: Checkout
         uses: actions/checkout@v4
@@ -56,14 +57,16 @@ jobs:
             Use the @gemini-imagen.generate_image tool to generate ${{ github.event.inputs.num }} image(s)
             from this prompt: "${{ github.event.inputs.image_prompt }}".
             Use aspect ratio "${{ github.event.inputs.aspect_ratio }}".
-            If "seed" is provided, use it: "${{ github.event.inputs.seed || '' }}".
+            If a seed is provided, use it: "${{ github.event.inputs.seed }}".
             Save files under ./generated-images and list only the filenames.
 
       - name: Verify outputs
         shell: bash
         run: |
           set -euo pipefail
-          test -d generated-images || { echo "generated-images not found"; exit 1; }
+          if [ ! -d generated-images ]; then
+            echo "generated-images not found"; exit 1
+          fi
           echo "== Generated files =="
           ls -lh generated-images
           cnt=$(ls -1 generated-images | wc -l)
@@ -80,25 +83,25 @@ jobs:
           set -euo pipefail
 
           DATE_UTC=$(date -u +%Y%m%d)
-          DEST="assets/imagen4/${DATE_UTC}-${{ github.run_id }}"
+          TS_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)
+          DEST="assets/imagen4/${DATE_UTC}-${GITHUB_RUN_ID}"
           mkdir -p "$DEST"
 
           cp -v generated-images/* "$DEST"/
 
-          cat > "$DEST/index.json" <<'EOF'
-          {
-            "repo": "${{ github.repository }}",
-            "run_id": "${{ github.run_id }}",
-            "run_url": "https://github.com/${{ github.repository }}/actions/runs/${{ github.run_id }}",
-            "workflow": "${{ github.workflow }}",
-            "prompt": "${{ github.event.inputs.image_prompt || '' }}",
-            "model": "${{ github.event.inputs.model || '' }}",
-            "aspect_ratio": "${{ github.event.inputs.aspect_ratio || '' }}",
-            "num": "${{ github.event.inputs.num || '' }}",
-            "seed": "${{ github.event.inputs.seed || '' }}",
-            "timestamp_utc": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
-          }
-          EOF
+          # index.json を安全に生成（式展開はbash側で完結させる）
+          printf '%s\n' "{
+            \"repo\": \"${GITHUB_REPOSITORY}\",
+            \"run_id\": \"${GITHUB_RUN_ID}\",
+            \"run_url\": \"https://github.com/${GITHUB_REPOSITORY}/actions/runs/${GITHUB_RUN_ID}\",
+            \"workflow\": \"${GITHUB_WORKFLOW}\",
+            \"prompt\": \"${{ github.event.inputs.image_prompt }}\",
+            \"model\": \"${{ github.event.inputs.model }}\",
+            \"aspect_ratio\": \"${{ github.event.inputs.aspect_ratio }}\",
+            \"num\": \"${{ github.event.inputs.num }}\",
+            \"seed\": \"${{ github.event.inputs.seed }}\",
+            \"timestamp_utc\": \"${TS_UTC}\"
+          }" > "$DEST/index.json"
 
           git config user.name  "$GH_USER_NAME"
           git config user.email "$GH_USER_EMAIL"
@@ -109,9 +112,9 @@ jobs:
             exit 0
           fi
 
-          git commit -m "chore(images): add Imagen outputs for run ${{ github.run_id }}"
-          git push origin HEAD:${{ github.ref_name }}
+          git commit -m "chore(images): add Imagen outputs for run ${GITHUB_RUN_ID}"
+          git push origin "HEAD:${GITHUB_REF_NAME}"
 
       - name: Show saved path
         shell: bash
-        run: echo "Saved to: assets/imagen4/${{ github.run_id }}"
+        run: echo "Saved to: assets/imagen4/$(date -u +%Y%m%d)-${GITHUB_RUN_ID}"
```
