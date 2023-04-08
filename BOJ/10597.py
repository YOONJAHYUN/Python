import sys
input = sys.stdin.readline

# 813371411156121541029

def my_num(idx, n, result, N):
    if idx == n:
        if len(set(result)) == N:
            print(*result)
            exit(0)
        return

    if idx > n:
        return

    num = int(data[idx])

    if num == 0:
        return
    if not v[num]:
        v[num] = 1
        my_num(idx+1, n, result+[num], N)
        v[num] = 0

    if idx < n-1:
        # and int(data[idx]+data[idx+1]) <= N an:
        num2 = int(data[idx]+data[idx+1])
        if num2 <= N and not v[num2]:
            v[num2] = 1

            my_num(idx+2, n, result+[num2], N)
            v[num2] = 0



data = input().rstrip()
# print(data)

# 길이를 통해서 N을 유추하기

n = len(data)
# print(n)
N = 0

if n <= 9:
    N = n
else:
    n = n - 9
    n = n//2

    N = n + 9
    # print(N)
# print(N)
v = [0] * (N+1)
my_num(0, len(data), [], N)
