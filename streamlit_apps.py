import streamlit as st

# Define the pages
main_page = st.Page("test_1.py", title="Main Page", icon="🎈")
page_2 = st.Page("test_2.py", title="Page 2", icon="❄️")
page_3 = st.Page("test_3.py", title="Page 3", icon="🎉")
page_4 = st.Page("uber_pickups.py", title="Page 4", icon="🚀")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3, page_4])

# Run the selected page
pg.run()