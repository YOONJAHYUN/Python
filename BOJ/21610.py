import sys
input = sys.stdin.readline

def shark(d, s):
    global rain_cloud

    # 비 구름들 이동시키기
    new_cloud = []
    for wi, wj in rain_cloud:
        wi = (wi + dy[d]*s) % N
        wj = (wj + dx[d]*s) % N
        # 구름이 정착하면 비가 1씩 내린다.
        data[wi][wj] += 1
        # 비구름 새로 받아준다.
        new_cloud.append((wi, wj))
    # print(new_cloud)

    # 대각선 방향 확인
    di = [1, -1, -1, 1]
    dj = [1, 1, -1, -1]

    for wi, wj in new_cloud:
        cnt = 0
        for k in range(4):
            ni = wi + di[k]
            nj = wj + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if data[ni][nj]:
                    cnt += 1
        # 대각선 확인 다 한 후 원래자리에  더하기
        data[wi][wj] += cnt

    new_cloud_rain = []
    for i in range(N):
        for j in range(N):
            if data[i][j] >= 2 and (i, j) not in new_cloud:
                new_cloud_rain.append((i, j))
                data[i][j] -= 2

    rain_cloud = new_cloud_rain
    # for i in data:
    #     print(*i)
    # print()


N, M = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

# 방향
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

# 비구름 생기는곳
rain_cloud = [(N-2, 0), (N-1, 0), (N-2, 1), (N-1, 1)]

for _ in range(M):
    d, s = map(int, input().split())
    shark(d-1, s)

result = 0
for i in data:
    result += sum(i)

print(result)
