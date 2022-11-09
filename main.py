import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lon=-80.2269744873047&lat=26.01918730099294#.Y2wE2ffMLIU")
print(page.status_code)
soup = BeautifulSoup(page.content, 'html.parser')

parent_container = soup.find_all(id="seven-day-forecast")[0]
forecast_list_items = parent_container.select(".tombstone-container .period-name")
eight_list_items = forecast_list_items[1:]
periods = [i.get_text() for i in eight_list_items]


print(len(periods))
print(periods)