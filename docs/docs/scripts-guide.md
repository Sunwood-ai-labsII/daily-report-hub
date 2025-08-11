---
sidebar_position: 4
---

# 📜 スクリプトガイド

Daily Report Hub のCI/CDシステムは、5つの専用スクリプトで構成されています。各スクリプトの詳細な機能と使用方法をご説明します。

## 📊 スクリプト概要

| スクリプト名 | サイズ | 行数 | 主要機能 |
|-------------|--------|------|----------|
| `generate-markdown-reports.sh` | 5.2 KB | 191行 | Markdownレポート生成 |
| `analyze-git-activity.sh` | 3.0 KB | 59行 | Git活動分析 |
| `create-docusaurus-structure.sh` | 2.7 KB | 111行 | Docusaurus構造作成 |
| `sync-to-hub.sh` | 2.1 KB | 71行 | レポートハブ同期 |
| `calculate-week-info.sh` | 1.6 KB | 44行 | 週情報計算 |

## 🔧 各スクリプトの詳細

### 1. 📅 `calculate-week-info.sh`
**週情報を計算し、環境変数を設定**

```bash
#!/bin/bash
# 週情報を計算するスクリプト
# 使用方法: ./calculate-week-info.sh [WEEK_START_DAY]

set -e

WEEK_START_DAY=${1:-1}  # デフォルトは月曜日
```

#### 🎯 主要機能
- **週の開始日計算**: カスタマイズ可能な週開始日
- **週番号生成**: 年間通しての週番号計算
- **フォルダ名生成**: `week-32_2025-08-11_to_2025-08-17` 形式
- **環境変数出力**: 後続スクリプトで使用する変数を設定

#### 📤 出力環境変数
- `REPO_NAME`: リポジトリ名
- `DATE`: 現在の日付 (YYYY-MM-DD)
- `YEAR`: 現在の年
- `WEEK_FOLDER`: 週フォルダ名
- `WEEK_START_DATE`: 週の開始日
- `WEEK_END_DATE`: 週の終了日
- `WEEK_NUMBER`: 週番号

### 2. 🔍 `analyze-git-activity.sh`
**Gitの活動を分析し、生データファイルを生成**

```bash
#!/bin/bash
# Git活動を分析してMarkdownファイルを生成するスクリプト

set -e

DATE=${DATE:-$(date '+%Y-%m-%d')}
echo "🔍 Fetching all commits for $DATE..."
```

#### 🎯 主要機能
- **日次コミット取得**: その日の全コミット履歴を時刻順で取得
- **差分分析**: 累積差分と統計情報の生成
- **初回コミット対応**: 親コミットが存在しない場合の特別処理
- **最新変更追跡**: 最新コミットの個別差分取得

#### 📁 生成ファイル
- `daily_commits_raw.txt`: その日のコミット一覧
- `daily_cumulative_diff_raw.txt`: その日の累積差分
- `daily_diff_stats_raw.txt`: その日の統計情報
- `daily_code_diff_raw.txt`: その日のコード差分
- `latest_diff_raw.txt`: 最新の差分
- `latest_code_diff_raw.txt`: 最新のコード差分

### 3. 📝 `generate-markdown-reports.sh`
**生データから美しいMarkdownレポートを生成**

```bash
#!/bin/bash
# Markdownレポートを生成するスクリプト

set -e

# ファイル変更のステータスアイコンを取得する関数
get_status_icon() {
  case $1 in
    A) echo "- 🆕 **Added:** \`$2\`" ;;
    M) echo "- ✏️ **Modified:** \`$2\`" ;;
    D) echo "- 🗑️ **Deleted:** \`$2\`" ;;
    R*) echo "- 🔄 **Renamed:** \`$2\`" ;;
    *) echo "- 📝 **$1:** \`$2\`" ;;
  esac
}
```

#### 🎯 主要機能
- **視覚的レポート**: 絵文字とアイコンで魅力的な表示
- **詳細コミット分析**: 各コミットの変更ファイル、統計、差分を表示
- **ステータスアイコン**: ファイル変更タイプの視覚的表現
- **包括的サマリー**: 日次活動の完全な概要

#### 📄 生成レポート
- `daily_commits.md`: コミット詳細レポート
- `daily_cumulative_diff.md`: ファイル変更レポート
- `daily_diff_stats.md`: 統計レポート
- `daily_code_diff.md`: コード差分レポート
- `latest_diff.md`: 最新変更レポート
- `latest_code_diff.md`: 最新コード差分レポート
- `daily_summary.md`: 日次サマリーレポート

### 4. 🏗️ `create-docusaurus-structure.sh`
**Docusaurusの構造と`_category_.json`ファイルを作成**

```bash
#!/bin/bash
# Docusaurusの構造と_category_.jsonファイルを作成するスクリプト

set -e

# 必要な環境変数をチェック
: ${REPO_NAME:?}
: ${DATE:?}
: ${YEAR:?}
: ${WEEK_FOLDER:?}
: ${WEEK_NUMBER:?}
: ${WEEK_START_DATE:?}
: ${WEEK_END_DATE:?}
```

#### 🎯 主要機能
- **階層構造作成**: 年/週/日/リポジトリの4層構造
- **カテゴリファイル生成**: Docusaurus用の`_category_.json`自動作成
- **ナビゲーション設定**: 美しいサイドバーナビゲーション
- **位置計算**: 日付ベースの表示順序設定

#### 📁 作成される構造
```
docs/docs/activities/
├── _category_.json          # 📊 Activities
└── 2025/
    ├── _category_.json      # 2025
    └── week-32_2025-08-11_to_2025-08-17/
        ├── _category_.json  # Week 32 (2025-08-11 to 2025-08-17)
        └── 2025-08-11/
            ├── _category_.json  # 📅 2025-08-11
            └── your-repo/
                └── _category_.json  # 🔧 your-repo
```

### 5. 🔄 `sync-to-hub.sh`
**レポートハブにファイルを同期**

```bash
#!/bin/bash
# レポートハブに同期するスクリプト

set -e

# 必要な環境変数をチェック
: ${GITHUB_TOKEN:?}
: ${REPORT_HUB_REPO:?}
: ${TARGET_DIR:?}
: ${REPO_NAME:?}
: ${DATE:?}
: ${WEEK_NUMBER:?}
```

#### 🎯 主要機能
- **ファイル同期**: 生成されたレポートをハブリポジトリにコピー
- **メタデータ生成**: 構造化されたJSON形式の活動データ
- **自動コミット**: タイムスタンプ付きでの自動コミット・プッシュ
- **エラーハンドリング**: 変更がない場合の適切な処理

#### 📋 生成メタデータ
```json
{
  "repository": "Sunwood-ai-labsII/daily-report-hub_sample1",
  "date": "2025-08-11",
  "week_folder": "week-32_2025-08-11_to_2025-08-17",
  "week_number": 32,
  "week_start_date": "2025-08-11",
  "week_end_date": "2025-08-17",
  "branch": "main",
  "latest_commit_sha": "18c42d6e83abf34c0cf328b830be36f72b9eb1a7",
  "sync_timestamp": "2025-08-11T07:29:57Z",
  "workflow_run": "16873679050",
  "daily_commit_count": 26,
  "daily_files_changed": 14,
  "has_activity": true,
  "files": {
    "readme": "README.md",
    "summary": "daily_summary.md",
    "commits": "daily_commits.md",
    "file_changes": "daily_cumulative_diff.md",
    "stats": "daily_diff_stats.md",
    "code_diff": "daily_code_diff.md",
    "latest_diff": "latest_diff.md",
    "latest_code_diff": "latest_code_diff.md"
  }
}
```

## ⚙️ ワークフロー設定

### 📄 `sync-to-report.yml`
**GitHub Actionsワークフロー設定**

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
```

#### 🎯 主要特徴
- **柔軟なトリガー**: push と pull_request の両方に対応
- **週設定**: カスタマイズ可能な週の開始日
- **段階的実行**: 5つのスクリプトを順次実行
- **エラーハンドリング**: 各ステップでの適切なエラー処理

## 🔧 カスタマイズオプション

### 週の開始日設定
```yaml
env:
  WEEK_START_DAY: 1  # 0=日曜日, 1=月曜日, 2=火曜日, etc.
```

### 必要なシークレット
- **`GH_PAT`**: GitHub Personal Access Token
- **`REPORT_HUB_REPO`**: レポートハブのリポジトリ名

### 環境変数
- **`GITHUB_REPOSITORY`**: 自動設定されるリポジトリ名
- **`GITHUB_SHA`**: 最新コミットのハッシュ
- **`GITHUB_RUN_ID`**: ワークフロー実行ID

## 🚀 実行フロー

1. **📅 週情報計算** → 環境変数設定
2. **🔍 Git活動分析** → 生データファイル生成
3. **📝 レポート生成** → Markdownファイル作成
4. **🏗️ 構造作成** → Docusaurus対応構造
5. **🔄 ハブ同期** → 最終的な同期とコミット

## 📊 統計情報

- **総スクリプト数**: 5個
- **総行数**: 476行（bash）
- **総サイズ**: 14.5 KB
- **対応言語**: bash, yaml, markdown

---

これらのスクリプトにより、完全に自動化された開発活動レポートシステムが実現されています。各スクリプトは独立して動作し、メンテナンスしやすい設計になっています。 🎉