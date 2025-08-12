# 🔄 Latest Code Changes

```diff
diff --git a/.github/workflows/sync-to-hf.yml b/.github/workflows/sync-to-hf.yml
index a64c4cb..5879e47 100644
--- a/.github/workflows/sync-to-hf.yml
+++ b/.github/workflows/sync-to-hf.yml
@@ -21,15 +21,12 @@ jobs:
         env:
           HF_TOKEN: ${{ secrets.HF_TOKEN }}
         run: |
-          # リポジトリ名を取得
-          REPO_NAME="${GITHUB_REPOSITORY##*/}"
-          
           # Git設定
           git config --global user.email "action@github.com"
           git config --global user.name "GitHub Action"
           
           # Hugging Face Hubにリモートを追加
-          git remote add hf https://huggingface.co/spaces/${{ github.repository_owner }}/${REPO_NAME}
+          git remote add hf https://huggingface.co/spaces/MakiAi/wikipedia-to-markdown
           
           # 強制プッシュでHugging Faceに同期
-          git push --force https://user:$HF_TOKEN@huggingface.co/spaces/${{ github.repository_owner }}/${REPO_NAME} HEAD:main
\ No newline at end of file
+          git push --force https://user:$HF_TOKEN@huggingface.co/spaces/MakiAi/wikipedia-to-markdown HEAD:main
```
