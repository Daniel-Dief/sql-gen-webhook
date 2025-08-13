class ResponseAPI:
    """
    Representa a estrutura de uma resposta de API contendo
    identificador, modelo e prompt utilizado.

    Attributes:
        id (str): Identificador único da resposta (UUID).
        model (str): Nome do modelo seleciona.
        prompt (str): Texto do prompt enviado para processamento.
    """
    def __init__(self, id: str, model: str, prompt: str):
        self.id = id
        self.model = model
        self.prompt = prompt

    def to_json(self) -> dict:
        """
        Converte o objeto em um dicionário JSON-compatível.

        Returns:
            dict: Dicionário com as chaves "id", "model" e "prompt".
        """
        return {
            "id": self.id,
            "model": self.model,
            "prompt": self.prompt
        }
