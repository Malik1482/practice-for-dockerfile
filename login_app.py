import streamlit as st

# Dummy credentials
USERNAME = "admin"
PASSWORD = "1234"

# UI
st.set_page_config(page_title="Login Page", page_icon="🔐")
st.title("🔐 Login Page")

st.markdown("Please enter your credentials:")

# Input fields
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Login button
if st.button("Login"):
    if username == USERNAME and password == PASSWORD:
        st.success("✅ Login successful!")
        st.balloons()
    else:
        st.error("❌ Incorrect username or password.")
