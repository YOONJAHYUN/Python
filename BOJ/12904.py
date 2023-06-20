import sys

input = sys.stdin.readline

# 시간초과...
# def AB(text):
#     global ans
#     if len(text) == len(t):
#         if text == t:
#             print(1)
#             exit(0)
#         return
#
#     AB(text+'A')
#     AB(text[::-1]+'B')


s = input().rstrip()
t = input().rstrip()

while True:
    if t == s:
        print(1)
        break

    if len(t) == len(s):
        print(0)
        break

    if t[-1] == 'A':
        t = t.removesuffix('A')
    else:
        t = t.removesuffix('B')[::-1]
