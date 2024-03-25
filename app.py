import streamlit as st

st.title("Hello World :D")
fav_movie = st.text_input("favorite movie?")

if fav_movie  == "Dune":
    st.balloons()
st.text(fav_movie)
