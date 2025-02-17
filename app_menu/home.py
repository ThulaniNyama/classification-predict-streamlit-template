#streamlit dependencies
import streamlit as st
from nlppreprocess import NLP
nlp = NLP()
from PIL import Image

# @st.cache

# """Climate Belief Classifier App"""
def home_menu():
    st.title('Climate Belief Classifier App \U0001F4E1')
    image = Image.open('./resources/imgs/tweet_birds1.png')
    st.image(image, caption='Do you believe in man-made climate change?', use_column_width=True)
