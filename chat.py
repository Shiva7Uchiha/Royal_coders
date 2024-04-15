import streamlit as st
from PIL import Image
import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections



nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to help.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!",]
    ],
    [
        r"(.*) (good|great|well|doing well)",
        ["That's great to hear!",]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand. Can you please rephrase?",]
    ]
]

def chatbot_response(user_input):
    chatbot = Chat(pairs, reflections)
    response = chatbot.respond(user_input)
    return response

