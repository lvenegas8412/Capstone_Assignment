#Weather History Tracker
from  gui_window import entry
import requests

def get_data():
    city_name = entry
    if city_name != '':
        try:
            url = weather_api_url + '?q=' + city_name + '&appid=' + api_key + '&units=imperial'
            data = requests.get(url)
            info = data.json
            temp= info['main']['temp']
            description = info['weather'][0]['description']
            precipitation = info['main']['precipitation']
            temp_label.config(text="Temperature: " + str(temp)+ ' °F') #ADDED °F FOR READABILITY
            cond_label.config(text="Conditions: " + description) #CHANGED DESCRIP TO CONDITIONS, MORE READER FRIENDLY
            precip_label.config(text="Precipitation: " + str(precipitation) + "%") #ADDED % FOR READABILITY
            with open("data.txt", "a") as f: #CHANGED TO OPEN W/ "A" TO RECORD ALL ENRIES
                f.write(city_name + "," + str(temp) + "," + description + "," + str(humidity) + '\n')   
        except: