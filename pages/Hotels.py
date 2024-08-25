import streamlit as st
import requests

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

st.set_page_config(page_title="Hotel")

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Hotel")

st.sidebar.button("Admin")
st.sidebar.button("Login")

# Sidebar for navigation
st.sidebar.header("Navigation")
sidebar_option = st.sidebar.selectbox("Choose an option", ["Search Hotels", "Manage Bookings", "Room Availability", "Manage Rooms"])

if sidebar_option == "Search Hotels":
    search_query = st.text_input("Search for Hotels")

    if search_query:
        st.write(f"You searched for: {search_query}")

        api_url = "http://localhost:8000/api/v1/hotels/"  
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

elif sidebar_option == "Manage Bookings":
    customer_name = st.text_input("Customer Name")
    checkin_date = st.date_input("Check-in Date")
    checkout_date = st.date_input("Check-out Date")
    total_amount = st.number_input("Total Amount", min_value=0.0, format="%.2f")

    if st.button("Create Booking"):
        api_url = "http://localhost:8000/api/v1/bookings/"
        data = {
            "customer_name": customer_name,
            "checkin_date": checkin_date.isoformat(),
            "checkout_date": checkout_date.isoformat(),
            "total_amount": total_amount
        }

        try:
            response = requests.post(api_url, json=data)

            if response.status_code == 201:
                st.write("Booking created successfully.")
                st.json(response.json())
            else:
                st.write(f"Failed to create booking. Status code: {response.status_code}")
        except requests.RequestException as e:
            st.write(f"An error occurred: {e}")

elif sidebar_option == "Room Availability":
    availability_id = st.text_input("Availability ID")
    nights = st.number_input("Number of Nights", min_value=1)
    zipcode = st.text_input("Zip Code")
    availability_date = st.date_input("Availability Date")

    if st.button("Check Availability"):
        api_url = "http://localhost:8000/api/v1/room-availability/"
        data = {
            "availability_id": availability_id,
            "nights": nights,
            "zipcode": zipcode,
            "availability_date": availability_date.isoformat()
        }

        try:
            response = requests.post(api_url, json=data)

            if response.status_code == 200:
                availability = response.json()
                st.write("Room Availability:")
                st.json(availability)
            else:
                st.write(f"Failed to retrieve room availability. Status code: {response.status_code}")
        except requests.RequestException as e:
            st.write(f"An error occurred: {e}")

elif sidebar_option == "Manage Rooms":
    room_number = st.text_input("Room Number")
    room_type = st.text_input("Room Type")
    price_per_night = st.number_input("Price Per Night", min_value=0.0, format="%.2f")
    max_occupancy = st.number_input("Max Occupancy", min_value=1, format="%d")

    if st.button("Add Room"):
        api_url = "http://localhost:8000/api/v1/rooms/"
        data = {
            "room_number": room_number,
            "type": room_type,
            "price_per_night": price_per_night,
            "max_occupancy": max_occupancy
        }

        try:
            response = requests.post(api_url, json=data)

            if response.status_code == 201:
                st.write("Room added successfully.")
                st.json(response.json())
            else:
                st.write(f"Failed to add room. Status code: {response.status_code}")
        except requests.RequestException as e:
            st.write(f"An error occurred: {e}")
