# 不定参数
def set_fun(fun):
    def call_fun(*args, **kargs):
        print("-----call_fun结果----")
        print(args)
        print(kargs)
        fun(*args, **kargs)
    return call_fun

@set_fun
def test(*args, **kargs):
    print("------test结果-----")
    print(args)
    print(kargs)


test(1, 2, 3, a=5, b=6)


