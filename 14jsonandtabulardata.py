import json
import pandas as pd

data = '''
{
    "cities": [
        {"city": "Kochi", "weather": {"temp": 30, "humidity": 70}},
        {"city": "Delhi", "weather": {"temp": 35, "humidity": 60}},
        {"city": "Mumbai", "weather": {"temp": 32, "humidity": 65}}
    ]
}
'''

weather = json.loads(data)

df = pd.json_normalize(weather["cities"])

df = df.rename(columns={
    "weather.temp": "Temperature",
    "weather.humidity": "Humidity"
})

print(df)
print("\nAverage Temperature:", df["Temperature"].mean())
print("Average Humidity:", df["Humidity"].mean())