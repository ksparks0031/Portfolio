import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

df = pd.read_csv('data.csv', sep=';')

print(df)

col1, col2 = st.columns(2)

with col1:
    st.image(r'images\Me.jpg')

with col2:
    st.title('Kaleb Sparks')
    content = """Hi, I'm Kaleb! I am a Python programmer. I started my journey with python in March 2023. 
    I wanted to create something that would show off my little coding projects. I am currently a Computer
    Technician in the Clark County School District. I hope you enjoy my projects below. Feel free to contact
    me through the Contact Me page for any inquiries. """
    st.info(content)

st.text('Below you can find some of the apps that I have built in Python. Feel free to contact me', )

col3, col4 = st.columns(2)

with col3:
    for row, column in df[:10].iterrows():
        st.subheader(column['title'])
        st.write(column['description'])
        st.image('images\\' + column['image'])

with col4:
    for row, column in df[10:].iterrows():
        st.subheader(column['title'])
        st.write(column['description'])
        st.image('images\\' + column['image'])