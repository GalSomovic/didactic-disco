import streamlit as st
from src.save_system.save_manager import SaveManager

# Ensure save is loaded once
if "save_loaded" not in st.session_state:
    SaveManager.load_save_game()
    st.session_state.save_loaded = True

st.title("🌍 War Room")
st.subheader("What is going on in the world?")

if st.button("Next Day"):
    world = SaveManager.get("world")
    world.day += 1

    if world.events:
        st.write(f"The world was {', '.join(world.events)}")
        world.events.clear()  # Clear events after showing
    else:
        st.write("A calm day...")

    SaveManager.push()