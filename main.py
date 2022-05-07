import pandas as pd
from justwatch import JustWatch
import streamlit as st

st.set_page_config(layout="centered")
proveedor = ['prv', 'hbm', 'nfx', 'dnp']

peli_key = 'e.g.: house'

st.title('Xpress Streaming Movies')

st.image('./data/menu.JPG')

prov = st.selectbox('Select your provider: Netflix(nfx), Amazon Prime Video(prv), HBOMax(hbm) o Disney+(dnp)', proveedor)
st.write('You selected:', prov)

box = st.text_input('Enter your movie word', peli_key)



just_watch = JustWatch(country='ES', providers = prov)



lista_pelis = just_watch.search_for_item(query=box, content_types=['movie'], providers = [prov], monetization_types=['flatrate'])
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

my_recommendation.sort_values(by=['averageRating'], inplace=True, ascending=False)

st.header('These are my recommendations...')
st.dataframe(my_recommendation['primaryTitle'])

for i in range(len(my_recommendation)):
    st.header(my_recommendation.loc[i, 'primaryTitle'])
    c1, c2, c3, c4 = st.columns((2, 1, 1, 1))
    c1.image('https://images.justwatch.com'+ my_recommendation.loc[i,'poster'].replace('{profile}', '')  + 's592/')
    c2.metric('Year', my_recommendation.loc[i,'original_release_year'])
    c3.metric('IMDB Rating', my_recommendation.loc[i,'averageRating'])
    c4.metric('Age Certification', my_recommendation.loc[i,'age_certification'])
    


    st.write(my_recommendation.loc[i,'short_description'])



#just_watch = JustWatch(country='ES')