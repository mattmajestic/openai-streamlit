import requests
import streamlit as st
from streamlit_lottie import st_lottie
from bokeh.models.widgets import Div
import openai
import os
import numpy as np
from io import BytesIO
import streamlit.components.v1 as components
from streamlit_chat import message

openai.api_key = os.getenv('OPENAI_API_KEY')

st.set_page_config(
    page_title="OpenAI Streamlit Gallery",
    page_icon=":rocket:",
    layout="wide",
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
#  To get rid of the Streamlit branding stuff
local_css("css/styles.css")


#  Anchor
st.title("#")  # This anchor is needed for the page to start at the top when it is called.

# --- INTRO ---

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.title("Welcome the OpenAI Streamlit Gallery")
        st.subheader(
            """
            Using pure Python :snake: for leveraging OpenAI's product offerings including *Speech Recognition*, *AI Image Generation*, *Autocomplete*, *chatGPT*, *etc* with Streamlit.
            """
        )
        st.write("""""")
    with col2:
        st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-lightmark-lighttext.png")


with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Create AI Artwork")
        st.caption("Note: Currently static image as I have it OpenAI API query limit")
        ai_image_idea = st.text_input("Enter an Image to Create","two dogs playing chess, oil painting",key="placeholder")
        st.button("Generate Art 🏃",key="generate")
        
    with col2:
        with st.spinner('Generating your Art'):
            st.image("dalle-dogs.png")
            #image_resp = openai.Image.create(prompt=ai_image_idea, n=4, size='256x256')
            #st.image(image_resp["data"][0]["url"])
            #st.image(image_resp["data"][1]["url"])
         
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        message("My message") 
        message("OpenAI Reponse from Whisper", is_user=True) 
        
    with col2:
       st.header("OpenAI Whisper Chat in Streamlit")
       st.subheader("Emulating chatGPT")
     
# --- Docs ---
with st.container():
    st.write("---")
    st.header("Docs")
    st.write("##")

    col1, col2 = st.columns(2)
    with col1:
        components.iframe("https://www.youtube.com/embed/yPSMC3FTYtA")
        st.subheader("Demo Video")
        st.write("Check out OpenAI as a company. We go over their funding, products & general thoughts on the company.")
    with col2:
        st.image("https://avatars.githubusercontent.com/u/14957082?s=200&v=4")
        st.subheader("OpenAI Python Docs")
        st.write("This is a pure Python web app leveraging the OpenAI package within Streamlit.")

st.write("---")
st.subheader("Deployed via Github :octocat: & Google Cloud via Docker 🐋")
