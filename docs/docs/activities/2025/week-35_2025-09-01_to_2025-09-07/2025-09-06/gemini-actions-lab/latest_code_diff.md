# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/imagen4.yml b/.github/workflows/imagen4.yml
index 2bbb708..a5b3b05 100644
--- a/.github/workflows/imagen4.yml
+++ b/.github/workflows/imagen4.yml
@@ -124,4 +124,6 @@ jobs:
 
       - name: Show saved path
         shell: bash
-        run: echo "Saved to: assets/imagen4/$(date -u +%Y%m%d)-${GITHUB_RUN_ID}"
+        env:
+          DATE_FORMAT: "%Y%m%d"
+        run: echo "Saved to: assets/imagen4/$(date -u +"$DATE_FORMAT")-$GITHUB_RUN_ID"
```
