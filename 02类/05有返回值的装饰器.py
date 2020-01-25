def set_fun(fun):
    def call_fun(*args, **kargs):
        print("------call_fun------")
        a = fun(*args, **kargs)
        print("-----返回值：",a)
    return call_fun

@set_fun
def test(*args, **kargs):
    return args, kargs

a = test(1, 3, 4, a=5, b= 6)
print(a)
