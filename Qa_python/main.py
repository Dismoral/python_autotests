import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change_name = {
    "pokemon_id": "211724",
    "name": "Добрый Клоун",
    "photo_id": 3
}

body_add_pokeball = {
    "pokemon_id": "211724"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.status_code)
print(response_create.text)'''


'''response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.status_code)
print(response_change_name.text)'''

'''response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.status_code)
print(response_add_pokeball.text)'''