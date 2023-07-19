from httpx import get
from celery import Celery

from Pokemon import Pokemon

app = Celery(
    'amqp://guest@localhost//'
)

@app.task
def get_pokemon(id: int):
    response = get(
        url=f'https://pokeapi.co/api/v2/pokemon/{id}'
    )
    if response.status_code == 200:
        return response.json()
    raise ValueError('Erro ao recuperar informações da POKEAPI')


def save_pokemon_data(pokemon: Pokemon):
    ...
