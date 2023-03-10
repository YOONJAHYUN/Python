import sys
input = sys.stdin.readline

def make_tree(data):
    global tree

    if len(data) > 1:
        tree.append(data[1])
    else:
        return

    left = [0]
    right = [0]

    for i in range(2, len(data)):
        if data[1] < data[i]:
            right.append(data[i])
        else:
            left.append(data[i])
    if left:
        make_tree(left)
    if right:
        make_tree(right)


# numbers는 전위순회한 값으로 되어있다.
numbers = [0]
while True:
    try:
        number = int(sys.stdin.readline())
        numbers.append(number)

    except:
        break

tree = [0]

print(numbers)
make_tree(numbers)

N = len(numbers)
# 전위순회한 값을 다시 원래 트리로 만들어주자.


print(tree)
# left = []
# right = []
#
# for i in range(2, N):
#     if tree[1] < numbers[i]:
#         right.append(numbers[i])
#     else:
#         left.append(numbers[i])
#
#
# print(right)
# print(left)

'''
[0, 50, 30, 24, 5, 28, 45, 98, 52, 60]
[0, 50, 30, 98, 24, 45, 52, 5, 28, 60]
'''
