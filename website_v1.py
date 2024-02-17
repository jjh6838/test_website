import streamlit as st
view = [100, 150, 30]
st.write('# Test Homepage of Jihyeon Jeong (Ji)')
st.write('## Welcome to my homepage')
st.write('### My name is Jihyeon Jeong and I am working as a data and knowledge management specialist at the Green Climate Fund. You will be able to see my academic and professional work here.')

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "col1": np.random.randn(1000) / 50 + 37.76,
    "col2": np.random.randn(1000) / 50 + -122.4,
    "col3": np.random.randn(1000) * 100,
    "col4": np.random.rand(1000, 4).tolist(),
})

st.map(df,
    latitude='col1',
    longitude='col2',
    size='col3',
    color='col4')
