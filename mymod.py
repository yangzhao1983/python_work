import sys
"""
reads an input file and counts the number of lines in it
"""
def countLines(name):
    f = open(name,'r')
    print('number of lines in file ' + name + ' is ' + str(len(f.readlines())))

"""
    reads an input file and counts the number of character in it
"""
def countChars(name):
    cnum = 0
    for line in open(name, 'r'):
        cnum += len(line)
    print('char number in file ' + name + ' is :' + str(cnum))

"""
    test(name) function that calls both counting functions with a given input name
"""
def test(name):
    countLines(name)
    countChars(name)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        test(sys.argv[0])
    else:
        test(sys.argv[1])