size = 6
L = []
for i in range(7):
    L.append(2**i)

print(L)

X=5
target=2**X
if target in L:
    print('at index',L.index(target))
else:
    print(X, 'not found')