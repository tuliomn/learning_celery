from tasks import get_pokemon


for x in range(1,20):
    get_pokemon.delay(x)
