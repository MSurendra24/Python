unames=['nm','nt','os2','ce','java']
# map_obj=map(lambda x:x.upper(),unames)
# print(list(map_obj))
# print(list(map(lambda x:x.upper(),unames)))
# print(list(x.upper() for x in unames))  # list comprehension
for uname in unames:
    unames.append(uname.upper())
print(unames)
