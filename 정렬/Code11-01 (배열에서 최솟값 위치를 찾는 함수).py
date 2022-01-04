def findMinIdx(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if(ary[minIdx]>ary[i]):
            minIdx = i
    return minIdx

def findMaxIdx(ary):
    maxIdx = 0
    for i in range(1, len(ary)):
        if(ary[maxIdx] < ary[i]):
            maxIdx = i
    return maxIdx

testAry = [55, 88, 33, 77]
minPos = findMinIdx(testAry)
print('최솟값 -->', testAry[minPos])

maxPos = findMaxIdx(testAry)
print('최댓값 -->', testAry[maxPos])
