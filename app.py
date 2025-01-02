from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from PIL import Image
import io
from model import run_model
from s3 import Upload

app = Flask(__name__)
CORS(app)

@app.route('/')
def page():
    return " "

@app.route('/api', methods=['POST'])
def index():
    req_json = request.get_json()
    s3_url = req_json.get("s3Url")

    labelled_image_url = run_model(s3_url)

    return jsonify({ "s3_labelled_url": labelled_image_url })

if __name__ == "__main__":
    app.run(host="0.0.0.0")
   
    