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


.chat-message {
    margin-bottom: 20px;
    padding: 8px;
    border-radius: 5px;
}

.user-message {
    background-color: #B0B0B0; /* Dark Gray */
    color: black;
    text-align: left;
}

.api-message {
    background-color: #909090; /* Light Gray */
    color: white;
    text-align: left;
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
st.set_page_config(page_title="Passengers")

# Apply the custom CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title of the page
st.title("Passengers")

# Initialize the chat history and input field in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [{"role": "api", "message": "Hello! How can I assist you today?"}]
if 'user_message' not in st.session_state:
    st.session_state.user_message = ""

# Function to handle API request
def get_api_response(user_message):
    api_url = "https://example.com/api/chat"  # Replace with your API URL
    params = {"message": user_message}
    response = requests.post(api_url, json=params)
    
    if response.status_code == 200:
        return response.json().get('response', 'No response from API')
    else:
        return "Failed to get response from API."


for message in st.session_state.chat_history:
    if message['role'] == 'user':
        st.markdown(f'<div class="chat-message user-message">You: {message["message"]}</div>', unsafe_allow_html=True)
    elif message['role'] == 'api':
        st.markdown(f'<div class="chat-message api-message">Wingman: {message["message"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


with st.form(key='message_form', clear_on_submit=True):
    user_message = st.text_input("Type your message here:", key="user_message_input")
    submit_button = st.form_submit_button("Send")
    
    if submit_button:
        if user_message:
            st.session_state.chat_history.append({"role": "user", "message": user_message})

            api_response = get_api_response(user_message)
            
            st.session_state.chat_history.append({"role": "api", "message": api_response})

            st.session_state.user_message = ""
