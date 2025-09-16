import json
fp=open("emp.json","r")
employee=json.load(fp)
print(employee)
for emp in employee:
    # print(emp['eid'])
    if emp['avail']==True:
        print(emp['ename'])