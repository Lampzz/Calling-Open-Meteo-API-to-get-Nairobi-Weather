import requests
import pandas as pd

def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": -1.29,
        "longitude": 36.82,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "Africa/Nairobi"
    }
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def parse_weather(data):
    days = data["daily"]["time"]
    max_temps = data["daily"]["temperature_2m_max"]
    min_temps = data["daily"]["temperature_2m_min"]

    return pd.DataFrame({
        "Date": days,
        "Temp Max": max_temps,
        "Temp Min": min_temps
    })

def main():
    data = fetch_weather()
    df = parse_weather(data)
    df.to_csv("C:\\Users\\MUKUNA\\Downloads\\Telegram Desktop\\nairobi_weather.csv", index=False)
    print("Saved nairobi_weather.csv")

if __name__ == "__main__":
    main()

