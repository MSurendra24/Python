enames=['nm','nt','os2','ce','java']
def changecase(name):
    return name.upper()
enames=list(map(changecase,enames))
print(enames)