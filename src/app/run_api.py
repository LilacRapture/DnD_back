from typing import Annotated, Any
from fastapi import FastAPI, Header, Response, status, Depends
import uvicorn
from mediatr import Mediator

from src.app.utils.DiContainer import DiContainer

from src.app.user.create import user_create_handler, UserDto
from src.app.user.delete import user_delete_handler
from src.app.character.list import character_list_handler
from src.app.character.view import character_handler
from src.app.character.create import character_create_handler
from src.app.character.edit import character_edit_handler
from src.app.character.delete import character_delete_handler
from src.business.domain.character_class.use_cases.list import ListCharacterClassesRequest
from src.app.character.manage_spells import add_spell_to_character_handler, delete_spell_from_character_handler
from src.app.spell.view import spell_handler
from src.app.spell.list import spell_list_handler

# update spells list with character class parameter


app = FastAPI()
container = DiContainer()
container.wire(packages=["src.business", "src.infrastructure"])
# container.init_resources()


@app.post("/api/auth/sign-up")
async def create_user(user: Annotated[UserDto, Depends(user_create_handler)]):
    return user


@app.delete("/api/users/{user_id}")
async def delete_user(_: Annotated[UserDto, Depends(user_delete_handler)]):
    return


@app.get("/api/characters/")
async def list_characters(response: Response,
                          characters: Annotated[list, Depends(character_list_handler)],
                          x_dnd_auth: Annotated[str | None, Header()] = None):
    if x_dnd_auth is None:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return

    return characters


@app.get("/api/character-classes/")
async def list_character_classes(mediator: Annotated[Mediator, Depends(Mediator)],
                                 x_dnd_auth: Annotated[str | None, Header()] = None):
    character_classes = await mediator.send_async(ListCharacterClassesRequest())
    return character_classes


@app.post("/api/characters/", status_code=201)
async def create_character(character: Annotated[Any, Depends(character_create_handler)],
                           x_dnd_auth: Annotated[str | None, Header()] = None):
    return character


@app.get("/api/characters/{character_id}")
async def read_character(response: Response,
                         character: Annotated[Any, Depends(character_handler)],
                         x_dnd_auth: Annotated[str | None, Header()] = None):
    if character is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return
    return character


@app.put("/api/characters/")
async def edit_character(character: Annotated[Any, Depends(character_edit_handler)],
                         x_dnd_auth: Annotated[str | None, Header()] = None):
    return character


@app.delete("/api/characters/{character_id}")
async def delete_character(_: Annotated[Any, Depends(character_delete_handler)],
                           x_dnd_auth: Annotated[str | None, Header()] = None):
    return


@app.get("/api/spells/")
async def list_spells(spells: Annotated[list, Depends(spell_list_handler)],
                      x_dnd_auth: Annotated[str | None, Header()] = None):
    return spells


@app.post("/api/characters/{character_id}/spells/{spell_id}", status_code=201)
async def add_spell_to_character(_: Annotated[Any, Depends(add_spell_to_character_handler)],
                                 x_dnd_auth: Annotated[str | None, Header()] = None):
    return


@app.delete("/api/characters/{character_id}/spells/{spell_id}")
async def delete_spell_from_character(_: Annotated[Any, Depends(delete_spell_from_character_handler)],
                                      x_dnd_auth: Annotated[str | None, Header()] = None):
    return


@app.get("/api/spells/{spell_id}")
async def read_spell(spell: Annotated[Any, Depends(spell_handler)],
                     x_dnd_auth: Annotated[str | None, Header()] = None):
    return spell


if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=8000)  # for prod
    uvicorn.run("run_api:app", host="0.0.0.0", port=8000, reload=True)  # for development
