import pandas as pd
import os
import sqlalchemy as alch
import dotenv

dotenv.load_dotenv()

passw = os.getenv("mysql")
dbName = "musicablecero"
connectionData = f"mysql+pymysql://root:{passw}@localhost/{dbName}"
engine = alch.create_engine(connectionData)

def maxuts():
    '''
    llama a la función maxuts que devuelve el último uts insertado en la tabla scrobbling
    '''
    return list(engine.execute(f'SELECT maxuts();'))[0][0]

def columnas(tabla):
    '''
    recibe el nombre de una tabla y devuleve una lista de las columnas de esa tabla
    '''
    df = pd.read_sql_query(f"""
        SELECT * FROM {tabla} ;
        """
        , engine)
    
    return list(df.columns)


def insert_data(uts, artist, artist_mbid, album, album_mbid, title, track_mbid):
    '''
    recibe los datos del datframe creado con la api de ultimos tracks de lastfm
    inserta los datos en la tabla scrobbling de mysql
    '''
    
    if '"' not in str(artist) and '"' not in str(album) and '"' not in str(title):
        try:
            engine.execute(f"""
                    INSERT INTO scrobbling (uts, artist, artist_mbid, album, album_mbid, title, track_mbid)
                    VALUES ({uts}, "{artist}", "{artist_mbid}", "{album}", "{album_mbid}", "{title}","{track_mbid}");
                    """)
        except:
            print(f'{uts} sin comillas en ningún lugar')    
            next
    elif '"' in str(artist) and '"' not in str(album) and '"' not in str(title):
        try:
            engine.execute(f"""
                    INSERT INTO scrobbling (uts, artist, artist_mbid, album, album_mbid, title, track_mbid)
                    VALUES ({uts}, '{artist}', "{artist_mbid}", "{album}", "{album_mbid}", "{title}","{track_mbid}");
                    """)
        except:
            print(f'{uts} con comillas en artista')    
            next
    elif '"' not in str(artist) and '"' in str(album) and '"' not in str(title):
        try:
            engine.execute(f"""
                    INSERT INTO scrobbling (uts, artist, artist_mbid, album, album_mbid, title, track_mbid)
                    VALUES ({uts}, "{artist}", "{artist_mbid}", '{album}', "{album_mbid}", "{title}","{track_mbid}");
                    """)
        except:
            print(f'{uts} con comillas en album')    
            next
    elif '"' not in str(artist) and '"' not in str(album) and '"' in str(title):
        try:
            engine.execute(f"""
                    INSERT INTO scrobbling (uts, artist, artist_mbid, album, album_mbid, title, track_mbid)
                    VALUES ({uts}, "{artist}", "{artist_mbid}", "{album}", "{album_mbid}", '{title}',"{track_mbid}");
                    """)
        except:
            print(f'{uts} con comillas en title')    
            next

def insert_newalb(Artist, Album, Title, Track, released, secs, kbs, creado, ruta, archivo,tipo, bitrate):
    
    '''
    recibe los datos del datframe con los tags de un nuevo album
    inserta los datos en la tabla tag del la base de datos musicablecero
    '''
    folder = ruta.replace('\\','\\\\')
    
    if '"' not in str(Artist) and '"' not in str(Album) and '"' not in str(Title):
        try:
            engine.execute(f"""
                    INSERT INTO tag (artist, album, title, Track, released, secs, kbs,creado, folder,archivo, tipo, bitrate)
                    VALUES  ("{Artist}", "{Album}", "{Title}", {Track}, {released}, {secs}, {kbs},"{creado}", "{folder}", "{archivo}", "{tipo}", {bitrate});
                    """)
        except Exception as e:
            print(e)
            print(f'{archivo} sin comillas en ningún lugar')    
            next
    elif '"' in str(Artist) and '"' not in str(Album) and '"' not in str(Title):
        try:
            engine.execute(f"""
                    INSERT INTO tag (artist, album, title, Track, released, secs, kbs,creado, folder,archivo, tipo, bitrate)
                    VALUES ('{Artist}', "{Album}", "{Title}", {Track}, {released}, {secs}, {kbs},"{creado}", "{folder}", "{archivo}", "{tipo}", {bitrate});
                    """)
        except Exception as e:
            print(e)
            print(f'{archivo} con comillas en artista')    
            next
    elif '"' not in str(Artist) and '"' in str(Album) and '"' not in str(Title):
        try:
            engine.execute(f"""
                    INSERT INTO tag (artist, album, title, Track, released, secs, kbs,creado, folder,archivo, tipo, bitrate)
                    VALUES  ("{Artist}", '{Album}', "{Title}", {Track}, {released}, {secs}, {kbs},"{creado}", "{folder}", "{archivo}", "{tipo}", {bitrate});
                    """)
        except Exception as e:
            print(e)
            print(f'{archivo} con comillas en album')    
            next
    elif '"' not in str(Artist) and '"' not in str(Album) and '"' in str(Title):
        try:
            engine.execute(f"""
                    INSERT INTO tag (artist, album, title, Track, released, secs, kbs,creado, folder,archivo, tipo, bitrate)
                    VALUES  ("{Artist}", "{Album}", '{Title}', {Track}, {released}, {secs}, {kbs},"{creado}", "{folder}", "{archivo}", "{tipo}", {bitrate});
                    """)
        except Exception as e:
            print(e)
            print(f'{archivo} con comillas en title')    
            next
    