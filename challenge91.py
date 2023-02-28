#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    # Part 1 
    # print(pokeapi["sprites"]["front_default"])

    # Part 2
    # for move in pokeapi["moves"]:
    #     print(move["move"]["name"])

    # Part 3
    print(f"{pokeapi['name']} has appeared in this many games: {len(pokeapi['game_indices'])}.")

    # Part 3 with a for loop
    game_indices = 0

    for game in pokeapi['game_indices']:
        game_indices += 1
    
    print(f"{pokeapi['name']} has appeard in {game_indices} video games.")

    



main()
