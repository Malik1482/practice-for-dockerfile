import streamlit as st
import re

# Email validation function using regex
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Streamlit UI
st.title("📧 Email Validator & Saver")

email = st.text_input("Enter your email:")

if st.button("Check & Save"):
    if is_valid_email(email):
        with open("valid_emails.txt", "a") as file:
            file.write(email + "\n")
        st.success("✅ Valid email! Saved successfully.")
    else:
        st.error("❌ Invalid email format. Please try again.")

