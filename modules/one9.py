numbers=[10,13,20,25,30,37,40,49,50,51]
def iseven(num):
    return num%2==0
filter_obj=filter(iseven,numbers)
print(list(filter_obj))