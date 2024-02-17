import streamlit as st
view = [100, 150, 30]
st.write('# Ji test homepage')
st.write('# Welcome to my homepage')
st.write('## Test bar chart')
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview
