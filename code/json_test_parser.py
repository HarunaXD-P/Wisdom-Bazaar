import json
import json_parser_0

data = json_parser_0.json_parser('pengjunlee.json')

print(data)

name_0 = data['name']
age_0 = data['age']
vip_0 = data['vip']
address_0 = data['address']
print("info about convert 1")
print(name_0)
print(age_0)
print(vip_0)
print(address_0)
print("make dict")
json_parser_0.make_json(name_0, age_0, vip_0, address_0)