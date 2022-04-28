import os
from IPython.display import display
import pandas as pd
import time

import src.apilast as als
import src.sqltools as sqt
import src.cleansing as cls



keylast = os.getenv("keylast") # API key de last.fm
# l_user = input('enter lastfm user: ')
# if l_user.lower() != 'sinatxester':
#     print(f"has escrito '{l_user.upper()}', seguro que querías poner 'SINATXESTER', vamos a runear esto como si lo hubieras escrito bien")
#     l_user = 'sinatxester'
# elif l_user.lower() == 'sinatxester':
#     print('muy bien, aprendiste a escribir')
l_user = 'sinatxester' # usuario de last.fm
print(f'Importing scrobbles from {l_user}') # imprime en pantalla 
time.sleep(2) # espera 2 segundos
limit = 1000 # limit de scrobbles a importar
lastuts = sqt.maxuts() # obtiene la última fecha de importación de scrobbles

dating = cls.utslocal(lastuts) # convierte la última fecha de importación a formato local

print(f'recovering scrobbles since {dating}') # imprime en pantalla
time.sleep(2) # espera 2 segundos

recenttracks = als.req_lastfm (l_user,limit,lastuts) # obtiene los scrobbles de la API de last.fm usando la API key y parámetros: usuario, limit y última fecha de importación

if type(recenttracks) == pd.DataFrame: # si el tipo de dato es un dataframe (es decir, si la API de last.fm devuelve datos)
    print(f'ready to insert {len(recenttracks)} new tracks') # imprime en pantalla el número de nuevos scrobbles
else: # si no
    print(recenttracks)  # imprime en pantalla el mensaje de error de la API de last.fm
time.sleep(2) # espera 2 segundos


if type(recenttracks) == pd.DataFrame: # si el tipo de dato es un dataframe (es decir, si la API de last.fm devuelve datos)
    for i,r in recenttracks.iterrows(): # itera sobre los scrobbles de la API de last.fm (iterrows() itera sobre los índices y los datos)
        sqt.insert_data(r.uts, r.artist, r.artist_mbid, r.album, r.album_mbid, r.title, r.track_mbid) # inserta los datos de los scrobbles en la base de datos

    insertadas = sqt.act_scro() # obtiene el número de scrobbles insertados en la base de datos (act_scro() es una función definida en sqltools.py)
    display(insertadas) # muestra el número de scrobbles insertados en la base de datos

