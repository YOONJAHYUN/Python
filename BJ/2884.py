H, M = map(int, input().split())

new_H = 0
new_M = 0

if M >= 45:
    new_M = M - 45
    new_H = H
elif M < 45:
    new_M = M + 15
    if H == 0:
        new_H = 23
    else:
        new_H = H - 1

print(new_H, new_M)
