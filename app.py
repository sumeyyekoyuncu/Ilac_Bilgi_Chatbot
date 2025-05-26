from flask import Flask, render_template, request, jsonify
from responses import get_bot_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    data = request.get_json()
    print("Gelen veri:", data)
    if not data or "msg" not in data:
        return jsonify({"reply": "Bir hata oluştu: mesaj alınamadı."})
    user_input = data["msg"]
    response = get_bot_response(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
