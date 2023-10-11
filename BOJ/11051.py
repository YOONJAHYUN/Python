import sys

input = sys.stdin.readline

n, k = map(int, input().split())

ans = 1

number = n
cnt = 0
while cnt < k:
    ans *= number
    number -= 1
    cnt += 1

number = 1
cnt = 0

while cnt < k:
    cnt += 1
    ans //= cnt


print(ans%10007)