## import all libraries
## set the title and a box for input
##check if city exist find the data of weather from url and apistore result in data
## main = key that stores the useful information like temperature,humidity because we have json data it stores large datathat are not so useful
##description we take the first entry 
## now write these in markdown in streamlit like temp,humidity in percentage and description also
## if any city not found the statement else run
## finally run the streamlit app and get the result according to any city

import requests
import streamlit as st
import os
import dotenv

dotenv.load_dotenv()
key = os.getenv("API")

st.title("Weather App")
city = st.text_input("Enter the city name:")
if city:
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    response = requests.get(weather_url)
    data = response.json()

    if  data.get("main"):
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].title()
        icon = data["weather"][0]["icon"]

        st.write(f"**Temperature:** {temp}°C")
        st.write(f"**Humidity:** {humidity}%")
        st.write(f"**Weather:** {description}")  
else:
    st.error("City not found!")          