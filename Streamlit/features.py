def by_features():
    
    #libraries
    import pandas as pd
    import numpy as np
    import random
    import streamlit as st
    from PIL import Image

    import warnings
    warnings.filterwarnings('ignore')
    
    import nltk
    from nltk.tokenize import word_tokenize
    from sklearn.feature_extraction.text import CountVectorizer
    
    from sklearn import cluster, datasets
    from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
    from sklearn.cluster import KMeans
    
    # data
    clustered_df = pd.read_csv('clustered_df.csv')
#     clustered_folded = pd.read_csv('clustered_folded.csv')
    
    # Lists of acceptable values
    red_white = ['Red', 'White']
    body = ['Strong','Medium','Weak', 'Very Weak']
    acidity = ['High','Medium','Low']

    
    
    
    
    with st.form("my_form"):
        # Get input values

        red_white = st.radio("Are you looking for a Red or White Wine? ",red_white, key = '5')
        body = st.radio("How do you like the body of your wine? ",body, key = '6')
        acidity = st.radio("How do you like the acidity? ",acidity, key = '7')

        submitted = st.form_submit_button("Submit")
        if submitted:

            values_list = clustered_df.loc[(clustered_df['body_description']==body)&(clustered_df['type']==red_white)&(clustered_df['acidity_description']==acidity)]['wine_id'].values

            if len(values_list) > 0:
                recomendation = random.choice(values_list)
                print(recomendation)
                wine = clustered_df[clustered_df['wine_id']==recomendation]['wine_name'].values[0]
                print(wine)
                region = clustered_df[clustered_df['wine_id']==recomendation]['region'].values[0]
                print(region)
                country = clustered_df[clustered_df['wine_id']==recomendation]['country'].values[0]
                print(country)

                st.success('I recommend you to try:    '+ wine+ ' from '+region+ ' in '+country)
            else: 
                st.error("Sorry, I don't have recomendations for those characteristics.")

    st.image('wine3.jpg')