import time
import pandas as pd
import os
import shutil
import dotenv
dotenv.load_dotenv()
import sqlalchemy as alch

passw = os.getenv("mysql")
dbName = "musicablecero"
connectionData = f"mysql+pymysql://root:{passw}@localhost/{dbName}"
engine = alch.create_engine(connectionData)


#ccheking if ther is not list to create

def check_tempos():
    lista = []
    temporadas = list(engine.execute(f'''
    select distinct temporada from temporadas order by id_tem
    '''))
    tem_list = [t[0] for t in temporadas]
    for tem in tem_list:
        if tem+'.m3u' not in os.listdir('../../Music_listas/archivosm3u/'):
            lista.append(tem)
    if len(lista) == 0:
        return 'listas de rep al día'
    else:
        return lista

def create_datframe(lista):
    for l in lista:
        tempo = l
        idtem_q = list(engine.execute(f'''
                  select id_tem from temporadas where temporada = '{tempo}'  
                    '''))[0][0]
        print(f'creating dataframe with temoporada: {tempo}')
        time.sleep(1)
        df = pd.read_sql_query(f'''
                   select  artist, album, title, ruta, secs
                    from total where id_Can in (select id_Can from listas_rep where id_tem = {idtem_q} order by id_lr);
                    ''',engine)
        print(f'creating m3u file with temoporada: {tempo}')
        time.sleep(1)
        file = open(f'output/listas_rep/{tempo}.txt','w')
        file.write('#EXTM3U'+os.linesep)
        file.write(f'''#PLAYLIST:{tempo}'''+os.linesep)
        for i,r in df.iterrows():
            file.write(f'''#EXTINF:{r.secs}, {r.artist} - {r.album} - {r.title}'''+os.linesep)
            file.write(f'''{r.ruta} '''+os.linesep)
        file.close()
        pre, ext = os.path.splitext(file.name)
        os.rename(file.name, pre + '.m3u')
        src_file = f'''output/listas_rep/{tempo}.m3u'''
        dest_file = f'''../../Music_listas/archivosm3u/{tempo}.m3u'''
        shutil.copyfile(src_file,dest_file)
        print(f'''{tempo} creado y copiado''')
        time.sleep(1)
        
        


