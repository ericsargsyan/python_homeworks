import os
import json
import yaml

path = os.path.join(os.getcwd(),"sample_json.json")

with open(path,"r") as file_json:
    data = json.load(file_json)
final_list = []
# print(data["items"])
for dict_ in data['items']:
    new_data = {}
    if dict_['age'] > 36:
        new_data['name'] = dict_['name']
        new_data["age"] = dict_["age"]
        final_list.append(new_data)
result = {"items":final_list}  
print(result)

with open("new_yaml.yml", "w") as file:
    yaml.dump(result, file, indent=4)
# print(type(data))
