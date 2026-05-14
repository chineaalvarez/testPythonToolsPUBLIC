import json
import os
import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Load locations from JSON file
script_dir = os.path.dirname(os.path.abspath(__file__))
locations_file = os.path.join(script_dir, 'locations.json')
with open(locations_file) as f:
    locations = json.load(f)

if not locations:
    print("No locations found in locations.json")
    exit()

print("Available locations:")
for i, loc in enumerate(locations, 1):
    print(f"{i}. {loc['name']}")

while True:
    try:
        choice = int(input("Select a location by number: "))
        if 1 <= choice <= len(locations):
            selected_loc = locations[choice - 1]
            break
        else:
            print(f"Invalid choice. Please enter a number between 1 and {len(locations)}")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": selected_loc["latitude"],
    "longitude": selected_loc["longitude"],
    "hourly": "temperature_2m",
    "past_days": 0,
    "forecast_days": 7,
}
responses = openmeteo.weather_api(url, params = params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"\nWeather for {selected_loc['name']}")
print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation: {response.Elevation()} m asl")
print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
    start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
    end =  pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
    freq = pd.Timedelta(seconds = hourly.Interval()),
    inclusive = "left"
)}

hourly_data["temperature_2m"] = hourly_temperature_2m

hourly_dataframe = pd.DataFrame(data = hourly_data)
print("\nHourly data\n", hourly_dataframe)