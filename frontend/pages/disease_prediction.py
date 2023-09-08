import streamlit as st
import requests

def show_page():
    st.title("Disease Prediction")

    # User input for epochs
    epochs = st.number_input("Number of Epochs", min_value=1, step=1)

    # Train Model button
    if st.button("Train Model"):
        if epochs >= 1:
            st.info(f"Training the model for {epochs} epochs...")

            # Send a request to the backend with the selected epochs
            response = send_train_request(epochs)

            # Display the backend's response (you can customize this)
            st.success(response)
        else:
            st.error("Please choose a valid number of epochs.")

def send_train_request(epochs):
    # Define the backend API URL
    backend_url = "http://disease_prediction:8000/train"  # Replace with your backend URL

    try:
        # Send a POST request to the backend with 'epochs' as a query parameter
        response = requests.post(backend_url, params={"epochs": epochs})

        # Check the response status code
        if response.status_code == 200:
            return "Model training started successfully."
        else:
            return f"Error: {response.status_code} - {response.text}"

    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    show_page()
