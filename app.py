from flask import Flask, request, jsonify
import requests
from io import BytesIO

app = Flask(__name__)

# 🔥 API_URL پێویستە بەم شێوەیە بێت بۆ وەرگرتنی پڕۆمپت لە وێنە
API_URL = "https://api.deepai.org/api/analyze-image-for-ads"

@app.route("/")
def home():
    return {
        "credit": "@j4ck_721s",
        "endpoint": "/jack-img2prompt?url=IMAGE_URL"
    }

@app.route("/jack-img2prompt")
def img2txt():
    image_url = request.args.get("url")

    if not image_url:
        return jsonify({
            "success": False,
            "error": "Missing image url"
        })

    try:
        # 🔥 Headers بۆ download کردن
        headers_img = {
            "User-Agent": "Mozilla/5.0"
        }

        img = requests.get(image_url, headers=headers_img, timeout=20)

        if img.status_code != 200:
            return jsonify({
                "success": False,
                "error": "Failed to download image"
            })

        # 🔥 بۆ دەناردنی وێنە بە DeepAI
        files = {
            "image": ("image.jpg", BytesIO(img.content))
        }

        # 🔐 API KEY (ئەمە ئەوەی تۆ نووسیوە، بەڵام دەتوانیت لە Environment Variable داینابێیت)
        api_key = "fe256fa3-fd5f-4418-a8c8-5152eb945fd6"
        
        headers = {
            "api-key": api_key,
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.post(API_URL, files=files, headers=headers, timeout=60)

        if r.status_code != 200:
            return jsonify({
                "success": False,
                "error": r.text
            })

        result = r.json()
        
        # 🔥 دەرهێنانی پڕۆمپت لە وەڵامەکە
        prompt = None
        # هەندێک جار DeepAI لە "output"دا دەگەڕێت، نەک "descriptions"
        if result.get("descriptions"):
            prompt = result["descriptions"][0]
        elif result.get("output"):
            prompt = result["output"]

        return jsonify({
            "success": True,
            "prompt": prompt
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=8080)
