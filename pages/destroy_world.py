import streamlit as st
from src.save_system.save_manager import SaveManager

st.title("💥 Destroy the World")

if st.button("Do it."):
    world = SaveManager.get("world")
    world.events.append("destroyed")
    st.success("You doomed the planet 🌎")
