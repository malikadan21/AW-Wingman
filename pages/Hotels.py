import streamlit as st

# Define custom CSS to set the background color and dots
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #000000; /* Black background */
    opacity: 0.8;
    background-image: radial-gradient(#ffffff 0.5px, #000000 0.5px); /* White dots on a black background */
    background-size: 60px 60px; /* Size of the dots */
}

[data-testid="stSidebar"] {
    margin-top: 50px;
}


[data-testid="collapsedControl"] {
    margin-top: 50px;
}
</style>
"""

# Set up the page configuration
st.set_page_config(page_title="Hotels")

# Apply the custom CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title of the page
st.title("Hotels")

# Sidebar buttons
st.sidebar.button("Admin")
st.sidebar.button("Login")

# Text input for search query
search_query = st.text_input("Search for Hotels")

if search_query:
    st.write(f"You searched for: {search_query}")
