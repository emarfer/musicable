import src.mongofun as mong
import src.cleansing as cls

lastuser = 'AveKaesar'
print(f'importando datos de lastfm del usuario {lastuser} e insertándolos en mongodb' )
mong.mongouser(lastuser)

lastuser = 'Sinatxester'
print(f'importando datos de lastfm del usuario {lastuser} e insertándolos en mongodb')
mong.mongouser(lastuser)

masusuarios = cls.newuser()
if masusuarios == False:
    print('Hasta luego Maricarmen')
else:
    usuario = input('¿Qué usuario quieres insertar?: \n')
    print(f'importando datos de lastfm del usuario {usuario} e insertándolos en mongodb' )
    mong.mongouser(usuario)

