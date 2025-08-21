d1={}
emp={
    'eid':101,
    'ename':'nm',
    'esal':45000,
    'email':'nm@gmail.com'
    }
print(d1)
print(emp)
print(emp['eid'])
emp['ename']='nms'
print(emp)
emp['avail']=True
print(emp)
del emp['email']
print(emp)
del emp
print(emp)