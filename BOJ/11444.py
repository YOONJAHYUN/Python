import sys

input = sys.stdin.readline

# 행렬 곱셈
def mul(data1, data2):
    n = len(data1)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans = 0
            for k in range(n):
                ans += data1[i][k] * data2[k][j]
            result[i][j] = (ans % 1000000007)
    return result

# 분할
def square(data, B):
    if B == 1:
        for i in range(len(data)):
            for j in range(len(data)):
                data[i][j] %= 1000000007

        return data

    else:

        tmp = square(data, B//2)

        # 홀수라면
        if B % 2:
            return mul(mul(tmp, tmp), data)
        else:
            return mul(tmp, tmp)


'''
n번째 피보나치 수를 1,000,000,007으로 나눈 나머지를 출력

숫자가 크기대문에 행렬을 활용해야한다.
-> O(logN) 까지 줄일 수 있음

n번째 피보나치 수를 구할 때, n/2번째 피보나치 수를 찾아 제곱하면 되고,
n/2번째 수를 구하려면 n/2/2번째 피보나치 수를 제곱하면 된다.
이 때문에 n번째 피보나치 수를 구하기 위한 빅오가 logN이 되는 결과를 가져온다. 
'''
N = int(input())
arr = [[1, 1], [1, 0]]
answer = square(arr, N)[-1][0]

print(answer)