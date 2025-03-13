import json
import requests
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

url = f"https://api.openweathermap.org/data/2.5/weather?units=metric&lang=ru&lat={50.799393}&lon={42.013846}&appid={os.getenv("OPENWEATHER_KEY")}"
response = requests.post(url)
if response.status_code == 200:
    data = json.loads(response.text)
    print(f"Погода в городе {data["name"]} сегодня:")
    
    print(f"Температура: {data["main"]["temp"]}°C \n" + 
          f"Влажность: {data["main"]["humidity"]}% \n" + 
          f"Давление: {data["main"]["grnd_level"]}гПа \n" + 
          f"Облачность: {data["clouds"]["all"]}% \n")
