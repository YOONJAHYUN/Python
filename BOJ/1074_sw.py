idx = -1

def Z(n, x, y, dy, dx):
    global idx

    if not(x<= dx < n+x and y<= dy < n + y):
        idx += n**2
        return

    if n == 2:
        for i in range(y, y + (2 ** (n - 1))):
            if i < dy - 2:
                idx += 4
                break

            else:
                for j in range(x, x + (2 ** (n - 1))):
                    if j < (dx-2):
                        idx += 2
                        break
                    else:
                        idx += 1
                        if i == dy and j == dx:
                            print(idx)
        return

    else:
        Z(n//2, x, y, dy, dx)

        Z(n//2, x + n//2, y, dy, dx)

        Z(n//2, x, y + n//2, dy, dx)

        Z(n//2, x + n//2, y + n//2, dy, dx)


N, r, c = map(int, input().split())

Z(2**N, 0, 0, r, c)