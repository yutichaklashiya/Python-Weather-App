import urllib.request
import json
import tkinter as tk
from tkinter import messagebox

API_KEY = '9d2c32dfef90e02a1f42ebdfac560c08'

def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            return data
    except:
        return None

def show_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Error", "Enter city name")
        return

    data = get_weather(city)

    if data and data.get("cod") == 200:
        name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"].title()

        result = f"{name}, {country}\n\n🌡 {temp}°C\nFeels: {feels}°C\n💧 {humidity}%\n☁ {desc}"

        result_label.config(text=result)

    else:
        messagebox.showerror("Error", "City not found")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x420")
root.configure(bg="#1e1e2f")

tk.Label(root,text="Weather App",font=("Segoe UI",20,"bold"),bg="#1e1e2f",fg="white").pack(pady=15)

city_entry = tk.Entry(root,font=("Segoe UI",14),justify="center")
city_entry.pack(pady=10,ipady=5)

tk.Button(root,text="Get Weather",font=("Segoe UI",12,"bold"),
bg="#4CAF50",fg="white",width=18,command=show_weather).pack(pady=15)

result_label = tk.Label(root,text="",font=("Segoe UI",13),
bg="#1e1e2f",fg="white",justify="center")
result_label.pack(pady=20)

tk.Label(root,text="Made with Python ❤️",bg="#1e1e2f",fg="gray").pack(side="bottom",pady=10)

root.mainloop()
