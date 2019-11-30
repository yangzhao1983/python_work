f=open('myfile.txt','w')
f.write('Hello file world!')
f.close()

print(open('myfile.txt').read())