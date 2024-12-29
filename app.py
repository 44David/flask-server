from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from PIL import Image
import io
from model import run_model
from s3 import upload

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
    file = request.data
    
    img = Image.open(io.BytesIO(file))
    img.save('output.png')
    
    # await run_model(file)

    # s3_link = await upload()
    
    # return jsonify({"s3_link": s3_link})

    return 'Hello'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
   
    