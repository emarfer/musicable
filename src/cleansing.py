import datetime
import os
from IPython.display import display
import time
import pandas as pd 

#import src.sqltools as sqt



def utslocal (uts):
    '''
    recibe una cadena de texto o interger que es uts(unix time stamp, valor en segundos de una fecha)
        unix timestamp count = This count starts at the Unix Epoch on January 1st, 1970 at UTC
    devuelve fecha y hora local. 
    '''
    if type(uts) == int:
        return datetime.datetime.fromtimestamp(uts).strftime('%Y-%m-%d %H:%M:%S')
    else:
        return datetime.datetime.fromtimestamp(int(uts)).strftime('%Y-%m-%d %H:%M:%S')



# def albumscv ():
#     print('cargando último csv generado')
#     time.sleep(1)
#     csvnewalbs = ('../../Base de datos/00_musicablecero/New_album/')
#     os.chdir(csvnewalbs)
#     reciente = sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)[-1] #último elemento de la lista es el archivo + reciente
#     if sqt.check_csv(reciente):
#         return('la estás liando, no toques más ¿por qué tocas?')
#     else:
#         ruta_archivo = f'../{csvnewalbs}{reciente}'
#         new_alb = pd.read_csv(ruta_archivo,sep=';')
#         print('datos cargados: ')
#         display(new_alb.head())
#         time.sleep(1)
#         print('modificando algunos datos para su insercción en base de datos musicablecero de mysql')
#         time.sleep(1)
#         new_alb.kbs = new_alb.kbs.str.replace(',','.').astype('float')
#         new_alb.creado = pd.to_datetime(new_alb.creado)
#         print('nuevos inserts en tag:\r')
#         time.sleep(1)
#         sqt.insert_csv(reciente)
#         new_inserts = sqt.taginserts(new_alb)
#         return new_inserts

def albumscv (csvnewalbs,reciente):

    ruta_archivo = f'../{csvnewalbs}{reciente}'
    new_alb = pd.read_csv(ruta_archivo,sep=';')
    print('datos cargados: ')
    display(new_alb.head())
    time.sleep(1)
    print('modificando algunos datos para en el dataframe para insertar posteriormente en mysql')
    time.sleep(1)
    new_alb.kbs = new_alb.kbs.str.replace(',','.').astype('float')
    new_alb.creado = pd.to_datetime(new_alb.creado)
    return new_alb

def archivojpg(relativa):
    try:
        x = [x for x in os.listdir(relativa) if x.lower() == 'folder.jpg'][0]
        return x
    except:
        return 'errrrrror'
  