# in terminal with enabled venv: pytest run.py
import requests


def test_create_delete_user():
    r_create = requests.post("https://dnd-back.onrender.com/api/auth/sign-up")
    assert r_create.status_code == 200

    user_id = r_create.json()["token"]
    r_delete = requests.delete(f"https://dnd-back.onrender.com/api/users/{user_id}")
    assert r_delete.status_code == 200


# def test_crud_character():
#     r_create_user = requests.post("https://dnd-back.onrender.com/api/auth/sign-up")
#     user_id = r_create_user.json()["token"]
#     character = {"id": "3ed1edf7-be94-4c90-84b4-08b8f365a081",
#                  "name": "Test",
#                  "character_class_id": "ebc892d8-3e86-4cf4-b43b-f459a836cf08"}
#     r_post = requests.post("https://dnd-back.onrender.com/api/characters/",
#                            headers={"x-dnd-auth": user_id},
#                            json=character)
#     assert r_post.status_code == 201
#
#     r_get = requests.get("https://dnd-back.onrender.com/api/characters/3ed1edf7-be94-4c90-84b4-08b8f365a081")
#     expected_character = {"id": "3ed1edf7-be94-4c90-84b4-08b8f365a081",
#                           "name": "Test",
#                           "character_class": {'id': 'ebc892d8-3e86-4cf4-b43b-f459a836cf08',
#                                               'name': 'Wizard'},
#                           "spells": []}
#     assert expected_character == r_get.json()
#
#     character_updated = {"id": "3ed1edf7-be94-4c90-84b4-08b8f365a081",
#                          "name": "Key",
#                          "character_class_id": "ebc892d8-3e86-4cf4-b43b-f459a836cf08"}
#     r_update = requests.put("https://dnd-back.onrender.com/api/characters/", json=character_updated)
#     assert r_update.status_code == 200
#
#     r_get_updated = requests.get("https://dnd-back.onrender.com/api/characters/3ed1edf7-be94-4c90-84b4-08b8f365a081")
#     expected_character_updated = {"id": "3ed1edf7-be94-4c90-84b4-08b8f365a081",
#                                   "name": "Key",
#                                   "character_class": {'id': 'ebc892d8-3e86-4cf4-b43b-f459a836cf08',
#                                                       'name': 'Wizard'},
#                                   "spells": []}
#     assert expected_character_updated == r_get_updated.json()
#
#     r_delete = requests.delete("https://dnd-back.onrender.com/api/characters/3ed1edf7-be94-4c90-84b4-08b8f365a081")
#     assert r_delete.status_code == 200
#
#     r_get_deleted = requests.get("https://dnd-back.onrender.com/api/characters/3ed1edf7-be94-4c90-84b4-08b8f365a081")
#     assert r_get_deleted.status_code == 404
#     requests.delete(f"http://0.0.0.0:8000/api/users/{user_id}")
#
#
# def test_add_delete_character_spell():
#     r_create_user = requests.post("https://dnd-back.onrender.com/api/auth/sign-up")
#     user_id = r_create_user.text
#     character = {"id": "18953a1b-4c25-489c-9171-3de06f670b26",
#                  "name": "Test",
#                  "character_class_id": "ebc892d8-3e86-4cf4-b43b-f459a836cf08"}
#     r_post_character = requests.post("https://dnd-back.onrender.com/api/characters/",
#                                      headers={"x-dnd-auth": user_id},
#                                      json=character)
#
#     r_post_spell = requests.post("https://dnd-back.onrender.com/api/characters"
#                                  "/18953a1b-4c25-489c-9171-3de06f670b26/spells/b851efe1-7a92-43d9-af00-8338d413f045")
#     assert r_post_spell.status_code == 201
#
#     character_with_spell = {"id": "18953a1b-4c25-489c-9171-3de06f670b26",
#                             "name": "Test",
#                             "character_class": {'id': 'ebc892d8-3e86-4cf4-b43b-f459a836cf08',
#                                                 'name': 'Wizard'},
#                             "spells": [{"id": "b851efe1-7a92-43d9-af00-8338d413f045",
#                                         "name": "Fireball"}]}
#     r_get_character_with_spell = requests.get("https://dnd-back.onrender.com/api/characters"
#                                               "/18953a1b-4c25-489c-9171-3de06f670b26")
#     assert character_with_spell == r_get_character_with_spell.json()
#
#     r_delete_spell = requests.delete("https://dnd-back.onrender.com/api/characters/"
#                                      "18953a1b-4c25-489c-9171-3de06f670b26/spells/b851efe1-7a92-43d9-af00-8338d413f045")
#     assert r_delete_spell.status_code == 200
#
#     r_get_character_without_spell = requests.get(
#         "https://dnd-back.onrender.com/api/characters/18953a1b-4c25-489c-9171-3de06f670b26")
#     character_without_spell = {"id": "18953a1b-4c25-489c-9171-3de06f670b26",
#                                "name": "Test",
#                                "character_class": {'id': 'ebc892d8-3e86-4cf4-b43b-f459a836cf08',
#                                                    'name': 'Wizard'},
#                                "spells": []}
#     assert character_without_spell == r_get_character_without_spell.json()
#
#     requests.delete(f"http://0.0.0.0:8000/api/users/{user_id}")
