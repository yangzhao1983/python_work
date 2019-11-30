class A():
    def __str__(self):
        print('in A')
class B(A):
    def __str__(self):
        print('in B')

#print('B.class', B.__mro__)

#print(str(B))

class C():
    def __getattr__(self, name):
        return getattr(self.data,name)

m=C()
m.data = 'abc'

str(m)
m.upper()