import pandas as pd
import folium

data = pd.read_csv("crimes5.csv",sep =";") #Carrega o csv, esse arquivo precisa estar na pasta do projeto do PyCharm
filtered = data.DIA_DA_SEMANA == "Wednesday"  #Aplica o filtro para Wednesday
print(data[filtered]) #Printa os valores filtrados
print(len(data[filtered]))
filtrado = data[filtered]

mapa = folium.Map(location=[45.5236, -122.6750])
folium.Marker([45.5236, -122.675], popup='<i>Mt. Hood Meadows</i>').add_to(mapa)
#for diasemana in filtrado:
#    folium.Marker([filtrado.LATITUDE, filtrado.LONGITUDE], popup='<i>Mt. Hood Meadows</i>').add_to(mapa)
#mapa.save('Mapa.html')

