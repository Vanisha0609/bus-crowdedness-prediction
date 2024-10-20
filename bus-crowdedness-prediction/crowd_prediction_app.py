# Install streamlit in your environment: !pip install streamlit
import joblib
import streamlit as st
clf = joblib.load('random_forest_model.pkl')
# Title
st.title('Bus Crowdedness Prediction')

# Input form for user to provide data
temperature = st.number_input('Temperature (Celsius)', min_value=25.0, max_value=40.0, value=30.0)
humidity = st.number_input('Humidity (%)', min_value=50.0, max_value=90.0, value=60.0)
rainfall = st.number_input('Rainfall (mm)', min_value=0.0, max_value=50.0, value=10.0)
traffic_congestion = st.slider('Traffic Congestion (1-10)', min_value=1, max_value=10, value=5)
avg_speed = st.number_input('Average Speed (km/h)', min_value=20.0, max_value=50.0, value=40.0)
num_stops = st.slider('Number of Stops', min_value=5, max_value=30, value=15)
is_weekend = st.selectbox('Is it a Weekend?', [0, 1])  # 0 = Weekday, 1 = Weekend

# Button to make the prediction
if st.button('Predict Crowdedness'):
    # Prepare input for prediction
    input_data = [[temperature, humidity, rainfall, traffic_congestion, avg_speed, num_stops, is_weekend]]
    prediction = clf.predict(input_data)

    # Display the result
    if prediction[0] == 1:
        st.write("Prediction: The bus will be **Crowded**.")
    else:
        st.write("Prediction: The bus will **NOT** be Crowded.")
