import math
import timeit
def printObject(o):
    print(o)

#printObject()

printObject(1)

printObject('1')
printObject([1,2])
printObject({'name':'z'})

def adder(left, right):
    return left + right

adder('s1','s2')

adder([1,2],[3,4])

adder(1.1,2.2)

def adderMultiP(*item):
    if item:
        mySum = item[0]
        for x in item[1:]:
            print(x)
            mySum += x
        return mySum
    else:
        print("item=empty")
        return item

print(adderMultiP(1,2,3,4))

def adderKeywords(**kw):
    if kw:
        key1 = list(kw.keys()).pop();
        s = kw.get(key1)
        for key in kw.keys():
            if not key1 == key:
                s += kw.get(key)

        return s
    else:
        return ""

print(adderKeywords(x=1, y=2))

def copyDict(dict):
    newDict = {}
    for key in dict.keys():
        newDict[key] = dict.get(key)
    return newDict

def addDict(dict1, dict2):
    dictAll = {}
    for key in dict1.keys():
        dictAll[key]= dict1.get(key)
    for key in dict2.keys():
        dictAll[key] = dict2.get(key)
    print(dictAll)

dict1 = {'dict1_key1':'dict1_value2'}
dict2 = {'dict2_key1':'dict2_value2'}
addDict(dict1, dict2)

def f1(a,b):
    print(a,b)

def f2(a, *b):
    print(a,b)

def f3(a, **b):
    print(a,b)

def f4(a, *b, **c):
    print(a, b, c)

def f5(a, b=2, c=3):
    print(a,b,c)

def f6(a,b=2,*c):
    print(a,b,c)

f1(1,2)

f1(b=2, a=1)

f2(1,2,3)

f3(1,x=2,y=3)

f4(1,2,3,x=2,y=3)

f5(1)

f5(1,4)

f6(1)

f6(1,3,4)

def getPrime(y):
    target = y
    if type(y) is float:
        target = int(y)
    x = target // 2
    while x>1:
        if target%x == 0:
            print(y, 'has factor', x)
            break
        x -= 1
    else:
        print(y, 'is prime')


getPrime(10.0)

def eratosthenesGetPrime(target):
    # check for target TODO
    # target should >=4
    # target should be integer

    lbound = 2
    ubound = target-1
    targetMap = {}
    for i in range(2,target+1):
        targetMap[i] = True

    # print(targetMap)
    for i in range(2, target):
        targetMap[i] = False
        j = i + i
        while j <= target:
            if targetMap[j]:
                targetMap[j] = False
            j = j + i
        if not targetMap[target]:
            print(target, 'has factor', i)
            break
    else:
        print(target, "is prime")

eratosthenesGetPrime(40)


def myComprehension():
    numList = [2, 4, 9, 16, 25]
    resList = [math.sqrt(x) for x in numList]
    print(resList)

myComprehension()

s =timeit.repeat(stmt='math.sqrt(89)',number=100,setup='import math')
print(s)
