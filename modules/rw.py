import json
fp1=open('users.json','r')
fp2=open('emp.json','w')
users=json.load(fp1)
print(len(users))
json.dump(users,fp2)
print("data written to emp.json")
fp1.close()
fp2.close()
