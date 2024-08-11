import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from src.pokemon import StatusEffect

cvs_file= "./ej2a.csv"
data=pd.read_csv(cvs_file)

group_by=data.groupby('Status')

data = pd.read_csv(cvs_file).pivot(index='Status', columns='Pokemon', values='CatchRate')
order = ["caterpie", "snorlax", "jolteon", "onix", "mewtwo"]
data = data[order]
statusOrder = [StatusEffect.POISON.name, StatusEffect.BURN.name,
                StatusEffect.PARALYSIS.name, StatusEffect.SLEEP.name, StatusEffect.FREEZE.name]
data = data.reindex(statusOrder)

plt.figure(figsize=(10,8))

barsCount = len(data)
width = 0.15
x = np.arange(len(data))

for i, pokemon in enumerate(data.columns):
    plt.bar(x + i * width, data[pokemon], width, label=pokemon)

plt.xlabel('Health Status Effect')
plt.ylabel('Capture Rate / Capture Rate when status is NONE')
plt.title('Pokémon Capture Rates by Status Effect and Pokemon')
plt.xticks(x + width * (barsCount / 2 - 0.5), data.index)
plt.legend(title='Pokemon')
plt.axhline(y=1, color='r', linestyle='--', label='Threshold = 1')

plt.show()