import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data.get("cod") != 200:
        print("City not found or error occurred.")
        return
    print(f"Weather in {city}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Description: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")

def main():
    api_key = "OPENWEATHER_API_KEY"
    city = input("Enter city name: ")
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
