import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.title('Streamlit 超入門')
st.write('Display Image')

option = st.selectbox(
    'Select number',
    list(range(1,11))
)
'you selected ',option

condition = st.slider('あなたの今の調子は',0,100,50)
if condition==0:

    img =Image.open('sample.jpg')
    st.image(img, caption='usagi', width=None)
