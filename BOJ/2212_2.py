import sys
input = sys.stdin.readline


N = int(input())
K = int(input())

data = list(map(int, input().split()))

data.sort()
# print(data)
sensor = []
for i in range(1, N):
    sensor.append(data[i]-data[i-1])
# print(sensor)
sensor.sort()
# print(sensor)

print(sum(sensor[0:N-K]))
