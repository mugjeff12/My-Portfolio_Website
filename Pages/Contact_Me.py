import streamlit as st
import send_email as se
st.title("Contact me")

with st.form(key="Email Form"):
    user_email=st.text_input("Your Email Address: ")
    raw_message =st.text_area("Message")
    message = f"""\
Subject: New Email from {user_email}
From: {user_email}
{raw_message}"""

    button =st.form_submit_button("Submit")
    if button:
        se.send_email(message)
        st.info("Your email was sent successfully!")