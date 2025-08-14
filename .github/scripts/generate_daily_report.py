#!/usr/bin/env python3
"""
AIにタグ付きで日報を生成させ、保存時にタグを削除して
純粋なMarkdownコンテンツのみをファイルに書き込むスクリプト。
レートリミット対応版。
"""

import os
import json
import glob
import re
import time
import random
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

def call_llm_with_retry(prompt, repo_name, max_retries=5, base_delay=1.0):
    """
    レートリミット対応のLLM呼び出し関数
    Exponential backoff + jitterを使用してリトライ
    詳細なエラー情報を表示
    """
    
    for attempt in range(max_retries):
        try:
            print(f"🤖 API呼び出し開始... (試行 {attempt + 1}/{max_retries})")
            
            # デバッグ: プロンプトの長さを表示
            print(f"📏 プロンプト長: {len(prompt)} 文字")
            
            response = litellm.completion(
                model="gemini/gemini-2.5-pro",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )
            
            # 詳細なレスポンス検証
            print(f"🔍 レスポンス詳細検証開始...")
            
            if not response:
                print(f"❌ レスポンスオブジェクトがNullです")
                return None
            
            print(f"✅ レスポンスオブジェクト受信: {type(response)}")
            
            # レスポンス構造の詳細ログ
            if hasattr(response, '__dict__'):
                print(f"🔍 レスポンス属性: {list(response.__dict__.keys())}")
            
            if not hasattr(response, 'choices'):
                print(f"❌ レスポンスに'choices'属性がありません")
                print(f"🔍 利用可能な属性: {dir(response)}")
                return None
            
            if not response.choices:
                print(f"❌ choices配列が空です")
                return None
            
            print(f"✅ choices配列長: {len(response.choices)}")
            
            choice = response.choices[0]
            if not hasattr(choice, 'message'):
                print(f"❌ choice[0]に'message'属性がありません")
                print(f"🔍 choice[0]の属性: {dir(choice)}")
                return None
            
            message = choice.message
            if not hasattr(message, 'content'):
                print(f"❌ messageに'content'属性がありません")
                print(f"🔍 messageの属性: {dir(message)}")
                return None
            
            content = message.content
            print(f"🔍 コンテンツタイプ: {type(content)}")
            print(f"🔍 コンテンツがNone: {content is None}")
            
            if content is None:
                print(f"❌ コンテンツがNoneです")
                return None
            
            content_str = str(content).strip()
            print(f"🔍 コンテンツ長（文字列化後）: {len(content_str)}")
            
            if not content_str:
                print(f"❌ コンテンツが空文字列です")
                # 空文字列の場合の詳細情報
                print(f"🔍 元のcontent repr: {repr(content)}")
                return None
            
            # 成功時の詳細ログ
            print(f"✅ AI応答受信完了 - 長さ: {len(content_str)} 文字")
            print(f"🔍 応答プレビュー（最初の200文字）: {content_str[:200]}...")
            
            return content_str
                
        except Exception as e:
            # より詳細なエラー情報を表示
            error_str = str(e).lower()
            print(f"❌ API呼び出し例外発生:")
            print(f"   エラータイプ: {type(e).__name__}")
            print(f"   エラーメッセージ: {str(e)}")
            
            # エラーの詳細情報があれば表示
            if hasattr(e, '__dict__'):
                print(f"   エラー属性: {e.__dict__}")
            
            # レートリミット関連のエラーを検出
            is_rate_limit = any(keyword in error_str for keyword in [
                'rate limit', 'quota exceeded', 'too many requests', 
                'rate_limit_exceeded', 'quota_exceeded', 'resource_exhausted',
                '429', 'throttled', 'rate limiting'
            ])
            
            if is_rate_limit:
                print(f"🚨 レートリミットエラーを検出")
                if attempt < max_retries - 1:  # 最後の試行でなければリトライ
                    # Exponential backoff with jitter
                    delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                    print(f"⏳ レートリミット対応: {delay:.1f}秒後にリトライします... ({attempt + 1}/{max_retries})")
                    time.sleep(delay)
                    continue
                else:
                    print(f"❌ レートリミット: 最大リトライ回数に達しました ({repo_name})")
                    return None
            else:
                # レートリミット以外のエラー
                print(f"❌ その他のAPI呼び出しエラー ({repo_name})")
                if attempt < max_retries - 1:
                    # 軽いリトライ（短い待機時間）
                    delay = base_delay + random.uniform(0, 0.5)
                    print(f"⏳ {delay:.1f}秒後にリトライします...")
                    time.sleep(delay)
                    continue
                else:
                    print(f"❌ その他エラー: 最大リトライ回数に達しました")
                    return None
    
    print(f"❌ 最大リトライ回数に達しました ({repo_name})")
    return None


def generate_repo_daily_report(repo_data, date):
    """個別リポジトリの日報を生成（AIにタグ付けを指示）- 改善版"""
    repo_name = repo_data['name']
    print(f"\n🤖 AI日報生成開始: {repo_name}")
    
    # まず最初にフォールバック用のコンテンツを準備
    fallback_content = f"""<output-report>
# 📅 {repo_name} - 日報 ({date})

## ⚠️ 注意
AI による日報生成に失敗しました。

## 📊 利用可能なデータ
"""
    
    # 利用可能なデータを追加
    if 'summary' in repo_data:
        fallback_content += f"\n### サマリー\n{repo_data['summary'][:500]}...\n"
    if 'commits' in repo_data:
        fallback_content += f"\n### コミット\n{repo_data['commits'][:500]}...\n"
    if 'stats' in repo_data:
        fallback_content += f"\n### 統計\n{repo_data['stats'][:200]}...\n"
    
    fallback_content += "\n</output-report>"
    
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
- **重要**: 完成した日報は、必ず `<output-report>` と `</output-report>` で全体を囲んでください。

また、下記を活用してエージェントからのこの日報の一言レビューを記載して
PANDA 先生 は客観的な評価を、FOX 教官は厳しめの評価を行います。
キャット ギャル はギャル口調で本質を捉えつつ経営者的な観点からの評価をします
```
:::tip PANDA 先生

一言レビュー

:::

:::danger FOX 教官

一言レビュー

:::

:::caution キャット ギャル

一言レビュー

:::

```

""")

    prompt = "\n".join(prompt_parts)
    
    # プロンプトの内容を一部確認
    print(f"📝 プロンプト生成完了 - 総文字数: {len(prompt)}")
    print(f"🔍 プロンプトプレビュー:\n{prompt[:300]}...")
    
    # レートリミット対応のLLM呼び出し（改善版）
    content = call_llm_with_retry(prompt, repo_name, max_retries=5, base_delay=1.0)
    
    if content:
        print(f"✅ AI日報生成成功 - {repo_name}")
        return content
    else:
        print(f"⚠️ AI生成失敗 - フォールバックコンテンツを使用: {repo_name}")
        return fallback_content

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
    print("🚀 Gemini 2.5 Pro 日報生成スクリプト開始（レートリミット対応版）")
    
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
        
        # AIにタグ付きで日報を生成させる（レートリミット対応）
        ai_response_with_tags = generate_repo_daily_report(repo_data, date)
        
        # この時点でai_response_with_tagsは必ず有効な文字列のはず（関数内で保証）
        
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
        
        # clean_reportが空でないことを確認
        if not clean_report:
            print("⚠️ 警告: 抽出されたコンテンツが空です。基本的な日報を生成します。")
            clean_report = f"""# 📅 {repo_data['name']} - 日報 ({date})

## ⚠️ 注意
日報の生成で問題が発生しました。データは正常に収集されています。
"""
        
        # タグが削除されたクリーンなコンテンツをファイルに保存
        save_repo_daily_report(repo_data, clean_report, date)
        
        # 複数のリポジトリを処理する場合、連続呼び出しを避けるため軽い待機
        if i < len(repo_dirs):
            print(f"⏳ 次のリポジトリ処理まで少し待機...")
            time.sleep(0.5)  # 500ms待機
    
    print("\n" + "="*50)
    print("✅ 全てのリポジトリの日報生成が完了しました。")
    print("="*50)

if __name__ == "__main__":
    main()

