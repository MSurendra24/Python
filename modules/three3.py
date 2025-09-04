def user_module():
    print("started user module")
    def login():
        print('login function')
        def logout():
            pass
    return login
inn=user_module()
print(type(inn))
print(inn)
inn()