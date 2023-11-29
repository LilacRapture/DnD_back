from typing import Annotated
from fastapi import FastAPI, Header, Response, status, Depends
import uvicorn

from character.list import character_list_handler
from character.view import character_handler, spell_handler


app = FastAPI()


@app.get("/api/characters/")
async def list_characters(response: Response,
                          characters: Annotated[list, Depends(character_list_handler)],
                          x_dnd_auth: Annotated[str | None, Header()] = None):
    if x_dnd_auth is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return

    return characters


@app.get("/api/characters/{character_id}")
async def read_character(character_id: str):
    return character_handler(character_id)


@app.get("/api/spells/{spell_id}")
async def read_spell(spell_id: str):
    return spell_handler(spell_id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# source venv/bin/activate.fish
# add '.' in imports
# uvicorn app.run_api:app --host 0.0.0.0 --port 8000
