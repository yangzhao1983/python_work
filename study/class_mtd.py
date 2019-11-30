class A:
    count = 0
    def __init__(self):
        self.count += self.count + 1

    def printCount(cls):
        print(cls.count)

class B(A): pass

if __name__ == '__main__':
    b = B()
    b.printCount()

    b = A()
    b.printCount()

