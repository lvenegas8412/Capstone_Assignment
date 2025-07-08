#WEATHER HISTORY TRACKER


import requests
from config import weather_api_url, api_key
import tkinter as tk
import os


def get_data(entry, temp_label, cond_label, precip_label, max_temp_label, rain_label, snow_label):
    city_name = entry.get()
    
    if city_name != '':
        try:

            #Call OpenWeather for data
            url = weather_api_url + '?q=' + city_name + '&appid=' + api_key + '&units=imperial'
            data = requests.get(url)
            info = data.json()
            if data.status_code !=200:
                raise ValueError("Invalid city")
            
            #ID info I want to bring from OpenWeather
            temp= info['main']['temp']
            description = info['weather'][0]['description']
            wind_speed = info['wind']['speed']
            max_temp = info['main']['temp_max']
            # rain = info['rain']['1h']
            # snow = info['snow']['1h']
            rain = info.get('rain', {}).get('1h', 0.0)
            rain_in = rain / 25.4
            snow = info.get('snow', {}).get('1h', 0.0)
            snow_in = snow / 25.4


            #Reset the Weather Labels with updated information
            temp_label.config(text="Current Temperature: " + str(temp)+ ' °F') 
            cond_label.config(text="Conditions: " + description)
            precip_label.config(text="Wind Speed: " + str(round(wind_speed)) + 'mph')
            max_temp_label.config(text='Max Temp: ' + str(max_temp)+ ' °F')
            rain_label.config(text=f"Rain: {rain_in:.2f} in/hr")
            snow_label.config(text=f"Snow: {snow_in:.2f} in/hr")
            with open("data.txt", "a") as f: #CHANGED TO OPEN W/ "A" TO RECORD ALL ENRIES
                f.write(city_name + "," + str(temp) + "," + description + "," + str(wind_speed) + '\n')   

        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END,'ENTER A VALID CITY')
            entry.config(foreground='red')                 
            entry.config(foreground='black')
            print("Error:", e) 
    else:
        print("No city")

