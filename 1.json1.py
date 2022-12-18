#json
#HTML,Plaintext,XML,Json
#XML
#json --> python dictionary
import json
myJson = """{
"name":"khine",
"age" : 24,
"hobby":["coding","training","crypto"]
}
"""
data = json.loads(myJson)
#convert json data to python
print(data)
print(type(data))#python dictionary
for key,value in data.items():
    print(value)
print(data['name'])
