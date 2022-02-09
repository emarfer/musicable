import os
from IPython.display import display
import pandas as pd
import time

import src.apilast as als
import src.sqltools as sqt
import src.cleansing as cls



keylast = os.getenv("keylast")
l_user = input('enter lastfm user: ')
if l_user.lower() != 'sinatxester':
    print(f"has escrito '{l_user.upper()}', seguro que querías poner 'SINATXESTER', vamos a runear esto como si lo hubieras escrito bien")
    l_user = 'sinatxester'
elif l_user.lower() == 'sinatxester':
    print('muy bien, aprendiste a escribir')
time.sleep(2)
limit = 1000
lastuts = sqt.maxuts()

dating = cls.utslocal(lastuts)

print(f'recovering scrobbles since {dating}')
time.sleep(2)

recenttracks = als.req_lastfm (l_user,limit,lastuts)

if type(recenttracks) == pd.DataFrame:
    print(f'ready to insert {len(recenttracks)} new tracks')
else:
    print(recenttracks)
time.sleep(2)


if type(recenttracks) == pd.DataFrame:
    for i,r in recenttracks.iterrows():
        sqt.insert_data(r.uts, r.artist, r.artist_mbid, r.album, r.album_mbid, r.title, r.track_mbid)

    insertadas = sqt.act_scro()
    display(insertadas)

