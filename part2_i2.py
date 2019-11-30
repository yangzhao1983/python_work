import os
L = [0,1,2,3];
#print(L[4]);

print(L[-1000:100]);
print(L[-1:1]);
print(L[-1:1:-1]);
print(L[1:-1]);
print(L[1:-1:-1]);
print(L[3:1]);

dirs = os.popen('ls')
for dir_item in dirs: print(dir_item)