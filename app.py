from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
ENDPOINT = os.getenv("ENDPOINT")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    audio_data = request.data
    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Content-Type": "audio/wav"
    }
    params = {"language": "en-US"}
    response = requests.post(
        f"{ENDPOINT}/speech/recognition/conversation/cognitiveservices/v1",
        headers=headers,
        params=params,
        data=audio_data
    )
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)