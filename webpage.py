import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
st.sidebar.title("Navigation")
options = st.sidebar.radio("## COURSES", options=["HOME",
                                                  "Graphics Designing Courses",
                                                  "Crypto Currency",
                                                  "Forex Trading Courses",
                                                  "Video Editing Courses",
                                                  "Web Designing Courses",
                                                  "Ultimate Money Making Course"])
try:
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
except Exception as err:
    print(err)


with st.container():
    st.subheader("Hi, i am Emmanuel :wave:")
    st.title("Just made my first website")
    st.write("I am passionate about finding ways to use python and vba to be more efficient and effective for business")
    st.write("[learn more >](the links)")
try:
    lottie_coding = "https://lottie.host/8dd72c14-ee38-47ca-b1cb-1ecd288e04de/dKmyFttO6G.json"
    img_contact_form = Image.open("pic/black2.jpg")
    img_contact = Image.open("pic/blue1.jpg")
except Exception as err:
    print(err)

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what i do")
        st.write(
            """
            This is the website that helps me out with everthing and stuff
            and it can be used to do many things
            but its most helpful in selling
            """)
        st.write("[YouTube Channel >]( the links)")

with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact)

    with text_column:
        st.subheader("How to make something out of nothing")
        st.write(
            """
            learn how to different things fast
            the answer is here
            look no further
            """)
        st.markdown("[watch video...]( the link)")
