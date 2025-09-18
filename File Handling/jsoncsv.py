import json,csv
fp1=open("emp.json","r")
fp2=open("emp.csv","w",)
employees=json.load(fp1)
# print(employees)
# emp_data=csv.writer(fp2)
# print(emp_data)
new_employees=[]
for emp in employees:
    new_employees.append((emp['eid'],emp['ename']))
    # print(new_employees)
    cw=csv.writer(fp2)
    cw.writerows('eid','ename')
    cw.writerows(new_employees)
    print("Data written to csv file")
fp1.close()