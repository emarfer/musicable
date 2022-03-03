import src.cleansing as cls
from IPython.display import display
import src.sqltools as sqt
import time

nuevoentag = cls.albumscv()
if nuevoentag == 'la estás liando, no toques más ¿por qué tocas?':
    print(nuevoentag)
    time.sleep(1)
    print('no te dejo que toques')
else:
    display(nuevoentag)
    time.sleep(1)
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
    print('insertando en mysql todos los datos')
    sqt.insertartistanoalbum()