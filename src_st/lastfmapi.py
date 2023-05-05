import requests
import pandas as pd
import os
import streamlit as st
from PIL import Image
from io import BytesIO
from datetime  import datetime
from streamlit_lottie import st_lottie
from src_st.kukismo import laod_lottie_ima

keylast = os.getenv("keylast")


def dataframe_count(r):
    keys_count = ['playcount','artist_count','track_count','album_count']
    lista = []
    for k in keys_count:
        dic = {}
        dic['Count'] = k.split('_')[0]
        dic['#'] = int(r[k])
        lista.append(dic)
    return pd.DataFrame(lista)[['Count','#']]

def user_info_complet(user):
    st.markdown("""---""")
    req = requests.get(f'http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user={user}&api_key={keylast}&format=json').json()['user']
    url_image = req['image'][2]['#text']
    unixtime = int(req['registered']['unixtime'].strip())
    fecha = datetime.utcfromtimestamp(unixtime).strftime('%Y-%m-%d')
    
    with st.container():
        iz_col, cent_col, de_col = st.columns(3)
        
        with iz_col:
            st.image(url_image)
        with cent_col:
            st.header(f'[@{user}](http://www.lastfm.es/user/{user})')
            st.write(f'En Last FM desde {fecha}')
            if user == 'jesteruki':
                st.write('No se actualiza desde 2015')
        with de_col:
            st.dataframe(dataframe_count(req))
            
def info_song(r,i):
    dic = {}
    dic['#'] = i
    dic['temazo'] = r['name']
    dic['artista'] = r['artist']['#text']
    dic['album'] = r['album']['#text']
    return dic

def recent_tracks(user,k):
    url = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={user}&api_key={keylast}&limit=10&format=json'
    req = requests.get(url).json()['recenttracks']['track']
    if '@attr' in req[0].keys():
        # now playing
        url_imagen = req[0]['image'][3]['#text']
        dic = info_song(req[0],0)
        st.title('Now playing, bitches...')
        with st.container():
            
            iz_col, cent_col, de_col= st.columns(3)
            with iz_col:
                laod_lottie_ima('https://assets9.lottiefiles.com/packages/lf20_lvzxe6un.json',k)
            with cent_col:
                temazo = dic['temazo']
                artista = dic['artista']
                
                
                st.subheader(f"{temazo}")
                st.subheader(f"(by {artista})")
            with de_col:
                st.image(url_imagen)
                
        st.markdown('''---''')
        req = req[1:]
    st.subheader('Últimas 10 canciones reproduccidas')
    
    lista = []
    i = 1
    for r in req:
        lista.append(info_song(r,i))
        i +=1
    st.dataframe(pd.DataFrame(lista))
    
def tienescuenta(k):
    st.title('Quieres ver tus cosicas en esta kukiweb y lo sabes')
    cuenta = st.radio(
    "Tienes cuenta de Last FM",
    ('No','Sí'))
    if cuenta == 'No':
        st.stop()
    elif cuenta == 'Sí':
        usercillo = st.text_input('¿Cuál es tu usuario?')
        if usercillo == '':
            st.stop()
        else:
            user_info_complet(usercillo)
            recent_tracks(usercillo,k)

        