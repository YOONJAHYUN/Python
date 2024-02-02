import sys
input = sys.stdin.readline

def binary_search(left, right, target):

    global temp

    while left <= right:

        mid = (left+right) // 2

        if lis[mid] > target:
            right = mid - 1
            temp = mid
        else:
            left = mid + 1


n = int(input())

switches = list(map(int, input().split()))
lights = list(map(int, input().split()))

temp = 0
# lights들의 index가 담겨있는 곳
data = [0] * (n+1)
lis = []
idx = []

for i, v in enumerate(lights, start=1):
    data[v] = i

for switch in switches:
    # 현재 스위치와 연결된 전구의 위치
    now = data[switch]
    if len(lis) == 0 or lis[-1] < now:
        idx.append(len(lis))
        lis.append(now)
    else:
        binary_search(0, len(lis), now)
        lis[temp] = now
        idx.append(temp)


result = []
my_max = max(idx)
for i in idx[::-1]:
    n -= 1
    if i == my_max:
        result.append(switches[n])
        my_max -= 1

print(len(result))
print(*sorted(result))