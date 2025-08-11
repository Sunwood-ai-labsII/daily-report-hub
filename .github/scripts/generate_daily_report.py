#!/usr/bin/env python3
"""
AIへのプロンプトを修正し、AI自身に出力をタグで囲ませるスクリプト。
デバッグ情報を大幅に追加。
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
    print(f"📅 年: {year}")
    
    activities_dir = Path('docs/docs/activities')
    print(f"📁 ベースディレクトリ: {activities_dir}")
    
    repo_dirs = []
    
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
                        print(f"✅ 追加: {repo_dir}")

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
                    print(f"    ✅ {filename}: 読み込み成功")
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
    
    # --- ★★★ ここが修正点 ★★★ ---
    # プロンプトの末尾に、XMLタグで囲むよう明確な指示を追加
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
    print(f"🤖 プロンプト長: {len(prompt)} 文字")
    
    try:
        print("🤖 API呼び出し開始...")
        response = litellm.completion(
            model="gemini/gemini-2.5-pro",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        
        # --- ★★★ ここが修正点 ★★★ ---
        # AIからの応答をそのまま返す（AIがタグを付けてくれるはず）
        content = response.choices[0].message.content
        print(f"✅ AI応答受信: {len(content)} 文字")
        print(f"📝 AI応答プレビュー: {content[:150]}...")
        
        return content
        
    except Exception as e:
        print(f"❌ AI生成エラー ({repo_name}): {e}")
        
        # フォールバックコンテンツは、後続処理のために引き続きPython側でタグ付け
        fallback_content = f"""# 📅 {repo_name} - 日報 ({date})
## ⚠️ 注意
AI による日報生成に失敗しました。"""
        return f"<output-report>\n{fallback_content}\n</output-report>"

def save_repo_daily_report(repo_data, ai_generated_content, date):
    """リポジトリフォルダに日報を保存"""
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
    # AIがタグ付けしたコンテンツをそのまま結合する
    full_content = frontmatter + ai_generated_content
    
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"✅ ファイル保存成功: {report_file}")
    except Exception as e:
        print(f"❌ ファイル保存エラー: {e}")

def extract_report_content(filepath):
    """指定されたファイルから <output-report> タグ内のコンテンツを抽出"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.search(r'<output-report>(.*?)</output-report>', content, re.DOTALL)
        if match:
            return match.group(1).strip()
        else:
            print(f"⚠️ 警告: ファイル内に <output-report> タグが見つかりませんでした。 in {filepath}")
            # タグが見つからない場合は、フロントマター以降の全内容を返すなどの代替案も考えられる
            return None
    except FileNotFoundError:
        print(f"❌ 抽出エラー: ファイル '{filepath}' が見つかりません。")
        return None
    except Exception as e:
        print(f"❌ 抽出中にエラーが発生しました: {e}")
        return None

def main():
    print("🚀 Gemini 2.5 Pro で個別リポジトリ日報生成開始")
    
    if not os.getenv('GOOGLE_API_KEY'):
        print("❌ GOOGLE_API_KEY が未設定です。")
        return
    
    print("\n" + "="*50)
    print("📊 データ収集フェーズ")
    date, repo_dirs = find_todays_repos()
    
    if not repo_dirs:
        print("📝 本日の活動なし - 処理終了")
        return
    
    print("\n" + "="*50)
    print("🤖 日報生成・保存・抽出フェーズ")
    
    for i, repo_dir in enumerate(repo_dirs, 1):
        print(f"\n--- {i}/{len(repo_dirs)}: {repo_dir.name} ---")
        
        repo_data = load_repo_data(repo_dir)
        ai_generated_content = generate_repo_daily_report(repo_data, date)
        save_repo_daily_report(repo_data, ai_generated_content, date)
        
        # 保存したファイルからコンテンツを抽出して確認
        report_file_path = repo_dir / 'ai_daily_report.md'
        print(f"\n🔍 保存ファイルからコンテンツ抽出を実行: {report_file_path}")
        extracted_content = extract_report_content(report_file_path)
        
        if extracted_content:
            print("✅ 抽出成功！")
        else:
            print("❌ 抽出に失敗、またはタグが見つかりませんでした。")
    
    print("\n" + "="*50)
    print("✅ 全リポジトリの処理完了")
    print("="*50)

if __name__ == "__main__":
    main()
