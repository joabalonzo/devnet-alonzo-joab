import requests
import random


poke_list = ["charizard" , "ivysaur" , "charmeleon" , "blastoise" , "bulbasaur"]
url = "https://pokeapi.co/api/v2/pokemon/"

def get_random_pokemon():

    random_pokemon = random.choice(poke_list)

    response = requests.get(f"{url}/{random_pokemon}")
    return response.json()

print(get_random_pokemon())





 