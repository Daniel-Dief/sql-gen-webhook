import uuid
from pathlib import Path

def generate_uuid() -> str:
    while True:
        gen_uuid = str(uuid.uuid4())
        if not Path(
            f"./app/responses/{gen_uuid}.sql"
        ).exists():
            return gen_uuid
