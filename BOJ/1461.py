import sys
from heapq import heappop, heappush
input = sys.stdin.readline


# n 책 개수 m 최대 개수
n, m = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
print(data)

'''
양수 음수 중 더 큰 곳을 가장 마지막에 방문
최대개수를 채워 다니기?
'''

now = 0
# 두개 부호가 다르면?
# if data[0]*data[-1] < 0:
#
#     if abs(data[0]) > abs(data[-1]):
#         now = n-1
#
# while True:
#

