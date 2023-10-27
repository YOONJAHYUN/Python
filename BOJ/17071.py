import sys
from collections import deque
input = sys.stdin.readline

def BFS(x):

    q = deque()

    q.append(x)

    while q:




'''
수빈
--
걷기 => 1초후 => x-1, x+1
순간이동 => 1초후 => 2*x
--
동생

k+ 시간

'''
n, k = map(int, input().split())

BFS(n)