from dotenv import load_dotenv
from psycopg2 import connect
from os import getenv
from app.types.modelsTypes import ModelType

load_dotenv()

def save_request(uuid: str, model: ModelType, client_prompt: str) -> None:
    """
    Salva uma requisição no banco de dados para rastreamento futuro.

    Args:
        uuid (str): Identificador único da requisição.
        model (ModelType): Objeto contendo informações do modelo (nome, arquivo SQL e template).
        client_prompt (str): Prompt original enviado pelo cliente.

    Returns:
        None: A função não retorna valor.

    Observações:
        - A função conecta-se ao banco de dados PostgreSQL usando as variáveis de ambiente.
        - Insere um registro na tabela "Responses" com o UUID, nome do modelo e prompt do cliente.
        - Em caso de erro, a transação é revertida e uma mensagem de erro é impressa no console.    
    """
    conn = connect(
        dbname=getenv('DBNAME'),
        user=getenv('DBUSER'),
        password=getenv('DBPASSWORD'),
        host=getenv('DBHOST'),
        port=getenv('DBPORT')
    )
    cur = conn.cursor()

    insert_query = """
        INSERT INTO "Responses" ("Key", "Model", "ClientPrompt")
        VALUES (%s, %s, %s)
    """

    try:
        cur.execute(insert_query, (uuid, model.name, client_prompt))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"An error occurred while saving the request: {e}")
    finally:
        cur.close()
        conn.close()

def save_response(uuid: str, response: str) -> None:
    """
    Salva a resposta gerada pela IA no banco de dados.

    Args:
        uuid (str): Identificador único da requisição, usado para localizar o registro.
        response (str): Resposta gerada pela IA que deve ser salva.

    Returns:
        None: A função não retorna valor.
    
    Observações:
        - A função conecta-se ao banco de dados PostgreSQL usando as variáveis de ambiente.
        - Atualiza o registro na tabela "Responses" com a resposta gerada.
        - Em caso de erro, a transação é revertida e uma mensagem de erro é impressa no console.
    """
    
    conn = connect(
        dbname=getenv('DBNAME'),
        user=getenv('DBUSER'),
        password=getenv('DBPASSWORD'),
        host=getenv('DBHOST'),
        port=getenv('DBPORT')
    )
    cur = conn.cursor()

    update_query = """
        UPDATE "Responses"
        SET "Query" = %s
        WHERE "Key" = %s
    """

    try:
        cur.execute(update_query, (response, uuid))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"An error occurred while saving the response: {e}")
    finally:
        cur.close()
        conn.close()