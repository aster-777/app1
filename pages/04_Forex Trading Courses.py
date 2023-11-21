import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

forex1 = Image.open("other_stuff/forex1.jpeg")
forex2 = Image.open("other_stuff/forex2.jpeg")
forex3 = Image.open("other_stuff/forex3.jpeg")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = "https://lottie.host/c337b7a3-d3de-4e55-b7c5-4a428cef8821/j7h08aT9Zm.json"

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("# Forex Trading Courses")
        st.write("""
                   "Embark on a journey to financial mastery with our online Forex trading course. Whether you're
                    a beginner or an experienced trader, our comprehensive program covers everything from the
                    basics to advanced strategies. Dive into the world of currency markets, grasp technical analysis,
                    and hone your trading skills with real-world scenarios. Learn to navigate the complexities of
                    Forex with confidence, make strategic decisions, and seize opportunities in the global market.
                    Elevate your trading game, unlock potential profits, and shape your financial destiny. Ready to
                    trade your way to success? Enroll now and take the first step towards becoming a proficient
                    Forex trader!
                    """)
        st.write("---")
        st.write("##")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


def forex():
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(forex1)

        with text_column:
            st.subheader("Bank secrets Forex Course")
            
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/543223/7698642)")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(forex2)

        with text_column:
            st.subheader("Profitable Forex Strategies")
            
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/386279/7698642)")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(forex3)

        with text_column:
            st.subheader("Mastering Forex Synthetic Indices For Financial Success")
        
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/915996/7698642)")


if True:
    forex()
