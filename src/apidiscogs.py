import pandas as pd
import requests
import os
import numpy as np

def generosdiscog(artista,album,id_alb):
    '''
    recibe el nombre de un artista, el album y el id_alb(base de datos mysal)
    llama a la api de discogs 
    devuelve un diccionario con el género según discogs
    '''
    try:
        tokendis = os.getenv("discog")
        lista = []
        # dicc = {}
        url = f'https://api.discogs.com/database/search?artist={artista}&release_title={album}&token={tokendis}'
        req = requests.get(url).json()
        if req['results'] == []:
            dicc = {'id_alb':id_alb,'gen':np.nan,'genres':np.nan,'subgenres':np.nan}


        else:
            dicc = {'id_alb':id_alb,'gen':req['results'][0]['genre'][0],'genres':",".join(req['results'][0]['genre']),'subgenres':",".join(req['results'][0]['style'])}
        
        if id_alb%10==0:
            print(f'{id_alb}:{artista,album} hecho')

        return dicc
    except Exception as e:
        print(f'error: {e}, {req}, id = {id_alb}')
        return {'id_alb':id_alb,'gen':'error','genres':f'{e}','subgenres':'error'}

        #next