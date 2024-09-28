import pickle
import streamlit as st
import requests

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
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

st.markdown(
    """
    <style>
    .title {
        font-size: 50px;
        font-weight: 700;
        text-align: center;
        color: #ffffff;
        background: #4CAF50;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
        margin-bottom: 30px;
        letter-spacing: 1px;
    }
    </style>
    <div class="title">
        Welcome to Movie Recommender
    </div>
    """,
    unsafe_allow_html=True
)


movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values


st.markdown(
    """
    <style>
    .selectbox-container {
        background-color: #f0f0f0;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
    }
    .selectbox-label {
        font-size: 20px;
        font-weight: bold;
        color: #333333;
        margin-bottom: 8px;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .selectbox-dropdown {
        font-size: 16px;
        color: #333333;
        background-color: #ffffff;
        border: 1px solid #ddd;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.05);
    }
    </style>
    <div class="selectbox-container">
        <div class="selectbox-label">Type or Select a Movie from the Dropdown</div>
    </div>
    """,
    unsafe_allow_html=True
)


selected_movie = st.selectbox(
    "",
    movie_list
)

# Display the selected movie
st.write(f"You selected: {selected_movie}")


if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown('<div class="movie-column">', unsafe_allow_html=True)
        st.markdown(f'<p class="movie-title">{recommended_movie_names[0]}</p>', unsafe_allow_html=True)
        st.image(recommended_movie_posters[0])
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="movie-column">', unsafe_allow_html=True)
        st.markdown(f'<p class="movie-title">{recommended_movie_names[1]}</p>', unsafe_allow_html=True)
        st.image(recommended_movie_posters[1])
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="movie-column">', unsafe_allow_html=True)
        st.markdown(f'<p class="movie-title">{recommended_movie_names[2]}</p>', unsafe_allow_html=True)
        st.image(recommended_movie_posters[2])
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="movie-column">', unsafe_allow_html=True)
        st.markdown(f'<p class="movie-title">{recommended_movie_names[3]}</p>', unsafe_allow_html=True)
        st.image(recommended_movie_posters[3])
        st.markdown('</div>', unsafe_allow_html=True)

    with col5:
        st.markdown('<div class="movie-column">', unsafe_allow_html=True)
        st.markdown(f'<p class="movie-title">{recommended_movie_names[4]}</p>', unsafe_allow_html=True)
        st.image(recommended_movie_posters[4])
        st.markdown('</div>', unsafe_allow_html=True)



# credit at the bottom right
st.markdown(
    """
    <style>
    .credit {
        position: fixed;
        right: 10px;
        bottom: 10px;
        background-color: rgba(0, 0, 0, 0.7);
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        font-family: Arial, sans-serif;
        font-size: 12px;
    }
    </style>
    <div class="credit">
        © 2024 Project by Piyush Jha
    </div>
    """,
    unsafe_allow_html=True
)



