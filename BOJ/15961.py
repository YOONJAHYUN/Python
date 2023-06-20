import sys
input = sys.stdin.readline

# 접시의 수 n 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
n, d, k, c = map(int, input().split())

'''
어떤위치부터 k개까지 다 먹을 경우 할인
+ 초밥 종류 하나 공짜

다양한 종류의 초밥을 먹어야됨

회전형식이니까 k만큼만 뒤에 더 적어준다.
left를 0으로, right를 k로 잡고 lst에다가 하나하나 넣는다.
그리고 초밥 종류를 count

left와 right를 하나씩 옮기면서 count를 빼주고 더해주면서 초밥 종류를 다시 갱신시키고 max값을 설정

이때 쿠폰과 같은 스시가 있는지 없는지 체크하고 max값을 갱신시킴

'''
sushi = [int(input()) for _ in range(n)]
sushi = sushi + sushi[:k+1]

# print(sushi)

left = 0
right = k-1

lst = [0] * (d+1)
cnt = 0
flag = 0

for i in range(k):
    if lst[sushi[i]] == 0:
       cnt += 1
    lst[sushi[i]] += 1
    # 만약 쿠폰과 같은 스시일 경우 flag를 하나 올려준다.
    if sushi[i] == c:
        flag += 1

if flag == 0:
    ans = cnt + 1
else:
    ans = cnt

while right < n+k:
    # print(left, right, ans)

    # left 작업
    # 근데 이게 쿠폰이다
    if sushi[left] == c:
        flag -= 1

    # 하나만 먹었었다.
    if lst[sushi[left]] == 1:
        # cnt 빼기
        cnt -= 1
    # left 빼주기
    lst[sushi[left]] -= 1

    # 다음을 위해 한칸 업그레이드
    left += 1

    # right 작업
    right += 1
    # 근데 이게 쿠폰이다.
    if sushi[right] == c:
        flag += 1

    # 처음 먹는거다.
    if lst[sushi[right]] == 0:
        cnt += 1
    # right 더해주기
    lst[sushi[right]] += 1

    # left right 작업 후 ans 값 정하기
    if flag:
        ans = max(ans, cnt)
    else:
        ans = max(ans, cnt+1)



print(ans)


