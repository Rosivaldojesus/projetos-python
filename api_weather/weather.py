from cProfile import label
import tkinter as tk
import requests
import time


api = "https://api.openweathermap.org/data/2.5/weather?lat=-23.532881&lon=-46.792004&appid=755e641fcb8e7e9ad9f20f464623dd98"
json_data = requests.get(api).json()
condition = json_data['weather'][0]['main']
temp = int(json_data['main']['temp'] - 273.15)
min_temp = int(json_data['main']['temp_min'] - 273.15)
max_temp = int(json_data['main']['temp_max'] - 273.15)
pressure = json_data['main']['pressure']
humidity = json_data['main']['humidity']
wind = json_data['wind']['speed']
wind = wind * 3.6 # Convertedo m/s por km/h

sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] ))
sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] ))





print(f'temperatura: {temp} ºC')
print(f'temperatura mínima: {min_temp} ºC')
print(f'temperatura náxima: {max_temp} ºC')
print(f'Pressão atmosférica: {pressure} hPa')
print(f'Humidade: {humidity}%')
print(f'Vento: {wind} km/h')

print(f'sunrise: {sunrise}')
print(f'sunrise: {sunrise}')





from tkinter import *
from tkinter import ttk


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text=temp).grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

root.mainloop()


