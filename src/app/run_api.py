from typing import Annotated, Any
from fastapi import FastAPI, Header, Response, status, Depends
import uvicorn
from sqlmodel import SQLModel, create_engine

from character.list import character_list_handler
from character.view import character_handler
from spell.view import spell_handler


app = FastAPI()


# @app.on_event("startup")
# async def startup():
#     db_name = "database.db"
#     url = f'sqlite:///{db_name}'
#     engine = create_engine(url, echo=True)
#     SQLModel.metadata.create_all(engine)


@app.get("/api/characters/")
async def list_characters(response: Response,
                          characters: Annotated[list, Depends(character_list_handler)],
                          x_dnd_auth: Annotated[str | None, Header()] = None):
    if x_dnd_auth is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return

    return characters


@app.get("/api/characters/{character_id}")
async def read_character(character: Annotated[Any, Depends(character_handler)]):
    return character


@app.get("/api/spells/{spell_id}")
async def read_spell(spell_id, spell: Annotated[Any, Depends(spell_handler)]):
    return spell


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# source venv/bin/activate.fish
# add '.' in imports
# uvicorn app.run_api:app --host 0.0.0.0 --port 8000
