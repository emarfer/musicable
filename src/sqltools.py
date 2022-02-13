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


def car_esp(palabrita):
    '''
    recibe un elemento, si no es string lo convierte
    comprueba si en la cadena de texto existen una serie de caracteres
    si estos caracteres están en la cadena los reemplaza
    devuelve la palabrita
    '''
    palabrita = str(palabrita)
    dicc = {'\\':'\\\\',"'":"\\'",'"':'\\"'}
    if "'" in palabrita or '"' in palabrita  or '\\' in palabrita :
        for k,v in dicc.items():
            palabrita = palabrita.replace(k,v)
        return palabrita
    else:
        return palabrita

def insert_data(uts, artist, artist_mbid, album, album_mbid, title, track_mbid):
    '''
    recibe los datos del datframe creado con la api de ultimos tracks de lastfm
    inserta los datos en la tabla scrobbling de mysql
    '''
    fechahora = utslocal(uts)
    artista = car_esp(artist)
    disco = car_esp(album)
    titu = car_esp(title)

    try:
        engine.execute(f"""
                INSERT INTO scrobbling (uts, artist, artist_mbid, album, album_mbid, title, track_mbid, fechahora)
                VALUES ({uts}, '{artista}', '{artist_mbid}', '{disco}', '{album_mbid}', '{titu}','{track_mbid}','{fechahora}');
                """)
    except Exception as e:
        print(f'{uts}: {title} no insertado por {e}')  


def insert_newalb(Artist, Album, Title, Track, released, secs, kbs, creado, ruta, archivo,tipo, bitrate):
    
    '''
    recibe los datos del datframe con los tags de un nuevo album
    inserta los datos en la tabla tag del la base de datos musicablecero
    '''
    folder = car_esp(ruta)
    art_ = car_esp(Artist)
    alb_ = car_esp(Album)
    tit_ = car_esp(Title)
    arc_ = car_esp(archivo)
    
    try:
        engine.execute(f"""
                INSERT INTO tag (artist, album, title, Track, released, secs, kbs,creado, folder,archivo, tipo, bitrate)
                VALUES  ("{art_}", "{alb_}", "{tit_}", {Track}, {released}, {secs}, {kbs},"{creado}", "{folder}", "{arc_}", "{tipo}", {bitrate});
                """)
    except Exception as e:
        print(f'{archivo} ha dado error: {e}')    
        


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

def checkalb(alb_,idart):
    if len(list(engine.execute(f"select * from albums where album = '{alb_}', and id_art = {idart}"))) == 0:
        return False #no existe
    else:
        return True #existe

def get_id_art(art_):
    return list(engine.execute(f"select id_art from artistas where artist = '{art_}'"))[0][0]

def get_id_alb(alb_):
    return list(engine.execute(f"select id_alb from albums where album = '{alb_}'"))[0][0]

def get_id_pais(pais):
    #recibe el nombre de un pais, checkea si está en la base de datos (corecctamente escrito)
    #devuelve el id_del pais , si existe.
    if len(list(engine.execute(f"select id_p from paises where nombre = '{pais}'"))) == 0:
        print('este pais no existe, checkea que esté bien escrito... estos son los paises disponibles:')
        tabla = pd.read_sql_query(f'''
        SELECT nombre from paises
        ''', engine)
        print(list(tabla.nombre.unique()))
        print("si no lo tienes claro, o te da pereza googlear puedes introudcir = 'indet'")
        nuevo_pais = input('vuelve a introducir el nombre del pais: \r')
        return get_id_pais(nuevo_pais)
    else:
        return list(engine.execute(f"select id_p from paises where nombre = '{pais}'"))[0][0]

def insert_newart(art_,sex_,gen_,band_,pais_):
    #recibe unos parámetros de información sobre un artista/banda musical 
    #inserta estos datos en mysql
    artist = car_esp(art_)
    sexo = car_esp(sex_) #fem, band, indet
    genero = car_esp(gen_) #genero musical
    banda = car_esp(band_) 
    pais = car_esp(pais_)
    id_p = get_id_pais(pais)
    
    
    try:
        engine.execute(f'''
        INSERT INTO artistas (artist,sexo,genero,band,id_p) VALUES ('{artist}','{sexo}','{genero}','{banda}',{id_p})
        ''')
        return f'{artist} insertado'
    
    except Exception as e:
        return f'ya la estás liadndo, mira que error has cometido: {e}'
    