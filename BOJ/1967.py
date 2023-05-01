import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

def check(num):
    q = []
    graph = [1e9 for _ in range(n + 1)]
    graph[num] = 0
    q.append(num)
    my_max = 0
    my_idx = -1
    while q:
        # q의 아이들에게 가
        p = q.pop()

        for i in child[p]:
            power, baby = i

            if graph[baby] > power + graph[p]:
                q.append(baby)
                graph[baby] = power + graph[p]
                if graph[baby] > my_max:
                    my_max = graph[baby]
                    my_idx = baby
    return (my_max, my_idx)


n = int(input())
# 1이 항상 root
child = [[]for _ in range(n+1)]
for _ in range(n-1):
    p, c, power = map(int, input().split())
    child[c].append((power, p))
    child[p].append((power, c))

res, idx = check(1)
print(check(idx)[0])
# print(check(idx)[0]+res)
