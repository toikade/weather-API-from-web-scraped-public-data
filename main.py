import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

base_url = "https://forecast.weather.gov/"
page = requests.get(base_url+"MapClick.php?lon=-80.2269744873047&lat=26.01918730099294#.Y2wE2ffMLIU")
print(page.status_code)
soup = BeautifulSoup(page.content, 'html.parser')

parent_container = soup.find_all(id="seven-day-forecast")[0]
forecast_list_items = parent_container.select(".tombstone-container")

# periods of the day
periods = [i.select(".period-name")[0].get_text() for i in forecast_list_items]
# a description of the weather
descs = [i.select("img")[0]["alt"] for i in forecast_list_items]
# get the description image
desc_image = [i.select("img")[0]["src"] for i in forecast_list_items]
# temperatures in deg. Fahrenheit
temp = [i.select(".temp")[0].get_text() for i in forecast_list_items]
# A short description of the weather
short_descs = [i.select(".short-desc")[0].get_text() for i in forecast_list_items]


# print(periods)
# print(descs)
# print(temp)
# print(short_descs)

weather = pd.DataFrame({
    "period":periods,
    "desc":descs,
    "temp":temp,
    "short_descs":short_descs,
    "desc_image":desc_image
})

num_temp = weather['temp'].str.extract("(\d+)", expand=False)
weather['num_temp_fahr'] = num_temp.astype('int')

# check if its day or night
is_day = weather["temp"].str.contains("High")
weather["is_day"] = is_day

# drop the weather column
weather.drop("temp", axis=1, inplace=True)

# format the data to JSON
weather_json = json.loads(weather.to_json(orient = 'records'))

# pretty print
formatted_weather_json = json.dumps(weather_json, indent=2)
print(formatted_weather_json)

