def save_response(uuid: str, response: str) -> None:
    with open(f"./app/responses/{uuid}.sql", "w", encoding="utf-8") as f:
        f.write(response)