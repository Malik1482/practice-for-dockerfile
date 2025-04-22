import streamlit as st
import random

facts = [
    "Honey never spoils.",
    "A day on Venus is longer than a year.",
    "Bananas are berries, but strawberries aren't.",
    "Octopuses have three hearts.",
    "The Eiffel Tower can grow in summer."
]

st.title("🧠 Random Fun Fact Generator")

if st.button("Give me a fun fact!"):
    fact = random.choice(facts)
    st.info(fact)
