import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


cvs_file = "ej2d.csv"
data = pd.read_csv(cvs_file)


pokemons = data['pokemon'].unique()
levels = data['level'].unique()


bar_width = 0.2
spacing = 0.3
index = np.arange(len(levels)) * (len(pokemons) * bar_width + spacing)

plt.figure(figsize=(12, 6))

for i, pokemon in enumerate(pokemons):
    subset = data[data['pokemon'] == pokemon]
    level_indices = np.array([np.where(levels == level)[0][0] for level in subset['level']])
    plt.bar(index[level_indices] + i * bar_width, subset['Catch Rate'], bar_width, label=pokemon)

plt.xlabel('Nivel')
plt.ylabel('Catch Rate')
plt.title('Catch Rate por Nivel para Diferentes Pokémon')
plt.xticks(index + bar_width * len(pokemons) / 2, levels)
plt.legend(title='Pokémon')
plt.grid(True, axis='y')

plt.show()
