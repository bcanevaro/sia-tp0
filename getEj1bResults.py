import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import json

with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)
        balls = config["pokeballs"]
        pokemons = config["pokemon"]

balls.remove('pokeball')
print(balls)
print(pokemons)

cvs_file= "ej1a.csv"
data=pd.read_csv(cvs_file)

normalizedData = [[None for _ in range(len(balls))] for _ in range(len(pokemons))]


for i, pokemon in enumerate(pokemons):
    for j, ball in enumerate(balls):
        normalizedData[i][j] = (data[(data['pokemon'] == pokemon) & (data['ball'] == ball)]['Catch Rate'].values[0])/(data[(data['pokemon'] == pokemon) & (data['ball'] == 'pokeball')]['Catch Rate'].values[0])

# Sample data
labels = balls

# Number of labels
x = np.arange(len(labels))

# Width of the bars
width = 0.15  # Adjusted width for five bars

# Create the figure and axis
fig, ax = plt.subplots()

# Plotting the bars with correct offset
bar1 = ax.bar(x - 2*width, normalizedData[0], width, label=pokemons[0])
bar2 = ax.bar(x - width, normalizedData[1], width, label=pokemons[1])
bar3 = ax.bar(x, normalizedData[2], width, label=pokemons[2])
bar4 = ax.bar(x + width, normalizedData[3], width, label=pokemons[3])
bar5 = ax.bar(x + 2*width, normalizedData[4], width, label=pokemons[4])

# Adding labels, title, and legend
ax.set_xlabel('Ball')
ax.set_ylabel('Efectiveness: Ball catch rate / Pokeball catch rate')
ax.set_title('Effectiveness of pokeballs according to intrinsic properties of pokemons')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.axhline(y=1, color='r', linestyle='--', label='Threshold = 1')
# Show the plot
plt.show()
