import datetime
import os
from IPython.display import display
import time
import pandas as pd 
import src.sqltools as sqt
import src.cleansing as cls




csvnewalbs = ('../../Base de datos/00_musicablecero/New_album/')
os.chdir(csvnewalbs) #cambia dirección dónde se encuentra python
reciente = sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)[-1]
print(f'comprobando archivo {reciente}')
point = sqt.checkpoint_tag() #por si acaso hay que borrar luego los inserts en tag
if sqt.check_csv(reciente) == True:
    print('ya existe el archivo, deja de tocar cosas')
elif sqt.check_csv(reciente) == False:
    print('limipando datos')
    new_alb = cls.albumscv(csvnewalbs,reciente)
    print('insertando en mysql')
    nuevoentag = sqt.taginserts(new_alb)
    
    #comprobar si artista existe:
    art_ = list(nuevoentag.artist.unique())[0]
    if sqt.checkart(art_):
        print(f'{art_} existe, continuamos para bingo')
    else:
        print(f'hay que insertar datos de {art_} en mysql, que todavía no existe')
        sex_ = input(f'elige: masc, fem o indet como sexo de {art_}:\n')
        gen_ = input(f'qué tipo de música toca {art_}:\n')
        band_ = input(f'solitario: s, banda:b \n')
        pais_ = input(f'Cuál es el país originario de {art_}\n')
        print('vamos a insertar tus datos:')
        sqt.insert_newart(art_,sex_,gen_,band_,pais_)
    time.sleep(1)
    print('insertando/actualziadndo en mysql todos los datos en sus correspondientes tablas')
    sqt.insertartistanoalbum()
    sqt.insert_csv(reciente)
    #print(list(nuevoentag.jpg.unique()))
    print('insertando en mysql archivo de imagen')
    time.sleep(1)
    dfjpg = sqt.jpgalbum(point)
    dfjpg['relativa'] = dfjpg.folder.str.replace('\\','/',regex=True).str.replace('H:','../../..',regex=True)
    dfjpg['archivojpg'] = dfjpg.relativa.apply(cls.archivojpg)
    sqt.insert_jpg(dfjpg)
    print('imagen insertadas')


else:
    print(sqt.check_csv(reciente))

