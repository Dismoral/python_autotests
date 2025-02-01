import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'TOKEN'
HEADER = {'Content-Type' : 'application/json'}
TRAINER_ID = '17744'

def test_status_code():
    response_status_code = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_status_code.status_code == 200

def test_part_of_response():
    response_part_of_response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_part_of_response.json()["data"][0]["trainer_name"] == 'Dismoral'