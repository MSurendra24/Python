def outerfun():
    print('outer function')
    def innerfun():
        print('inner function')
    innerfun()
# def fun():
#     pass
outerfun()
# innerfun()
# fun()