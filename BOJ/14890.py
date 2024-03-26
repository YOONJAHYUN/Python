import sys
input = sys.stdin.readline

n, l = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = list(map(list, zip(*arr1)))
visited = [[False] * n for _ in range(n)]


def check1(i, j, arr):
    if visited[i][j]:
        return False

    # l만큼 상관없는지 확인
    for k in range(1, l):
        if j + k >= n:
            return False
        if visited[i][j+k]:
            return False

        if arr[i][j + k] != arr[i][j]:
            return False

    for k in range(l):
        visited[i][j+k] = True
        # arr[i][j+k] += 1
    return True

def check2(i, j, arr):
    if visited[i][j]:
        return False
    # l만큼 상관없는지 확인
    for k in range(1, l):
        if j-k < 0:
            return False
        if visited[i][j-k]:
            return False
        if arr[i][j - k] != arr[i][j]:
            return False

    for k in range(l-1):
        visited[i][j-k] = True
    #     arr[i][j-k] += 1
    return True


def solution(arr):
    global answer
    for i in range(n):
        for j in range(1, n):
            # 높이가 전과 같을 경우
            if arr[i][j] == arr[i][j-1]:
                continue
            # 높이 차이가 1인 경우
            if abs(arr[i][j] - arr[i][j-1]) == 1:
                temp = check1(i, j, arr) if arr[i][j] < arr[i][j-1] else check2(i, j-1, arr)
                # 경사로를 못 놓을 경우
                if not temp:
                    break
            else:
                break

        else:
            # print(i, "열")
            answer += 1

answer = 0
solution(arr1)


visited = [[False] * n for _ in range(n)]
solution(arr2)



print(answer)

