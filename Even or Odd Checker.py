import streamlit as st
import random

st.title("🔢 Even or Odd Checker")

num = random.randint(1, 100)

if st.button("Check a Random Number"):
    st.write(f"Number: **{num}**")
    if num % 2 == 0:
        st.success("It's Even!")
    else:
        st.info("It's Odd!")
