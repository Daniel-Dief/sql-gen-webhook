import uuid
from pathlib import Path

def generate_uuid() -> str:
    """
    Gera um identificador UUID único que não esteja associado
    a um arquivo `.sql` existente no diretório `./app/responses/`.

    Returns:
        str: UUID gerado no formato de string.

    Observações:
        - A função garante que o UUID retornado não colida com um arquivo
          existente em `./app/responses/`.
        - O UUID é gerado no formato padrão `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.
    """
    while True:
        gen_uuid = str(uuid.uuid4())
        if not Path(f"./app/responses/{gen_uuid}.sql").exists():
            return gen_uuid