import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.title('Streamlit 超入門')
img =Image.open('sample.jpg')
st.image(img, caption='usagi', width=None)
#witdh true は画像の幅を調整するかどうか noneだと元のサイズのまま固定
st.image(img, caption='usagi2', use_container_width=True)

# df = pd.DataFrame(
#     np.random.randn(100, 2) / [50, 50] + [35.67, 139.75],
#     columns=["lat", "lon"],
# )
# st.map(df)