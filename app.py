from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

genai.configure(api_key="AIzaSyBCwiVnS9C1oVNBv2wzA7RBtRTbpG2Q458")
model = genai.GenerativeModel("models/gemini-2.5-flash")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    response = model.generate_content(user_msg)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)
