import streamlit as st
from PIL import Image

# Load the image
image = Image.open("my_plot.png")

# Display in Streamlit
st.image(image, caption='Sample Plot', use_column_width=True)
