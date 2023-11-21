import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

vid1 = Image.open("other_stuff/vid1.jpeg")
vid2 = Image.open("other_stuff/vid2.jpeg")
vid3 = Image.open("other_stuff/vid3.jpg")
vid4 = Image.open("other_stuff/vid4.jpg")
vid5 = Image.open("other_stuff/vid5.jpeg")
vid6 = Image.open("other_stuff/vid6.jpg")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = "https://lottie.host/3f3f5011-7889-45cc-bf10-537332fa8311/FfST9ZvJak.json"

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("# Video Editing Courses")
        st.write("""
                    Unlock the secrets of captivating video creation with our comprehensive video editing course!
                    From basic editing to advanced techniques, this course is designed for both beginners and
                    enthusiasts eager to elevate their skills. Discover the art of storytelling through seamless edits,
                    master industry-standard software, and unleash your creativity. Join us on a journey where you
                    not only learn the tools but also gain the confidence to bring your unique vision to life. Don't just
                    edit videos—craft cinematic experiences. Enroll now and transform your passion into
                    professional mastery!""")
        st.write("---")
        st.write("##")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


def video_edit():
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(vid1)

        with text_column:
            st.subheader("VIDEO CONTENT WORKSHOP")
            
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/432822/7698642)")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(vid2)

        with text_column:
            st.subheader("FULL PACK SMARTPHONE VIDEO EDITING COURSE")
            
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/100057/7698642")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(vid3)

        with text_column:
            st.subheader("SMARTPHONE VIDEO EDITING/CREATION MASTERY COURSE")
            st.write(
                """
                learn how to different things fast
                the answer is here
                look no further
                """)
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/10828/7698642")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(vid4)

        with text_column:
            st.subheader("VIDEO EDITING MASTERY")
            
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/267662/7698642")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(vid5)

        with text_column:
            st.subheader("THE COMPLETE SMARTPHONE VIDEOGRAPHY")
            
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/31234/7698642")

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(vid6)

        with text_column:
            st.subheader("The New Smartphone Video-Editing Boss Program")
            
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/548887/7698642")


if True:
    video_edit()
