import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lon=-80.2269744873047&lat=26.01918730099294#.Y2wE2ffMLIU")
print(page.status_code)
soup = BeautifulSoup(page.content, 'html.parser')

parent_container = soup.find_all(id="seven-day-forecast")[0]
forecast_list_items = parent_container.select(".tombstone-container")

periods = [i.select(".period-name")[0].get_text() for i in forecast_list_items]
descs = [i.select("img")[0]["alt"] for i in forecast_list_items]
temp = [i.select(".temp")[0].get_text() for i in forecast_list_items]
short_descs = [i.select(".short-desc")[0].get_text() for i in forecast_list_items]


print(len(forecast_list_items))
print(forecast_list_items)
print('+'*100)
print(short_descs)