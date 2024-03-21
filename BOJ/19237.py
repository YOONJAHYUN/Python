import sys

input = sys.stdin.readline

'''
1. 각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 
2. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
2-1. 상어가 
3. 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.

1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지를 구하는 프로그램
'''
# 위, 아래, 왼쪽, 오른쪽
DIR = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

def go(num, d, y, x):
    global count
    ny, nx = y + DIR[d][0], x + DIR[d][1]

    # 범위 내라면
    if 0 <= ny < n and 0 <= nx < n and (arr[ny][nx] == 0 or arr[ny][nx] > num):
        sharks[num] = [d, y, x]

        # 향기
        visited[y][x] = (num, k + 1)
        # 나보다 먼저 온 놈이 있다면
        if arr[ny][nx]:
            # 죽는다.
            # sharks.pop(sharks.index((num, d, y, x)))
            sharks[num] = []
            arr[y][x] = 0
            count -= 1
            return
        # 아니라면 위치 이동 표기
        arr[y][x], arr[ny][nx] = 0, num
        sharks[num] = [d, ny, nx]

    # 범위 내가 아니거나 이미 향기가 있을 경우
    else:
        # 빈 칸 중 갈 수 있는 곳 먼저 선택
        for dir_num in range(4):
            # 우선순위
            new_dir = sharks_dir[num-1][d-1][dir_num]
            new_ny, new_nx = y+DIR[new_dir][0], x+DIR[new_dir][1]
            # 아무도 없는지
            if not arr[new_ny][new_nx]:
                # 아무도 없으면 이동
                go(num, new_dir, y, x)


            go(num, sharks_dir[num - 1][d-1].index(dir_num)+1, y, x)


n, m, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

now_dir = list(map(int, input().split()))
sharks_dir = [[list(map(int, input().split())) for _ in range(4)] for _ in range(m)]

sharks = [[] for _ in range(m+1)]

count = m

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            sharks[arr[i][j]] = [now_dir[arr[i][j] - 1], i, j]

# for i in sharks_dir:
#     print(i)
# print(sharks_dir[0][2])

answer = 0

visited = [[(0, 0) for _ in range(n)] for _ in range(n)]

while count > 1:
    answer += 1

    for i in range(1, m+1):
        if sharks[i]:
            d, y, x = sharks[i]
            go(i, d, y, x)
        # for num, d, y, x in sharks:
        #     go(num, d, y, x)

    # 한 바퀴 다 돌리고 향기 빼기
    for i in range(n):
        for j in range(n):
            now_num, perfume = visited[i][j]
            if now_num != 0:
                if perfume - 1 == 0:
                    now_num = 0
                visited[i][j] = (now_num, perfume-1)


    print(sharks)
    for i in visited:
        print(i)

    print("###############################")

print(answer)

