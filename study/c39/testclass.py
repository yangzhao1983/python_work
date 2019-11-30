class A: pass
class B (A):
    def __call__(self):
        print('__call__ in B ' + self)
class C(B): pass

print(dir(C))
print(C.__class__)
I = C()
print(dir(I))
print(I.__class__)




