###############################
# This program lets you       #
# - Create a dashboard        #
# - Every dashboard page is  #
# created in a separate file  #
###############################

# Python libraries
import streamlit as st
from PIL import Image

# User module files
from main import main_recommender
from name import by_name
from grape import by_grape
from variety import by_variety
from features import by_features
from country import by_country

def main():

    #############
    # Main page #
    #############

    options = ['Welcome','By Name','By Grape', 'By Variety', 'By Features','By Country','AWR','Stop']
    choice = st.sidebar.selectbox("Menu",options, key = '1')  

    if ( choice == 'Welcome' ):
        st.markdown("# :wine_glass: Welcome to the ") 
        st.markdown("# Amazing Wine Recommender :wine_glass:")
        st.image('meme.jpg')
        pass
    
    elif ( choice == 'By Name' ):
        by_name()
        pass
    
    elif ( choice == 'By Grape' ):
        by_grape()
        pass
      
    elif ( choice == 'By Variety' ):
        by_variety()
        pass
    
    elif ( choice == 'By Features' ):
        by_features()
        pass
    
    elif ( choice == 'By Country' ):
        by_country()
        pass
    
    elif ( choice == 'AWR' ):
        main_recommender()
        pass
    
    else:
        st.stop()


main()
