import requests


def test_crud_character():
    character = {"id": "3ed1edf7-be94-4c90-84b4-08b8f365a081",
                 "name": "K",
                 "character_class_id": "aa147908-0a75-4863-9dc0-1602e865e287"}
    r_post = requests.post("https://dnd-back.onrender.com/api/characters/", json=character)
    assert r_post.status_code == 201

    r_get = requests.get("https://dnd-back.onrender.com/api/characters/3ed1edf7-be94-4c90-84b4-08b8f365a081")
    expected_character = {"id": "3ed1edf7-be94-4c90-84b4-08b8f365a081",
                          "name": "K",
                          "character_class": {'id': 'aa147908-0a75-4863-9dc0-1602e865e287',
                                              'name': 'Wizard'},
                          "spells": []}
    assert expected_character == r_get.json()

    character_updated = {"id": "3ed1edf7-be94-4c90-84b4-08b8f365a081",
                         "name": "Key",
                         "character_class_id": "aa147908-0a75-4863-9dc0-1602e865e287"}
    r_update = requests.put("https://dnd-back.onrender.com/api/characters/", json=character_updated)
    assert r_update.status_code == 200

    r_get_updated = requests.get("https://dnd-back.onrender.com/api/characters/3ed1edf7-be94-4c90-84b4-08b8f365a081")
    expected_character_updated = {"id": "3ed1edf7-be94-4c90-84b4-08b8f365a081",
                                  "name": "Key",
                                  "character_class": {'id': 'aa147908-0a75-4863-9dc0-1602e865e287',
                                                      'name': 'Wizard'},
                                  "spells": []}
    assert expected_character_updated == r_get_updated.json()

    r_delete = requests.delete("https://dnd-back.onrender.com/api/characters/3ed1edf7-be94-4c90-84b4-08b8f365a081")
    assert r_delete.status_code == 200

    r_get_deleted = requests.get("https://dnd-back.onrender.com/api/characters/3ed1edf7-be94-4c90-84b4-08b8f365a081")
    assert r_get_deleted.status_code == 404


def test_add_delete_character_spell():
    character = {"id": "18953a1b-4c25-489c-9171-3de06f670b26",
                 "name": "K",
                 "character_class_id": "aa147908-0a75-4863-9dc0-1602e865e287"}
    r_post_character = requests.post("https://dnd-back.onrender.com/api/characters/", json=character)

    r_post_spell = requests.post("https://dnd-back.onrender.com/api/characters/18953a1b-4c25-489c-9171-3de06f670b26/spells/8f92ed98-0ea0-46c0-8e0a-78358d5fc061")
    assert r_post_spell.status_code == 201

    character_with_spell = {"id": "18953a1b-4c25-489c-9171-3de06f670b26",
                                  "name": "K",
                                  "character_class": {'id': 'aa147908-0a75-4863-9dc0-1602e865e287',
                                                      'name': 'Wizard'},
                                  "spells": [{"id": "8f92ed98-0ea0-46c0-8e0a-78358d5fc061",
                                              "name": "Fireball"}]}
    r_get_character_with_spell = requests.get("https://dnd-back.onrender.com/api/characters/18953a1b-4c25-489c-9171-3de06f670b26")
    assert character_with_spell == r_get_character_with_spell.json()

    r_delete_spell = requests.delete("https://dnd-back.onrender.com/api/characters/18953a1b-4c25-489c-9171-3de06f670b26/spells/8f92ed98-0ea0-46c0-8e0a-78358d5fc061")
    assert r_delete_spell.status_code == 200

    r_get_character_without_spell = requests.get(
        "https://dnd-back.onrender.com/api/characters/18953a1b-4c25-489c-9171-3de06f670b26")
    character_without_spell = {"id": "18953a1b-4c25-489c-9171-3de06f670b26",
                               "name": "K",
                               "character_class": {'id': 'aa147908-0a75-4863-9dc0-1602e865e287',
                                                   'name': 'Wizard'},
                               "spells": []}
    assert character_without_spell == r_get_character_without_spell.json()
