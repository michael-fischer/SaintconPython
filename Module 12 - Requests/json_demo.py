import requests
import json

weather_url = "https://api.weather.gov/gridpoints/SLC/104,150"

headers = {
    'accept': "application/json",
    }

response = requests.request("GET", weather_url, headers=headers)
data = response.json()

# Here is the code that wrote out the data file
with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

# The following this the same as what we saw in module 9.
# It is included to show that the code would be the same 
# regardless of the source.

# print temperatures
for temp in data['properties']['temperature']['values']:
    print(temp['validTime'], temp['value'])

# Partial Output
# 2021-10-24T07:00:00+00:00/PT3H 7.777777777777778
# 2021-10-24T10:00:00+00:00/PT2H 7.222222222222222
# 2021-10-24T12:00:00+00:00/PT1H 6.666666666666667
# 2021-10-24T13:00:00+00:00/PT2H 6.111111111111111
# 2021-10-24T15:00:00+00:00/PT1H 6.666666666666667
# 2021-10-24T16:00:00+00:00/PT1H 7.777777777777778
# 2021-10-24T17:00:00+00:00/PT1H 9.444444444444445
# 2021-10-24T18:00:00+00:00/PT1H 11.11111111111111
# 2021-10-24T19:00:00+00:00/PT1H 12.222222222222221
# 2021-10-24T20:00:00+00:00/PT1H 12.777777777777779
# 2021-10-24T21:00:00+00:00/PT4H 13.333333333333334