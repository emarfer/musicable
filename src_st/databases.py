import pandas as pd
import os
import sqlalchemy as alch
import dotenv
import datetime
import time
from IPython.display import display
import streamlit as st

dotenv.load_dotenv()

passw = os.getenv("mysql")
dbName = "musicablecero"
connectionData = f"mysql+pymysql://root:{passw}@localhost/{dbName}"
engine = alch.create_engine(connectionData)

def short_long_term():

    min_rep = list(engine.execute('select min(rep) from prediction'))[0][0]
    # print(min_rep)
    st.write(f'The min reps are {min_rep}')
    # min_rep_var = int(input('number to substract to min_rep: '))
    min_rep_var = st.text_input('Insert a number')
    if min_rep_var == '':
        st.stop()
    else:
        min_rep_var = int(min_rep_var)
        check_repetitions =  pd.read_sql_query(f'''select id_can, artist, album, title, genero, sexo, rep, veces from prediction
            where veces > 0
        union
        select id_can, artist, album, title, genero, sexo, rep, veces from base_pred
            where id_art in (select id_art from prediction where veces > 0) and veces = 0
                and rep >( {min_rep} - {min_rep_var})
        order by artist, rep desc;'''
        , engine)
        if len(check_repetitions)== 0:
            # print('Todos las reproducciones para el próximo mes son nuevas')
            st.write('Todos las reproducciones para el próximo mes son nuevas')
        else:
            # display(check_repetitions)
            st.dataframe(check_repetitions)
        
    min_rep_longterm = list(engine.execute('select min(rep) from prediction_dos'))[0][0]
    st.write(f'The min reps long term are {min_rep_longterm}')
    # min_rep_longterm_var = int(input('number to substract to min_rep_longterm: '))
    min_rep_longterm_var = st.text_input('Insert a number',key='dos')
    if min_rep_longterm_var == '':
        st.stop()
    else:
        min_rep_longterm_var = int(min_rep_longterm_var)


        check_rep_longterm = pd.read_sql_query(f'''
        select id_can, artist, album, title, genero, sexo, rep, veces,prec from prediction_dos
            where veces > 0 or prec is True
        UNION
        select id_can, artist, album, title, genero, sexo, rep, veces,prec  from base_pred_dos
            where id_art in (select id_art from prediction_dos where veces > 0 or prec is true )
                and veces = 0
                and prec is false
                and rep >= ({min_rep_longterm} - {min_rep_longterm_var})
        order by artist, rep desc, prec desc; 
                                            ''',engine)
        if len(check_rep_longterm) == 0:
            print("Todas las reproducciones a long term son nuevas")
            st.write("Todas las reproducciones a long term son nuevas")
        else:
            # display(check_rep_longterm)
            st.dataframe(check_rep_longterm)
            
    prediction_df = pd.read_sql_query('select * from prediction',engine)
    long_term_prediction_df = pd.read_sql_query('select * from prediction_dos',engine)
    st.subheader('Pediction')
    st.dataframe(prediction_df)
    st.subheader('Prediction Long term')
    st.dataframe(long_term_prediction_df)
    
    # possiblities not in list
    # prediction
    
    st.subheader('possiblities prediction')
    pos_pred = pd.read_sql_query(f'''
        select id_can, artist, album, title, genero, sexo, rep, veces from base_pred 
            where id_art not in (Select id_art from prediction
                                -- where veces = 0
                                -- and rep >= @minrep+2
                                                                )
                and rep >=  ({min_rep} - {min_rep_var})
                -- and sexo = 'fem'
                and veces = 0
            --  and id_can not in (select id_can from prediction_dos)           
                                 ''',engine)
    st.dataframe(pos_pred)
    
    st.subheader('possibilities long term')
    pos_long_term = pd.read_sql_query(f'''
        select id_can, artist, album, title, genero, sexo, rep, veces, prec from base_pred_dos 
            where id_art not in (Select id_art from prediction_dos 
                            -- where veces = 0
                                )
                and prec is false
                -- and id_can not in (select id_can from scrobbling where date(fechahora) > '2023-03-20')
                and rep >= ({min_rep_longterm} -2)
            -- and sexo = 'fem'
            and veces = 0
             ''',engine)
    st.dataframe(pos_long_term)