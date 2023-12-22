from typing import Annotated, Any
from fastapi import FastAPI, Header, Response, status, Depends
import uvicorn

from src.app.character.list import character_list_handler, character_class_list_handler
from src.app.character.view import character_handler
from src.app.character.create import character_create_handler
from src.app.character.edit import character_edit_handler
from src.app.character.manage_spells import add_spell_to_character_handler, delete_spell_from_character_handler
from src.app.spell.view import spell_handler
from src.app.spell.list import spell_list_handler


app = FastAPI()


@app.get("/api/characters/")
async def list_characters(response: Response,
                          characters: Annotated[list, Depends(character_list_handler)],
                          x_dnd_auth: Annotated[str | None, Header()] = None):
    if x_dnd_auth is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return

    return characters


@app.get("/api/character_classes/")
async def list_character_classes(character_classes: Annotated[list, Depends(character_class_list_handler)]):
    return character_classes


@app.post("/api/characters/", status_code=201)
async def create_character(character: Annotated[Any, Depends(character_create_handler)]):
    return character


@app.get("/api/characters/{character_id}")
async def read_character(character: Annotated[Any, Depends(character_handler)]):
    return character


@app.put("/api/characters/")
async def edit_character(character: Annotated[Any, Depends(character_edit_handler)]):
    return character


@app.get("/api/spells/")
async def list_spells(spells: Annotated[list, Depends(spell_list_handler)]):
    return spells


@app.post("/api/characters/{character_id}/spells/{spell_id}", status_code=201)
async def add_spell_to_character(_: Annotated[Any, Depends(add_spell_to_character_handler)]):
    return


@app.delete("/api/characters/{character_id}/spells/{spell_id}")
async def delete_spell_from_character(_: Annotated[Any, Depends(delete_spell_from_character_handler)]):
    return


@app.get("/api/spells/{spell_id}")
async def read_spell(spell: Annotated[Any, Depends(spell_handler)]):
    return spell


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
