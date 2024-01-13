from typing import Annotated, Any
from fastapi import FastAPI, Header, Response, status, Depends, Request, HTTPException
import uvicorn
from mediatr import Mediator
from uuid import UUID

from src.app.utils.DiContainer import DiContainer

from src.app.character.create import character_create_handler
from src.app.character.edit import character_edit_handler

from src.business.domain.user.use_cases.create import CreateUserRequest
from src.business.domain.user.use_cases.delete import DeleteUserRequest
from src.business.domain.character.use_cases.list import ListCharactersRequest
from src.business.domain.character.use_cases.read import ReadCharacterRequest
from src.business.domain.character.use_cases.delete import DeleteCharacterRequest
from src.business.domain.character.use_cases.add_spell import AddSpellToCharacterRequest
from src.business.domain.character.use_cases.delete_spell import DeleteSpellFromCharacterRequest
from src.business.domain.character_class.use_cases.list import ListCharacterClassesRequest
from src.business.domain.spell.use_cases.list import ListSpellsRequest
from src.business.domain.spell.use_cases.read import ReadSpellRequest

# update spells list with character class parameter


app = FastAPI()
container = DiContainer()
container.wire(packages=["src.business", "src.infrastructure"])
container.init_resources()


@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    if request.url.path.startswith("/api/auth/"):
        return await call_next(request)

    if "X-DND-AUTH" not in request.headers:
        return Response(status_code=403, content="Forbidden")

    return await call_next(request)


@app.post("/api/auth/sign-up")
async def create_user(mediator: Annotated[Mediator, Depends(Mediator)]):
    return await mediator.send_async(CreateUserRequest())


@app.delete("/api/users/me")
async def delete_user(mediator: Annotated[Mediator, Depends(Mediator)],
                      x_dnd_auth: Annotated[str | None, Header()] = None):
    print(x_dnd_auth)
    await mediator.send_async(DeleteUserRequest(x_dnd_auth))


@app.get("/api/characters/")
async def list_characters(mediator: Annotated[Mediator, Depends(Mediator)],
                          x_dnd_auth: Annotated[str | None, Header()] = None):
    characters = await mediator.send_async(ListCharactersRequest(x_dnd_auth))
    return characters


@app.get("/api/character-classes/")
async def list_character_classes(mediator: Annotated[Mediator, Depends(Mediator)]):
    character_classes = await mediator.send_async(ListCharacterClassesRequest())
    return character_classes


@app.post("/api/characters/", status_code=201)
async def create_character(character: Annotated[Any, Depends(character_create_handler)]):
    return character


@app.get("/api/characters/{character_id}")
async def read_character(character_id: UUID,
                         response: Response,
                         mediator: Annotated[Mediator, Depends(Mediator)],
                         x_dnd_auth: Annotated[str | None, Header()] = None):
    character = await mediator.send_async(ReadCharacterRequest(x_dnd_auth, character_id))
    if character is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return
    return character


@app.put("/api/characters/")
async def edit_character(character: Annotated[Any, Depends(character_edit_handler)]):
    return character


@app.delete("/api/characters/{character_id}")
async def delete_character(character_id: UUID,
                           mediator: Annotated[Mediator, Depends(Mediator)],
                           x_dnd_auth: Annotated[str | None, Header()] = None):
    await mediator.send_async(DeleteCharacterRequest(x_dnd_auth, character_id))


@app.get("/api/spells/")
async def list_spells(mediator: Annotated[Mediator, Depends(Mediator)]):
    spells = await mediator.send_async(ListSpellsRequest())
    return spells


@app.post("/api/characters/{character_id}/spells/{spell_id}", status_code=201)
async def add_spell_to_character(character_id: UUID,
                                 spell_id: UUID,
                                 mediator: Annotated[Mediator, Depends(Mediator)],
                                 x_dnd_auth: Annotated[str | None, Header()] = None):
    # TODO: check auth
    await mediator.send_async(AddSpellToCharacterRequest(character_id, spell_id))


@app.delete("/api/characters/{character_id}/spells/{spell_id}")
async def delete_spell_from_character(character_id: UUID,
                                      spell_id: UUID,
                                      mediator: Annotated[Mediator, Depends(Mediator)],
                                      x_dnd_auth: Annotated[str | None, Header()] = None):
    # TODO: check auth
    await mediator.send_async(DeleteSpellFromCharacterRequest(character_id, spell_id))


@app.get("/api/spells/{spell_id}")
async def read_spell(spell_id: UUID,
                     mediator: Annotated[Mediator, Depends(Mediator)]):
    spell = await mediator.send_async(ReadSpellRequest(spell_id))
    return spell


if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=8000)  # for prod
    uvicorn.run("run_api:app", host="0.0.0.0", port=8000, reload=True)  # for development
