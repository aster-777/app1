import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = "https://lottie.host/b62bdf03-779d-4494-84c7-1f5841f55635/HIiGP916NW.json"

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("# Graphic Designing Courses")
        st.write("""
                    Dive into the world of graphic design with our online course that goes beyond the basics.
                    Unleash your creativity as you learn to design stunning visuals, master essential tools, and
                    cultivate a unique design perspective. Whether you're a beginner or seeking to refine your skills,
                    our course offers hands-on projects and expert insights to elevate your graphic design game.
                    Stand out in a crowded digital landscape, create impactful designs, and open doors to exciting
                    opportunities. Ready to turn your passion into pixel-perfect proficiency? **Enroll now and embark
                    on a visual journey of skill enhancement!**""")
        st.write("---")
        st.write("##")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


graph1 = Image.open("other_stuff/graph1.jpg")
graph2 = Image.open("other_stuff/graph2.jpg")
graph3 = Image.open("other_stuff/graph3.jpg")

def graph_des():
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(graph1)

        with text_column:
            st.subheader("Beyond Graphic Design Course")
    
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/874325/7698642)")
            print("---")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(graph2)

        with text_column:
            st.subheader("Learn and Master Graphic Design in 30 Days ...The Complete course...")
           
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/8519/7698642)")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(graph3)

        with text_column:
            st.subheader("Design to Dollars: The Steady Graphic Design Income Generator ...For Smartphone & PC...")
        
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/851987/7698642)")


if True:
    graph_des()

