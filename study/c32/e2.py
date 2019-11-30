"""
1. __getitem__: called by [] and slice
2. X.nonExistAttr will call __getattr__, but X.mul will not call X.__getattr__,
    if __mul__ (operation overloaded method) is not implemented in X. On the other side, methods such as sort() will trigger __getattr__.
3. If there is no __iter__, __getitem__ will be used.
"""

class MyList():
    def __init__(self, start=[]):
        print('init ' + repr(start))
        self.innerList = list(start)

    def __getattr__(self, item):
        print('call get attr')
        return getattr(self.innerList, item)

    def __add__(self, target):
        print('add')
        return MyList(self.innerList + target)

    def __radd__(self, left):
        print('radd')
        return MyList(left + self.innerList)

    # copied from answer
    def __mul__(self, time):
        print('mul')
        return MyList(self.innerList * time)

    # copied form answer
    def __getitem__(self, offset):                # Also passed a slice in 3.X
        print('__getitem__')
        return self.innerList[offset]               # For iteration if no __iter__
    # copied form answer
    def __len__(self):
        print('len')
        return len(self.innerList)

    # copied form answer
    def __getslice__(self, low, high):            # Ignored in 3.X: uses __getitem__
        print('__getslice__')
        return MyList(self.wrapped[low:high])

    # copied form answer
    def append(self, node):
        print('append')
        self.innerList.append(node)

    def __repr__(self):
        print('repr')
        return repr(self.innerList)

# call: init
#X = MyList([1])

# call getattr? ====> No
# print will try to find __str__ and __repr__, if not implemented, __str__ from object will be called
# if no __str__ is implemented, then try to find __repr__.

# call: repr
#print(X)

# call: add --> init[1,1] -->repr
#print(X+[1])

# call: radd --> init[1,1] -->repr
# print([1] + X)

# call: getitem
#print(X[0])

# call: getitem
#print(X[1:])

# call: mul-->init-->repr
# print(X * 3)

#X.append('a')

# call get attr
#X.sort()

#print(dir(X))