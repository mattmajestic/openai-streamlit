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
import qrcode

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
            Using pure Python :snake: for leveraging OpenAI's product offerings including *Speech Recognition*, *AI Image Generation*, *chatGPT* examples within Streamlit.
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
        st.caption("Note: Currently static image as OpenAI API query limit has been reached")
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
    st.header("chatGPT in Streamlit")
    st.write("##")
    col1, col2 = st.columns(2)
    with col1:
        chat_msg = st.text_input("You:"," ",key="chat_msg")
        message(chat_msg, is_user=True) 
        chat_msg_res = "You asked me the following: " + chat_msg
        message(chat_msg_res) 
        
    with col2:
        st.header("OpenAI Whisper Chat in Streamlit")
        st.subheader("Emulating chatGPT but with Audio Input")
     
# --- Docs ---
with st.container():
    st.write("---")
    st.header("Documentation via Youtube")
    st.write("##")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("OpenAI Streamlit App in 1 minute")
        components.iframe("https://www.youtube.com/embed/yPSMC3FTYtA")
        st.write("Copy my code to make your own OpenAI Streamlit app.")
        
    with col2:
        st.subheader("OpenAI Python Overview")
        components.iframe("https://www.youtube.com/embed/0-caqm9hu38")
        st.write("Check out OpenAI as a company. We go over their funding, products & general thoughts on the company.")

# --- Mobile ---
with st.container():
    st.write("---")
    st.header("Scan for Mobile")
    st.caption("Question: Does Streamlit have a way to check the device type like in `shinybrowser` in `R`")
    st.write("##")

    col1, col2 = st.columns(2)
    with col1:
        data = 'https://openai-streamlit.app'
        img = qrcode.make(data)
        img.save("app_qr.png")
        st.image("app_qr.png")
    with col2:
        st.header("Infrastructure Notes")
        st.subheader("Code Hosted on Github & deployed on Google Cloud Run with Docker 🐋")
        st.write("Contribute to the Repo below")
        st.write("https://github.com/mattmajestic/openai-streamlit")
