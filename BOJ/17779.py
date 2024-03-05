import sys
input = sys.stdin.readline

def cal(si, sj, d1, d2):
    v = [[0] * n  for _ in range(n)]
    alst = [0] * 5

    v[si][sj] = 1

    j1 = j2 = sj

    # 마름모 모양을 구현할 때 사용할 수 있는 방법
    # di => 증가되는 칸 수
    for di in range(1, d1+d2+1):
        if di <= d1:
            j1 -= 1
        else:
            j1 += 1

        if di <= d2:
            j2 += 1
        else:
            j2 -= 1

        v[si+di][j1:j2+1] = [1] * (j2-j1+1)

    for i in range(n):
        for j in range(n):
            if v[i][j] == 1:
                alst[4] += arr[i][j]
                continue
            if i < si + d1 and j <= sj:
                alst[0] += arr[i][j]
            elif i<=si+d2 and sj<j:
                alst[1]+=arr[i][j]
            elif si+d1<=i and j<sj-d1+d2:
                alst[2]+=arr[i][j]
            if si+d2<i and sj-d1+d2<=j:
                alst[3]+=arr[i][j]

    return max(alst) - min(alst)



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
tot = sum(map(sum, arr))
ans = n * n * 100

for si in range(n-2):
    for sj in range(1, n-1):
        for d1 in range(1, n):
            if 0 <= si + d1 < n and 0 <= sj - d1 < n:
                for d2 in range(1, n):
                    if 0 <= si+d1+d2 < n and sj+d2 < n:
                        ans = min(ans, cal(si, sj, d1, d2))

print(ans)