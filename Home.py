import streamlit as st

# Define custom CSS to set the background color to black and the dots to white
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
st.set_page_config(page_title="AW Wingman")

# Apply the custom CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title and text for the page
st.title("AW Wingman")

st.write(
    """
    Keeping global travel seamless to air travelers regardless of the extreme weather conditions.
    """
)
