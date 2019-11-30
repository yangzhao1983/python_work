class Adder:
    def __init__(self, x):
        self.data = x
    def add(self, x, y):
        print('Not implemented')
    def __add__(self, Y):
        return self.add(self.data, Y)
    def __radd__(self, other):
        return self.add(other, self.data)

class ListAdder(Adder):
    def add(self, x, y):
        return x + y

class DictAdder(Adder):
    def add(self, x, y):
        x.update(y)
        return x

listX = [1,2,3]
listY = [4,5,6]

dictX = {'a':1}
dictY = {'b':2}

a = Adder([])
#a.add(listX, listY)

la = ListAdder([])
#la.add(listX, listY)

da = DictAdder({})
#da.add(dictX, dictY)

listX1 = ListAdder([1,2,3])
listX2 = ListAdder([4,5,6])

print(listX1 + listX2)

