from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from pathlib import Path
from app.types.modelsTypes import ModelType
from app.helpers.save_response import save_response
from app.helpers.uuid import generate_uuid
from threading import Thread
from app.types.responseAPI import ResponseAPI

def gen_query(prompt: str, model: ModelType) -> ResponseAPI:
    template = Path(f"./app/prompts/{model.prompt_file}").read_text(encoding="utf-8")
    schema = Path(f"./app/models/{model.file_name}").read_text(encoding="utf-8")

    prompt_template = PromptTemplate(
        input_variables=["schema", "prompt"],
        template=template
    )
    final_prompt = prompt_template.format(schema=schema, prompt=prompt)

    uuid = generate_uuid()

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
    llm_model = OllamaLLM(model="gpt-oss:20b")
    response = llm_model.invoke(prompt)

    save_response(
        uuid,
        response
    )