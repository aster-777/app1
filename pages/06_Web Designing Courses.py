import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

web = Image.open("other_stuff/web.jpeg")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = "https://lottie.host/6a51f1fb-2744-4c5c-93e5-3bf45796f01d/ES1iTFqDwX.json"

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("# Web Designing Courses")
        st.write("""
                    Transform your passion for web design into a career-ready skill set with our online course.
                    From coding essentials to the latest design trends, our comprehensive program is crafted for
                    beginners and aspiring professionals alike. Dive into hands-on projects, master responsive
                    design, and unleash your creativity on the digital canvas. Whether you're dreaming of creating
                    stunning websites or pursuing a career in UX/UI design, our course provides the tools and
                    knowledge to bring your vision to life. Join us in shaping the digital landscape—enroll now and
                    embark on a journey to become a proficient web designer!""")
        st.write("---")
        st.write("##")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


def web_des():
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(web)

        with text_column:
            st.subheader("WP2PROFITS - 2 in 1 Web Design Master Class")
            
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/670063/7698642)")


if True:
    web_des()
