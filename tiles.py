import streamlit as st
from PIL import Image
import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections
from chat import chatbot_response


def tiles():
    "st.session_state object:",st.session_state
    st.markdown("### Tiles")
    
    col1, col3, col4 = st.columns(5)
    
    if col1.button("Tile 1"):
        st.write("""Here's some information about Ancient civilizations
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""")
        if col3.button("Tile 3"):
            st.sidebar.title("About")
            st.sidebar.info("This is a simple chatbot created using Streamlit and NLTK.")
            st.header("Chatbot")
            user_input = st.text_input("You: ", "")
            if st.button("Ask"):
                response = chatbot_response(user_input)
                st.text_area("Chatbot:", value=response, height=200, max_chars=None, key=None)
    if col4.button("Tile 3"):
        st.write("Button 3 clicked!")


