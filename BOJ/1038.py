import sys

input = sys.stdin.readline

def decrease_num(depth, idx, num):

    if depth == idx:
        decrease_numbers.append(num)
        return

    for i in range(10):
        if not visited[i]:
            visited[i] = True
            decrease_num(depth+1, idx, num)
            visited[i] = False

N = int(input())

decrease_numbers = []

numbers = list(range(0, 10))
numbers.sort(reverse=True)
print(numbers)
visited = [False] * 10
decrease_num(0, 1, '')
print(decrease_numbers)

