import os
for (root, sub, files) in os.walk('.'):
    for file in files:
        print('start')
        print('file:' + file)
        print('root:' + root)
        print(sub)
        print('end')