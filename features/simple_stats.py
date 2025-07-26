#WEATHER HISTORY TRACKER

import requests
from config import weather_api_url, api_key
import tkinter as tk
from datetime import datetime
import pytz
from PIL import Image, ImageTk 
from tkinter import messagebox


def get_data(entry, temp_label, cond_label, wind_label, max_temp_label, rain_label, snow_label, date_label, weather_icon_label):
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
            rain = info.get('rain', {}).get('1h', 0.0)
            #convert mm/hr into inches/hr
            rain_in = rain / 25.4
            snow = info.get('snow', {}).get('1h', 0.0)
            #convert mm/hr into inches/hr
            snow_in = snow / 25.4
            #get date
            utc_timestamp = info['dt']
            utc_time = datetime.utcfromtimestamp(utc_timestamp)
            pst_timezone = pytz.timezone('US/Pacific')
            pst_time = utc_time.replace(tzinfo=pytz.utc).astimezone(pst_timezone)
            icon_id = info['weather'][0]['icon'] 
            icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"



           
            
            #Update labels
            date_label.config(text=f'Date & Time: {pst_time.strftime('%m-%d-%Y / %I:%M %p')}')
            temp_label.config(text="Current Temperature: " + str(temp)+ ' °F') 
            cond_label.config(text="Conditions: " + description)
            wind_label.config(text="Wind Speed: " + str(round(wind_speed)) + 'mph')
            max_temp_label.config(text='Max Temp: ' + str(max_temp)+ ' °F')
            rain_label.config(text=f"Rain: {rain_in:.2f} in/hr")
            snow_label.config(text=f"Snow: {snow_in:.2f} in/hr")
            img = Image.open(requests.get(icon_url, stream=True).raw)
            img = img.resize((200, 200))  
            photo = ImageTk.PhotoImage(img)             
            weather_icon_label.config(image=photo)
            weather_icon_label.image = photo            
            with open("data.txt", "a") as f: 
                f.write(city_name + ", " + str(temp) + ", " + description + ", " + str(wind_speed) + ", " + pst_time.strftime('%m-%d-%Y / %I:%M %p') +'\n')   

        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END,'ENTER A VALID CITY')
            entry.config(foreground='red')                 
            entry.config(foreground='black')
            print("Error:", e)
            messagebox.showerror("Invalid Input", str(e))
            
    else:
        print("No city")

