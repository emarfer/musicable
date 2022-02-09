import os
import pandas as pd
import requests
import time

def df_fromtracks(tracks):
    '''
    recibe una lista de diccionarios con los datos de los últimos scrobbles de un usuario en lastfm
    devuelve un dataframe con los datos que nos interesan
    '''
    lista_dic = []
    for t in tracks:
        dic_bas = {}
        dic_bas['uts'] = t['date']['uts']
        dic_bas['artist'] = t['artist']['#text']
        dic_bas['artist_mbid'] = t['artist']['mbid']
        dic_bas['album'] = t['album']['#text']
        dic_bas['album_mbid'] = t['album']['mbid']
        dic_bas['title'] = t['name']
        dic_bas['track_mbid'] = t['mbid']
        lista_dic.append(dic_bas)
    return pd.DataFrame(lista_dic)


def req_lastfm (l_user,limit,lastuts):
    '''
    recibe parámetros para el endopint de la api de lastfm de rectents tracks de un usuario
    l_user: cadena de texto, nombre del usuario
    limit: integer del 1 a 1000 (preferible 1000) #si sabemos cuántos scrobbles hay y son menos de 1000 podemos poner un número
    lastuts: int el último uts registrado en la base de datos de mysql (fecha en segundos)
    devuelve un diccionario (json) con los últimos tracks
    '''
    uts_num = lastuts + 1 #le sumamos uno al uts recibido para no tenerlo en cuenta porque ya está en la base de datos
    keylast = os.getenv("keylast") #lastf key para la api
    url = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={l_user}&limit={limit}&from={uts_num}&api_key={keylast}&format=json'
    req = requests.get(url).json()
    if req['recenttracks']['@attr']['totalPages'] == '0':
        if len(req['recenttracks']['track']) == 0:

            return 'No hay nuevos scrobbles'
        elif '@attr' in req['recenttracks']['track'].keys():
            art_play = req['recenttracks']['track']['artist']['#text']
            tit_play = req['recenttracks']['track']['name']
            print(f'Now playing: {art_play.capitalize()} - {tit_play.capitalize()}')
            time.sleep(1)
            return 'No hay nuevos scrobbles'
        else:

            return 'No hay nuevos scrobbles'
    
    elif req['recenttracks']['@attr']['totalPages'] == '1':
        if '@attr' in req['recenttracks']['track'][0].keys():
            art_play = req['recenttracks']['track'][0]['artist']['#text']
            tit_play = req['recenttracks']['track'][0]['name']
            print(f'Now playing: {art_play.capitalize()} - {tit_play.capitalize()}')
            time.sleep(1)
            return df_fromtracks(req['recenttracks']['track'][1:])
        else:
            tracks = req['recenttracks']['track']            
            return df_fromtracks(tracks)
    else:
        lista_lista = []
        pages = int(req['recenttracks']['@attr']['totalPages'])
        if '@attr' in req['recenttracks']['track'][0].keys():
            art_play = req['recenttracks']['track'][0]['artist']['#text']
            tit_play = req['recenttracks']['track'][0]['name']
            print(f'Now playing: {art_play.capitalize()} - {tit_play.capitalize()}')
            time.sleep(1)
            for i in range(1,pages+1):
                page = i
                url_p = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={l_user}&limit={limit}&from={uts_num}&page={page}&api_key={keylast}&format=json'
                rq_p = requests.get(url_p).json()['recenttracks']['track']
                lista_lista.append(rq_p)
            tracks = [l for lista in lista_lista for l in lista]
            for t in tracks:
                if 'date' not in t.keys():
                    tracks.remove(t)
            return df_fromtracks(tracks)
        else:
        
            for i in range(1,pages+1):
                page = i
                url_p = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={l_user}&limit={limit}&from={uts_num}&page={page}&api_key={keylast}&format=json'
                rq_p = requests.get(url_p).json()['recenttracks']['track']
                lista_lista.append(rq_p)
            tracks = [l for lista in lista_lista for l in lista]
        
            return df_fromtracks(tracks) #llamamos a la función df_fromtracks
        
def tot_scro(l_user):
    '''
    recibe un nombre de usuario de lastfm
    llama a la api de lastfm con el endpoint de rencentracks para recibir todos los scrobbles de este usuario en lastfm
    devuelve un dataframe con todos los tracks
    '''
    keylast = os.getenv("keylast")
    url = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={l_user}&limit=1000&api_key={keylast}&format=json'
    req = requests.get(url).json()['recenttracks']
    pages = int(req['@attr']['totalPages'])
    print(f'recovering {pages} pages')
    listas = []

    for i in range(1,pages+1):
        page = i
        url_t = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={l_user}&limit=1000&page={page}&api_key={keylast}&format=json'
        req_t = requests.get(url_t).json()['recenttracks']['track']
        listas.append(req_t)
        if i%5==0:
            print(f'pag {i} done')
    tracks = [l for lista in listas for l in lista]
    for t in tracks:
        if 'date' not in t.keys():
            tracks.remove(t)
    return df_fromtracks(tracks)