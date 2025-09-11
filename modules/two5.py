enames=['nm','nt','os2','ce','java']
# enames=list(filter(lambda name: len(name)>2,enames))
# print(enames)
def checkname(name):
    return name.startswith('n')
enames=list(filter(checkname,enames))
print(enames)