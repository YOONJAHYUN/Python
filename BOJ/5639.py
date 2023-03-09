import sys

# def postorder_traverse(T):
# 	if T:
# 	    postorder_traverse(T.left)
# 	    postorder_traverse(T.right)
# 		visit(T)


# numbers는 전위순회한 값으로 되어있다.
numbers = [0]
while True:
    try:
        number = int(sys.stdin.readline())
        numbers.append(number)

    except:
        break

print(numbers)
N = len(numbers)
# 전위순회한 값을 다시 원래 트리로 만들어주자.
tree = [0]*(N+1)
tree[1] = numbers[1]
idx = 1

left = []
right = []

for i in range(2, N):
    if tree[1] < numbers[i]:
        right.append(numbers[i])
    else:
        left.append(numbers[i])


print(right)
print(left)

'''
[0, 50, 30, 24, 5, 28, 45, 98, 52, 60]
[0, 50, 30, 98, 24, 45, 52, 5, 28, 60]
'''
