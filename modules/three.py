employees=[
{'name':'nms','age':23,'salary':10000},
{'name':'rms','age':24,'salary':20000},
{'name':'sms','age':25,'salary':30000}]
for emp in employees:
 if emp['age']<=24:
    print(emp['name'])