import sys

input = sys.stdin.readline

N, B = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

# B가 홀수인경우, 짝수인경우 나눠서 계산

# B가 짝수인경우는
# data **(B//2) * data ** (B//2)

# B가 홀수인 경우는
# data ** (B//2) ??

# 행렬 곱셈
def mul(data1, data2):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ans = 0
            for k in range(N):
                ans += data1[i][k] * data2[k][j]
            result[i][j] = (ans % 1000)
    return result

# 분할
def square(data, B):
    if B == 1:
        for i in range(len(data)):
            for j in range(len(data)):
                data[i][j] %= 1000

        return  data

    else:

        tmp = square(data, B//2)

        # 홀수라면
        if B % 2:
            return mul(mul(tmp,tmp), data)
        else:
            return mul(tmp, tmp)

answer = square(data,B)

for i in answer:
    print(*i)


