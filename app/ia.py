from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from pathlib import Path
from app.types.modelsTypes import ModelType
from random import random

def gen_query(prompt: str, model: ModelType):
    template = Path(f"./app/prompts/{model.prompt_file}").read_text(encoding="utf-8")
    schema = Path(f"./app/models/{model.file_name}").read_text(encoding="utf-8")

    prompt_template = PromptTemplate(
        input_variables=["schema", "prompt"],
        template=template
    )

    final_prompt = prompt_template.format(schema=schema, prompt=prompt)

    llm_model = OllamaLLM(model="gpt-oss:20b")

    response = llm_model.invoke(final_prompt)

    uuid = str(random()).split(".")[1]

    with open(f"./app/responses/{uuid}.sql", "w", encoding="utf-8") as f:
        f.write(response)