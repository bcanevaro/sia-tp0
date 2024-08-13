import json
import sys
import csv

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect

if __name__ == "__main__":
    factory = PokemonFactory("pokemon.json")

    with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)
        ball = config["pokeball"]
        pokemon = config["pokemon"]

        # Experiment parameters
        noise = 0.15
        samples = 100 # This is the amount of point we want to evaluate in the range of HP between 0 and 100%
        iterations = 100 # This is the amount of evaluations we want to take for each evaluation point

        data=[]
        hpPercentage = 0
        pokemonInstances = []
        hpIncrement = 1/samples

        # Load the pokemons with different HP %
        for i in range(samples):
            instance = factory.create(pokemon, 100, StatusEffect.NONE, hpPercentage)
            pokemonInstances.append(instance)            
            hpPercentage += hpIncrement

        # Append an array with the setted noise
        for _ in range(iterations):
            data.append([attempt_catch(pokemonInstances[i], ball, noise)[1] for i in range(samples)])

        # print(data)
        # pdData = pd.DataFrame(data)
        # print(pdData)
        with open("ej2b.csv", "w") as file:
            writer = csv.writer(file)
            header = [f'HP_{i}' for i in range(samples)]
            writer.writerow(header)
            writer.writerows(data)