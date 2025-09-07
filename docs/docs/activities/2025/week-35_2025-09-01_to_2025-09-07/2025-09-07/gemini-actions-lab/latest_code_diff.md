# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index 9b2d7fa..63671e6 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -234,16 +234,18 @@ jobs:
             echo "Prompt template not found: ${TEMPLATE_PATH}" >&2
             exit 1
           fi
-          # Safe variable substitution without executing content
-          EXPANDED=$(sed \
-            -e "s|\\$\\{REPOSITORY\\}|${REPOSITORY}|g" \
-            -e "s|\\$\\{EVENT_NAME\\}|${EVENT_NAME}|g" \
-            -e "s|\\$\\{ISSUE_NUMBER\\}|${ISSUE_NUMBER}|g" \
-            -e "s|\\$\\{IS_PR\\}|${IS_PR}|g" \
-            -e "s|\\$\\{DESCRIPTION\\}|${DESCRIPTION}|g" \
-            -e "s|\\$\\{COMMENTS\\}|${COMMENTS}|g" \
-            -e "s|\\$\\{USER_REQUEST\\}|${USER_REQUEST}|g" \
-            "${TEMPLATE_PATH}")
+
+          # sedの代わりにperlを使用して、改行を含む変数を安全に置換
+          EXPANDED=$(perl -p -e '
+            s/\$\{REPOSITORY\}/$ENV{REPOSITORY}/g;
+            s/\$\{EVENT_NAME\}/$ENV{EVENT_NAME}/g;
+            s/\$\{ISSUE_NUMBER\}/$ENV{ISSUE_NUMBER}/g;
+            s/\$\{IS_PR\}/$ENV{IS_PR}/g;
+            s/\$\{DESCRIPTION\}/$ENV{DESCRIPTION}/g;
+            s/\$\{COMMENTS\}/$ENV{COMMENTS}/g;
+            s/\$\{USER_REQUEST\}/$ENV{USER_REQUEST}/g;
+          ' "${TEMPLATE_PATH}")
+
           {
             echo "prompt<<EOF"
             echo "${EXPANDED}"
```
