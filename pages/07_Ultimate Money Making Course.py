import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


aff = Image.open("other_stuff/aff.jpeg")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = "https://lottie.host/ffd63ca1-6f04-4809-96c2-5b4c2a0cb2f4/dSLC4QZc1u.json"

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("# Ultimate Money Making Course")
        st.write("""
                    Unlock the potential of passive income with our online affiliate marketing course. Tailored for
                    beginners and marketers aiming to boost their earnings, this program delves into the strategies
                    and tactics that successful affiliates use. From choosing profitable niches to optimizing
                    conversion funnels, discover the step-by-step process to create a sustainable affiliate income
                    stream. Learn how to select the right products, leverage social media, and maximize your
                    commissions. Ready to turn your online presence into a revenue-generating powerhouse?
                    Enroll now and embark on a journey to master the art of affiliate marketing!""")
        st.write("---")
        st.write("##")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


def umm_aff():
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(aff)

        with text_column:
            st.subheader("Ultimate Affiliate Marketing Program + DFY Sales System U.A.M.P ")
        
            st.markdown("[Click to learn more and Enroll >](https://aff.stakecut.com/501/7698642)")


if True:
    umm_aff()
