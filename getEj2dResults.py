import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Leer el archivo CSV
cvs_file = "ej2d.csv"
data = pd.read_csv(cvs_file)

# Obtener la lista de Pokémon y niveles únicos
pokemons = data['pokemon'].unique()
levels = data['level'].unique()

# Configurar el ancho de las barras y la separación entre niveles
bar_width = 0.2
spacing = 0.3  # Espaciado adicional entre grupos de niveles
index = np.arange(len(levels)) * (len(pokemons) * bar_width + spacing)

# Crear el gráfico
plt.figure(figsize=(12, 6))

# Graficar los datos para cada Pokémon
for i, pokemon in enumerate(pokemons):
    subset = data[data['pokemon'] == pokemon]
    level_indices = np.array([np.where(levels == level)[0][0] for level in subset['level']])
    plt.bar(index[level_indices] + i * bar_width, subset['Catch Rate'], bar_width, label=pokemon)

# Ajustar etiquetas y títulos
plt.xlabel('Nivel')
plt.ylabel('Catch Rate')
plt.title('Catch Rate por Nivel para Diferentes Pokémon')
plt.xticks(index + bar_width * len(pokemons) / 2, levels)
plt.legend(title='Pokémon')
plt.grid(True, axis='y')

# Mostrar el gráfico
plt.show()
