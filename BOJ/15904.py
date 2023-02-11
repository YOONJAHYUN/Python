import sys

input = sys.stdin.readline

word = input().rstrip()

UCPC = 'UCPC'

idx = 0
# 단어를 순회하면서 UCPC와 같은 걸 찾는다.
for i in word:
    # 찾아야 idx가 증가한다.
    if i == UCPC[idx]:
        idx += 1
    # 4가지 다 찾으면 idx가 4가 되므로 다 찾은 것이다.
    if idx == 4:
        print('I love UCPC')
        break
# 찾지 못한 경우
else:
    print('I hate UCPC')


