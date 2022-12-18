import json
import requests
from random import randint
food_choice = input("Please enter your choice: ")
url = f"https://api.punkapi.com/v2/beers?food={food_choice}"
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
# print(beer_list)
value = randint(0,len(beer_list))#0,25 value =6
print(len(beer_list))
print(value)
try_this = beer_list[value]#beer_list[6] = AB:05
print(try_this)
try_name = try_this['name']
try_tagline = try_this['tagline']
try_abv = try_this['abv']
print(f"You should try {try_name} , {try_tagline},{try_abv}")


