s2={10,20,30,40}
s2.remove(30)  # remove specified element from set object
print(s2)      #{40,10,20}
#s2.remove(50)  #KeyError: 50
s2.discard(50)  # discard specified element from set object if element not found then no error
s2.discard(20)
print(s2)      #{40,10}