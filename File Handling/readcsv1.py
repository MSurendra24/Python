import csv
fp=open("emp.csv",'r')
emp_data=csv.reader(fp)
print(emp_data)
for emp in emp_data:
    print(emp[1])