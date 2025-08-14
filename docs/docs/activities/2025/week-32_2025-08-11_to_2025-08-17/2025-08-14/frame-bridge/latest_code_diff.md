# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/sync-to-hf.yml b/.github/workflows/sync-to-hf.yml
index 5879e47..dca6955 100644
--- a/.github/workflows/sync-to-hf.yml
+++ b/.github/workflows/sync-to-hf.yml
@@ -26,7 +26,7 @@ jobs:
           git config --global user.name "GitHub Action"
           
           # Hugging Face Hubにリモートを追加
-          git remote add hf https://huggingface.co/spaces/MakiAi/wikipedia-to-markdown
+          git remote add hf https://huggingface.co/spaces/MakiAi/frame-bridge
           
           # 強制プッシュでHugging Faceに同期
-          git push --force https://user:$HF_TOKEN@huggingface.co/spaces/MakiAi/wikipedia-to-markdown HEAD:main
+          git push --force https://user:$HF_TOKEN@huggingface.co/spaces/MakiAi/frame-bridge HEAD:main
```
