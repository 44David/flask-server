from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from PIL import Image
import io
from model import run_model
from s3 import Upload

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Does this update?'

@app.route('/test', methods=['GET', 'POST'])
def test():    
    message = { "res": "Hello from flask server" }
    return jsonify(message)


@app.route('/api', methods=['POST'])
def index():
    req_json = request.get_json()
    
    img_buffer = req_json.get("fileBuffer")
    img_name = req_json.get("fileName")
    img_type = req_json.get("fileType")


    upload = Upload()

    s3_link = upload.s3_upload(img_buffer, img_name, img_type)
    run_model(s3_link)

    return 'Hello'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
   
    