import json
employees_str='''
[
    {"eid":101,"ename":"Rahul","avail":true},
    {"eid":102,"ename":"Sonia","avail":false},
    {"eid":103,"ename":"Priyanka","avail":true},
    {"eid":104,"ename":"Modi","avail":true}
]
'''
employees=json.loads(employees_str)
print(employees)
for emp in employees:
    for key in emp:
        print(key,":",emp[key])
