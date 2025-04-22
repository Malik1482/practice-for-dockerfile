import streamlit as st
import random

st.title("🎵 Random Music Mood")
moods = ["Chill", "Party", "Focus", "Romantic", "Sad", "Energetic"]

if st.button("What should I listen to?"):
    mood = random.choice(moods)
    st.write(f"Try some **{mood}** music today!")
