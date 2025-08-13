from flask import Flask, request, jsonify
from dotenv import load_dotenv
from app.types.modelsTypes import dictModelType
from app.ia import gen_query
import os

load_dotenv()
app = Flask(__name__)

@app.route('/ai-process', methods=['POST'])
def process_request():
    """
    Endpoint para processar solicitações de geração de query via IA.

    Returns:
        flask.Response: Resposta JSON no formato:
            {
                "id": "<uuid>",
                "model": "<nome_do_modelo>",
                "prompt": "<prompt_original>"
            }

    Códigos de resposta HTTP:
        - 200: Solicitação aceita com sucesso.
        - 400: Caso o JSON enviado esteja incompleto ou inválido (não tratado explicitamente no código atual).

    Observações:
        - A execução real da IA ocorre em segundo plano; o endpoint retorna imediatamente.
        - O resultado gerado será salvo em `./app/responses/{uuid}.sql`.
    """
    prompt = request.json.get('prompt')
    model = dictModelType[request.json.get('model')]

    response = gen_query(prompt, model)

    return jsonify(response.to_json())

if __name__ == '__main__':
    app.run(
        host=os.getenv('HOST'),
        port=int(os.getenv('PORT', 5000)),
        debug=True,
        threaded=True
    )