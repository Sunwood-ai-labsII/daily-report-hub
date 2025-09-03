# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/gemini-cli.yml b/.github/workflows/gemini-cli.yml
index ca66afa..a736018 100644
--- a/.github/workflows/gemini-cli.yml
+++ b/.github/workflows/gemini-cli.yml
@@ -112,7 +112,7 @@ jobs:
             IS_PR="true"
           fi
 
-a          # Clean up user request
+          # Clean up user request
           USER_REQUEST=$(echo "${USER_REQUEST}" | sed 's/.*@gemini-cli//' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
 
           # Write outputs safely (supporting newlines/special chars)
```
