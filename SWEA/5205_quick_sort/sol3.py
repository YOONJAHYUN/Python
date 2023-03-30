import sys
sys.stdin = open('input.txt')

def cal(s, e, arr):
    # pivot을 제일 오른쪽에 설치하기

    i = s-1
    j = s

    pivot = arr[e]

    while j < e:
        if arr[j] < pivot:
            i += 1

            if i< j:
                arr[i], arr[j] = arr[j], arr[i]

        j += 1

    arr[i+1], arr[j] = arr[j], arr[i+1]
    return i+1



def quick_sort(start, end, arr):

    if start < end:
        mid = cal(start, end, arr)
        quick_sort(start, mid-1, arr)
        quick_sort(mid+1, end, arr)




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    quick_sort(0, N-1, data)
    print(f'#{tc}', data[N//2])