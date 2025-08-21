employees=[{"eid":1,"ename":"Maurizia","gender":"Female"},
{"eid":2,"ename":"Melisse","gender":"Female"},
{"eid":3,"ename":"Ashton","gender":"Male"},
{"eid":4,"ename":"Alia","gender":"Female"},
{"eid":5,"ename":"Karylin","gender":"Female"},
{"eid":6,"ename":"Foss","gender":"Male"},
{"eid":7,"ename":"Gwendolen","gender":"Female"},
{"eid":8,"ename":"Helaina","gender":"Female"},
{"eid":9,"ename":"Ryan","gender":"Male"},
{"eid":10,"ename":"Mathew","gender":"Male"}]
# for emp in employees:
#     print('emp names:',emp['ename'])
# for emp in employees:
#     if emp['gender']=='Male':
#         print("emp name",emp['ename'])
for emp in employees:
    if emp['eid']==1:
        print('Eid:',emp['ename'])