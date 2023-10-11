import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

data = [[[] for _ in range(N)] for _ in range(N)]

# y, x 순서
dir = [
    (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
]

for _ in range(M):
    # r, c 가 위치 m 질량 d 방향 s 속력
    r, c, m, s, d = map(int, input().split())

    r, c = r-1, c-1
    data[r][c].append((m, s, d))

for _ in range(K):
    new_data = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j]:

                while data[i][j]:
                    m, s, d = data[i][j].pop()
                    y, x = i, j
                    y += dir[d][0] * s
                    x += dir[d][1] * s
                    new_data[y % N][x % N].append((m, s, d))

    # 한바퀴 돌고 나서
    for i in range(N):
        for j in range(N):

            if new_data[i][j] and len(new_data[i][j]) >= 2:

                new_m, new_s = 0, 0
                new_d = set()

                for m, s, d in new_data[i][j]:
                    new_m += m
                    new_s += s
                    new_d.add(d % 2)

                new_m //= 5
                new_s //= len(new_data[i][j])

                new_data[i][j] = []
                # 질량이 0이 된 경우 예외처리
                if new_m == 0:
                    continue
                # 다 홀수거나 짝수
                if len(new_d) == 1:
                    for k in range(0, 7, 2):
                        new_data[i][j].append((new_m, new_s, k))
                else:
                    for k in range(1, 8, 2):
                        new_data[i][j].append((new_m, new_s, k))

    data= new_data

answer = 0
for i in range(N):
    for j in range(N):
        if data[i][j]:
          for m, s, d in data[i][j]:
              answer += m
print(answer)



