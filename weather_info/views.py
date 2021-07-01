from django.http import HttpRequest
from django.shortcuts import render
import requests


def get_weather_data(request: HttpRequest):
    api_key = "YOUR_API From https://openweathermap.org/"
    search_query = request.GET.get("location")

    if search_query:
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + search_query + "&units=metric&appid=" + api_key
        print(url)
        response = requests.get(url)
    else:
        response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + "pabna" + "&units=metric&appid=" + api_key)

    response = response.json()
    if response["cod"] == 200:
        temperature = response["main"]["temp"]
        air_pressure = str(float(response["main"]["pressure"])*0.75)
        wind_speed = response["wind"]["speed"]
        humidity = response["main"]["humidity"]
        city_name = response["name"]
        context = {
            "city_name": city_name,
            "temp": temperature,
            "pressure": air_pressure,
            "wind": wind_speed,
            "humidity": humidity
        }
    else:
        try:
            context = {"message": response["message"]}
        except KeyError:
            context = {"message": "Something Went Wrong"}
    return render(request, "index.html", context)
