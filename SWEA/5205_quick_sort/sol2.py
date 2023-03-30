import sys
sys.stdin = open('input.txt')
def cal(s, e, arr):

    # 피봇을 제일 왼쪽으로 설정
    i = s
    j = e
    pivot = arr[s]
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j-= 1

        if i< j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[s] = arr[s], arr[j]
    return j

def quick_sort(start, end, arr):

    if start < end:
        mid = cal(start, end, arr)
        quick_sort(start, mid-1,arr)
        quick_sort(mid+1, end, arr)


for _ in range(3):
    data = list(map(int, input().split()))

    quick_sort(0, len(data)-1, data)
    print(*data)