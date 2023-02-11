N = int(input())
numbers = list(map(int, input().split()))

# 소수 개수 세기
count = 0

# 5 7 11 15

# numbers에 있는 숫자들을 순회한다.
for num in numbers:
    if num == 1:
        continue

    for i in range(2, num):
        # 나머지가 0이나오면 소수가 아니다.
        if num % i == 0:
            break
    else:
        count += 1
            
print(count)
