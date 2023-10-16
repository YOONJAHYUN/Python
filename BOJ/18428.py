import sys
input = sys.stdin.readline

'''
T = 선생님 S 학생 O 장애물

장애물 3개 설치 => 모든학생 감시 피하기

'''

def put_obstacle(depth, arr):

    if depth == 4:
        return

    if check(arr):
        print("YES")
        exit(0)

    for i in range(n):
        for j in range(n):
            if arr[i][j] == "X":
                arr[i][j] = 'O'
                put_obstacle(depth+1, arr)
                arr[i][j] = 'X'




def check(arr):

    for ty, tx in teacher:

        for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            mul = 1

            while True:
                ny, nx = ty+dy*mul, tx+dx*mul

                if 0 <= ny < n and 0 <= nx < n:
                    # 학생을 만난다면 이건 안되는 경우
                    if arr[ny][nx] == 'S':
                        return False
                    # 장애물이거나 선생님을 만난다면 이 방향은 끝
                    elif arr[ny][nx] == "O" or arr[ny][nx] == 'T':
                        break
                    # "X"라면 다음 방향도 가봐야됨
                    else:
                        mul += 1
                # 범위를 벗어나면 이 방향은 이제 끝임
                else:
                    break

    return True


n = int(input())

teacher = []
arr = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'T':
            teacher.append((i, j))


put_obstacle(0, arr)
print("NO")

