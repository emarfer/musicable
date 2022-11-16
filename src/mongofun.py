from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
import requests
import time

keylast = os.getenv("keylast")
client = MongoClient("localhost:27017")
lastusers = client.get_database("lastusers")

def utsmongo(colecion):
    '''
    recibe un colección de una base de datos en mongo (usuario específico en lastusers)
    devuelve el mayor uts de la colección.
    '''
    numerito = 0
    for ut in colecion.distinct('date.uts'):
        if int(ut)>numerito:
            numerito = int(ut)
    return numerito

def mongouser(lastuser):
    if lastuser.lower() not in lastusers.list_collection_names():
        lastusers.create_collection(lastuser.lower())
        coluser = lastusers.get_collection(f"{lastuser.lower()}")

        url = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={lastuser}&limit=1000&api_key={keylast}&format=json'
        req = requests.get(url).json()['recenttracks']
        scrobs = req['@attr']['total']
        pages = int(req['@attr']['totalPages'])
        print(f'recovering {scrobs} scrobbles in {pages} pages')


        for i in range(1,pages+1):
            page = i
            url_t = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={lastuser}&limit=1000&page={page}&api_key={keylast}&format=json'
            req_t = requests.get(url_t).json()['recenttracks']['track']
            for r in req_t:
                if '@attr' not in r.keys():
                    coluser.insert_one(r)
                elif '@attr' in r.keys() and i ==1:
                    art_play = r['artist']['#text']
                    tit_play = r['name']
                    print (f'Now playing: {art_play.capitalize()} - {tit_play.capitalize()}')

            if i%5==0:
                print(f'pag {i} done')
            elif i == pages:
                print('all done, bitches')
    else:
       
        coluser = lastusers.get_collection(f"{lastuser.lower()}")
        uts_num = utsmongo(coluser) + 1
        url = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={lastuser}&limit=1000&from={uts_num}&api_key={keylast}&format=json'
        req = requests.get(url).json()['recenttracks']

         
        if req['@attr']['totalPages'] == '0':
            if len(req['track']) == 0:            
                print('no hay nada que insertar')
            
            else:
                if '@attr' in req['track'].keys():                    
                    art_play = req['track']['artist']['#text']
                    tit_play = req['track']['name']
                    print('nada que insertar')
                    print( f'Now playing: {art_play.capitalize()} - {tit_play.capitalize()}')


        elif req['@attr']['totalPages'] != '0':   
            scrobs = req['@attr']['total']
            pages = int(req['@attr']['totalPages'])
            print(f'recovering {scrobs} scrobbles in {pages} pages')

            for i in range(1,pages+1):
                page = i
                url = f'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={lastuser}&limit=1000&from={uts_num}&page={page}&api_key={keylast}&format=json'
                req = requests.get(url).json()['recenttracks']


                for r in req['track']:
                    if '@attr' in r.keys() and i ==1:
                        art_play = r['artist']['#text']
                        tit_play = r['name']
                        print (f'Now playing: {art_play.capitalize()} - {tit_play.capitalize()}')
                        
                    elif '@attr' not in r.keys():
                        coluser.insert_one(r)
                if i%5==0:
                    print(f'pag {i} done')
                elif i == pages:
                    print('all done, bitches')
        else:
            print('no insertamos nada porque nada hay que insertar') #este else sobra solo hay dos posibilidades =0 o != 0

   