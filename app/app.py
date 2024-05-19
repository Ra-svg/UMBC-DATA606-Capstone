import streamlit as st
import numpy as np
import joblib

# Load your trained model
model = joblib.load('best_model.pkl')

# Function to make predictions
def predict_price(beds, bath, propertysqft, state, locality, sublocality):
    # Convert inputs to array
    input_array = np.array([[beds, bath, propertysqft, 0, 0]])  # Adding placeholder values for state, locality, and sublocality
    # Make prediction 
    prediction = model.predict(input_array)
    # Calculate total price
    total_price = prediction * propertysqft
    return total_price

# Title of the web page
st.title('New York Housing Price Prediction')

# Layout for the input fields
col1, col2 = st.columns(2)
with col1:
    beds = st.number_input('Number of Bedrooms', min_value=1, max_value=10, value=3)
with col2:
    bath = st.number_input('Number of Bathrooms', min_value=1, max_value=10, value=2)

propertysqft = st.number_input('Property Square Feet', min_value=100, max_value=10000, value=1000)
state = st.text_input('State', value='New York')
locality = st.text_input('Locality', value='New York City')
sublocality = st.text_input('Sublocality', value='Manhattan')

# Button to make prediction
if st.button('Predict Price'):
    total_price = predict_price(beds, bath, propertysqft, state, locality, sublocality)
    st.write(f"Estimated total price: ${total_price[0]:,.2f}")

# Include the model download link
st.write('Download the model for offline predictions:')
st.download_button(label="Download Model",
                   data=open('best_model.pkl', "rb"),
                   file_name='best_model.pkl',
                   mime='application/octet-stream')


