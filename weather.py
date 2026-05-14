import requests

def get_weather(city: str, api_key: str) -> dict:
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "ru"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            "city": data.get("name"),
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "humidity": data["main"]["humidity"]
        }
    return None

if __name__ == "__main__":
    API_KEY = "7cf22bb257edeefb648f06363b4848b9"
    city_input = input("Введите название города: ").strip()
    weather = get_weather(city_input, API_KEY)

    if weather:
        print(f"\nГород: {weather['city']}")
        print(f"Температура: {weather['temp']}°C")
        print(f"Описание: {weather['description']}")
    else:
        print("Ошибка получения данных.")