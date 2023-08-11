
# Project: Automated Weather Alert System
"""
Description: This project automates the process of checking the weather forecast for a specific location and sending weather alerts via email or text message if certain weather conditions are met.
It uses an external weather API to retrieve weather data and sends notifications to users based on their preferences.

Steps:

Choose a weather API service (e.g., OpenWeatherMap) and obtain an API key.
Write a Python script to interact with the weather API to fetch weather data for a specific location.
Implement logic to check weather conditions and decide whether to trigger an alert.
Set up a notification system to send alerts to users (via email or text message).
Requirements:

Python (installed on your system)
An API key from the chosen weather API service.
Knowledge of working with APIs, sending notifications, and handling data in Python.
Example Code (using OpenWeatherMap API and SMTP email for notifications):
"""
import requests
import smtplib
from email.message import EmailMessage
import time

def get_weather_data(api_key, city, country):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{city},{country}",
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def send_weather_alert(receiver_email, weather_data):
    msg = EmailMessage()
    msg['Subject'] = f"Weather Alert: {weather_data['weather'][0]['description']}"
    msg['From'] = "your_sender_email@gmail.com"  # Replace with your sender email
    msg['To'] = receiver_email

    body = f"Current weather in {weather_data['name']}, {weather_data['sys']['country']}:\n"
    body += f"Temperature: {weather_data['main']['temp']}°C\n"
    body += f"Description: {weather_data['weather'][0]['description']}\n"

    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("your_sender_email@gmail.com", "your_sender_email_password")  # Replace with your sender email and password
        smtp.send_message(msg)

if __name__ == "__main__":
    api_key = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key
    city = "London"
    country = "GB"
    receiver_email = "your_receiver_email@gmail.com"  # Replace with your receiver email

    while True:
        weather_data = get_weather_data(api_key, city, country)

        # Check if weather conditions meet your alert criteria (e.g., temperature below a threshold)
        if weather_data['main']['temp'] < 10:
            send_weather_alert(receiver_email, weather_data)

        time.sleep(1800)  # Check the weather every 30 minutes