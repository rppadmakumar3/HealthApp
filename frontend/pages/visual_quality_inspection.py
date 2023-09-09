import streamlit as st
import requests

st.title("Model Training App")

# Create checkboxes for user options
dataaug = st.checkbox("Enable Data Augmentation", False)
hyperparams = st.checkbox("Enable Hyperparameter Tuning", False)
intel = st.checkbox("Enable Intel PyTorch Optimizations", False)

# Create a button to trigger model training
if st.button("Train Model"):
    # Define the payload with user-specified options as integers
    payload = {
        "dataaug": int(dataaug),  # Convert boolean to integer
        "hyperparams": int(hyperparams),  # Convert boolean to integer
        "intel": int(intel),  # Convert boolean to integer
    }

    # Send a POST request to the backend API
    backend_url = "http://visual_quality_inspection:8001/train"  # Replace with your backend URL

    try:
        response = requests.post(backend_url, data=payload)
        if response.status_code == 200:
            st.text("Training process initiated successfully.")
        else:
            st.text(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.text(f"Error: {e}")
