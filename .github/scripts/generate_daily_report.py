#!/usr/bin/env python3
"""
各リポジトリフォルダに個別の日報のみを生成するシンプルスクリプト
デバッグ情報を大幅に追加
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
    
    print(f"🔍 検索開始: {today}")
    print(f"📅 年: {year}")
    
    # activities ディレクトリから今日のデータを探す
    activities_dir = Path('docs/docs/activities')
    print(f"📁 ベースディレクトリ: {activities_dir}")
    print(f"📁 ディレクトリ存在確認: {activities_dir.exists()}")
    
    repo_dirs = []
    
    # 年/週/日付の構造を探索
    year_dirs = list(activities_dir.glob(year))
    print(f"📂 年ディレクトリ数: {len(year_dirs)}")
    
    for year_dir in year_dirs:
        print(f"📂 年ディレクトリ: {year_dir}")
        week_dirs = list(year_dir.glob('week-*'))
        print(f"📅 週ディレクトリ数: {len(week_dirs)}")
        
        for week_dir in week_dirs:
            print(f"📅 週ディレクトリ: {week_dir}")
            date_dir = week_dir / today
            print(f"📅 日付ディレクトリ: {date_dir}")
            print(f"📅 日付ディレクトリ存在: {date_dir.exists()}")
            
            if date_dir.exists():
                repo_candidates = list(date_dir.iterdir())
                print(f"🔍 リポジトリ候補数: {len(repo_candidates)}")
                
                for repo_dir in repo_candidates:
                    print(f"📦 チェック中: {repo_dir}")
                    print(f"📦 ディレクトリ?: {repo_dir.is_dir()}")
                    
                    metadata_file = repo_dir / 'metadata.json'
                    print(f"📋 metadata.json: {metadata_file}")
                    print(f"📋 metadata.json存在: {metadata_file.exists()}")
                    
                    if repo_dir.is_dir() and metadata_file.exists():
                        repo_dirs.append(repo_dir)
                        print(f"✅ 追加: {repo_dir}")
                    else:
                        print(f"❌ スキップ: {repo_dir}")
    
    print(f"📊 最終的に見つかったリポジトリ数: {len(repo_dirs)}")
    for repo_dir in repo_dirs:
        print(f"  📦 {repo_dir}")
    
    return today, repo_dirs

def load_repo_data(repo_dir):
    """リポジトリのデータを読み込み"""
    print(f"\n📖 データ読み込み開始: {repo_dir.name}")
    repo_data = {'name': repo_dir.name, 'path': repo_dir}
    
    # 各ファイルの存在確認と読み込み
    files_to_check = [
        ('summary', 'daily_summary.md'),
        ('commits', 'daily_commits.md'),
        ('changes', 'daily_cumulative_diff.md'),
        ('stats', 'daily_diff_stats.md'),
        ('code_diff', 'daily_code_diff.md')
    ]
    
    for key, filename in files_to_check:
        file_path = repo_dir / filename
        print(f"  📄 {filename}: 存在={file_path.exists()}")
        
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if key == 'commits':
                        content = content[:3000]  # 最初の3000文字
                    repo_data[key] = content
                    print(f"    ✅ 読み込み成功: {len(content)} 文字")
            except Exception as e:
                print(f"    ❌ 読み込みエラー: {e}")
        else:
            print(f"    ⚠️ ファイルなし")
    
    print(f"📖 読み込み完了: {len(repo_data)-2} ファイル")  # name, path除く
    return repo_data

def generate_repo_daily_report(repo_data, date):
    """個別リポジトリの日報を生成"""
    repo_name = repo_data['name']
    print(f"\n🤖 AI日報生成開始: {repo_name}")
    
    # プロンプト構築
    prompt_parts = [f"以下の{repo_name}リポジトリの{date}の活動データから、日報をMarkdown形式で作成してください:\n"]
    
    if 'summary' in repo_data:
        prompt_parts.append(f"## サマリー:\n{repo_data['summary']}\n")
        print(f"  📊 サマリー追加: {len(repo_data['summary'])} 文字")
    
    if 'commits' in repo_data:
        prompt_parts.append(f"## コミット詳細:\n{repo_data['commits']}\n")
        print(f"  💻 コミット追加: {len(repo_data['commits'])} 文字")
    
    if 'changes' in repo_data:
        prompt_parts.append(f"## ファイル変更:\n{repo_data['changes']}\n")
        print(f"  📁 変更追加: {len(repo_data['changes'])} 文字")
    
    if 'stats' in repo_data:
        prompt_parts.append(f"## 統計:\n{repo_data['stats']}\n")
        print(f"  📈 統計追加: {len(repo_data['stats'])} 文字")
    
    prompt_parts.append("""
日報作成要求:
- このリポジトリの今日の開発活動を要約
- 主要な変更点と技術的ポイントをハイライト
- 開発の進捗状況を評価
- 注目すべき改善や追加機能があれば言及
- 明日以降の開発への提案があれば記載
- 日本語で読みやすく、簡潔に記述
- 絵文字を効果的に使用""")
    
    prompt = "\n".join(prompt_parts)
    print(f"🤖 プロンプト長: {len(prompt)} 文字")
    print(f"🤖 使用モデル: gemini/gemini-2.5-pro")
    
    try:
        print("🤖 API呼び出し開始...")
        response = litellm.completion(
            model="gemini/gemini-2.5-pro",  # 正しいモデル名に修正
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        
        content = response.choices[0].message.content
        print(f"✅ AI応答受信: {len(content)} 文字")
        print(f"📝 AI応答プレビュー: {content[:100]}...")
        
        return content
        
    except Exception as e:
        print(f"❌ AI生成エラー ({repo_name}): {e}")
        print(f"🔍 エラー詳細: {type(e).__name__}")
        
        # フォールバック日報
        fallback_content = f"""# 📅 {repo_name} - 日報 ({date})

## 📊 基本情報
- リポジトリ: {repo_name}
- 日付: {date}
- 生成時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## ⚠️ 注意
AI による日報生成に失敗しました。既存のサマリーファイルをご確認ください。

### 利用可能なデータ
"""
        
        for key in ['summary', 'commits', 'changes', 'stats']:
            if key in repo_data:
                fallback_content += f"- {key}: ✅\n"
            else:
                fallback_content += f"- {key}: ❌\n"
        
        fallback_content += "\n---\n*手動での日報作成をお願いします*"
        
        return fallback_content

def save_repo_daily_report(repo_data, daily_report, date):
    """リポジトリフォルダに日報を保存"""
    repo_dir = repo_data['path']
    report_file = repo_dir / 'ai_daily_report.md'
    
    print(f"\n💾 ファイル保存開始: {report_file}")
    
    # フロントマター作成（デバッグ情報付き）
    frontmatter = f"""---
title: "{repo_data['name']} - AI日報"
date: "{date}"
sidebar_position: 1
description: "AI生成による{repo_data['name']}の開発日報"
tags: ["daily-report", "ai-generated", "{repo_data['name']}", "{date}"]
---

"""
    
    print(f"📝 フロントマター:")
    print(frontmatter)
    
    # 完全なコンテンツ
    full_content = frontmatter + daily_report
    
    print(f"📝 総コンテンツ長: {len(full_content)} 文字")
    
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        print(f"✅ ファイル保存成功: {report_file}")
        
        # 保存後の確認
        if report_file.exists():
            file_size = report_file.stat().st_size
            print(f"📊 保存ファイルサイズ: {file_size} bytes")
        else:
            print(f"❌ ファイル保存確認失敗")
            
    except Exception as e:
        print(f"❌ ファイル保存エラー: {e}")

def main():
    print("🚀 Gemini 2.5 Pro で個別リポジトリ日報生成開始")
    print(f"⏰ 実行時刻: {datetime.now().isoformat()}")
    
    # 環境変数確認
    api_key = os.getenv('GOOGLE_API_KEY')
    if api_key:
        print(f"🔑 GOOGLE_API_KEY: 設定済み (長さ: {len(api_key)})")
    else:
        print("❌ GOOGLE_API_KEY: 未設定")
        return
    
    # データ収集
    print("\n" + "="*50)
    print("📊 データ収集フェーズ")
    print("="*50)
    
    date, repo_dirs = find_todays_repos()
    print(f"\n📊 結果: {date} - {len(repo_dirs)}個のリポジトリ")
    
    if not repo_dirs:
        print("📝 本日の活動なし - 処理終了")
        return
    
    # 各リポジトリの日報生成
    print("\n" + "="*50)
    print("🤖 日報生成フェーズ")
    print("="*50)
    
    for i, repo_dir in enumerate(repo_dirs, 1):
        print(f"\n--- {i}/{len(repo_dirs)}: {repo_dir.name} ---")
        
        # データ読み込み
        repo_data = load_repo_data(repo_dir)
        
        # 日報生成
        daily_report = generate_repo_daily_report(repo_data, date)
        
        # 保存
        save_repo_daily_report(repo_data, daily_report, date)
    
    print("\n" + "="*50)
    print("✅ 全リポジトリの日報生成完了")
    print("="*50)

if __name__ == "__main__":
    main()
