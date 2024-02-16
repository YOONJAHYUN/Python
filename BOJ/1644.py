import sys
input = sys.stdin.readline


n = int(input())
# n보다 작은 소수들
numbers = [True] * (n+1)

for i in range(2, int(n**0.5)+1):
    if numbers[i]:
        for j in range(i*i, n+1, i):
            numbers[j] = False

sosu = []

for i in range(2, n+1):
    if numbers[i]:
        sosu.append(i)

start = 0
end = 0
cnt = 0

while end <= len(sosu):
    my_sum = sum(sosu[start:end])

    if my_sum == n:
        cnt += 1
        end += 1
    elif my_sum < n:
        end += 1
    else:
        start += 1

print(cnt)