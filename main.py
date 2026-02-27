import requests
from twilio.rest import Client
import os

API_END_POINT='https://api.openweathermap.org/data/2.5/forecast'
API_KEY=os.getenv("OWM_KEY")

ACCOUNT_SID=os.environ.get("TWILO_SID")
AUTH_TOKEN=os.environ.get("TWILO_KEY")


MY_LAT=42.04593336913892
MY_LON=87.85122419411847
# MY_LON=-81.1053764

parameter={
    "lat":MY_LAT,
    "lon":MY_LON,
    "appid":API_KEY,
    "cnt":6
}

response=requests.get(API_END_POINT,parameter)
response.raise_for_status()
data=response.json()

day_time=[]
will_rain=False
for each in data["list"]:
    day_time=each['dt_txt'].split(" ")   
    if each["weather"][0]['id']<700:
        will_rain=True
        break
        # print(f'On {day_time[0]} at around {day_time[1]} , so you will need an umbrella')
if will_rain:
    print('It will rain today')
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
    from_=os.environ.get("MY_TWILONUM"),
    body="It's going to rain today. Remember to bring an umbrella ☂️",
    to=os.environ.get("MY_WHATSAPP")
    )
    print(message.status)      
else:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
    from_="whatsapp:+14155238886",
    body="It will not rain today 🌞",
    to="whatsapp:+12248661559"
    )    

    print(message.status)      


