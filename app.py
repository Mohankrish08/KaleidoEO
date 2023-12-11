# importing libraries

import streamlit as st
import streamlit_lottie as lottie
import cv2
import numpy as np
import matplotlib.pyplot as plt
from inference import inferencing_model
from PIL import Image
import os
import requests

# set up the page
st.set_page_config(page_title='KaleidEO', page_icon=":computer:", layout='wide')

# loading animations

def loader_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# lottie files

icon = loader_url('https://lottie.host/93d70947-ecf4-4aaf-be0c-2f19e11ae8aa/7jZ0o76bAw.json')


# main code

st.markdown("<h1 style='text-align: center;'>KaleidEO: MLOps Engineer Assignment</h1>", unsafe_allow_html=True)


with st.container():
    i,j = st.columns((1,2))
    with i:
        st.lottie(icon, height=300, key='icon')
    with j:
        photo = st.file_uploader('Upload the image', type=['jpg','jpeg','png','tiff'])
        if st.button('Enter') and photo is not None:
            inferencing_model(photo)
            st.image('predictions.jpg')

            os.remove('sample.jpg')
            os.remove('predictions.jpg')