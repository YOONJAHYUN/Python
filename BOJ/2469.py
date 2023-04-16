import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

'''
시간복잡도 사다리 만들기에 2^k
연산 n*k
최악의 경우 1조 넘어감..실패..ㅠㅠ
'''

def gogo(lst):
    my_data[q_idx] = lst
    my_ans = [0]*k
    for turn in range(k):
        num = turn
        idx = 0

        while True:

            if idx == n:
                my_ans[num] = turn
                if my_ans[num] != result[num]:
                    return
                break

            if 0 <= num < k-1 and my_data[idx][num] == '-':
                num += 1

            elif 0 <= num-1 < k and my_data[idx][num-1] == '-':
                num -= 1
            idx += 1

    if my_ans == result:
        return ''.join(lst)

    else:
        return


def select(depth, n, result):
    global flag

    if depth == n:
        if gogo(result):
            flag = True
            print(gogo(result))
            exit(0)
        return
    # 안건너가기
    select(depth+1, n, result+['*'])
    # 건너기
    if result and result[-1] != '-':
        select(depth+1, n, result+['-'])

    if depth == 0:
        select(depth+1, n, result+['-'])


flag = False
# k 참가한 사람 수
k = int(input())
# n 가로 줄의 수
n = int(input())
# 사다리 결과
res = list(input().rstrip())
result =[]
for char in res:
    result.append(ord(char)-65)
# print(result)
# 사다리
my_data = [list(input().rstrip()) for _ in range(n)]

q_idx = 0
for i in range(n):
    if my_data[i] == ['?'] * (k-1):
        q_idx = i
        break

select(0, k-1, [])

if not flag:
    print('x'*(k-1))