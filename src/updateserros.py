import os
import sqlalchemy as alch
import dotenv

passw = os.getenv("mysql")
dbName = "musicablecero"
connectionData = f"mysql+pymysql://root:{passw}@localhost/{dbName}"
engine = alch.create_engine(connectionData)


def actual_error():


    engine.execute("update scrobbling set artist = 'Juan Luis Guerra y 4.40' where album = 'Bachata Rosa' and artist = 'Juan Luis Guerra';")
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