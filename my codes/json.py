# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 09:47:36 2025

@author: Surface
"""
import json
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json=json.dumps(data)
print(data_json)
with open('data.json','w') as file:
    file.write(data_json)
with open('data.json') as file:
    data2=json.load(file)
student_json = """{"name":"Hasan","l_name":"Husanov","b_year":2000}"""
student=json.loads(student_json)
name=student['name']
l_name=student["l_name"]
print(f"{name} {l_name}")

with open('info.json','w') as f:
    f.write(data_json+'\n')
    f.write(student_json+'\n')
    
with open('students.json') as f:
    data=json.load(f)
#for item in data['student']:
#    print(f"{item['name']} {item['lastname']}. Faculty: {item['faculty']}")

with open('api-result.json') as file:
    result_json=json.load(file)
    
print(result_json['query']['pages']['13801']['title'])
print(result_json['query']['pages']['13801']['extract'])
