employees=[
{'name':'nms','age':23,'salary':10000},
{'name':'rms','age':24,'salary':20000},
{'name':'sms','age':25,'salary':30000}]
i=0
while i<len(employees):
    if employees[i]['age']<=24:
        print(employees[i]['name'])
    i=i+1