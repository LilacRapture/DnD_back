import requests


# def test_post_character():
#     character = {"id": "3ed1edf7-be94-4c90-84b4-08b8f365a081",
#                  "name": "K",
#                  "character_class_id": "aa147908-0a75-4863-9dc0-1602e865e287"}
#     r_post = requests.post("https://dnd-back.onrender.com/api/characters/", json=character)
#     assert r_post.status_code == 201
#
#     r_get = requests.get("https://dnd-back.onrender.com/api/characters/3ed1edf7-be94-4c90-84b4-08b8f365a081")
#     expected_character = {"id": "3ed1edf7-be94-4c90-84b4-08b8f365a081",
#                           "name": "K",
#                           'character_class': {'id': 'aa147908-0a75-4863-9dc0-1602e865e287',
#                                               'name': 'Wizard'},
#                           "spells": []}
#     assert expected_character == r_get.json()


def test_delete_character():
    r_delete = requests.delete("https://dnd-back.onrender.com/api/characters/3ed1edf7-be94-4c90-84b4-08b8f365a081")
    assert r_delete.status_code == 200