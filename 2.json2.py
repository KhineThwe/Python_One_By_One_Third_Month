#https://docs.python.org/3/library/json.html
#https://jsonlint.com/
import json
myJson = """{
"name":"khine",
"age" : 24,
"hobby":["coding","training","crypto"]
}
"""
#serialization ---> python data type တွေကနေ ပြီးတော့ json format
#dump / dumps
with open("jdataFile.json","w") as jsFile:
    json.dump(myJson,jsFile)
#dump ----> python obj,json file
