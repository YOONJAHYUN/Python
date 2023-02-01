K = int(input())

A = 1
B = 0

for _ in range(K):
    A, B = B, B+A
  
print(A, B)