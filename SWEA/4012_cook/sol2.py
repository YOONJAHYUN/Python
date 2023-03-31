import sys
sys.stdin = open('input.txt')

def cook(i, n, group1, group2):
    global selection, result
    # 조합 결성시 return
    if len(group1) == n//2 and len(group2) == n//2:
        ans1 = 0
        ans2 = 0
        for i in range(n//2):
            for j in range(i, n//2):
                ans1 += data[group1[i]][group1[j]] + data[group1[j]][group1[i]]
                ans2 += data[group2[i]][group2[j]]+ data[group2[j]][group2[i]]
        result = min(result, abs(ans1-ans2))
        return

    # 조합 만들기
    # 애초에 group1과 group2를 나눠서 두가지로 만든다.
    if len(group1) < n//2 and len(group2) < n//2:
        cook(i+1, n, group1+[i], group2)
        cook(i+1, n, group1, group2+[i])

    elif len(group1) < n//2:
        cook(i + 1, n, group1 + [i], group2)

    else:
        cook(i + 1, n, group1, group2 + [i])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    selection = [False]*N
    result = 20000 * N**2
    cook(0, N, [], [])

    print(f'#{tc}', result)
