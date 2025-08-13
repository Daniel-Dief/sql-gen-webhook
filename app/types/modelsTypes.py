class ModelType:
    """
    Representa a estrutura de um modelo de ETL.

    Attributes:
        name (str): Nome do modelo.
        file_name (str): Endereço do arquivo SQL.
        prompt_file (str): Endereço do arquivo de prompt.
    """
    def __init__(self, name: str, file_name: str, prompt_file: str) -> None:
        self.name: str = name
        self.file_name: str = file_name
        self.prompt_file: str = prompt_file


# Dicionário com os modelos e endereços já mapeados.
dictModelType = {
    "hotel": ModelType("hotel", "hotel.sql", "hotel.txt"),
}