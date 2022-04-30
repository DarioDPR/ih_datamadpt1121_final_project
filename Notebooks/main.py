#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from justwatch import JustWatch
#import streamlit as st


# In[2]:


#st.title('Your recommended movie')

proveedor = 'nfx', 'prv'
just_watch = JustWatch(country='ES', providers=[proveedor])
peli_key = 'house'

#box = st.text_input('Enter your movie word', peli_key)

lista_pelis = just_watch.search_for_item(query=peli_key, content_types=['movie'])
total_list = len(lista_pelis['items'])

# In[3]:


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
table_col = table.drop(['backdrops', 'external_ids', 'genre_ids', 'permanent_audiences', 
                            'localized_release_date', 'upcoming', 'poster_blur_hash', 
                            'full_paths.MOVIE_DETAIL_OVERVIEW', 'offers', 'clips', 'scoring','credits'], axis = 1)


table_col = table_col.rename(columns = {'original_title':'originalTitle'}, inplace = True)

print(table_col)

#st.table(table_col)
recommend = pd.read_csv('../Data/recommend.csv')
my_recommendation = pd.merge(recommend, table_col, how='inner', on=['originalTitle'], left_on=None, right_on=None,
left_index=False, right_index=False, sort=True)

#st.dataframe(my_recommendation)

