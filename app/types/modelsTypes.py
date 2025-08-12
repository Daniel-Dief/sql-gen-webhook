class ModelType:
    def __init__(self, name: str, file_name: str, prompt_file: str) -> None:
        self.name : str = name
        self.file_name : str = file_name
        self.prompt_file : str = prompt_file

dictModelType = {
    "hotel": ModelType("hotel", "hotel.sql", "hotel.txt"),
}