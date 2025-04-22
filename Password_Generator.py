import streamlit as st
import random
import string

st.title("🔐 Random Password Generator")
length = st.slider("Password Length", 4, 32, 12)

if st.button("Generate Password"):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    st.code(password)
