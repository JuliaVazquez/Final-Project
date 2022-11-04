def by_variety():
    
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
    varietal_folded = pd.read_csv('varietal_folded.csv')
    
    
    text = st.text_input("What variety you like?   ").casefold()
    
    if st.button("Get Your Recommendation"):


        if text in varietal_folded['varietal_name'].values:

            df = varietal_folded[varietal_folded['varietal_name'] == text]

            recommended = random.choice(df['wine_id'].values)

            wine = varietal_df[varietal_df['wine_id']==recommended]['wine_name'].values[0]
            region = varietal_df[varietal_df['wine_id']==recommended]['region'].values[0]
            country = varietal_df[varietal_df['wine_id']==recommended]['country'].values[0].capitalize()

            st.success("If you like " + text.capitalize() + ", " + wine + ' from ' + region + ' in ' + country + ' is from the same variety.')

        elif text not in varietal_folded['varietal_name'].values:
            st.error("Sorry I don't have any suggestions for that")
            
    st.image('wine4.jpg')