import sys

input = sys.stdin.readline

def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x



n = int(input())

data = [list(input().rstrip()) for _ in range(n)]
print(data)

parent = [i for i in range(n+1)]

print(ord("a") - 96)
print(ord("A") - 38)


'''
연결의 유무 먼저 판단

연결 무 => -1
연결 유 => 최소로 사이클 만들기

'''

