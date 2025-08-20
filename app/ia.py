from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from pathlib import Path
from app.types.modelsTypes import ModelType
from app.helpers.save_response import save_response, save_request
from app.helpers.uuid import generate_uuid
from threading import Thread
from app.types.responseAPI import ResponseAPI

def gen_query(prompt: str, model: ModelType) -> ResponseAPI:
    """
    Gera uma requisição assíncrona para criar uma query baseada em um modelo de IA e um prompt fornecido.

    Args:
        prompt (str): Texto de solicitação do usuário.
        model (ModelType): Objeto contendo informações do modelo (nome, arquivo SQL e template).

    Returns:
        ResponseAPI: Objeto contendo o ID (UUID), o nome do modelo e o prompt original.

    Observações:
        - A execução da IA ocorre em segundo plano via `Thread`.
        - Ao iniciar a requisição para o modelo de IA, é criado um registro no banco para a futura query.
    """
    template = Path(f"./app/prompts/{model.prompt_file}").read_text(encoding="utf-8")
    schema = Path(f"./app/models/{model.file_name}").read_text(encoding="utf-8")

    prompt_template = PromptTemplate(
        input_variables=["schema", "prompt"],
        template=template
    )
    final_prompt = prompt_template.format(schema=schema, prompt=prompt)

    uuid = generate_uuid()

    save_request(uuid, model, final_prompt)

    Thread(
        target=request_ai,
        args=(final_prompt, uuid)
    ).start()

    return ResponseAPI(
        id=uuid,
        model=model.name,
        prompt=prompt
    )

def request_ai(prompt: str, uuid: str) -> None:
    """
    Executa a requisição ao modelo de IA e salva o resultado em arquivo.

    Args:
        prompt (str): Prompt formatado a ser enviado para o modelo.
        uuid (str): Identificador único da requisição, usado para nomear o arquivo de resposta.

    Returns:
        None: A função não retorna valor.

    Observações:
        - A resposta gerada é salva em um banco de dados postgres.
    """
    llm_model = OllamaLLM(model="gpt-oss:20b")
    response = llm_model.invoke(prompt)

    save_response(
        uuid,
        response
    )