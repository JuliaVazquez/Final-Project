def by_country():
    
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
    countries = ['All','portugal', 'spain', 'italy', 'france', 'argentina', 'australia',
       'brazil', 'chile', 'new-zealand', 'south-africa', 'united-states',
       'israel', 'germany', 'switzerland']
    variety = ['All','Cabernet Sauvignon', 'Garnacha', 'Mencía', 'Merlot',
       'Monastrell', 'Blend del Ródano', 'Rioja', 'Syrah', 'Tempranillo',
       'Amarone', 'Barbaresco', 'Barolo', 'Bolgheri', 'Brunello',
       'Chianti', 'Nebbiolo', 'Pinot Noir', 'Ripasso', 'Primitivo',
       'Barbera', 'Sangiovese', 'Montepulciano', 'Cannonau', 'Albariño',
       'Bonarda', 'Blend de Burdeos', 'White', 'Cabernet', 'Carménère',
       'Chablis', 'Chardonnay', 'Chenin blanc', 'Côte-Rotie', 'Gavi',
       'Gewürztraminer', 'Malbec', 'Müller Thurgau', 'Pinot Blanc',
       'Pinot Gris', 'Grauburgunder', 'Spätburgunder', 'Pinotage',
       'Riesling', 'Sauvignon Blanc', 'Jerez', 'Soave', 'Shiraz',
       'Verdejo', 'Vinho verde', 'Viognier', 'Zinfandel',
       'Cabernet Franc', 'Silvaner', 'Médoc', 'Margaux', 'Pauillac',
       'Pomerol', 'Libourne', 'Torrontés', 'Moscatel', 'Saint-Estèphe',
       'Cote Nuits', 'Cote Beaune', 'Cote Chalonnaise', 'Maconnais',
       'Condrieu', 'Cornas', 'Crozes-Hermitage', 'Hermitage',
       'Saint-Péray', 'Pedro Ximenez', 'Chasselas', 'Vin Jaune',
       'Vino espumoso', 'Dornfelder']
   
    
    with st.form("my_form"):
        # Get input values

        red_white = st.radio("Are you looking for a Red or White Wine? ",red_white, key = '13')
        country = st.selectbox("Where are you looking for wine?",countries, key = '14')
        country2 = st.selectbox("Where is from a wine that you like? ",countries, key = '15')
        variety = st.selectbox('Would you like to choose a variety that you like?',variety,key = '16')
        

        submitted = st.form_submit_button("Submit")
        if submitted:
            
            if country2 != 'All':
                df = clustered_df[clustered_df['country']==country2]
            else:
                df = clustered_df
            
            if variety != 'All':
                df = df[df['varietal_name']==variety]
            else:
                pass
            
            clusters_list = df['clusters'].values
            
            
            if red_white != 'All':
                recom_df = clustered_df[clustered_df['type']==red_white]
            else:
                recom_df = clustered_df
                
            if country != 'All':
                recom_df = recom_df[recom_df['country']==country]
            else:
                pass
             
                

            if len(clusters_list) > 0:
                
                clusters_list_2 = recom_df['clusters'].values
                recomendation = random.choice(list(set(clusters_list).intersection(clusters_list_2)))              

                
                if recomendation != None:
                    recom = random.choice(recom_df['wine_id'].values)
              
                    wine = recom_df[recom_df['wine_id']==recom]['wine_name'].values[0]
                    type = recom_df[recom_df['wine_id']==recom]['type'].values[0]

                    region = recom_df[recom_df['wine_id']==recom]['region'].values[0]

                    country = recom_df[recom_df['wine_id']==recom]['country'].values[0]


                    st.success('I recommend you to try:    '+ wine+ ', a '+type.casefold()+' wine from '+region+ ' in '+country)
                    
                else:
                    st.warning("Sorry, I don't have a recommendation for you with those parameters. Please, try a different ones.")
            else: 
                recom = random.choice(recom_df['wine_id'].values)
              
                wine = recom_df[recom_df['wine_id']==recom]['wine_name'].values[0]
                type = recom_df[recom_df['wine_id']==recom]['type'].values[0]

                region = recom_df[recom_df['wine_id']==recom]['region'].values[0]

                country = recom_df[recom_df['wine_id']==recom]['country'].values[0]
                st.success('I recommend you to try:    '+ wine+ ', a '+type.casefold()+' wine from '+region+ ' in '+country)

    
    st.image('countries.jpg')