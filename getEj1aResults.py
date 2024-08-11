import matplotlib.pyplot as plt
import pandas as pd

cvs_file= "ej1a.csv"
data=pd.read_csv(cvs_file)

group_by=data.groupby('ball')

balls=[]
catch_rates=[]
std_devs=[]

for ball,group_data in group_by:
    balls.append(ball)
    catch_rates.append(group_data['Catch Rate'].mean())
    std_devs.append(group_data['Catch Rate'].std())

plt.errorbar(
        balls,
        catch_rates,
        yerr=std_devs,
        fmt="o",
        label="Catch Rate",
        capsize=5
)

plt.xlabel("Pokeball")
plt.ylabel("Average Catch Rate")
plt.title("Average Catch Rate vs. Pokeball")
plt.grid()
plt.legend()

plt.show()

# Calcular la varianza de Catch Rate por tipo de ball
varianza = data.groupby('ball')['Catch Rate'].var()

# Crear un gráfico de barras para mostrar la varianza
plt.figure(figsize=(8, 5))
varianza.plot(kind='bar', color=['blue', 'orange'])

# Añadir etiquetas y título
plt.xlabel('Pokeball')
plt.ylabel('Varianza')
plt.title('Varianza de Catch Rate por Tipo de Pokéball')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar el gráfico
plt.show()