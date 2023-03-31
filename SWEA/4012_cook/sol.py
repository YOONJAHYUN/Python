import sys
sys.stdin = open('input.txt')

def cook(i, n, group1, group2):
    global selection, result
    # 조합 결성시 return
    if i == n:
        ans1 = 0
        ans2 = 0
        print(group1, group2)
        for i in range(1, n//2):
            print(i)
            ans1 += data[group1[i]][group1[i-1]] + data[group1[i-1]][group1[i]]
            ans2 += data[group2[i]][group2[i-1]] + data[group2[i-1]][group2[i]]
        print(ans1, ans2)
        result.append(abs(ans1-ans2))
        return

    # 조합 만들기
    if len(group1) < n//2:
        for j in range(n):
            if not selection[j]:
                selection[j] = True
                cook(i+1, n, group1+[j], group2)
                selection[j] = False

    else:
        for j in range(n):
            if not selection[j]:
                selection[j] = True
                cook(i + 1, n, group1, group2 + [j])
                selection[j] = False




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    selection = [False]*N
    result = []
    # print(selection)
    cook(0, N, [], [])
    print(f'#{tc}', min(result))
    print("##"*100)