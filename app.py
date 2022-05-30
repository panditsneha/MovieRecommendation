import pickle
import pandas as pd
import requests
import streamlit as st



st.title("Movie Recommender System")

# loading the saved dictionary and converting it to the dataframe
movie_list = pickle.load(open('movies_dict.pkl','rb'))
df = pd.DataFrame(movie_list)

# loading the saved similarity pkl file
m_similarity = pickle.load(open('similarity.pkl','rb'))

selected_movies = st.selectbox('Select a movie', df['title'].values)

def recommend(movie):
    movie_index = df[df['title'] == movie].index[0]
    distance = m_similarity[movie_index]
    # sorting on the basis of vectors of movie
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:11]
    # enumerator returns an object that contains a counter as a key for each value within an object
    movie_lst = []
    movie_lst_posters = []
    for i in movie_list:
        movie_id = df.iloc[i[0]].id
        movie_lst.append(df.iloc[i[0]].title)
        movie_lst_posters.append(fetch_poster(movie_id))
    return movie_lst, movie_lst_posters

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

if st.button('Recommend'):
     names, posters = recommend(selected_movies)
     col1, col2, col3, col4 = st.columns(4)
     with col1:
         st.text(names[0])
         st.image(posters[0])
     with col2:
         st.text(names[1])
         st.image(posters[1])
     with col3:
         st.text(names[2])
         st.image(posters[2])
     with col4:
         st.text(names[3])
         st.image(posters[3])

     c1, c2, c3, c4 = st.columns(4)
     with c1:
         st.text(names[4])
         st.image(posters[4])
     with c2:
         st.text(names[5])
         st.image(posters[5])
     with c3:
         st.text(names[6])
         st.image(posters[6])
     with c4:
         st.text(names[7])
         st.image(posters[7])


