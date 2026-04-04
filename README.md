🧠 IMAGE → PROMPT API DOCS

---

🔗 BASE URL
"https://your-domain.vercel.app"

---

📌 ENDPOINT
"GET /img2txt"

---

📥 PARAMS

- url (string) ✅ → Direct image link

---

🚀 REQUEST

/img2txt?url=IMAGE_URL

---

✅ RESPONSE

{
  "success": true,
  "prompt": "Generated image description"
}

---

❌ ERROR

{
  "success": false,
  "error": "Error message"
}

---

⚙️ WORKFLOW
URL → Fetch Image → DeepAI API → Prompt Output

---

📦 FEATURES

- ⚡ Fast response
- 🧠 AI prompt generation
- 🌐 Public image support

---

⚠️ NOTES

- Image must be public
- Timeout: 5s (fetch) / 20s (API)
- Uses DeepAI

---

👨‍💻 CREDIT
"@ab_devs"