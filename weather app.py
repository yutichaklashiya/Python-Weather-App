import urllib.request
import json
import tkinter as tk
from tkinter import messagebox


API_KEY = '9d2c32dfef90e02a1f42ebdfac560c08'

def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q=Surat&appid=9d2c32dfef90e02a1f42ebdfac560c08&units=metric"
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            return data
    except Exception as e:
        print("⚠️ ERROR:", e)  
        return None

def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    data = get_weather(city)
    
    if data is None:
        messagebox.showerror("Error", "Unable to fetch data. Check your internet or API key.")
        return

    print("API Response:", data) 

    if data.get("cod") == 200:
        name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].title()
        result = f"Weather in {name}, {country}:\n{temp}°C\n{desc}"
        result_label.config(text=result)
    else:
        messagebox.showerror("Error", f"City not found or invalid: {data.get('message', 'Unknown error')}")


root = tk.Tk()
root.title("Simple Weather App")
root.geometry("320x280")

tk.Label(root, text="Enter City Name:", font=("Helvetica", 12)).pack(pady=10)
city_entry = tk.Entry(root, font=("Helvetica", 12))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=show_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
result_label.pack(pady=20)

root.mainloop()
