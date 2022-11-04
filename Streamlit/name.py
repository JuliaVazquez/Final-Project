def by_name():
    
    
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
    clustered_df = pd.read_csv('clustered_df.csv')
    clustered_folded = pd.read_csv('clustered_folded.csv')


    text = st.text_input("Write a wine name and I will recommend a similar one:   ").casefold()
    if st.button("Get Your Recommendation"):
        
        tokens = word_tokenize(text)


        bow_vect = CountVectorizer()
        bow_vect.fit(tokens)     
        

        values = []
        for i in range(len(clustered_folded['tokenized'])):
              values.append(np.sum(bow_vect.transform([clustered_folded['tokenized'][i]]).toarray()))

        
        if max(values) == 0:

                st.error("Sorry, I don't recognize this wine.")
        else:

            indexes = []
            for i in range(len(values)):
                if values[i]==max(values):
                    indexes.append(i)



            random_index = random.choice(indexes)
            cluster = clustered_folded.loc[random_index]['clusters']
            df = clustered_df[clustered_df['clusters'] == cluster]

            
            
            recommended = random.choice(df['wine_id'].values)
            wine = df[df['wine_id']==recommended]['wine_name'].values[0]
            type = df[df['wine_id']==recommended]['type'].values[0]
            region = df[df['wine_id']==recommended]['region'].values[0]
            country = df[df['wine_id']==recommended]['country'].values[0].capitalize()

            st.success('My recommendation is:    ')
            st.subheader( wine +' a '+type.casefold()+' wine from ' + region+ ' in '+ country.capitalize())

    st.image('name.jpg')