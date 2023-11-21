import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="asterix online courses", page_icon=":tada:", layout="wide")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url = "https://lottie.host/8dd72c14-ee38-47ca-b1cb-1ecd288e04de/dKmyFttO6G.json"
lottie_json = load_lottieurl(lottie_url)


def homepage():
    with st.container():
        st.subheader("Welcome to Asterix Online Courses :wave:")
        st.title("A Website with a Variety of Courses.")
        st.write(
            "Currently on discount from November 1st - December 31th")

    with st.container():
        st.write('---')
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown("# HOME")
            st.markdown("##")

            st.write(
                """
                Embark on a transformative learning journey with our courses! Gain more than just knowledge
                – acquire practical skills that set you apart. Whether you're a beginner or looking to level up, our
                expert-led courses provide a roadmap to success. Join a community of like-minded learners,
                unlock your potential, and chart a course to new horizons. It's not just about education; it's about
                empowerment. Ready to turn aspirations into achievements? Enroll now and step into a world of
                growth and possibilities!
                """)

        with right_column:
            st_lottie(lottie_json, height=300, key="coding")


if True:
    homepage()
