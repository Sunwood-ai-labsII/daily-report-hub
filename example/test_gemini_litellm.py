#!/usr/bin/env python3
import os, json, sys
import litellm

print("📦 litellm version:", getattr(litellm, "__version__", "unknown"))
print("🔑 GOOGLE_API_KEY set?:", bool(os.getenv("GOOGLE_API_KEY")))

# 失敗時に原因が見えるようログを有効化（標準出力に出ます）
litellm.set_verbose = True

prompt = "返答は日本語で、2語だけ。『動作OK』とだけ返して。"

try:
    resp = litellm.completion(
        model="gemini/gemini-2.5-pro",
        messages=[{"role": "user", "content": prompt}],
        # max_tokens=20,
        # temperature=0.2,
    )

    # 返却形式の揺れに強い取り出し
    content = ""
    ch0 = resp.choices[0]

    # OpenAI 互換パス
    try:
        msg = getattr(ch0, "message", None)
        if isinstance(msg, dict):
            content = msg.get("content") or ""
        elif msg is not None and hasattr(msg, "get"):
            content = msg.get("content") or ""
    except Exception:
        pass

    # text フィールド側に入るケース
    if not content and hasattr(ch0, "text"):
        content = ch0.text or ""

    # dataclass 風の .message.content に入るケース
    if not content and getattr(ch0, "message", None) is not None:
        content = getattr(ch0.message, "content", "") or content

    print("🧪 Model raw content:", repr(content))
    if not content.strip():
        raise RuntimeError("空の応答（content）が返りました。")

    print("✅ テスト成功")
    sys.exit(0)

except Exception as e:
    print("❌ テスト失敗:", type(e).__name__, e)
    # 可能なら生レスポンスも表示
    try:
        print("🔍 raw response:", json.dumps(resp.model_dump(), ensure_ascii=False)[:1200])
    except Exception:
        pass
    sys.exit(1)
