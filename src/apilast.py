import os
import pandas as pd
import requests

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
    if requests.get(url).json()['recenttracks']['@attr']['totalPages'] == '1':
        tracks = requests.get(url).json()['recenttracks']['track']
    else:
        pages = int(requests.get(url).json()['recenttracks']['@attr']['totalPages'])
        lista_lista = []
        for i in range(1,pages+1):
            page = i
            url_p = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={l_user}&limit={limit}&from={uts_num}&page={page}&api_key={keylast}&format=json'
            rq_p = requests.get(url_p).json()['recenttracks']['track']
            lista_lista.append(rq_p)
        tracks = [l for lista in lista_lista for l in lista]
    
    return df_fromtracks(tracks) #llamamos a la función df_fromtracks