# daily-report-hub_dev

<div align="center">

<img src="https://img.shields.io/badge/GitHub%20Actions-CICD-blue?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
<img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Bash" />

</div>

---

## 📖 概要

このリポジトリは、**GitHub Actionsを活用してGitのコミット履歴から日報を自動生成し、集約用リポジトリ（[daily-report-hub](https://github.com/Sunwood-ai-labs/daily-report-hub)）へ同期するCICDワークフローのサンプル・テンプレートです。

- **開発アクティビティの可視化・自動集約**
- **週次・日次レポートの自動生成**
- **PRベースの自動同期・自動承認・自動マージ対応**

---

## 🚩 このリポジトリでできること

- Gitのコミット履歴・差分から日報（Markdown形式）を自動生成
- 週単位・日単位でレポートを整理
- 別リポジトリ（daily-report-hub）へPRベースで自動同期
- プルリクエストの自動承認・自動マージ（設定可）
- Docusaurus用のディレクトリ・ナビゲーション構造も自動生成

---

## ⚙️ ワークフロー概要

1. **GitHub Actions**がmainブランチへのpushやPRをトリガー
2. `.github/scripts/`配下のシェルスクリプトで
    - 週情報の計算
    - Git活動の分析
    - Markdownレポートの生成
    - Docusaurus用ディレクトリ構造の作成
3. 集約用リポジトリ（daily-report-hub）をクローンし、レポートをコピー
4. PR作成・自動承認・自動マージ（設定に応じて自動化）

---

## 📝 主なスクリプト

- `.github/scripts/calculate-week-info.sh`  
  週情報（週番号・開始日・終了日など）を計算し環境変数に出力

- `.github/scripts/analyze-git-activity.sh`  
  Gitのコミット履歴・差分を分析し、生データファイルを生成

- `.github/scripts/generate-markdown-reports.sh`  
  生データから日報・統計・差分などのMarkdownレポートを自動生成

- `.github/scripts/create-docusaurus-structure.sh`  
  Docusaurus用のディレクトリ・_category_.jsonを自動生成

- `.github/scripts/sync-to-hub-gh.sh`  
  集約リポジトリへPR作成・自動承認・自動マージ（YUKIHIKO権限）

---

## 🚀 使い方（クイックスタート）

1. このリポジトリをforkまたはclone
2. `.github/workflows/sync-to-report-gh.yml`の設定を必要に応じて編集
3. `GH_PAT`（GitHub Personal Access Token）など必要なシークレットを設定
4. mainブランチにpushすると自動で日報生成＆集約リポジトリへ同期

---

## 📁 ディレクトリ構成例

```
.
├── .github/
│   ├── scripts/
│   │   ├── calculate-week-info.sh
│   │   ├── analyze-git-activity.sh
│   │   ├── generate-markdown-reports.sh
│   │   ├── create-docusaurus-structure.sh
│   │   ├── sync-to-hub-gh.sh
│   │   └── sync-to-hub.sh
│   └── workflows/
│       └── sync-to-report-gh.yml
├── .SourceSageignore
├── README.md
```

---

## 🛠️ 設定・カスタマイズ

- `.github/workflows/sync-to-report-gh.yml`  
  - `WEEK_START_DAY`：週の開始曜日（0=日, 1=月, ...）
  - `AUTO_APPROVE`：PR自動承認
  - `AUTO_MERGE`：PR自動マージ
  - `CREATE_PR`：PR作成/直接push切替

- スクリプトの詳細は[.github/scripts/README.md](.github/scripts/README.md)参照

---

## 🔗 参考リンク

- [集約用日報ハブリポジトリ](https://github.com/Sunwood-ai-labs/daily-report-hub)
- [GitHub Actions公式ドキュメント](https://docs.github.com/ja/actions)
- [Docusaurus公式サイト](https://docusaurus.io/ja/)

---

© 2025 Sunwood-ai-labsII