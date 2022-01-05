import random

def bubbleSort(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        changeYN = False
        print('#사이클-->',ary)
        for cur in range(0, end):
            if(ary[cur] > ary[cur+1]):
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
                changeYN = True
        if not changeYN:
            break
    return ary

def bubbleDescendingSort(ary):
    n = len(ary)
    global cnt
    for end in range(n-1, 0, -1):
        changeYN = False
        for cur in range(0, end):
            if(ary[cur] < ary[cur+1]):
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
                cnt += 1
                changeYN = True
        if not changeYN:
            break
    return ary


##dataAry = [50, 105, 120, 188, 150, 162, 168, 177]
##print('정렬 전 -->',dataAry)
##dataAry = bubbleSort(dataAry)
##print('정렬 후 -->',dataAry)


##self Study 12-1
cnt = 0

dataAry = []
for i in range(10):
    rn = random.randint(0,200)
    dataAry.append(rn)
    
print('정렬 전 -->',dataAry)
dataAry = bubbleDescendingSort(dataAry)
print('정렬 후 -->',dataAry)
print("## {}회로 정렬 완료".format(cnt))

