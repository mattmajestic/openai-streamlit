#  pip install requests streamlit streamlit_lottie bokeh==2.4.1
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from bokeh.models.widgets import Div
import openai
import os
import numpy as np
from io import BytesIO
import streamlit.components.v1 as components

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
        
def audiorec_demo_app():

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    # Custom REACT-based component for recording client audio in browser
    build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
    # specify directory and initialize st_audiorec object functionality
    st_audiorec = components.declare_component("st_audiorec", path=build_dir)

    # STREAMLIT AUDIO RECORDER Instance
    val = st_audiorec()
    # web component returns arraybuffer from WAV-blob
    st.write('Audio data received in the Python backend will appear below this message ...')

    if isinstance(val, dict):  # retrieve audio data
        with st.spinner('retrieving audio-recording...'):
            ind, val = zip(*val['arr'].items())
            ind = np.array(ind, dtype=int)  # convert to np array
            val = np.array(val)             # convert to np array
            sorted_ints = val[ind]
            stream = BytesIO(b"".join([int(v).to_bytes(1, "big") for v in sorted_ints]))
            wav_bytes = stream.read()

        # wav_bytes contains audio data in format to be further processed
        # display audio data as received on the Python side
        st.audio(wav_bytes, format='audio/wav')


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
        ai_image_idea = st.text_input("Enter an Image to Create","two orange cats playing chess, oil painting",key="placeholder")
        st.button("Generate Art 🏃",key="generate")
        
    with col2:
        with st.spinner('Generating your Art'):
            image_resp = openai.Image.create(prompt=ai_image_idea, n=4, size='256x256')
            st.image(image_resp["data"][0]["url"])
            st.image(image_resp["data"][1]["url"])
            
# --- Audio ---
audiorec_demo_app()
        
# --- Docs ---
with st.container():
    st.write("---")
    st.header("Docs")
    st.write("##")

    col1, col2 = st.columns(2)
    with col1:
        st.image("https://avatars.githubusercontent.com/u/14957082?s=200&v=4")
        st.subheader("Demo Video")
        st.write("Check out OpenAI as a company. We go over their funding, products & general thoughts on the company.")
    with col2:
        st.image("https://avatars.githubusercontent.com/u/14957082?s=200&v=4")
        st.subheader("OpenAI Python Docs")
        st.write("This is a pure Python web app leveraging the OpenAI package within Streamlit.")

st.write("---")
st.subheader("Deployed via Github & Google Cloud 💻")
