import streamlit as st

import random

# List of names
names = ["Caleb", "Nya", "Connor", "Elliot", "Morgan"]

# Set the title of the app
st.title("Random Name Selector")

# Add a button to trigger the random selection
if st.button("Select a Random Name"):
    # Randomly select a name
    selected_name = random.choice(names)
    # Display the selected name
    st.write(f"The randomly selected name is: **{selected_name}**")
else:
    st.write("Click the button to select a random name!")

