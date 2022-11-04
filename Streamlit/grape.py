def by_grape():
    
    
    # libraries
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

    # data
    varietal_df = pd.read_csv('varietal_df.csv')

    
    grapes = ['Touriga Nacional', 'Tempranillo', 'Sangiovese', 'Pinot Noir', 'Malbec', 'Shiraz/Syrah', 'Cabernet Sauvignon', 'Riesling', 'Tinta Roriz', 'Garnacha', 'Merlot', 'Carménère', 'Sauvignon Blanc', 'Spätburgunder', 'Chardonnay', 'Touriga Franca', 'Weissburgunder', 'Chasselas', 'All']
    
    grape = st.radio("What variety of grape do you like? ",grapes, key = '3')
    
    if st.button("Submit"):

        if grapes != 'All':
            
            df = varietal_df[(varietal_df['grapes_1_name']==grape)|(varietal_df['grapes_2_name']==grape)|(varietal_df['grapes_3_name']==grape)]

            recommended = random.choice(df['wine_id'].values)

            wine = varietal_df[varietal_df['wine_id']==recommended]['wine_name'].values[0]
            region = varietal_df[varietal_df['wine_id']==recommended]['region'].values[0]
            country = varietal_df[varietal_df['wine_id']==recommended]['country'].values[0].capitalize()

            st.success("Maybe you would like to try " + wine + ' from ' + region + ' in ' + country)

        elif grapes == 'All':

            recommended = random.choice(varietal_df['wine_id'].values)

            wine = varietal_df[varietal_df['wine_id']==recommended]['wine_name'].values[0]
            region = varietal_df[varietal_df['wine_id']==recommended]['region'].values[0]
            country = varietal_df[varietal_df['wine_id']==recommended]['country'].values[0].capitalize

            st.success("Maybe you would like to try " + wine + ' from ' + region + ' in ' + country)
            
            
    st.image('grapes.jpg')