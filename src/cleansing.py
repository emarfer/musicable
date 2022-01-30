import datetime

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