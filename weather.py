import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.set_page_config(
    layout="wide",  
    page_title="Wearher Forecast", 
    page_icon="https://media.istockphoto.com/id/1007768414/photo/blue-sky-with-bright-sun-and-clouds.jpg?s=612x612&w=0&k=20&c=MGd2-v42lNF7Ie6TtsYoKnohdCfOPFSPQt5XOz4uOy4=", 
    initial_sidebar_state="auto" 
)



def fetch_weather(city):
    url = f"https://www.weather-forecast.com/locations/{city}/forecasts/latest"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    temperature = soup.find("span", {"class": "temp"}).text
    condition = soup.find("span", {"class": "phrase"}).text
    return temperature, condition

# Define cities
cities = {
    "Karachi": "karachi",
    "Lahore": "lahore",
    "Islamabad": "islamabad",
    "Peshawar": "peshawar",
    "Quetta": "quetta"
}




st.markdown("<div style='height:10px; border-radius:50px; background-color: blue; border: none;'></div>", unsafe_allow_html=True)  
st.markdown(
    """
    
    <h1 style="text-align: center;">wheather forcasting website</h1>
    """,
    unsafe_allow_html=True
)
st.markdown("<div style='height:10px;  border-radius:50px; background-color: blue; border: none;'></div>", unsafe_allow_html=True)  


col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://media.istockphoto.com/id/1007768414/photo/blue-sky-with-bright-sun-and-clouds.jpg?s=612x612&w=0&k=20&c=MGd2-v42lNF7Ie6TtsYoKnohdCfOPFSPQt5XOz4uOy4=")
with col2:
    selected_cities = st.multiselect("Select cities".upper(), list(cities.keys()))
    st.markdown("<div style='height:8px; margin-bottom:20px; border-radius:50px; background-color: blue; border: none;'></div>", unsafe_allow_html=True)  
    st.markdown("<div style='height:6px; margin-bottom:20px; border-radius:50px; background-color: blue; border: none;'></div>", unsafe_allow_html=True)  
    st.markdown("<div style='height:4px; margin-bottom:20px; border-radius:50px; background-color: blue; border: none;'></div>", unsafe_allow_html=True)  
    st.markdown("<div style='height:3px; margin-bottom:20px; border-radius:50px; background-color: blue; border: none;'></div>", unsafe_allow_html=True)  
    st.markdown("<div style='height:2px; margin-bottom:20px; border-radius:50px; background-color: blue; border: none;'></div>", unsafe_allow_html=True)  
    st.markdown("<div style='height:1px; margin-bottom:20px; border-radius:50px; background-color: blue; border: none;'></div>", unsafe_allow_html=True)  
with col3:
    search_city = st.text_input(" Search by city name ".upper())
                               
    st.markdown("<div style='height:8px; margin-bottom:20px; border-radius:50px; background-color: blue; border: none;'></div>", unsafe_allow_html=True)  
    st.markdown("<div style='height:6px; margin-bottom:20px; border-radius:50px; background-color: blue; border: none;'></div>", unsafe_allow_html=True)  
    st.markdown("<div style='height:4px; margin-bottom:20px; border-radius:50px; background-color: blue; border: none;'></div>", unsafe_allow_html=True)  
    st.markdown("<div style='height:3px; margin-bottom:20px; border-radius:50px; background-color: blue; border: none;'></div>", unsafe_allow_html=True)  
    st.markdown("<div style='height:2px; margin-bottom:20px; border-radius:50px; background-color: blue; border: none;'></div>", unsafe_allow_html=True)  
    st.markdown("<div style='height:1px; margin-bottom:20px; border-radius:50px; background-color: blue; border: none;'></div>", unsafe_allow_html=True)  
      
    
# list for weather data
weather_data = []

# Fetch weather for selected cities
for selected_city in selected_cities:
    city_code = cities[selected_city]
    temperature, condition = fetch_weather(city_code)
    weather_data.append({"City": selected_city, "Temperature": temperature, "Condition": condition})

# Fetch weather for searched city
if search_city:
    city_code = search_city.lower().replace(" ", "-")
    try:
        temperature, condition = fetch_weather(city_code)
        weather_data.append({"City": search_city.title(), "Temperature": temperature, "Condition": condition})
    except:
        st.write(f"Weather data for {search_city.title()} is not available.")

# Display the data in a table if available
if weather_data:
    df = pd.DataFrame(weather_data, columns=["City", "Temperature", "Condition"])

    st.markdown("<div style='height:10px; margin-bottom:20px; border-radius:1px; background-color: red; border: none;'></div>", unsafe_allow_html=True)  
    
    st.table(df.set_index('City'))

    st.markdown("<div style='height:10px; margin-bottom:20px; border-radius:50px; background-color: blue; border: none;'></div>", unsafe_allow_html=True)  
