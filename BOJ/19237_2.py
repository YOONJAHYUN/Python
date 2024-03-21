import sys
input = sys.stdin.readline

DIR = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
n, m, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

now_dir = list(map(int, input().split()))
sharks_dir = [[list(map(int, input().split())) for _ in range(4)] for _ in range(m)]

sharks = [[] for _ in range(m+1)]

answer = 0

visited = [[(0, 0) for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            sharks[arr[i][j]] = [now_dir[arr[i][j] - 1], i, j]
            visited[i][j] = (arr[i][j], k)

def check(y, x, d, num):
    # 빈 칸 중 갈 수 있는 곳 먼저 선택
    for dir_num in sharks_dir[num - 1][d - 1]:
        # 우선순위
        new_ny, new_nx = y + DIR[dir_num][0], x + DIR[dir_num][1]

        if 0 <= new_ny < n and 0 <= new_nx < n and visited[new_ny][new_nx] == (0, 0):
            print(num, visited[new_ny][new_nx])
            arr[new_ny][new_nx] = num
            sharks[num] = [dir_num, new_ny, new_nx]
            visited[new_ny][new_nx] = (num, k)
            return True

        elif 0 <= new_ny < n and 0 <= new_nx < n and arr[new_ny][new_nx]:
            sharks[num] = []
            return True

    return False

def check2(y, x, d, num):
    # 빈 칸 중 갈 수 있는 곳 먼저 선택
    for dir_num in sharks_dir[num - 1][d - 1]:
        # 우선순위
        new_ny, new_nx = y + DIR[dir_num][0], x + DIR[dir_num][1]

        if 0 <= new_ny < n and 0 <= new_nx < n and visited[new_ny][new_nx][0] == num:
            print(visited[new_ny][new_nx][0] == num)
            print(num)
            print(visited[new_ny][new_nx][0])

            arr[new_ny][new_nx] = num
            sharks[num] = [dir_num, new_ny, new_nx]
            visited[new_ny][new_nx] = (num, k)
            return True

    return False


for count in range(1, 1001):
    cnt = 0

    for i in range(n):
        for j in range(n):
            now_num, now_count = visited[i][j]
            if now_num:
                if now_count == 0:
                    now_num = 0
                    now_count = 1
                visited[i][j] = (now_num, now_count - 1)

    for num in range(1, m+1):

        if not len(sharks[num]):
            continue


        cnt += 1

        d, y, x = sharks[num]

        if check(y, x, d, num):
            # 이동
              arr[y][x] = 0
        else:
            check2(y, x, d, num)
            arr[y][x] = 0



    print(sharks)
    for i in visited:
        print(i)
    print("####"* 100)

    if cnt == 1:
        print(count)
        break

else:
    print(-1)

