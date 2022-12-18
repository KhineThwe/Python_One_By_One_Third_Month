import json
with open('states.json') as f:
    data = json.load(f)
    print(type(data))

for state in data['states']:
    name = state['name']
    abbre = state['abbreviation']
    area_codes = state['area_codes']
    if abbre == "AL":
        print("We found AL")
    print(name," ",abbre," ",area_codes)


with open('new_states.json',"w") as f:
    json.dump(data,f,indent=2,sort_keys=True)
