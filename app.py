from flask import Flask, request, jsonify
import requests
from io import BytesIO

app = Flask(__name__)

API_URL = "https://api.deepai.org/analyze-image-for-ads"

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
        img = requests.get(image_url, timeout=20)
        if img.status_code != 200:
            return jsonify({
                "success": False,
                "error": "Failed to download image"
            })

        files = {
            "image": ("image.jpg", BytesIO(img.content))
        }

        data = {
            "tool_name": "IMAGE TO PROMPT",
            "tool_description": "Get Image to Prompt by AI."
        }

        headers = {
    "api-key": "fe256fa3-fd5f-4418-a8c8-5152eb945fd6",
    "User-Agent": "Mozilla/5.0"
}

        r = requests.post(API_URL, files=files, data=data, headers=headers, timeout=60)

        if r.status_code != 200:
            return jsonify({
                "success": False,
                "error": r.text
            })

        result = r.json()

        prompt = None
        if result.get("descriptions"):
            prompt = result["descriptions"][0]

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
    app.run(host="0.0.0.0", port=5000)