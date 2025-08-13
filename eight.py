a=(12,34,56,78,90)
print(a)
print(a[3])
print(a[1:4])
print(a[0:4:3])
print(a[0:5:2])
print(a)
print(a[-1])
# a[2]=100  # This will raise an error since tuples are immutable
# print(a)
# del a[1]  # This will also raise an error since tuples are immutable
# a.clear()  # This will also raise an error since tuples are immutable
# print(a)  # This will also raise an error since tuples are immutable
# print(a[5])  # IndexError: tuple index out of range
a[3]='nm'
print(a)