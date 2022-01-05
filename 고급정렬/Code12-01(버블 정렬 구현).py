def BubbleSort(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        for cur in range(0, end):
            if(ary[cur] > ary[cur+1]):
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
    return ary

dataAry = [188, 162, 168, 120, 50, 150, 177, 105]

print('정렬 전 -->',dataAry)
dataAry = BubbleSort(dataAry)
print('정렬 후 -->',dataAry)
