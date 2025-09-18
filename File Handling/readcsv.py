import csv
fp1=open("emp.csv","r")
emp_data=csv.reader(fp1)
print(emp_data)
print(type(emp_data))
for emp in emp_data:
    # print(emp)
    # print(emp['ename'])  # TypeError: list indices must be integers or slices, not str
    print(emp[1])
fp1.close()