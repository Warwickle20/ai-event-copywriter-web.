import streamlit as st
import time

st.set_page_config(page_title="AI Event Copywriter", layout="centered")

st.title("✨ AI Event Marketing Generator")
st.write("Generate engaging event names and marketing copy instantly.")

event_theme = st.text_input("Enter the event theme (e.g., Retro Bollywood, Tech Conference):")
target_audience = st.selectbox("Target Audience", ["Corporate", "Students", "Families", "General Public"])

if st.button("Generate Web Copy"):
    if event_theme:
        with st.spinner("AI is generating your copy..."):
            time.sleep(1.5) # Simulating API latency
            
            st.success("Generation Complete!")
            st.subheader("Suggested Event Names:")
            st.write(f"1. The {event_theme.title()} Experience")
            st.write(f"2. {target_audience} presents: A Night of {event_theme.title()}")
            
            st.subheader("Landing Page Hero Text:")
            st.info(f"Join us for an unforgettable evening celebrating {event_theme}. Designed exclusively for {target_audience}, this event will feature live entertainment, networking, and premium experiences.")
    else:
        st.warning("Please enter an event theme to proceed.")
