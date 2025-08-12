from flask import Flask, request, jsonify
from dotenv import load_dotenv
from app.types.modelsTypes import dictModelType
from app.ia import gen_query
import os

load_dotenv()
app = Flask(__name__)

@app.route('/ai-process', methods=['POST'])
def process_request():
    prompt = request.json.get('prompt')
    model = dictModelType[request.json.get('model')]

    gen_query(prompt, model)

    return jsonify({
        "sucess": "OK"
    })

if __name__ == '__main__':
    app.run(
        host=os.getenv('HOST'),
        port=int(os.getenv('PORT', 5000)),
        debug=True,
        threaded=True
    )
