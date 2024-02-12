import sys
input = sys.stdin.readline

# 소수 판별
def check(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# 이분매칭
def bitmatch(now):

    if visited[now]:
        return False
    
    visited[now] = True

    for i in range(n-2):
        if i == now:
            continue
        # 소수라면
        if check(new_data[now] + new_data[i]) and (selected[i] == -1 or bitmatch(selected[i])):
            selected[i] = now
            return True
    return False

n = int(input())
data = list(map(int, input().split()))
result = []

for i in range(1, n):
    # 첫번째 값과 더한 값이 소수라면
    if check(data[0]+data[i]):
        # 이분매칭한다. -> 해당 값들을 빼고
        new_data = data[1:i] + data[i+1:]
        selected = [-1] * (n-2)
        for j in range(0, n-2):
            visited = [False] * (n-2)
            bitmatch(j)
        # print(selected)
        if sorted(selected) == [i for i in range(n-2)]:
            result.append(data[i])

result.sort()
if result:
    print(*result)
else:
    print(-1)