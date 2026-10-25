
import requests
import random

my_pokemon_team = ["pikachu", "charizard", "bulbasaur", "squirtle", "gengar"]

chosen_pokemon = random.choice(my_pokemon_team)

pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{chosen_pokemon}"

pokemon_response = requests.get(pokemon_url, timeout=10)

if pokemon_response.status_code == 200:
    pokemon_data = pokemon_response.json()

    secret_pokemon = pokemon_data["name"]
    pokemon_height = pokemon_data["height"]
    pokemon_weight = pokemon_data["weight"]

    pokemon_skills = []

    for skill in pokemon_data["abilities"]:
        pokemon_skills.append(skill["ability"]["name"])

    print("Welcome to the Pokemon Guessing Game!")
    print("Guess the Pokemon using these clues:")
    print("Height:", pokemon_height)
    print("Weight:", pokemon_weight)
    print("Abilities:", ", ".join(pokemon_skills))

    remaining_chances = 3

    while remaining_chances > 0:
        my_guess = input("Enter your guess: ").strip().lower()

        if not my_guess:
            print("Please enter a Pokemon name.")
            remaining_chances -= 1
            print("Attempts left:", remaining_chances)
            continue

        guess_url = f"https://pokeapi.co/api/v2/pokemon/{my_guess}"
        guess_response = requests.get(guess_url, timeout=10)

        if guess_response.status_code == 404:
            print("Invalid Pokemon name.")
            remaining_chances -= 1
            print("Attempts left:", remaining_chances)
            continue

        if guess_response.status_code != 200:
            print("Failed to check the Pokemon name.")
            break

        if my_guess == secret_pokemon:
            print("Wow! Congrats!")
            break
        else:
            print("Wrong guess!")
            remaining_chances -= 1
            print("Attempts left:", remaining_chances)

    if remaining_chances == 0:
        print("Game over! The correct Pokemon was", secret_pokemon)

else:
    print("Failed to retrieve Pokemon data.")
