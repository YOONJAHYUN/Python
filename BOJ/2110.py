import sys
input = sys.stdin.readline

def binary(lst, start, end):
    
    global ans

    while start <= end:
        mid = (start+end)//2

        current = lst[0]
        count = 1

        for i in range(1, len(lst)):
            if lst[i] >= current + mid:
                count += 1
                current = lst[i]

        if count >= c:
            start = mid + 1
            ans = mid





n, c = map(int, input().split())
ans = 0
home = []
for _ in range(n):
    x = int(input())
    home.append(x)

home.sort()
print(home)
# 인접하다 ->인덱싱
# 두공유기사이의 최대거리 -> 값
binary(home, 0, home[-1]-home[0])

