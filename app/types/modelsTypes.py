class ModelType:
    def __init__(self, name, file_name, prompt_file) -> None:
        self.name = name,
        self.file_name = file_name
        self.prompt_file = prompt_file

dictModelType = {
    "hotel": ModelType("hotel", "hotel.sql", "hotel.txt"),
}