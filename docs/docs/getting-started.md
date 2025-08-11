---
sidebar_position: 2
---

# 🚀 セットアップガイド

Daily Report Hub へようこそ！このガイドでは、AI駆動の開発活動分析プラットフォームのセットアップと使用方法をご説明します。

## 🎯 概要

Daily Report Hub は、複数のリポジトリの開発活動を自動的に追跡し、インテリジェントなレポートを生成します。以下の手順で始めましょう：

## 📋 前提条件

開始前に以下を確認してください：

- **追跡したいGitリポジトリ**
- **GitHubアカウント** とリポジトリアクセス権限
- **GitHub Actions** の実行権限
- **Node.js 18+** （ローカル開発用）

## 🚀 クイックセットアップ

### ステップ 1: リポジトリ統合

追跡したいリポジトリにワークフローを追加：

1. リポジトリに `.github/workflows/sync-to-report.yml` を作成
2. 以下のワークフロー設定をコピー：

```yaml
name: Sync to Daily Report Hub v1.4
on:
  push:
    branches: [main, master]
  pull_request:
    types: [opened, synchronize, closed]

# 週の開始日を制御する設定
env:
  WEEK_START_DAY: 1 # 週の開始日 (0=日曜日, 1=月曜日, 2=火曜日, 3=水曜日, 4=木曜日, 5=金曜日, 6=土曜日)

jobs:
  sync-data:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout current repo
        uses: actions/checkout@v4
        with:
          fetch-depth: 0 # 全履歴を取得してその日の全コミットを追跡

      - name: Make scripts executable
        run: chmod +x .github/scripts/*.sh

      - name: Calculate week information
        run: ./.github/scripts/calculate-week-info.sh ${{ env.WEEK_START_DAY }}

      - name: Analyze Git activity
        run: ./.github/scripts/analyze-git-activity.sh

      - name: Generate Markdown reports
        run: ./.github/scripts/generate-markdown-reports.sh

      - name: Clone report hub and create structure
        env:
          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
        run: |
          # Git設定
          git config --global user.name "GitHub Actions Bot"
          git config --global user.email "actions@github.com"
          
          # daily-report-hubをクローン
          git clone https://x-access-token:${GITHUB_TOKEN}@github.com/${REPORT_HUB_REPO}.git daily-report-hub

      - name: Create Docusaurus structure
        run: ./.github/scripts/create-docusaurus-structure.sh

      - name: Sync to report hub
        env:
          GITHUB_TOKEN: ${{ secrets.GH_PAT }}
          REPORT_HUB_REPO: ${{ vars.REPORT_HUB_REPO || 'Sunwood-ai-labs/daily-report-hub' }}
        run: ./.github/scripts/sync-to-hub.sh
```

### ステップ 2: 必要なスクリプト

以下のスクリプトをリポジトリの `.github/scripts/` ディレクトリにコピー：

#### 📊 スクリプト一覧

| スクリプト名 | サイズ | 機能 |
|-------------|--------|------|
| `calculate-week-info.sh` | 1.6 KB | 週情報の計算と環境変数設定 |
| `analyze-git-activity.sh` | 3.0 KB | Git活動の分析と生データ生成 |
| `generate-markdown-reports.sh` | 5.2 KB | Markdownレポートの生成 |
| `create-docusaurus-structure.sh` | 2.7 KB | Docusaurus構造の作成 |
| `sync-to-hub.sh` | 2.1 KB | レポートハブへの同期 |

#### 🔧 各スクリプトの詳細

**`calculate-week-info.sh`**
- 週情報を計算し、環境変数を設定
- 週の開始日をカスタマイズ可能
- 出力: `REPO_NAME`, `DATE`, `YEAR`, `WEEK_FOLDER` など

**`analyze-git-activity.sh`**
- その日のGit活動を分析
- 生成ファイル: `daily_commits_raw.txt`, `daily_code_diff_raw.txt` など
- コミット数、差分統計を収集

**`generate-markdown-reports.sh`**
- 生データから美しいMarkdownレポートを生成
- 絵文字とアイコンで視覚的に魅力的
- 生成ファイル: `daily_summary.md`, `daily_commits.md` など

**`create-docusaurus-structure.sh`**
- Docusaurus対応のディレクトリ構造を作成
- `_category_.json` ファイルの自動生成
- 年/週/日/リポジトリの階層構造

**`sync-to-hub.sh`**
- レポートハブへの同期処理
- メタデータの生成
- 自動コミット・プッシュ

### ステップ 3: シークレットの設定

リポジトリ設定で以下のシークレットを追加：

- **`GH_PAT`**: リポジトリ権限を持つGitHub Personal Access Token
- **`REPORT_HUB_REPO`**: ターゲットリポジトリ（例: 'your-org/daily-report-hub'）

## 📊 生成されるレポート

設定完了後、各コミットで自動生成されるもの：

### 📝 日次レポート
- **📅 daily_summary.md**: 日次活動の概要・統計
- **💻 daily_commits.md**: 全コミットの詳細情報
- **🔄 daily_code_diff.md**: 完全なコード変更内容
- **📊 daily_diff_stats.md**: ファイル変更統計
- **🆕 latest_diff.md**: 最新コミットの変更
- **📋 metadata.json**: 構造化された活動データ

### 📁 整理された構造
```
docs/docs/activities/
├── _category_.json
└── 2025/
    ├── _category_.json
    └── week-32_2025-08-11_to_2025-08-17/
        ├── _category_.json
        └── 2025-08-11/
            ├── _category_.json
            └── your-repo/
                ├── _category_.json
                ├── daily_summary.md
                ├── daily_commits.md
                ├── daily_code_diff.md
                ├── daily_diff_stats.md
                ├── latest_diff.md
                ├── latest_code_diff.md
                ├── README.md
                └── metadata.json
```

## 🔧 カスタマイズ

### 週の開始日設定
`WEEK_START_DAY` 環境変数で週の開始日を設定：

```yaml
env:
  WEEK_START_DAY: 1  # 0=日曜日, 1=月曜日, 2=火曜日, など
```

### リポジトリ変数
プロジェクト固有の変数を設定：

- **`REPORT_HUB_REPO`**: レポートハブリポジトリ
- **カスタムメタデータ**: プロジェクト固有情報の追加

## 🤖 AI機能（開発中）

開発中の高度なAI機能：

- **🧠 スマート要約**: LLM生成の活動要約
- **🔍 コード分析**: AI駆動のコード品質インサイト
- **📈 パターン認識**: 開発パターンの自動検出
- **💡 改善提案**: AI駆動の改善提案

## 🔍 レポートの閲覧

セットアップ完了後、以下でレポートを確認：
- **ライブサイト**: `https://your-org.github.io/daily-report-hub/`
- **活動セクション**: Activitiesセクションに移動
- **日付ベースナビゲーション**: 日付・週別でブラウジング

## 🆘 トラブルシューティング

### よくある問題

**ワークフローが実行されない？**
- GitHub Actionsの権限を確認
- シークレットが正しく設定されているか確認
- スクリプトに実行権限があるか確認

**レポートが生成されない？**
- `GH_PAT` に十分な権限があるか確認
- リポジトリ変数が正しく設定されているか確認
- GitHub Actionsログでエラーを確認

**データが不足している？**
- checkout actionで `fetch-depth: 0` が設定されているか確認
- Git履歴が利用可能か確認
- 日付・時刻設定を確認

## 📞 サポート

お困りの際はお気軽にお問い合わせください：

- 📧 **Issues**: [GitHub Issues](https://github.com/Sunwood-ai-labsII/daily-report-hub/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Sunwood-ai-labsII/daily-report-hub/discussions)
- 📖 **ドキュメント**: このサイト！

---

開発活動の追跡を始める準備はできましたか？最初のリポジトリをセットアップしましょう！ 🚀