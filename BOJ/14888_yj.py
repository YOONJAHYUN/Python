# 예진이 코드... 이렇게도 할 수 있다 ㅇ0ㅇ!!!
import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline
"""
덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력
"""


def backtracking(s, num):
    global add, sub, mul, div, max_ans, min_ans, arr

    if s == N:
        max_ans = max(max_ans, num)
        min_ans = min(min_ans, num)
    else:
        if add > 0:
            add -= 1
            backtracking(s + 1, num + arr[s])
            add += 1  # 초기화 해주기
        if sub > 0:
            sub -= 1
            backtracking(s + 1, num - arr[s])
            sub += 1
        if mul > 0:
            mul -= 1
            backtracking(s + 1, num * arr[s])
            mul += 1
        if div > 0:
            div -= 1
            backtracking(s + 1, int(num / arr[s]))  # 나누기는 float으로 반환돼서 int로 묶음
            div += 1


N = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())  # 덧셈 뺄셈 곱셈 나눗셈
min_ans = 1e9
max_ans = -1e9

backtracking(1, arr[0])
print(max_ans)
print(min_ans)