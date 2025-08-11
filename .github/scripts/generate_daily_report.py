#!/usr/bin/env python3
"""
AIにタグ付きで日報を生成させ、保存時にタグを削除して
純粋なMarkdownコンテンツのみをファイルに書き込むスクリプト。
"""

import os
import json
import glob
import re
from pathlib import Path
from datetime import datetime
import litellm

def find_todays_repos():
    """今日のリポジトリフォルダを検索"""
    today = datetime.now().strftime('%Y-%m-%d')
    year = today.split('-')[0]
    
    print(f"🔍 検索開始: {today}")
    activities_dir = Path('docs/docs/activities')
    
    repo_dirs = []
    if not activities_dir.exists():
        print(f"❌ ベースディレクトリが見つかりません: {activities_dir}")
        return today, repo_dirs

    year_dirs = list(activities_dir.glob(year))
    for year_dir in year_dirs:
        week_dirs = list(year_dir.glob('week-*'))
        for week_dir in week_dirs:
            date_dir = week_dir / today
            if date_dir.exists():
                for repo_dir in date_dir.iterdir():
                    metadata_file = repo_dir / 'metadata.json'
                    if repo_dir.is_dir() and metadata_file.exists():
                        repo_dirs.append(repo_dir)
                        print(f"✅ 対象リポジトリを追加: {repo_dir.name}")

    print(f"📊 最終的に見つかったリポジトリ数: {len(repo_dirs)}")
    return today, repo_dirs

def load_repo_data(repo_dir):
    """リポジトリのデータを読み込み"""
    print(f"\n📖 データ読み込み開始: {repo_dir.name}")
    repo_data = {'name': repo_dir.name, 'path': repo_dir}
    
    files_to_check = [
        ('summary', 'daily_summary.md'),
        ('commits', 'daily_commits.md'),
        ('changes', 'daily_cumulative_diff.md'),
        ('stats', 'daily_diff_stats.md'),
        ('code_diff', 'daily_code_diff.md')
    ]
    
    for key, filename in files_to_check:
        file_path = repo_dir / filename
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if key == 'commits':
                        content = content[:3000]
                    repo_data[key] = content
            except Exception as e:
                print(f"    ❌ {filename}: 読み込みエラー: {e}")

    return repo_data

def generate_repo_daily_report(repo_data, date):
    """個別リポジトリの日報を生成（AIにタグ付けを指示）"""
    repo_name = repo_data['name']
    print(f"\n🤖 AI日報生成開始: {repo_name}")
    
    prompt_parts = [f"以下の{repo_name}リポジトリの{date}の活動データから、日報をMarkdown形式で作成してください:\n"]
    
    if 'summary' in repo_data: prompt_parts.append(f"## サマリー:\n{repo_data['summary']}\n")
    if 'commits' in repo_data: prompt_parts.append(f"## コミット詳細:\n{repo_data['commits']}\n")
    if 'changes' in repo_data: prompt_parts.append(f"## ファイル変更:\n{repo_data['changes']}\n")
    if 'stats' in repo_data: prompt_parts.append(f"## 統計:\n{repo_data['stats']}\n")
    
    prompt_parts.append("""
日報作成要求:
- このリポジトリの今日の開発活動を要約
- 主要な変更点と技術的ポイントをハイライト
- 開発の進捗状況を評価
- 注目すべき改善や追加機能があれば言及
- 明日以降の開発への提案があれば記載
- 日本語で読みやすく、簡潔に記述
- 絵文字を効果的に使用
- **重要**: 完成した日報は、必ず `<output-report>` と `</output-report>` で全体を囲んでください。""")
    
    prompt = "\n".join(prompt_parts)
    
    try:
        print("🤖 API呼び出し開始...")
        response = litellm.completion(
            model="gemini/gemini-2.5-pro",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        
        content = response.choices[0].message.content
        print(f"✅ AI応答受信完了。")
        return content
        
    except Exception as e:
        print(f"❌ AI生成エラー ({repo_name}): {e}")
        fallback_content = f"""# 📅 {repo_name} - 日報 ({date})
## ⚠️ 注意
AI による日報生成に失敗しました。"""
        # フォールバック時も、後続処理のためにタグで囲む
        return f"<output-report>\n{fallback_content}\n</output-report>"

def save_repo_daily_report(repo_data, clean_report_content, date):
    """リポジトリフォルダに、タグなしのクリーンな日報を保存"""
    repo_dir = repo_data['path']
    report_file = repo_dir / 'ai_daily_report.md'
    
    print(f"\n💾 ファイル保存開始: {report_file}")
    
    frontmatter = f"""---
title: "{repo_data['name']} - AI日報"
date: "{date}"
sidebar_position: 1
description: "AI生成による{repo_data['name']}の開発日報"
tags: ["daily-report", "ai-generated", "{repo_data['name']}", "{date}"]
---

"""
    # フロントマターと、タグが削除されたクリーンなコンテンツを結合
    full_content = frontmatter + clean_report_content
    
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"✅ ファイル保存成功: {report_file}")
    except Exception as e:
        print(f"❌ ファイル保存エラー: {e}")

def main():
    print("🚀 Gemini 2.5 Pro 日報生成スクリプト開始")
    
    if not os.getenv('GOOGLE_API_KEY'):
        print("❌ GOOGLE_API_KEY が未設定です。処理を終了します。")
        return
    
    print("\n" + "="*50)
    print("📊 データ収集フェーズ")
    date, repo_dirs = find_todays_repos()
    
    if not repo_dirs:
        print("📝 本日の活動は記録されていませんでした。処理を終了します。")
        return
    
    print("\n" + "="*50)
    print("🤖 日報生成・保存フェーズ")
    
    for i, repo_dir in enumerate(repo_dirs, 1):
        print(f"\n--- {i}/{len(repo_dirs)}: {repo_dir.name} ---")
        
        repo_data = load_repo_data(repo_dir)
        
        # AIにタグ付きで日報を生成させる
        ai_response_with_tags = generate_repo_daily_report(repo_data, date)
        
        # --- ★★★ ここが最重要ポイント ★★★ ---
        # AIの応答から<output-report>タグの中身だけを抽出する
        print("🔍 AI応答から日報コンテンツを抽出中...")
        clean_report = None
        match = re.search(r'<output-report>(.*?)</output-report>', ai_response_with_tags, re.DOTALL)
        
        if match:
            clean_report = match.group(1).strip()
            print("✅ 抽出成功。")
        else:
            print("⚠️ 警告: AIの応答に<output-report>タグが見つかりませんでした。")
            print("AIの応答をそのまま日報コンテンツとして使用します。")
            clean_report = ai_response_with_tags.strip()
        # --- ★★★ ★★★ ★★★ ★★★ ★★★
        
        # タグが削除されたクリーンなコンテンツをファイルに保存
        save_repo_daily_report(repo_data, clean_report, date)
    
    print("\n" + "="*50)
    print("✅ 全てのリポジトリの日報生成が完了しました。")
    print("="*50)

if __name__ == "__main__":
    main()
