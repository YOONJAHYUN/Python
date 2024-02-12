import sys
input = sys.stdin.readline

'''
가장 처음에 양분은 모든 칸에 5만큼 들어있다.

1. 봄
- 나이만큼 양분 먹기 (1*1 한정), 어린 나무부터 양분 먹기
- 나이 += 1
- 양분이 자기 나이만큼 없으면 즉시 죽는다.

2. 여름
- 죽은 나무가 양분으로 변함
- 나이를 2로 나눈 값이 양분으로 추가. 몫만

3. 가을
- 나무 번식 : 나이가 5의 배수일때만, 그리고 인접한 8개의 칸에 나이가 1인 나무가 생김

4. 겨울
- 땅에 양분 추가
- 양분의 양은 A[r][c] 이고 입력으로 주어진다.

k 년이 지난 후 살아있는 나무의 개수 구하기
'''

N, M, K = map(int, input().split())

# 땅
arr = [[[] for _ in range(N)] for _ in range(N)]

food = [[5]*N for _ in range(N)]

# 양분
A = [list(map(int, input().split())) for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    arr[x-1][y-1].append(z)
    # arr[x-1][y-1] = z

# k 년
for _ in range(K):
    # 봄
    for i in range(N):
        for j in range(N):
            # 나무가 있다면
            if arr[i][j]:
                # 나이 어린 순부터
                arr[i][j].sort()
                flag = -1

                for k in range(len(arr[i][j])):
                    year = arr[i][j][k]
                    if flag != -1:
                        break
                    # 양분이 적당히 있다면
                    if food[i][j] - year >= 0:
                        # 양분을 먹이고
                        food[i][j] -= year
                        # 나이를 한살 더 먹는다.
                        arr[i][j][k] += 1
                    # 양분이 없는 경우
                    else:
                        flag = k

                if flag != -1:
                    # 여름 양분됨
                    arr[i][j], temp = arr[i][j][:flag], arr[i][j][flag:]
                    for now in temp:
                        food[i][j] += now//2

    # 가을
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                for k in arr[i][j]:
                    if k % 5 == 0:
                        for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)):
                            ny, nx = dy+i, dx+j
                            if 0 <= nx < N and 0 <= ny < N:
                                arr[ny][nx].append(1)
    # 겨울
    for i in range(N):
        for j in range(N):
            food[i][j] += A[i][j]


# for i in arr:
#     print(i)

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(arr[i][j])

print(ans)

