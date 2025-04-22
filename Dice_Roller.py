import streamlit as st
import random

st.title("🎲 Random Dice Roller")
if st.button("Roll the Dice"):
    dice = random.randint(1, 6)
    st.write(f"You rolled a **{dice}**!")
