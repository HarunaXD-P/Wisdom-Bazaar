import json
 
data = {
    'name': 'pengjunlee',
    'age': 32,
    'vip': True,
    'address': {'province': 'GuangDong', 'city': 'ShenZhen'}
}

name_0 = data['name']
age_0 = data['age']
vip_0 = data['vip']
address_0 = data['address']
print("info about convert 1")
print(name_0)
print(age_0)
print(vip_0)
print(address_0)
# 将 Python 字典类型转换为 JSON 对象
json_str = json.dumps(data)
print(json_str) # 结果 {"name": "pengjunlee", "age": 32, "vip": true, "address": {"province": "GuangDong", "city": "ShenZhen"}}
 
# 将 JSON 对象类型转换为 Python 字典
user_dic = json.loads(json_str)
print(user_dic['address']) # 结果 {'province': 'GuangDong', 'city': 'ShenZhen'}
 
# 将 Python 字典直接输出到文件
with open('pengjunlee.json', 'w', encoding='utf-8') as f:
    json.dump(user_dic, f, ensure_ascii=False, indent=4)
 
# 将类文件对象中的JSON字符串直接转换成 Python 字典
with open('pengjunlee.json', 'r', encoding='utf-8') as f:
    ret_dic = json.load(f)
    print(type(ret_dic)) # 结果 <class 'dict'>
    print(ret_dic['name']) # 结果 pengjunlee