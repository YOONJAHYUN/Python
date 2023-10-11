import sys
input = sys.stdin.readline

def union(x, y):
    parent[find_set(y)] = find_set(x)


def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x

n, m = map(int, input().split())

parent = list(range(n))

for num in range(1, m+1):
    dot1, dot2 = map(int, input().split())

    ddot1 = find_set(dot1)
    ddot2 = find_set(dot2)

    if ddot1 == ddot2:
        print(num)
        exit(0)
    else:
        if ddot1 > ddot2:
            parent[ddot1] = ddot2
        else:
            parent[ddot2] = ddot1

print(0)

