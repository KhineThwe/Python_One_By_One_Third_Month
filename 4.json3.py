import json
with open("newjdataFile.json") as jsFile:
    data = json.load(jsFile)

for i in data['cars']:
    print(i)


with open("newjdataFile1.json","w") as JsFile:
    json.dump(data,JsFile,indent=2,sort_keys=True)
