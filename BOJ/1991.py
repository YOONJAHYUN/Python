import sys

input = sys.stdin.readline

def preorder(node):
    if node != '.':
        # 전위 순회기 떄문에
        # 내가 할일 먼저 한다.
        # 지금 문제에서 할일은? 나를 출력
        print(node, end='')
        # 왼쪽 자식을 조사
        preorder(tree[node][0])
        # 오른쪽 자식을 조사
        preorder(tree[node][1])

def inorder(node):
    if node != '.':

        # 왼쪽 자식을 조사
        inorder(tree[node][0])
        # 중위 순회
        print(node, end='')
        # 오른쪽 자식을 조사
        inorder(tree[node][1])

def postorder(node):
    if node != '.':

        # 왼쪽 자식을 조사
        postorder(tree[node][0])
        # 오른쪽 자식을 조사
        postorder(tree[node][1])
        # 후위 순회
        print(node, end='')


N = int(input())
tree = {}

for i in range(1,N+1):
    root, left, right = input().split()
    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
