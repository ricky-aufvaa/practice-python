"""
File: frontend.py

Description:
This file contains the frontend logic for the Employee Sign-In application using Streamlit.
The frontend provides a simple user interface where users can input their name and employee ID,
submit the information, and receive a personalized welcome message from the backend.

Key Features:
- Displays two input fields for the user to enter their name and employee ID.
- Includes a "Sign In" button to submit the form data to the backend.
- Sends the input data to the Flask backend via an HTTP POST request.
- Displays the welcome message returned by the backend or shows error messages if the input is invalid.

How It Works:
1. The user enters their name and employee ID in the respective input fields.
2. When the "Sign In" button is clicked, the frontend collects the input data and sends it as a JSON payload to the Flask backend.
3. The backend processes the data and returns a welcome message (e.g., "Welcome John Doe - 12345").
4. The frontend displays the welcome message to the user.

Usage:
- Run this file to start the Streamlit app:
  $ streamlit run frontend.py
- The app will open in your browser at http://localhost:8501 by default.
- Ensure the Flask backend is running and accessible at http://127.0.0.1:5000.

Dependencies:
- Streamlit: A Python library for building interactive web apps.
- Requests: A library for making HTTP requests to the backend.
- Install dependencies using `pip install -r requirements.txt`.

Author: Sarabjot Singh
Date: 21-02-2025
Version: 1.0
"""

import streamlit as st
import requests

st.title("Employee Sign-In App")

# Input fields for name and employee ID
name = st.text_input("Enter your name:")
employee_id = st.text_input("Enter your employee ID:")

# Button to submit the form
if st.button("Sign In"):
    if name and employee_id:
        # Prepare the data to send to the Flask backend
        data = {
            "name": name,
            "employee_id": employee_id
        }

        # Send a POST request to the Flask backend
        response = requests.post("http://127.0.0.1:5000/signin", json=data)

        # Check the response status
        if response.status_code == 200:
            result = response.json()
            st.success(result["message"])  # Display the welcome message
        else:
            st.error("Error: Please provide both name and employee ID.")
    else:
        st.warning("Please fill in both fields.")
