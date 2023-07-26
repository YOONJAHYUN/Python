import sys

input = sys.stdin.readline

# hint : 각 자리의 중요도를 표기한다.

n = int(input())
words = []

for _ in range(n):
    words.append(input().rstrip())

alpha = [0] * 26
for word in words:
    length = len(word) - 1
    for char in word:
        alpha[ord(char)-65] += 10**length
        length -= 1
# print(alpha)

new_alpha = []
for i, j in enumerate(alpha):
    if j:
        new_alpha.append((i, j))
new_alpha.sort(key=lambda x:-x[1])
# print(new_alpha)

now = 9
for idx, val in new_alpha:
    alpha[idx] = now
    now -= 1

# print(alpha)

ans = 0
for word in words:
    new = ''
    for char in word:
        new += str(alpha[ord(char)-65])
    ans += int(new)
print(ans)