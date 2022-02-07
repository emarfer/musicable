import os
from IPython.display import display

import src.apilast as als
import src.sqltools as sqt
import src.cleansing as cls


keylast = os.getenv("keylast")
l_user = input('enter lastfm user: ')
limit = 1000
lastuts = sqt.maxuts()

dating = cls.utslocal(lastuts)

print(f'recovering scrobbles since {dating}')

recenttracks = als.req_lastfm (l_user,limit,lastuts)

for i,r in recenttracks.iterrows():
    sqt.insert_data(r.uts, r.artist, r.artist_mbid, r.album, r.album_mbid, r.title, r.track_mbid)

insertadas = sqt.insert_scro()
display(insertadas)