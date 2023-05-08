import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

def check1(num):

    q = []
    v = [False] * (n+1)
    v[num] = True
    q.append(num)
    while q:
        number = q.pop()

        for i in graph1[number]:
            if not v[i]:
                q.append(i)
                v[i] = True
    return v.count(True) - 1

def check2(num):

    q = []
    v = [False] * (n+1)
    v[num] = True
    q.append(num)
    while q:
        number = q.pop()

        for i in graph2[number]:
            if not v[i]:
                q.append(i)
                v[i] = True
    return v.count(True) - 1

graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]

# res = [0]*(n+1)
for _ in range(m):
    # 앞의 물건이 뒤에보다 더 무겁다.
    big, small = map(int, input().split())
    graph1[small].append(big)
    graph2[big].append(small)

for i in range(1, n+1):
    print(n -check1(i)-check2(i)-1)

