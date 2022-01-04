#배열 2개를 사용하는 방법

def findMinIdx(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if(ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx

before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

print('정렬 전 -->', before)

for _ in range(len(before)):
    minPos = findMinIdx(before)
    after.append(before[minPos])
    del(before[minPos])
print('정렬 후 -->', after)
