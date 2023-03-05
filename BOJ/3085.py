import sys

input = sys.stdin.readline

def bomboni(data):
   global ans

   for i in range(N):
       for j in range(N-1):
           # 인접한 두 사탕의 종류가 같지않다면, 둘을 바꿔준다.
           cnt = 0
           if data[i][j] != data[i][j+1]:
               data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
               # 둘을 바꾸고 바꾼 줄의 candy를 세어본다.
               # 열먼저
               for k in range(N-1):
                   if data[i][k] == data[i][k+1]:
                       cnt += 1
                       if k == N-2:
                           ans = max(ans, cnt+1)
                           cnt = 0
                   else:
                       ans = max(ans, cnt+1)
                       cnt = 0



                # 행도 세어준다.
               for l in range(N-1):
                   if data[l][j] == data[l+1][j]:
                       cnt += 1
                       if l == N-2:
                           ans = max(ans, cnt+1)
                           cnt = 0
                   else:
                       ans = max(ans, cnt+1)
                       cnt = 0

               for l in range(N - 1):
                   if data[l][j+1] == data[l + 1][j+1]:
                       cnt += 1
                       if l == N - 2:
                           ans = max(ans, cnt + 1)
                           cnt = 0
                   else:
                       ans = max(ans, cnt + 1)
                       cnt = 0



                # 다하고 다시 제자리
               data[i][j], data[i][j+1] = data[i][j+1], data[i][j]



N = int(input())
candy = [list(input().rstrip()) for _ in range(N)]
candy_t = list(map(list, zip(*candy)))

ans = 0
# ans초기값 설정.
for i in range(N):
    cnt1 = 0
    cnt2 = 0
    for j in range(N-1):
        if candy[i][j] == candy[i][j+1]:
            cnt1 += 1
            if j == N-2:
                ans = max(cnt1+1, ans)
        else:
            ans = max(cnt1+1, ans)
            cnt1 = 0

        if candy_t[i][j] == candy_t[i][j + 1]:
            cnt2 += 1
            if j == N - 2:
                ans = max(cnt2 + 1, ans)
        else:
            ans = max(cnt2 + 1, ans)
            cnt2 = 0


bomboni(candy)
bomboni(candy_t)
print(ans)

# for i in candy_t:
#     print(i)

