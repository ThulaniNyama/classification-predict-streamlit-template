"""
    Simple Streamlit webserver application for serving developed classification
	models.
    Author: Explore Data Science Academy.
    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------
    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.
	For further help with the Streamlit framework, see:
	https://docs.streamlit.io/en/latest/
"""
import streamlit as st
# from sympy import im
import app_menu.home as am
import app_menu.about_tweet_classifier_app as atca
import app_menu.data_profession as dp
import app_menu.classify_tweets as ct
import app_menu.analyze_tweets as at

def main():
    with st.sidebar:
        app_menu_items = st.radio("", ('🏠 Home', '📰 About', '📈 Analyze', '🐦 Classify Tweets', '💻 CW3 Data Professionals'))

    if app_menu_items == '🏠 Home':
        am.home_menu()
    elif app_menu_items == '📰 About':
        atca.about()
    elif app_menu_items == '📈 Analyze':
        at.analyzer()
    elif app_menu_items == '🐦 Classify Tweets':
        ct.classifier()
    elif app_menu_items == '💻 CW3 Data Professionals':
        dp.data_professionals()
    
if __name__ == '__main__':
	main()
