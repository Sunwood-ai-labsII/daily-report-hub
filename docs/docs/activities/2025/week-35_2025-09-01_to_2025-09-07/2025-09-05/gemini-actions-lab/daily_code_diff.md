# 💻 Daily Code Changes

## Full Diff

```diff
diff --git a/.github/workflows/gemini-release-notes.yml b/.github/workflows/gemini-release-notes.yml
new file mode 100644
index 0000000..9d95cd6
--- /dev/null
+++ b/.github/workflows/gemini-release-notes.yml
@@ -0,0 +1,163 @@
+name: "📝 Gemini Release Notes"
+
+on:
+  push:
+    tags:
+      - "*"
+
+permissions:
+  contents: write
+
+defaults:
+  run:
+    shell: bash
+
+jobs:
+  release-notes:
+    runs-on: ubuntu-latest
+    timeout-minutes: 5
+    steps:
+      - name: Checkout
+        uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # ratchet:actions/checkout@v4
+        with:
+          fetch-depth: 0
+
+      - name: Prepare context
+        id: ctx
+        env:
+          REPOSITORY: "${{ github.repository }}"
+          TAG_NAME: "${{ github.ref_name }}"
+          GITHUB_TOKEN: "${{ secrets.GITHUB_TOKEN }}"
+        run: |
+          set -euo pipefail
+
+          TAG="${TAG_NAME}"
+          git fetch --tags --prune --force >/dev/null 2>&1 || true
+
+          # Try to get previous released tag (from Releases). Fallback to previous git tag reachable from current.
+          PREV_RELEASE_TAG="$(gh release list --limit 100 --json tagName --jq 'map(.tagName) | map(select(. != env.TAG)) | .[0]' || true)"
+          if [[ -z "${PREV_RELEASE_TAG}" || "${PREV_RELEASE_TAG}" == "null" ]]; then
+            PREV_RELEASE_TAG="$(git describe --tags --abbrev=0 "${TAG}^" 2>/dev/null || true)"
+          fi
+
+          BASE_RANGE=""
+          COMPARE_URL=""
+          if [[ -n "${PREV_RELEASE_TAG}" ]]; then
+            BASE_RANGE="${PREV_RELEASE_TAG}..${TAG}"
+            COMPARE_URL="https://github.com/${REPOSITORY}/compare/${PREV_RELEASE_TAG}...${TAG}"
+          else
+            # Initial release: include history up to the tag commit
+            BASE_RANGE="${TAG}"
+          fi
+
+          # Collect data (trim to keep prompt concise)
+          COMMITS="$(git log --no-merges --pretty=format:'- %s (%h) by %an' ${BASE_RANGE} | head -n 300 || true)"
+          CHANGED_FILES="$( ( [[ -n "${PREV_RELEASE_TAG}" ]] && git diff --name-only ${BASE_RANGE} || git ls-tree -r --name-only HEAD ) | sed 's/^/- /' | head -n 500 || true)"
+          CONTRIBUTORS="$(git log --format='%an' ${BASE_RANGE} | sort -u | sed 's/^/- /' | head -n 200 || true)"
+
+          {
+            echo "tag=${TAG}"
+            echo "prev_tag=${PREV_RELEASE_TAG}"
+            echo "compare_url=${COMPARE_URL}"
+            echo 'commits<<EOF'
+            echo "${COMMITS}"
+            echo 'EOF'
+            echo 'files<<EOF'
+            echo "${CHANGED_FILES}"
+            echo 'EOF'
+            echo 'contributors<<EOF'
+            echo "${CONTRIBUTORS}"
+            echo 'EOF'
+          } >> "$GITHUB_OUTPUT"
+
+      - name: Generate release notes with Gemini
+        id: gemini
+        uses: google-github-actions/run-gemini-cli@v0
+        env:
+          REPOSITORY: "${{ github.repository }}"
+          TAG_NAME: "${{ steps.ctx.outputs.tag }}"
+          PREV_TAG: "${{ steps.ctx.outputs.prev_tag }}"
+          COMPARE_URL: "${{ steps.ctx.outputs.compare_url }}"
+          COMMITS: "${{ steps.ctx.outputs.commits }}"
+          CHANGED_FILES: "${{ steps.ctx.outputs.files }}"
+          CONTRIBUTORS: "${{ steps.ctx.outputs.contributors }}"
+        with:
+          gemini_api_key: "${{ secrets.GEMINI_API_KEY }}"
+          gcp_workload_identity_provider: "${{ vars.GCP_WIF_PROVIDER }}"
+          gcp_project_id: "${{ vars.GOOGLE_CLOUD_PROJECT }}"
+          gcp_location: "${{ vars.GOOGLE_CLOUD_LOCATION }}"
+          gcp_service_account: "${{ vars.SERVICE_ACCOUNT_EMAIL }}"
+          use_vertex_ai: "${{ vars.GOOGLE_GENAI_USE_VERTEXAI }}"
+          use_gemini_code_assist: "${{ vars.GOOGLE_GENAI_USE_GCA }}"
+          settings: |
+            { "debug": false, "maxSessionTurns": 10, "telemetry": { "enabled": false, "target": "gcp" } }
+          prompt: |
+            あなたはリリースノート作成のエキスパートです。以下の情報から、日本語で読みやすいMarkdownのリリースノートを作成してください。
+
+            # コンテキスト
+            - リポジトリ: ${{ github.repository }}
+            - リリースタグ: ${{ steps.ctx.outputs.tag }}
+            - 前リリースタグ: ${{ steps.ctx.outputs.prev_tag }}
+            - 比較URL: ${{ steps.ctx.outputs.compare_url }}
+
+            # 変更コミット（抜粋）
+            ${{ steps.ctx.outputs.commits }}
+
+            # 変更ファイル（抜粋）
+            ${{ steps.ctx.outputs.files }}
+
+            # コントリビューター（抜粋）
+            ${{ steps.ctx.outputs.contributors }}
+
+            # 執筆方針
+            - 見出しと箇条書きを用いて簡潔に。
+            - 主な変更点(Highlights)、Breaking Changes（あれば）、改善・修正、貢献者の順でまとめる。
+            - 可能ならConventional Commitsを手掛かりに分類（feat/fix/docs/chore/refactor/perf/test 等）。
+            - コミットメッセージから重大変更を推測できる場合は「Breaking Changes」に明記。
+            - 最後に比較URLを記載。
+            - 出力はMarkdownのみ（余計な前置きや後書き、コードフェンスは不要）。
+
+            # 期待するMarkdownの構成例
+            # ${{ steps.ctx.outputs.tag }} ～このリリースノートの内容が分かるようなタイトル～
+            ## ✨ Highlights
+            - 主要な変更点の要約…
+
+            ## 💥 Breaking Changes
+            - 重大な変更点…（なければこの節は省略可）
+
+            ## 🛠 変更一覧
+            - feat: …
+            - fix: …
+            - docs: …
+            - refactor: …
+            - chore: …
+
+            ## 👥 Contributors
+            - ユーザー名一覧（抜粋）
+
+            ---
+            比較: ${{ steps.ctx.outputs.compare_url }}
+
+      - name: Write notes to file
+        run: |
+          set -euo pipefail
+          # Write without shell interpolation to avoid ${...} expansion issues
+          cat > release_notes.md << 'EOF'
+          ${{ steps.gemini.outputs.summary }}
+          EOF
+          echo "Wrote release_notes.md (size: $(wc -c < release_notes.md) bytes)"
+
+      - name: Create or update GitHub Release
+        env:
+          GITHUB_TOKEN: "${{ secrets.GITHUB_TOKEN }}"
+          TAG: "${{ steps.ctx.outputs.tag }}"
+        run: |
+          set -euo pipefail
+          if gh release view "${TAG}" >/dev/null 2>&1; then
+            gh release edit "${TAG}" --notes-file release_notes.md
+          else
+            # Mark pre-releases automatically if tag contains pre-release identifiers
+            PRERELEASE_FLAG=""
+            if [[ "${TAG}" =~ -(alpha|beta|rc) ]]; then PRERELEASE_FLAG="--prerelease"; fi
+            gh release create "${TAG}" --title "${TAG}" --notes-file release_notes.md ${PRERELEASE_FLAG}
+          fi
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
new file mode 100644
index 0000000..5fe2bca
--- /dev/null
+++ b/.github/workflows/imagen4.yml
@@ -0,0 +1,55 @@
+name: Imagen4 via Gemini CLI (MCP)
+
+on:
+  workflow_dispatch:
+    inputs:
+      prompt:
+        description: "画像プロンプト"
+        required: true
+      aspect_ratio:
+        description: "1:1 | 3:4 | 4:3 | 9:16 | 16:9"
+        required: false
+        default: "1:1"
+      model:
+        description: "imagen-4.0-(generate|fast-generate|ultra-generate)-preview-06-06"
+        required: false
+        default: "imagen-4.0-fast-generate-preview-06-06"
+
+jobs:
+  generate:
+    runs-on: ubuntu-latest
+    steps:
+      - uses: actions/checkout@v4
+
+      # Gemini CLI をGitHub Actionsから実行
+      - name: Run Gemini CLI with Imagen4 MCP
+        uses: google-github-actions/run-gemini-cli@v0.1.12
+        with:
+          # Gemini CLI が読む settings.json をインラインで書き込み
+          settings: |
+            {
+              "mcpServers": {
+                "gemini-imagen4": {
+                  "command": "npx",
+                  "args": ["gemini-imagen4"],
+                  "env": { "GEMINI_API_KEY": "${{ secrets.GEMINI_API_KEY }}" }
+                }
+              }
+            }
+          # ここが実際の“指示”。MCPツール名はサーバ側ドキュメント準拠
+          prompt: |
+            Use @gemini-imagen4.generate_image_from_text with:
+            prompt="${{ inputs.prompt }}",
+            model="${{ inputs.model }}",
+            aspectRatio="${{ inputs.aspect_ratio }}".
+            Return the saved file paths (./generated-images) and a short summary.
+          gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
+          gemini_cli_version: latest
+          gemini_debug: true
+
+      - name: Upload generated images
+        if: always()
+        uses: actions/upload-artifact@v4
+        with:
+          name: imagen4-output
+          path: generated-images/**
```
