import matplotlib.pyplot as plt
import pandas as pd

cvs_file= "ej1a.csv"
data=pd.read_csv(cvs_file)

basePokeballData=data[data['ball']=='pokeball'].drop(columns=['ball'])

pokemons=[]
catch_rates=[]


for catch_rate,pokemon in basePokeballData.values:
    pokemons.append(pokemon)
    catch_rates.append(catch_rate)


plt.bar(pokemons,height=catch_rates)
plt.show()



#
# balls=[]
# catch_rates=[]
# std_devs=[]
#
#
# for ball,group_data in group_by:
#     balls.append(ball)
#     catch_rates.append(group_data['Catch Rate'].mean())
#
#
#
# plt.bar(x=balls,height=catch_rates)
# plt.show()