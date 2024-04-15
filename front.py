import streamlit as st
from PIL import Image
import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections
from tiles import tiles






session_state = st.session_state
if 'logged_in' not in session_state:
    session_state.logged_in = True
    

    


def main():
    

    if True:
        img = Image.open("logo.jpg")
        st.image(img, width=150)

        username = st.text_input(label="", value='', placeholder="Enter your username")
        password = st.text_input(label="", value='', placeholder="Enter your password", type='password')
        if st.button(label='Login'):
            # Check login credentials (dummy check for demonstration)
            if username == "varun" and password == "varun2004":
                session_state.logged_in = True
                tiles()
                
                
    elif page == "Tiles" and session_state.logged_in:
        st.title("Tiles Page")
        







if __name__ == "__main__":
    main()