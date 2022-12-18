import json
import requests

url = "https://api.punkapi.com/v2/beers"
r = requests.get(url)
data = json.loads(r.text)#list
# print(data)
# print(data[0]['name'])
# print(data[0]['tagline'])
# print(data[0]['id'])

beer_list = []
for beer in data:
    name = beer['name']
    tagline = beer['tagline']
    abv = beer['abv']
    # print(name,tagline,abv)
    beer_items = {
        "name":name,
        "tagline":tagline,
        "abv":abv
    }
    beer_list.append(beer_items)
print(beer_list)

