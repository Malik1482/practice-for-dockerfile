import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="📅 Date & Time", page_icon="⏰")

st.title("📅 Current Date & Time")

# Real-time toggle
live_update = st.checkbox("🔄 Enable live update", value=False)

# Main loop
if live_update:
    placeholder = st.empty()
    while True:
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        placeholder.markdown(f"### ⏰ {current_time}")
        time.sleep(1)
else:
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    st.markdown(f"### ⏰ {current_time}")
