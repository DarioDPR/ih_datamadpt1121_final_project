import pandas as pd
from justwatch import JustWatch
import streamlit as st

proveedor = ['prv' , 'hbm', 'dsn', 'nfx']

peli_key = 'Ejemplo: house'

st.title('Your recommended movie')

prov = st.selectbox('Seleccione un proveedor', proveedor)
st.write('You selected:', prov)

box = st.text_input('Enter your movie word', peli_key)



just_watch = JustWatch(country='ES', providers=prov)



lista_pelis = just_watch.search_for_item(query=box, content_types=['movie'])
total_list = len(lista_pelis['items'])

total_pelis = []
for item in range(total_list):
    total_pelis.append(lista_pelis['items'][item]['id'])

extra_info = []
for e in range(len(total_pelis)):
    try:
        peli = just_watch.get_title(title_id=total_pelis[e])
        extra_info.append(peli)
    except:
        extra_info.append('/-----------------------------no info-----------------------------------/')

table = pd.json_normalize(extra_info)

print('esta es la primera tabla', table)

table_col = table.drop(['backdrops', 'external_ids', 'genre_ids', 'permanent_audiences', 
                            'localized_release_date', 'upcoming', 'poster_blur_hash', 
                            'full_paths.MOVIE_DETAIL_OVERVIEW', 'offers', 'clips', 'scoring','credits'], axis = 1)

print('Imprime la tabla 2:', table_col)

table_col.rename(columns = {'original_title':'originalTitle'}, inplace = True)

print('Imprime la tabla 3:', table_col)

#st.table(table_col)
recommend = pd.read_csv('./Data/recommend.csv')
my_recommendation = pd.merge(recommend, table_col, how='inner', on=['originalTitle'], left_on=None, right_on=None,
left_index=False, right_index=False, sort=True)

st.dataframe(my_recommendation)

for i in range(len(my_recommendation)):
    st.image('https://images.justwatch.com'+ my_recommendation.loc[i,'poster'].replace('{profile}', '')  + 's592/')



#just_watch = JustWatch(country='ES')