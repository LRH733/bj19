def set_func(func):
    def call_func(a):
        print("-----call_func-----")
        func(a)
    return call_func

@set_func
def test(num):
    print("------test-----%d" %num)

test(1000)
