# ih_datamadpt1121_final_project

![menu](https://user-images.githubusercontent.com/91491555/167191151-4f2f2ca3-3319-4a35-8997-9964894bd313.jpg)

# :clapper: **Xpress Streaming Movies**
The concept of this project is to create an app to quickly choose quality movies from main streaming services in Spain, instead of wasting time through infinite providers menus.


# :mortar_board: **IMDb Dataset**
The source to select quality movies are [IMDb datasets](https://www.imdb.com/interfaces/). 
The datasets used are *title.basics.tsv.gz* and *title.ratings.tsv.gz*.
The datastes are merged and then reduced to movies with average rating from 7.0 to 10 with at least 25000 votes, which results in 2551 recommended movies


## :vhs: **Unofficial JustWatch API**
[Unofficial Justwatch API](https://github.com/dawoudt/JustWatchAPI) is used to check how many recommended movies are present in main streaming providers catalogues   and some movie details.


## :point_up_2: **Streamlit App**
The final result is [here](https://share.streamlit.io/dariodpr/ih_datamadpt1121_final_project/main/main.py)



# :computer: **Stack**
- Python
- pandas
- JustWatch
- Streamlit

# :sweat_smile: **To do**
- Add a message when the input word return no result
- Additional criteria for quality movies (e.g.: RottenTomatoes, Awards...)
- Improve the App visual design
- Clean up the code
