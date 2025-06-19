from flask import Flask, request, render_template, jsonify
import openai
import os

# 从环境变量中读取 API Key（不写死在代码中）
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")

    # 使用你的微调模型（如果有），否则可改为 gpt-3.5-turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 或 "ft:gpt-3.5-turbo:xxx"（换成你的微调模型ID）
        messages=[
            {"role": "system", "content": "你是一位温柔体贴、懂得倾听的AI伴侣，善于理解人类情绪并给予鼓励。"},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

