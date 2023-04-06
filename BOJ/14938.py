import sys
input = sys.stdin.readline

'''
5 5 4
5 7 8 2 3
1 4 5
5 2 4
3 2 3
1 2 3


5 8 4
5 7 8 2 3
1 4 5
5 2 4
3 2 3
1 2 3
'''
def max_items(start, path, get,route):
    global visited, num
    # visited = [False] * (n + 1)
    # visited[start] = True
    if path > m:
        return

    if sum(value) == n:
        return

    if path <= m:

        value[start] = 1
        # for r in route:
        #     if value[r]:
        #         value[r] = 0
        #     value[start] = max(value[start], get)

    for i in range(1, n+1):
        # 갈 수 있다?
        if locations[start][i]:
            # 방문을 안했던 곳?
            if not visited[i]:
                visited[i] = True
                max_items(i, path+locations[start][i], get+items[i],route+[i])
                # visited[i] = False
            else:
                max_items(i, path+locations[start][i], get, route+[i])




# n 지역개수 m 수색범위 r 길의 개수
n, m, r = map(int, input().split())

# 아이템의 수
items = [0]+list(map(int, input().split()))

locations = [[0]*(n+1) for _ in range(n+1)]

# 길은 양방향 통행 가능
for _ in range(r):
    a, b, l = map(int, input().split())
    locations[a][b] = l
    locations[b][a] = l


result = 0

for num in range(1, n+1):
    visited = [0] * (n + 1)
    value = [0] * (n+1)
    visited[num] = 1
    max_items(num, 0, 0,[num])
    # print(value)
    ans = 0
    for k in range(n+1):
        if value[k]:
            ans += items[k]
    result = max(result, ans)
print(result)

