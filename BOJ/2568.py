import sys
input = sys.stdin.readline

def binary_search(start, end, target):

    while start <= end:
        mid = (start + end) // 2

        if result[mid] == target:
            return mid

        if result[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start



n = int(input())

lst = [0] * 500001

for _ in range(n):
    a, b = map(int, input().split())
    lst[a] = b

result = []
# lst의 숫자들이 몇 번째 배열에 들어가는 지 작성
record = [-1] * 500001

# 선택하는 것들이 증가하는 형태로 나타 나야함 => 최장증가 부분수열 알고리즘 활용

for i in range(500001):
    num = lst[i]

    if num == 0:
        continue

    # 증가하는 형태가 될 때
    if len(result) == 0 or result[-1] < num:
        result.append(num)
        record[i] = len(result) - 1
    # 증가하는 형태가 되지 않을 때
    else:
        # 어디에 넣을 지 찾는다.
        # temp = 넣을 위치
        temp = binary_search(0, len(result)-1, num)
        result[temp] = num
        record[i] = temp
my_max = max(record)
# print(result)
# print(record[:10])
answer = []
for i in range(500000, -1, -1):
    if record[i] == my_max:
        my_max -= 1
    elif record[i] != -1:
        answer.append(i)

    # if now > my_max:
    #     break

print(len(answer))
for i in answer[::-1]:
    print(i)