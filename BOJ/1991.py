import sys

input = sys.stdin.readline

N = int(input())
tree = [0 for _ in range(27)]

for i in range(1,N+1):
    root, left, right = input().split()
    print(root, left, right)
    # tree만들기
    if root == 'A':

        tree[i] = root
        if left != '.':
            tree[i*2] = left
        if right != '.':
            tree[i*2+1] = right
    else:
        idx = tree.index(root)
        if left != '.':
            tree[idx*2] = left
        if right != '.':
            tree[idx*2+1] = right

print(tree)

# 전위 순회
for char in tree:
    if char != 0:
        print(char, end='')
print()

# 중위 순회
# 가장 왼쪽 아래 구하기
last_left = 16
while last_left > 1:

    if not tree[last_left]:
        last_left //= 2
    else:
        break
print(last_left)



