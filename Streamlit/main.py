def main_recommender():
        
    #libraries
    import pandas as pd
    import numpy as np
    import random
    import streamlit as st
    from PIL import Image
    import time

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
    clustered_folded = pd.read_csv('clustered_folded.csv')
    
    
    # Lists of acceptable values
    type = ['Red', 'White']
    country = ['All','portugal', 'spain', 'italy', 'france', 'argentina', 'australia',
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
    body = ['All','Strong','Medium','Weak', 'Very Weak']
    acidity = ['All','High','Medium','Low']
#     grapes = ['All','Touriga Nacional', 'Tempranillo', 'Sangiovese', 'Pinot Noir', 'Malbec', 'Shiraz/Syrah', 'Cabernet Sauvignon', 'Riesling', 'Tinta Roriz', 'Garnacha', 'Merlot', 'Carménère', 'Sauvignon Blanc', 'Spätburgunder', 'Chardonnay', 'Touriga Franca', 'Weissburgunder', 'Chasselas']
    

    # Get inputs:
    with st.form("main_form"):
        
        country = st.selectbox('Which country would you like be your recommended wine?',country,key = '8')
        red_white = st.radio("Are you looking for a Red or White Wine? ",type, key = '9')
        region = st.text_input('Would you like to choose a region?').casefold()
        variety = st.selectbox('Would you like to select a variety?',variety,key = '10').casefold()
#         grape = st.selectbox('Would you like to select type of grape?',grapes,key = '11').casefold()
        body = st.radio("How do you like the body of your wine? ",body, key = '12')
        acidity = st.radio("How do you like the acidity? ",acidity, key = '13')
        similar_wine = st.text_input('Tell me a wine you like:      ').casefold()
        similar_token = word_tokenize(similar_wine)
        
        my_bar = st.progress(0)
        percent_complete = 0
  
        
        submitted = st.form_submit_button("Submit")
        if submitted:
 
   
            df = clustered_folded[clustered_folded['type']==red_white.casefold()]
#             st.text(df)


            if country != 'All':
                df = df[df['country']==country]
            else:
                pass
#             st.text(df)

            if region in df['region'].values:
                df = df[df['region']==region]
            else:
                pass
#             st.text(df)
            
#             if grapes != 'all':
#                 df = df[(df['grapes_1_name']==grape)|(df['grapes_2_name']==grape)|(df['grapes_3_name']==grape)]
#             else:
#                 pass
#             st.text(df)
            
            if variety != 'all':
                df = df[df['varietal_name']==variety]
            else:
                pass
#             st.text(df)

            if body != 'all':
                df = df[df['body_description']==body]
            else:
                pass
#             st.text(df)

            if acidity != 'All':
                df = df[df['acidity_description']==acidity]
            else:
                pass
#             st.text(df)
            percent_complete += 10
            my_bar.progress(percent_complete)
            
            if df.shape[0] == 0:

                df = clustered_df[(clustered_df['type']==red_white)&(clustered_df['country']==country)]
#                 st.text(df)
                recommended = random.choice(df['wine_id'].values)
                
                wine = df[df['wine_id']==recommended]['wine_name'].values[0]
                region = df[df['wine_id']==recommended]['region'].values[0]
                country = df[df['wine_id']==recommended]['country'].values[0]

                my_bar.progress(percent_complete + 90)
                st.warning("Sorry, I don't have recommendations for all of those parameters but maybe you could try:    ")
                st.subheader( wine +' from ' + region+ ' in '+ country.capitalize())
            
                
            elif df.shape[0] < 12:
                recommended = random.choice(df['wine_id'].values)

                wine = clustered_df[clustered_df['wine_id']==recommended]['wine_name'].values[0]
                region = clustered_df[clustered_df['wine_id']==recommended]['region'].values[0]
                country = clustered_df[clustered_df['wine_id']==recommended]['country'].values[0]

                my_bar.progress(percent_complete + 90)
                st.success("My recommendation is:    ")
                st.subheader( wine +' from ' + region+ ' in '+ country.capitalize())
                

            else:

                df_num = df[['body','acidity_1','acidity_2','fizziness','intensity','sweetness','tannin','num_ratings','rate']]


                #fit and transform scaling numericals MinMax
                transformer = MinMaxScaler().fit(df_num)
                
                percent_complete += 10
                my_bar.progress(percent_complete)
                
                X_num = transformer.transform(df_num)
                # convert to dataframe again
                X_num = pd.DataFrame(X_num,columns=df_num.columns).reset_index(drop=True)
                
                percent_complete += 10
                my_bar.progress(percent_complete)


                # HOW MANY CLUSTERS IN RELATION WITH HOW MANY VARIABLES¿?

                #building clusters with default 12
                kmeans = KMeans(n_clusters=12)
                kmeans.fit(X_num)
                
                percent_complete += 10
                my_bar.progress(percent_complete)

                # Assigning the clusters:
                new_clusters = kmeans.predict(X_num)
                df['new_clusters'] = new_clusters
                
                percent_complete += 10
                my_bar.progress(percent_complete)


                bow_vect = CountVectorizer()

                # For SIMILAR wine
                bow_vect.fit(similar_token)
                
                percent_complete += 10
                my_bar.progress(percent_complete)

                values = []
                for i in range(len(clustered_folded['tokenized'])):
                    values.append(np.sum(bow_vect.transform([clustered_folded['tokenized'][i]]).toarray()))
                    
                percent_complete += 10
                my_bar.progress(percent_complete)
                
                
                
                indexes = []
                for i in range(len(values)):
                    if values[i]==max(values):
                        indexes.append(i)
                        
                percent_complete += 10        
                my_bar.progress(percent_complete)                        
                        
                if max(values) == 0:
                    random_id = random.choice(df['wine_id'].values)
                    wine = df[df['wine_id']==random_id]['wine_name'].values
                    type = df[df['wine_id']==random_id]['type'].values
                    region = df[df['wine_id']==random_id]['region'].values
                    country = df[df['wine_id']==random_id]['country'].values
                
                    percent_complete += 20
                    my_bar.progress(percent_complete)   
                    
                    
                    st.error("Sorry, I don't recognize this wine, but I can recommend you: ")
                    st.subheader(wine+', a '+type.casefold()+' wine from '+region+' i n '+country.capitalize())

                
                else:
                    index_random = random.choice(indexes)
                    df2 = clustered_df.loc[index_random]
                    df2_num = pd.DataFrame(df2[['body','acidity_1','acidity_2','fizziness','intensity','sweetness','tannin','num_ratings','rate']]).T
                    
                    X2_num = transformer.transform(df2_num)
                    # convert to dataframe again
                    X2_num = pd.DataFrame(X2_num,columns=df2_num.columns).reset_index(drop=True)
                    
                    percent_complete += 10
                    my_bar.progress(percent_complete)
                              
                    #predict cluster
                    X2_cluster = kmeans.predict(X2_num)
                    
                    values_list = df[df['new_clusters'] == X2_cluster[0]]['wine_id'].values

                    recomendation = random.choice(values_list)
                    
                    percent_complete += 10
                    my_bar.progress(percent_complete)
                              
                    wine = clustered_df[clustered_df['wine_id']==recomendation]['wine_name'].values[0]
                    
                    type = clustered_df[clustered_df['wine_id']==recomendation]['type'].values[0]

                    region = clustered_df[clustered_df['wine_id']==recomendation]['region'].values[0]

                    country = clustered_df[clustered_df['wine_id']==recomendation]['country'].values[0]

                    st.success('My recommendation is:    ')
                    st.subheader(wine +', a '+type.casefold()+' wine from ' + region + ' in ' + country.capitalize())

