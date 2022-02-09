import pandas as pd
import os
import sqlalchemy as alch
import dotenv
import datetime
import time

dotenv.load_dotenv()

passw = os.getenv("mysql")
dbName = "musicablecero"
connectionData = f"mysql+pymysql://root:{passw}@localhost/{dbName}"
engine = alch.create_engine(connectionData)




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
    fechahora = utslocal(uts)
    

    if '"' not in str(artist) and '"' not in str(album) and '"' not in str(title):
        try:
            engine.execute(f"""
                    INSERT INTO scrobbling (uts, artist, artist_mbid, album, album_mbid, title, track_mbid, fechahora)
                    VALUES ({uts}, "{artist}", "{artist_mbid}", "{album}", "{album_mbid}", "{title}","{track_mbid}","{fechahora}");
                    """)
        except:
            print(f'{uts} sin comillas en ningún lugar')    
            next
    elif '"' in str(artist) and '"' not in str(album) and '"' not in str(title):
        try:
            engine.execute(f"""
                    INSERT INTO scrobbling (uts, artist, artist_mbid, album, album_mbid, title, track_mbid, fechahora)
                    VALUES ({uts}, '{artist}', "{artist_mbid}", "{album}", "{album_mbid}", "{title}","{track_mbid}","{fechahora}");
                    """)
        except:
            print(f'{uts} con comillas en artista')    
            next
    elif '"' not in str(artist) and '"' in str(album) and '"' not in str(title):
        try:
            engine.execute(f"""
                    INSERT INTO scrobbling (uts, artist, artist_mbid, album, album_mbid, title, track_mbid, fechahora)
                    VALUES ({uts}, "{artist}", "{artist_mbid}", '{album}', "{album_mbid}", "{title}","{track_mbid}","{fechahora}");
                    """)
        except:
            print(f'{uts} con comillas en album')    
            next
    elif '"' not in str(artist) and '"' not in str(album) and '"' in str(title):
        try:
            engine.execute(f"""
                    INSERT INTO scrobbling (uts, artist, artist_mbid, album, album_mbid, title, track_mbid, fechahora)
                    VALUES ({uts}, "{artist}", "{artist_mbid}", "{album}", "{album_mbid}", '{title}',"{track_mbid}","{fechahora}");
                    """)
        except:
            print(f'{uts} con comillas en title')    
            next
    elif '"' not in str(artist) and '"'  in str(album) and '"' in str(title):
        try:
            engine.execute(f"""
                    INSERT INTO scrobbling (uts, artist, artist_mbid, album, album_mbid, title, track_mbid, fechahora)
                    VALUES ({uts}, "{artist}", "{artist_mbid}", '{album}', "{album_mbid}", '{title}',"{track_mbid}","{fechahora}");
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


def actual_error():


    engine.execute("update scrobbling set artist = 'Juan Luis Guerra y 4.40' where album in('Bachata Rosa','Ojalá Que Llueva Café') and artist = 'Juan Luis Guerra';")
    engine.execute("update scrobbling set artist = 'Robe' where artist = 'Robe.';")
    engine.execute("""
    update scrobbling set title = "Can't Hold Us Down (ft. Lil' Kim)" where artist = 'Christina Aguilera' and title = "Can't Hold Us Down";
    """)
    engine.execute("""
    update scrobbling set title = 'Satisfaction' where title = "(I Can't Get No) Satisfaction" and album = 'Out of Our Heads';
    """)
    engine.execute("update scrobbling set artist = 'Loquillo Y Trogloditas' where artist = 'Loquillo Y Los Trogloditas';")
    engine.execute("update scrobbling set album = '[Desconocido]' where album = '' and artist in ('Rob Thomas','funk2maka','Jordi Estévez','Elena Bugedo','Joaquín Calderón','Zahara','Los Capos de México','Julio Muñoz');")
    engine.execute("update scrobbling set title = 'La Senda Del Tiempo (directo)' where title = 'La Senda Del Tiempo' and album = 'Nos vemos en los bares';")
    engine.execute("update scrobbling set title = 'Shake It Out (Unplugged)' where title = 'Shake It Out (Acoustic)' and album  = 'MTV Unplugged';")
    engine.execute("""
    update scrobbling set title = "You've Got the Love (Fraser T. Smith's Mix)" where title = "You've Got The Love (Fraser T Smith's Mix)" and album = 'Lungs';
    """)
    engine.execute("update scrobbling set title = 'Time After Time (Live)' where title = 'Time After Time (Live) (Live Australia)' and album = 'Live From Australia' and artist = 'Matchbox Twenty';")
    engine.execute("update scrobbling set album = 'Dúos, Tríos Y Otras Perversiones' where album = 'Duos, trios y otras perversiones' and artist = 'Ariel Rot';")
    engine.execute("update scrobbling set title = 'Me Estás Atrapando Otra Vez (Con M-Clan)' where title = 'Me Estás Atrapando Otra Vez' and album = 'Dúos, Tríos Y Otras Perversiones';")
    engine.execute("update scrobbling set title = 'Mi Alma Vuela En Silencio (Rumba)' where title = 'Mi Alma Vuela En Silencio' and artist = 'Rosario La Tremendita';")
    engine.execute("update scrobbling set title = 'We Go Together' where title ='We Go Together (© ¤ @)' and album = 'Grease [Original Soundtrack]';")
    engine.execute("update scrobbling set title = 'Alegrías De La Lole' where title = 'Alegrías De Lole' and artist = 'Lole Y Manuel';")
    engine.execute("update scrobbling set title = 'Oniria E Insomnia' where title = 'Oniria E Insomia' and artist = 'Love of Lesbian';")
    engine.execute("update scrobbling set title = 'Sick & Tired' where title = 'Sick and Tired' and album = 'Anastacia';")
    engine.execute("update scrobbling set title = '7-11' where title = '7/11' and album = 'Kamikazes Enamorados';")
    engine.execute("update scrobbling set title = 'Hoy Es El Principio Del Final (Acústica)' where title = 'Hoy Es El Principio Del Final (Versión Acústica)' and album = 'Hacia Lo Salvaje';")
    engine.execute("update scrobbling set title = 'You And I & I (Live)' where title = 'You And I & I (Live) (Live Australia)' and album = 'Live from Australia';")
    engine.execute("""
    update scrobbling set title = "It's Now or Never Loves" where title = "It’s Now or Never Loves" and album = 'I Aubade';
    """)
    engine.execute("update scrobbling set title = 'On the Floor' where title = 'On the Floor (feat. Pitbull)' and album = 'Love?';")
    engine.execute("update scrobbling set title = 'Rock & Roll Suspension' where title = 'Rock And Roll Suspension' and album = 'Spring Session M';")    
    engine.execute("update scrobbling set title = 'Ce Matin là' where title = 'Ce Matin-là' and album = 'Moon Safari';")    
    engine.execute("update scrobbling set artist = 'Anni B Sweet' where artist = 'Anni B. Sweet';")   
    engine.execute("update scrobbling set album = 'Chasing Illusions' where artist = 'Anni B Sweet' and album = '';")     
    engine.execute("update scrobbling set artist = 'NSYNC' where artist = '*NSYNC';")


    
# *NSYNC


def act_scro():
    last_uts = list(engine.execute(f'select max(uts) from scrobbling where id_can is not null;'))[0][0]

    time.sleep(2)
    cuenta = list(engine.execute(f'''
    select count(uts) from scrobbling where concat(artist, album, title) not in (select completo from total)
    '''))[0][0]
    if cuenta == 0:
        engine.execute(f'''
            update scrobbling sc join total tt on tt.completo = concat(sc.artist,sc.album,sc.title)
            set sc.id_Can = tt.id_Can
            where sc.id_Can is null;
            ''')
        filas = list(engine.execute(f'select count(*) as  "Filas Actualizadas"from scrobbling where uts > {last_uts};'))[0][0]
        print(f'Filas actualizadas: {filas}')
        insertades =  pd.read_sql_query(f'''
            select * from scrobbling where uts > {last_uts};
            
            ''',engine)
        return insertades[['uts','artist','album','title','fechahora']].head(10)
    else:
        print('corrigiendo algunos errores de insertación')
        actual_error()
        cuenta_again = list(engine.execute(f'''
                select count(uts) from scrobbling where concat(artist, album, title) not in (select completo from total)
                '''))[0][0]
        if cuenta_again == 0:
            engine.execute(f'''
                update scrobbling sc join total tt on tt.completo = concat(sc.artist,sc.album,sc.title)
                set sc.id_Can = tt.id_Can
                where sc.id_Can is null;
                ''')
            filas = list(engine.execute(f'select count(*) as  "Filas Actualizadas"from scrobbling where uts > {last_uts};'))[0][0]
            print(f'Filas actualizadas: {filas}')
            insertades =  pd.read_sql_query(f'''
                select * from scrobbling where uts > {last_uts};
                
                ''',engine)
            return insertades[['uts','artist','album','title','fechahora']].head(10)
        else:
            print('los siguientes errores no se han podido corregir')
            print('(no se insertarán ninguno de los nuevos scrobbles hasta corregir erroes, stay tuned)')
                
            errores =  pd.read_sql_query(f'''
                select * from scrobbling where concat(artist, album, title) not in (select completo from total);
                ''',engine)
            
            engine.execute(f'delete from scrobbling where uts > {last_uts}')

            return errores[['uts','artist','album','title','fechahora']]
            


def checkuts(uts_):
    cuenta = list(engine.execute(f"select count(*) from scrobbling where uts = {uts_}"))[0][0]
    if cuenta == 0:
        return False
    else:
        return True

def checkart(art_):
    if len(list(engine.execute(f"select * from artistas where artist = '{art_}'"))) == 0:
        return False #no existe
    else:
        return True #existe

def checkalb(alb_):
    if len(list(engine.execute(f"select * from albums where album = '{alb_}'"))) == 0:
        return False #no existe
    else:
        return True #existe

def get_id_art(art_):
    return list(engine.execute(f"select id_art from artistas where artist = '{art_}'"))[0][0]

def get_id_alb(alb_):
    return list(engine.execute(f"select id_alb from albums where album = '{alb_}'"))[0][0]