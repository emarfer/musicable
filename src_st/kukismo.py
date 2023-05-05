import requests
from streamlit_lottie import st_lottie


def laod_lottie_ima(url,k):
    r = requests.get(url)
    if r.status_code != 200:
        None
    ima_json = r.json()
    return st_lottie(ima_json,key=k)