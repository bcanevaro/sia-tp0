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
        balls = config["pokeballs"][0]

        pokemons = config["pokemon"]

        iterations = 10000
        data = []

        statusList = [StatusEffect.POISON, StatusEffect.BURN, StatusEffect.PARALYSIS,
                      StatusEffect.SLEEP, StatusEffect.FREEZE]

        noneStatusCatchRate = {}

        for pokemon in pokemons:
            pokemonInstance = factory.create(pokemon, 100, StatusEffect.NONE, 1)
            averageCatchRate = np.average([attempt_catch(pokemonInstance, balls)[0] for _ in range(iterations)])
            noneStatusCatchRate[pokemon] = averageCatchRate


        for pokemon in pokemons:
            for status in statusList:
                pokemonInstance = factory.create(pokemon, 100, status, 1)

                normalizedAverageCatchRate = np.average([attempt_catch(pokemonInstance, balls)[0] for _ in range(iterations)]) / noneStatusCatchRate[pokemon]
                data.append([pokemonInstance.name, status, balls, normalizedAverageCatchRate])



        with open("ej2a.csv", "w") as file:
            writer = csv.writer(file)
            header = ["Pokemon", "Status", "Ball", "CatchRate"]
            writer.writerow(header)
            writer.writerows(data)

        # for pokemon in pokemons:
        #     pokemonInstances.append(factory.create(pokemon, 100, StatusEffect.NONE, 1))
        #
        # data=[]
        # for ball,pokemonInstance in product(balls, pokemonInstances):
        #         averageCatchRate=np.average([attempt_catch(pokemonInstance,ball)[0] for _ in range(iterations)])
        #         data.append([averageCatchRate,pokemonInstance.name,ball])
        #
        # with open("ej1a.csv", "w") as file:
        #     writer = csv.writer(file)
        #
        #     header = ["Catch Rate", "pokemon", "ball"]
        #     writer.writerow(header)
        #     writer.writerows(data)

