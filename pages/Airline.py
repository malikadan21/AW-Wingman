import streamlit as st
import requests

# Define custom CSS to set the background color and dots
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #000000; /* Black background */
    opacity: 0.8;
    background-image: radial-gradient(#ffffff 0.5px, #000000 0.5px); /* White dots on a black background */
    background-size: 60px 60px; /* Size of the dots */
}
</style>
"""

st.set_page_config(page_title="Airline")

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Airline")

st.sidebar.button("Admin")
st.sidebar.button("Login")

search_query = st.text_input("Search for Airline")

if search_query:
    st.write(f"You searched for: {search_query}")

    api_url = "https://example.com/api/search"  
    params = {"query": search_query}

    try:
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            results = response.json()
            st.write("Results from API:")
            st.json(results)
        else:
            st.write(f"Failed to retrieve data from the API. Status code: {response.status_code}")
            st.write(f"Response text: {response.text}")
    except requests.RequestException as e:
        st.write(f"An error occurred: {e}")
