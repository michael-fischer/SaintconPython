import requests

weather_url = "https://api.weather.gov/gridpoints/SLC/104,150"

headers = {
    'accept': "application/json",
    }

response = requests.request("GET", weather_url, headers=headers)
data = response.json()

# print temperatures
for temp in data['properties']['temperature']['values']:
    print(temp['validTime'], temp['value'])




# # Save the data for posterity
# with open('data.json', 'w') as f:
#     json.dump(data, f, indent=4)

# with open('data.json') as f:
#     data = json.load(f)    

# import json
# https://api.weather.gov/points/{latitude},{longitude}
# https://api.weather.gov/gridpoints/SLC/40.234672517180776,-111.66257172827694

# office_url = "https://api.weather.gov/points/40.234672517180776,-111.66257172827694"
# response = requests.request("GET", office_url, headers=headers)
# print(response.text)
