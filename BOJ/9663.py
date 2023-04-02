import sys
input = sys.stdin.readline

def queen(i, n, data):
    global cnt
    # arr = [[0] * n for _ in range(n)]
    if i == n:
        cnt += 1

        # print(data)
        # idx = 0
        # for j in data:
        #     arr[idx][j] = 1
        #     idx +=1
        #
        # for j in arr:
        #     print(*j)

        return

    for j in range(n):
        # 기본적으로 조합같은 방향으로 간다.
        if not selection1[j]:
            # 이전값에 +- 1위치에 퀸을 놓으면 대각선방향에 놓아지는 거임
            # 따라서 대각선방향에 놓아지지 않은 경우를 조건으로 건다.
            # 데이터가 있는 경우
            if data:

                for k in range(1, i+1):
                    if j == data[-k] + k or j == data[-k] - k:
                        break
                else:
                    selection1[j] = True
                    queen(i+1, n, data+[j])
                    selection1[j] = False

            # data에 아무것도 없는 경우 걍 추가
            elif not data:
                selection1[j] = True
                queen(i + 1, n, data + [j])
                selection1[j] = False

N = int(input())
cnt = 0
selection1 = [False] * N
queen(0, N, [])

print(cnt)
