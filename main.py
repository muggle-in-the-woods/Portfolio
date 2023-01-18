import streamlit as st
import pandas


st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title("Taras Koziupa")
    content0 = """
    Hey, I'm Taras! I'm a renewable energy engineer.
    """

    st.info(content0)

content1 = """
Below you can find some of the apps I've built with Python as well as my contact information
"""

st.write(content1)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])