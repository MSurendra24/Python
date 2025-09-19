def verify(func):
    def inner(name):
        if name == "admin":
            print("Permission granted")
        else:
            return func(name)
    return inner