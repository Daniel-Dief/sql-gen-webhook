class ResponseAPI:
    def __init__(self, id: str, model: str, prompt: str):
        self.id = id
        self.model = model
        self.prompt = prompt

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "model": self.model,
            "prompt": self.prompt
        }