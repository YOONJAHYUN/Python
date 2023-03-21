import sys

input = sys.stdin.readline

# 필요없는 걸 버리는 연습해야겠다..
idx = -1

def Z(n, x, y, dy, dx):
    global idx

    if n == 2:
        if x <= dx+2 and y <= dy+2:
            for i in range(y, y + (2 ** (n - 1))):
                for j in range(x, x + (2 ** (n - 1))):
                    idx += 1

                    if i == dy and j == dx:
                        print(idx)
                        return
        else:
            idx +=4
            return

    else:
        Z(n//2, x, y, dy, dx)

        Z(n//2, x + n//2, y, dy, dx)

        Z(n//2, x, y + n//2, dy, dx)

        Z(n//2, x + n//2, y + n//2, dy, dx)


N, r, c = map(int, input().split())

Z(2**N, 0, 0, r, c)
