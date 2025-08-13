one=[12,34,56,78,90]
print(one)
print(one[3])
print(one[1:4])
print(one[0:4:3])
print(one[-1])
one[2]=100
print(one)
del one[1]
print(one)
# del one
# This will raise an error since 'one' is deleted
one.clear()
print(one)# This will also raise an error since 'one' is deleted
# print(one[5]) # IndexError: list index out of range

two=[]
three=[12,30.5,'nm',10+10J,True,{}, (1,2,3), {1,2,3}, None]
print(two)
print(three)
print(three[2])
print(three[3])
print(three[1:5])
