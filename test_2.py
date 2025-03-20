import streamlit as st
import pandas as pd
import numpy as np
st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [13.0827, 80.2707],
    columns=['lat', 'lon'])

st.map(map_data)

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)