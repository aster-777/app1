import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

crypto1 = Image.open("other_stuff/crypto1.jpeg")
crypto2 = Image.open("other_stuff/crypto2.jpeg")
crypto3 = Image.open("other_stuff/crypto3.jpeg")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = "https://lottie.host/932aea21-3e40-44f8-a849-c1f3381f835d/mgYJgFHyCk.json"

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("# Crypto Currency Courses")
        st.write("""
                    Dive into the dynamic world of cryptocurrency with our online course designed for both
                    newcomers and seasoned enthusiasts. Understand the fundamentals of blockchain, demystify
                    complex concepts, and gain practical insights into trading strategies. Whether you're looking to
                    invest wisely or comprehend the technology shaping the future, our comprehensive course
                    provides a roadmap to navigate the crypto landscape. Equip yourself with the knowledge to
                    make informed decisions, identify market trends, and harness the potential of blockchain. Join
                    us in decoding the crypto universe — because understanding is the first step to success. Enroll
                    today and take control of your financial future!""")
        st.write("---")
        st.write("##")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


def crypto():
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(crypto1)

        with text_column:
            st.subheader("CRYPTO PROFIT KIT")
            
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/740613/7698642)")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(crypto2)

        with text_column:
            st.subheader("A-Z Advanced Cryptocurrency Investment Course")
            
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/182163/7698642)")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(crypto3)

        with text_column:
            st.subheader("10X CRYPTOCURRENCIES MASTERMIND")
    
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/820523/7698642)")


if True:
    crypto()
