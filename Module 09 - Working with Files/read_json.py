import json

with open('data.json') as json_file:
    data = json.load(json_file)

# print temperatures
for temp in data['properties']['temperature']['values']:
    print(temp['validTime'], temp['value'])

