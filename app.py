import streamlit as st

st.write("Hello, *semua. selamat datang di webheyo!* :sunglasses:")
st.title("Asiknya Belajar Kimia 🦠🧪🧫")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
st.markdown("*Streamlit* is **really** ***cool***.")
st.metric(label="Temperature", value="70 °F")
st.metric(label="Temperature", value="70 °F")

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)
if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
