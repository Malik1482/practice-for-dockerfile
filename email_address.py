import streamlit as st

st.title("📧 Email Collector")

email = st.text_input("Enter your email address:")

if st.button("Submit"):
    if "@" in email and "." in email:
        with open("emails.txt", "a") as f:
            f.write(email + "\n")
        st.success("Email saved successfully!")
    else:
        st.error("Please enter a valid email address.")
