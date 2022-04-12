from cProfile import label
import tkinter as tk
import requests
import time


def getWeather(canvas):
    city = textfield.get()
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








    label.config(text = temp)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()