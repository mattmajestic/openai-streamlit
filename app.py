#  pip install requests streamlit streamlit_lottie bokeh==2.4.1
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from bokeh.models.widgets import Div
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')


st.set_page_config(
    page_title="OpenAI Streamlit Gallery",
    page_icon=":rocket:",
    layout="wide",
)

st.balloons()

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
    col1, col2 = st.columns((2, 1))
    with col1:
        st.title("Welcome the OpenAI Streamlit Gallery")
        st.subheader("Deployed via Github & Google Cloud 💻")
        st.subheader(
            """
            Using pure Python for leveraging OpenAI's product offerings including *Speech Recognition*, *AI Image Generation*, *Autocomplete*, *chatGPT*, *etc*.
            """
        )
        st.write("""""")
        st.subheader(
            """
            This page is made with pure Python :snake: with Streamlit library.
            """
        )
    with col2:
        st_lottie(
            load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_bniew9j6.json"),
            height=500,
        )


# --- ABOUT ---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Create AI Artwork")
        
        st.text_input("Enter an Image to Create","two dogs playing chess, oil painting",key="placeholder")
        
        st.write(
            """
            Done via DALLE 🍕
            """
        )
    with col2:
        image_resp = openai.Image.create(prompt="two dogs playing chess, oil painting", n=4, size="512x512")
        st.image(image_resp["data"][0]["url"])
        
# --- Docs ---
with st.container():
    st.write("---")
    st.header("Docs")
    st.write("##")

    col1, col2 = st.columns(2)
    with col1:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("Demo Video")
        st.write("Check out OpenAI as a company. We go over their funding, products & general thoughts on the comapny.")
    with col2:
        st.image("https://csharpcorner-mindcrackerinc.netdna-ssl.com/UploadFile/NewsImages/08172020000734AM/Learn-Python.png")
        st.subheader("OpenAI Python Docs")
        st.write("This is a pure Python web app leveraging the OpenAI package within Streamlit.")

with st.container():
    st.write("---")
    st.markdown("<h2 style='text-align: center;'>Contact</h2>", unsafe_allow_html=True)
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col2:
        contact_form = """
        <form action="https://formsubmit.co/805cc992f02da35ae356f2451ece18be" method="POST">
            <input type="hidden" name="_captcha" value="true">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
