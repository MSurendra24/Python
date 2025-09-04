def user_module(name,status):
    print("started user module")
    def login():
        print('login function')
    def logout():
        print('logout function')
    if status==True:
        return login
    else:
        return logout
inner=user_module('nm',True)
# print(type(inn))
# print(inn)
inner()