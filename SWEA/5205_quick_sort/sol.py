def mid(s, e, arr):

    mid = (s+e) // 2
    pivot = arr[mid]

    i = s
    j = e
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
            i += 1
    return i


def quicksort(start, end, arr):
    if start < end:
        middle = mid(start, end, arr)
        quicksort(0, middle-1, arr)
        quicksort(middle,end, arr)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    quicksort(0, N-1, data)
    print(f'#{tc}', data)