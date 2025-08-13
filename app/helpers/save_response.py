def save_response(uuid: str, response: str) -> None:
    """
    Salva uma resposta em um novo arquivo `.sql` no diretório `./app/responses/`.

    Args:
        uuid (str): Identificador único usado para nomear o arquivo.
        response (str): Conteúdo a ser salvo no arquivo, geralmente um script SQL.

    Returns:
        None: A função não retorna valor.

    Observações:
        - Se já existir um arquivo com o mesmo `uuid`, será levantado um FileExistsError.
        - O diretório `./app/responses/` deve existir antes da execução da função.
    """
    with open(f"./app/responses/{uuid}.sql", "x", encoding="utf-8") as f:
        f.write(response)