class A: pass
class B(A): pass

b = B()

#print('b.__class__', b.__class__, sep='=>\n')

#print('B.__base__', B.__base__, sep='=>\n')

#print('B.__bases__', B.__bases__, sep='=>\n')

#print('B.__class__', B.__class__, sep='=>\n')

print('============')

class SuperMeta(type):
    def __call__(meta, classname, supers,classdict):
        print('In SuperMeta.call:',  classname, supers,classdict, sep='\n...')
        return type.__call__(meta, classname, supers, classdict)
    def __init__(Class, classname, supers, classdict):
        print("In SuperMeta init:", classname, supers, classdict)
        print('...init class object:', list(Class.__dict__.keys()))

print('making metaclass')

class SubMeta(type, metaclass=SuperMeta):
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new: ', classname, supers, classdict, sep='\n...')
        return type.__new__(meta,classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In SubMeta.init: ', classname, supers, classdict, sep='\n...')
        print('... init class object:', list(Class.__dict__.keys()))

class Eggs:
    pass

print("making class")

class Spam(Eggs, metaclass=SubMeta):
    data = 1
    def meth(self, arg):
        return self.data +arg

print("making instance")

X=Spam()

print('data:', X.data, X.meth(2))


class A():
    def __init__(self):
        self.data = 1

class B(A): pass

X = B()
print('X:', X.__dict__)
print('X.data', X.data)

print('Spam MRO :', Spam.__mro__)