import json
person_list = []
with open('json_fake_data.json') as f:
    data = json.load(f)
    # print(data[0]['name'])
    # print(data[0]['company'])
    # print(data[0]['email'])

for item in data:
    name = item['name']
    email = item['email']
    balance = item['balance']
    # print(name," ",email," ",balance)
    person = {
        'Username':name,
        'email':email,
        'balance':balance
    }#dict
    person_list.append(person)
    print(person_list)


# with open('new_states.json',"w") as f:
#     json.dump(data,f,indent=2,sort_keys=True)
