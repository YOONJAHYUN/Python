import sys
input = sys.stdin.readline

# n 덩어리의 개수 m 은혜가 필요한 고기의 양
n, m = map(int, input().split())

# 고기 무게와 가격
data = [tuple(map(int, input().split())) for _ in range(n)]

data.sort(key=lambda x:(x[1], -x[0]))
ans = 0
total_weight = 0
before_cost = 0
i = 0

while i < n:

    weight, cost = data[i]

    # 다음 가격이 더 비싼 경우
    if cost > before_cost:
        if total_weight >= m:
            ans = min(cost, ans)
        else:
            ans = cost

    # 다음 가격이 현재랑 같은 경우
    else:
        if total_weight >= m:
            pass
        else:
            ans += cost

    before_cost = cost
    total_weight += weight
    i += 1

if total_weight >= m:
    print(ans)
else:
    print(-1)


'''
input:
3 2
1 5
1 5
2 6

ans:
6

input:
4 10
3 2
3 2
4 6
4 6
10 5 

ans:
5


5 5000
500 1
1000 2
3000 2
2000 2
500 3
'''