'''
Author: Bappy Ahmed
Email: entbappy73@gmail.com
Date: 2021-Nov-15
'''

import pickle
import streamlit as st
import requests

def logout():
    st.session_state["authenticated"] = False
    st.switch_page("login.py")
    
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.warning("You are not logged in. Redirecting to login page...")
    st.switch_page("login.py") 

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_link = []
    for i in distances[1:7]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_link.append(movies.iloc[i[0]].movie_link)
    return recommended_movie_names,recommended_movie_posters,recommended_movie_link

# Set background color
st.markdown("""
    <style>
    body {
        background-color: #1E1E1E;
        color: white;
    }
    .header-section {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #333;
        padding: 10px;
        border-radius: 10px;
    }
    .header-section a {
        color: white;
        text-decoration: none;
        margin: 0 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Add navigation bar
st.markdown("""
    <div class='header-section'>
        <h2>CineMatch</h2>
        <button onclick="window.location.href='login.py'">Logout</button>
    </div>
""", unsafe_allow_html=True)

st.header('Movie Recommender System Using Machine Learning')
movies = pickle.load(open(r"C:\CDAC PROJECT FINAL\artifacts\movies.pkl",'rb'))
similarity = pickle.load(open(r"C:\CDAC PROJECT FINAL\artifacts\similarity.pkl",'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendations'):
    recommended_movie_names,recommended_movie_posters,recommended_movie_link = recommend(selected_movie)
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    

    with col1:
        st.text(selected_movie)
        movie1_index = movies[movies['title'] == selected_movie ].index[0]
        movie1_id = movies.iloc[movie1_index].movie_id
        movie1_poster = fetch_poster(movie1_id)
        movie1_link = movies.iloc[movie1_index].movie_link
        st.markdown(f"[![selected_movie]({movie1_poster})]({movie1_link})", unsafe_allow_html=True)

    with col2:
        st.text(recommended_movie_names[1])
        st.markdown(f"[![{recommended_movie_names[1]}]({recommended_movie_posters[1]})]({recommended_movie_link[1]})", unsafe_allow_html=True)

    with col3:
        st.text(recommended_movie_names[2])
        st.markdown(f"[![{recommended_movie_names[2]}]({recommended_movie_posters[2]})]({recommended_movie_link[2]})", unsafe_allow_html=True)

    with col4:
        st.text(recommended_movie_names[3])
        st.markdown(f"[![{recommended_movie_names[3]}]({recommended_movie_posters[3]})]({recommended_movie_link[3]})", unsafe_allow_html=True)

    with col5:
        st.text(recommended_movie_names[4])
        st.markdown(f"[![{recommended_movie_names[4]}]({recommended_movie_posters[4]})]({recommended_movie_link[4]})", unsafe_allow_html=True)

    with col6:
        st.text(recommended_movie_names[5])
        st.markdown(f"[![{recommended_movie_names[5]}]({recommended_movie_posters[5]})]({recommended_movie_link[5]})", unsafe_allow_html=True)

if st.button("Logout"):
    logout()