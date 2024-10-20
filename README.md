# bus-crowdedness-prediction

The problem we are addressing is the unpredictability of passenger crowds in public buses, which leads to inefficient number of buses ,delays, overcrowding, and passenger discomfort, especially during peak hours in urban areas like Chennai. Public transportation systems often struggle to adjust bus schedules and frequencies dynamically due to a lack of accurate real-time data on passenger demand and external factors like traffic and weather.


Solution Approach:

A synthetic dataset was created to simulate daily bus and metro ridership over 365 days, incorporating factors like temperature, humidity, rainfall, traffic congestion, and route information (average speed, number of stops).
A Random Forest Classifier was trained on the dataset to predict bus crowdedness based on the input features.
The model was evaluated using accuracy score, confusion matrix, and classification report to measure performance
A user-friendly Streamlit app was built to recieve predictions on bus crowdness

Tech Stack

Programming Language:

Python: Used for building the machine learning model and developing the web application.

Libraries/Frameworks:

pandas: For data manipulation and preprocessing.
numpy: For numerical computations.
scikit-learn: For implementing the Random Forest Classifier and other machine learning utilities.
Streamlit: For creating the web interface to display predictions interactively.
joblib: For saving and loading the trained machine learning model.
Machine Learning:

Random Forest Classifier: A robust model used to predict bus crowdedness based on features of the dataset available
Deployment:

Streamlit: Used to deploy the machine learning model as a web application where users can receive predictions.
