def qSort(arr, start, end):
    if end <= start:
        return

    low = start
    high = end

    pivot = arr[(low+high)//2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1

    mid = low

    qSort(arr, start, mid-1)
    qSort(arr, mid, end)

    
def quickSort(ary):
    qSort(ary, 0, len(ary)-1)


dataAry = [188, 150, 168, 162, 105, 120, 177, 50]
    
print('정렬 전 -->',dataAry)
quickSort(dataAry)
print('정렬 후 -->',dataAry)


