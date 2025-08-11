#!/usr/bin/env python3
import os, sys
import google.generativeai as genai

api_key = os.getenv("GOOGLE_API_KEY")
print("🔑 GOOGLE_API_KEY set?:", bool(api_key))
if not api_key:
    sys.exit(1)

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-pro")
resp = model.generate_content("返答は日本語で2語だけ。「動作OK」とだけ返して。")
text = (resp.text or "").strip()
print("🧪 SDK response:", repr(text))
if "動作OK" in text:
    print("✅ SDK OK")
    sys.exit(0)
else:
    print("⚠️ SDKは応答したが期待値と不一致")
    sys.exit(2)
