def login_page(func):
    print("Login Page")
    def inner(is_in):
        if is_in == False:
            print("Permission not granted")
        else:
            return func(is_in)
    return inner
    login_page(False)
    inner(False)
login_page("true")
login_page("false")
@login_page
def pages(is_in):
    print("You are not logged in")