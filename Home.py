import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="JK Lakshmi Cement",
    page_icon="👋",
)

# Display a logo image
import streamlit as st

# Define the logo and text
logo = "pic.png"

# Create a two-column layout
col1, col2 = st.columns([1, 2.4])

# Display the logo in the first column
with col1:
    st.image(logo, use_column_width=True)

# Display the text in the second column
with col2:
    st.title("Face Detection and Recognition JK Lakshmi Cement")














# image = Image.open("C:\\Users\\modip\\PycharmProjects\\AMSBOC\\Hackathon\\JK-LAKSHMI-CEMENT-pic.png")
# st.image(image, height=50, width=50)


