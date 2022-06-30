#streamlit dependencies
from matplotlib.pyplot import title
from nltk.corpus.reader.pl196x import ANA
import streamlit as st
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.tokenize import TreebankWordTokenizer
tbt = TreebankWordTokenizer()
import pandas as pd
from nlppreprocess import NLP
nlp = NLP()
from PIL import Image

def analyzer():
        df_train = pd.read_csv('https://raw.githubusercontent.com/TEAM-CW3/classification-predict-streamlit-data/main/train.csv')
        st.info('The following are some of the charts that we have created from the raw data. Some diagrams might be small, feel free to click on the maximize button on top right of the chart to see it properly.')

        # Number of Messages Per Sentiment

        all_analyzers = ['Choose Analyzer','Line & Bar Graphs', 'Pie Chart', 'Word Cloud', 'Missing Values']
        analyzer = st.selectbox('Select Analyzer', all_analyzers)

        #delete above

        # Inserting our visuals for analysing data
        if analyzer == 'Line & Bar Graphs':
                #import functions.line_and_bar as graph
                #graph.plot_line_and_bar()
                image = Image.open('resources/imgs/Bargraph.png')
                st.image(image)
                st.info('By observing the graphs you can see that the average length for all opinions is relatively the same,\nthis may be due to that every tweet has a word limit. However when we comparing the density between negative and positive sentiments there is noticable difference.')

        elif analyzer == 'Pie Chart':
                st.write('Distribution of the sentiments')
                import functions.pie_chart as pie
                pie.plot_pie_chart()
                st.info('After observing our Pie-Chart above you can see than more than half of the sample tweets come from positive sentiments, tweets from sentiment that do not believe in man-made climate change are the least and News are the second most popular.')
        

        elif analyzer == 'Word Cloud':
                #import functions.plot_word_cloud as pwd
                #pwd.gen_wordcloud(title)
                image = Image.open('resources/imgs/word_cloud.png')
                st.image(image, use_column_width=True)

        elif analyzer == 'Missing Values':
                #import functions.missing_values as missing
                #missing.missing_vals()
                image = Image.open('resources/imgs/missingwords.png')
                st.image(image)