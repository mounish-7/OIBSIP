import requests

def get_weather(city):
    api_key = "1cc540ed8b5d01517bfa6437b1238c4d"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        print(f"Temperature in {city}: {temp}°C")
        print(f"Weather: {weather}")
    else:
        print("City not found or API error.")
        print("Debug Info:", response.text)

# Main
city = input("Enter city name: ").strip()
get_weather(city)