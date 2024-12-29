from flask import Flask, jsonify, make_response
from flask_cors import CORS
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


@app.route('/api')
async def index():

    await run_model()

    s3_link = await upload()
    
    return jsonify({"s3_link": s3_link})

if __name__ == "__main__":
    app.run(host="0.0.0.0")
   
    