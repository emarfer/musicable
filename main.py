import streamlit as st
import pandas as pd
import requests as req
from streamlit_lottie import st_lottie
#create music playlists based in predictions
from src_st import databases, lastfmapi, kukismo
import os
import random

keylast = os.getenv("keylast")

st.set_page_config(page_title='Musiquismos',
                  # page_icon=":tada:",
                   layout="wide", initial_sidebar_state="expanded",
                   menu_items=None)

# CSS to inject contained in a string
hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

        
with st.sidebar:
  
    kukismo.laod_lottie_ima('https://assets9.lottiefiles.com/private_files/lf30_fjln45y5.json','a')
    st.sidebar.write(':copyright: Powered by [Ester Sinaxe](http://estersinatxe.blogspot.com/2015/12/su-mente-rota.html/)')
    kukismo.laod_lottie_ima('https://assets5.lottiefiles.com/packages/lf20_rcsjdi1p.json','b')

with st.container():
    st.title('Musiquismos :musical_note:')
    st.write("Soy Ester Sinatxe y me encanta el análisis de datos y la música")
    st.write("[Last.Fm Profile](http://www.lastfm.es/user/sinatxester)")

with st.container():
    iz_col, de_col = st.columns(2)
    with iz_col:
        st.write('Vengo a crear listas de reproducción')
    with de_col:
        kukismo.laod_lottie_ima("https://assets9.lottiefiles.com/packages/lf20_vixkj2dq.json",'c')

# databases.short_long_term()        
#now playing

lastfmapi.user_info_complet('jesteruki')
lastfmapi.user_info_complet('sinatxester')
st.markdown("""---""")

num = random.randint(0, 10)
lastfmapi.recent_tracks('sinatxester',str(num))

lastfmapi.tienescuenta(str(num+1))