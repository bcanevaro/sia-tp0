import json
import sys
import csv
from itertools import product

import numpy as np

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

class pokemonInstanceWithLevel:
    def __init__(self,pokemonInstance,pokemonLevel):
        self.pokemonInstance=pokemonInstance
        self.pokemonLevel=pokemonLevel

    def getPokemonInstance(self):
        return self.pokemonInstance

    def getPokemonLevel(self):
        return self.pokemonLevel



if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")

    with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)
        balls = config["pokeballs"]

        pokemons = config["pokemon"]
        levels=[1,20,40,60,80,100]

        pokemonInstancesWithLevel=[]
        iterations=100000


        for pokemon in pokemons:
            for level in levels:
                pokemonInstancesWithLevel.append(pokemonInstanceWithLevel(factory.create(pokemon, level, StatusEffect.NONE, 1),level))


        data=[]
        for ball,pokemonInstanceWithLevel in product(balls, pokemonInstancesWithLevel):
                averageCatchRate=np.average([attempt_catch(pokemonInstanceWithLevel.getPokemonInstance(),ball)[0] for _ in range(iterations)])
                data.append([averageCatchRate,pokemonInstanceWithLevel.getPokemonInstance().name,pokemonInstanceWithLevel.getPokemonLevel()])

        with open("ej2d.csv", "w") as file:
            writer = csv.writer(file)

            header = ["Catch Rate", "pokemon","level"]
            writer.writerow(header)
            writer.writerows(data)



