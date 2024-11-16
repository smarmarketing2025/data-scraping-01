import requests
from bs4 import BeautifulSoup
import streamlit as st

# Scraping URL
url = "https://www.aljazeera.com/where/pakistan/"
web = requests.get(url)
soup = BeautifulSoup(web.content, 'html.parser')


# Scraping titles
titles = soup.find_all("h3", class_="gc__title")
title_list = [title.text.strip() for title in titles]

# Scraping dates
dates = soup.find_all("div", class_="gc__date gc__date--published")
date_list = [date.text.strip() for date in dates]

# Streamlit title
st.title("PAKISTAN NEWS")
st.image("https://www.shutterstock.com/shutterstock/photos/2421539967/display_1500/stock-photo-wide-format-breaking-news-live-broadcast-graphic-on-digital-world-map-d-rendering-2421539967.jpg")

# Loop through each article and display in columns
for i in range(len(title_list)):
    # Create three columns
    col2, col3 = st.columns([3, 2])
    
    # Display the title in the second column
    with col2:
        st.subheader(title_list[i])
    
    # Display the date in the third column
    with col3:
        st.caption(date_list[i])
        
    # Divider line between articles
    st.write("---")