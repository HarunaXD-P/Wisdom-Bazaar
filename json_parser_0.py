import json

# json_parser
# opens the recieved json file 
# returns a python dict
def json_parser(json_name):
    with open(json_name, 'r', encoding = 'utf-8') as test_0_front:
        json_0 = json.load(test_0_front)
    return json_0

# make_json
# take the input data to form a json file
def make_json(x, y, z, t):
    temp_dict = dict(name = x, age = y, vip = z, address = t)
    json_packer(temp_dict)


# json_packer
# take the python dict from make_json as input
# output a json file and saves it 
def json_packer(python_dict):
    with open('target.json', 'w', encoding = 'utf-8') as test_out_0:
        json.dump(python_dict, test_out_0.write, ensure_ascii=False, indent=4)
     
