import src.mongofun as mong # importa el módulo mongofun.py
import src.cleansing as cls # importa el módulo cleansing.py

lastuser = 'aveKaesar' # usuario de last.fm
print(f'importando datos de lastfm del usuario {lastuser}' ) # imprime en pantalla el mensaje
mong.mongouser(lastuser) # inserta los datos de los scrobbles en la base de datos (mongouser() es una función definida en mongofun.py)

lastuser = 'sinatxester' # usuario de last.fm
print(f'importando datos de lastfm del usuario {lastuser}') # imprime en pantalla el mensaje
mong.mongouser(lastuser) # inserta los datos de los scrobbles en la base de datos (mongouser() es una función definida en mongofun.py)

masusuarios = cls.newuser() # obtiene los nuevos usuarios de la base de datos (newuser() es una función definida en cleansing.py)
if masusuarios == False: # si no hay nuevos usuarios en la base de datos
    print('Hasta luego Maricarmen') # imprime en pantalla el mensaje

elif masusuarios == True: # si hay nuevos usuarios en la base de datos
    # print(masusuarios, 'prueba') # imprime en pantalla el número de nuevos usuarios
    usuario_imput = input('¿Qué usuario quieres insertar?: \n') # pide al usuario que introduzca el nombre de un usuario
    usuario = usuario_imput.lower()
    print(f'importando datos de lastfm del usuario {usuario}' ) # imprime en pantalla el mensaje
    mong.mongouser(usuario) # inserta los datos de los scrobbles en la base de datos (mongouser() es una función definida en mongofun.py)