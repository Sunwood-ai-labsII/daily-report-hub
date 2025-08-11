#!/usr/bin/env python3
"""
各リポジトリフォルダに個別の日報のみを生成するシンプルスクリプト
"""

import os
import json
import glob
from pathlib import Path
from datetime import datetime
import litellm

def find_todays_repos():
    """今日のリポジトリフォルダを検索"""
    today = datetime.now().strftime('%Y-%m-%d')
    year = today.split('-')[0]
    
    # activities ディレクトリから今日のデータを探す
    activities_dir = Path('docs/docs/activities')
    repo_dirs = []
    
    # 年/週/日付の構造を探索
    for year_dir in activities_dir.glob(year):
        for week_dir in year_dir.glob('week-*'):
            date_dir = week_dir / today
            if date_dir.exists():
                for repo_dir in date_dir.iterdir():
                    if repo_dir.is_dir() and (repo_dir / 'metadata.json').exists():
                        repo_dirs.append(repo_dir)
    
    return today, repo_dirs

def load_repo_data(repo_dir):
    """リポジトリのデータを読み込み"""
    repo_data = {'name': repo_dir.name, 'path': repo_dir}
    
    # サマリー
    summary_file = repo_dir / 'daily_summary.md'
    if summary_file.exists():
        with open(summary_file, 'r', encoding='utf-8') as f:
            repo_data['summary'] = f.read()
    
    # コミット詳細
    commits_file = repo_dir / 'daily_commits.md'
    if commits_file.exists():
        with open(commits_file, 'r', encoding='utf-8') as f:
            repo_data['commits'] = f.read()[:3000]  # 最初の3000文字
    
    # ファイル変更
    changes_file = repo_dir / 'daily_cumulative_diff.md'
    if changes_file.exists():
        with open(changes_file, 'r', encoding='utf-8') as f:
            repo_data['changes'] = f.read()
    
    # 統計
    stats_file = repo_dir / 'daily_diff_stats.md'
    if stats_file.exists():
        with open(stats_file, 'r', encoding='utf-8') as f:
            repo_data['stats'] = f.read()
    
    return repo_data

def generate_repo_daily_report(repo_data, date):
    """個別リポジトリの日報を生成"""
    repo_name = repo_data['name']
    
    prompt = f"""以下の{repo_name}リポジトリの{date}の活動データから、日報をMarkdown形式で作成してください:

"""
    
    if 'summary' in repo_data:
        prompt += f"## サマリー:\n{repo_data['summary']}\n\n"
    
    if 'commits' in repo_data:
        prompt += f"## コミット詳細:\n{repo_data['commits'][:1500]}\n\n"
    
    if 'changes' in repo_data:
        prompt += f"## ファイル変更:\n{repo_data['changes']}\n\n"
    
    if 'stats' in repo_data:
        prompt += f"## 統計:\n{repo_data['stats']}\n\n"
    
    prompt += """
日報作成要求:
- このリポジトリの今日の開発活動を要約
- 主要な変更点と技術的ポイントをハイライト
- 開発の進捗状況を評価
- 注目すべき改善や追加機能があれば言及
- 明日以降の開発への提案があれば記載
- 日本語で読みやすく、簡潔に記述
- 絵文字を効果的に使用"""

    try:
        response = litellm.completion(
            model="gemini/gemini-2.5-pro",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"日報生成エラー ({repo_name}): {e}")
        return f"""# 📅 {repo_name} - 日報 ({date})

## 📊 基本情報
- リポジトリ: {repo_name}
- 日付: {date}
- 生成時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## ⚠️ 注意
AI による日報生成に失敗しました。既存のサマリーファイルをご確認ください。

---
*手動での日報作成をお願いします*"""

def save_repo_daily_report(repo_data, daily_report, date):
    """リポジトリフォルダに日報を保存"""
    repo_dir = repo_data['path']
    report_file = repo_dir / 'ai_daily_report.md'
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(f"""---
title: "📅 {repo_data['name']} - AI日報"
date: {date}
sidebar_position: 1
---

{daily_report}
""")
    
    print(f"📄 日報保存: {report_file}")

def main():
    print("🚀 Gemini で個別リポジトリ日報生成開始")
    
    # データ収集
    date, repo_dirs = find_todays_repos()
    print(f"📊 {date}: {len(repo_dirs)}個のリポジトリ")
    
    if not repo_dirs:
        print("📝 本日の活動なし")
        return
    
    # 各リポジトリの日報生成
    for repo_dir in repo_dirs:
        print(f"🤖 {repo_dir.name} の日報生成中...")
        
        # データ読み込み
        repo_data = load_repo_data(repo_dir)
        
        # 日報生成
        daily_report = generate_repo_daily_report(repo_data, date)
        
        # 保存
        save_repo_daily_report(repo_data, daily_report, date)
    
    print("✅ 全リポジトリの日報生成完了")

if __name__ == "__main__":
    main()
