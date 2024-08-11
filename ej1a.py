import json
import sys
import csv
from itertools import product

import numpy as np

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")

    with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)
        balls = config["pokeballs"]

        pokemons = config["pokemon"]

        pokemonInstances=[]
        iterations=100000

        for pokemon in pokemons:
            pokemonInstances.append(factory.create(pokemon, 100, StatusEffect.NONE, 1))

        data=[]
        for ball,pokemonInstance in product(balls, pokemonInstances):
                averageCatchRate=np.average([attempt_catch(pokemonInstance,ball)[0] for _ in range(iterations)])
                data.append([averageCatchRate,pokemonInstance.name,ball])

        with open("ej1a.csv", "w") as file:
            writer = csv.writer(file)

            header = ["Catch Rate", "pokemon", "ball"]
            writer.writerow(header)
            writer.writerows(data)



