import streamlit as st
from send_email import send_mail

st.header("Contact Me")

with st.form('email_form'):
    user_email = st.text_input('Your email address')
    message = st.text_area('Your message')
    message = f"""\
Subject: New email form {user_email}

From: {user_email}
{message}
"""
    button = st.form_submit_button('Submit')
    if button:
        send_mail(message)
        st.info("Email sent successfully")



