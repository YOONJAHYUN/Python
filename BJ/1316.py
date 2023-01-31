import sys

input = sys.stdin.readline

N = int(input())

result = 0

# input을 받고, 글자 하나하나를 그전과 비교한다.
for i in range(N):
    word = input()
    char = []
    for j in range(len(word)):
        if word[j] == word[j-1]:
            continue
        else:
            if word[j] not in char:
                char.append(word[j])
                
            else:
                break

    if '\n' in char:
        result += 1
print(result)