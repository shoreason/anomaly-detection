from bs4 import BeautifulSoup
import requests
import csv

url = 'https://weather.com/weather/hourbyhour/l/45240:4:US'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')



weather_table = soup.find(class_='twc-table')



time_tags = weather_table.select(".hourly-time .dsx-date")




time = [tt.get_text() for tt in time_tags]
print(time)


temp_tags = weather_table.select(".temp")

temp = [tempt.get_text() for tempt in temp_tags]


new_temp = temp[1:]
print(new_temp)

newlines = zip(time, new_temp)

with open('weather.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(newlines)
