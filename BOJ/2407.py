
n, m = map(int, input().split())

ans = 1
for num in range(n, n-m, -1):
    ans *= num
for num in range(1, m+1):
    ans //= num
print(ans)