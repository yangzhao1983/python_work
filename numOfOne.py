'''
calculate the number of "1"s for a integer in binary format
  19: 100011
  output: 3
  -19:11111111 11111111 11111111 111011110
  output: 30
'''
import sys
print(sys.argv[0])
target = -19
print(bin(target))
print(sum([(target >> ++i & 1) for i in range(0,32)]))