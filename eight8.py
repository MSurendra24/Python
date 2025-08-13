eids=[12,34,56,78,90]
print(eids)
print(eids[3])
eids[2]='nm'
print(eids)
print(eids[1:3])
uids=(12,34,56,78,90)
print(uids)
print(uids[3])
print(uids[1:2])
uids[2]='nm'  # This will raise an error since tuples are immutable
print(uids)