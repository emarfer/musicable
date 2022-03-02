import src.cleansing as cls
from IPython.display import display
import src.sqltools as sqt

nuevoentag = cls.albumscv()
display(nuevoentag)

#comprobar si artista existe:
art_ = list(nuevoentag.artist.unique())[0]
if sqt.checkart(art_):
    print(f'{art_} existe, continuamos para bingo')
else:
    print(f'hay que insertar datos de {art_} en mysql, que todavía no existe')
    sex_ = input('elige: masc, fem o indet como sexo de {art_}:\r')
    gen_ = input('qué tipo de música toca {art_}:\r')
    band_ = input('solitario: s, banda:b\r')
    pais_ = input('Cuál es el país originario de {art_}')
    print('vamos a insertar tus datos:')
    sqt.insert_newart(art_,sex_,gen_,band_,pais_)

print('insertando en mysql todos los datos')
sqt.insertartistanoalbum()