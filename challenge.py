import streamlit as st
import requests

nasa_api = "DJXziUmmPgDohYjGljMXmJVd1QBa9kN9Rb8DabnK"

url = "https://api.nasa.gov/planetary/apod?"
params = {'api_key': nasa_api}
response = requests.get(url, params)
# response = requests.get(url=url2)

content = response.json()
title = content['title']
explanation = content['explanation']

# extract the picture (commented out so it wouldn't download it everytime)

img_url = content['url']
img_response = requests.get(img_url)

with open("image.png", "wb") as file:
    file.write(img_response.content)

# configure website
# st.set_page_config(layout="wide")
st.header(title)
st.image("image.png")

st.write(explanation)