import datetime
import os
from IPython.display import display
import time
import pandas as pd 
import src.sqltools as sqt
import src.cleansing as cls




csvnewalbs = ('../../Base de datos/00_musicablecero/New_album/') # directorio de los nuevos álbumes
os.chdir(csvnewalbs) #cambia dirección dónde se encuentra python
reciente = sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)[-1]  # obtiene el último archivo de la carpeta
print(f'comprobando archivo {reciente}') # imprime en pantalla el nombre del último archivo de la carpeta
point = sqt.checkpoint_tag() #por si acaso hay que borrar luego los inserts en tag y album
if sqt.check_csv(reciente) == True: # comprueba si el archivo es un csv válido (check_csv() es una función definida en sqltools.py)
    print('ya existe el archivo, deja de tocar cosas')  # imprime en pantalla el mensaje
elif sqt.check_csv(reciente) == False: # comprueba si el archivo es un csv válido (check_csv() es una función definida en sqltools.py)
    print('limipando datos') # imprime en pantalla el mensaje
    new_alb = cls.albumscv(csvnewalbs,reciente) # limpia los datos del álbum (albumscv() es una función definida en cleansing.py) 
    print('insertando en mysql') # imprime en pantalla el mensaje
    nuevoentag = sqt.taginserts(new_alb) # inserta los datos de los tags en la base de datos (taginserts() es una función definida en sqltools.py)
    
    #comprobar si artista existe:
    art_ = list(nuevoentag.artist.unique())[0] # obtiene el artista del álbum  (unique() es una función definida en pandas)
    if sqt.checkart(art_): # comprueba si el artista existe en la base de datos (checkart() es una función definida en sqltools.py)
        print(f'{art_} existe, continuamos para bingo') # imprime en pantalla el mensaje
    else:   # si el artista no existe en la base de datos
        print(f'hay que insertar datos de {art_} en mysql, que todavía no existe') # imprime en pantalla el mensaje
        sex_ = input(f'elige: masc, fem o indet como sexo de {art_}:\n') # pregunta el sexo del artista y da a elegir entre tres opciones
        gen_ = input(f'qué tipo de música toca {art_}:\n') # pregunta por el género de la música que toca el artista 
        band_ = input(f'solitario: s, banda:b \n') # pregunta si es solitario o es una banda
        pais_ = input(f'Cuál es el país originario de {art_}\n') # pregunta por el país de origen del artista
        print('vamos a insertar tus datos:') # imprime en pantalla el mensaje
        sqt.insert_newart(art_,sex_,gen_,band_,pais_) # inserta datos del artista en la base de datos (insert_newart es una función definida en sqltools.py)
    time.sleep(1) # espera un segundo
    print('insertando/actualziadndo en mysql todos los datos en sus correspondientes tablas') # imprime en pantalla el mensaje
    sqt.insertartistanoalbum() # inserta los datos de los artistas en la tabla artistas (insertartistanoalbum() es una función definida en sqltools.py)
    sqt.insert_csv(reciente) # inserta los datos del álbum en la tabla newcsv (insert_csv es una función definida en sqltools.py)
    #print(list(nuevoentag.jpg.unique()))
    print('insertando en mysql archivo de imagen') # imprime en pantalla el mensaje
    time.sleep(1) # espera un segundo
    dfjpg = sqt.jpgalbum(point) # inserta los datos de las imágenes en la tabla jpg (jpgalbum() es una función definida en sqltools.py)
    dfjpg['relativa'] = dfjpg.folder.str.replace('\\','/',regex=True).str.replace('H:','../../..',regex=True) # reemplaza los caracteres especiales de la ruta
    dfjpg['archivojpg'] = dfjpg.relativa.apply(cls.archivojpg) # crea una columna con el nombre del archivo de la imagen (archivojpg() es una función definida en cleansing.py)
    sqt.insert_jpg(dfjpg) # inserta los datos de las imágenes en la tabla jpg (insert_jpg es una función definida en sqltools.py)
    print('imagen insertadas') # imprime en pantalla el mensaje


else: # si el archivo no es un csv válido
    print(sqt.check_csv(reciente))  # imprime en pantalla el mensaje de error de csv inválido (check_csv() es una función definida en sqltools.py)

