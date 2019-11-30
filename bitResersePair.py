'''
get the smallest number which is larger than target
'''
def searchPairs(nums):
    bit = [0] * (len(nums) + 1)
    sortedNums = list(nums)
    sortedNums.sort()
    sumOfNum = 0
    for num in nums[-1::-1]:
        index = binSearch(sortedNums, 0, len(sortedNums)-1, num) + 1
        sumOfNum += query(bit, index)
        largeIndex = binSearch(sortedNums, 0, len(sortedNums)-1, 2*num +1) + 1
        update(bit, largeIndex)
    return sumOfNum

def query(bit, cur):
    sumOfNum = 0
    while cur > 0:
        sumOfNum += bit[cur]
        cur -= cur & (-cur)
    return sumOfNum

def update(bit, cur):
    while cur < len(bit):
        bit[cur] += 1
        cur += cur & (-cur)

def runBinSearch():
    nums = [1,3,5,7,9]
    target = 8
    print(binSearch(nums, 0, len(nums)-1, target));

def binSearch(nums, start, end, target):
    if start > end :
        return start;
    mid = start + (end - start)//2
    if nums[mid] > target:
        return binSearch(nums, start, mid - 1, target)
    elif nums[mid] < target:
        return binSearch(nums, mid +1, end, target)
    else:
        return mid

def testsearchPairs():
    nums = [1,3,2,3,1]
    sum = searchPairs(nums)
    print(sum)

    nums = [2,4,3,5,1]
    sum = searchPairs(nums)
    print(sum)

    nums = [7,4,3,5,1]
    sum = searchPairs(nums)
    print(sum)

    nums = [2147483647,2147483647,2147483647,2147483647,2147483647,2147483647]
    sum = searchPairs(nums)
    print(sum)

testsearchPairs()