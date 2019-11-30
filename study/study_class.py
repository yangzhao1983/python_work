class A: pass
class B(A):pass

# type
print(type(A))

# type
print(type(B))

# A
print(B.__base__)

# type
print(B.__class__)

class X: pass
class Y(X): pass

class Z(B,Y): pass

print(Z.mro())