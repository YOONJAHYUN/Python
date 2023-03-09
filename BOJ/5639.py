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

for i in range(1, N//2+1):
    # 부모보다 작다면 왼쪽에
    # 부모j
    j = i//2

    while numbers[i] < numbers[j]:
        numbers[j*2]


    # if numbers[i] < tree[j]:
    #     # 아직 없다면
    #     if not tree[j*2]:
    #         tree[j*2] = numbers[i]
    #     # 만약 있다면
    #     else:
    #         if tree[j*2] > numbers[i]:
    #             tree[j*2*2] = numbers[i]
    #         else:
    #             tree[j*2*2+1] = numbers[i]
    #
    # # 부모보다 크다면 오른쪽에
    # else:
    #     if not tree[j * 2+1]:
    #         tree[j * 2+1] = numbers[i]
    #     # 만약 있다면
    #     else:
    #         if tree[j * 2+1] > numbers[i]:
    #             tree[(j * 2+1) * 2] = numbers[i]
    #         else:
    #             tree[j * 2 * 2 + 1] = numbers[i]



print(numbers)

'''
[0, 50, 30, 24, 5, 28, 45, 98, 52, 60]
[0, 50, 30, 98, 24, 45, 52, 5, 28, 60]
'''
