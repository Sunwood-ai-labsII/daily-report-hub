# 📝 Daily Commits

## ⏰ 16:38:48 - `fbf04f2`
**add**
*by maki*

### 📋 Changed Files
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Fri Sep 5 16:38:48 2025 +0000
A	.github/workflows/gemini-release-notes.yml
```

### 📊 Statistics
```bash
Author: maki <sunwood.ai.labs@gmail.com>
Date:   Fri Sep 5 16:38:48 2025 +0000

    add

 .github/workflows/gemini-release-notes.yml | 161 +++++++++++++++++++++++++++++
 1 file changed, 161 insertions(+)
```

### 💻 Code Changes
```diff
diff --git a/.github/workflows/gemini-release-notes.yml b/.github/workflows/gemini-release-notes.yml
new file mode 100644
index 0000000..36d68bb
--- /dev/null
+++ b/.github/workflows/gemini-release-notes.yml
@@ -0,0 +1,161 @@
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
```

---

