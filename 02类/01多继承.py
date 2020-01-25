# 用类名继承
class Parant(object):
    def __init__(self, name):
        self.name =name

    def show_name(self):
        print(self.name)


class Son1(Parant):
    def __init__(self, name):
        Parant.__init__(self)
        self.name = name

print(Son1.__mro__)
