import sys
input = sys.stdin.readline

N = int(input())
edge = [[]*(N+1) for _ in range(N+1)]
# data = []
for _ in range(N-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
    # data.append(a)
    # data.append(b)
# print(edge)

q = int(input())

for i in range(q):
    t, k = map(int, input().split())

    # 단절점인지
    if t == 1:
        if len(edge[k]) == 1:
            print("no")
        else:
            print("yes")
    # 단절선 무조건 yes
    else:
        print('yes')