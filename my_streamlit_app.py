requirements.txt
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Text elements
st.title("Jamies App")
st.header("Jamies Header")
st.subheader("Jamies Subheader")
st.text("Hier kommt mein cooler text. Irgendwann.")
st.markdown("Und dies ist ein **Cooler** *Text* mit **vielen** speizal *ZEICHEN*.")

# Data elements
data = pd.DataFrame({'x': range(1, 11), 'y': np.random.randn(10)})
st.dataframe(data)

# Chart elements
st.line_chart(data)

# Input Widgets
number = st.sidebar.number_input("Wähle eine Zahl", step=1)
st.write(f"Die gewählte Zahl ist {number}")

# Sidebar with layout und Containers
with st.sidebar:
    selected = st.radio("Wählen Sie eine Option", options=['A', 'B'])

with st.container():
    st.write("Dies ist ein Container")
    if selected == 'A':
        st.write("Option Links wurde gewählt")
    else:
        st.write("Option Rechts wurde gewählt")

# Chat-Element: Da Streamlit kein natives Chat-Element hat,
# können wir Input Widgets nutzen, um eine einfache Interaktion nachzuahmen
with st.container():
    st.header("Einfacher Chat-ähnlicher Dialog")
    user_input = st.text_input("Deine Nachricht:")
    if st.button("Senden"):
        st.write(f"Benutzer: {user_input}")
